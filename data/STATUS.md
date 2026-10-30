# Collector status

- Last run: 2026-10-30T14:15:49+00:00 UTC, 548s
- Companies working: 629 of 630
- New roles last run: 6; roles in feed: 1848
- Universe (all other known career sites): 4911 boards, 4083 checked in the last hour, 2 errors; 3 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 461, "senior titles from boards/aggregators": 197}
- Companies with open roles: 1060
- Skipped (backing off broken sites): 826; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
