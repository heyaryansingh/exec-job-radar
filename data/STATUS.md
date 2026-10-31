# Collector status

- Last run: 2026-10-31T04:45:25+00:00 UTC, 478s
- Companies working: 628 of 630
- New roles last run: 8; roles in feed: 1588
- Universe (all other known career sites): 4940 boards, 4107 checked in the last hour, 0 errors; 0 employer names learned; 8 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 461, "senior titles from boards/aggregators": 199}
- Companies with open roles: 1125
- Skipped (backing off broken sites): 833; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 4 | Expecting value: line 1 column 1 (char 0) |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
