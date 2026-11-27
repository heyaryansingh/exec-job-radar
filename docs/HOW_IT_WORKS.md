# Exec Job Radar

A Simplify-style feed for senior roles (Director, VP, SVP, MD, Head of, CTO/CIO), plus a
Claude playbook that ranks the best new roles each day, writes tailored materials, fills the
applications in the candidate's own browser, and submits them as far as the candidate allows.

```
 GitHub Actions, hourly (free)            Candidate's computer, 2 runs a day (Claude)
 ┌──────────────────────────────┐         ┌──────────────────────────────────────────┐
 │ ~6,000 employer career sites │         │ self-check (tools/check_setup.py)        │
 │  (Workday, Greenhouse, Lever,│         │ read data/apply_queue.json + job alerts  │
 │   Ashby, SmartRecruiters,    │ ──────▶ │ rank against the real career record      │
 │   Oracle, custom sites)      │  data   │ tailored resume + letter for the best    │
 │ + Indeed, Adzuna, JSearch,   │ branch  │ fill forms in Chrome; submit as far as   │
 │   USAJOBS                    │         │  the autonomy level allows, with proof   │
 │ rule filter: level, domain,  │         │ update tracker + phone dashboard         │
 │  pay, location, freshness    │         └──────────────────────────────────────────┘
 └──────────────────────────────┘                        │
                                                          ▼
                     Candidate: ~10 min a day for clicks, accounts and decisions
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
- `collector/aggregators.py`, `collector/boards.py`: job boards and official aggregator APIs
  (Indeed via python-jobspy, Adzuna, JSearch, USAJOBS and others; keys are repo secrets).
- `.github/workflows/heartbeat.yml`: triggers collection every hour (GitHub's scheduler
  alone is unreliable on free repos).
- `PLAYBOOK.md`: what the daily Claude run does, step by step.
- `ONBOARD.md`: the setup Claude runs for a new candidate (one pasted prompt).
- `tools/check_setup.py`: checks a Job Search folder and the machine; every run starts with it.
- `candidate_template/`: the files that live in the candidate's `Job Search` folder.
- `tools/render_dashboard.py`: turns the tracker into the review page.
- `collector/store.py`: the role database (`data/roles.json`): de-duplication across sources,
  separate openings kept apart by requisition id, repost detection, closed-role detection.
- `collector/readme.py`: renders the README role list and `data/daily/` digests.
- `data/`: written by the collector. Readable pages (`STATUS.md`, `apply_queue.md`, `daily/`)
  are on `main`; the JSON (`roles.json`, `latest.json`, `apply_queue.json`, state) lives on the
  `data` branch, replaced every run so the repo stays small.

Start with [SETUP.md](../SETUP.md).

Local test: `pip install -r requirements.txt pytest && python -m pytest -q tests`
Dry run: `python -m collector.run --dry-run --no-boards`
