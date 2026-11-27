# Resume and cover letter review (every kit, before anything is uploaded)

`build_latex.py` runs the mechanical checks and writes `review.json` plus a PNG of every
page. That is not the review. The review is you **opening every page image and the final
PDF** and checking the list below the way a recruiter for a VP role would. A kit is not
uploaded until every item passes and `review.md` is written.

## 1. Look at every page (required, every time)

Open each `resume_page-N.png` and `letter_page-1.png` with the image viewer (Read), at full
size. If an image looks off, open the PDF itself. Check:
- **Overflow**: no text past the margins, no clipped lines, nothing cut at the page bottom.
- **Page fill and balance**: page 1 full to the bottom; page 2 (if any) at least a third
  full and ending on a complete section; no big empty band anywhere. The letter sits in
  the top two thirds to full page, not crammed and not a short block at the top.
- **Evenness**: bullets roughly even in length; no bullet ending in a line with one or two
  words; no role title or section heading stranded at the bottom of a page; right-aligned
  dates and locations line up down the page.
- **Spacing**: same gap above every section, between roles, and between bullets; no double
  blank lines; no squeezed-looking area from tightening.
- **Typography**: one font, consistent bold/italic use (titles bold, dates italic), no
  stray symbols (`\`, `{`, `--` showing as text, `?` boxes for unsupported characters).

## 2. Read every word (professionalism and errors)

- Spelling, grammar, punctuation, capitalization of company and product names (AWS,
  ServiceNow, Kubernetes), consistent tense (past for past roles).
- One date style everywhere ("Jun 2005 - Feb 2013"), en dashes between dates, no
  "Present" unless `currently_employed: yes`.
- No first person on the resume; no clichés ("results-driven", "passionate", "synergy"),
  no em dashes, nothing that sounds generated.
- Every bullet = action + scale + result. Lead with outcomes, not duties.
- Every number, title, date, employer and tool appears in `master_resume.md`. Nothing
  rounded up, nothing combined into a claim the record doesn't make.
- Nothing implies current employment unless `candidate.yaml` says so (rule 5).
- Contact line correct (phone, email, LinkedIn, city); file names
  `<First>_<Last>_Resume.pdf` / `<First>_<Last>_Cover_Letter.pdf`.

## 3. Fit for this role (keywords, experience, ATS)

- `review.json` lists the posting's top terms and which are missing. For each missing term:
  add it where the record genuinely supports it (in a real bullet, not a keyword dump);
  otherwise leave it out and note it. Target 70%+ coverage of the terms the record supports.
- Headline and summary name the target role's level and domain in the posting's words.
- The 3 achievements most relevant to this posting are first.
- The most recent 10-15 years carry the most space; older roles are 1-2 lines.
- Level fit: scope (team size, budget, footprint) is visible in the first half of page 1.
- ATS: `review.json` has no problems (name, headings and achievements extract as text;
  single column; no tables or images holding key facts).

## 4. Cover letter

- Dated today; addressed to the right company (and person or team when known); no `[Company]` left.
- Every claim in the letter is in the record, including time spans ("for the last decade" needs dates that show it).
- Opens with why this role and company, specifically (one fact from research).
- Two or three proofs mapped to the posting's top needs, each with a number from the record.
- Under 300 words, one page, in the candidate's voice (`writing`, `notes.md` voice samples).
- Same name, contact line and look as the resume.

## 5. Write `review.md` and record it

In the application folder write `review.md`:

```
# Review: <Company>, <Role>   (<date>)
Visual check: viewed resume p1, p2, letter p1 at full size: PASS
Overflow/fill/evenness/spacing: PASS (page 1 100%, page 2 52%, letter 70%)
Errors/professionalism: PASS (fixed: "Kuberentes" typo, mixed date style)
Keywords: 78% of posting terms; added: FinOps (record: cloud cost program); not supported: Terraform
Facts: all checked against master_resume.md
Letter: PASS
Result: READY
```

Then set `"visual_check": "pass"` in `review.json`. Any FAIL means fix `kit.json`, rebuild,
and look again (the new PNGs, not the old ones). After 3 rebuilds that still fail, hold the
role as `needs_review` with the reason instead of uploading a weak kit.
