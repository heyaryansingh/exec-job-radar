# Collector status

- Last run: 2026-11-12T05:14:22+00:00 UTC, 714s
- Companies working: 634 of 635
- New roles last run: 8; roles in feed: 1479
- Universe (all other known career sites): 5283 boards, 4425 checked in the last hour, 0 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 444, "jsearch": 21, "senior titles from boards/aggregators": 221}
- Companies with open roles: 1685
- Skipped (backing off broken sites): 858; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 25 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
