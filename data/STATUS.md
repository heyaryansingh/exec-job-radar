# Collector status

- Last run: 2026-11-11T17:31:55+00:00 UTC, 607s
- Companies working: 634 of 635
- New roles last run: 12; roles in feed: 1446
- Universe (all other known career sites): 5269 boards, 4410 checked in the last hour, 2 errors; 1 employer names learned; 7 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 453, "senior titles from boards/aggregators": 226}
- Companies with open roles: 1654
- Skipped (backing off broken sites): 858; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 24 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
