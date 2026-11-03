# Collector status

- Last run: 2026-11-03T18:05:24+00:00 UTC, 814s
- Companies working: 632 of 633
- New roles last run: 9; roles in feed: 1376
- Universe (all other known career sites): 5019 boards, 4181 checked in the last hour, 0 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 411, "senior titles from boards/aggregators": 177}
- Companies with open roles: 1245
- Skipped (backing off broken sites): 839; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 8 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
