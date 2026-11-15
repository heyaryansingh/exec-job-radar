# Collector status

- Last run: 2026-11-15T02:49:32+00:00 UTC, 390s
- Companies working: 600 of 635
- New roles last run: 0; roles in feed: 1329
- Universe (all other known career sites): 5351 boards, 3826 checked in the last hour, 0 errors; 0 employer names learned; 4 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 315, "senior titles from boards/aggregators": 121}
- Companies with open roles: 1792
- Skipped (backing off broken sites): 1556; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 30 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 9 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Abbott | 7 | Expecting value: line 1 column 1 (char 0) |
| Allstate | 7 | Expecting value: line 1 column 1 (char 0) |
| Amgen | 7 | Expecting value: line 1 column 1 (char 0) |
| Baker Hughes | 7 | Expecting value: line 1 column 1 (char 0) |
| Centene | 7 | Expecting value: line 1 column 1 (char 0) |
| Cigna | 7 | Expecting value: line 1 column 1 (char 0) |
| Citi | 7 | Expecting value: line 1 column 1 (char 0) |
| Cushman & Wakefield | 7 | Expecting value: line 1 column 1 (char 0) |
| Discover | 7 | Expecting value: line 1 column 1 (char 0) |
| Disney | 7 | Expecting value: line 1 column 1 (char 0) |
| Elevance Health | 7 | Expecting value: line 1 column 1 (char 0) |
| FedEx | 7 | Expecting value: line 1 column 1 (char 0) |
| General Motors | 7 | Expecting value: line 1 column 1 (char 0) |
| HP | 7 | Expecting value: line 1 column 1 (char 0) |
| Humana | 7 | Expecting value: line 1 column 1 (char 0) |
| IQVIA | 7 | HTTP 429 for https://iqvia.wd1.myworkdayjobs.com/wday/cxs/iqvia/IQVIA/jobs |
| Intel | 7 | Expecting value: line 1 column 1 (char 0) |
| Jabil | 7 | Expecting value: line 1 column 1 (char 0) |
| Kemper | 7 | Expecting value: line 1 column 1 (char 0) |
| Kyndryl | 7 | Expecting value: line 1 column 1 (char 0) |
| NVIDIA | 7 | Expecting value: line 1 column 1 (char 0) |
| PNC | 7 | Expecting value: line 1 column 1 (char 0) |
| Prudential | 7 | Expecting value: line 1 column 1 (char 0) |
| RTX | 7 | Expecting value: line 1 column 1 (char 0) |
| Ryder | 7 | Expecting value: line 1 column 1 (char 0) |
| S&P Global | 7 | Expecting value: line 1 column 1 (char 0) |
| Target | 7 | Expecting value: line 1 column 1 (char 0) |
| Travelers | 7 | Expecting value: line 1 column 1 (char 0) |
| Workday | 7 | Expecting value: line 1 column 1 (char 0) |
| Associated Bank | 1 | HTTP 429 for https://associatedbank.wd1.myworkdayjobs.com/wday/cxs/associatedbank/external_careers/j |
| Bloomberg | 1 | HTTP 429 for https://bloomberg.wd1.myworkdayjobs.com/wday/cxs/bloomberg/Bloombergindustrygroup_Exter |
| PVH | 1 | HTTP 429 for https://pvh.wd1.myworkdayjobs.com/wday/cxs/pvh/PVH_Careers/jobs |
| T-Mobile | 1 | HTTP 429 for https://tmobile.wd1.myworkdayjobs.com/wday/cxs/tmobile/External/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
