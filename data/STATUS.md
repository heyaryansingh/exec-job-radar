# Collector status

- Last run: 2026-11-15T03:41:49+00:00 UTC, 346s
- Companies working: 623 of 635
- New roles last run: 0; roles in feed: 1329
- Universe (all other known career sites): 5354 boards, 3829 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1792
- Skipped (backing off broken sites): 1536; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 30 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 9 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Amgen | 7 | Expecting value: line 1 column 1 (char 0) |
| Cushman & Wakefield | 7 | Expecting value: line 1 column 1 (char 0) |
| Discover | 7 | Expecting value: line 1 column 1 (char 0) |
| Elevance Health | 7 | Expecting value: line 1 column 1 (char 0) |
| FedEx | 7 | Expecting value: line 1 column 1 (char 0) |
| IQVIA | 7 | HTTP 429 for https://iqvia.wd1.myworkdayjobs.com/wday/cxs/iqvia/IQVIA/jobs |
| Intel | 7 | Expecting value: line 1 column 1 (char 0) |
| Kemper | 7 | Expecting value: line 1 column 1 (char 0) |
| Target | 7 | Expecting value: line 1 column 1 (char 0) |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
