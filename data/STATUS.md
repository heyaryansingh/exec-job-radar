# Collector status

- Last run: 2026-10-24T10:13:13+00:00 UTC, 269s
- Companies working: 506 of 511
- New roles last run: 3; roles in feed: 2216
- Universe (all other known career sites): 4823 boards, 3580 checked in the last hour, 2 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 454, "senior titles from boards/aggregators": 211}
- Companies with open roles: 767
- Skipped (backing off broken sites): 1242; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |
| Forrester | 3 | Expecting value: line 1 column 1 (char 0) |
| Golub Capital | 3 | Expecting value: line 1 column 1 (char 0) |
| J.B. Hunt | 3 | Expecting value: line 1 column 1 (char 0) |
| Nordstrom | 3 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
