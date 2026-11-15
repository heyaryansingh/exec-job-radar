# Collector status

- Last run: 2026-11-15T17:50:47+00:00 UTC, 339s
- Companies working: 633 of 636
- New roles last run: 1; roles in feed: 1345
- Universe (all other known career sites): 5356 boards, 3830 checked in the last hour, 0 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 188, "senior titles from boards/aggregators": 47}
- Companies with open roles: 1798
- Skipped (backing off broken sites): 1528; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 31 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| R1 RCM | 1 | HTTP 429 for https://r1rcm.wd1.myworkdayjobs.com/wday/cxs/r1rcm/R1RCM/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
