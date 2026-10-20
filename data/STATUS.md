# Collector status

- Last run: 2026-10-20T14:19:24+00:00 UTC, 327s
- Companies working: 510 of 511
- New roles last run: 5; roles in feed: 1489
- Universe (all other known career sites): 4619 boards, 3814 checked in the last hour, 1 errors; 1 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 405, "remotive": 0, "senior titles from boards/aggregators": 153}
- Companies with open roles: 470
- Skipped (backing off broken sites): 804; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anduril Industries | 1 | HTTPSConnectionPool(host='boards-api.greenhouse.io', port=443): Read timed out. (read timeout=25) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
