"""Adapters for the applicant tracking systems most large employers use.

Every adapter has the signature
    fetch(company: dict, s: Session, ctx: Ctx) -> list[Posting]
and only fetches job *details* for postings whose title passes ctx.title_ok and
that have not been seen before, so a 10,000-job employer costs a few list calls.

Company entries (config/companies.yaml) look like:
    - {name: Capital One, ats: workday, host: capitalone.wd12.myworkdayjobs.com, site: Capital_One, tier: 1, sector: bank}
    - {name: Stripe, ats: greenhouse, slug: stripe, tier: 1, sector: fintech}
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Callable

from .common import Posting, get_json, html_to_text, iso_from_ms


@dataclass
class Ctx:
    title_ok: Callable[[str], bool]   # cheap level/domain check on the title
    known: set                        # uids already processed
    level_queries: list               # search words for sites with keyword search
    max_age_days: int = 30

    def is_new(self, p: Posting) -> bool:
        return p.uid not in self.known


def _base(company: dict, **kw) -> Posting:
    return Posting(company=company["name"], tier=int(company.get("tier", 2)),
                   sector=company.get("sector", ""), **kw)


STANDARD_FIELDS = {"first_name", "last_name", "email", "phone", "resume", "resume_text", "cover_letter",
                   "cover_letter_text"}


def compact_questions(qs: list) -> list:
    """Greenhouse application questions, minus the standard contact/resume fields, kept
    small: label, required, type, and up to 12 options."""
    out = []
    for q in qs:
        fields = q.get("fields") or []
        if not fields or all(f.get("name") in STANDARD_FIELDS for f in fields):
            continue
        f = fields[0]
        out.append({"label": html_to_text(q.get("label", ""))[:200], "required": bool(q.get("required")),
                    "type": f.get("type", ""),
                    "options": [v.get("label", "") for v in (f.get("values") or [])][:12]})
    return out[:25]


# ----------------------------------------------------------------- Greenhouse
def greenhouse(c, s, ctx):
    """Light listing (titles only), then the full posting for new matching titles, so a
    board with thousands of jobs costs one call plus one per new match."""
    base = f"https://boards-api.greenhouse.io/v1/boards/{c['slug']}"
    data = get_json(s, f"{base}/jobs")
    out = []
    for j in data.get("jobs", []):
        if not ctx.title_ok(j.get("title", "")):
            continue
        p = _base(c, source="greenhouse", job_id=str(j["id"]), title=j["title"].strip(),
                  url=j.get("absolute_url", ""),
                  location=(j.get("location") or {}).get("name", ""),
                  posted_at=(j.get("first_published") or j.get("updated_at") or "")[:10] or None,
                  description=html_to_text(j.get("content")))
        if not p.description and ctx.is_new(p):
            try:
                d = get_json(s, f"{base}/jobs/{j['id']}", tries=2, params={"questions": "true"})
                p.description = html_to_text(d.get("content"))
                qs = compact_questions(d.get("questions") or [])
                if qs:
                    p.extra["questions"] = qs
                p.posted_at = (d.get("first_published") or "")[:10] or p.posted_at
            except Exception:
                pass
        p.remote = "remote" in p.location.lower()
        p.fill_pay_from_text()
        out.append(p)
    return out


# ----------------------------------------------------------------- Lever
def lever(c, s, ctx):
    data = get_json(s, f"https://api.lever.co/v0/postings/{c['slug']}", params={"mode": "json"})
    out = []
    for j in data if isinstance(data, list) else []:
        title = j.get("text", "")
        if not ctx.title_ok(title):
            continue
        cats = j.get("categories") or {}
        parts = [j.get("descriptionPlain") or ""]
        for lst in j.get("lists") or []:
            parts.append(lst.get("text", ""))
            parts.append(html_to_text(lst.get("content", "")))
        parts.append(j.get("additionalPlain") or "")
        p = _base(c, source="lever", job_id=j["id"], title=title.strip(),
                  url=j.get("hostedUrl", ""), location=cats.get("location", "") or "",
                  posted_at=iso_from_ms(j.get("createdAt")),
                  description="\n".join(x for x in parts if x).strip())
        p.remote = (j.get("workplaceType") == "remote") or "remote" in p.location.lower()
        sr = j.get("salaryRange") or {}
        if sr.get("max") and (sr.get("interval") in (None, "per-year-salary")):
            p.pay_min, p.pay_max = int(sr.get("min") or 0) or None, int(sr["max"])
            p.pay_text = f"${p.pay_min or '?'}-${p.pay_max} (posted range)"
        p.fill_pay_from_text()
        out.append(p)
    return out


# ----------------------------------------------------------------- Ashby
def ashby(c, s, ctx):
    data = get_json(s, f"https://api.ashbyhq.com/posting-api/job-board/{c['slug']}",
                    params={"includeCompensation": "true"})
    out = []
    for j in data.get("jobs", []):
        if not j.get("isListed", True) or not ctx.title_ok(j.get("title", "")):
            continue
        locs = [j.get("location") or ""] + [x.get("location", "") for x in j.get("secondaryLocations") or []]
        p = _base(c, source="ashby", job_id=j["id"], title=j["title"].strip(),
                  url=j.get("jobUrl", ""), location="; ".join(x for x in locs if x),
                  remote=bool(j.get("isRemote")) or j.get("workplaceType") == "Remote",
                  posted_at=(j.get("publishedAt") or "")[:10] or None,
                  description=j.get("descriptionPlain") or html_to_text(j.get("descriptionHtml")))
        comp = j.get("compensation") or {}
        for comp_part in comp.get("summaryComponents") or []:
            if comp_part.get("compensationType") == "Salary" and comp_part.get("maxValue"):
                p.pay_min = int(comp_part.get("minValue") or 0) or None
                p.pay_max = int(comp_part["maxValue"])
                p.pay_text = comp.get("compensationTierSummary") or ""
        p.fill_pay_from_text()
        out.append(p)
    return out


# ----------------------------------------------------------------- SmartRecruiters
def smartrecruiters(c, s, ctx):
    slug = c["slug"]
    out, offset = [], 0
    for q in ctx.level_queries:
        offset = 0
        while offset < 500:
            data = get_json(s, f"https://api.smartrecruiters.com/v1/companies/{slug}/postings",
                            params={"limit": 100, "offset": offset, "q": q, "country": "us"})
            items = data.get("content", [])
            for j in items:
                if not ctx.title_ok(j.get("name", "")):
                    continue
                loc = j.get("location") or {}
                p = _base(c, source="smartrecruiters", job_id=str(j["id"]), title=j["name"].strip(),
                          url=f"https://jobs.smartrecruiters.com/{slug}/{j['id']}",
                          location=", ".join(x for x in [loc.get("city"), loc.get("region"), loc.get("country")] if x),
                          remote=bool(loc.get("remote")),
                          posted_at=(j.get("releasedDate") or "")[:10] or None,
                          extra={"check": f"https://api.smartrecruiters.com/v1/companies/{slug}/postings/{j['id']}"})
                if any(o.uid == p.uid for o in out):
                    continue
                if ctx.is_new(p):
                    try:
                        d = get_json(s, f"https://api.smartrecruiters.com/v1/companies/{slug}/postings/{j['id']}")
                        secs = ((d.get("jobAd") or {}).get("sections") or {})
                        p.description = "\n\n".join(html_to_text((secs.get(k) or {}).get("text"))
                                                    for k in ("companyDescription", "jobDescription",
                                                              "qualifications", "additionalInformation"))
                        p.url = d.get("postingUrl") or p.url
                    except Exception:
                        pass
                p.fill_pay_from_text()
                out.append(p)
            offset += 100
            if len(items) < 100:
                break
    return out


# ----------------------------------------------------------------- Workday
_WD_AGE = re.compile(r"(\d+)\+?\s+Days?\s+Ago", re.I)


def _wd_posted(text: str):
    t = (text or "").lower()
    today = date.today()
    if "today" in t:
        return today.isoformat(), 0
    if "yesterday" in t:
        return (today - timedelta(days=1)).isoformat(), 1
    m = _WD_AGE.search(text or "")
    if m:
        n = int(m.group(1))
        return (today - timedelta(days=n)).isoformat(), n + (1 if "+" in text else 0)
    return None, None


def workday(c, s, ctx):
    host = c["host"]                      # e.g. capitalone.wd12.myworkdayjobs.com
    site = c["site"]                      # e.g. Capital_One
    tenant = c.get("tenant") or host.split(".")[0]
    api = f"https://{host}/wday/cxs/{tenant}/{site}"
    public = c.get("public_base") or f"https://{host}/en-US/{site}"
    out, seen_paths = [], set()
    ok_calls, first_err = 0, None
    queries = list(ctx.level_queries)
    tried_plain = False
    while queries:
        q = queries.pop(0)
        for offset in range(0, 200, 20):  # newest first; stop early on old jobs
            try:
                data = get_json(s, f"{api}/jobs", method="POST", tries=2,
                                body={"appliedFacets": {}, "limit": 20, "offset": offset, "searchText": q})
            except Exception as e:  # one bad page or query shouldn't sink the company
                first_err = first_err or e
                break
            ok_calls += 1
            posts = data.get("jobPostings") or []
            too_old = 0
            for j in posts:
                path = j.get("externalPath") or ""
                if not path or path in seen_paths:
                    continue
                seen_paths.add(path)
                posted, age = _wd_posted(j.get("postedOn", ""))
                if age is not None and age > ctx.max_age_days:
                    too_old += 1
                    continue
                title = j.get("title", "")
                if not ctx.title_ok(title):
                    continue
                job_id = (j.get("bulletFields") or [path.rsplit("_", 1)[-1]])[0]
                p = _base(c, source="workday", job_id=str(job_id), title=title.strip(),
                          url=f"{public}{path}", location=j.get("locationsText", "") or "",
                          posted_at=posted, extra={"check": f"{api}{path}"})
                if ctx.is_new(p):
                    try:
                        d = get_json(s, f"{api}{path}")
                        org = (d.get("hiringOrganization") or {}).get("name")
                        if org and not c.get("_org"):
                            c["_org"] = org.strip()
                        info = d.get("jobPostingInfo") or {}
                        p.description = html_to_text(info.get("jobDescription"))
                        p.url = info.get("externalUrl") or p.url
                        locs = [info.get("location")] + (info.get("additionalLocations") or [])
                        p.location = "; ".join(x for x in locs if x) or p.location
                        p.posted_at = info.get("startDate") or p.posted_at
                        p.remote = "remote" in (info.get("remoteType") or "").lower() or \
                                   "remote" in p.location.lower()
                    except Exception:
                        pass
                p.fill_pay_from_text()
                out.append(p)
            if len(posts) < 20 or too_old >= 10:
                break
        if not queries and ok_calls == 0 and not tried_plain:
            # some sites reject keyword search (HTTP 422); fall back to the plain newest-first list
            tried_plain = True
            s.headers["Accept-Language"] = "en-US"
            queries = [""]
    if ok_calls == 0 and first_err:
        raise first_err
    return out


# ----------------------------------------------------------------- Oracle Cloud HCM (e.g. JPMorgan)
def oracle(c, s, ctx):
    host, site = c["host"], c["site"]     # jpmc.fa.oraclecloud.com, CX_1001
    base = f"https://{host}/hcmRestApi/resources/latest"
    out, ids = [], set()
    for q in ctx.level_queries:
        for offset in range(0, 200, 25):
            finder = (f'findReqs;siteNumber={site},limit=25,offset={offset},'
                      f'keyword="{q}",sortBy=POSTING_DATES_DESC')
            data = get_json(s, f"{base}/recruitingCEJobRequisitions",
                            params={"onlyData": "true", "expand": "requisitionList.secondaryLocations",
                                    "finder": finder})
            items = (data.get("items") or [{}])[0].get("requisitionList") or []
            for j in items:
                jid = str(j.get("Id"))
                if jid in ids or not ctx.title_ok(j.get("Title", "")):
                    continue
                ids.add(jid)
                p = _base(c, source="oracle", job_id=jid, title=j["Title"].strip(),
                          url=f"https://{host}/hcmUI/CandidateExperience/en/sites/{site}/job/{jid}",
                          location=j.get("PrimaryLocation", "") or "",
                          remote="remote" in (j.get("WorkplaceType") or "").lower(),
                          posted_at=(j.get("PostedDate") or "")[:10] or None,
                          extra={"check": f'{base}/recruitingCEJobRequisitionDetails?onlyData=true'
                                          f'&finder=ById;Id="{jid}",siteNumber={site}'})
                if p.posted_at:
                    try:
                        if (date.today() - date.fromisoformat(p.posted_at)).days > ctx.max_age_days:
                            continue
                    except ValueError:
                        pass
                if ctx.is_new(p):
                    try:
                        d = get_json(s, f"{base}/recruitingCEJobRequisitionDetails",
                                     params={"onlyData": "true", "expand": "all",
                                             "finder": f'ById;Id="{jid}",siteNumber={site}'})
                        it = (d.get("items") or [{}])[0]
                        p.description = "\n\n".join(html_to_text(it.get(k)) for k in (
                            "ExternalDescriptionStr", "ExternalResponsibilitiesStr",
                            "ExternalQualificationsStr", "CorporateDescriptionStr") if it.get(k))
                    except Exception:
                        pass
                p.fill_pay_from_text()
                out.append(p)
            if len(items) < 25:
                break
    return out


def check_open(role: dict, s) -> "bool | None":
    """Is this posting still up? True / False, or None when it can't be told."""
    url = (role.get("extra") or {}).get("check")
    if not url:
        return None
    try:
        r = s.get(url, timeout=20)
    except Exception:
        return None
    if r.status_code in (404, 410):
        return False
    if r.status_code != 200:
        return None
    try:
        d = r.json()
    except ValueError:
        return None
    src = role.get("source")
    if src == "workday":
        info = d.get("jobPostingInfo")
        if not info:
            return False
        return info.get("canApply", True) is not False
    if src == "oracle":
        return bool(d.get("items"))
    if src == "smartrecruiters":
        return d.get("active", True) is not False
    if src == "eightfold":
        return bool(d.get("id") or d.get("name"))
    return None


from .sources_extra import EXTRA_ADAPTERS  # noqa: E402

ADAPTERS = {
    **EXTRA_ADAPTERS,
    "greenhouse": greenhouse,
    "lever": lever,
    "ashby": ashby,
    "smartrecruiters": smartrecruiters,
    "workday": workday,
    "oracle": oracle,
}
