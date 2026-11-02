# Collector status

- Last run: 2026-11-02T17:52:14+00:00 UTC, 722s
- Companies working: 632 of 633
- New roles last run: 13; roles in feed: 1356
- Universe (all other known career sites): 4977 boards, 4142 checked in the last hour, 0 errors; 1 employer names learned; 9 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 255, "senior titles from boards/aggregators": 82}
- Companies with open roles: 1183
- Skipped (backing off broken sites): 836; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
