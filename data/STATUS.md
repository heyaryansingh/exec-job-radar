# Collector status

- Last run: 2026-11-04T18:28:33+00:00 UTC, 832s
- Companies working: 631 of 633
- New roles last run: 2; roles in feed: 1497
- Universe (all other known career sites): 5058 boards, 4215 checked in the last hour, 1 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1307
- Skipped (backing off broken sites): 843; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
