# Collector status

- Last run: 2026-11-25T00:52:09+00:00 UTC, 743s
- Companies working: 602 of 638
- New roles last run: 1; roles in feed: 1286
- Universe (all other known career sites): 5564 boards, 3853 checked in the last hour, 91 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1996
- Skipped (backing off broken sites): 1641; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 49 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 28 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 21 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| Cedar | 15 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| LendingClub | 12 | HTTP 429 for https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/lendingclub/External/jobs |
| Arctic Wolf | 7 | HTTP 429 for https://arcticwolf.wd1.myworkdayjobs.com/wday/cxs/arcticwolf/External/jobs |
| Centene | 7 | HTTP 429 for https://centene.wd5.myworkdayjobs.com/wday/cxs/centene/Centene_External/jobs |
| Dimensional Fund Advisors | 7 | HTTP 429 for https://dimensional.wd5.myworkdayjobs.com/wday/cxs/dimensional/DFA_Careers/jobs |
| Dow | 7 | HTTP 429 for https://dow.wd1.myworkdayjobs.com/wday/cxs/dow/ExternalCareers/jobs |
| Martin Marietta | 7 | HTTP 429 for https://martinmarietta.wd5.myworkdayjobs.com/wday/cxs/martinmarietta/Martin_Marietta_Ca |
| Rackspace | 7 | HTTP 429 for https://rackspace.wd1.myworkdayjobs.com/wday/cxs/rackspace/External/jobs |
| Viatris | 7 | HTTP 429 for https://viatris.wd5.myworkdayjobs.com/wday/cxs/viatris/External/jobs |
| Voya Financial | 7 | HTTP 429 for https://godirect.wd5.myworkdayjobs.com/wday/cxs/godirect/voya_jobs/jobs |
| Darktrace | 6 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| Equinor | 6 | HTTP 429 for https://equinor.wd3.myworkdayjobs.com/wday/cxs/equinor/EQNR/jobs |
| GlobalFoundries | 6 | HTTP 429 for https://globalfoundries.wd1.myworkdayjobs.com/wday/cxs/globalfoundries/External/jobs |
| Grubhub | 6 | HTTP 429 for https://wonder.wd1.myworkdayjobs.com/wday/cxs/wonder/Grubhub_Careers/jobs |
| Ovintiv | 6 | HTTP 429 for https://ovintiv.wd3.myworkdayjobs.com/wday/cxs/ovintiv/ovintivcareers/jobs |
| RingCentral | 6 | HTTP 429 for https://ringcentral.wd1.myworkdayjobs.com/wday/cxs/ringcentral/RingCentral_Careers/jobs |
| Thoughtworks | 6 | 404 Client Error: Not Found for url: https://boards-api.greenhouse.io/v1/boards/thoughtworks/jobs |
| Unisys | 6 | HTTP 429 for https://unisys.wd5.myworkdayjobs.com/wday/cxs/unisys/External/jobs |
| Accenture | 4 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |
| Credit Acceptance | 2 | HTTP 429 for https://creditacceptance.wd5.myworkdayjobs.com/wday/cxs/creditacceptance/Credit_Accepta |
| LSEG | 2 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| Old Dominion Freight Line | 2 | HTTP 429 for https://odfl.wd1.myworkdayjobs.com/wday/cxs/odfl/ODFL_Careers/jobs |
| United Rentals | 2 | HTTP 429 for https://ur.wd1.myworkdayjobs.com/wday/cxs/ur/URcareers/jobs |
| Zoetis | 2 | HTTP 429 for https://zoetis.wd5.myworkdayjobs.com/wday/cxs/zoetis/zoetis/jobs |
| Amgen | 1 | HTTP 429 for https://amgen.wd1.myworkdayjobs.com/wday/cxs/amgen/Careers/jobs |
| Baxter | 1 | HTTP 429 for https://baxter.wd1.myworkdayjobs.com/wday/cxs/baxter/baxter/jobs |
| Danaher | 1 | HTTP 429 for https://danaher.wd1.myworkdayjobs.com/wday/cxs/danaher/DanaherJobs/jobs |
| Global Payments | 1 | HTTP 429 for https://global.wd1.myworkdayjobs.com/wday/cxs/global/globalpartnerscareers/jobs |
| Huron Consulting | 1 | HTTP 429 for https://huron.wd1.myworkdayjobs.com/wday/cxs/huron/huroncareers/jobs |
| Logitech | 1 | HTTP 429 for https://logitech.wd5.myworkdayjobs.com/wday/cxs/logitech/Logitech/jobs |
| Masco | 1 | HTTP 429 for https://masco.wd1.myworkdayjobs.com/wday/cxs/masco/masco/jobs |
| Shell | 1 | HTTP 429 for https://shell.wd3.myworkdayjobs.com/wday/cxs/shell/ShellCareers/jobs |
| Simon Property Group | 1 | HTTP 429 for https://simon.wd1.myworkdayjobs.com/wday/cxs/simon/Simon/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
