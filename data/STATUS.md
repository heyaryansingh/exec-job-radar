# Collector status

- Last run: 2026-11-16T04:53:54+00:00 UTC, 390s
- Companies working: 631 of 636
- New roles last run: 0; roles in feed: 1170
- Universe (all other known career sites): 5360 boards, 3776 checked in the last hour, 18 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1802
- Skipped (backing off broken sites): 1568; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| J.B. Hunt | 1 | HTTP 429 for https://jbhunt.wd501.myworkdayjobs.com/wday/cxs/jbhunt/Careers/jobs |
| Salesforce | 1 | HTTP 429 for https://salesforce.wd12.myworkdayjobs.com/wday/cxs/salesforce/External_Career_Site/jobs |
| Workiva | 1 | HTTP 429 for https://workiva.wd503.myworkdayjobs.com/wday/cxs/workiva/careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
