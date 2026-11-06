# Collector status

- Last run: 2026-11-06T18:34:50+00:00 UTC, 543s
- Companies working: 632 of 633
- New roles last run: 5; roles in feed: 1679
- Universe (all other known career sites): 5148 boards, 4300 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1448
- Skipped (backing off broken sites): 849; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 14 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
