# Collector status

- Last run: 2026-11-23T20:51:11+00:00 UTC, 779s
- Companies working: 615 of 638
- New roles last run: 21; roles in feed: 1286
- Universe (all other known career sites): 5513 boards, 3921 checked in the last hour, 88 errors; 0 employer names learned; 9 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 320, "senior titles from boards/aggregators": 134}
- Companies with open roles: 1959
- Skipped (backing off broken sites): 1516; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 47 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 26 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 18 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 13 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| LendingClub | 9 | HTTP 429 for https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/lendingclub/External/jobs |
| Accenture | 6 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Cityblock Health | 6 | HTTP 429 for https://cityblockhealth.wd1.myworkdayjobs.com/wday/cxs/cityblockhealth/CityblockExterna |
| Darktrace | 6 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| Equinor | 6 | HTTP 429 for https://equinor.wd3.myworkdayjobs.com/wday/cxs/equinor/EQNR/jobs |
| Fresenius Medical Care | 6 | HTTP 429 for https://freseniusmedicalcare.wd3.myworkdayjobs.com/wday/cxs/freseniusmedicalcare/fme/jo |
| S&P Global | 6 | HTTP 429 for https://spgi.wd5.myworkdayjobs.com/wday/cxs/spgi/SPGI_Careers/jobs |
| Wellington Management | 6 | HTTP 429 for https://wellington.wd5.myworkdayjobs.com/wday/cxs/wellington/External/jobs |
| Air Liquide | 2 | HTTP 429 for https://airliquidehr.wd3.myworkdayjobs.com/wday/cxs/airliquidehr/AirLiquideExternalCare |
| Analog Devices | 2 | HTTP 429 for https://analogdevices.wd1.myworkdayjobs.com/wday/cxs/analogdevices/External/jobs |
| Blue Owl Capital | 2 | HTTP 429 for https://blueowl.wd1.myworkdayjobs.com/wday/cxs/blueowl/blueowl/jobs |
| Fannie Mae | 2 | HTTP 429 for https://fanniemae.wd1.myworkdayjobs.com/wday/cxs/fanniemae/FannieMaeCareers/jobs |
| PVH | 2 | HTTP 429 for https://pvh.wd1.myworkdayjobs.com/wday/cxs/pvh/PVH_Careers/jobs |
| Arrow Electronics | 1 | HTTP 429 for https://arrow.wd1.myworkdayjobs.com/wday/cxs/arrow/AC/jobs |
| Cleveland Clinic | 1 | HTTP 429 for https://ccf.wd1.myworkdayjobs.com/wday/cxs/ccf/ClevelandClinicCareersUK/jobs |
| ONEOK | 1 | HTTP 429 for https://oneok.wd1.myworkdayjobs.com/wday/cxs/oneok/ONEOK/jobs |
| Peak6 | 1 | HTTP 429 for https://peak6group.wd1.myworkdayjobs.com/wday/cxs/peak6group/apexfintechsolutions/jobs |
| SailPoint | 1 | HTTP 429 for https://sailpoint.wd1.myworkdayjobs.com/wday/cxs/sailpoint/SailPoint/jobs |
| Santander | 1 | HTTP 429 for https://santander.wd3.myworkdayjobs.com/wday/cxs/santander/SantanderCareers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
