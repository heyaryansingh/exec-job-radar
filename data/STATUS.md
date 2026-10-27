# Collector status

- Last run: 2026-10-27T11:49:33+00:00 UTC, 420s
- Companies working: 629 of 630
- New roles last run: 1; roles in feed: 2455
- Universe (all other known career sites): 4791 boards, 3976 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 408, "senior titles from boards/aggregators": 187}
- Companies with open roles: 872
- Skipped (backing off broken sites): 815; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
