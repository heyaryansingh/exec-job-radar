"""Build a directory of public career sites from the Common Crawl index.

Common Crawl (commoncrawl.org) is a free public archive of the web with an open index
API that does not block automated use. One pass over its index lists every Workday,
Greenhouse, Lever, Ashby and Oracle career site it has crawled, which covers thousands
of employers. tools/discover.py matches company names against this directory.

    python tools/ats_directory.py            # build/refresh data/ats_directory.json
    python tools/ats_directory.py --max-pages 20   # quick partial build for testing
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from add_company import parse  # noqa: E402
from collector.common import session  # noqa: E402

OUT = ROOT / "data" / "ats_directory.json"
INDEX = "https://index.commoncrawl.org"

# (url pattern, optional filter) per career-site system
PATTERNS = [
    ("*.myworkdayjobs.com", None),
    ("*.myworkdaysite.com", None),
    ("boards.greenhouse.io/*", None),
    ("job-boards.greenhouse.io/*", None),
    ("jobs.lever.co/*", None),
    ("jobs.ashbyhq.com/*", None),
    ("*.oraclecloud.com", "~url:.*CandidateExperience/[a-z]{2}/sites/.*"),
]
BAD_SITES = {"", "wday", "job", "jobs", "robots.txt", "favicon.ico", "login", "embed", "v1",
             "sitemap.xml", "assets", "static"}


def _get(s, url, params, tries=5):
    for i in range(tries):
        try:
            r = s.get(url, params=params, timeout=90)
            if r.status_code == 200:
                return r
            if r.status_code == 404:  # no captures for this pattern
                return None
        except Exception:
            pass
        time.sleep(5 * (i + 1))  # the index is busy at times; back off
    return None


def crawls(s, n: int) -> list[str]:
    r = _get(s, f"{INDEX}/collinfo.json", None)
    if not r:
        raise RuntimeError("Common Crawl index unreachable")
    return [c["cdx-api"] for c in r.json()[:n]]


def harvest(api: str, pattern: str, flt, max_pages: int, log) -> Counter:
    s = session()
    s.headers["Accept"] = "*/*"
    base = {"url": pattern, "output": "json", "fl": "url"}
    if flt:
        base["filter"] = flt
    r = _get(s, api, {**base, "showNumPages": "true"})
    if not r:
        return Counter()
    try:
        pages = int(r.json().get("pages", 0))
    except ValueError:
        pages = 0
    pages = min(pages, max_pages)
    log(f"  {pattern} @ {api.rsplit('/', 1)[-1]}: {pages} pages")
    found = Counter()

    def one(p):
        rr = _get(s, api, {**base, "page": p})
        got = Counter()
        if not rr:
            return got
        for line in rr.text.splitlines():
            try:
                u = json.loads(line)["url"]
            except Exception:
                continue
            try:
                e = parse(u)
            except ValueError:
                continue
            key = e.get("site") if e["ats"] in ("workday", "oracle") else e.get("slug")
            if not key or key.lower() in BAD_SITES or len(key) > 80:
                continue
            got[json.dumps(e, sort_keys=True)] += 1
        return got

    with ThreadPoolExecutor(max_workers=3) as ex:
        for got in ex.map(one, range(pages)):
            found.update(got)
    return found


def build(max_pages: int, n_crawls: int, log=print) -> dict:
    s = session()
    s.headers["Accept"] = "*/*"
    apis = crawls(s, n_crawls)
    counts: Counter = Counter()
    for api in apis:
        for pattern, flt in PATTERNS:
            counts.update(harvest(api, pattern, flt, max_pages, log))
    # keep, per board, how often it was seen (more captures = more likely the main site)
    out = defaultdict(list)
    for k, n in counts.most_common():
        e = json.loads(k)
        e["seen"] = n
        out[e["ats"]].append(e)
    d = {"built": datetime.now(timezone.utc).isoformat(timespec="seconds"),
         "crawls": [a.rsplit("/", 1)[-1] for a in apis],
         "boards": dict(out)}
    log("directory: " + ", ".join(f"{k}={len(v)}" for k, v in out.items()))
    return d


def load(max_age_days: int = 30, **kw) -> dict:
    """Return the cached directory, rebuilding it when missing or old."""
    if OUT.exists():
        try:
            d = json.loads(OUT.read_text())
            age = datetime.now(timezone.utc) - datetime.fromisoformat(d["built"])
            if age.days < max_age_days and d.get("boards"):
                return d
        except Exception:
            pass
    d = build(**kw)
    if d.get("boards"):
        OUT.parent.mkdir(exist_ok=True)
        tmp = OUT.with_suffix(".tmp")
        tmp.write_text(json.dumps(d, separators=(",", ":")))
        tmp.replace(OUT)
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-pages", type=int, default=400, help="per pattern per crawl")
    ap.add_argument("--crawls", type=int, default=2)
    a = ap.parse_args()
    if OUT.exists():
        OUT.unlink()
    load(max_pages=a.max_pages, n_crawls=a.crawls)


if __name__ == "__main__":
    main()
