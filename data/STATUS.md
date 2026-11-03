# Collector status

- Last run: 2026-11-03T08:22:21+00:00 UTC, 666s
- Companies working: 632 of 633
- New roles last run: 5; roles in feed: 1324
- Universe (all other known career sites): 5010 boards, 4173 checked in the last hour, 1 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 392, "senior titles from boards/aggregators": 161}
- Companies with open roles: 1232
- Skipped (backing off broken sites): 837; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 8 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
