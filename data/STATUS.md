# Collector status

- Last run: 2026-10-24T02:26:50+00:00 UTC, 507s
- Companies working: 509 of 511
- New roles last run: 0; roles in feed: 2193
- Universe (all other known career sites): 4805 boards, 3992 checked in the last hour, 1 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 755
- Skipped (backing off broken sites): 812; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 3 | Expecting value: line 1 column 1 (char 0) |
| BNY | 1 | HTTP 503 for https://eofe.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisit |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
