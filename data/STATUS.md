# Collector status

- Last run: 2026-10-24T16:03:29+00:00 UTC, 275s
- Companies working: 509 of 511
- New roles last run: 0; roles in feed: 2222
- Universe (all other known career sites): 4826 boards, 3582 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 769
- Skipped (backing off broken sites): 1245; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
