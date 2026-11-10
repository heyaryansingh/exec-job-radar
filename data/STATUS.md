# Collector status

- Last run: 2026-11-10T09:37:24+00:00 UTC, 440s
- Companies working: 633 of 635
- New roles last run: 1; roles in feed: 1304
- Universe (all other known career sites): 5230 boards, 4378 checked in the last hour, 2 errors; 1 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1590
- Skipped (backing off broken sites): 852; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 21 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| EchoStar | 6 | HTTP 503 for https://efgz-dev2.fa.us6.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobReq |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
