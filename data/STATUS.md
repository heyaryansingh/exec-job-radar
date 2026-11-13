# Collector status

- Last run: 2026-11-13T09:15:28+00:00 UTC, 689s
- Companies working: 633 of 635
- New roles last run: 7; roles in feed: 1502
- Universe (all other known career sites): 5316 boards, 4453 checked in the last hour, 2 errors; 0 employer names learned; 4 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 465, "senior titles from boards/aggregators": 210}
- Companies with open roles: 1739
- Skipped (backing off broken sites): 863; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 27 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
