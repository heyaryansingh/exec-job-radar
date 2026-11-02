# Collector status

- Last run: 2026-11-02T08:57:18+00:00 UTC, 445s
- Companies working: 631 of 633
- New roles last run: 1; roles in feed: 1301
- Universe (all other known career sites): 4975 boards, 4140 checked in the last hour, 1 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1171
- Skipped (backing off broken sites): 835; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Home Depot | 1 | 403 Client Error: Forbidden for url: https://careers.homedepot.com/jobsitemap |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
