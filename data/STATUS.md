# Collector status

- Last run: 2026-10-30T21:08:42+00:00 UTC, 704s
- Companies working: 629 of 630
- New roles last run: 19; roles in feed: 1936
- Universe (all other known career sites): 4918 boards, 4087 checked in the last hour, 0 errors; 2 employer names learned; 7 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 468, "senior titles from boards/aggregators": 217}
- Companies with open roles: 1083
- Skipped (backing off broken sites): 831; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| ONEOK | 1 | HTTP 429 for https://oneok.wd1.myworkdayjobs.com/wday/cxs/oneok/ONEOK/jobs |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
