# Collector status

- Last run: 2026-11-09T21:00:47+00:00 UTC, 678s
- Companies working: 633 of 635
- New roles last run: 20; roles in feed: 1397
- Universe (all other known career sites): 5196 boards, 4342 checked in the last hour, 1 errors; 2 employer names learned; 14 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 331, "senior titles from boards/aggregators": 115}
- Companies with open roles: 1559
- Skipped (backing off broken sites): 855; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 20 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Blackstone | 7 | 401 Client Error: Unauthorized for url: https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
