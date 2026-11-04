# Collector status

- Last run: 2026-11-04T22:05:42+00:00 UTC, 739s
- Companies working: 632 of 633
- New roles last run: 17; roles in feed: 1544
- Universe (all other known career sites): 5060 boards, 4217 checked in the last hour, 0 errors; 3 employer names learned; 6 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 448, "senior titles from boards/aggregators": 206}
- Companies with open roles: 1325
- Skipped (backing off broken sites): 844; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
