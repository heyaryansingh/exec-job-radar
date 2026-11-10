# Collector status

- Last run: 2026-11-10T21:10:57+00:00 UTC, 608s
- Companies working: 633 of 635
- New roles last run: 19; roles in feed: 1406
- Universe (all other known career sites): 5237 boards, 4382 checked in the last hour, 1 errors; 1 employer names learned; 11 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 434, "senior titles from boards/aggregators": 195}
- Companies with open roles: 1615
- Skipped (backing off broken sites): 855; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 22 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
