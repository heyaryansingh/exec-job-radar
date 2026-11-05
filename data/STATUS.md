# Collector status

- Last run: 2026-11-05T12:35:40+00:00 UTC, 692s
- Companies working: 632 of 633
- New roles last run: 1; roles in feed: 1547
- Universe (all other known career sites): 5092 boards, 4249 checked in the last hour, 1 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 437, "senior titles from boards/aggregators": 191}
- Companies with open roles: 1356
- Skipped (backing off broken sites): 843; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 12 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
