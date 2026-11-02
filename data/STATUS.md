# Collector status

- Last run: 2026-11-02T20:42:12+00:00 UTC, 702s
- Companies working: 632 of 633
- New roles last run: 18; roles in feed: 1408
- Universe (all other known career sites): 4985 boards, 4150 checked in the last hour, 2 errors; 0 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 319, "senior titles from boards/aggregators": 113}
- Companies with open roles: 1191
- Skipped (backing off broken sites): 834; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 7 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
