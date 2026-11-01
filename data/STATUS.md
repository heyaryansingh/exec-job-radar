# Collector status

- Last run: 2026-11-01T04:55:09+00:00 UTC, 399s
- Companies working: 629 of 630
- New roles last run: 0; roles in feed: 1452
- Universe (all other known career sites): 4973 boards, 4139 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1158
- Skipped (backing off broken sites): 832; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
