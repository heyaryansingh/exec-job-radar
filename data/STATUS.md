# Collector status

- Last run: 2026-11-12T19:45:49+00:00 UTC, 754s
- Companies working: 634 of 635
- New roles last run: 24; roles in feed: 1569
- Universe (all other known career sites): 5292 boards, 4432 checked in the last hour, 1 errors; 2 employer names learned; 10 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 454, "senior titles from boards/aggregators": 204}
- Companies with open roles: 1713
- Skipped (backing off broken sites): 860; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 26 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
