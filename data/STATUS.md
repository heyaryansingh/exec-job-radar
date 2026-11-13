# Collector status

- Last run: 2026-11-13T02:31:28+00:00 UTC, 1066s
- Companies working: 633 of 635
- New roles last run: 4; roles in feed: 1472
- Universe (all other known career sites): 5306 boards, 4446 checked in the last hour, 789 errors; 0 employer names learned; 6 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 459, "senior titles from boards/aggregators": 225}
- Companies with open roles: 1730
- Skipped (backing off broken sites): 72; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 26 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 3 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
