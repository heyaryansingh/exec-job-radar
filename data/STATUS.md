# Collector status

- Last run: 2026-11-13T00:35:22+00:00 UTC, 708s
- Companies working: 634 of 635
- New roles last run: 11; roles in feed: 1464
- Universe (all other known career sites): 5303 boards, 4440 checked in the last hour, 4 errors; 1 employer names learned; 4 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 455, "senior titles from boards/aggregators": 229}
- Companies with open roles: 1727
- Skipped (backing off broken sites): 860; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 26 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
