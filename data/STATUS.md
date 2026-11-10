# Collector status

- Last run: 2026-11-10T08:37:39+00:00 UTC, 459s
- Companies working: 633 of 635
- New roles last run: 3; roles in feed: 1303
- Universe (all other known career sites): 5228 boards, 4376 checked in the last hour, 2 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 409, "senior titles from boards/aggregators": 182}
- Companies with open roles: 1589
- Skipped (backing off broken sites): 852; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 21 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| EchoStar | 6 | HTTP 503 for https://efgz-dev2.fa.us6.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobReq |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
