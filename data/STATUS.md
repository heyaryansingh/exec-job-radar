# Collector status

- Last run: 2026-11-09T22:58:50+00:00 UTC, 561s
- Companies working: 634 of 635
- New roles last run: 20; roles in feed: 1429
- Universe (all other known career sites): 5205 boards, 4350 checked in the last hour, 1 errors; 1 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 374, "senior titles from boards/aggregators": 139}
- Companies with open roles: 1571
- Skipped (backing off broken sites): 855; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 20 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
