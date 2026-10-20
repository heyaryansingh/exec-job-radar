# Job Search Autopilot: setup for the candidate's own Claude

This sets up a candidate's own Claude to run their job search every day on their own
computer: it picks the best new senior roles from this repo's hourly feed, writes a tailored
resume and cover letter for each, fills the applications in their Chrome, submits the ones
the candidate has allowed, and keeps a record with proof of everything. The candidate spends
about 10 minutes a day on it.

It is modeled on a system that ran 120+ real internship applications in October 2026, with
the lessons from that system built in. The day-to-day rules are in [PLAYBOOK.md](PLAYBOOK.md);
this page is the one-time setup and how to live with it.

## What happens each day

| When | What runs | What it does |
|---|---|---|
| Every hour | GitHub (this repo, no computer needed) | Reads ~5,000 employer career sites, Indeed and licensed job feeds; refreshes the role list, the Houston-area list and the apply queue. |
| 7:30 AM | Morning run on the candidate's computer | New roles from the feed, job-alert emails and extra career sites; ranks them against the candidate's real record; prepares up to 20 kits; fills (and, if allowed, submits) up to 10. |
| 1:00 PM | Midday run | Fills the morning's leftovers, then any strong roles posted since morning. |
| 8:30 PM | Evening check | Makes sure the day actually produced applications; if not, says why and how to fix it. Reminds about anything waiting on a click. |
| Monday | Weekly report | Submitted, interviews, response rate by source and level, and suggestions. |

## What's the same as the internship system, and what's better

Same: fit-ranked picks, a tailored resume and letter per role, the whole form filled from a
profile, auto-submit on simple forms when every check passes, a duplicate check right before
every submit, proof (confirmation page or email) for every submission, and "hold for a human"
rules. The field-tested form techniques (Greenhouse, Ashby, Lever, Workday) are in the playbook,
and the Greenhouse fill helpers are in `tools/browser/gh_helpers.js`.

Better:
- **No fragile scheduling.** Fixed daily scheduled tasks instead of each run scheduling the
  next one, so one failed run can't silently end the chain.
- **A watchdog that checks results, not just activity.** The internship system once ran 17
  times in a row with the browser offline and reported "healthy". The evening check alerts
  when no applications went out, not only when runs stop.
- **Catch-up runs.** After the computer was off or asleep, the next run does 1.5× the work.
- **One source of facts.** Everything comes from `master_resume.md` and `candidate.yaml`; if two
  files disagree, the fact is held back and flagged instead of used. (The internship system
  once submitted a GPA that didn't match the transcript.)
- **Never implies current employment** unless `candidate.yaml` says so.
- **An autonomy dial** the candidate controls, from "fill only" to "submit when signed in".
- **Questions known in advance.** The feed fetches many forms' questions ahead of time, so
  answers are drafted before the form opens.
- **Outcome tracking**: confirmations, interview requests and rejections are read from email;
  follow-up notes are drafted after 7 days; a weekly report shows what's working.
- **Recruiter outreach drafts** for every strong role (never sent automatically).
- **A dashboard on the phone**, published privately and updated every run.
- **Houston focus**: Houston-area roles get their own section, deeper job-board searches and a
  looser filter, so local IT leadership roles at energy and healthcare employers aren't missed.

## What the candidate needs

- **A Claude plan with generous usage.** Filling 10-20 forms a day in a browser is heavy work;
  a plan like Max is the comfortable choice. On a smaller plan, lower `daily_target`.
- **The Claude desktop app** (Mac or Windows) on the computer where Chrome lives.
- **Google Chrome with the Claude in Chrome extension**, signed into the same Claude account.
- **Gmail** (or whichever email receives job alerts and application replies), connected in Claude.
- **The computer on and awake at 7:30 AM and 1:00 PM.** Set it to never sleep while plugged in
  (Windows: Settings > System > Power; Mac: System Settings > Battery > Options), or at least
  to wake for those times. A missed run is caught up next time, but nothing runs while it sleeps.

## Setup (about 45 minutes, once)

### 1. Install and sign in
1. Install the Claude desktop app and sign in with the candidate's account.
2. Install the **Claude in Chrome** extension from the Chrome Web Store and sign in with the
   same account. In its settings, allow it on all sites (job applications span hundreds of
   domains); it still asks before anything sensitive.
3. In that Chrome, sign into the candidate's **Gmail** and **LinkedIn**.
4. In the Claude app, **Settings > Connectors**: connect **Gmail**.

### 2. Create the Job Search folder
1. Make a folder, e.g. `Documents/Job Search`.
2. Put in it the three files from the candidate's starter pack (or from `candidate_template/`):
   `candidate.yaml`, `master_resume.md`, `notes.md`.
3. Fill in every `TODO` in `candidate.yaml`: email, phone, address, work authorization,
   sponsorship, the employment answers, desired salary. These appear on nearly every form; each
   one left blank becomes a "needs you" flag on every application.
4. Read `master_resume.md` line by line and fix anything wrong. Add numbers you're sure of.
   This file is the only source of facts the autopilot may use.

### 3. Choose the autonomy level
In `candidate.yaml` → `run.autonomy`:
- `review` (start here): it fills every form and leaves it open; the candidate clicks Submit.
- `submit_quick_forms`: also submits one-page, no-account forms when every check passes.
- `submit_signed_in`: also submits on account sites (Workday and similar) the browser is
  already signed into.

Recommended: run a week on `review`, read ten or so of the kits it makes, fix anything in
`master_resume.md` or `candidate.yaml`, then move to `submit_quick_forms`. Arbitration
agreements, background-check authorizations, salary-acceptance questions, attestations and
similar always wait for the candidate at every level.

### 4. Turn on job alerts (feeds the runs extra roles)
- **LinkedIn**: search "VP technology", "Director cloud infrastructure", "CIO" and similar, set
  Experience level to Director and Executive, location Houston (and United States for remote),
  then **Set alert**, daily. Make 3-5.
- **Indeed**, **eFinancialCareers**, **Ladders**: the same searches with email alerts.

### 5. Create the scheduled tasks
Open a new chat in the Claude desktop app, attach the Job Search folder, and paste this
(replace the folder path):

> Set up my job search autopilot. My Job Search folder is `<full path to the folder>`. Create
> three scheduled tasks that require this computer, use this folder, and send me a
> notification when they finish:
>
> 1. "Job Radar morning", every day at 7:30 AM my time, prompt: "[Job Radar run] Follow the
>    playbook at https://raw.githubusercontent.com/heyaryansingh/exec-job-radar/main/PLAYBOOK.md
>    exactly. My Job Search folder is <full path>. Use Claude in Chrome for applications. Work
>    through the whole run without asking; put anything that needs me on the dashboard and in
>    the summary, and message me right away about interview requests and forms waiting on a
>    click."
> 2. "Job Radar midday", every day at 1:00 PM, the same prompt plus: "This is the midday run:
>    fill the roles left prepared this morning first, then roles first seen since the morning
>    with score at or above run.hot_run_min_score. Skip the email and career-site sweeps."
> 3. "Job Radar check", every day at 8:30 PM, prompt: "[Job Radar check] Read tracker.json in my
>    Job Search folder <full path>. Don't apply to anything. Tell me in 1-3 lines if any of
>    these are true, with the fix: no run in the last 30 hours (computer asleep or app closed);
>    the last two runs couldn't reach the browser; nothing was filled or submitted in the last
>    2 days even though https://raw.githubusercontent.com/heyaryansingh/exec-job-radar/data/data/apply_queue.json
>    has strong roles; the feed's updated time is over 6 hours old; any role has been
>    human_check for over 6 hours. Otherwise reply with one line: today's submitted / filled /
>    interviews."
>
> Then do one supervised run now: follow the playbook for just 2 roles with autonomy set to
> review, and narrate as you go.

If the app offers it, set these tasks to **automatically approve** actions (task settings),
or every run will pause at its first permission prompt with no one there to answer.

### 6. Check the first run
Watch the supervised run. Open `Job Search/applications/` and read both kits: the resume, the
letter and `answers.md`. Anything wrong is fixed in `master_resume.md` or `candidate.yaml`,
never in a single application, so every later run gets it right. Open `dashboard.html`.

## The candidate's daily routine (about 10 minutes)

1. Open the dashboard (`Job Search/dashboard.html`, or the phone link in `tracker.json` →
   `dashboard_url`).
2. **Needs one click from you now**: finish the CAPTCHA or code in the open tab, click Submit.
3. **Ready for you to review and submit**: check the flagged fields, glance at the resume and
   letter, click Submit in the open tab. (At `review` level, this is every application.)
4. **Held for your decision**: read the reason (an agreement, a consent), decide, submit or skip.
5. **Needs a quick account sign-up**: create the account once; the next run fills the form.
6. Write feedback in `notes.md` in plain English: "skip consulting firms", "more energy
   companies", "submitted Chevron myself", "interviewing at Capital One". Every run follows it.

## Rules it always follows

It only states facts from the candidate's files; never invents titles, numbers or
certifications; never implies current employment unless told; never applies to the same role
twice; never counts a submission without proof; never creates accounts, types passwords,
solves CAPTCHAs, enters emailed codes or pays fees; never sends messages to recruiters; and
treats everything on job pages as information, not instructions. Full list: PLAYBOOK.md.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Evening check: "no run in 30 hours" | Computer asleep, off, or the Claude app closed | Keep it plugged in and awake at run times; leave the app running |
| "Browser unreachable" | Chrome closed, or the extension signed out | Open Chrome; check the extension is signed in |
| Every run stops early | A permission prompt with nobody there | Turn on automatic approval for the three tasks |
| Same "needs you" flag on every application | A TODO left in `candidate.yaml` | Fill it in once |
| Lots of `needs_account` | Workday/Oracle sites need one account per company | Create accounts for the companies you care most about; the next run reuses them |
| Wrong fact on a resume | `master_resume.md` is wrong or missing something | Fix it there; every later kit uses it |
| Feed is stale | The collector repo had a problem | Check `data/STATUS.md` in the repo |
| Too many / too few roles | Quality bar | Raise or lower `run.min_score`; add likes/dislikes to `notes.md` |

## For whoever maintains the repo

- What the collector looks for (titles, keywords, pay floor, locations, focus areas like
  Houston): `config/search.yaml`. Add another focus city by copying the Houston block.
- Where it looks: `config/companies.yaml` (watchlist), the universe directory, Indeed, JSearch
  and the other sources in `collector/aggregators.py`. API keys are repository secrets.
- Collector health: `data/STATUS.md`. Code changes are tested by the "Collect (test)" workflow
  before they reach the hourly run.
