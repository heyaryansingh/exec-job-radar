"""Add a company to config/companies.yaml from any job-posting or careers URL.

    python tools/add_company.py "<url>" "Company Name" [tier] [sector]

Recognizes Workday, Greenhouse, Lever, Ashby, SmartRecruiters and Oracle Cloud
career sites. Prints the entry it added, or explains what it could not parse.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from collector.atsurl import parse  # noqa: E402,F401  (re-exported for tools/discover.py)
COMPANIES = ROOT / "config" / "companies.yaml"


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    url, name = sys.argv[1], sys.argv[2]
    tier = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    sector = sys.argv[4] if len(sys.argv) > 4 else ""
    try:
        entry = parse(url)
    except ValueError as e:
        print(e)
        sys.exit(2)
    text = COMPANIES.read_text() if COMPANIES.exists() else ""
    if re.search(rf"name:\s*{re.escape(name)}\s*,", text):
        print(f"{name} is already in companies.yaml")
        sys.exit(0)
    fields = [f"name: {name}"] + [f"{k}: {v!r}" if k == "site" else f"{k}: {v}" for k, v in entry.items()]
    fields += [f"tier: {tier}"] + ([f"sector: {sector}"] if sector else [])
    line = "- {" + ", ".join(fields) + "}"
    with open(COMPANIES, "a") as fh:
        fh.write(("\n" if text and not text.endswith("\n") else "") + line + "\n")
    print("Added:", line)


if __name__ == "__main__":
    main()
