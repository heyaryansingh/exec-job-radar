# Collector status

- Last run: 2026-11-16T03:07:47+00:00 UTC, 413s
- Companies working: 632 of 636
- New roles last run: 0; roles in feed: 1170
- Universe (all other known career sites): 5360 boards, 3777 checked in the last hour, 29 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1802
- Skipped (backing off broken sites): 1556; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| FMC | 1 | HTTP 429 for https://fmc.wd12.myworkdayjobs.com/wday/cxs/fmc/FMC/jobs |
| Tapestry | 1 | HTTP 429 for https://tapestry.wd108.myworkdayjobs.com/wday/cxs/tapestry/Tapestry_Careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
