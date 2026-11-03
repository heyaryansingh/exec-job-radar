# Collector status

- Last run: 2026-11-03T07:20:44+00:00 UTC, 580s
- Companies working: 632 of 633
- New roles last run: 0; roles in feed: 1319
- Universe (all other known career sites): 5010 boards, 4173 checked in the last hour, 3 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1231
- Skipped (backing off broken sites): 835; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 8 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
