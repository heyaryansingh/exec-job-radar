# Collector status

- Last run: 2026-11-07T10:24:48+00:00 UTC, 474s
- Companies working: 631 of 633
- New roles last run: 4; roles in feed: 1628
- Universe (all other known career sites): 5174 boards, 4321 checked in the last hour, 0 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 441, "senior titles from boards/aggregators": 205}
- Companies with open roles: 1508
- Skipped (backing off broken sites): 855; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 15 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
