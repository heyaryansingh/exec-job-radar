"""Render tracker.json into a single self-contained dashboard.html.

    python tools/render_dashboard.py <path/to/tracker.json> [<out.html>]

The Claude run calls this at the end of every run and saves the page next to the
tracker in the candidate's Job Search folder. Links to application materials are
relative, so they open straight from that folder.
"""
from __future__ import annotations

import html
import json
import sys
from datetime import datetime
from pathlib import Path

SECTIONS = [
    ("human_check", "Needs one click from you now",
     "A CAPTCHA or emailed code stopped the run. The tab is open and filled: finish the check and click Submit."),
    ("interviewing", "Interviewing", ""),
    ("offer", "Offers", ""),
    ("filled", "Ready for you to review and submit",
     "Filled in your browser and waiting on the Submit click. Check flagged fields first."),
    ("needs_review", "Held for your decision",
     "Filled, but something needs your judgment first (an agreement, a consent, or an unconfirmed submit)."),
    ("needs_account", "Needs a quick account sign-up",
     "This site needs an account Claude can't create. Sign up once, then the next run fills it."),
    ("needs_input", "Needs your answer",
     "A question only you can answer. Reply in the Claude chat or edit candidate.yaml."),
    ("prepared", "Materials ready (not filled yet)",
     "Tailored resume and cover letter are ready; the form will be filled on the next run."),
    ("submitted", "Submitted", "Each has proof: the confirmation page or email."),
    ("rejected", "Closed out", ""),
    ("duplicate", "Duplicates caught", "Already applied; not submitted again."),
    ("closed", "Posting closed", ""),
    ("skipped", "Reviewed and passed on", "Below the bar this time. Tell Claude if any of these deserve a second look."),
]

CSS = """
:root{--bg:#f7f6f2;--card:#fff;--ink:#1d1d1b;--muted:#6b6a64;--line:#e4e2db;--accent:#1f5f8b;
--good:#2d7a4b;--warn:#a46a00;--chip:#efeee8}
@media (prefers-color-scheme:dark){:root{--bg:#151514;--card:#1e1e1c;--ink:#ecebe6;--muted:#a3a29b;
--line:#33322e;--accent:#7db7e0;--good:#7cc79a;--warn:#e0b25c;--chip:#2a2a27}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:1000px;margin:0 auto;padding:28px 16px 64px}
h1{font-size:26px;margin:0 0 4px}.sub{color:var(--muted);margin:0 0 22px}
.stats{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:28px}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;min-width:120px}
.stat b{display:block;font-size:22px}.stat span{color:var(--muted);font-size:13px}
h2{font-size:17px;margin:30px 0 2px}.hint{color:var(--muted);font-size:13px;margin:0 0 10px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:10px 0}
.top{display:flex;justify-content:space-between;gap:12px;align-items:baseline;flex-wrap:wrap}
.title{font-weight:600;font-size:16px}.title a{color:var(--ink);text-decoration:none}
.title a:hover{text-decoration:underline}.co{color:var(--muted)}
.score{font-weight:700;color:var(--good);white-space:nowrap}
.meta{color:var(--muted);font-size:13px;margin:4px 0 8px}
.chip{display:inline-block;background:var(--chip);border-radius:20px;padding:1px 9px;font-size:12px;margin-right:6px}
.why{margin:6px 0}.attn{color:var(--warn);font-size:14px;margin:6px 0 0;padding-left:18px}
.links a{color:var(--accent);margin-right:14px;font-size:14px}
details>summary{cursor:pointer;color:var(--muted);margin:24px 0 6px}
.row{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid var(--line);padding:6px 0;font-size:14px}
.row a{color:var(--ink)}
"""


def esc(x) -> str:
    return html.escape(str(x or ""))


def card(r: dict) -> str:
    pay = r.get("pay_text") or (f"up to ${r['pay_max']:,}" if r.get("pay_max") else "pay not posted")
    chips = "".join(f'<span class="chip">{esc(c)}</span>' for c in
                    [r.get("sector"), r.get("source_label"), f"posted {r['posted_at']}" if r.get("posted_at") else ""] if c)
    attn = "".join(f"<li>{esc(a)}</li>" for a in r.get("attention") or [])
    folder = r.get("folder")
    links = [f'<a href="{esc(r.get("apply_url") or r.get("url"))}" target="_blank">Open application</a>']
    if r.get("url") and r.get("apply_url") and r["url"] != r["apply_url"]:
        links.append(f'<a href="{esc(r["url"])}" target="_blank">Job posting</a>')
    if folder:
        for label, fn in (("Resume", "resume.pdf"), ("Cover letter", "cover_letter.pdf"), ("Answers", "answers.md")):
            links.append(f'<a href="{esc(folder)}/{fn}">{label}</a>')
    proof = (r.get("proof") or {})
    proof_html = ""
    if proof.get("page") or proof.get("email"):
        ptxt = (proof.get("page") or {}).get("text") or (proof.get("email") or {}).get("subject") or ""
        proof_html = f'<div class="meta">Proof: {esc(ptxt)[:140]}</div>'
    contacts = r.get("contacts") or []
    contact_html = ""
    if contacts:
        contact_html = '<div class="meta">Who to reach: ' + "; ".join(esc(c) for c in contacts) + "</div>"
    return f"""<div class="card"><div class="top"><div class="title">
<a href="{esc(r.get('url'))}" target="_blank">{esc(r.get('title'))}</a> <span class="co">· {esc(r.get('company'))}</span></div>
<div class="score">{esc(r.get('claude_score', ''))}</div></div>
<div class="meta">{esc(r.get('location'))} · {esc(pay)}</div><div>{chips}</div>
<div class="why">{esc(r.get('reason'))}</div>{contact_html}{proof_html}
{f'<ul class="attn">{attn}</ul>' if attn else ''}
<div class="links">{''.join(links)}</div></div>"""


def render(tracker: dict) -> str:
    roles = list((tracker.get("roles") or {}).values())
    by = {}
    for r in roles:
        by.setdefault(r.get("status", "prepared"), []).append(r)
    for v in by.values():
        v.sort(key=lambda r: (-(r.get("claude_score") or 0), r.get("status_at", "")))
    runs = tracker.get("runs") or []
    last = runs[-1] if runs else {}
    week_ago = datetime.now().timestamp() - 7 * 86400

    def recent(r):
        try:
            return datetime.fromisoformat(r.get("status_at", "")[:19]).timestamp() >= week_ago
        except ValueError:
            return False

    stats = [
        (len(by.get("human_check", [])), "need a click now"),
        (len(by.get("filled", [])), "ready to submit"),
        (len(by.get("needs_account", [])) + len(by.get("needs_input", [])), "need you"),
        (sum(1 for r in by.get("submitted", []) if recent(r)), "submitted this week"),
        (len(by.get("submitted", [])) + len(by.get("interviewing", [])) + len(by.get("offer", [])), "submitted total"),
        (len(by.get("interviewing", [])), "interviewing"),
    ]
    out = [f"<!doctype html><html lang=en><head><meta charset=utf-8>"
           f"<meta name=viewport content='width=device-width,initial-scale=1'>"
           f"<title>Job Search Dashboard</title><style>{CSS}</style></head><body><main>",
           f"<h1>{esc(tracker.get('candidate', 'Job search'))}</h1>",
           f"<p class=sub>Last run {esc(last.get('at', 'not yet'))}. {esc(last.get('summary', ''))}</p>",
           '<div class="stats">' + "".join(f'<div class="stat"><b>{n}</b><span>{esc(l)}</span></div>' for n, l in stats) + "</div>"]
    for key, head, hint in SECTIONS:
        items = by.get(key, [])
        if not items:
            continue
        if key in ("skipped", "closed", "rejected", "duplicate"):
            rows = "".join(f'<div class="row"><a href="{esc(r.get("url"))}" target=_blank>{esc(r.get("title"))} · '
                           f'{esc(r.get("company"))}</a><span>{esc(r.get("claude_score", ""))} {esc(r.get("reason", ""))[:90]}</span></div>'
                           for r in items[:150])
            out.append(f"<details><summary>{esc(head)} ({len(items)})</summary>"
                       f"<p class=hint>{esc(hint)}</p>{rows}</details>")
        else:
            out.append(f"<h2>{esc(head)} ({len(items)})</h2><p class=hint>{esc(hint)}</p>")
            out.extend(card(r) for r in items)
    out.append("</main></body></html>")
    return "\n".join(out)


def main():
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_name("dashboard.html")
    tracker = json.loads(src.read_text()) if src.exists() else {"roles": {}}
    dst.write_text(render(tracker))
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
