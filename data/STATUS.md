# Collector status

- Last run: 2026-11-05T04:45:09+00:00 UTC, 680s
- Companies working: 631 of 633
- New roles last run: 0; roles in feed: 1529
- Universe (all other known career sites): 5078 boards, 4235 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1345
- Skipped (backing off broken sites): 844; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Discover | 1 | HTTP 429 for https://ensign.wd1.myworkdayjobs.com/wday/cxs/ensign/DiscoveryCareerSite/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
