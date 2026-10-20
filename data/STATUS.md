# Collector status

- Last run: 2026-10-20T07:27:41+00:00 UTC, 243s
- Companies working: 510 of 511
- New roles last run: 26; roles in feed: 1398
- Universe (all other known career sites): 4614 boards, 3810 checked in the last hour, 3 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 394, "senior titles from boards/aggregators": 150}
- Companies with open roles: 459
- Skipped (backing off broken sites): 801; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
