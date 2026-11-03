# Collector status

- Last run: 2026-11-03T00:30:20+00:00 UTC, 575s
- Companies working: 632 of 633
- New roles last run: 4; roles in feed: 1269
- Universe (all other known career sites): 4995 boards, 4160 checked in the last hour, 0 errors; 1 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1202
- Skipped (backing off broken sites): 836; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 7 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
