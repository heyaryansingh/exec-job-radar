# Collector status

- Last run: 2026-11-13T10:15:15+00:00 UTC, 671s
- Companies working: 633 of 635
- New roles last run: 6; roles in feed: 1508
- Universe (all other known career sites): 5319 boards, 4455 checked in the last hour, 10 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1739
- Skipped (backing off broken sites): 856; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 27 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
