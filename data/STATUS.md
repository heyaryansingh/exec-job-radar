# Collector status

- Last run: 2026-11-09T13:17:35+00:00 UTC, 517s
- Companies working: 633 of 635
- New roles last run: 7; roles in feed: 1319
- Universe (all other known career sites): 5191 boards, 4337 checked in the last hour, 0 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 126, "senior titles from boards/aggregators": 22}
- Companies with open roles: 1538
- Skipped (backing off broken sites): 856; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 19 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Blackstone | 7 | 401 Client Error: Unauthorized for url: https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
