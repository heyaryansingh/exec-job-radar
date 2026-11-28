# Collector status

- Last run: 2026-11-28T10:07:11+00:00 UTC, 781s
- Companies working: 603 of 638
- New roles last run: 2; roles in feed: 1185
- Universe (all other known career sites): 5612 boards, 3812 checked in the last hour, 43 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 159, "senior titles from boards/aggregators": 46}
- Companies with open roles: 1954
- Skipped (backing off broken sites): 1767; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 56 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 35 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 27 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 22 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| LendingClub | 18 | 422 Client Error: Unprocessable Entity for url: https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/l |
| Thoughtworks | 13 | 404 Client Error: Not Found for url: https://boards-api.greenhouse.io/v1/boards/thoughtworks/jobs |
| Fannie Mae | 7 | HTTP 429 for https://fanniemae.wd1.myworkdayjobs.com/wday/cxs/fanniemae/FannieMaeCareers/jobs |
| Mastercard | 7 | HTTP 429 for https://mastercard.wd1.myworkdayjobs.com/wday/cxs/mastercard/CorporateCareers/jobs |
| Ovintiv | 7 | HTTP 429 for https://ovintiv.wd3.myworkdayjobs.com/wday/cxs/ovintiv/ovintivcareers/jobs |
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |
| Dimensional Fund Advisors | 6 | HTTP 429 for https://dimensional.wd5.myworkdayjobs.com/wday/cxs/dimensional/DFA_Careers/jobs |
| Equinor | 6 | HTTP 429 for https://equinor.wd3.myworkdayjobs.com/wday/cxs/equinor/EQNR/jobs |
| Unilever | 6 | HTTP 429 for https://unilever.wd3.myworkdayjobs.com/wday/cxs/unilever/Unilever_Experienced_Professio |
| Chevron | 4 | HTTP 429 for https://chevron.wd5.myworkdayjobs.com/wday/cxs/chevron/jobs/jobs |
| LSEG | 4 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| Lumentum | 4 | HTTP 429 for https://lumentum.wd5.myworkdayjobs.com/wday/cxs/lumentum/LITE/jobs |
| Wellington Management | 4 | HTTP 429 for https://wellington.wd5.myworkdayjobs.com/wday/cxs/wellington/External/jobs |
| Air Liquide | 1 | HTTP 429 for https://airliquidehr.wd3.myworkdayjobs.com/wday/cxs/airliquidehr/AirLiquideExternalCare |
| Availity | 1 | HTTP 429 for https://availity.wd1.myworkdayjobs.com/wday/cxs/availity/Availity_Careers_US/jobs |
| Baxter | 1 | HTTP 429 for https://baxter.wd1.myworkdayjobs.com/wday/cxs/baxter/baxter/jobs |
| CME Group | 1 | HTTP 429 for https://cmegroup.wd1.myworkdayjobs.com/wday/cxs/cmegroup/cme_careers/jobs |
| Cerberus Capital Management | 1 | HTTP 429 for https://cerberus.wd1.myworkdayjobs.com/wday/cxs/cerberus/CerberusCareers/jobs |
| Discover | 1 | HTTP 429 for https://ensign.wd1.myworkdayjobs.com/wday/cxs/ensign/DiscoveryCareerSite/jobs |
| Dow | 1 | HTTP 429 for https://dow.wd1.myworkdayjobs.com/wday/cxs/dow/ExternalCareers/jobs |
| Dow Jones | 1 | HTTP 429 for https://dowjones.wd1.myworkdayjobs.com/wday/cxs/dowjones/News_Corp_Australia_Careers/jo |
| Huron Consulting | 1 | HTTP 429 for https://huron.wd1.myworkdayjobs.com/wday/cxs/huron/huroncareers/jobs |
| MassMutual | 1 | HTTP 429 for https://massmutual.wd1.myworkdayjobs.com/wday/cxs/massmutual/mmcareers/jobs |
| Nike | 1 | HTTP 429 for https://nike.wd1.myworkdayjobs.com/wday/cxs/nike/nke2/jobs |
| Nordstrom | 1 | HTTP 429 for https://nordstrom.wd501.myworkdayjobs.com/wday/cxs/nordstrom/nordstrom_careers/jobs |
| Shell | 1 | HTTP 429 for https://shell.wd3.myworkdayjobs.com/wday/cxs/shell/ShellCareers/jobs |
| Tyson Foods | 1 | HTTP 429 for https://tysonfoods.wd5.myworkdayjobs.com/wday/cxs/tysonfoods/TSN/jobs |
| Unisys | 1 | HTTP 429 for https://unisys.wd5.myworkdayjobs.com/wday/cxs/unisys/External/jobs |
| Xcel Energy | 1 | HTTP 429 for https://xcelenergy.wd1.myworkdayjobs.com/wday/cxs/xcelenergy/External/jobs |
| Zayo | 1 | HTTP 429 for https://zayo.wd1.myworkdayjobs.com/wday/cxs/zayo/Zayo_Careers/jobs |
| athenahealth | 1 | HTTP 429 for https://athenahealth.wd1.myworkdayjobs.com/wday/cxs/athenahealth/External/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
