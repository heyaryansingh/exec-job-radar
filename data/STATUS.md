# Collector status

- Last run: 2026-11-28T04:07:04+00:00 UTC, 657s
- Companies working: 608 of 638
- New roles last run: 0; roles in feed: 1183
- Universe (all other known career sites): 5612 boards, 3878 checked in the last hour, 8 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1954
- Skipped (backing off broken sites): 1739; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 55 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 34 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 27 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 21 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| LendingClub | 18 | 422 Client Error: Unprocessable Entity for url: https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/l |
| Thoughtworks | 12 | 404 Client Error: Not Found for url: https://boards-api.greenhouse.io/v1/boards/thoughtworks/jobs |
| Baxter | 8 | HTTP 429 for https://baxter.wd1.myworkdayjobs.com/wday/cxs/baxter/baxter/jobs |
| CVS Health | 8 | HTTP 429 for https://cvshealth.wd1.myworkdayjobs.com/wday/cxs/cvshealth/CVS_Health_Careers/jobs |
| Cushman & Wakefield | 8 | HTTP 429 for https://cw.wd1.myworkdayjobs.com/wday/cxs/cw/External/jobs |
| Duck Creek Technologies | 8 | HTTP 429 for https://duckcreek.wd1.myworkdayjobs.com/wday/cxs/duckcreek/duckcreekcareers/jobs |
| Fannie Mae | 7 | HTTP 429 for https://fanniemae.wd1.myworkdayjobs.com/wday/cxs/fanniemae/FannieMaeCareers/jobs |
| Mastercard | 7 | HTTP 429 for https://mastercard.wd1.myworkdayjobs.com/wday/cxs/mastercard/CorporateCareers/jobs |
| Dimensional Fund Advisors | 6 | HTTP 429 for https://dimensional.wd5.myworkdayjobs.com/wday/cxs/dimensional/DFA_Careers/jobs |
| Ovintiv | 6 | HTTP 429 for https://ovintiv.wd3.myworkdayjobs.com/wday/cxs/ovintiv/ovintivcareers/jobs |
| Air Liquide | 5 | HTTP 429 for https://airliquidehr.wd3.myworkdayjobs.com/wday/cxs/airliquidehr/AirLiquideExternalCare |
| LSEG | 5 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| Shell | 4 | HTTP 429 for https://shell.wd3.myworkdayjobs.com/wday/cxs/shell/ShellCareers/jobs |
| Alignment Health | 3 | Expecting value: line 1 column 1 (char 0) |
| Zayo | 3 | HTTP 429 for https://zayo.wd1.myworkdayjobs.com/wday/cxs/zayo/Zayo_Careers/jobs |
| Amgen | 2 | HTTP 429 for https://amgen.wd1.myworkdayjobs.com/wday/cxs/amgen/Careers/jobs |
| Bloomberg | 2 | HTTP 429 for https://bloomberg.wd1.myworkdayjobs.com/wday/cxs/bloomberg/Bloombergindustrygroup_Exter |
| Fresenius Medical Care | 2 | HTTP 429 for https://freseniusmedicalcare.wd3.myworkdayjobs.com/wday/cxs/freseniusmedicalcare/fme/jo |
| R1 RCM | 2 | HTTP 429 for https://r1rcm.wd1.myworkdayjobs.com/wday/cxs/r1rcm/R1RCM/jobs |
| Unilever | 2 | HTTP 429 for https://unilever.wd3.myworkdayjobs.com/wday/cxs/unilever/Unilever_Experienced_Professio |
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Darktrace | 1 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| Equinor | 1 | HTTP 429 for https://equinor.wd3.myworkdayjobs.com/wday/cxs/equinor/EQNR/jobs |
| MassMutual | 1 | HTTP 429 for https://massmutual.wd1.myworkdayjobs.com/wday/cxs/massmutual/mmcareers/jobs |
| RingCentral | 1 | HTTP 429 for https://ringcentral.wd1.myworkdayjobs.com/wday/cxs/ringcentral/RingCentral_Careers/jobs |
| Xcel Energy | 1 | HTTP 429 for https://xcelenergy.wd1.myworkdayjobs.com/wday/cxs/xcelenergy/External/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
