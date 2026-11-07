# Collector status

- Last run: 2026-11-07T03:14:35+00:00 UTC, 505s
- Companies working: 631 of 633
- New roles last run: 6; roles in feed: 1591
- Universe (all other known career sites): 5166 boards, 4316 checked in the last hour, 2 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 449, "senior titles from boards/aggregators": 210}
- Companies with open roles: 1482
- Skipped (backing off broken sites): 849; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 15 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Alignment Health | 2 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
