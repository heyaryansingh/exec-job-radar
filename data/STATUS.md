# Collector status

- Last run: 2026-11-04T10:25:01+00:00 UTC, 730s
- Companies working: 632 of 633
- New roles last run: 1; roles in feed: 1455
- Universe (all other known career sites): 5051 boards, 4211 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1293
- Skipped (backing off broken sites): 839; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
