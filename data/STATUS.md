# Collector status

- Last run: 2026-11-06T10:46:57+00:00 UTC, 700s
- Companies working: 631 of 633
- New roles last run: 8; roles in feed: 1625
- Universe (all other known career sites): 5144 boards, 4297 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 482, "senior titles from boards/aggregators": 238}
- Companies with open roles: 1432
- Skipped (backing off broken sites): 845; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 14 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
