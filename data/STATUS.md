# Collector status

- Last run: 2026-11-13T04:25:25+00:00 UTC, 701s
- Companies working: 633 of 635
- New roles last run: 5; roles in feed: 1477
- Universe (all other known career sites): 5310 boards, 4450 checked in the last hour, 0 errors; 0 employer names learned; 4 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 463, "senior titles from boards/aggregators": 219}
- Companies with open roles: 1731
- Skipped (backing off broken sites): 861; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 26 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 5 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
