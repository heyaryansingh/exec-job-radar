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
COMPANIES = ROOT / "config" / "companies.yaml"


def parse(url: str) -> dict:
    u = urlparse(url.strip())
    host = u.netloc.lower()
    parts = [p for p in u.path.split("/") if p]
    if parts and re.fullmatch(r"[a-z]{2}-[A-Z]{2}", parts[0]):
        parts = parts[1:]  # drop locale like en-US

    if host.endswith("myworkdayjobs.com") and parts:
        return {"ats": "workday", "host": host, "site": parts[0]}
    if host.endswith("myworkdaysite.com") and len(parts) >= 3 and parts[0] == "recruiting":
        tenant, site = parts[1], parts[2]
        return {"ats": "workday", "host": host, "tenant": tenant, "site": site,
                "public_base": f"https://{host}/en-US/recruiting/{tenant}/{site}"}
    if "greenhouse.io" in host and parts:
        slug = parts[0] if parts[0] not in ("embed", "v1") else None
        if not slug:
            m = re.search(r"for=([\w-]+)", u.query)
            slug = m.group(1) if m else None
        if slug:
            return {"ats": "greenhouse", "slug": slug}
    if host == "jobs.lever.co" and parts:
        return {"ats": "lever", "slug": parts[0]}
    if host == "jobs.ashbyhq.com" and parts:
        return {"ats": "ashby", "slug": parts[0]}
    if "smartrecruiters.com" in host and parts:
        return {"ats": "smartrecruiters", "slug": parts[0]}
    if "oraclecloud.com" in host and "sites" in parts:
        return {"ats": "oracle", "host": host, "site": parts[parts.index("sites") + 1]}
    raise ValueError(
        "Could not recognize this career site. Open one specific job posting and copy the "
        "address from the browser bar; if the company uses its own custom site (e.g. "
        "Goldman Sachs, Amazon, Google), it can't be added here, but the job-board sweep "
        "and the Claude run's career-site checks still cover it.")


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
