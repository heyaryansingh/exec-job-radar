# Collector status

- Last run: 2026-11-06T07:57:55+00:00 UTC, 760s
- Companies working: 632 of 633
- New roles last run: 6; roles in feed: 1616
- Universe (all other known career sites): 5143 boards, 4294 checked in the last hour, 5 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 467, "senior titles from boards/aggregators": 230}
- Companies with open roles: 1425
- Skipped (backing off broken sites): 845; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 13 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
