# Collector status

- Last run: 2026-11-10T11:27:35+00:00 UTC, 441s
- Companies working: 633 of 635
- New roles last run: 6; roles in feed: 1310
- Universe (all other known career sites): 5230 boards, 4377 checked in the last hour, 2 errors; 1 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 421, "senior titles from boards/aggregators": 188}
- Companies with open roles: 1591
- Skipped (backing off broken sites): 853; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 21 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| EchoStar | 6 | HTTP 503 for https://efgz-dev2.fa.us6.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobReq |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
