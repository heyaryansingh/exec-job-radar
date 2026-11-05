# Collector status

- Last run: 2026-11-05T22:14:28+00:00 UTC, 736s
- Companies working: 632 of 633
- New roles last run: 27; roles in feed: 1671
- Universe (all other known career sites): 5107 boards, 4264 checked in the last hour, 0 errors; 0 employer names learned; 24 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 450, "senior titles from boards/aggregators": 222}
- Companies with open roles: 1397
- Skipped (backing off broken sites): 843; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 13 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
