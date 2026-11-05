# Collector status

- Last run: 2026-11-05T10:34:26+00:00 UTC, 620s
- Companies working: 632 of 633
- New roles last run: 3; roles in feed: 1544
- Universe (all other known career sites): 5090 boards, 4247 checked in the last hour, 1 errors; 1 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 442, "senior titles from boards/aggregators": 189}
- Companies with open roles: 1355
- Skipped (backing off broken sites): 843; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 12 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
