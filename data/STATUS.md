# Collector status

- Last run: 2026-11-23T04:18:16+00:00 UTC, 658s
- Companies working: 614 of 638
- New roles last run: 8; roles in feed: 1212
- Universe (all other known career sites): 5503 boards, 3900 checked in the last hour, 26 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 139, "senior titles from boards/aggregators": 74}
- Companies with open roles: 1941
- Skipped (backing off broken sites): 1583; ran out of time: 0

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
| Unilever | 4 | HTTP 429 for https://unilever.wd3.myworkdayjobs.com/wday/cxs/unilever/Unilever_Experienced_Professio |
| MassMutual | 3 | HTTP 429 for https://massmutual.wd1.myworkdayjobs.com/wday/cxs/massmutual/mmcareers/jobs |
| Shell | 3 | HTTP 429 for https://shell.wd3.myworkdayjobs.com/wday/cxs/shell/ShellCareers/jobs |
| Air Liquide | 2 | HTTP 429 for https://airliquidehr.wd3.myworkdayjobs.com/wday/cxs/airliquidehr/AirLiquideExternalCare |
| LSEG | 2 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| T. Rowe Price | 2 | HTTP 429 for https://troweprice.wd5.myworkdayjobs.com/wday/cxs/troweprice/TRowePrice/jobs |
| Wintrust | 2 | HTTP 429 for https://wintrust.wd1.myworkdayjobs.com/wday/cxs/wintrust/Search/jobs |
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Blackstone | 1 | HTTP 429 for https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone/Blackstone_Careers/jobs |
| Bloomberg | 1 | HTTP 429 for https://bloomberg.wd1.myworkdayjobs.com/wday/cxs/bloomberg/Bloombergindustrygroup_Exter |
| Equinor | 1 | HTTP 429 for https://equinor.wd3.myworkdayjobs.com/wday/cxs/equinor/EQNR/jobs |
| Humana | 1 | HTTP 429 for https://humana.wd5.myworkdayjobs.com/wday/cxs/humana/Humana_External_Career_Site/jobs |
| Medtronic | 1 | HTTP 429 for https://medtronic.wd1.myworkdayjobs.com/wday/cxs/medtronic/MedtronicCareers/jobs |
| Nationwide | 1 | HTTP 429 for https://nationwide.wd1.myworkdayjobs.com/wday/cxs/nationwide/Nationwide_Career/jobs |
| Plains All American | 1 | HTTP 429 for https://plains.wd1.myworkdayjobs.com/wday/cxs/plains/plains/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
