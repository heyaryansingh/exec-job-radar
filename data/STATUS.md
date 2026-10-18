# Collector status

- Last run: 2026-10-18T23:52:47+00:00 UTC, 93s
- Companies working: 94 of 105
- New roles last run: 367; roles in feed: 367
- Skipped (backing off broken sites): 0; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| BNY | 3 | 422 Client Error: Unprocessable Entity for url: https://bnymellon.wd1.myworkdayjobs.com/wday/cxs/bny |
| Charles Schwab | 3 | 422 Client Error: Unprocessable Entity for url: https://schwab.wd1.myworkdayjobs.com/wday/cxs/schwab |
| Comcast | 3 | 422 Client Error: Unprocessable Entity for url: https://comcast.wd5.myworkdayjobs.com/wday/cxs/comca |
| Dell Technologies | 3 | 422 Client Error: Unprocessable Entity for url: https://dell.wd1.myworkdayjobs.com/wday/cxs/dell/Ext |
| Northern Trust | 3 | 422 Client Error: Unprocessable Entity for url: https://northerntrust.wd1.myworkdayjobs.com/wday/cxs |
| Walmart | 3 | 422 Client Error: Unprocessable Entity for url: https://walmart.wd5.myworkdayjobs.com/wday/cxs/walma |
| Anduril | 1 | 404 Client Error: Not Found for url: https://boards-api.greenhouse.io/v1/boards/anduril/jobs?content |
| Marqeta | 1 | 404 Client Error: Not Found for url: https://boards-api.greenhouse.io/v1/boards/marqeta/jobs?content |
| Plaid | 1 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/plaid?mode=json |
| Retool | 1 | 404 Client Error: Not Found for url: https://api.ashbyhq.com/posting-api/job-board/retool?includeCom |
| USAA | 1 | 404 Client Error: Not Found for url: https://usaa.wd1.myworkdayjobs.com/wday/cxs/usaa/USAAJOBS/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
