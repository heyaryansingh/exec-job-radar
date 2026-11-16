# Collector status

- Last run: 2026-11-16T06:45:28+00:00 UTC, 474s
- Companies working: 630 of 636
- New roles last run: 0; roles in feed: 1184
- Universe (all other known career sites): 5361 boards, 3760 checked in the last hour, 30 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1808
- Skipped (backing off broken sites): 1573; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 32 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Accenture | 2 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Nordstrom | 2 | HTTP 429 for https://nordstrom.wd501.myworkdayjobs.com/wday/cxs/nordstrom/nordstrom_careers/jobs |
| Genpact | 1 | HTTP 429 for https://genpact.wd108.myworkdayjobs.com/wday/cxs/genpact/External_Careers/jobs |
| J.B. Hunt | 1 | HTTP 429 for https://jbhunt.wd501.myworkdayjobs.com/wday/cxs/jbhunt/Careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
