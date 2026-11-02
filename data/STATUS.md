# Collector status

- Last run: 2026-11-02T15:52:44+00:00 UTC, 750s
- Companies working: 632 of 633
- New roles last run: 7; roles in feed: 1329
- Universe (all other known career sites): 4976 boards, 4140 checked in the last hour, 1 errors; 2 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 186, "senior titles from boards/aggregators": 57}
- Companies with open roles: 1178
- Skipped (backing off broken sites): 836; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
