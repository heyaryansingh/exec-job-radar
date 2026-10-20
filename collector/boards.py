"""Broad job-board sweep (Indeed + Google Jobs) via the open-source python-jobspy
library. Catches employers that are not on the company watchlist. Optional: if the
library is missing or a board blocks the request, the run continues without it.

LinkedIn is deliberately not scraped (its terms forbid it); LinkedIn coverage comes
from the job-alert emails the Claude run reads instead.
"""
from __future__ import annotations

import math

from .atsurl import try_parse
from .common import Posting


def _clean(v):
    if v is None:
        return None
    try:
        if isinstance(v, float) and math.isnan(v):
            return None
    except Exception:
        pass
    return v


def sweep(cfg: dict, ctx, log, links: list | None = None, counts: dict | None = None) -> list[Posting]:
    """Search job boards. Every result that links to an employer career site (any title,
    not only matches) is appended to `links`, so the universe grows on its own."""
    b = cfg.get("boards") or {}
    if not b.get("enabled", True):
        return []
    try:
        from jobspy import scrape_jobs  # type: ignore
    except Exception as e:  # library not installed
        log(f"boards: jobspy unavailable ({e}); skipping")
        return []

    out: list[Posting] = []
    sites = b.get("sites", ["indeed", "google"])
    hours = int(b.get("hours_old", 24))
    per = int(b.get("results_per_search", 50))
    searches = [(t, l, hours, None) for t in b.get("search_terms", []) for l in b.get("locations", ["United States"])]
    for f in cfg.get("focus_locations") or []:
        if f.get("board_location"):
            searches += [(t, f["board_location"], int(f.get("board_hours_old", hours)), f.get("board_radius_miles"))
                         for t in f.get("board_terms") or []]
    for term, loc, hrs, radius in searches:
        try:
            kw = {"distance": int(radius)} if radius else {}
            df = scrape_jobs(site_name=sites, search_term=term,
                             google_search_term=f"{term} jobs near {loc} since yesterday",
                             location=loc, results_wanted=per, hours_old=hrs,
                             country_indeed="USA", description_format="markdown",
                             verbose=0, **kw)
        except Exception as e:
            log(f"boards: '{term}' @ {loc} failed: {e}")
            continue
        log(f"boards: '{term}' @ {loc} -> {len(df)} results " + str(dict(df["site"].value_counts())) if len(df) else
            f"boards: '{term}' -> 0 results")
        for row in df.to_dict("records"):
            site = str(row.get("site", "web"))
            if counts is not None:
                counts[site] = counts.get(site, 0) + 1
            if links is not None:
                e = try_parse(str(_clean(row.get("job_url_direct")) or ""))
                if e:
                    e["name"] = str(_clean(row.get("company")) or "") or None
                    links.append(e)
            title = str(_clean(row.get("title")) or "")
            if not ctx.title_ok(title):
                continue
            company = str(_clean(row.get("company")) or "Unknown")
            p = Posting(source=f"board-{row.get('site', 'web')}", company=company,
                        job_id=str(_clean(row.get("id")) or row.get("job_url")), title=title.strip(),
                        url=str(_clean(row.get("job_url_direct")) or _clean(row.get("job_url")) or ""),
                        location=str(_clean(row.get("location")) or ""),
                        remote=bool(_clean(row.get("is_remote"))),
                        posted_at=str(_clean(row.get("date_posted")) or "")[:10] or None,
                        description=str(_clean(row.get("description")) or ""),
                        tier=3)
            interval = _clean(row.get("interval"))
            hi, lo = _clean(row.get("max_amount")), _clean(row.get("min_amount"))
            if hi and interval in ("yearly", None):
                p.pay_max, p.pay_min = int(hi), int(lo) if lo else None
                p.pay_text = f"${p.pay_min or '?'}-${p.pay_max} (board)"
            elif hi and interval == "hourly":
                p.pay_max, p.pay_min = int(hi * 2080), int(lo * 2080) if lo else None
            p.fill_pay_from_text()
            out.append(p)
    return out
