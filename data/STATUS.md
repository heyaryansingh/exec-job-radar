# Collector status

- Last run: 2026-11-05T15:26:10+00:00 UTC, 710s
- Companies working: 631 of 633
- New roles last run: 15; roles in feed: 1566
- Universe (all other known career sites): 5093 boards, 4250 checked in the last hour, 1 errors; 2 employer names learned; 4 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 441, "senior titles from boards/aggregators": 206}
- Companies with open roles: 1364
- Skipped (backing off broken sites): 843; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 12 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
