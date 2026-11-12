# Collector status

- Last run: 2026-11-12T08:03:16+00:00 UTC, 640s
- Companies working: 634 of 635
- New roles last run: 5; roles in feed: 1485
- Universe (all other known career sites): 5285 boards, 4426 checked in the last hour, 1 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 446, "senior titles from boards/aggregators": 212}
- Companies with open roles: 1690
- Skipped (backing off broken sites): 859; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 25 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
