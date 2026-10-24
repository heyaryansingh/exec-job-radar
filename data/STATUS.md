# Collector status

- Last run: 2026-10-24T05:29:16+00:00 UTC, 652s
- Companies working: 508 of 511
- New roles last run: 1; roles in feed: 2207
- Universe (all other known career sites): 4816 boards, 4000 checked in the last hour, 3 errors; 0 employer names learned; 4 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 451, "senior titles from boards/aggregators": 208}
- Companies with open roles: 764
- Skipped (backing off broken sites): 813; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Alignment Health | 6 | Expecting value: line 1 column 1 (char 0) |
| Kohl's | 1 | HTTP 503 for https://kohls.wd504.myworkdayjobs.com/wday/cxs/kohls/kohlscareers/jobs |
| Petco | 1 | HTTP 503 for https://petco.wd504.myworkdayjobs.com/wday/cxs/petco/External/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
