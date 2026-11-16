# Collector status

- Last run: 2026-11-16T05:55:42+00:00 UTC, 493s
- Companies working: 621 of 636
- New roles last run: 17; roles in feed: 1187
- Universe (all other known career sites): 5360 boards, 3745 checked in the last hour, 47 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 144, "jsearch": 35, "senior titles from boards/aggregators": 80}
- Companies with open roles: 1808
- Skipped (backing off broken sites): 1570; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Salesforce | 2 | HTTP 429 for https://salesforce.wd12.myworkdayjobs.com/wday/cxs/salesforce/External_Career_Site/jobs |
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Atmos Energy | 1 | HTTP 429 for https://atmosenergy.wd108.myworkdayjobs.com/wday/cxs/atmosenergy/External_Career_Site/j |
| Capital One | 1 | HTTP 429 for https://capitalone.wd12.myworkdayjobs.com/wday/cxs/capitalone/Capital_One/jobs |
| Fortress Investment Group | 1 | HTTP 429 for https://fortress.wd503.myworkdayjobs.com/wday/cxs/fortress/Careers/jobs |
| Kohl's | 1 | HTTP 429 for https://kohls.wd504.myworkdayjobs.com/wday/cxs/kohls/kohlscareers/jobs |
| Live Nation | 1 | HTTP 429 for https://livenation.wd503.myworkdayjobs.com/wday/cxs/livenation/LNExternalSite/jobs |
| Nordstrom | 1 | HTTP 429 for https://nordstrom.wd501.myworkdayjobs.com/wday/cxs/nordstrom/nordstrom_careers/jobs |
| Realty Income | 1 | HTTP 429 for https://realtyincome.wd108.myworkdayjobs.com/wday/cxs/realtyincome/realty_income_career |
| Tapestry | 1 | HTTP 429 for https://tapestry.wd108.myworkdayjobs.com/wday/cxs/tapestry/Tapestry_Careers/jobs |
| Texas Capital Bank | 1 | HTTP 429 for https://texascapitalbank.wd12.myworkdayjobs.com/wday/cxs/texascapitalbank/Careers/jobs |
| Verizon | 1 | HTTP 429 for https://verizon.wd12.myworkdayjobs.com/wday/cxs/verizon/verizon-careers/jobs |
| Zebra Technologies | 1 | HTTP 429 for https://zebra.wd501.myworkdayjobs.com/wday/cxs/zebra/Zebra_careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
