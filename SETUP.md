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
   reads `data/latest.json`; the full role database is `data/roles.json`.

### Keeping it healthy
- `data/STATUS.md` shows, at a glance: last run, how many company sites are working, and a
  table of failing ones with their errors.
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

The daily run fills applications in the candidate's own browser, so it runs on their
computer under their own Claude account. Filling 5-10 forms a day is browser-heavy, so a
plan with generous usage is recommended.

1. **Install** the Claude desktop app and sign in. Install the **Claude in Chrome**
   extension and sign in with the same account.
2. **In that Chrome**, sign into the candidate's Gmail and LinkedIn. Keep Chrome open
   when the daily run is scheduled, and keep the computer awake (not sleeping).
3. **Create a folder** called `Job Search` (Documents is fine) and put these files in it:
   `candidate.yaml`, `master_resume.md`, `notes.md` (start from `candidate_template/`).
   - Fill in every TODO in `candidate.yaml` (contact details, work authorization, the
     employment answers) and set `run.repo` to `<you>/exec-job-radar`.
   - Go through `master_resume.md` line by line. It is the only source of facts Claude may
     use, so correct anything wrong and add numbers where you have them.
4. **Connect Gmail** in Claude (Settings → Connectors). The run reads job-alert emails and
   application replies from it.
5. **Turn on job alerts** (they email new matches daily):
   - LinkedIn Jobs: search e.g. "VP cloud infrastructure", filter Experience level =
     Director + Executive, then **Set alert** (daily). Make 3-5 of these with different
     keywords.
   - Indeed: same searches, **Get new jobs emailed**.
   - eFinancialCareers (finance tech) and Ladders (six-figure roles): create a profile and
     saved-search alerts.
6. **Create the daily scheduled task.** In a new Claude chat on that computer, connect the
   `Job Search` folder, then paste this message (fill in the two placeholders):

   > Create a scheduled task named "Job Radar" that runs every day at 7:30 AM my time,
   > requires this computer, and uses my Job Search folder. Its prompt:
   > "[Job Radar daily run] Follow the playbook at
   > https://raw.githubusercontent.com/<you>/exec-job-radar/main/PLAYBOOK.md exactly. The
   > candidate's Job Search folder is <full path to the folder> on this computer. Use Claude
   > in Chrome for applications (the built-in browser if Chrome is unavailable). Never
   > submit an application. End with the 3-6 line summary."

   Turn on notifications for the task so the summary reaches the candidate's phone. If the
   computer is asleep at 7 AM the run is missed, so set it to stay awake (or wake) then.

   Recommended second task, at 1:00 PM, to keep volume high:
   > Same as above, named "Job Radar midday", with this added to the prompt: "This is the
   > midday run: first fill the roles left `prepared` this morning, then consider collector
   > roles first seen since the morning run with score at or above run.hot_run_min_score.
   > Skip the email and career-site sweeps."

   With both runs, expect about 15-20 tailored, filled applications a day on a normal day
   (more when many good roles post). That is browser-heavy, so a plan with generous usage
   is needed; lower `daily_target` if runs hit usage limits.

7. **Do one supervised run.** In the chat, say: *"Run the Job Radar playbook now, but only
   for 2 roles, and narrate as you go."* Watch it fill the forms, check the materials in
   `Job Search/applications/`, and correct `candidate.yaml` or `master_resume.md` wherever
   something came out wrong.

### Daily routine for the candidate
1. Open `Job Search/dashboard.html`.
2. For each role under **Ready for you to review and submit**: read the flagged fields,
   check the resume and cover letter, switch to the open browser tab, and click Submit.
3. Do the account sign-ups listed under **Needs a quick account sign-up**.
4. Write any feedback in `notes.md` ("skip consulting", "submitted Chevron"). The next run
   follows it.
