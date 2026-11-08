# Collector status

- Last run: 2026-11-08T04:25:42+00:00 UTC, 498s
- Companies working: 632 of 633
- New roles last run: 16; roles in feed: 1456
- Universe (all other known career sites): 5186 boards, 4333 checked in the last hour, 0 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"jsearch": 30, "senior titles from boards/aggregators": 30}
- Companies with open roles: 1529
- Skipped (backing off broken sites): 854; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 17 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
