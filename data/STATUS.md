# Collector status

- Last run: 2026-11-10T18:20:27+00:00 UTC, 597s
- Companies working: 634 of 635
- New roles last run: 7; roles in feed: 1368
- Universe (all other known career sites): 5234 boards, 4379 checked in the last hour, 0 errors; 0 employer names learned; 4 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 425, "senior titles from boards/aggregators": 189}
- Companies with open roles: 1604
- Skipped (backing off broken sites): 856; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 22 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
