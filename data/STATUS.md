# Collector status

- Last run: 2026-10-31T11:34:01+00:00 UTC, 384s
- Companies working: 629 of 630
- New roles last run: 2; roles in feed: 1600
- Universe (all other known career sites): 4951 boards, 4116 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 453, "senior titles from boards/aggregators": 198}
- Companies with open roles: 1134
- Skipped (backing off broken sites): 836; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
