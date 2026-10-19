"""Job aggregators with official public APIs. Each returns Postings; any failure is
logged and skipped so an outage at one source never affects the run.

  The Muse   https://www.themuse.com/developers/api/v2  no key needed
  Adzuna     https://developer.adzuna.com               free key: set repo secrets
                                                        ADZUNA_APP_ID and ADZUNA_APP_KEY
"""
from __future__ import annotations

import os
from datetime import datetime, timezone

from .common import Posting, get_json, html_to_text, session


def themuse(cfg: dict, ctx, log) -> list[Posting]:
    a = (cfg.get("aggregators") or {}).get("themuse") or {}
    if not a.get("enabled", True):
        return []
    s = session()
    out, pages = [], int(a.get("pages", 15))
    for page in range(1, pages + 1):
        try:
            d = get_json(s, "https://www.themuse.com/api/public/jobs", tries=2, params={
                "page": page, "level": ["Senior Level", "Management"]})
        except Exception as e:
            log(f"themuse: page {page} failed ({e})")
            break
        items = d.get("items") or []
        if page == 1:
            log(f"themuse: page 1 returned {len(items)} items of {d.get('total')} total")
        for j in items:
            title = j.get("name") or ""
            if not ctx.title_ok(title):
                continue
            locs = "; ".join(x.get("name", "") for x in j.get("locations") or [])
            p = Posting(source="themuse", company=(j.get("company") or {}).get("name") or "Unknown",
                        job_id=str(j.get("id")), title=title.strip(),
                        url=(j.get("refs") or {}).get("landing_page", ""), location=locs,
                        remote="remote" in locs.lower() or "flexible" in locs.lower(),
                        posted_at=(j.get("publication_date") or "")[:10] or None,
                        description=html_to_text(j.get("contents")), tier=3)
            p.fill_pay_from_text()
            out.append(p)
        if page >= int(d.get("page_count") or 0):
            break
    return out


def adzuna(cfg: dict, ctx, log) -> list[Posting]:
    a = (cfg.get("aggregators") or {}).get("adzuna") or {}
    app_id, key = os.environ.get("ADZUNA_APP_ID"), os.environ.get("ADZUNA_APP_KEY")
    if not a.get("enabled", True) or not (app_id and key):
        return []
    s = session()
    out, seen = [], set()
    for title_q in a.get("title_queries") or ["vice president", "director", "head of", "chief",
                                              "executive director", "managing director"]:
        for page in range(1, int(a.get("pages", 4)) + 1):
            try:
                d = get_json(s, f"https://api.adzuna.com/v1/api/jobs/us/search/{page}", tries=2, params={
                    "app_id": app_id, "app_key": key, "results_per_page": 50, "title_only": title_q,
                    "max_days_old": int(a.get("max_days_old", 3)), "sort_by": "date",
                    "salary_min": int(cfg.get("pay", {}).get("min_annual", 0)) or None,
                    "category": a.get("category", "it-jobs"), "content-type": "application/json"})
            except Exception as e:
                log(f"adzuna: '{title_q}' p{page} failed ({e})")
                break
            res = d.get("results") or []
            for j in res:
                jid = str(j.get("id"))
                title = j.get("title") or ""
                if jid in seen or not ctx.title_ok(title):
                    continue
                seen.add(jid)
                p = Posting(source="adzuna", company=(j.get("company") or {}).get("display_name") or "Unknown",
                            job_id=jid, title=html_to_text(title).strip(), url=j.get("redirect_url", ""),
                            location=(j.get("location") or {}).get("display_name", ""),
                            posted_at=(j.get("created") or "")[:10] or None,
                            description=html_to_text(j.get("description")), tier=3)
                if j.get("salary_max") and not j.get("salary_is_predicted") in ("1", 1, True):
                    p.pay_max = int(float(j["salary_max"]))
                    p.pay_min = int(float(j["salary_min"])) if j.get("salary_min") else None
                    p.pay_text = "posted range (via Adzuna)"
                p.remote = "remote" in (p.location + " " + p.title).lower()
                out.append(p)
            if len(res) < 50:
                break
    return out


def himalayas(cfg: dict, ctx, log) -> list[Posting]:
    """Remote jobs (himalayas.app public API, no key)."""
    a = (cfg.get("aggregators") or {}).get("himalayas") or {}
    if not a.get("enabled", True):
        return []
    s = session()
    out = []
    offset = 0
    while offset < int(a.get("max", 600)):
        try:
            d = get_json(s, "https://himalayas.app/jobs/api", tries=2, params={"limit": 20, "offset": offset})
        except Exception as e:
            log(f"himalayas: failed ({e})")
            break
        jobs = d.get("jobs") or []
        if offset == 0:
            log(f"himalayas: {len(jobs)} jobs on first page")
        for j in jobs:
            title = j.get("title") or ""
            if not ctx.title_ok(title):
                continue
            locs = j.get("locationRestrictions") or []
            loc = "Remote" + (f" ({', '.join(locs)})" if locs else "")
            p = Posting(source="himalayas", company=j.get("companyName") or "Unknown",
                        job_id=str(j.get("guid") or j.get("applicationLink")), title=title.strip(),
                        url=j.get("applicationLink") or "", location=loc, remote=True,
                        posted_at=_epoch_date(j.get("pubDate")), description=html_to_text(j.get("description")), tier=3)
            if j.get("maxSalary"):
                p.pay_max, p.pay_min = int(j["maxSalary"]), int(j["minSalary"]) if j.get("minSalary") else None
                p.pay_text = "posted range"
            p.fill_pay_from_text()
            out.append(p)
        if not jobs:
            break
        offset += len(jobs)
    return out


def remotive(cfg: dict, ctx, log) -> list[Posting]:
    """Remote jobs (remotive.com public API; they ask for at most a few calls a day)."""
    a = (cfg.get("aggregators") or {}).get("remotive") or {}
    if not a.get("enabled", True):
        return []
    s = session()
    out = []
    for cat in a.get("categories") or ["software-dev", "devops", "data"]:
        try:
            d = get_json(s, "https://remotive.com/api/remote-jobs", tries=1, params={"category": cat})
        except Exception as e:
            log(f"remotive: {cat} failed ({e})")
            continue
        log(f"remotive: {cat}: {len(d.get('jobs') or [])} jobs")
        for j in d.get("jobs") or []:
            title = j.get("title") or ""
            if not ctx.title_ok(title):
                continue
            p = Posting(source="remotive", company=j.get("company_name") or "Unknown", job_id=str(j.get("id")),
                        title=title.strip(), url=j.get("url") or "",
                        location="Remote" + (f" ({j['candidate_required_location']})"
                                             if j.get("candidate_required_location") else ""),
                        remote=True, posted_at=(j.get("publication_date") or "")[:10] or None,
                        description=html_to_text(j.get("description")), tier=3)
            p.fill_pay_from_text()
            out.append(p)
    return out


def usajobs(cfg: dict, ctx, log) -> list[Posting]:
    """Federal roles incl. Senior Executive Service (official API; free key: set
    USAJOBS_API_KEY and USAJOBS_EMAIL secrets)."""
    a = (cfg.get("aggregators") or {}).get("usajobs") or {}
    key, email = os.environ.get("USAJOBS_API_KEY"), os.environ.get("USAJOBS_EMAIL")
    if not a.get("enabled", True) or not (key and email):
        return []
    s = session()
    s.headers.update({"Authorization-Key": key, "User-Agent": email, "Host": "data.usajobs.gov"})
    out = []
    for kw in a.get("keywords") or ["information technology", "chief information officer", "cloud",
                                    "cybersecurity", "data"]:
        try:
            d = get_json(s, "https://data.usajobs.gov/api/search", tries=2, params={
                "Keyword": kw, "DatePosted": 3, "ResultsPerPage": 250,
                "RemunerationMinimumAmount": int(cfg.get("pay", {}).get("min_annual", 0)) or None})
        except Exception as e:
            log(f"usajobs: '{kw}' failed ({e})")
            continue
        for item in ((d.get("SearchResult") or {}).get("SearchResultItems") or []):
            j = item.get("MatchedObjectDescriptor") or {}
            title = j.get("PositionTitle") or ""
            if not ctx.title_ok(title) and "senior executive" not in str(j).lower():
                continue
            pay = (j.get("PositionRemuneration") or [{}])[0]
            p = Posting(source="usajobs", company=j.get("OrganizationName") or "US Government",
                        job_id=str(j.get("PositionID") or item.get("MatchedObjectId")), title=title.strip(),
                        url=j.get("PositionURI") or "", location=j.get("PositionLocationDisplay") or "",
                        posted_at=(j.get("PublicationStartDate") or "")[:10] or None,
                        description=html_to_text(((j.get("UserArea") or {}).get("Details") or {}).get("JobSummary")),
                        tier=2)
            try:
                p.pay_max, p.pay_min = int(float(pay.get("MaximumRange"))), int(float(pay.get("MinimumRange")))
                p.pay_text = "posted range"
            except (TypeError, ValueError):
                pass
            out.append(p)
    return out


def jsearch(cfg: dict, ctx, log) -> list[Posting]:
    """JSearch (RapidAPI): a licensed Google-for-Jobs feed that includes roles posted on
    LinkedIn, Indeed, Glassdoor, ZipRecruiter and employer sites. Needs RAPIDAPI_KEY;
    the free tier allows ~200 calls a month, so it runs a few queries once a day."""
    a = (cfg.get("aggregators") or {}).get("jsearch") or {}
    key = os.environ.get("RAPIDAPI_KEY")
    if not a.get("enabled", True) or not key:
        return []
    s = session()
    s.headers.update({"X-RapidAPI-Key": key, "X-RapidAPI-Host": "jsearch.p.rapidapi.com"})
    out = []
    for q in a.get("queries") or ["vice president technology in USA", "director cloud infrastructure in USA",
                                  "head of engineering in USA", "chief technology officer in USA"]:
        try:
            d = get_json(s, "https://jsearch.p.rapidapi.com/search", tries=2,
                         params={"query": q, "date_posted": "today", "num_pages": int(a.get("pages", 1)),
                                 "country": "us"})
        except Exception as e:
            log(f"jsearch: '{q}' failed ({e})")
            continue
        for j in d.get("data") or []:
            title = j.get("job_title") or ""
            if not ctx.title_ok(title):
                continue
            loc = ", ".join(x for x in [j.get("job_city"), j.get("job_state")] if x) or (j.get("job_country") or "")
            p = Posting(source="jsearch", company=j.get("employer_name") or "Unknown", job_id=str(j.get("job_id")),
                        title=title.strip(), url=j.get("job_apply_link") or j.get("job_google_link") or "",
                        location=loc, remote=bool(j.get("job_is_remote")),
                        posted_at=(j.get("job_posted_at_datetime_utc") or "")[:10] or None,
                        description=j.get("job_description") or "", tier=3,
                        extra={"via": j.get("job_publisher")})
            if j.get("job_max_salary") and (j.get("job_salary_period") or "YEAR").upper() == "YEAR":
                p.pay_max = int(j["job_max_salary"])
                p.pay_min = int(j["job_min_salary"]) if j.get("job_min_salary") else None
            p.fill_pay_from_text()
            out.append(p)
    return out


def _epoch_date(v):
    try:
        return datetime.fromtimestamp(int(v), tz=timezone.utc).date().isoformat()
    except (TypeError, ValueError):
        return None


# name -> (function, minimum hours between calls); free tiers are respected
SOURCES = {"themuse": (themuse, 1), "adzuna": (adzuna, 1), "himalayas": (himalayas, 3),
           "remotive": (remotive, 8), "usajobs": (usajobs, 6), "jsearch": (jsearch, 24)}


def collect(cfg: dict, ctx, log, state: dict | None = None) -> tuple[list[Posting], dict]:
    """Run every due source. `state` remembers when each last ran (persisted by caller)."""
    out, counts = [], {}
    state = state if state is not None else {}
    now = datetime.now(timezone.utc)
    for name, (fn, every) in SOURCES.items():
        last = state.get(name)
        if last:
            try:
                if (now - datetime.fromisoformat(last)).total_seconds() < every * 3600 - 300:
                    continue
            except ValueError:
                pass
        try:
            got = fn(cfg, ctx, log)
            state[name] = now.replace(microsecond=0).isoformat()
        except Exception as e:  # never let a source sink the run
            log(f"{name}: failed ({e})")
            got = []
        counts[name] = len(got)
        out.extend(got)
    return out, counts
