# Collector status

- Last run: 2026-11-04T20:06:07+00:00 UTC, 767s
- Companies working: 632 of 633
- New roles last run: 13; roles in feed: 1516
- Universe (all other known career sites): 5058 boards, 4215 checked in the last hour, 1 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 452, "senior titles from boards/aggregators": 199}
- Companies with open roles: 1315
- Skipped (backing off broken sites): 843; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
