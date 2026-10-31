# Collector status

- Last run: 2026-10-31T01:57:46+00:00 UTC, 632s
- Companies working: 629 of 630
- New roles last run: 8; roles in feed: 1552
- Universe (all other known career sites): 4929 boards, 4095 checked in the last hour, 3 errors; 0 employer names learned; 17 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 459, "senior titles from boards/aggregators": 213}
- Companies with open roles: 1099
- Skipped (backing off broken sites): 831; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 1 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
