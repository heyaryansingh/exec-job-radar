# Collector status

- Last run: 2026-11-10T01:49:31+00:00 UTC, 828s
- Companies working: 633 of 635
- New roles last run: 7; roles in feed: 1279
- Universe (all other known career sites): 5210 boards, 4356 checked in the last hour, 789 errors; 0 employer names learned; 14 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 396, "senior titles from boards/aggregators": 168}
- Companies with open roles: 1577
- Skipped (backing off broken sites): 66; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 20 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| EchoStar | 1 | HTTP 503 for https://efgz-dev2.fa.us6.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobReq |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
