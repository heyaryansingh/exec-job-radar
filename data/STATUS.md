# Collector status

- Last run: 2026-11-05T17:27:03+00:00 UTC, 760s
- Companies working: 632 of 633
- New roles last run: 20; roles in feed: 1595
- Universe (all other known career sites): 5097 boards, 4254 checked in the last hour, 1 errors; 4 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 436, "senior titles from boards/aggregators": 200}
- Companies with open roles: 1369
- Skipped (backing off broken sites): 843; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 12 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
