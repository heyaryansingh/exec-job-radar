"""Offline tests for company discovery: name matching and Common Crawl parsing."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT), str(ROOT / "tools")]

import ats_directory  # noqa: E402
import discover as d  # noqa: E402


def wd(host, site):
    return {"ats": "workday", "host": host, "site": site}


def score(name, e, aliases=()):
    return d.match_score(d.name_keys(name, list(aliases)), e)


def test_strong_matches():
    assert score("Capital One", wd("capitalone.wd12.myworkdayjobs.com", "Capital_One")) >= 4
    assert score("Synchrony", wd("synchronyfinancial.wd5.myworkdayjobs.com", "careers")) >= 3
    assert score("Regions Financial", wd("regions.wd5.myworkdayjobs.com", "Regions_Careers")) >= 3
    assert score("M&T Bank", wd("mtb.wd5.myworkdayjobs.com", "MTB")) >= 2           # acronym
    assert score("Fifth Third Bank", wd("fifththird.wd5.myworkdayjobs.com", "53")) >= 3
    assert score("Stripe", {"ats": "greenhouse", "slug": "stripe"}) >= 4


def test_aliases():
    assert score("Fidelity", wd("fmr.wd1.myworkdayjobs.com", "FidelityCareers"), ["fmr"]) >= 4


def test_no_false_matches_on_generic_words():
    # "American" / "First" / "National" alone must not match other companies
    assert score("American Express", wd("americanairlines.wd1.myworkdayjobs.com", "jobs")) < 3
    assert score("First Horizon", wd("firstcitizens.wd1.myworkdayjobs.com", "External")) < 2
    assert score("Cadence Bank", wd("cadence.wd1.myworkdayjobs.com", "External_Careers")) < 3  # review only
    assert score("Morgan Stanley", {"ats": "lever", "slug": "morganlewis"}) < 3  # review at most


def test_best_candidate_wins(monkeypatch):
    entries = [wd("caremark.wd1.myworkdayjobs.com", "jobs_x"),
               dict(wd("cvshealth.wd1.myworkdayjobs.com", "CVS_Health_Careers"), seen=50)]
    monkeypatch.setattr(d, "_DIRECTORY", entries)
    calls = []

    def fake_count(s, e):
        calls.append(e["host"])
        return 10
    monkeypatch.setattr(d, "count_jobs", fake_count)
    e, ok = d.probe_directory(None, "CVS Health", [])
    assert e["host"].startswith("cvshealth") and ok
    assert calls[0].startswith("cvshealth")


def test_cc_line_parsing(monkeypatch):
    lines = "\n".join(json.dumps({"url": u}) for u in [
        "https://regions.wd5.myworkdayjobs.com/en-US/Regions_Careers/job/Birmingham/VP_R1",
        "https://regions.wd5.myworkdayjobs.com/Regions_Careers/job/X/Y_R2",
        "https://regions.wd5.myworkdayjobs.com/wday/cxs/regions/Regions_Careers/jobs",
        "https://regions.wd5.myworkdayjobs.com/robots.txt",
        "https://boards.greenhouse.io/stripe/jobs/123",
        "https://jobs.lever.co/palantir/abc",
    ])

    class R:
        status_code = 200
        text = lines

        def json(self):
            return {"pages": 1}

    monkeypatch.setattr(ats_directory, "_get", lambda s, url, params, tries=5: R())
    got = ats_directory.harvest("api", "*.myworkdayjobs.com", None, 5, lambda *_: None)
    keys = {json.loads(k)["site"] if "site" in json.loads(k) else json.loads(k)["slug"]: n for k, n in got.items()}
    assert keys["Regions_Careers"] == 2
    assert "wday" not in keys and "robots.txt" not in keys
    assert keys["stripe"] == 1 and keys["palantir"] == 1


def test_domain_guesses():
    assert d.guess_domains("Cheniere Energy", [])[0] == "cheniereenergy.com"
    assert "cheniere.com" in d.guess_domains("Cheniere Energy", [])
