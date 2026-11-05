# Collector status

- Last run: 2026-11-05T14:26:51+00:00 UTC, 745s
- Companies working: 632 of 633
- New roles last run: 3; roles in feed: 1553
- Universe (all other known career sites): 5093 boards, 4250 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1358
- Skipped (backing off broken sites): 844; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 12 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
