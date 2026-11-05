# Collector status

- Last run: 2026-11-05T01:54:40+00:00 UTC, 669s
- Companies working: 632 of 633
- New roles last run: 2; roles in feed: 1509
- Universe (all other known career sites): 5070 boards, 4227 checked in the last hour, 2 errors; 0 employer names learned; 0 new employer sites found via job boards
- Job boards and aggregators: {"senior titles from boards/aggregators": 0}
- Companies with open roles: 1334
- Skipped (backing off broken sites): 842; ran out of time: 0

## Failing companies

| Company | Failures in a row | Last error |
|---|---:|---|
| Anyscale | 11 | 404 Client Error: Not Found for url: https://api.lever.co/v0/postings/anyscale?mode=json |

Fix an entry with tools/add_company.py, or add `disabled: true` to it in config/companies.yaml.
