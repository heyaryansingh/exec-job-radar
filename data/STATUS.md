# Collector status

- Last run: 2026-11-07T01:19:25+00:00 UTC, 792s
- Companies working: 632 of 633
- New roles last run: 16; roles in feed: 1582
- Universe (all other known career sites): 5159 boards, 4311 checked in the last hour, 789 errors; 0 employer names learned; 9 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 450, "senior titles from boards/aggregators": 209}
- Companies with open roles: 1477
- Skipped (backing off broken sites): 60; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 15 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
