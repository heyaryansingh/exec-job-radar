# Collector status

- Last run: 2026-10-20T01:37:29+00:00 UTC, 246s
- Companies working: 510 of 511
- New roles last run: 16; roles in feed: 1260
- Universe (all other known career sites): 4599 boards, 3799 checked in the last hour, 0 errors; 1 employer names learned; 11 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 391, "himalayas": 6, "senior titles from boards/aggregators": 138}
- Companies with open roles: 446
- Skipped (backing off broken sites): 800; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Accenture | 1 | HTTP 429 for https://accenture.wd103.myworkdayjobs.com/wday/cxs/accenture/AccentureCareers/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
