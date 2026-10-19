"""Recognize an employer career-site URL (Workday, Greenhouse, Lever, Ashby,
SmartRecruiters, Oracle) and return the board entry the collector can poll."""
from __future__ import annotations

import re
from urllib.parse import urlparse

BAD_SLUGS = {"embed", "v1", "jobs", "job", "wday", "login", "careers", "search", "api"}


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
        slug = parts[0] if parts[0] not in BAD_SLUGS else None
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


def try_parse(url: str):
    """parse() that returns None instead of raising, and rejects obviously bad entries."""
    try:
        e = parse(url or "")
    except (ValueError, IndexError):
        return None
    key = e.get("site") if e["ats"] in ("workday", "oracle") else e.get("slug")
    if not key or key.lower() in BAD_SLUGS or len(key) > 80:
        return None
    return e
