# Collector status

- Last run: 2026-11-04T09:24:41+00:00 UTC, 719s
- Companies working: 632 of 633
- New roles last run: 0; roles in feed: 1449
- Universe (all other known career sites): 5049 boards, 4210 checked in the last hour, 6 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1293
- Skipped (backing off broken sites): 834; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
