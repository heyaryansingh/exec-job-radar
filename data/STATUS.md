# Collector status

- Last run: 2026-10-21T17:20:58+00:00 UTC, 338s
- Companies working: 509 of 511
- New roles last run: 20; roles in feed: 1726
- Universe (all other known career sites): 4687 boards, 3880 checked in the last hour, 0 errors; 1 employer names learned; 15 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 427, "senior titles from boards/aggregators": 177}
- Companies with open roles: 554
- Skipped (backing off broken sites): 807; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anduril Industries | 1 | HTTPSConnectionPool(host='boards-api.greenhouse.io', port=443): Read timed out. (read timeout=25) |
| Home Depot | 1 | sitemap: no job URLs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
