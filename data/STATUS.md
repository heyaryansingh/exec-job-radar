# Collector status

- Last run: 2026-11-07T04:14:20+00:00 UTC, 486s
- Companies working: 631 of 633
- New roles last run: 18; roles in feed: 1609
- Universe (all other known career sites): 5168 boards, 4318 checked in the last hour, 1 errors; 0 employer names learned; 1 new employer sites found via job boards
- Job boards and aggregators: {"jsearch": 37, "senior titles from boards/aggregators": 37}
- Companies with open roles: 1494
- Skipped (backing off broken sites): 850; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 15 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |
| Alignment Health | 3 | Expecting value: line 1 column 1 (char 0) |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
