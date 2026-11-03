# Collector status

- Last run: 2026-11-03T03:32:14+00:00 UTC, 689s
- Companies working: 632 of 633
- New roles last run: 21; roles in feed: 1309
- Universe (all other known career sites): 5002 boards, 4166 checked in the last hour, 2 errors; 0 employer names learned; 6 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 386, "jsearch": 27, "senior titles from boards/aggregators": 188}
- Companies with open roles: 1227
- Skipped (backing off broken sites): 835; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 7 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
