# Collector status

- Last run: 2026-11-08T00:49:25+00:00 UTC, 494s
- Companies working: 632 of 633
- New roles last run: 1; roles in feed: 1438
- Universe (all other known career sites): 5180 boards, 4327 checked in the last hour, 0 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 383, "senior titles from boards/aggregators": 177}
- Companies with open roles: 1519
- Skipped (backing off broken sites): 854; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 17 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
