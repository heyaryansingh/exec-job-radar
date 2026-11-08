# Collector status

- Last run: 2026-11-08T02:24:20+00:00 UTC, 421s
- Companies working: 632 of 633
- New roles last run: 0; roles in feed: 1439
- Universe (all other known career sites): 5181 boards, 4328 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1519
- Skipped (backing off broken sites): 852; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 17 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
