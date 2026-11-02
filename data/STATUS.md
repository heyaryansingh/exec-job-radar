# Collector status

- Last run: 2026-11-02T03:16:34+00:00 UTC, 418s
- Companies working: 632 of 633
- New roles last run: 11; roles in feed: 1297
- Universe (all other known career sites): 4974 boards, 4140 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 131, "jsearch": 25, "senior titles from boards/aggregators": 66}
- Companies with open roles: 1170
- Skipped (backing off broken sites): 834; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 3 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
