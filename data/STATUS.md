# Collector status

- Last run: 2026-10-24T19:53:16+00:00 UTC, 255s
- Companies working: 510 of 511
- New roles last run: 5; roles in feed: 2231
- Universe (all other known career sites): 4831 boards, 3587 checked in the last hour, 0 errors; 0 employer names learned; 5 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 424, "senior titles from boards/aggregators": 179}
- Companies with open roles: 775
- Skipped (backing off broken sites): 1245; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 7 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
