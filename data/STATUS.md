# Collector status

- Last run: 2026-11-15T23:07:18+00:00 UTC, 518s
- Companies working: 631 of 636
- New roles last run: 0; roles in feed: 1350
- Universe (all other known career sites): 5358 boards, 3769 checked in the last hour, 63 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1801
- Skipped (backing off broken sites): 1528; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Capital One | 1 | HTTP 429 for https://capitalone.wd12.myworkdayjobs.com/wday/cxs/capitalone/Capital_One/jobs |
| Texas Capital Bank | 1 | HTTP 429 for https://texascapitalbank.wd12.myworkdayjobs.com/wday/cxs/texascapitalbank/Careers/jobs |
| Verizon | 1 | HTTP 429 for https://verizon.wd12.myworkdayjobs.com/wday/cxs/verizon/verizon-careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
