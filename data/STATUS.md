# Collector status

- Last run: 2026-11-04T17:16:59+00:00 UTC, 819s
- Companies working: 632 of 633
- New roles last run: 12; roles in feed: 1485
- Universe (all other known career sites): 5054 boards, 4211 checked in the last hour, 3 errors; 2 employer names learned; 4 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 455, "senior titles from boards/aggregators": 188}
- Companies with open roles: 1305
- Skipped (backing off broken sites): 841; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
