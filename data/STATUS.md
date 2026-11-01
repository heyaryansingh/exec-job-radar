# Collector status

- Last run: 2026-11-01T03:05:49+00:00 UTC, 445s
- Companies working: 629 of 630
- New roles last run: 19; roles in feed: 1452
- Universe (all other known career sites): 4967 boards, 4134 checked in the last hour, 0 errors; 0 employer names learned; 8 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 297, "jsearch": 31, "senior titles from boards/aggregators": 147}
- Companies with open roles: 1157
- Skipped (backing off broken sites): 833; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
