# Collector status

- Last run: 2026-11-16T01:54:51+00:00 UTC, 452s
- Companies working: 628 of 636
- New roles last run: 1; roles in feed: 1169
- Universe (all other known career sites): 5359 boards, 3782 checked in the last hour, 30 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1802
- Skipped (backing off broken sites): 1549; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Realty Income | 3 | HTTP 429 for https://realtyincome.wd108.myworkdayjobs.com/wday/cxs/realtyincome/realty_income_career |
| Capital One | 2 | HTTP 429 for https://capitalone.wd12.myworkdayjobs.com/wday/cxs/capitalone/Capital_One/jobs |
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Live Nation | 1 | HTTP 429 for https://livenation.wd503.myworkdayjobs.com/wday/cxs/livenation/LNExternalSite/jobs |
| Salesforce | 1 | HTTP 429 for https://salesforce.wd12.myworkdayjobs.com/wday/cxs/salesforce/External_Career_Site/jobs |
| Texas Capital Bank | 1 | HTTP 429 for https://texascapitalbank.wd12.myworkdayjobs.com/wday/cxs/texascapitalbank/Careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
