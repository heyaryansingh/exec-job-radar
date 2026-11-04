# Collector status

- Last run: 2026-11-04T03:43:51+00:00 UTC, 694s
- Companies working: 632 of 633
- New roles last run: 6; roles in feed: 1423
- Universe (all other known career sites): 5039 boards, 4202 checked in the last hour, 0 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"jsearch": 17, "senior titles from boards/aggregators": 17}
- Companies with open roles: 1286
- Skipped (backing off broken sites): 838; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 9 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
