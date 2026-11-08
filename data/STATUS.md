# Collector status

- Last run: 2026-11-08T08:14:44+00:00 UTC, 432s
- Companies working: 632 of 633
- New roles last run: 1; roles in feed: 1458
- Universe (all other known career sites): 5188 boards, 4335 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 255, "senior titles from boards/aggregators": 90}
- Companies with open roles: 1528
- Skipped (backing off broken sites): 854; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 17 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
