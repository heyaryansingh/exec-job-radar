# Collector status

- Last run: 2026-11-09T18:11:51+00:00 UTC, 752s
- Companies working: 633 of 635
- New roles last run: 7; roles in feed: 1353
- Universe (all other known career sites): 5194 boards, 4340 checked in the last hour, 0 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 258, "senior titles from boards/aggregators": 83}
- Companies with open roles: 1551
- Skipped (backing off broken sites): 856; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 20 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Blackstone | 7 | 401 Client Error: Unauthorized for url: https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
