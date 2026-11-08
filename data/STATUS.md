# Collector status

- Last run: 2026-11-08T03:24:46+00:00 UTC, 444s
- Companies working: 632 of 633
- New roles last run: 1; roles in feed: 1440
- Universe (all other known career sites): 5181 boards, 4328 checked in the last hour, 0 errors; 0 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 318, "senior titles from boards/aggregators": 125}
- Companies with open roles: 1520
- Skipped (backing off broken sites): 854; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 17 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
