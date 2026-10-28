# Collector status

- Last run: 2026-10-28T00:21:06+00:00 UTC, 469s
- Companies working: 629 of 630
- New roles last run: 10; roles in feed: 2583
- Universe (all other known career sites): 4808 boards, 3993 checked in the last hour, 0 errors; 1 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 421, "senior titles from boards/aggregators": 178}
- Companies with open roles: 905
- Skipped (backing off broken sites): 815; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anduril Industries | 1 | HTTPSConnectionPool(host='boards-api.greenhouse.io', port=443): Read timed out. (read timeout=25) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
