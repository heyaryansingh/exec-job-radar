"""Probe large employers' custom career sites to see which readers work for them.

    python tools/probe_custom.py data/test_reports/custom_sites.md

Tries Eightfold, Phenom and sitemap/JSON-LD candidates and reports, for each, whether it
answered and a few senior titles found. Working entries are printed as ready-to-paste
config/companies.yaml lines. Nothing is changed.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import yaml  # noqa: E402

from collector import sources_extra  # noqa: E402
from collector.common import session  # noqa: E402
from collector.filters import Rules  # noqa: E402
from collector.sources import Ctx  # noqa: E402

EIGHTFOLD = [  # (company, host, domain)
    ("Microsoft", "apply.careers.microsoft.com", "microsoft.com"), ("Netflix", "explore.jobs.netflix.net", "netflix.com"),
    ("American Express", "aexp.eightfold.ai", "aexp.com"), ("Qualcomm", "careers.qualcomm.com", "qualcomm.com"),
    ("PayPal", "paypal.eightfold.ai", "paypal.com"), ("Micron", "careers.micron.com", "micron.com"),
    ("Bayer", "bayer.eightfold.ai", "bayer.com"), ("Starbucks", "starbucks.eightfold.ai", "starbucks.com"),
    ("Cisco", "cisco.eightfold.ai", "cisco.com"), ("Vertex Pharmaceuticals", "vrtx.eightfold.ai", "vrtx.com"),
    ("Morgan Stanley", "morganstanley.eightfold.ai", "morganstanley.com"), ("Dexcom", "dexcom.eightfold.ai", "dexcom.com"),
    ("Chevron", "chevron.eightfold.ai", "chevron.com"), ("AMD", "careers.amd.com", "amd.com"),
]
PHENOM = [  # (company, host)
    ("HPE", "careers.hpe.com"), ("Thermo Fisher Scientific", "jobs.thermofisher.com"), ("AbbVie", "careers.abbvie.com"),
    ("CVS Health", "jobs.cvshealth.com"), ("Mastercard", "careers.mastercard.com"), ("Kroger", "jobs.kroger.com"),
    ("Boeing", "jobs.boeing.com"), ("Accenture", "www.accenture.com"), ("Johnson & Johnson", "www.careers.jnj.com"),
    ("Lowe's", "talent.lowes.com"), ("Intel", "jobs.intel.com"), ("Siemens", "jobs.siemens.com"),
    ("Booz Allen Hamilton", "careers.boozallen.com"), ("Bristol Myers Squibb", "careers.bms.com"),
    ("Caterpillar", "careers.caterpillar.com"), ("Walgreens", "jobs.walgreens.com"),
]
SITEMAP = [  # (company, host)
    ("Apple", "jobs.apple.com"), ("Goldman Sachs", "higher.gs.com"), ("Lockheed Martin", "www.lockheedmartinjobs.com"),
    ("UnitedHealth Group", "careers.unitedhealthgroup.com"), ("ExxonMobil", "jobs.exxonmobil.com"),
    ("IBM", "www.ibm.com"), ("Google", "www.google.com"), ("Oracle", "careers.oracle.com"),
    ("Home Depot", "careers.homedepot.com"), ("Walmart", "careers.walmart.com"), ("Deloitte", "apply.deloitte.com"),
    ("EY", "careers.ey.com"), ("PwC", "jobs.us.pwc.com"), ("Citi", "jobs.citi.com"), ("Bank of America", "careers.bankofamerica.com"),
    ("AT&T", "www.att.jobs"), ("Verizon", "mycareer.verizon.com"), ("Dell Technologies", "jobs.dell.com"),
    ("Tesla", "www.tesla.com"), ("Meta", "www.metacareers.com"), ("ConocoPhillips", "careers.conocophillips.com"),
    ("Halliburton", "careers.halliburton.com"), ("Kinder Morgan", "kindermorgan.jobs"),
]


def main():
    out = Path(sys.argv[1])
    rules = Rules(yaml.safe_load((ROOT / "config" / "search.yaml").read_text()))
    ctx = Ctx(title_ok=rules.title_ok, known=set(), level_queries=["Vice President", "Director"], max_age_days=30)
    lines = ["# Custom career-site probe", ""]
    good = []

    def run(kind, company, entry, fn):
        s = session()
        try:
            got = fn({"name": company, **entry}, s, ctx)
            titles = [p.title for p in got if rules.title_ok(p.title)][:4]
            lines.append(f"| {kind} | {company} | ok, {len(got)} senior | {'; '.join(titles)[:150]} |")
            if got:
                good.append({"name": company, "ats": kind, **entry, "tier": 1})
        except Exception as e:
            lines.append(f"| {kind} | {company} | fail | {str(e)[:120]} |")

    lines += ["| Reader | Company | Result | Sample titles |", "|---|---|---|---|"]
    for company, host, domain in EIGHTFOLD:
        run("eightfold", company, {"host": host, "domain": domain}, sources_extra.eightfold)
    for company, host in PHENOM:
        run("phenom", company, {"host": host, "locale": "us/en"}, sources_extra.phenom)
    s = session()
    for company, host in SITEMAP:
        maps = []
        try:
            r = s.get(f"https://{host}/robots.txt", timeout=15)
            if r.ok:
                maps = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", r.text)
        except Exception:
            pass
        maps = maps or [f"https://{host}/sitemap.xml"]
        done = False
        for m in maps[:4]:
            try:
                got = sources_extra.sitemap({"name": company, "sitemap": m, "max_new": 8}, session(), ctx)
                lines.append(f"| sitemap | {company} | ok via {m}, {len(got)} pages read | "
                             f"{'; '.join(p.title for p in got[:3])[:150]} |")
                if got:
                    good.append({"name": company, "ats": "sitemap", "sitemap": m, "tier": 1})
                done = True
                break
            except Exception as e:
                last = str(e)[:80]
        if not done:
            lines.append(f"| sitemap | {company} | fail | {last if maps else 'no sitemap'} ({len(maps)} sitemaps listed) |")
    lines += ["", "## Ready-to-paste entries", "", "```yaml"]
    lines += ["- " + json.dumps(g) for g in good]
    lines += ["```"]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out}: {len(good)} working")


if __name__ == "__main__":
    main()
