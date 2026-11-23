# Collector status

- Last run: 2026-11-23T00:27:34+00:00 UTC, 621s
- Companies working: 612 of 638
- New roles last run: 0; roles in feed: 1189
- Universe (all other known career sites): 5503 boards, 3843 checked in the last hour, 3 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1936
- Skipped (backing off broken sites): 1666; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 45 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 24 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 17 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 12 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| Disney | 9 | HTTP 429 for https://disney.wd5.myworkdayjobs.com/wday/cxs/disney/disneycareer/jobs |
| Blackstone | 8 | HTTP 429 for https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone/Blackstone_Careers/jobs |
| DataRobot | 8 | HTTP 429 for https://datarobot.wd1.myworkdayjobs.com/wday/cxs/datarobot/DataRobot_External_Careers/j |
| LendingClub | 8 | HTTP 429 for https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/lendingclub/External/jobs |
| Ovintiv | 7 | HTTP 429 for https://ovintiv.wd3.myworkdayjobs.com/wday/cxs/ovintiv/ovintivcareers/jobs |
| Analog Devices | 6 | HTTP 429 for https://analogdevices.wd1.myworkdayjobs.com/wday/cxs/analogdevices/External/jobs |
| Invesco | 6 | HTTP 429 for https://invesco.wd1.myworkdayjobs.com/wday/cxs/invesco/IVZ/jobs |
| Shell | 3 | HTTP 429 for https://shell.wd3.myworkdayjobs.com/wday/cxs/shell/ShellCareers/jobs |
| Accenture | 2 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Arctic Wolf | 2 | HTTP 429 for https://arcticwolf.wd1.myworkdayjobs.com/wday/cxs/arcticwolf/External/jobs |
| Darktrace | 2 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| Fresenius Medical Care | 2 | HTTP 429 for https://freseniusmedicalcare.wd3.myworkdayjobs.com/wday/cxs/freseniusmedicalcare/fme/jo |
| Frost Bank | 2 | HTTP 429 for https://frostbank.wd5.myworkdayjobs.com/wday/cxs/frostbank/external/jobs |
| LSEG | 2 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| Unilever | 2 | HTTP 429 for https://unilever.wd3.myworkdayjobs.com/wday/cxs/unilever/Unilever_Experienced_Professio |
| Air Liquide | 1 | HTTP 429 for https://airliquidehr.wd3.myworkdayjobs.com/wday/cxs/airliquidehr/AirLiquideExternalCare |
| Coca-Cola | 1 | HTTP 429 for https://coke.wd1.myworkdayjobs.com/wday/cxs/coke/coca-cola-careers/jobs |
| Edwards Lifesciences | 1 | HTTP 429 for https://edwards.wd5.myworkdayjobs.com/wday/cxs/edwards/edwardscareers/jobs |
| Equinor | 1 | HTTP 429 for https://equinor.wd3.myworkdayjobs.com/wday/cxs/equinor/EQNR/jobs |
| MassMutual | 1 | HTTP 429 for https://massmutual.wd1.myworkdayjobs.com/wday/cxs/massmutual/mmcareers/jobs |
| Santander | 1 | HTTP 429 for https://santander.wd3.myworkdayjobs.com/wday/cxs/santander/SantanderCareers/jobs |
| Unisys | 1 | HTTP 429 for https://unisys.wd5.myworkdayjobs.com/wday/cxs/unisys/External/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
