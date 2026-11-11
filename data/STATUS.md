# Collector status

- Last run: 2026-11-11T03:59:14+00:00 UTC, 488s
- Companies working: 634 of 635
- New roles last run: 11; roles in feed: 1389
- Universe (all other known career sites): 5255 boards, 4400 checked in the last hour, 0 errors; 0 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 448, "senior titles from boards/aggregators": 226}
- Companies with open roles: 1642
- Skipped (backing off broken sites): 855; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 23 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
