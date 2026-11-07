# Collector status

- Last run: 2026-11-07T09:56:31+00:00 UTC, 590s
- Companies working: 629 of 633
- New roles last run: 0; roles in feed: 1624
- Universe (all other known career sites): 5174 boards, 4321 checked in the last hour, 7 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1505
- Skipped (backing off broken sites): 848; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 15 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |
| Availity | 3 | HTTPSConnectionPool(host='availity.wd1.myworkdayjobs.com', port=443): Read timed out. (read timeout= |
| Marvell | 1 | HTTP 500 for https://marvell.wd1.myworkdayjobs.com/wday/cxs/marvell/MarvellCareers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
