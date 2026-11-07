# Collector status

- Last run: 2026-11-07T17:43:23+00:00 UTC, 391s
- Companies working: 631 of 633
- New roles last run: 0; roles in feed: 1634
- Universe (all other known career sites): 5176 boards, 4323 checked in the last hour, 2 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 434, "senior titles from boards/aggregators": 190}
- Companies with open roles: 1512
- Skipped (backing off broken sites): 853; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 16 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
