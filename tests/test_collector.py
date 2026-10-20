"""Offline tests: each adapter is fed responses shaped like the real APIs."""
from datetime import date, timedelta
from pathlib import Path

import yaml

from collector import sources
from collector.common import parse_pay, html_to_text
from collector.filters import Rules
from collector.sources import Ctx

ROOT = Path(__file__).resolve().parent.parent
CFG = yaml.safe_load((ROOT / "config" / "search.yaml").read_text())
RULES = Rules(CFG)
TODAY = date.today().isoformat()


def ctx():
    return Ctx(title_ok=RULES.title_ok, known=set(), level_queries=["Vice President"], max_age_days=21)


def fake(routes):
    def get_json(s, url, **kw):
        for key, val in routes.items():
            if key in url:
                return val(kw) if callable(val) else val
        raise RuntimeError("no route " + url)
    return get_json


DESC = ("<p>Lead our cloud infrastructure and platform engineering org. AWS, Azure, Kubernetes, "
        "SRE, observability, incident management, data center modernization.</p>"
        "<p>Pay range: $245,000 - $330,000 per year.</p>")


def test_pay_parse():
    assert parse_pay("The range is $245,000 - $330,000.")[:2] == (245000, 330000)
    assert parse_pay("$180K–$220K base")[:2] == (180000, 220000)
    assert parse_pay("$85.00 - $110.00 per hour")[1] == 228800
    assert parse_pay("we manage $5 billion to $9 billion")[:2] == (None, None)


def test_title_rules():
    ok = RULES.title_ok
    assert ok("Vice President, Cloud Infrastructure")
    assert ok("Head of Site Reliability Engineering")
    assert ok("Executive Director - Technology Transformation")
    assert ok("Chief Technology Officer")
    assert not ok("Assistant Vice President, Cloud")
    assert not ok("Associate Director, Data")
    assert not ok("VP, Enterprise Sales")
    assert not ok("Director of Nursing")
    assert not ok("Senior Software Engineer")
    assert not ok("Executive Assistant to the CTO")


def test_greenhouse(monkeypatch):
    monkeypatch.setattr(sources, "get_json", fake({"greenhouse": {"jobs": [
        {"id": 1, "title": "VP, Platform Engineering", "absolute_url": "https://x/1",
         "location": {"name": "Remote - US"}, "updated_at": TODAY + "T10:00:00Z",
         "content": DESC.replace("<", "&lt;").replace(">", "&gt;")},
        {"id": 2, "title": "Software Engineer", "absolute_url": "https://x/2",
         "location": {"name": "NYC"}, "content": ""},
    ]}}))
    out = sources.greenhouse({"name": "Acme", "slug": "acme", "tier": 1}, None, ctx())
    assert len(out) == 1
    p = out[0]
    assert p.pay_max == 330000 and p.remote and "Kubernetes" in p.description
    ok, why, score = RULES.evaluate(p)
    assert ok, why
    assert score >= 60


def test_lever(monkeypatch):
    monkeypatch.setattr(sources, "get_json", fake({"lever": [
        {"id": "abc", "text": "Head of Infrastructure", "hostedUrl": "https://jobs.lever.co/a/abc",
         "categories": {"location": "Houston, TX"}, "createdAt": 1_700_000_000_000,
         "descriptionPlain": "Cloud, AWS, SRE, observability, Kubernetes", "lists": [],
         "salaryRange": {"min": 250000, "max": 310000, "interval": "per-year-salary"}}]}))
    p = sources.lever({"name": "A", "slug": "a"}, None, ctx())[0]
    assert p.pay_max == 310000 and p.location == "Houston, TX"


def test_ashby(monkeypatch):
    monkeypatch.setattr(sources, "get_json", fake({"ashbyhq": {"jobs": [
        {"id": "z", "title": "Director, AI Platform", "jobUrl": "https://jobs.ashbyhq.com/a/z",
         "location": "San Francisco", "isRemote": False, "publishedAt": TODAY,
         "descriptionPlain": "Build our LLM and agentic AI platform on AWS and Kubernetes.",
         "compensation": {"compensationTierSummary": "$260K – $300K",
                          "summaryComponents": [{"compensationType": "Salary", "minValue": 260000,
                                                 "maxValue": 300000}]}}]}}))
    p = sources.ashby({"name": "A", "slug": "a"}, None, ctx())[0]
    assert p.pay_max == 300000
    assert RULES.evaluate(p)[0]


def test_workday(monkeypatch):
    listing = {"total": 3, "jobPostings": [
        {"title": "Vice President, Cloud Engineering", "externalPath": "/job/Plano-TX/VP-Cloud_R1",
         "locationsText": "Plano, TX", "postedOn": "Posted Today", "bulletFields": ["R1"]},
        {"title": "Vice President, Commercial Sales", "externalPath": "/job/X/VP-Sales_R2",
         "locationsText": "Plano, TX", "postedOn": "Posted 2 Days Ago", "bulletFields": ["R2"]},
        {"title": "Vice President, Data Platforms", "externalPath": "/job/X/VP-Data_R3",
         "locationsText": "Bengaluru, India", "postedOn": "Posted Yesterday", "bulletFields": ["R3"]},
    ]}
    detail = {"jobPostingInfo": {"jobDescription": DESC, "location": None,
                                 "startDate": TODAY, "externalUrl": "https://cap.wd12/x"}}
    monkeypatch.setattr(sources, "get_json", fake({"/jobs": listing, "/job/": detail}))
    out = sources.workday({"name": "Cap", "host": "cap.wd12.myworkdayjobs.com", "site": "Ext", "tier": 1},
                          None, ctx())
    titles = [p.title for p in out]
    assert "Vice President, Commercial Sales" not in titles
    results = {p.title: RULES.evaluate(p) for p in out}
    assert results["Vice President, Cloud Engineering"][0]
    assert not results["Vice President, Data Platforms"][0]   # India location dropped


def test_oracle(monkeypatch):
    old = (date.today() - timedelta(days=60)).isoformat()
    monkeypatch.setattr(sources, "get_json", fake({
        "recruitingCEJobRequisitions": {"items": [{"requisitionList": [
            {"Id": "210001", "Title": "Executive Director - Cloud Infrastructure",
             "PostedDate": TODAY, "PrimaryLocation": "Houston, TX, United States"},
            {"Id": "210002", "Title": "Executive Director - Platform", "PostedDate": old,
             "PrimaryLocation": "New York, NY"}]}]},
        "recruitingCEJobRequisitionDetails": {"items": [{"ExternalDescriptionStr": DESC}]},
    }))
    out = sources.oracle({"name": "JPMC", "host": "jpmc.fa.oraclecloud.com", "site": "CX_1001"}, None, ctx())
    assert [p.job_id for p in out] == ["210001"]
    assert "CandidateExperience" in out[0].url


def test_low_pay_dropped():
    from collector.common import Posting
    p = Posting(source="x", company="C", job_id="1", title="Director, Cloud Engineering", url="u",
                location="Remote", description="cloud AWS Kubernetes SRE observability",
                pay_min=150000, pay_max=180000)
    ok, why, _ = RULES.evaluate(p)
    assert not ok and why.startswith("pay")


def test_add_company_parse():
    import importlib.util
    spec = importlib.util.spec_from_file_location("ac", ROOT / "tools" / "add_company.py")
    ac = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ac)
    assert ac.parse("https://capitalone.wd12.myworkdayjobs.com/en-US/Capital_One/job/McLean-VA/VP_R1")[
        "site"] == "Capital_One"
    assert ac.parse("https://job-boards.greenhouse.io/stripe/jobs/123")["slug"] == "stripe"
    assert ac.parse("https://jobs.lever.co/palantir/abc")["ats"] == "lever"
    assert ac.parse("https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/2100")[
        "site"] == "CX_1001"
    wf = ac.parse("https://wd1.myworkdaysite.com/en-US/recruiting/wf/WellsFargoJobs/job/x")
    assert wf["tenant"] == "wf" and wf["site"] == "WellsFargoJobs"


def test_html_to_text():
    assert html_to_text("<ul><li>A</li><li>B</li></ul>").splitlines() == ["- A", "- B"]


def test_workday_falls_back_when_search_rejected(monkeypatch):
    listing = {"jobPostings": [{"title": "Vice President, Cloud Engineering", "externalPath": "/job/A/VP_R9",
                                "locationsText": "Dallas, TX", "postedOn": "Posted Today", "bulletFields": ["R9"]}]}

    def get_json(s, url, method="GET", body=None, **kw):
        if url.endswith("/jobs"):
            if body["searchText"]:
                raise RuntimeError("422 Client Error: Unprocessable Entity")
            return listing
        return {"jobPostingInfo": {"jobDescription": DESC}}

    class S:
        headers = {}
    monkeypatch.setattr(sources, "get_json", get_json)
    out = sources.workday({"name": "W", "host": "w.wd5.myworkdayjobs.com", "site": "Ext"}, S(), ctx())
    assert [p.job_id for p in out] == ["R9"]


def test_workday_raises_when_site_is_dead(monkeypatch):
    def get_json(*a, **kw):
        raise RuntimeError("404 Not Found")

    class S:
        headers = {}
    monkeypatch.setattr(sources, "get_json", get_json)
    import pytest
    with pytest.raises(RuntimeError):
        sources.workday({"name": "W", "host": "w.wd5.myworkdayjobs.com", "site": "Ext"}, S(), ctx())


def test_location_rules():
    from collector.common import Posting
    def ok(loc):
        p = Posting(source="x", company="C", job_id=loc, title="VP, Cloud Infrastructure", url="u",
                    location=loc, description="cloud AWS Kubernetes SRE observability incident")
        return RULES.evaluate(p)[0]
    assert ok("Houston, TX") and ok("Ontario, CA") and ok("Manchester, NH") and ok("Remote - US")
    assert ok("New York; London") and ok("Charlotte, North Carolina, United States")
    assert not ok("Seoul, South Korea") and not ok("Sofia, Bulgaria") and not ok("London, UK")


def test_houston_roles_get_a_looser_domain_filter():
    from collector.common import Posting
    desc = "Lead enterprise infrastructure and data center operations for our refining business."
    def p(loc):
        return Posting(source="x", company="C", job_id=loc, title="Director, Operations Excellence", url="u",
                       location=loc, description=desc)
    assert RULES.focus_of("Katy, TX") == "Houston" and RULES.focus_of("Austin, TX") == ""
    assert RULES.evaluate(p("Houston, TX"))[0]          # 2 domain hits are enough in Houston
    assert not RULES.evaluate(p("Chicago, IL"))[0]      # elsewhere it needs 4
