# Collector status

- Last run: 2026-11-02T22:41:15+00:00 UTC, 639s
- Companies working: 632 of 633
- New roles last run: 17; roles in feed: 1438
- Universe (all other known career sites): 4988 boards, 4153 checked in the last hour, 0 errors; 2 employer names learned; 9 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 345, "senior titles from boards/aggregators": 115}
- Companies with open roles: 1200
- Skipped (backing off broken sites): 836; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 7 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
