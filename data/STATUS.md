# Collector status

- Last run: 2026-11-11T11:39:46+00:00 UTC, 492s
- Companies working: 634 of 635
- New roles last run: 4; roles in feed: 1408
- Universe (all other known career sites): 5265 boards, 4409 checked in the last hour, 1 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 453, "senior titles from boards/aggregators": 228}
- Companies with open roles: 1649
- Skipped (backing off broken sites): 856; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 23 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
