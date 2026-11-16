# Collector status

- Last run: 2026-11-16T01:06:37+00:00 UTC, 567s
- Companies working: 623 of 636
- New roles last run: 1; roles in feed: 1168
- Universe (all other known career sites): 5358 boards, 3763 checked in the last hour, 69 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 164, "senior titles from boards/aggregators": 56}
- Companies with open roles: 1802
- Skipped (backing off broken sites): 1528; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Verizon | 3 | HTTP 429 for https://verizon.wd12.myworkdayjobs.com/wday/cxs/verizon/verizon-careers/jobs |
| Alteryx | 2 | HTTP 429 for https://alteryx.wd108.myworkdayjobs.com/wday/cxs/alteryx/AlteryxCareers/jobs |
| Atmos Energy | 2 | HTTP 429 for https://atmosenergy.wd108.myworkdayjobs.com/wday/cxs/atmosenergy/External_Career_Site/j |
| Expedia Group | 2 | HTTP 429 for https://expedia.wd108.myworkdayjobs.com/wday/cxs/expedia/search/jobs |
| Fortress Investment Group | 2 | HTTP 429 for https://fortress.wd503.myworkdayjobs.com/wday/cxs/fortress/Careers/jobs |
| Realty Income | 2 | HTTP 429 for https://realtyincome.wd108.myworkdayjobs.com/wday/cxs/realtyincome/realty_income_career |
| Tapestry | 2 | HTTP 429 for https://tapestry.wd108.myworkdayjobs.com/wday/cxs/tapestry/Tapestry_Careers/jobs |
| Capital One | 1 | HTTP 429 for https://capitalone.wd12.myworkdayjobs.com/wday/cxs/capitalone/Capital_One/jobs |
| FMC | 1 | HTTP 429 for https://fmc.wd12.myworkdayjobs.com/wday/cxs/fmc/FMC/jobs |
| Workiva | 1 | HTTP 429 for https://workiva.wd503.myworkdayjobs.com/wday/cxs/workiva/careers/jobs |
| Zebra Technologies | 1 | HTTP 429 for https://zebra.wd501.myworkdayjobs.com/wday/cxs/zebra/Zebra_careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
