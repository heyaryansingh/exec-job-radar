# Collector status

- Last run: 2026-10-25T00:43:43+00:00 UTC, 260s
- Companies working: 509 of 511
- New roles last run: 3; roles in feed: 2239
- Universe (all other known career sites): 4838 boards, 3594 checked in the last hour, 0 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 336, "senior titles from boards/aggregators": 131}
- Companies with open roles: 780
- Skipped (backing off broken sites): 1245; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 7 | Expecting value: line 1 column 1 (char 0) |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
