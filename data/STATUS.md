# Collector status

- Last run: 2026-11-02T01:17:02+00:00 UTC, 450s
- Companies working: 632 of 633
- New roles last run: 0; roles in feed: 1286
- Universe (all other known career sites): 4974 boards, 4140 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 137, "senior titles from boards/aggregators": 39}
- Companies with open roles: 1161
- Skipped (backing off broken sites): 832; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 1 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
