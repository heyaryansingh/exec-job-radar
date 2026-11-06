# Collector status

- Last run: 2026-11-06T01:05:45+00:00 UTC, 652s
- Companies working: 632 of 633
- New roles last run: 16; roles in feed: 1580
- Universe (all other known career sites): 5119 boards, 4276 checked in the last hour, 0 errors; 0 employer names learned; 20 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 460, "senior titles from boards/aggregators": 220}
- Companies with open roles: 1409
- Skipped (backing off broken sites): 844; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 13 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
