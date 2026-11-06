# Collector status

- Last run: 2026-11-06T20:27:03+00:00 UTC, 672s
- Companies working: 630 of 633
- New roles last run: 13; roles in feed: 1698
- Universe (all other known career sites): 5148 boards, 4300 checked in the last hour, 1 errors; 1 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 461, "senior titles from boards/aggregators": 209}
- Companies with open roles: 1457
- Skipped (backing off broken sites): 848; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 14 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Availity | 1 | HTTP 500 for https://availity.wd1.myworkdayjobs.com/wday/cxs/availity/Availity_Careers_US/jobs |
| Marvell | 1 | HTTPSConnectionPool(host='marvell.wd1.myworkdayjobs.com', port=443): Read timed out. (read timeout=2 |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
