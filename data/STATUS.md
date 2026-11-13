# Collector status

- Last run: 2026-11-13T21:50:58+00:00 UTC, 977s
- Companies working: 632 of 635
- New roles last run: 20; roles in feed: 1613
- Universe (all other known career sites): 5326 boards, 4463 checked in the last hour, 1 errors; 0 employer names learned; 8 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 455, "senior titles from boards/aggregators": 200}
- Companies with open roles: 1766
- Skipped (backing off broken sites): 864; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 28 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 7 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Johnson Controls | 2 | HTTP 502 for https://jci.wd5.myworkdayjobs.com/wday/cxs/jci/JCI/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
