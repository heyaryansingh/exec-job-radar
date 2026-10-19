"""The universe: every public career site we know about, not just the watchlist.

Sources of boards, merged and de-duplicated against config/companies.yaml:
  - data/ats_directory.json   career sites found in the Common Crawl web archive
                              (tools/ats_directory.py), thousands of employers
  - data/auto_boards.json     career sites found automatically when a job-board result
                              (Indeed, Google Jobs, ...) links to an employer's own site

Universe boards are polled the same way as watchlist companies, oldest-checked first
within the hourly time budget, so every board is visited every few hours and the
watchlist every hour. Their company names are learned from the career site itself and
cached in data/board_names.json.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from .common import get_json

MAX_SITES_PER_WORKDAY_TENANT = 2


def identity(e: dict) -> str:
    """Stable id for a career site, independent of the company name."""
    ats = e.get("ats", "")
    if ats in ("workday", "oracle"):
        tenant = e.get("tenant") or e.get("host", "").split(".")[0]
        return f"{ats}:{e.get('host', '').lower()}:{tenant.lower()}:{e.get('site', '').lower()}"
    return f"{ats}:{str(e.get('slug', '')).lower()}"


def tenant_key(e: dict) -> str:
    """Workday/Oracle tenant (one company can run several career sites)."""
    if e.get("ats") in ("workday", "oracle"):
        return f"{e['ats']}:{(e.get('tenant') or e.get('host', '').split('.')[0]).lower()}"
    return identity(e)


def pretty(slug: str) -> str:
    s = re.sub(r"(careers?|jobs|external|ext)$", "", slug, flags=re.I)
    s = re.sub(r"[-_.]+", " ", s).strip() or slug
    return " ".join(w.upper() if len(w) <= 3 and w.isalpha() and w.lower() not in ("inc", "the") else w.capitalize()
                    for w in s.split())


def _load(p: Path, default):
    try:
        return json.loads(p.read_text())
    except Exception:
        return default


def build(data_dir: Path, watchlist: list[dict]) -> list[dict]:
    """Universe boards not already covered by the watchlist, as company dicts."""
    covered = {identity(c) for c in watchlist} | {tenant_key(c) for c in watchlist}
    names = _load(data_dir / "board_names.json", {})
    boards: list[dict] = []
    directory = _load(data_dir / "ats_directory.json", {}).get("boards", {})
    for entries in directory.values():
        boards.extend(entries)
    for e in _load(data_dir / "auto_boards.json", {}).get("boards", []):
        boards.append({**e, "seen": 10_000})  # found via a live posting: definitely real

    # keep the busiest sites of each Workday tenant (internal/test sites are rarely busy)
    per_tenant = defaultdict(list)
    for e in boards:
        per_tenant[tenant_key(e)].append(e)
    out, seen_ids = [], set()
    for tk, es in per_tenant.items():
        if tk in covered:
            continue
        es.sort(key=lambda e: -int(e.get("seen", 0)))
        limit = MAX_SITES_PER_WORKDAY_TENANT if es[0].get("ats") in ("workday", "oracle") else 1
        for e in es[:limit]:
            bid = identity(e)
            if bid in covered or bid in seen_ids:
                continue
            seen_ids.add(bid)
            c = {k: v for k, v in e.items() if k not in ("seen", "name")}
            fallback = e.get("name") or pretty(c.get("slug") or c.get("tenant") or c.get("host", "").split(".")[0])
            c.update(name=names.get(bid) or fallback, tier=3, sector="", universe=True, board=bid,
                     named=bid in names or bool(e.get("name")))
            out.append(c)
    return out


# ------------------------------------------------------------------ learning names
def resolve_name(c: dict, s, sample_detail: dict | None = None) -> str | None:
    """Ask the career site for the employer's real name (one call per board, cached)."""
    try:
        if c["ats"] == "greenhouse":
            d = get_json(s, f"https://boards-api.greenhouse.io/v1/boards/{c['slug']}", tries=2)
            return clean_name(d.get("name"))
        if c["ats"] == "ashby":
            q = ("query ApiOrganizationFromHostedJobsPageName($organizationHostedJobsPageName: String!) "
                 "{ organization: organizationFromHostedJobsPageName(organizationHostedJobsPageName: "
                 "$organizationHostedJobsPageName) { name } }")
            d = get_json(s, "https://jobs.ashbyhq.com/api/non-user-graphql", method="POST", tries=2,
                         params={"op": "ApiOrganizationFromHostedJobsPageName"},
                         body={"operationName": "ApiOrganizationFromHostedJobsPageName",
                               "variables": {"organizationHostedJobsPageName": c["slug"]}, "query": q})
            return clean_name(((d.get("data") or {}).get("organization") or {}).get("name"))
        if c["ats"] == "workday" and sample_detail:
            org = (sample_detail.get("hiringOrganization") or {}).get("name")
            return org.strip() if org else None
    except Exception:
        return None
    return None


def clean_name(n: str | None) -> str | None:
    if not n:
        return None
    n = re.sub(r"^(careers|jobs|work)\s+(at|with)\s+", "", n.strip(), flags=re.I)
    n = re.sub(r"\s*[-|:]?\s*(careers?|jobs|job board|hiring)$", "", n, flags=re.I).strip()
    return n or None


def save_names(data_dir: Path, learned: dict):
    if not learned:
        return
    p = data_dir / "board_names.json"
    names = _load(p, {})
    names.update(learned)
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(names, indent=0, sort_keys=True))
    tmp.replace(p)


def add_auto_boards(data_dir: Path, found: list[dict]) -> int:
    """Remember employer career sites seen in job-board results; returns how many are new."""
    if not found:
        return 0
    p = data_dir / "auto_boards.json"
    cur = _load(p, {"boards": []})
    have = {identity(e) for e in cur["boards"]}
    added = 0
    for e in found:
        if identity(e) not in have:
            have.add(identity(e))
            cur["boards"].append(e)
            added += 1
    if added:
        tmp = p.with_suffix(".tmp")
        tmp.write_text(json.dumps(cur, indent=0, sort_keys=True))
        tmp.replace(p)
    return added
