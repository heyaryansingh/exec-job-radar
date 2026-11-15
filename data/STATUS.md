# Collector status

- Last run: 2026-11-15T06:32:04+00:00 UTC, 347s
- Companies working: 632 of 635
- New roles last run: 0; roles in feed: 1341
- Universe (all other known career sites): 5357 boards, 3832 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1796
- Skipped (backing off broken sites): 1525; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 30 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 9 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
