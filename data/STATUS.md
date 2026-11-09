# Collector status

- Last run: 2026-11-09T06:26:40+00:00 UTC, 478s
- Companies working: 633 of 635
- New roles last run: 1; roles in feed: 1311
- Universe (all other known career sites): 5189 boards, 4336 checked in the last hour, 2 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 125, "senior titles from boards/aggregators": 37}
- Companies with open roles: 1537
- Skipped (backing off broken sites): 853; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 19 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Blackstone | 6 | 401 Client Error: Unauthorized for url: https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
