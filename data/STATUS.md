# Collector status

- Last run: 2026-11-05T20:18:04+00:00 UTC, 805s
- Companies working: 632 of 633
- New roles last run: 17; roles in feed: 1633
- Universe (all other known career sites): 5100 boards, 4257 checked in the last hour, 1 errors; 1 employer names learned; 8 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 443, "senior titles from boards/aggregators": 212}
- Companies with open roles: 1384
- Skipped (backing off broken sites): 843; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 12 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
