# Collector status

- Last run: 2026-11-22T17:37:04+00:00 UTC, 612s
- Companies working: 605 of 638
- New roles last run: 0; roles in feed: 1347
- Universe (all other known career sites): 5503 boards, 3837 checked in the last hour, 7 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1971
- Skipped (backing off broken sites): 1674; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 45 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 24 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 16 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 11 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| Workday | 10 | HTTP 429 for https://workday.wd5.myworkdayjobs.com/wday/cxs/workday/Workday/jobs |
| Ameriprise Financial | 8 | HTTP 429 for https://ameriprise.wd5.myworkdayjobs.com/wday/cxs/ameriprise/Ameriprise/jobs |
| Blackstone | 8 | HTTP 429 for https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone/Blackstone_Careers/jobs |
| DataRobot | 8 | HTTP 429 for https://datarobot.wd1.myworkdayjobs.com/wday/cxs/datarobot/DataRobot_External_Careers/j |
| Disney | 8 | HTTP 429 for https://disney.wd5.myworkdayjobs.com/wday/cxs/disney/disneycareer/jobs |
| LendingClub | 7 | HTTP 429 for https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/lendingclub/External/jobs |
| Analog Devices | 6 | HTTP 429 for https://analogdevices.wd1.myworkdayjobs.com/wday/cxs/analogdevices/External/jobs |
| Availity | 6 | HTTP 429 for https://availity.wd1.myworkdayjobs.com/wday/cxs/availity/Availity_Careers_US/jobs |
| Gilead Sciences | 6 | HTTP 429 for https://gilead.wd1.myworkdayjobs.com/wday/cxs/gilead/gileadcareers/jobs |
| Invesco | 6 | HTTP 429 for https://invesco.wd1.myworkdayjobs.com/wday/cxs/invesco/IVZ/jobs |
| Ovintiv | 6 | HTTP 429 for https://ovintiv.wd3.myworkdayjobs.com/wday/cxs/ovintiv/ovintivcareers/jobs |
| Darktrace | 3 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| Unilever | 3 | HTTP 429 for https://unilever.wd3.myworkdayjobs.com/wday/cxs/unilever/Unilever_Experienced_Professio |
| Epicor | 2 | HTTP 429 for https://epicorsoftware.wd5.myworkdayjobs.com/wday/cxs/epicorsoftware/epicorjobs/jobs |
| LSEG | 2 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| PNC | 2 | HTTP 429 for https://pnc.wd5.myworkdayjobs.com/wday/cxs/pnc/External/jobs |
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Apollo Global Management | 1 | HTTP 429 for https://athene.wd5.myworkdayjobs.com/wday/cxs/athene/Apollo_Careers/jobs |
| Bloomberg | 1 | HTTP 429 for https://bloomberg.wd1.myworkdayjobs.com/wday/cxs/bloomberg/Bloombergindustrygroup_Exter |
| Booking Holdings | 1 | HTTP 429 for https://priceline.wd1.myworkdayjobs.com/wday/cxs/priceline/BookingHoldings/jobs |
| Credit Acceptance | 1 | HTTP 429 for https://creditacceptance.wd5.myworkdayjobs.com/wday/cxs/creditacceptance/Credit_Accepta |
| Dow Jones | 1 | HTTP 429 for https://dowjones.wd1.myworkdayjobs.com/wday/cxs/dowjones/News_Corp_Australia_Careers/jo |
| Duck Creek Technologies | 1 | HTTP 429 for https://duckcreek.wd1.myworkdayjobs.com/wday/cxs/duckcreek/duckcreekcareers/jobs |
| ONEOK | 1 | HTTP 429 for https://oneok.wd1.myworkdayjobs.com/wday/cxs/oneok/ONEOK/jobs |
| Peak6 | 1 | HTTP 429 for https://peak6group.wd1.myworkdayjobs.com/wday/cxs/peak6group/apexfintechsolutions/jobs |
| Santander | 1 | HTTP 429 for https://santander.wd3.myworkdayjobs.com/wday/cxs/santander/SantanderCareers/jobs |
| Texas Capital Bank | 1 | HTTP 429 for https://texascapitalbank.wd12.myworkdayjobs.com/wday/cxs/texascapitalbank/Careers/jobs |
| The Hartford | 1 | HTTP 429 for https://thehartford.wd5.myworkdayjobs.com/wday/cxs/thehartford/Careers_External/jobs |
| Toyota North America | 1 | HTTP 429 for https://toyota.wd503.myworkdayjobs.com/wday/cxs/toyota/TMNA/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
