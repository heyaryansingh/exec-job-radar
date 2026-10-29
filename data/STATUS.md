# Collector status

- Last run: 2026-10-29T20:53:30+00:00 UTC, 464s
- Companies working: 628 of 630
- New roles last run: 19; roles in feed: 2582
- Universe (all other known career sites): 4880 boards, 4056 checked in the last hour, 0 errors; 3 employer names learned; 11 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 444, "senior titles from boards/aggregators": 198}
- Companies with open roles: 1025
- Skipped (backing off broken sites): 824; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anduril Industries | 1 | HTTPSConnectionPool(host='boards-api.greenhouse.io', port=443): Read timed out. (read timeout=25) |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
