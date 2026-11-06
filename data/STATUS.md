# Collector status

- Last run: 2026-11-06T17:34:38+00:00 UTC, 531s
- Companies working: 632 of 633
- New roles last run: 16; roles in feed: 1669
- Universe (all other known career sites): 5146 boards, 4298 checked in the last hour, 2 errors; 1 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 471, "senior titles from boards/aggregators": 224}
- Companies with open roles: 1446
- Skipped (backing off broken sites): 847; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 14 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
