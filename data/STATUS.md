# Collector status

- Last run: 2026-11-04T06:33:01+00:00 UTC, 627s
- Companies working: 631 of 633
- New roles last run: 5; roles in feed: 1445
- Universe (all other known career sites): 5047 boards, 4209 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1292
- Skipped (backing off broken sites): 837; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 9 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Shield AI | 1 | HTTP 500 for https://api.lever.co/v0/postings/shieldai |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
