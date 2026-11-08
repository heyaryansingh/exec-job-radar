# Collector status

- Last run: 2026-11-08T17:55:23+00:00 UTC, 440s
- Companies working: 633 of 635
- New roles last run: 1; roles in feed: 1461
- Universe (all other known career sites): 5189 boards, 4336 checked in the last hour, 1 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 166, "senior titles from boards/aggregators": 51}
- Companies with open roles: 1530
- Skipped (backing off broken sites): 853; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 18 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Blackstone | 2 | 401 Client Error: Unauthorized for url: https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
