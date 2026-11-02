# Collector status

- Last run: 2026-11-02T08:07:01+00:00 UTC, 434s
- Companies working: 632 of 633
- New roles last run: 1; roles in feed: 1300
- Universe (all other known career sites): 4974 boards, 4139 checked in the last hour, 3 errors; 0 employer names learned; 3 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 134, "senior titles from boards/aggregators": 42}
- Companies with open roles: 1170
- Skipped (backing off broken sites): 833; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 6 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
