# Collector status

- Last run: 2026-11-02T11:56:28+00:00 UTC, 389s
- Companies working: 632 of 633
- New roles last run: 3; roles in feed: 1304
- Universe (all other known career sites): 4975 boards, 4140 checked in the last hour, 1 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1172
- Skipped (backing off broken sites): 835; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
