# Collector status

- Last run: 2026-11-06T05:55:46+00:00 UTC, 641s
- Companies working: 632 of 633
- New roles last run: 3; roles in feed: 1611
- Universe (all other known career sites): 5142 boards, 4296 checked in the last hour, 2 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 467, "senior titles from boards/aggregators": 228}
- Companies with open roles: 1423
- Skipped (backing off broken sites): 845; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 13 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
