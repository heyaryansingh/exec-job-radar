# Collector status

- Last run: 2026-11-04T15:17:36+00:00 UTC, 872s
- Companies working: 632 of 633
- New roles last run: 7; roles in feed: 1466
- Universe (all other known career sites): 5052 boards, 4209 checked in the last hour, 3 errors; 2 employer names learned; 4 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 454, "senior titles from boards/aggregators": 191}
- Companies with open roles: 1300
- Skipped (backing off broken sites): 841; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
