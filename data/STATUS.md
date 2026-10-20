# Collector status

- Last run: 2026-10-20T06:08:59+00:00 UTC, 263s
- Companies working: 509 of 511
- New roles last run: 40; roles in feed: 1362
- Universe (all other known career sites): 4614 boards, 3810 checked in the last hour, 4 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 394, "remotive": 0, "senior titles from boards/aggregators": 151}
- Companies with open roles: 457
- Skipped (backing off broken sites): 800; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
