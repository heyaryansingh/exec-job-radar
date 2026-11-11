# Collector status

- Last run: 2026-11-11T15:36:19+00:00 UTC, 555s
- Companies working: 634 of 635
- New roles last run: 4; roles in feed: 1428
- Universe (all other known career sites): 5266 boards, 4409 checked in the last hour, 0 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 455, "senior titles from boards/aggregators": 240}
- Companies with open roles: 1651
- Skipped (backing off broken sites): 858; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 23 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
