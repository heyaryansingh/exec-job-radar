# Collector status

- Last run: 2026-11-02T12:57:56+00:00 UTC, 466s
- Companies working: 632 of 633
- New roles last run: 5; roles in feed: 1309
- Universe (all other known career sites): 4975 boards, 4140 checked in the last hour, 0 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 155, "senior titles from boards/aggregators": 52}
- Companies with open roles: 1172
- Skipped (backing off broken sites): 836; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
