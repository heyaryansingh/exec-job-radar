# Collector status

- Last run: 2026-11-13T07:16:44+00:00 UTC, 761s
- Companies working: 633 of 635
- New roles last run: 1; roles in feed: 1494
- Universe (all other known career sites): 5314 boards, 4451 checked in the last hour, 4 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 464, "senior titles from boards/aggregators": 222}
- Companies with open roles: 1734
- Skipped (backing off broken sites): 861; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 27 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
