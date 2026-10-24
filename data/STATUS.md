# Collector status

- Last run: 2026-10-24T15:03:05+00:00 UTC, 257s
- Companies working: 510 of 511
- New roles last run: 1; roles in feed: 2222
- Universe (all other known career sites): 4826 boards, 3582 checked in the last hour, 0 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 449, "senior titles from boards/aggregators": 204}
- Companies with open roles: 769
- Skipped (backing off broken sites): 1245; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
