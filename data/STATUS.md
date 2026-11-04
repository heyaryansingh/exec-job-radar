# Collector status

- Last run: 2026-11-04T02:42:53+00:00 UTC, 633s
- Companies working: 631 of 633
- New roles last run: 12; roles in feed: 1417
- Universe (all other known career sites): 5038 boards, 4201 checked in the last hour, 0 errors; 0 employer names learned; 6 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 444, "senior titles from boards/aggregators": 216}
- Companies with open roles: 1282
- Skipped (backing off broken sites): 838; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 9 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Anduril Industries | 1 | HTTPSConnectionPool(host='boards-api.greenhouse.io', port=443): Read timed out. (read timeout=25) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
