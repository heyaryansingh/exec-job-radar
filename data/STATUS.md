# Collector status

- Last run: 2026-11-05T00:06:12+00:00 UTC, 703s
- Companies working: 632 of 633
- New roles last run: 8; roles in feed: 1506
- Universe (all other known career sites): 5065 boards, 4222 checked in the last hour, 0 errors; 0 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 451, "senior titles from boards/aggregators": 198}
- Companies with open roles: 1334
- Skipped (backing off broken sites): 844; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
