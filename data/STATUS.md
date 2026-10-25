# Collector status

- Last run: 2026-10-25T03:34:26+00:00 UTC, 288s
- Companies working: 510 of 511
- New roles last run: 2; roles in feed: 2248
- Universe (all other known career sites): 4840 boards, 3596 checked in the last hour, 0 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 256, "senior titles from boards/aggregators": 85}
- Companies with open roles: 786
- Skipped (backing off broken sites): 1245; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 7 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
