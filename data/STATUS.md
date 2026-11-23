# Collector status

- Last run: 2026-11-23T05:19:49+00:00 UTC, 742s
- Companies working: 612 of 638
- New roles last run: 5; roles in feed: 1217
- Universe (all other known career sites): 5504 boards, 3980 checked in the last hour, 12 errors; 1 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1942
- Skipped (backing off broken sites): 1521; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 46 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 25 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 17 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 12 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| Disney | 9 | HTTP 429 for https://disney.wd5.myworkdayjobs.com/wday/cxs/disney/disneycareer/jobs |
| LendingClub | 8 | HTTP 429 for https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/lendingclub/External/jobs |
| Analog Devices | 7 | HTTP 429 for https://analogdevices.wd1.myworkdayjobs.com/wday/cxs/analogdevices/External/jobs |
| Ovintiv | 7 | HTTP 429 for https://ovintiv.wd3.myworkdayjobs.com/wday/cxs/ovintiv/ovintivcareers/jobs |
| Santander | 6 | HTTP 429 for https://santander.wd3.myworkdayjobs.com/wday/cxs/santander/SantanderCareers/jobs |
| Unilever | 5 | HTTP 429 for https://unilever.wd3.myworkdayjobs.com/wday/cxs/unilever/Unilever_Experienced_Professio |
| Air Liquide | 3 | HTTP 429 for https://airliquidehr.wd3.myworkdayjobs.com/wday/cxs/airliquidehr/AirLiquideExternalCare |
| LSEG | 3 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| T. Rowe Price | 3 | HTTP 429 for https://troweprice.wd5.myworkdayjobs.com/wday/cxs/troweprice/TRowePrice/jobs |
| Wintrust | 3 | HTTP 429 for https://wintrust.wd1.myworkdayjobs.com/wday/cxs/wintrust/Search/jobs |
| Equinor | 2 | HTTP 429 for https://equinor.wd3.myworkdayjobs.com/wday/cxs/equinor/EQNR/jobs |
| Benchmark | 1 | HTTP 429 for https://benchmark.wd1.myworkdayjobs.com/wday/cxs/benchmark/PGH_Careers/jobs |
| Blue Owl Capital | 1 | HTTP 429 for https://blueowl.wd1.myworkdayjobs.com/wday/cxs/blueowl/blueowl/jobs |
| Broadridge | 1 | HTTP 429 for https://broadridge.wd5.myworkdayjobs.com/wday/cxs/broadridge/Careers/jobs |
| CME Group | 1 | HTTP 429 for https://cmegroup.wd1.myworkdayjobs.com/wday/cxs/cmegroup/cme_careers/jobs |
| ConocoPhillips | 1 | HTTP 429 for https://conocophillips.wd1.myworkdayjobs.com/wday/cxs/conocophillips/External/jobs |
| Cushman & Wakefield | 1 | HTTP 429 for https://cw.wd1.myworkdayjobs.com/wday/cxs/cw/External/jobs |
| Darktrace | 1 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| J.M. Smucker | 1 | HTTP 429 for https://smucker.wd5.myworkdayjobs.com/wday/cxs/smucker/US_External_Careers/jobs |
| NCR Voyix | 1 | HTTP 429 for https://ncr.wd1.myworkdayjobs.com/wday/cxs/ncr/ext_apac/jobs |
| PulteGroup | 1 | HTTP 429 for https://pultegroup.wd1.myworkdayjobs.com/wday/cxs/pultegroup/PGI/jobs |
| Verizon | 1 | HTTP 429 for https://verizon.wd12.myworkdayjobs.com/wday/cxs/verizon/verizon-careers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
