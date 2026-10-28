# Collector status

- Last run: 2026-10-28T21:42:10+00:00 UTC, 473s
- Companies working: 629 of 630
- New roles last run: 16; roles in feed: 2751
- Universe (all other known career sites): 4843 boards, 4023 checked in the last hour, 1 errors; 2 employer names learned; 16 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 445, "senior titles from boards/aggregators": 204}
- Companies with open roles: 968
- Skipped (backing off broken sites): 819; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
