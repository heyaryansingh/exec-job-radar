# Collector status

- Last run: 2026-10-31T00:09:08+00:00 UTC, 673s
- Companies working: 630 of 630
- New roles last run: 4; roles in feed: 1536
- Universe (all other known career sites): 4929 boards, 4098 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1092
- Skipped (backing off broken sites): 831; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anduril Industries | 1 | HTTPSConnectionPool(host='boards-api.greenhouse.io', port=443): Read timed out. (read timeout=25) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
