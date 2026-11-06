# Collector status

- Last run: 2026-11-06T03:06:02+00:00 UTC, 665s
- Companies working: 632 of 633
- New roles last run: 6; roles in feed: 1593
- Universe (all other known career sites): 5133 boards, 4289 checked in the last hour, 1 errors; 0 employer names learned; 9 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 471, "senior titles from boards/aggregators": 228}
- Companies with open roles: 1413
- Skipped (backing off broken sites): 844; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 13 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
