# Collector status

- Last run: 2026-10-22T04:00:21+00:00 UTC, 275s
- Companies working: 510 of 511
- New roles last run: 12; roles in feed: 1854
- Universe (all other known career sites): 4720 boards, 3913 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 597
- Skipped (backing off broken sites): 807; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
