# Collector status

- Last run: 2026-11-16T03:55:50+00:00 UTC, 512s
- Companies working: 625 of 636
- New roles last run: 0; roles in feed: 1170
- Universe (all other known career sites): 5360 boards, 3755 checked in the last hour, 47 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1802
- Skipped (backing off broken sites): 1560; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| FMC | 2 | HTTP 429 for https://fmc.wd12.myworkdayjobs.com/wday/cxs/fmc/FMC/jobs |
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Atmos Energy | 1 | HTTP 429 for https://atmosenergy.wd108.myworkdayjobs.com/wday/cxs/atmosenergy/External_Career_Site/j |
| Capital One | 1 | HTTP 429 for https://capitalone.wd12.myworkdayjobs.com/wday/cxs/capitalone/Capital_One/jobs |
| Genpact | 1 | HTTP 429 for https://genpact.wd108.myworkdayjobs.com/wday/cxs/genpact/External_Careers/jobs |
| Kohl's | 1 | HTTP 429 for https://kohls.wd504.myworkdayjobs.com/wday/cxs/kohls/kohlscareers/jobs |
| Live Nation | 1 | HTTP 429 for https://livenation.wd503.myworkdayjobs.com/wday/cxs/livenation/LNExternalSite/jobs |
| Realty Income | 1 | HTTP 429 for https://realtyincome.wd108.myworkdayjobs.com/wday/cxs/realtyincome/realty_income_career |
| Texas Capital Bank | 1 | HTTP 429 for https://texascapitalbank.wd12.myworkdayjobs.com/wday/cxs/texascapitalbank/Careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
