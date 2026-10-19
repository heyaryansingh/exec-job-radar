"""Experiment: how does Workday answer for real vs made-up company sites?

    python tools/probe_workday.py report.md

Used by the test workflow to learn which signals tell a real Workday tenant/site apart
from a made-up one, before building direct Workday probing into discovery.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from collector.common import session  # noqa: E402

KNOWN = [  # (tenant, wd, site) known to exist, from the working watchlist
    ("capitalone", "wd12", "Capital_One"),
    ("nvidia", "wd5", "NVIDIAExternalCareerSite"),
    ("pfizer", "wd1", "PfizerCareers"),
]
GUESS_TENANTS = ["walmart", "dell", "qualcomm", "redhat", "thermofisher", "zzqqxxfake"]
WDS = ["wd1", "wd3", "wd5", "wd12", "wd103", "wd501"]
SITES = ["External", "Careers", "careers", "jobs", "External_Careers"]


def main():
    out = Path(sys.argv[1])
    s = session()
    lines = ["# Workday probe experiment", "", "## 1. Root URL behaviour", "",
             "| Host | GET / status | final URL |", "|---|---|---|"]
    hosts = [f"{t}.{w}.myworkdayjobs.com" for t, w, _ in KNOWN] + \
            [f"{t}.{w}.myworkdayjobs.com" for t in GUESS_TENANTS for w in WDS]
    for h in hosts:
        try:
            r = s.get(f"https://{h}/", timeout=15, allow_redirects=True, headers={"Accept": "text/html"})
            lines.append(f"| {h} | {r.status_code} | {r.url[:90]} |")
        except Exception as e:
            lines.append(f"| {h} | ERR | {str(e)[:80]} |")
    lines += ["", "## 2. Jobs API with right and wrong site names", "",
              "| Host | Site | POST status | total |", "|---|---|---|---|"]
    tries = [(f"{t}.{w}.myworkdayjobs.com", t, site) for t, w, site in KNOWN]
    tries += [(f"{t}.{w}.myworkdayjobs.com", t, "WrongSiteName") for t, w, _ in KNOWN]
    tries += [(f"{t}.{w}.myworkdayjobs.com", t, site) for t in GUESS_TENANTS[:5] for w in ("wd1", "wd5") for site in SITES]
    for host, tenant, site in tries:
        try:
            r = s.post(f"https://{host}/wday/cxs/{tenant}/{site}/jobs",
                       json={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": ""}, timeout=15)
            total = r.json().get("total") if r.ok else ""
            lines.append(f"| {host} | {site} | {r.status_code} | {total} |")
        except Exception as e:
            lines.append(f"| {host} | {site} | ERR | {str(e)[:60]} |")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
