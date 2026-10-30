# Collector status

- Last run: 2026-10-30T23:57:27+00:00 UTC, 614s
- Companies working: 629 of 630
- New roles last run: 10; roles in feed: 1963
- Universe (all other known career sites): 4923 boards, 4092 checked in the last hour, 0 errors; 1 employer names learned; 7 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 474, "senior titles from boards/aggregators": 214}
- Companies with open roles: 1092
- Skipped (backing off broken sites): 831; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anduril Industries | 1 | HTTPSConnectionPool(host='boards-api.greenhouse.io', port=443): Read timed out. (read timeout=25) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
