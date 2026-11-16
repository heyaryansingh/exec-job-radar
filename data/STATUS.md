# Collector status

- Last run: 2026-11-16T00:06:05+00:00 UTC, 537s
- Companies working: 625 of 636
- New roles last run: 0; roles in feed: 1167
- Universe (all other known career sites): 5358 boards, 3769 checked in the last hour, 63 errors; 1 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1801
- Skipped (backing off broken sites): 1528; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Verizon | 2 | HTTP 429 for https://verizon.wd12.myworkdayjobs.com/wday/cxs/verizon/verizon-careers/jobs |
| Alteryx | 1 | HTTP 429 for https://alteryx.wd108.myworkdayjobs.com/wday/cxs/alteryx/AlteryxCareers/jobs |
| Atmos Energy | 1 | HTTP 429 for https://atmosenergy.wd108.myworkdayjobs.com/wday/cxs/atmosenergy/External_Career_Site/j |
| Expedia Group | 1 | HTTP 429 for https://expedia.wd108.myworkdayjobs.com/wday/cxs/expedia/search/jobs |
| Fortress Investment Group | 1 | HTTP 429 for https://fortress.wd503.myworkdayjobs.com/wday/cxs/fortress/Careers/jobs |
| J.B. Hunt | 1 | HTTP 429 for https://jbhunt.wd501.myworkdayjobs.com/wday/cxs/jbhunt/Careers/jobs |
| Realty Income | 1 | HTTP 429 for https://realtyincome.wd108.myworkdayjobs.com/wday/cxs/realtyincome/realty_income_career |
| Salesforce | 1 | HTTP 429 for https://salesforce.wd12.myworkdayjobs.com/wday/cxs/salesforce/External_Career_Site/jobs |
| Tapestry | 1 | HTTP 429 for https://tapestry.wd108.myworkdayjobs.com/wday/cxs/tapestry/Tapestry_Careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
