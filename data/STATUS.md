# Collector status

- Last run: 2026-10-25T14:14:56+00:00 UTC, 296s
- Companies working: 629 of 630
- New roles last run: 0; roles in feed: 2292
- Universe (all other known career sites): 4728 boards, 3539 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 172, "senior titles from boards/aggregators": 52}
- Companies with open roles: 793
- Skipped (backing off broken sites): 1189; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
