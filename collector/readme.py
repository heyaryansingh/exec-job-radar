"""Render README.md (the public role list) and the daily digests from the role database."""
from __future__ import annotations

import re
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
    TZ = ZoneInfo("America/New_York")
except Exception:  # pragma: no cover
    TZ = timezone(timedelta(hours=-5))

from .store import age_days, since

# (section, emoji, title pattern). First match wins, so order matters.
CATEGORIES = [
    ("Executive Technology Leadership", "👑", r"\b(chief|cto|cio|cdo|ciso|evp|executive vice president)\b"),
    ("Security & Risk Technology", "🛡️", r"\b(security|cyber|ciso|identity|risk technology|resilience)\b"),
    ("Data & AI", "🧠", r"\b(data|ai|artificial intelligence|machine learning|ml|analytics|genai|llm)\b"),
    ("Reliability & Operations", "🚦", r"\b(sre|site reliability|reliability|production|operations|incident|observability|support)\b"),
    ("Cloud & Infrastructure", "☁️", r"\b(cloud|infrastructure|platform|platforms|data center|network|hosting|devops|compute|storage)\b"),
    ("Architecture", "🏛️", r"\b(architect|architecture)\b"),
    ("Transformation & Delivery", "🔄", r"\b(transformation|modernization|program|portfolio|delivery|digital|strategy|pmo|tpm)\b"),
    ("Engineering & Software", "🛠️", r"\b(engineering|software|development|applications?|technology|technical|it)\b"),
]
OTHER = ("Other Senior Roles", "📌")
LEVELS = [
    ("C-level", r"\b(chief|cto|cio|cdo|ciso)\b"),
    ("EVP/SVP", r"\b(evp|svp|executive vice president|senior vice president)\b"),
    ("MD", r"\bmanaging director\b"),
    ("ED", r"\bexecutive director\b"),
    ("VP", r"\b(vp|vice president)\b"),
    ("Head", r"\bhead of\b"),
    ("Sr. Director", r"\b(senior|sr\.?) director\b"),
    ("Director", r"\bdirector\b"),
]
MAX_PER_SECTION = 400


def category(title: str):
    t = title.lower()
    for name, emoji, pat in CATEGORIES:
        if re.search(pat, t):
            return name, emoji
    return OTHER


def level(title: str) -> str:
    t = title.lower()
    for name, pat in LEVELS:
        if re.search(pat, t):
            return name
    return ""


def esc(s) -> str:
    return str(s or "").replace("|", "/").replace("\n", " ").strip()


def money(n) -> str:
    if not n:
        return ""
    return f"${n / 1000:,.0f}K" if n < 1_000_000 else f"${n / 1_000_000:.2f}M"


def pay(r) -> str:
    hi, lo = r.get("pay_max"), r.get("pay_min")
    if hi and lo and lo != hi:
        return f"{money(lo)}–{money(hi)}"
    return money(hi)


def place(r) -> str:
    loc = esc(r.get("location"))
    parts = [p.strip() for p in re.split(r";", loc) if p.strip()]
    text = parts[0][:42] if parts else ("Remote" if r.get("remote") else "")
    if len(parts) > 1:
        text += f" +{len(parts) - 1}"
    if r.get("remote") and "remote" not in text.lower():
        text += " · Remote"
    return text


def row(r, twins=None) -> str:
    badges = ""
    if r.get("status") == "open" and since(r.get("first_seen", ""), 24):
        badges += "🆕 "
    if r.get("reposted"):
        badges += "🔁 "
    if r.get("status") == "closed":
        badges += "🔒 "
    title = esc(r["title"])
    if twins and twins.get(r.get("dup_key"), 0) > 1:
        # several separate openings with the same title here: show each requisition id
        title += f" (req {esc(r.get('job_id'))[:24]})"
    elif r.get("opening_no"):
        title += f" (opening #{r['opening_no']})"
    company = esc(r["company"]) + (" ⭐" if r.get("tier") == 1 else "")
    apply = f"[Apply]({r['url']})" if r.get("status") == "open" else "Closed"
    extra = "".join(f" [alt]({u})" for u in (r.get("also_at") or [])[:1])
    age = age_days(r)
    return (f"| {company} | {badges}{title} | {level(r['title'])} | {place(r)} | {pay(r)} | "
            f"{age}d | {apply}{extra} |")


HEAD = "| Company | Role | Level | Location | Pay | Age | Apply |\n|---|---|---|---|---|---:|---|"


def anchor(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def heading(text: str, emoji: str = "") -> str:
    # explicit anchor: GitHub's automatic ids for emoji headings are unreliable
    return f'<a name="{anchor(text)}"></a>\n\n## {emoji + " " if emoji else ""}{text}'.replace("\n\n## ", "\n## ", 0)


def render(roles: list[dict], header: str, companies_watched: int, digest_links: list[str]) -> str:
    open_roles = [r for r in roles if r["status"] == "open"]
    open_roles.sort(key=lambda r: r.get("first_seen", ""), reverse=True)
    recent_closed = sorted((r for r in roles if r["status"] == "closed" and since(r.get("closed_at", ""), 24 * 14)),
                           key=lambda r: r.get("closed_at", ""), reverse=True)
    new24 = [r for r in open_roles if since(r.get("first_seen", ""), 24)]
    twins = Counter(r.get("dup_key") for r in open_roles)
    by_cat: dict = {}
    for r in open_roles:
        by_cat.setdefault(category(r["title"]), []).append(r)
    order = [(n, e) for n, e, _ in CATEGORIES] + [OTHER]
    n_companies = len({r["company"] for r in open_roles})
    updated = datetime.now(TZ).strftime("%b %d, %Y %I:%M %p ET")
    levels = Counter(level(r["title"]) for r in open_roles)

    out = [header.strip(), "",
           f"**{len(open_roles):,} open roles** at **{n_companies:,} companies** · "
           f"**{len(new24):,} new in the last 24 hours** · {companies_watched:,} company career sites "
           f"watched · updated hourly · last update {updated}", "",
           "By level: " + " · ".join(f"{k} {v}" for k, v in levels.most_common() if k), "",
           "🆕 found in the last 24h · 🔁 reposted after closing · 🔒 closed · ⭐ top-tier employer · "
           "Age = days since posted (or first seen). Every link goes to the employer's own posting.", "",
           "## Contents", "",
           f"- [🆕 New in the last 24 hours ({len(new24)})](#{anchor('New in the last 24 hours')})"]
    for name, emoji in order:
        if by_cat.get((name, emoji)):
            out.append(f"- [{emoji} {name} ({len(by_cat[(name, emoji)])})](#{anchor(name)})")
    out.append(f"- [🔒 Recently closed ({len(recent_closed)})](#{anchor('Recently closed')})")
    if digest_links:
        out.append("- Daily digests: " + " · ".join(digest_links))
    out.append("")

    out += [heading("New in the last 24 hours", "🆕"), ""]
    out += [HEAD] + [row(r, twins) for r in new24[:300]] if new24 else ["Nothing new yet today."]
    out.append("")
    for name, emoji in order:
        rs = by_cat.get((name, emoji)) or []
        if not rs:
            continue
        out += [heading(name, emoji), "", HEAD] + [row(r, twins) for r in rs[:MAX_PER_SECTION]]
        if len(rs) > MAX_PER_SECTION:
            out.append(f"\n_{len(rs) - MAX_PER_SECTION} older roles in this section are in data/roles.json._")
        out.append("")
    out += [heading("Recently closed", "🔒"), "", "<details><summary>Roles that closed in the last 14 days</summary>", "", HEAD]
    out += [row(r) for r in recent_closed[:300]]
    out += ["", "</details>", ""]
    return "\n".join(out) + "\n"


def digest(roles: list[dict], day_local: str) -> str:
    rows = [r for r in roles if r["status"] == "open" and _local_day(r.get("first_seen", "")) == day_local]
    rows.sort(key=lambda r: (-(r.get("score") or 0), r.get("company", "")))
    lines = [f"# New senior technology roles · {day_local}", "",
             f"{len(rows)} roles first found on this day, best quick-score first.", "", HEAD]
    lines += [row(r) for r in rows]
    return "\n".join(lines) + "\n"


def _local_day(iso: str) -> str:
    try:
        return datetime.fromisoformat(iso).astimezone(TZ).date().isoformat()
    except Exception:
        return ""


def today_local() -> str:
    return datetime.now(TZ).date().isoformat()


def write_all(root: Path, roles: list[dict], companies_watched: int, write):
    header_file = root / "config" / "readme_header.md"
    header = header_file.read_text() if header_file.exists() else "# Exec Job Radar"
    ddir = root / "data" / "daily"
    ddir.mkdir(parents=True, exist_ok=True)
    day = today_local()
    write(ddir / f"{day}.md", digest(roles, day))
    days = sorted((p.stem for p in ddir.glob("*.md")), reverse=True)
    for old in days[45:]:  # keep about six weeks of digests
        (ddir / f"{old}.md").unlink(missing_ok=True)
    links = [f"[{d[5:]}](data/daily/{d}.md)" for d in days[:7]]
    write(root / "README.md", render(roles, header, companies_watched, links))
