# Collector status

- Last run: 2026-11-15T15:22:17+00:00 UTC, 332s
- Companies working: 634 of 636
- New roles last run: 0; roles in feed: 1344
- Universe (all other known career sites): 5356 boards, 3830 checked in the last hour, 1 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"board-indeed (raw)": 197, "senior titles from boards/aggregators": 49}
- Companies with open roles: 1797
- Skipped (backing off broken sites): 1527; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 31 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| MetLife | 10 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/metlife?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
