# Collector status

- Last run: 2026-11-06T12:47:26+00:00 UTC, 718s
- Companies working: 632 of 633
- New roles last run: 3; roles in feed: 1628
- Universe (all other known career sites): 5144 boards, 4297 checked in the last hour, 0 errors; 1 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 482, "senior titles from boards/aggregators": 235}
- Companies with open roles: 1434
- Skipped (backing off broken sites): 848; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 14 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
