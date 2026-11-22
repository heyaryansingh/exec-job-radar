# Collector status

- Last run: 2026-11-22T04:11:00+00:00 UTC, 891s
- Companies working: 612 of 636
- New roles last run: 0; roles in feed: 1339
- Universe (all other known career sites): 5503 boards, 3810 checked in the last hour, 787 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 311, "senior titles from boards/aggregators": 150}
- Companies with open roles: 1968
- Skipped (backing off broken sites): 924; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 44 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 23 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Seismic | 15 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/seismic-change.co |
| athenahealth | 11 | HTTP 429 for https://athenahealth.wd1.myworkdayjobs.com/wday/cxs/athenahealth/External/jobs |
| Cedar | 10 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/cedar?includeComp |
| Williams-Sonoma | 9 | HTTP 429 for https://williams.wd5.myworkdayjobs.com/wday/cxs/williams/External/jobs |
| Workday | 9 | HTTP 429 for https://workday.wd5.myworkdayjobs.com/wday/cxs/workday/Workday/jobs |
| Albemarle | 7 | HTTP 429 for https://albemarle.wd5.myworkdayjobs.com/wday/cxs/albemarle/External/jobs |
| Ameriprise Financial | 7 | HTTP 429 for https://ameriprise.wd5.myworkdayjobs.com/wday/cxs/ameriprise/Ameriprise/jobs |
| Blackstone | 7 | HTTP 429 for https://blackstone.wd1.myworkdayjobs.com/wday/cxs/blackstone/Blackstone_Careers/jobs |
| Darktrace | 7 | HTTP 429 for https://darktrace.wd3.myworkdayjobs.com/wday/cxs/darktrace/DarktaceExternal/jobs |
| DataRobot | 7 | HTTP 429 for https://datarobot.wd1.myworkdayjobs.com/wday/cxs/datarobot/DataRobot_External_Careers/j |
| Disney | 7 | HTTP 429 for https://disney.wd5.myworkdayjobs.com/wday/cxs/disney/disneycareer/jobs |
| Proofpoint | 7 | HTTP 429 for https://proofpoint.wd5.myworkdayjobs.com/wday/cxs/proofpoint/proofpointcareers/jobs |
| The Hartford | 7 | HTTP 429 for https://thehartford.wd5.myworkdayjobs.com/wday/cxs/thehartford/Careers_External/jobs |
| Travelers | 7 | HTTP 429 for https://travelers.wd5.myworkdayjobs.com/wday/cxs/travelers/External/jobs |
| Illumina | 6 | HTTP 429 for https://illumina.wd1.myworkdayjobs.com/wday/cxs/illumina/illumina-careers/jobs |
| LendingClub | 6 | HTTP 429 for https://lendingclub.wd1.myworkdayjobs.com/wday/cxs/lendingclub/External/jobs |
| Santander | 3 | HTTP 429 for https://santander.wd3.myworkdayjobs.com/wday/cxs/santander/SantanderCareers/jobs |
| LSEG | 2 | HTTP 429 for https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs |
| Ovintiv | 2 | HTTP 429 for https://ovintiv.wd3.myworkdayjobs.com/wday/cxs/ovintiv/ovintivcareers/jobs |
| Fresenius Medical Care | 1 | HTTP 429 for https://freseniusmedicalcare.wd3.myworkdayjobs.com/wday/cxs/freseniusmedicalcare/fme/jo |
| Kohl's | 1 | HTTP 429 for https://kohls.wd504.myworkdayjobs.com/wday/cxs/kohls/kohlscareers/jobs |
| Realty Income | 1 | HTTP 429 for https://realtyincome.wd108.myworkdayjobs.com/wday/cxs/realtyincome/realty_income_career |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
