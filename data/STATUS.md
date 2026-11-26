# Collector status

- Last run: 2026-11-26T03:52:40+00:00 UTC, 678s
- Companies working: 611 of 638
- New roles last run: 2; roles in feed: 1409
- Universe (all other known career sites): 5594 boards, 3861 checked in the last hour, 29 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 2014
- Skipped (backing off broken sites): 1719; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 51 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 30 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 23 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 18 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| LendingClub | 14 | HTTP 429 for https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/lendingclub/External/jobs |
| Dow | 9 | HTTP 429 for https://dow.wd1.myworkdayjobs.com/wday/cxs/dow/ExternalCareers/jobs |
| Thoughtworks | 9 | 404 Client Error: Not Found for url: https://boards-api.greenhouse.io/v1/boards/thoughtworks/jobs |
| Blackstone | 7 | HTTP 429 for https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone/Blackstone_Careers/jobs |
| Booking Holdings | 7 | HTTP 429 for https://priceline.wd1.myworkdayjobs.com/wday/cxs/priceline/BookingHoldings/jobs |
| R1 RCM | 7 | HTTP 429 for https://r1rcm.wd1.myworkdayjobs.com/wday/cxs/r1rcm/R1RCM/jobs |
| Santander | 7 | HTTP 429 for https://santander.wd3.myworkdayjobs.com/wday/cxs/santander/SantanderCareers/jobs |
| Accenture | 6 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| LSEG | 6 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| MassMutual | 6 | HTTP 429 for https://massmutual.wd1.myworkdayjobs.com/wday/cxs/massmutual/mmcareers/jobs |
| Micron | 6 | HTTP 429 for https://micron.wd1.myworkdayjobs.com/wday/cxs/micron/External/jobs |
| Truist | 6 | HTTP 429 for https://truist.wd1.myworkdayjobs.com/wday/cxs/truist/Careers/jobs |
| Church & Dwight | 5 | HTTP 429 for https://churchdwight.wd1.myworkdayjobs.com/wday/cxs/churchdwight/chdcareers/jobs |
| DataRobot | 5 | HTTP 429 for https://datarobot.wd1.myworkdayjobs.com/wday/cxs/datarobot/DataRobot_External_Careers/j |
| PVH | 5 | HTTP 429 for https://pvh.wd1.myworkdayjobs.com/wday/cxs/pvh/PVH_Careers/jobs |
| CarMax | 4 | HTTP 429 for https://carmax.wd1.myworkdayjobs.com/wday/cxs/carmax/External/jobs |
| ONEOK | 4 | HTTP 429 for https://oneok.wd1.myworkdayjobs.com/wday/cxs/oneok/ONEOK/jobs |
| Darktrace | 3 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| Expedia Group | 2 | HTTP 429 for https://expedia.wd108.myworkdayjobs.com/wday/cxs/expedia/search/jobs |
| Guidehouse | 2 | HTTP 429 for https://guidehouse.wd1.myworkdayjobs.com/wday/cxs/guidehouse/External/jobs |
| Nationwide | 2 | HTTP 429 for https://nationwide.wd1.myworkdayjobs.com/wday/cxs/nationwide/Nationwide_Career/jobs |
| GlobalFoundries | 1 | HTTP 429 for https://globalfoundries.wd1.myworkdayjobs.com/wday/cxs/globalfoundries/External/jobs |
| United Rentals | 1 | HTTP 429 for https://ur.wd1.myworkdayjobs.com/wday/cxs/ur/URcareers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
