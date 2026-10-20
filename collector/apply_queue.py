"""The apply queue: the best newly posted roles, shaped for fast, high-volume applying.

data/apply_queue.json  read by the daily Claude run (PLAYBOOK.md): newest strong roles,
                       each tagged with how its application works, plus the application
                       questions when the career site publishes them (Greenhouse), so
                       answers can be drafted before the form is even opened.
data/apply_queue.md    the same as a readable checklist.
"""
from __future__ import annotations

from .store import age_days, since

QUICK = {"greenhouse", "lever", "ashby", "smartrecruiters"}          # one-page forms, no account
ACCOUNT = {"workday", "oracle", "eightfold", "amazon", "phenom"}     # sign-in / account first


def apply_via(r: dict) -> str:
    src = r.get("source", "")
    if src in QUICK:
        return "quick form"
    if src in ACCOUNT:
        return "account"
    if src.startswith("board-") or src in ("adzuna", "jsearch", "themuse", "himalayas", "remotive"):
        return "via job board"
    if src == "usajobs":
        return "usajobs account"
    return "employer site"


def build(open_roles: list[dict], limit: int = 300, max_age_days: int = 5, focus=None) -> list[dict]:
    fresh = [r for r in open_roles if since(r.get("first_seen", ""), 72) and
             (not r.get("posted_at") or age_days(r) <= max_age_days)]
    order = {"quick form": 0, "employer site": 1, "account": 1, "usajobs account": 2, "via job board": 2}
    fresh.sort(key=lambda r: (-(r.get("score") or 0), order.get(apply_via(r), 3), r.get("first_seen", "")))
    out = []
    for r in fresh[:limit]:
        out.append({
            "uid": r["uid"], "company": r["company"], "title": r["title"], "url": r["url"],
            "also_at": r.get("also_at", []), "location": r.get("location", ""), "remote": r.get("remote", False),
            "pay_min": r.get("pay_min"), "pay_max": r.get("pay_max"), "posted_at": r.get("posted_at"),
            "first_seen": r.get("first_seen"), "score": r.get("score"), "tier": r.get("tier"),
            "apply_via": apply_via(r), "questions": (r.get("extra") or {}).get("questions", []),
            "description": (r.get("description") or "")[:3000], "source": r.get("source"),
            "area": focus(r.get("location") or "") if focus else "",
        })
    return out


def markdown(q: list[dict]) -> str:
    lines = ["# Apply queue", "",
             "Best roles posted in the last few days, strongest first. ⚡ = one-page form, no account "
             "needed (fastest to apply). The daily Claude run works through this list.", "",
             "| # | Score | Company | Role | Location | Pay | How | Questions |",
             "|---:|---:|---|---|---|---|---|---:|"]
    areas = sorted({r.get("area") for r in q if r.get("area")})
    for i, r in enumerate(q, 1):
        how = "⚡ quick form" if r["apply_via"] == "quick form" else r["apply_via"]
        pay = f"${r['pay_max']:,}" if r.get("pay_max") else ""
        title = str(r["title"]).replace("|", "/")
        lines.append(f"| {i} | {r.get('score', '')} | {str(r['company']).replace('|', '/')} | [{title}]({r['url']}) | "
                     f"{str(r.get('location', '')).replace('|', '/')[:40]} | {pay} | {how} | {len(r['questions']) or ''} |")
    for a in areas:
        rs = [r for r in q if r.get("area") == a]
        lines += ["", f"## {a} area ({len(rs)})", "", "| Score | Company | Role | Pay | How |", "|---:|---|---|---|---|"]
        lines += [f"| {r.get('score', '')} | {str(r['company']).replace('|', '/')} | [{str(r['title']).replace('|', '/')}]({r['url']}) | "
                  f"{('$' + format(r['pay_max'], ',')) if r.get('pay_max') else ''} | "
                  f"{'⚡ quick form' if r['apply_via'] == 'quick form' else r['apply_via']} |" for r in rs]
    return "\n".join(lines) + "\n"
