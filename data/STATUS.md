# Collector status

- Last run: 2026-11-04T12:23:03+00:00 UTC, 615s
- Companies working: 632 of 633
- New roles last run: 2; roles in feed: 1456
- Universe (all other known career sites): 5051 boards, 4211 checked in the last hour, 3 errors; 1 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 454, "senior titles from boards/aggregators": 193}
- Companies with open roles: 1294
- Skipped (backing off broken sites): 838; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
