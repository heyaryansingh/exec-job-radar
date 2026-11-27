# Setup

There are two halves, and most people only need the second:

1. **The hourly role feed** (GitHub). A shared one already runs here, hourly, for US
   Director-and-up technology leadership roles (cloud, infrastructure, platform, SRE,
   architecture, data/AI, security, transformation; $200K+; Houston focus section).
   - **Path A, use the shared feed (0 minutes).** If the candidate is in that field, skip
     GitHub entirely. Every daily run ranks the feed against the candidate's own record and
     locations, so it works anywhere in the US.
   - **Path B, run your own feed (about 20 minutes).** Only for a different field or
     seniority, a non-US search, or if you want your own copy. See below.
2. **The candidate's computer** (their own Claude account). Start here:
   **[AUTOPILOT.md](AUTOPILOT.md)**. The fast way is one pasted prompt; Claude does the rest
   ([ONBOARD.md](ONBOARD.md)).

---

## Path B: run your own feed on GitHub

### 1. Copy the repository (fork)
1. Sign in at github.com and open `https://github.com/heyaryansingh/exec-job-radar`.
2. Click **Fork**. Keep the name `exec-job-radar`, keep it **Public** (public repos get
   unlimited free Actions minutes; the repo holds only code, search rules and public job
   postings, nothing personal).
   - Same field as the shared feed, just your own copy? **Untick "Copy the main branch
     only"**, so the `data` branch (the role database) comes along and you start with
     thousands of roles already tracked.
   - Different field? Leave it ticked; your feed starts fresh.

### 2. Turn on the workflows (forks start with them off)
1. **Settings → Actions → General**: under "Actions permissions" allow all actions; under
   **Workflow permissions** choose **Read and write permissions**. Save.
2. **Actions** tab → click **"I understand my workflows, go ahead and enable them"**.
3. GitHub also switches off *scheduled* workflows in forks. You don't need them: in
   **Actions → Heartbeat → Run workflow**, start the heartbeat once. It runs "Collect roles"
   every hour and restarts itself, so nothing else needs scheduling. (Optionally enable
   "Collect roles" and "Discover companies" from their pages too, as a backup.)

### 3. Retarget the search (different field only)
Everything about *who* the feed is for lives in `config/search.yaml`: title levels, domain
keywords, pay floor, locations, the focus-city section and the job-board searches. No code
changes. The easy way is to let Claude write it:

> Here is config/search.yaml from my fork of exec-job-radar [paste it, or give the link
> https://github.com/<you>/exec-job-radar/blob/main/config/search.yaml]. Rewrite it for this
> search: <field, e.g. "senior finance leadership: Controller, VP Finance, CFO">, <levels>,
> minimum base <$>, locations <cities / remote / US-wide>, focus city <city> (rename the
> Houston block and its regex and board searches). Keep the structure and every key, change
> only the values, and give me the whole file back.

Paste the result into GitHub (open the file, pencil icon, replace, **Commit changes**). The
collector re-runs on that commit. For a different focus city, also delete
`data/houston.md` and rename the "Houston" mention in `config/readme_header.md`.

### 4. First runs
1. **Actions → Validate companies → Run workflow.** The log's last lines list watchlist
   companies whose career sites didn't respond; fix them (see "Adding companies") or add
   `disabled: true`.
2. **Actions → Discover companies → Run workflow.** Resolves the 1,300+ names in
   `config/discover_seed.txt` to their career sites and adds the working ones to
   `config/companies.yaml` (1-2 hours the first time; unsure names go to
   `data/discover_review.md`, unfound ones retry weekly). For a different field, replace the
   seed names with employers that hire for it first.
3. **Actions → Collect roles → Run workflow** once. From then on it runs hourly: the README
   becomes the live role list, with daily digests in `data/daily/`. The daily Claude runs read
   `data/apply_queue.json` and `data/latest.json` from the `data` branch.
4. In the candidate's `candidate.yaml`, set `run.repo: <you>/exec-job-radar`. Check it with
   `python tools/check_setup.py "<Job Search folder>"`: it confirms the feed is reachable and fresh.

### 5. Optional job sources (repository secrets)
**Settings → Secrets and variables → Actions → New repository secret.** Each is free and
skipped when missing:
- `ADZUNA_APP_ID`, `ADZUNA_APP_KEY`: developer.adzuna.com (large aggregator, official API).
- `USAJOBS_API_KEY`, `USAJOBS_EMAIL`: developer.usajobs.gov (federal roles).
- `RAPIDAPI_KEY`: JSearch on RapidAPI (Google for Jobs results).

### Getting improvements from the original
The daily runs read `PLAYBOOK.md` from the original repo, so playbook improvements reach
you automatically. For collector fixes, click **Sync fork** on your repo's front page. If it
reports conflicts (both copies rewrite `README.md` and `data/*.md` every hour), ask Claude:
"merge upstream heyaryansingh/exec-job-radar into my fork; keep my `config/` files, take
upstream for code, and take mine for `README.md` and `data/`."

---

## Keeping a feed healthy
- `data/STATUS.md`: last run, how many company sites work, and the failing ones with errors.
- The "universe" (every other known career site, several thousand) is read in rotation within
  each run's 40-minute budget, so each is visited every few hours while the watchlist is read
  hourly. Turn it off with `universe: enabled: false` in `config/search.yaml`.
- Broken sites back off automatically (retried every 12 hours after 6 straight failures).
- If more than half the sites fail in one run, the run is marked failed and GitHub emails the
  repo owner. Results are still saved.
- Code changes are tested by **Collect (test)** (report in `data/test_reports/collect.md`) and
  **Discover (test)** before the hourly run uses them.

## Adding companies
Open any job posting at the company, copy the URL, then:
```
python tools/add_company.py "<url>" "Company Name" 1 bank
```
It recognizes Workday, Greenhouse, Lever, Ashby, SmartRecruiters and Oracle career sites.
Companies with fully custom sites (Goldman Sachs, Amazon, Google, ...) go in the candidate's
`run.extra_career_sites` instead; the job-board sweep also catches many of their roles.
