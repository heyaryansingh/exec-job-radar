# Collector status

- Last run: 2026-11-13T20:48:20+00:00 UTC, 824s
- Companies working: 632 of 635
- New roles last run: 9; roles in feed: 1594
- Universe (all other known career sites): 5326 boards, 4463 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1753
- Skipped (backing off broken sites): 863; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 28 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 7 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Johnson Controls | 1 | HTTP 502 for https://jci.wd5.myworkdayjobs.com/wday/cxs/jci/JCI/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
