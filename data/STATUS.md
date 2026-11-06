# Collector status

- Last run: 2026-11-06T21:25:08+00:00 UTC, 549s
- Companies working: 630 of 633
- New roles last run: 23; roles in feed: 1718
- Universe (all other known career sites): 5153 boards, 4304 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1459
- Skipped (backing off broken sites): 848; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 14 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Marvell | 2 | HTTP 500 for https://marvell.wd1.myworkdayjobs.com/wday/cxs/marvell/MarvellCareers/jobs |
| R1 RCM | 1 | HTTP 502 for https://r1rcm.wd1.myworkdayjobs.com/wday/cxs/r1rcm/R1RCM/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
