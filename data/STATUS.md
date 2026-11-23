# Collector status

- Last run: 2026-11-23T09:11:22+00:00 UTC, 824s
- Companies working: 612 of 638
- New roles last run: 4; roles in feed: 1227
- Universe (all other known career sites): 5504 boards, 4016 checked in the last hour, 15 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 141, "senior titles from boards/aggregators": 75}
- Companies with open roles: 1943
- Skipped (backing off broken sites): 1482; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 46 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 25 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 17 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 12 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| Disney | 9 | HTTP 429 for https://disney.wd5.myworkdayjobs.com/wday/cxs/disney/disneycareer/jobs |
| LendingClub | 8 | HTTP 429 for https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/lendingclub/External/jobs |
| Ovintiv | 8 | HTTP 429 for https://ovintiv.wd3.myworkdayjobs.com/wday/cxs/ovintiv/ovintivcareers/jobs |
| Analog Devices | 7 | HTTP 429 for https://analogdevices.wd1.myworkdayjobs.com/wday/cxs/analogdevices/External/jobs |
| Santander | 6 | HTTP 429 for https://santander.wd3.myworkdayjobs.com/wday/cxs/santander/SantanderCareers/jobs |
| Darktrace | 5 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| Epicor | 4 | HTTP 429 for https://epicorsoftware.wd5.myworkdayjobs.com/wday/cxs/epicorsoftware/epicorjobs/jobs |
| Citi | 3 | HTTP 429 for https://citi.wd5.myworkdayjobs.com/wday/cxs/citi/2/jobs |
| Fresenius Medical Care | 3 | HTTP 429 for https://freseniusmedicalcare.wd3.myworkdayjobs.com/wday/cxs/freseniusmedicalcare/fme/jo |
| Orion Advisor Solutions | 3 | HTTP 429 for https://orionadvisor.wd1.myworkdayjobs.com/wday/cxs/orionadvisor/Orion_Careers/jobs |
| S&P Global | 3 | HTTP 429 for https://spgi.wd5.myworkdayjobs.com/wday/cxs/spgi/SPGI_Careers/jobs |
| Unilever | 3 | HTTP 429 for https://unilever.wd3.myworkdayjobs.com/wday/cxs/unilever/Unilever_Experienced_Professio |
| Nike | 2 | HTTP 429 for https://nike.wd1.myworkdayjobs.com/wday/cxs/nike/nke2/jobs |
| Rackspace | 2 | HTTP 429 for https://rackspace.wd1.myworkdayjobs.com/wday/cxs/rackspace/External/jobs |
| Zoetis | 2 | HTTP 429 for https://zoetis.wd5.myworkdayjobs.com/wday/cxs/zoetis/zoetis/jobs |
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Air Liquide | 1 | HTTP 429 for https://airliquidehr.wd3.myworkdayjobs.com/wday/cxs/airliquidehr/AirLiquideExternalCare |
| Alteryx | 1 | HTTP 429 for https://alteryx.wd108.myworkdayjobs.com/wday/cxs/alteryx/AlteryxCareers/jobs |
| Duke Energy | 1 | HTTP 429 for https://dukeenergy.wd1.myworkdayjobs.com/wday/cxs/dukeenergy/search/jobs |
| Goodyear | 1 | HTTP 429 for https://goodyear.wd1.myworkdayjobs.com/wday/cxs/goodyear/GoodyearCareers/jobs |
| Shell | 1 | HTTP 429 for https://shell.wd3.myworkdayjobs.com/wday/cxs/shell/ShellCareers/jobs |
| The Hartford | 1 | HTTP 429 for https://thehartford.wd5.myworkdayjobs.com/wday/cxs/thehartford/Careers_External/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
