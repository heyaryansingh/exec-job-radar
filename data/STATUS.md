# Collector status

- Last run: 2026-11-07T06:03:44+00:00 UTC, 442s
- Companies working: 631 of 633
- New roles last run: 11; roles in feed: 1619
- Universe (all other known career sites): 5169 boards, 4317 checked in the last hour, 3 errors; 0 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 450, "senior titles from boards/aggregators": 218}
- Companies with open roles: 1502
- Skipped (backing off broken sites): 850; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 15 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Alignment Health | 5 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
