# Collector status

- Last run: 2026-11-11T01:59:06+00:00 UTC, 482s
- Companies working: 634 of 635
- New roles last run: 20; roles in feed: 1374
- Universe (all other known career sites): 5247 boards, 4392 checked in the last hour, 0 errors; 0 employer names learned; 9 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 452, "senior titles from boards/aggregators": 230}
- Companies with open roles: 1635
- Skipped (backing off broken sites): 856; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 22 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
