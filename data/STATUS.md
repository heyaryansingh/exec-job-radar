# Collector status

- Last run: 2026-11-07T09:05:55+00:00 UTC, 570s
- Companies working: 629 of 633
- New roles last run: 2; roles in feed: 1624
- Universe (all other known career sites): 5174 boards, 4320 checked in the last hour, 4 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1505
- Skipped (backing off broken sites): 852; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 15 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |
| Availity | 2 | HTTPSConnectionPool(host='availity.wd1.myworkdayjobs.com', port=443): Read timed out. (read timeout= |
| Wells Fargo | 2 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
