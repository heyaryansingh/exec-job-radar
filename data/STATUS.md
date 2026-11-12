# Collector status

- Last run: 2026-11-12T22:35:33+00:00 UTC, 725s
- Companies working: 634 of 635
- New roles last run: 24; roles in feed: 1605
- Universe (all other known career sites): 5299 boards, 4440 checked in the last hour, 1 errors; 0 employer names learned; 7 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 463, "senior titles from boards/aggregators": 228}
- Companies with open roles: 1721
- Skipped (backing off broken sites): 859; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 26 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
