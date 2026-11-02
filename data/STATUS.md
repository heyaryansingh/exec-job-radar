# Collector status

- Last run: 2026-11-02T16:50:48+00:00 UTC, 636s
- Companies working: 632 of 633
- New roles last run: 6; roles in feed: 1343
- Universe (all other known career sites): 4977 boards, 4141 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1177
- Skipped (backing off broken sites): 837; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
