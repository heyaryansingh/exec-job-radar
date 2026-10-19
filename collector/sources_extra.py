"""Readers for large employers' own career-search systems, beyond the common ATSs.

  eightfold  Eightfold "PCS" career sites (Microsoft, Netflix, and many large employers)
             entry: {ats: eightfold, host: apply.careers.microsoft.com, domain: microsoft.com}
  phenom     Phenom People career sites (HPE and many Fortune 500 employers)
             entry: {ats: phenom, host: careers.hpe.com, locale: us/en, refnum: HPE1US}
  amazon     amazon.jobs public search
             entry: {ats: amazon}
  sitemap    Any career site that publishes job pages for Google for Jobs: reads the
             site's sitemap and the schema.org JobPosting data embedded in each page.
             entry: {ats: sitemap, sitemap: https://careers.example.com/sitemap.xml,
                     include: "/job/"}

These are the same public endpoints the employers' own career pages call in a browser.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from xml.etree import ElementTree as ET

from .common import Posting, get_json, html_to_text


def _base(c: dict, **kw) -> Posting:
    return Posting(company=c["name"], tier=int(c.get("tier", 2)), sector=c.get("sector", ""), **kw)


def _too_old(iso: str | None, ctx) -> bool:
    if not iso:
        return False
    try:
        d = datetime.fromisoformat(iso[:10]).date()
        return (datetime.now(timezone.utc).date() - d).days > ctx.max_age_days
    except ValueError:
        return False


# ------------------------------------------------------------------ Eightfold
def eightfold(c, s, ctx):
    host, domain = c["host"], c["domain"]
    api = f"https://{host}/api/apply/v2/jobs"
    out, ids, ok = [], set(), 0
    for q in ctx.level_queries:
        for start in range(0, 100, 10):
            try:
                d = get_json(s, api, tries=2, params={"domain": domain, "start": start, "num": 10,
                                                       "query": q, "sort_by": "timestamp"})
            except Exception:
                break
            ok += 1
            pos = d.get("positions") or []
            for j in pos:
                jid = str(j.get("id"))
                title = j.get("name") or ""
                if jid in ids or not ctx.title_ok(title):
                    continue
                ids.add(jid)
                posted = None
                if j.get("t_create"):
                    posted = datetime.fromtimestamp(int(j["t_create"]), tz=timezone.utc).date().isoformat()
                if _too_old(posted, ctx):
                    continue
                locs = j.get("locations") or [j.get("location") or ""]
                p = _base(c, source="eightfold", job_id=jid, title=title.strip(),
                          url=j.get("canonicalPositionUrl") or f"https://{host}/careers/job/{jid}?domain={domain}",
                          location="; ".join(x for x in locs if x), posted_at=posted,
                          extra={"check": f"{api}/{jid}?domain={domain}"})
                p.remote = "remote" in (p.location + " " + str(j.get("work_location_option", ""))).lower()
                if ctx.is_new(p):
                    try:
                        dd = get_json(s, f"{api}/{jid}", tries=2, params={"domain": domain})
                        p.description = html_to_text(dd.get("job_description"))
                    except Exception:
                        pass
                p.fill_pay_from_text()
                out.append(p)
            if len(pos) < 10:
                break
    if not ok:
        raise RuntimeError(f"eightfold: no response from {host}")
    return out


# ------------------------------------------------------------------ Phenom
def phenom(c, s, ctx):
    host = c["host"]
    locale = c.get("locale", "us/en")
    country, lang = locale.split("/") if "/" in locale else ("us", "en")
    out, ids, ok = [], set(), 0
    for q in ctx.level_queries:
        for frm in range(0, 200, 50):
            body = {"lang": f"{lang}_{country}", "deviceType": "desktop", "country": country,
                    "pageName": "search-results", "ddoKey": "refineSearch", "sortBy": "Most recent",
                    "subsearch": "", "from": frm, "jobs": True, "counts": True, "all_fields": [],
                    "size": 50, "clearAll": False, "jdsource": "facets", "isSliderEnable": False,
                    "pageId": "page20", "siteType": "external", "keywords": q, "global": True,
                    "selected_fields": {}, "locationData": {}}
            if c.get("refnum"):
                body["refNum"] = c["refnum"]
            try:
                d = get_json(s, f"https://{host}/widgets", method="POST", tries=2, body=body)
            except Exception:
                break
            data = ((d.get("refineSearch") or {}).get("data") or {})
            jobs = data.get("jobs") or []
            ok += 1
            for j in jobs:
                jid = str(j.get("jobSeqNo") or j.get("jobId") or j.get("reqId"))
                title = j.get("title") or ""
                if jid in ids or not ctx.title_ok(title):
                    continue
                ids.add(jid)
                posted = (j.get("postedDate") or j.get("dateCreated") or "")[:10] or None
                if _too_old(posted, ctx):
                    continue
                loc = j.get("cityStateCountry") or j.get("location") or ", ".join(
                    x for x in [j.get("city"), j.get("state"), j.get("country")] if x)
                p = _base(c, source="phenom", job_id=jid, title=title.strip(),
                          url=f"https://{host}/{locale}/job/{jid}",
                          location=loc or "", posted_at=posted,
                          description=html_to_text(j.get("descriptionTeaser") or j.get("description") or ""))
                p.remote = "remote" in (loc or "").lower() or bool(j.get("isRemote"))
                p.fill_pay_from_text()
                out.append(p)
            if len(jobs) < 50:
                break
    if not ok:
        raise RuntimeError(f"phenom: no response from {host}")
    return out


# ------------------------------------------------------------------ Amazon
def amazon(c, s, ctx):
    out, ids = [], set()
    for q in ctx.level_queries:
        for offset in range(0, 300, 100):
            d = get_json(s, "https://www.amazon.jobs/en/search.json", tries=2, params={
                "base_query": q, "result_limit": 100, "offset": offset, "sort": "recent",
                "normalized_country_code[]": "USA"})
            jobs = d.get("jobs") or []
            for j in jobs:
                jid = str(j.get("id_icims") or j.get("id"))
                title = j.get("title") or ""
                if jid in ids or not ctx.title_ok(title):
                    continue
                ids.add(jid)
                posted = None
                try:
                    posted = datetime.strptime(j.get("posted_date", ""), "%B %d, %Y").date().isoformat()
                except ValueError:
                    pass
                if _too_old(posted, ctx):
                    continue
                desc = "\n\n".join(html_to_text(j.get(k)) for k in
                                   ("description", "basic_qualifications", "preferred_qualifications") if j.get(k))
                p = _base(c, source="amazon", job_id=jid, title=title.strip(),
                          url="https://www.amazon.jobs" + (j.get("job_path") or f"/en/jobs/{jid}"),
                          location=j.get("normalized_location") or j.get("location") or "",
                          posted_at=posted, description=desc)
                p.company = c["name"]
                p.fill_pay_from_text()
                out.append(p)
            if len(jobs) < 100:
                break
    return out


# ------------------------------------------------------------------ Sitemap + JSON-LD
_LD = re.compile(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', re.S | re.I)
LEVEL_IN_URL = re.compile(r"(director|vice-?president|\bvp\b|-vp-|head-of|chief|executive|managing|svp|evp|cto|cio)", re.I)


def _job_ld(html: str):
    for m in _LD.finditer(html):
        try:
            data = json.loads(m.group(1).strip())
        except ValueError:
            continue
        stack = data if isinstance(data, list) else [data]
        while stack:
            x = stack.pop()
            if isinstance(x, dict):
                t = x.get("@type")
                if t == "JobPosting" or (isinstance(t, list) and "JobPosting" in t):
                    return x
                stack.extend(x.get("@graph") or [])
            elif isinstance(x, list):
                stack.extend(x)
    return None


def _ld_location(ld: dict) -> str:
    locs = ld.get("jobLocation") or []
    locs = locs if isinstance(locs, list) else [locs]
    out = []
    for l in locs:
        a = (l or {}).get("address") or {}
        if isinstance(a, str):
            out.append(a)
        else:
            out.append(", ".join(x for x in [a.get("addressLocality"), a.get("addressRegion"),
                                               a.get("addressCountry") if isinstance(a.get("addressCountry"), str)
                                               else (a.get("addressCountry") or {}).get("name")] if x))
    return "; ".join(x for x in out if x)


def _sitemap_urls(s, url: str, include: re.Pattern, depth: int = 0) -> list[tuple[str, str]]:
    r = s.get(url, timeout=30, headers={"Accept": "application/xml,text/xml,*/*"})
    r.raise_for_status()
    root = ET.fromstring(r.content)
    ns = {"sm": root.tag.split("}")[0].strip("{")} if root.tag.startswith("{") else {}
    tag = (lambda t: f"sm:{t}") if ns else (lambda t: t)
    if root.tag.endswith("sitemapindex"):
        out = []
        for sm in root.findall(tag("sitemap"), ns)[:200]:
            loc = (sm.findtext(tag("loc"), "", ns) or "").strip()
            if depth < 2 and loc and re.search(r"job|position|career|posting", loc, re.I):
                try:
                    out += _sitemap_urls(s, loc, include, depth + 1)
                except Exception:
                    continue
        return out
    out = []
    for u in root.findall(tag("url"), ns):
        loc = (u.findtext(tag("loc"), "", ns) or "").strip()
        if loc and include.search(loc):
            out.append((loc, (u.findtext(tag("lastmod"), "", ns) or "").strip()))
    return out


def sitemap(c, s, ctx):
    include = re.compile(c.get("include") or r"/jobs?/|/position|/careers?/", re.I)
    urls = _sitemap_urls(s, c["sitemap"], include)
    if not urls:
        raise RuntimeError("sitemap: no job URLs")
    urls.sort(key=lambda t: t[1], reverse=True)
    out, fetched = [], 0
    for loc, lastmod in urls:
        if lastmod and _too_old(lastmod, ctx):
            continue
        slug = loc.rstrip("/").rsplit("/", 1)[-1]
        jid = re.sub(r"[^\w-]", "", slug)[:80] or hashlib.sha1(loc.encode()).hexdigest()[:16]
        probe = _base(c, source="sitemap", job_id=jid, title="", url=loc)
        if not ctx.is_new(probe):
            continue
        if re.search(r"[a-z]{4,}-[a-z]{3,}", loc, re.I) and not LEVEL_IN_URL.search(loc):
            continue  # the URL spells out a title, and it isn't a senior one
        if fetched >= int(c.get("max_new", 60)):
            break
        fetched += 1
        try:
            r = s.get(loc, timeout=25, headers={"Accept": "text/html"})
            ld = _job_ld(r.text) if r.ok else None
        except Exception:
            ld = None
        if not ld:
            continue
        title = html_to_text(ld.get("title") or "")
        p = _base(c, source="sitemap", job_id=jid, title=title.strip(), url=loc,
                  location=_ld_location(ld), posted_at=(ld.get("datePosted") or "")[:10] or None,
                  description=html_to_text(ld.get("description") or ""))
        org = (ld.get("hiringOrganization") or {})
        if isinstance(org, dict) and org.get("name") and c.get("name_from_page"):
            p.company = org["name"]
        p.remote = str(ld.get("jobLocationType", "")).upper() == "TELECOMMUTE" or "remote" in p.location.lower()
        sal = (ld.get("baseSalary") or {}).get("value") if isinstance(ld.get("baseSalary"), dict) else None
        if isinstance(sal, dict) and (sal.get("maxValue") or sal.get("value")):
            unit = str(sal.get("unitText", "YEAR")).upper()
            mult = 2080 if unit == "HOUR" else 1
            try:
                p.pay_max = int(float(sal.get("maxValue") or sal.get("value")) * mult)
                p.pay_min = int(float(sal["minValue"]) * mult) if sal.get("minValue") else None
                p.pay_text = "posted range"
            except (TypeError, ValueError):
                pass
        p.fill_pay_from_text()
        out.append(p)  # all fetched pages are returned so non-senior ones are remembered
    return out


EXTRA_ADAPTERS = {"eightfold": eightfold, "phenom": phenom, "amazon": amazon, "sitemap": sitemap}
