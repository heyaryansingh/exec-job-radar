# Collector status

- Last run: 2026-11-16T03:00:31+00:00 UTC, 837s
- Companies working: 623 of 636
- New roles last run: 1; roles in feed: 1170
- Universe (all other known career sites): 5359 boards, 3744 checked in the last hour, 853 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 149, "senior titles from boards/aggregators": 49}
- Companies with open roles: 1802
- Skipped (backing off broken sites): 764; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Capital One | 3 | HTTP 429 for https://capitalone.wd12.myworkdayjobs.com/wday/cxs/capitalone/Capital_One/jobs |
| Accenture | 2 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Salesforce | 2 | HTTP 429 for https://salesforce.wd12.myworkdayjobs.com/wday/cxs/salesforce/External_Career_Site/jobs |
| Texas Capital Bank | 2 | HTTP 429 for https://texascapitalbank.wd12.myworkdayjobs.com/wday/cxs/texascapitalbank/Careers/jobs |
| Atmos Energy | 1 | HTTP 429 for https://atmosenergy.wd108.myworkdayjobs.com/wday/cxs/atmosenergy/External_Career_Site/j |
| Expedia Group | 1 | HTTP 429 for https://expedia.wd108.myworkdayjobs.com/wday/cxs/expedia/search/jobs |
| Forrester | 1 | HTTP 429 for https://forrester.wd501.myworkdayjobs.com/wday/cxs/forrester/careers/jobs |
| Fortress Investment Group | 1 | HTTP 429 for https://fortress.wd503.myworkdayjobs.com/wday/cxs/fortress/Careers/jobs |
| Genpact | 1 | HTTP 429 for https://genpact.wd108.myworkdayjobs.com/wday/cxs/genpact/External_Careers/jobs |
| Kohl's | 1 | HTTP 429 for https://kohls.wd504.myworkdayjobs.com/wday/cxs/kohls/kohlscareers/jobs |
| Petco | 1 | HTTP 429 for https://petco.wd504.myworkdayjobs.com/wday/cxs/petco/External/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
