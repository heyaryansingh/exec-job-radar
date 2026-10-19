# JSearch test (1 API call)

- /search-v2: HTTP 200 '{"status":"OK","request_id":"972afee5-a9d6-4fe4-abb3-440dfe256576","parameters":{"query":"'
HTTP 200 via /search-v2
- x-ratelimit-requests-limit: 200
- x-ratelimit-requests-remaining: 196

Response shape: dict keys ['status', 'request_id', 'parameters', 'data']
```
{"status":"OK","request_id":"972afee5-a9d6-4fe4-abb3-440dfe256576","parameters":{"query":"vice president technology in USA","num_pages":1,"date_posted":"week","country":"us","language":"en"},"data":{"jobs":[{"job_id":"ZlZrT2VZUE5WblBYNjNZbkFBQUFBQT09OkVzd0JDb3dCUVVwcFZEUjBTVGw1VUVjelpuSTRSakUxU1V0T01sZGlObWhxY0dOaWVrUnZSM0Z0YldWSVZYQnJTMHgwVTA5VFRHdHlUM05vWWt3dFZubzRYMFZrYlVsdGJ6QkJVMGMzVlhsTkxVTk
```
- results: 10
- senior titles passing the rules: 8
- publishers: LinkedIn 3, Smart Recruiters Jobs 1, TriSearch 1, EFinancialCareers 1, Jobgether 1, Built In Boston 1, Hitachi Careers - Hitachi Global 1, CVS Health Careers 1

| Employer | Title | Via | Apply link |
|---|---|---|---|
| Korn Ferry | Vice President of Technology | LinkedIn | https://www.linkedin.com/jobs/view/vice-president-of-technology-at-korn-ferry-44 |
| M3USA | Vice President, Technology and Product (Remote) | Smart Recruiters Jobs | https://jobs.smartrecruiters.com/M3USA/744000155833950-vice-president-technology |
| Trisearch | Vice President Information Technology | TriSearch | https://www.trisearch.com/job-details/vice-president-information-technology-in-j |
| Unum Group | Senior Vice President, Technology Strategy & Enablement | Portland, OR, USA | EFinancialCareers | https://www.efinancialcareers.com/jobs-United_States-OR-Portland-Senior_Vice_Pre |
| M3 USA | Vice President, Technology and Product (Remote) | Jobgether | https://jobgether.com/offer/6ad1b6c749c73d7b9986dd1e-vice-president-technology-a |
| Boston Energy Trading and Marketing | Sr. Vice President, IT | Built In Boston | https://www.builtinboston.com/job/sr-vice-president-it/11661988 |
| Hitachi Global | Vice President of Information Technology | Hitachi Careers - Hitachi Global | https://careers.hitachi.com/vice-president-of-information-technology/job/R014154 |
| Axos Bank | SVP, Technology Strategy & Operations | LinkedIn | https://www.linkedin.com/jobs/view/svp-technology-strategy-operations-at-axos-ba |
| CVS Health | Associate Vice President, Technology Product Management | CVS Health Careers | https://jobs.cvshealth.com/us/en/job/R1045102/Associate-Vice-President-Technolog |
| MicroSurgical Technology | Vice President, North America Sales | LinkedIn | https://www.linkedin.com/jobs/view/vice-president-north-america-sales-at-microsu |
