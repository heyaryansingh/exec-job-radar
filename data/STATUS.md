# Collector status

- Last run: 2026-11-26T00:02:50+00:00 UTC, 702s
- Companies working: 608 of 638
- New roles last run: 13; roles in feed: 1401
- Universe (all other known career sites): 5589 boards, 3892 checked in the last hour, 9 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 433, "senior titles from boards/aggregators": 204}
- Companies with open roles: 2012
- Skipped (backing off broken sites): 1710; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 51 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 30 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 22 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 17 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| LendingClub | 13 | HTTP 429 for https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/lendingclub/External/jobs |
| Dow | 9 | HTTP 429 for https://dow.wd1.myworkdayjobs.com/wday/cxs/dow/ExternalCareers/jobs |
| Centene | 8 | HTTP 429 for https://centene.wd5.myworkdayjobs.com/wday/cxs/centene/Centene_External/jobs |
| Dimensional Fund Advisors | 8 | HTTP 429 for https://dimensional.wd5.myworkdayjobs.com/wday/cxs/dimensional/DFA_Careers/jobs |
| Martin Marietta | 8 | HTTP 429 for https://martinmarietta.wd5.myworkdayjobs.com/wday/cxs/martinmarietta/Martin_Marietta_Ca |
| Thoughtworks | 8 | 404 Client Error: Not Found for url: https://boards-api.greenhouse.io/v1/boards/thoughtworks/jobs |
| Viatris | 8 | HTTP 429 for https://viatris.wd5.myworkdayjobs.com/wday/cxs/viatris/External/jobs |
| Booking Holdings | 7 | HTTP 429 for https://priceline.wd1.myworkdayjobs.com/wday/cxs/priceline/BookingHoldings/jobs |
| R1 RCM | 7 | HTTP 429 for https://r1rcm.wd1.myworkdayjobs.com/wday/cxs/r1rcm/R1RCM/jobs |
| Santander | 7 | HTTP 429 for https://santander.wd3.myworkdayjobs.com/wday/cxs/santander/SantanderCareers/jobs |
| Blackstone | 6 | HTTP 429 for https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone/Blackstone_Careers/jobs |
| Cleveland Clinic | 6 | HTTP 429 for https://ccf.wd1.myworkdayjobs.com/wday/cxs/ccf/ClevelandClinicCareersUK/jobs |
| Highmark Health | 6 | HTTP 429 for https://highmarkhealth.wd1.myworkdayjobs.com/wday/cxs/highmarkhealth/highmark/jobs |
| LSEG | 6 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| Loews | 6 | HTTP 429 for https://loewscorp.wd1.myworkdayjobs.com/wday/cxs/loewscorp/loewscorp/jobs |
| MassMutual | 6 | HTTP 429 for https://massmutual.wd1.myworkdayjobs.com/wday/cxs/massmutual/mmcareers/jobs |
| Micron | 6 | HTTP 429 for https://micron.wd1.myworkdayjobs.com/wday/cxs/micron/External/jobs |
| Prudential | 6 | HTTP 429 for https://pru.wd5.myworkdayjobs.com/wday/cxs/pru/Careers/jobs |
| Simon Property Group | 6 | HTTP 429 for https://simon.wd1.myworkdayjobs.com/wday/cxs/simon/Simon/jobs |
| Truist | 6 | HTTP 429 for https://truist.wd1.myworkdayjobs.com/wday/cxs/truist/Careers/jobs |
| Accenture | 5 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Adobe | 1 | HTTP 429 for https://adobe.wd5.myworkdayjobs.com/wday/cxs/adobe/external_experienced/jobs |
| Darktrace | 1 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| Equinor | 1 | HTTP 429 for https://equinor.wd3.myworkdayjobs.com/wday/cxs/equinor/EQNR/jobs |
| Fresenius Medical Care | 1 | HTTP 429 for https://freseniusmedicalcare.wd3.myworkdayjobs.com/wday/cxs/freseniusmedicalcare/fme/jo |
| Travelers | 1 | HTTP 429 for https://travelers.wd5.myworkdayjobs.com/wday/cxs/travelers/External/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
