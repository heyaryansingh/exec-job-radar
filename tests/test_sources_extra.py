"""Offline tests for the extra career-site readers, aggregators and the apply queue."""
import json
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

from collector import aggregators, apply_queue, sources, sources_extra
from collector.filters import Rules
from collector.sources import Ctx

ROOT = Path(__file__).resolve().parent.parent
RULES = Rules(yaml.safe_load((ROOT / "config" / "search.yaml").read_text()))
TODAY = date.today().isoformat()
DESC = "<p>Lead cloud infrastructure: AWS, Azure, Kubernetes, SRE, observability, incident management.</p>"


def ctx():
    return Ctx(title_ok=RULES.title_ok, known=set(), level_queries=["Vice President"], max_age_days=21)


def fake(routes):
    def get_json(s, url, **kw):
        for key, val in routes.items():
            if key in url:
                return val(url, kw) if callable(val) else val
        raise RuntimeError("no route " + url)
    return get_json


def test_eightfold(monkeypatch):
    now = int(datetime.now(timezone.utc).timestamp())
    monkeypatch.setattr(sources_extra, "get_json", fake({
        "/api/apply/v2/jobs/": {"job_description": DESC},
        "/api/apply/v2/jobs": {"positions": [
            {"id": 7, "name": "Vice President, Cloud Infrastructure", "locations": ["Redmond, WA"], "t_create": now},
            {"id": 8, "name": "Software Engineer II", "locations": ["Redmond, WA"], "t_create": now}]}}))
    out = sources_extra.eightfold({"name": "Microsoft", "host": "apply.careers.microsoft.com",
                                   "domain": "microsoft.com"}, None, ctx())
    assert [p.job_id for p in out] == ["7"] and "Kubernetes" in out[0].description
    assert RULES.evaluate(out[0])[0]


def test_phenom(monkeypatch):
    monkeypatch.setattr(sources_extra, "get_json", fake({"/widgets": {"refineSearch": {"data": {"jobs": [
        {"jobSeqNo": "HPE1US1217311EXTERNALENUS", "title": "VP, Hybrid Cloud Platform Engineering",
         "cityStateCountry": "Houston, Texas, United States", "postedDate": TODAY + "T00:00:00",
         "descriptionTeaser": "Lead cloud platform engineering and SRE for HPE GreenLake."}]}}}}))
    out = sources_extra.phenom({"name": "HPE", "host": "careers.hpe.com", "locale": "us/en", "refnum": "HPE1US"},
                               None, ctx())
    assert out[0].url == "https://careers.hpe.com/us/en/job/HPE1US1217311EXTERNALENUS"
    assert RULES.evaluate(out[0])[0]


def test_amazon(monkeypatch):
    posted = datetime.now().strftime("%B %d, %Y")
    monkeypatch.setattr(sources_extra, "get_json", fake({"amazon.jobs": {"jobs": [
        {"id_icims": "301", "title": "Director, AWS Infrastructure Engineering", "job_path": "/en/jobs/301/x",
         "normalized_location": "Seattle, Washington, USA", "posted_date": posted, "description": DESC}]}}))
    out = sources_extra.amazon({"name": "Amazon"}, None, ctx())
    assert out[0].url == "https://www.amazon.jobs/en/jobs/301/x" and out[0].posted_at == date.today().isoformat()


class R:
    def __init__(self, text, ok=True):
        self.text, self.content, self.ok, self.status_code = text, text.encode(), ok, 200 if ok else 404

    def raise_for_status(self):
        pass


def test_sitemap_jsonld():
    ld = {"@context": "https://schema.org", "@type": "JobPosting", "title": "Vice President, Enterprise Architecture",
          "datePosted": TODAY, "description": DESC,
          "jobLocation": {"@type": "Place", "address": {"addressLocality": "Houston", "addressRegion": "TX",
                                                         "addressCountry": "US"}},
          "baseSalary": {"@type": "MonetaryAmount", "value": {"minValue": 250000, "maxValue": 320000, "unitText": "YEAR"}}}
    pages = {
        "https://x.com/sitemap.xml": '<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'<url><loc>https://x.com/jobs/vice-president-enterprise-architecture-123</loc><lastmod>{TODAY}</lastmod></url>'
        f'<url><loc>https://x.com/jobs/warehouse-associate-124</loc><lastmod>{TODAY}</lastmod></url>'
        '<url><loc>https://x.com/about</loc></url></urlset>',
        "https://x.com/jobs/vice-president-enterprise-architecture-123":
            f'<html><script type="application/ld+json">{json.dumps(ld)}</script></html>'}
    fetched = []

    class S:
        def get(self, url, **kw):
            fetched.append(url)
            return R(pages.get(url, ""), url in pages)
    out = sources_extra.sitemap({"name": "X Corp", "sitemap": "https://x.com/sitemap.xml"}, S(), ctx())
    assert len(out) == 1 and out[0].pay_max == 320000 and out[0].location == "Houston, TX, US"
    assert "https://x.com/jobs/warehouse-associate-124" not in fetched   # skipped by URL, never fetched
    assert RULES.evaluate(out[0])[0]


def test_greenhouse_questions(monkeypatch):
    monkeypatch.setattr(sources, "get_json", fake({
        "/jobs/9": {"content": DESC, "questions": [
            {"label": "First Name", "required": True, "fields": [{"name": "first_name", "type": "input_text"}]},
            {"label": "Are you authorized to work in the US?", "required": True,
             "fields": [{"name": "question_1", "type": "multi_value_single_select",
                         "values": [{"label": "Yes", "value": 1}, {"label": "No", "value": 0}]}]}]},
        "/boards/acme/jobs": {"jobs": [{"id": 9, "title": "VP, Platform Engineering", "absolute_url": "https://a/9",
                                        "location": {"name": "Remote - US"}}]}}))
    out = sources.greenhouse({"name": "Acme", "slug": "acme"}, None, ctx())
    qs = out[0].extra["questions"]
    assert len(qs) == 1 and qs[0]["options"] == ["Yes", "No"] and qs[0]["required"]


def test_aggregator_schedule_respected(monkeypatch):
    calls = []
    monkeypatch.setattr(aggregators, "SOURCES", {"a": (lambda c, x, l: calls.append("a") or [], 1),
                                                 "b": (lambda c, x, l: calls.append("b") or [], 24)})
    state = {}
    aggregators.collect({}, ctx(), print, state)
    aggregators.collect({}, ctx(), print, state)          # immediately again: neither is due
    assert calls == ["a", "b"] and set(state) == {"a", "b"}


def test_apply_queue_orders_quick_forms_first():
    now = datetime.now(timezone.utc).isoformat()
    base = {"status": "open", "first_seen": now, "posted_at": TODAY, "location": "", "score": 80}
    roles = [dict(base, uid="w", company="W", title="VP", url="u1", source="workday"),
             dict(base, uid="g", company="G", title="VP", url="u2", source="greenhouse",
                  extra={"questions": [{"label": "Why us?"}]}),
             dict(base, uid="old", company="O", title="VP", url="u3", source="greenhouse", posted_at="2020-01-01")]
    q = apply_queue.build(roles)
    assert [r["uid"] for r in q] == ["g", "w"]
    assert q[0]["apply_via"] == "quick form" and q[0]["questions"]
    assert "⚡ quick form" in apply_queue.markdown(q)


def test_sources_without_keys_are_not_marked_as_run(monkeypatch):
    monkeypatch.delenv("RAPIDAPI_KEY", raising=False)
    state = {}
    monkeypatch.setattr(aggregators, "SOURCES", {"jsearch": (aggregators.jsearch, 24)})
    aggregators.collect({}, ctx(), print, state)
    assert "jsearch" not in state          # runs as soon as a key is added, not a day later


def test_jsearch_budget_stops_before_the_plan_runs_out(monkeypatch):
    monkeypatch.setenv("RAPIDAPI_KEY", "k")
    calls = []

    class Resp:
        status_code = 200
        headers = {"x-ratelimit-requests-remaining": "21"}

        def raise_for_status(self):
            pass

        def json(self):
            return {"data": {"jobs": []}}

    class S:
        headers = {}

        def get(self, url, **kw):
            calls.append(kw["params"]["query"])
            Resp.headers = {"x-ratelimit-requests-remaining": str(21 - len(calls))}
            return Resp()
    monkeypatch.setattr(aggregators, "session", lambda: S())
    state = {}
    monkeypatch.setattr(aggregators, "SOURCES", {"jsearch": (aggregators.jsearch, 24)})
    cfg = {"aggregators": {"jsearch": {"monthly_cap": 150, "reserve": 20, "queries": ["a", "b", "c"]}}}
    aggregators.collect(cfg, ctx(), print, state)
    assert calls == ["a"]                                   # stopped once the plan reported 20 left
    assert state["jsearch_usage"]["calls"] == 1 and state["jsearch_usage"]["remaining"] == 20
    # a new month resets the count but the plan's own remaining figure is re-read on the next call
    state["jsearch_usage"]["month"] = "2000-01"
    state.pop("jsearch")
    aggregators.collect(cfg, ctx(), print, state)
    assert state["jsearch_usage"]["calls"] == 1


def test_jsearch_monthly_cap(monkeypatch):
    monkeypatch.setenv("RAPIDAPI_KEY", "k")
    month = datetime.now(timezone.utc).strftime("%Y-%m")
    state = {"jsearch_usage": {"month": month, "calls": 150}}
    calls = []

    class S:
        headers = {}

        def get(self, url, **kw):
            calls.append(url)
    monkeypatch.setattr(aggregators, "session", lambda: S())
    monkeypatch.setattr(aggregators, "SOURCES", {"jsearch": (aggregators.jsearch, 24)})
    aggregators.collect({"aggregators": {"jsearch": {"monthly_cap": 150}}}, ctx(), print, state)
    assert calls == [] and state["jsearch_usage"]["calls"] == 150
