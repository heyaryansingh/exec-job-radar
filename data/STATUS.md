# Collector status

- Last run: 2026-11-12T23:33:56+00:00 UTC, 628s
- Companies working: 634 of 635
- New roles last run: 6; roles in feed: 1611
- Universe (all other known career sites): 5303 boards, 4443 checked in the last hour, 1 errors; 1 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1723
- Skipped (backing off broken sites): 860; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 26 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
