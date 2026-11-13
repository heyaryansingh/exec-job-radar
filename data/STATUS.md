# Collector status

- Last run: 2026-11-13T18:57:47+00:00 UTC, 796s
- Companies working: 633 of 635
- New roles last run: 7; roles in feed: 1576
- Universe (all other known career sites): 5322 boards, 4459 checked in the last hour, 3 errors; 0 employer names learned; 6 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 467, "senior titles from boards/aggregators": 205}
- Companies with open roles: 1752
- Skipped (backing off broken sites): 861; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 28 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 7 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
