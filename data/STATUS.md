# Collector status

- Last run: 2026-11-08T15:23:01+00:00 UTC, 422s
- Companies working: 634 of 635
- New roles last run: 0; roles in feed: 1458
- Universe (all other known career sites): 5188 boards, 4335 checked in the last hour, 0 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 192, "senior titles from boards/aggregators": 55}
- Companies with open roles: 1529
- Skipped (backing off broken sites): 854; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 18 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
