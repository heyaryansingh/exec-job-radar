# Job Search Autopilot: setup for the candidate's own Claude

This sets up a candidate's own Claude to run their job search every day on their own
computer: it picks the best new senior roles from this repo's hourly feed, writes a tailored
resume and cover letter for each, fills the applications in their Chrome, submits the ones
the candidate has allowed, and keeps a record with proof of everything. The candidate spends
about 10 minutes a day on it.

It is modeled on a system that ran 120+ real internship applications in October 2026, with
the lessons from that system built in. The day-to-day rules are in [PLAYBOOK.md](PLAYBOOK.md);
this page is the one-time setup and how to live with it.

## Start here (the candidate's part, about 10 minutes)

1. Install the **Claude desktop app** and sign in. In Chrome, add the **Claude in Chrome**
   extension and sign in with the same account. In the app, connect **Gmail** (Settings >
   Connectors).
2. Put the Job Search folder you were given (or an empty one) in `Documents`, and drop in
   what you have, in any format: your resumes (current plus a couple of older ones), cover
   letters you've written, your LinkedIn profile as a PDF, and any bios or reviews.
3. Open a new chat in the Claude app, attach that folder, and paste this one line:

> Set up my Job Radar autopilot by following https://raw.githubusercontent.com/heyaryansingh/exec-job-radar/main/ONBOARD.md exactly. My Job Search folder is attached.

4. Claude writes the career record, a two-page executive resume and a cover letter in your
   voice (LaTeX, checked for applicant-tracking systems), then sends one message with the
   drafts and a few questions. Answer them, then click **Allow** when it asks. When it's done, open each
   of the three scheduled tasks it made and turn on **automatically approve**.

That's it. Claude checks and fixes everything else, and tells you if anything is missing.
The rest of this page is the detail behind those steps.

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
- **Claude-guided setup** ([ONBOARD.md](ONBOARD.md)): one pasted prompt; Claude builds the
  career record from the resume, asks only for missing facts, and creates the schedule.
- **Self-check and self-repair** every run (`tools/check_setup.py`): installs missing tools,
  catches TODOs and a stale feed before they waste a run, and falls back to Word files when
  LibreOffice is missing instead of failing.
- **Earned autonomy**: an opt-in ramp from "fill only" to submitting simple forms after a clean
  first week, and back down automatically if anything goes wrong.
- **Accounts to unlock**: the dashboard ranks which employer accounts would open up the most
  strong roles, so the candidate's few minutes of sign-ups go where they count.

## What the candidate needs

- **A Claude plan with generous usage.** Filling 10-20 forms a day in a browser is heavy work;
  a plan like Max is the comfortable choice. On a smaller plan, lower `daily_target`.
- **The Claude desktop app** (Mac or Windows) on the computer where Chrome lives.
- **Google Chrome with the Claude in Chrome extension**, signed into the same Claude account.
- **Gmail** (or whichever email receives job alerts and application replies), connected in Claude.
- **Node.js and LibreOffice** for building the resumes. Claude installs these or works around
  them during setup; the candidate is asked only if that fails (without LibreOffice, kits
  upload as Word files).
- **The computer on and awake at 7:30 AM and 1:00 PM.** Set it to never sleep while plugged in
  (Windows: Settings > System > Power; Mac: System Settings > Battery > Options), or at least
  to wake for those times. A missed run is caught up next time, but nothing runs while it sleeps.

## Setup (about 20 minutes of the candidate's time, once)

### Fast way: Claude sets it up (recommended)
1. Get the items under "What the candidate needs" in place: the Claude app, the Claude in
   Chrome extension signed into the same account, and the Gmail connector (Settings >
   Connectors). Claude checks the rest and walks the candidate through anything missing.
2. Make an empty folder, e.g. `Documents/Job Search`.
3. Open a new chat in the Claude desktop app, attach that folder and the candidate's resume
   (plus their LinkedIn profile saved as a PDF, if handy), and paste:

> Set up my Job Radar autopilot. Follow https://raw.githubusercontent.com/heyaryansingh/exec-job-radar/main/ONBOARD.md
> exactly. My Job Search folder is the one attached. Ask me everything you need in as few
> questions as possible, and do the rest yourself.

Claude then builds `master_resume.md` from the documents, fills `candidate.yaml` (asking only
for facts it can't find), checks the setup with `tools/check_setup.py`, creates the three
scheduled tasks, lists the accounts worth creating, publishes the phone dashboard, and does
a supervised 2-role run. Afterwards, turn on **automatically approve** in each scheduled
task's settings if the app offers it.

### Manual way
1. Put `candidate.yaml`, `master_resume.md` and `notes.md` from `candidate_template/` in the
   Job Search folder. Fill every `TODO` in `candidate.yaml` (each blank becomes a "needs you"
   flag on every application) and put the full, true career record in `master_resume.md`:
   it is the only source of facts the autopilot may use.
2. Leave `run.repo` as the shared feed unless you run your own ([SETUP.md](SETUP.md), Path B).
3. Choose autonomy (`run.autonomy`, below).
4. Run `python tools/check_setup.py "<folder>" --fix` from a copy of this repo until it says READY.
5. Create the three scheduled tasks exactly as in [ONBOARD.md](ONBOARD.md), Step 6, then do
   a supervised run: "Follow the playbook for just 2 roles with autonomy set to review, and
   narrate as you go."

### Autonomy
In `candidate.yaml` → `run`:
- `autonomy: review`: fills every form and leaves it open; the candidate clicks Submit.
- `autonomy: submit_quick_forms`: also submits one-page, no-account forms when every check passes.
- `autonomy: submit_signed_in`: also submits on account sites (Workday and similar) the
  browser is already signed into.
- `autonomy_ramp: true` (the default in new setups): start at `review`; after a clean first
  week (at least 8 of its filled forms submitted by the candidate, no fact corrections), it
  moves itself up to `submit_quick_forms` and says so. It drops back to `review` on its own if
  the candidate reports a wrong fact or an unwanted submission. It never goes to
  `submit_signed_in` by itself.
- `allow_google_signin: true` (default in new setups): may click "Continue with Google" with
  the account Chrome is signed into. It never types a password.

Arbitration agreements, background-check authorizations, salary-acceptance questions,
attestations and similar always wait for the candidate at every level.

### Job alerts (optional, extra roles)
- **LinkedIn**: search "VP technology", "Director cloud infrastructure", "CIO" and similar, set
  Experience level to Director and Executive, the candidate's locations (and United States
  for remote), then **Set alert**, daily. Make 3-5.
- **Indeed**, **eFinancialCareers**, **Ladders**: the same searches with email alerts.

### Check the first run
Open `Job Search/applications/` and read both kits: the resume, the letter and `answers.md`.
Anything wrong is fixed in `master_resume.md` or `candidate.yaml`, never in a single
application, so every later run gets it right. Open `dashboard.html`.

## The candidate's daily routine (about 10 minutes)

1. Open the dashboard (`Job Search/dashboard.html`, or the phone link in `tracker.json` →
   `dashboard_url`).
2. **Needs one click from you now**: finish the CAPTCHA or code in the open tab, click Submit.
3. **Ready for you to review and submit**: check the flagged fields, glance at the resume and
   letter, click Submit in the open tab. (At `review` level, this is every application.)
4. **Held for your decision**: read the reason (an agreement, a consent), decide, submit or skip.
5. **Needs a quick account sign-up**: create the account once; the next run fills the form.
   "Accounts that would unlock the most roles" shows which ones are worth it.
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
| Not sure what's wrong | Anything | Ask Claude: "run tools/check_setup.py on my Job Search folder and fix what it finds" |
| Wrong field of roles in the feed | The shared feed targets tech leadership | Run your own feed ([SETUP.md](SETUP.md), Path B) and retarget `config/search.yaml` |

## For whoever maintains the repo

- What the collector looks for (titles, keywords, pay floor, locations, focus areas like
  Houston): `config/search.yaml`. Add another focus city by copying the Houston block.
- Where it looks: `config/companies.yaml` (watchlist), the universe directory, Indeed, JSearch
  and the other sources in `collector/aggregators.py`. API keys are repository secrets.
- Collector health: `data/STATUS.md`. Code changes are tested by the "Collect (test)" workflow
  before they reach the hourly run.
