# Collector status

- Last run: 2026-11-01T15:20:52+00:00 UTC, 411s
- Companies working: 632 of 633
- New roles last run: 1; roles in feed: 1458
- Universe (all other known career sites): 4973 boards, 4139 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 203, "senior titles from boards/aggregators": 56}
- Companies with open roles: 1160
- Skipped (backing off broken sites): 834; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
