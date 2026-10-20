# Setup

Two parts: **A** puts the hourly collector on GitHub (free, about 15 minutes, done once by
whoever is comfortable with GitHub). **B** sets up the candidate's own computer and Claude
account (about 30 minutes, done with the candidate).

---

## A. The hourly collector (GitHub)

1. **Create the repository.** Sign in at github.com, click **New repository**, name it
   `exec-job-radar`, choose **Public**, and create it empty.
   Public is recommended: the repo only holds code, search rules and public job postings
   (no personal details), and public repos get unlimited free GitHub Actions minutes.
   A private repo works too, but the hourly runs will use up the free monthly minutes.
2. **Upload the code.** From a terminal in this folder:
   ```
   git init -b main
   git add .
   git commit -m "Job radar"
   git remote add origin https://github.com/<you>/exec-job-radar.git
   git push -u origin main
   ```
   (Or use GitHub Desktop. If you upload through the website instead, make sure the hidden
   `.github` folder comes along; on a Mac press Cmd+Shift+. in Finder to show it.)
3. **Let the workflows save results.** Repo **Settings → Actions → General → Workflow
   permissions → Read and write permissions → Save**.
4. **Check the company list.** **Actions** tab → enable workflows if asked → **Validate
   companies → Run workflow**. When it finishes, open the run's log: the last lines list any
   company whose career site didn't respond. Fix those entries (see "Adding companies") or
   add `disabled: true` to them.
5. **Grow the watchlist.** **Actions → Discover companies → Run workflow.** It resolves every
   name in `config/discover_seed.txt` (1,300+ companies) to its career site and adds the ones
   that return jobs to `config/companies.yaml`. It takes one to two hours the first time. Names
   it isn't sure about land in `data/discover_review.md`; names it can't find are retried
   automatically every week. To add companies later, add lines to the seed file and push.
6. **Start collecting.** **Actions → Collect roles → Run workflow** once by hand. After that
   it runs every hour on its own. The repo's front page (README) becomes the live role list,
   Simplify-style: grouped by function, newest first, with Apply links, pay, level, age,
   🆕 new and 🔒 closed markers, and a digest for each day in `data/daily/`. The Claude run
   reads `data/apply_queue.json` and `data/latest.json`; the full role database is
   `data/roles.json`. These three (and the collector's state files) live on the `data`
   branch, which is replaced on every run so the repository doesn't grow by megabytes a day.

7. **Turn on the heartbeat.** It starts by itself on the first push. To check: **Actions →
   Heartbeat** should show one run in progress. It triggers "Collect roles" every hour,
   because GitHub's own scheduler often skips hourly runs on free repositories.
8. **Optional: Adzuna** (a large job aggregator with an official free API). Sign up at
   developer.adzuna.com, then add two repository secrets under **Settings → Secrets and
   variables → Actions**: `ADZUNA_APP_ID` and `ADZUNA_APP_KEY`. Without them it is skipped.

### Testing changes before they go live
Edits to the collector code run **Actions → Collect (test)** first: a report-only run on a
sample of 600 career sites plus every job source, written to `data/test_reports/collect.md`.
The live feed picks up code changes on its next hourly run. Discovery changes have the same
kind of test (**Discover (test)**, report in `data/test_reports/discover.md`).

### Keeping it healthy
- `data/STATUS.md` shows, at a glance: last run, how many company sites are working, and a
  table of failing ones with their errors.
- The "universe" (every other known career site, several thousand) is read in a rotating
  order within each run's time budget, so each one is visited every few hours while the
  watchlist is read every hour. Switch it off with `universe: enabled: false` in
  config/search.yaml.
- Broken sites are backed off automatically (retried every 12 hours after 6 straight failures),
  so one bad entry never slows the whole run. Each hourly run has a 40-minute budget and
  checks the least recently checked companies first.
- If more than half the sites fail in one run (a sign of something systemic), the run is
  marked failed and GitHub emails the repo owner. Results are still saved.

### Retargeting for a different person
Edit `config/search.yaml`: seniority patterns, domain keywords, minimum pay, locations and
job-board search terms. No code changes are needed.

### Adding companies
Open any job posting at the company, copy the address bar URL, then:
```
python tools/add_company.py "<url>" "Company Name" 1 bank
```
It recognizes Workday, Greenhouse, Lever, Ashby, SmartRecruiters and Oracle career sites.
Companies with fully custom sites (Goldman Sachs, Amazon, Google, ...) go in the candidate's
`extra_career_sites` list instead; the job-board sweep also catches many of their roles.

---

## B. The candidate's computer

The candidate's side (their own Claude account, Chrome, the Job Search folder, autonomy level,
scheduled tasks and daily routine) is in **[AUTOPILOT.md](AUTOPILOT.md)**.
