# Collector status

- Last run: 2026-10-31T09:34:31+00:00 UTC, 410s
- Companies working: 629 of 630
- New roles last run: 1; roles in feed: 1596
- Universe (all other known career sites): 4950 boards, 4115 checked in the last hour, 2 errors; 0 employer names learned; 2 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 456, "senior titles from boards/aggregators": 203}
- Companies with open roles: 1132
- Skipped (backing off broken sites): 834; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
