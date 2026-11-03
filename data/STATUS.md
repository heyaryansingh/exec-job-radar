# Collector status

- Last run: 2026-11-03T20:53:40+00:00 UTC, 679s
- Companies working: 632 of 633
- New roles last run: 15; roles in feed: 1416
- Universe (all other known career sites): 5021 boards, 4183 checked in the last hour, 1 errors; 2 employer names learned; 10 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 417, "senior titles from boards/aggregators": 186}
- Companies with open roles: 1258
- Skipped (backing off broken sites): 838; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 9 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
