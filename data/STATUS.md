# Collector status

- Last run: 2026-11-10T20:10:48+00:00 UTC, 604s
- Companies working: 634 of 635
- New roles last run: 6; roles in feed: 1387
- Universe (all other known career sites): 5237 boards, 4382 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1608
- Skipped (backing off broken sites): 854; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 22 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
