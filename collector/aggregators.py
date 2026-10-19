"""Job aggregators with official public APIs. Each returns Postings; any failure is
logged and skipped so an outage at one source never affects the run.

  The Muse   https://www.themuse.com/developers/api/v2  no key needed
  Adzuna     https://developer.adzuna.com               free key: set repo secrets
                                                        ADZUNA_APP_ID and ADZUNA_APP_KEY
"""
from __future__ import annotations

import os

from .common import Posting, get_json, html_to_text, session


def themuse(cfg: dict, ctx, log) -> list[Posting]:
    a = (cfg.get("aggregators") or {}).get("themuse") or {}
    if not a.get("enabled", True):
        return []
    s = session()
    out, pages = [], int(a.get("pages", 15))
    for page in range(pages):
        try:
            d = get_json(s, "https://www.themuse.com/api/public/jobs", tries=2, params={
                "page": page, "descending": "true", "level": ["Senior Level", "management"]})
        except Exception as e:
            log(f"themuse: page {page} failed ({e})")
            break
        items = d.get("items") or []
        if page == 0:
            log(f"themuse: page 0 returned {len(items)} items of {d.get('total')} total")
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
        if page + 1 >= int(d.get("page_count") or 0):
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


SOURCES = {"themuse": themuse, "adzuna": adzuna}


def collect(cfg: dict, ctx, log) -> tuple[list[Posting], dict]:
    out, counts = [], {}
    for name, fn in SOURCES.items():
        try:
            got = fn(cfg, ctx, log)
        except Exception as e:  # never let a source sink the run
            log(f"{name}: failed ({e})")
            got = []
        counts[name] = len(got)
        out.extend(got)
    return out, counts
