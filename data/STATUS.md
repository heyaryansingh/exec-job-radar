# Collector status

- Last run: 2026-11-08T06:14:48+00:00 UTC, 439s
- Companies working: 632 of 633
- New roles last run: 2; roles in feed: 1457
- Universe (all other known career sites): 5186 boards, 4333 checked in the last hour, 1 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 262, "senior titles from boards/aggregators": 96}
- Companies with open roles: 1528
- Skipped (backing off broken sites): 853; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 17 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
