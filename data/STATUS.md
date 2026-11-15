# Collector status

- Last run: 2026-11-15T08:31:53+00:00 UTC, 331s
- Companies working: 633 of 635
- New roles last run: 1; roles in feed: 1342
- Universe (all other known career sites): 5357 boards, 3831 checked in the last hour, 1 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 243, "senior titles from boards/aggregators": 72}
- Companies with open roles: 1796
- Skipped (backing off broken sites): 1526; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 31 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
