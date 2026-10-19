"""One-call JSearch check: is the key valid and subscribed, and what comes back?

    RAPIDAPI_KEY=... python tools/test_jsearch.py data/test_reports/jsearch.md
"""
import collections
import os
import sys
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from collector.filters import Rules  # noqa: E402

out = Path(sys.argv[1])
key = os.environ.get("RAPIDAPI_KEY", "")
lines = ["# JSearch test (1 API call)", ""]
if not key:
    lines.append("RAPIDAPI_KEY is not set for this workflow.")
else:
    params = {"query": "vice president technology in USA", "page": 1, "num_pages": 1,
              "date_posted": "week", "country": "us"}
    hdr = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": "jsearch.p.rapidapi.com"}
    # the API's search path has changed over time; try the known variants (404s are free)
    for path in ("/search", "/search-v2", "/v2/search", "/search/v2", "/job-search", "/jobs/search", "/v1/search"):
        r = requests.get("https://jsearch.p.rapidapi.com" + path, timeout=40, headers=hdr, params=params)
        lines.append(f"- {path}: HTTP {r.status_code} {r.text[:90]!r}")
        if r.status_code != 404:
            break
    lines.append(f"HTTP {r.status_code} via {path}")
    for h in ("x-ratelimit-requests-limit", "x-ratelimit-requests-remaining"):
        if h in r.headers:
            lines.append(f"- {h}: {r.headers[h]}")
    try:
        d = r.json()
    except ValueError:
        d = {}
    if r.status_code != 200:
        lines += ["", "Response:", "```", r.text[:600], "```"]
    else:
        data = d.get("data") or []
        rules = Rules(yaml.safe_load((ROOT / "config" / "search.yaml").read_text()))
        pubs = collections.Counter(j.get("job_publisher") for j in data)
        passing = [j for j in data if rules.title_ok(j.get("job_title") or "")]
        lines += [f"- results: {len(data)}", f"- senior titles passing the rules: {len(passing)}",
                  "- publishers: " + ", ".join(f"{k} {v}" for k, v in pubs.most_common()), "",
                  "| Employer | Title | Via | Apply link |", "|---|---|---|---|"]
        for j in data[:15]:
            lines.append(f"| {j.get('employer_name')} | {j.get('job_title')} | {j.get('job_publisher')} | "
                         f"{(j.get('job_apply_link') or '')[:80]} |")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(lines) + "\n")
print("\n".join(lines[:8]))
