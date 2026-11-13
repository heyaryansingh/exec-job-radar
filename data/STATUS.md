# Collector status

- Last run: 2026-11-13T05:25:50+00:00 UTC, 723s
- Companies working: 633 of 635
- New roles last run: 16; roles in feed: 1493
- Universe (all other known career sites): 5314 boards, 4454 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"jsearch": 28, "senior titles from boards/aggregators": 28}
- Companies with open roles: 1733
- Skipped (backing off broken sites): 861; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 26 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
