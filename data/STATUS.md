# Collector status

- Last run: 2026-10-23T14:54:19+00:00 UTC, 401s
- Companies working: 510 of 511
- New roles last run: 12; roles in feed: 2079
- Universe (all other known career sites): 4773 boards, 3960 checked in the last hour, 1 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 451, "senior titles from boards/aggregators": 204}
- Companies with open roles: 705
- Skipped (backing off broken sites): 812; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anduril Industries | 1 | HTTPSConnectionPool(host='boards-api.greenhouse.io', port=443): Read timed out. (read timeout=25) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
