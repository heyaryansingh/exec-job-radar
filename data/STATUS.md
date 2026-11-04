# Collector status

- Last run: 2026-11-04T19:06:37+00:00 UTC, 799s
- Companies working: 632 of 633
- New roles last run: 6; roles in feed: 1503
- Universe (all other known career sites): 5058 boards, 4214 checked in the last hour, 3 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1308
- Skipped (backing off broken sites): 842; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
