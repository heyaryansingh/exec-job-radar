# Collector status

- Last run: 2026-11-28T12:07:29+00:00 UTC, 792s
- Companies working: 603 of 638
- New roles last run: 2; roles in feed: 1187
- Universe (all other known career sites): 5613 boards, 3836 checked in the last hour, 22 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 160, "senior titles from boards/aggregators": 46}
- Companies with open roles: 1954
- Skipped (backing off broken sites): 1768; ran out of time: 0

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
| Atmos Energy | 2 | HTTP 429 for https://atmosenergy.wd108.myworkdayjobs.com/wday/cxs/atmosenergy/External_Career_Site/j |
| Fresenius Medical Care | 2 | HTTP 429 for https://freseniusmedicalcare.wd3.myworkdayjobs.com/wday/cxs/freseniusmedicalcare/fme/jo |
| Peak6 | 2 | HTTP 429 for https://peak6group.wd1.myworkdayjobs.com/wday/cxs/peak6group/apexfintechsolutions/jobs |
| R1 RCM | 2 | HTTP 429 for https://r1rcm.wd1.myworkdayjobs.com/wday/cxs/r1rcm/R1RCM/jobs |
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Cityblock Health | 1 | HTTP 429 for https://cityblockhealth.wd1.myworkdayjobs.com/wday/cxs/cityblockhealth/CityblockExterna |
| Credit Acceptance | 1 | HTTP 429 for https://creditacceptance.wd5.myworkdayjobs.com/wday/cxs/creditacceptance/Credit_Accepta |
| GlobalFoundries | 1 | HTTP 429 for https://globalfoundries.wd1.myworkdayjobs.com/wday/cxs/globalfoundries/External/jobs |
| Intapp | 1 | HTTP 429 for https://intapp.wd1.myworkdayjobs.com/wday/cxs/intapp/Intapp/jobs |
| Intuit | 1 | HTTP 429 for https://intuitive.wd1.myworkdayjobs.com/wday/cxs/intuitive/irtc_careers/jobs |
| KLA | 1 | HTTP 429 for https://kla.wd1.myworkdayjobs.com/wday/cxs/kla/Search/jobs |
| Masco | 1 | HTTP 429 for https://masco.wd1.myworkdayjobs.com/wday/cxs/masco/masco/jobs |
| MassMutual | 1 | HTTP 429 for https://massmutual.wd1.myworkdayjobs.com/wday/cxs/massmutual/mmcareers/jobs |
| O'Reilly Auto Parts | 1 | HTTP 429 for https://oreillyauto.wd1.myworkdayjobs.com/wday/cxs/oreillyauto/oreilly/jobs |
| ONEOK | 1 | HTTP 429 for https://oneok.wd1.myworkdayjobs.com/wday/cxs/oneok/ONEOK/jobs |
| Old Dominion Freight Line | 1 | HTTP 429 for https://odfl.wd1.myworkdayjobs.com/wday/cxs/odfl/ODFL_Careers/jobs |
| Protiviti | 1 | HTTP 429 for https://roberthalf.wd1.myworkdayjobs.com/wday/cxs/roberthalf/ProtivitiNA/jobs |
| RingCentral | 1 | HTTP 429 for https://ringcentral.wd1.myworkdayjobs.com/wday/cxs/ringcentral/RingCentral_Careers/jobs |
| T. Rowe Price | 1 | HTTP 429 for https://troweprice.wd5.myworkdayjobs.com/wday/cxs/troweprice/TRowePrice/jobs |
| Texas Capital Bank | 1 | HTTP 429 for https://texascapitalbank.wd12.myworkdayjobs.com/wday/cxs/texascapitalbank/Careers/jobs |
| Wellington Management | 1 | HTTP 429 for https://wellington.wd5.myworkdayjobs.com/wday/cxs/wellington/External/jobs |
| Zendesk | 1 | HTTP 429 for https://zendesk.wd1.myworkdayjobs.com/wday/cxs/zendesk/zendesk/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
