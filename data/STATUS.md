# Collector status

- Last run: 2026-11-10T23:08:59+00:00 UTC, 487s
- Companies working: 634 of 635
- New roles last run: 16; roles in feed: 1432
- Universe (all other known career sites): 5244 boards, 4389 checked in the last hour, 0 errors; 1 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 443, "senior titles from boards/aggregators": 211}
- Companies with open roles: 1628
- Skipped (backing off broken sites): 856; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 22 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
