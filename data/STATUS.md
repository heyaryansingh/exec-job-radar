# Collector status

- Last run: 2026-11-11T02:59:01+00:00 UTC, 477s
- Companies working: 634 of 635
- New roles last run: 4; roles in feed: 1378
- Universe (all other known career sites): 5255 boards, 4400 checked in the last hour, 2 errors; 1 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1636
- Skipped (backing off broken sites): 854; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 22 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
