# Collector status

- Last run: 2026-10-20T11:18:11+00:00 UTC, 257s
- Companies working: 510 of 511
- New roles last run: 15; roles in feed: 1467
- Universe (all other known career sites): 4617 boards, 3813 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 400, "senior titles from boards/aggregators": 153}
- Companies with open roles: 466
- Skipped (backing off broken sites): 804; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
