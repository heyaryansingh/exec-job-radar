# Collector status

- Last run: 2026-11-07T20:34:07+00:00 UTC, 424s
- Companies working: 632 of 633
- New roles last run: 3; roles in feed: 1637
- Universe (all other known career sites): 5178 boards, 4325 checked in the last hour, 1 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 426, "senior titles from boards/aggregators": 205}
- Companies with open roles: 1516
- Skipped (backing off broken sites): 853; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 16 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
