# Collector status

- Last run: 2026-11-07T02:59:10+00:00 UTC, 443s
- Companies working: 631 of 633
- New roles last run: 0; roles in feed: 1585
- Universe (all other known career sites): 5166 boards, 4316 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1478
- Skipped (backing off broken sites): 849; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 15 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Alignment Health | 1 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
