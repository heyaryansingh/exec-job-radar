"""Write an ordered record of every application from tracker.json.

    python tools/app_index.py "<Job Search folder>"

Writes, inside the Job Search folder:
  applications/INDEX.md          every role, grouped by status, newest first, with links to
                                 the posting, resume, cover letter, review and proof
  applications/applications.csv  the same as a spreadsheet (one row per role), for sorting
                                 and filtering in Excel / Google Sheets
Application folders stay where they are (applications/<YYYY-MM-DD>_<Company>_<Role>/),
named so they sort by date.

The playbook runs this at the end of every run, right after the dashboard.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ORDER = [("submitted", "Submitted"), ("interviewing", "Interviewing"), ("offer", "Offers"),
         ("human_check", "Needs one click"), ("filled", "Filled, waiting for Submit"),
         ("needs_review", "Held for a decision"), ("needs_account", "Needs an account"),
         ("needs_input", "Needs an answer"), ("prepared", "Materials ready"),
         ("rejected", "Rejected"), ("duplicate", "Duplicates caught"), ("closed", "Posting closed"),
         ("skipped", "Passed on")]
COLUMNS = ["status", "status_at", "submitted_at", "company", "title", "location", "pay", "score",
           "source", "url", "folder", "resume", "cover_letter", "review", "proof"]


def files_in(folder: Path, root: Path) -> dict:
    def find(*pats):
        for pat in pats:
            hit = sorted(folder.glob(pat))
            if hit:
                return str(hit[0].relative_to(root))
        return ""
    if not folder.is_dir():
        return {"resume": "", "cover_letter": "", "review": "", "proof": ""}
    return {"resume": find("*_Resume.pdf", "resume.pdf", "*_Resume.docx"),
            "cover_letter": find("*_Cover_Letter.pdf", "cover_letter.pdf", "*_Cover_Letter.docx"),
            "review": find("review.md"),
            "proof": find("proof*.png", "proof*.pdf", "confirmation*")}


def rows(tracker: dict, root: Path) -> list[dict]:
    out = []
    for key, r in (tracker.get("roles") or {}).items():
        folder = r.get("folder") or ""
        f = files_in(root / folder, root) if folder else {"resume": "", "cover_letter": "", "review": "", "proof": ""}
        proof = r.get("proof") or {}
        out.append({
            "status": r.get("status", ""), "status_at": (r.get("status_at") or "")[:16],
            "submitted_at": (r.get("submitted_at") or (proof.get("page") or {}).get("at") or "")[:16],
            "company": r.get("company", ""), "title": r.get("title", ""), "location": r.get("location", ""),
            "pay": r.get("pay_text") or (f"up to ${r['pay_max']:,}" if r.get("pay_max") else ""),
            "score": r.get("claude_score", ""), "source": r.get("source_label") or r.get("source", ""),
            "url": r.get("apply_url") or r.get("url", ""), "folder": folder,
            **f, "proof": f["proof"] or (proof.get("email") or {}).get("subject", ""),
        })
    return out


def write(root: Path) -> tuple[Path, Path]:
    tracker = json.loads((root / "tracker.json").read_text()) if (root / "tracker.json").exists() else {}
    apps = root / "applications"
    apps.mkdir(exist_ok=True)
    data = rows(tracker, root)
    rank = {k: i for i, (k, _) in enumerate(ORDER)}
    data.sort(key=lambda d: (rank.get(d["status"], 99), d["submitted_at"] or d["status_at"]), reverse=False)
    csv_path = apps / "applications.csv"
    with csv_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(sorted(data, key=lambda d: d["submitted_at"] or d["status_at"], reverse=True))

    def rel(p: str) -> str:   # links from applications/INDEX.md
        return "../" + p.replace(" ", "%20") if p else ""

    md = [f"# Applications: {tracker.get('candidate', '')}", "",
          f"{sum(1 for d in data if d['status'] in ('submitted', 'interviewing', 'offer'))} submitted, "
          f"{sum(1 for d in data if d['status'] == 'interviewing')} interviewing, {len(data)} roles tracked. "
          "Spreadsheet: [applications.csv](applications.csv).", ""]
    for key, head in ORDER:
        group = sorted((d for d in data if d["status"] == key),
                       key=lambda d: d["submitted_at"] or d["status_at"], reverse=True)
        if not group:
            continue
        md += [f"## {head} ({len(group)})", "", "| Date | Company | Role | Location | Score | Files |", "|---|---|---|---|---|---|"]
        for d in group:
            links = [f"[posting]({d['url']})" if d["url"] else ""]
            for label, k in (("resume", "resume"), ("letter", "cover_letter"), ("review", "review")):
                if d[k]:
                    links.append(f"[{label}]({rel(d[k])})")
            if d["proof"]:
                links.append(f"[proof]({rel(d['proof'])})" if "/" in d["proof"] else f"proof: {d['proof'][:40]}")
            date = (d["submitted_at"] or d["status_at"])[:10]
            md.append(f"| {date} | {d['company']} | {d['title']} | {d['location']} | {d['score']} | "
                      f"{' · '.join(x for x in links if x)} |")
        md.append("")
    idx = apps / "INDEX.md"
    idx.write_text("\n".join(md))
    return idx, csv_path


def main(argv=None) -> int:
    a = list(argv if argv is not None else sys.argv[1:])
    if not a:
        print(__doc__); return 2
    idx, c = write(Path(a[0]))
    print(f"wrote {idx} and {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
