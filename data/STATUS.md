# Collector status

- Last run: 2026-10-31T15:28:33+00:00 UTC, 639s
- Companies working: 628 of 630
- New roles last run: 0; roles in feed: 1600
- Universe (all other known career sites): 4951 boards, 4116 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1134
- Skipped (backing off broken sites): 836; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |
| Peak6 | 1 | HTTP 429 for https://peak6group.wd1.myworkdayjobs.com/wday/cxs/peak6group/apexfintechsolutions/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
