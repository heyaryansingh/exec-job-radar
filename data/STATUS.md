# Collector status

- Last run: 2026-11-11T10:39:32+00:00 UTC, 484s
- Companies working: 634 of 635
- New roles last run: 1; roles in feed: 1404
- Universe (all other known career sites): 5265 boards, 4409 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1646
- Skipped (backing off broken sites): 857; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 23 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
