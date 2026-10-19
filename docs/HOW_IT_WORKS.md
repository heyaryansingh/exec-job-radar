# Exec Job Radar

A Simplify-style feed for senior roles (Director, VP, SVP, MD, Head of, CTO/CIO), plus a
Claude playbook that ranks the best new roles each day, writes tailored materials, fills the
applications in the candidate's own browser, and leaves them for the candidate to submit.

```
 GitHub Actions, hourly (free)            Candidate's computer, daily (Claude)
 ┌──────────────────────────────┐         ┌──────────────────────────────────────────┐
 │ ~100 company career sites    │         │ read data/latest.json + job-alert emails │
 │  (Workday, Greenhouse, Lever,│         │ rank top 40 against the real resume      │
 │   Ashby, SmartRecruiters,    │ ──────▶ │ pick 5-10, write resume + cover letter   │
 │   Oracle) + Indeed/Google    │  data/  │ fill each form in Chrome, never submit   │
 │ rule filter: level, domain,  │         │ update tracker + dashboard.html          │
 │  pay, location, freshness    │         └──────────────────────────────────────────┘
 └──────────────────────────────┘                        │
                                                          ▼
                                       Candidate reviews and clicks Submit
```

- `collector/`: the hourly scraper and rule filter. Reads each company's applicant-tracking
  system directly, so a full sweep takes minutes and costs nothing.
- `config/search.yaml`: who the search is for (levels, keywords, pay, locations).
- `config/companies.yaml`: the company watchlist. `tools/add_company.py` adds one from a URL.
- `config/discover_seed.txt` + `tools/discover.py`: 1,300+ company names resolved automatically
  to their career sites (direct API probes, the Common Crawl directory in
  `tools/ats_directory.py`, then each company's own careers page).
- `data/STATUS.md`: collector health at a glance.
- `collector/universe.py`: polls every other known career site (the Common Crawl directory
  plus employer sites found through job-board links) and learns each employer's name.
- `collector/aggregators.py`: The Muse and Adzuna official APIs.
- `.github/workflows/heartbeat.yml`: triggers collection every hour (GitHub's scheduler
  alone is unreliable on free repos).
- `PLAYBOOK.md`: what the daily Claude run does, step by step.
- `candidate_template/`: the files that live in the candidate's `Job Search` folder.
- `tools/render_dashboard.py`: turns the tracker into the review page.
- `collector/store.py`: the role database (`data/roles.json`): de-duplication across sources,
  separate openings kept apart by requisition id, repost detection, closed-role detection.
- `collector/readme.py`: renders the README role list and `data/daily/` digests.
- `data/`: written by the collector (`roles.json`, `latest.json`, `health.json`, `STATUS.md`).

Start with [SETUP.md](../SETUP.md).

Local test: `pip install -r requirements.txt pytest && python -m pytest -q tests`
Dry run: `python -m collector.run --dry-run --no-boards`
