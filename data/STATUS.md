# Collector status

- Last run: 2026-11-03T15:25:39+00:00 UTC, 760s
- Companies working: 632 of 633
- New roles last run: 7; roles in feed: 1350
- Universe (all other known career sites): 5019 boards, 4181 checked in the last hour, 1 errors; 1 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 403, "senior titles from boards/aggregators": 161}
- Companies with open roles: 1236
- Skipped (backing off broken sites): 838; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 8 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
