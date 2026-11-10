# Collector status

- Last run: 2026-11-10T16:21:02+00:00 UTC, 629s
- Companies working: 633 of 635
- New roles last run: 12; roles in feed: 1341
- Universe (all other known career sites): 5233 boards, 4378 checked in the last hour, 2 errors; 1 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 419, "senior titles from boards/aggregators": 182}
- Companies with open roles: 1595
- Skipped (backing off broken sites): 855; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 22 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| EchoStar | 6 | HTTP 503 for https://efgz-dev2.fa.us6.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobReq |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
