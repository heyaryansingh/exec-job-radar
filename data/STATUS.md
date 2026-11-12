# Collector status

- Last run: 2026-11-12T09:02:37+00:00 UTC, 596s
- Companies working: 634 of 635
- New roles last run: 2; roles in feed: 1487
- Universe (all other known career sites): 5286 boards, 4427 checked in the last hour, 3 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1690
- Skipped (backing off broken sites): 857; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 25 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
