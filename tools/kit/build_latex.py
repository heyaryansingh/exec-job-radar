"""Build an executive resume and cover letter as LaTeX -> PDF from one kit.json.

    python tools/kit/build_latex.py kit.json <out_dir> [--first-last First_Last]

Writes <out_dir>/<First>_<Last>_Resume.{tex,pdf} and <First>_<Last>_Cover_Letter.{tex,pdf},
then checks them and prints a short report (exit 0 = ready, 1 = needs a fix).

The design follows a Jake's-style template, adapted for senior roles: Palatino, a headline
under the name, an executive summary, a core-competencies grid (the keywords recruiters and
applicant-tracking systems search for), selected achievements, then experience with a scope
line per role. Up to 2 pages (page 2 carries a running name header); the letter is 1 page.

ATS hardening, kept from the original template: glyphtounicode + \\pdfgentounicode=1 so
fi/ff/fl ligatures extract as real letters, no hyphenation (keywords never split across
lines), plain text in a single column, real text for every heading. After compiling, the
script extracts the text the way a parser would and checks it.

Checks: page counts, every achievement and the name extract cleanly, no lone-word lines
(the last line of a bullet with one word wastes a line), no em dashes, no words implying
current employment unless the kit says so ("employed": true). If the resume runs over 2
pages it tightens spacing and font once or twice before failing with "cut content".

kit.json (every fact must come from master_resume.md / candidate.yaml):
{
  "name": "Gulab Singh", "employed": false,
  "contact": ["Katy, TX", "email", "phone", "linkedin.com/in/..."],
  "headline": "Technology Executive | Cloud, Infrastructure & Platform Engineering",
  "summary": "...",
  "competencies": ["Cloud Strategy (AWS, GCP)", "Site Reliability Engineering", ...],
  "highlights": ["...", ...],
  "experience": [{"org": "...", "location": "...", "dates": "...",
                  "roles": [{"title": "...", "dates": "...", "scope": "optional one line",
                             "bullets": ["..."]}]}],
  "board": ["optional advisory / board roles"],
  "education": ["M.Tech., Civil Engineering, IIT Kharagpur"],
  "certifications": ["..."], "skills": [["Cloud", "AWS, GCP, Azure"], ...],
  "letter": {"date": "...", "to": ["Hiring Team", "Company"], "salutation": "Dear ...,",
             "paragraphs": ["..."], "closing": "Sincerely,", "signature": "Gulab Singh"}
}
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

SPECIAL = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
           "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
CURRENT_WORDS = re.compile(r"\b(currently|presently|at present|to date|today I|I am (?:a|the|leading|responsible))\b", re.I)


def esc(text) -> str:
    s = "".join(SPECIAL.get(c, c) for c in str(text or ""))
    s = s.replace("–", "--").replace("—", "--").replace("’", "'").replace("‘", "`")
    s = s.replace("“", "``").replace("”", "''").replace("•", r"\textbullet{}")
    s = re.sub(r"(?<!\d)((?:19|20)\d\d)\s*-\s*((?:19|20)\d\d)(?!\d)", r"\1--\2", s)  # 2019-2022 (not phones)
    s = re.sub(r"(?<=\S) - (?=\S)", " -- ", s)            # "Jun 2005 - Feb 2013" -> en dash
    return s


def link(item: str) -> str:
    t = item.strip()
    if "@" in t and " " not in t:
        return rf"\href{{mailto:{t}}}{{{esc(t)}}}"
    if re.match(r"^(https?://)?(www\.)?(linkedin\.com|github\.com|[\w-]+\.(com|org|net|io|ai))/?", t, re.I):
        url = t if t.startswith("http") else "https://" + t
        return rf"\href{{{url}}}{{{esc(re.sub(r'^https?://(www\.)?', '', t))}}}"
    return esc(t)


PREAMBLE = r"""\documentclass[letterpaper,%(size)spt]{article}
\usepackage[T1]{fontenc}
\usepackage{mathpazo}
\usepackage[margin=%(margin)sin]{geometry}
\usepackage{enumitem,titlesec,tabularx,fancyhdr,lastpage,xcolor,needspace}
\usepackage[hidelinks]{hyperref}
\usepackage[protrusion=true,expansion=false]{microtype}
\input{glyphtounicode}
\pdfgentounicode=1
\definecolor{ink}{HTML}{1F2933}\definecolor{accent}{HTML}{1F4E79}\definecolor{muted}{HTML}{52606D}
\color{ink}
\raggedright
\hyphenpenalty=10000 \exhyphenpenalty=10000
\setlength{\parindent}{0pt}
\linespread{%(spread)s}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
%(header)s
\titleformat{\section}{\color{accent}\bfseries}{}{0em}{\MakeUppercase}[\color{accent}\titlerule]
\titlespacing*{\section}{0pt}{%(secgap)spt}{4pt}
\setlist[itemize]{leftmargin=1.1em,label={\small\textbullet},itemsep=%(itemsep)spt,topsep=2pt,parsep=0pt}
\newcommand{\role}[4]{\textbf{#1}\hfill{\color{muted}#2}\\[-1pt]{\itshape #3}\hfill{\color{muted}\itshape #4}\par}
\pdfinfo{/Title (%(title)s) /Author (%(name)s)}
\begin{document}
"""


def resume_tex(k: dict, size="10.5", margin="0.6", spread="1.02", secgap="9", itemsep="1.6") -> str:
    name = k["name"]
    header = (r"\fancyhead[R]{\ifnum\value{page}>1 {\color{muted}\small " + esc(name) +
              r" \textbar{} Page \thepage{} of \pageref{LastPage}}\fi}")
    out = [PREAMBLE % dict(size=size, margin=margin, spread=spread, secgap=secgap, itemsep=itemsep,
                           header=header, title=esc(name) + " Resume", name=esc(name))]
    out.append(r"\begin{center}{\fontsize{24}{28}\selectfont\bfseries " + esc(name) + r"}\\[4pt]")
    if k.get("headline"):
        out.append(r"{\large\color{accent} " + esc(k["headline"]) + r"}\\[3pt]")
    out.append(r"{\small " + r" \textbar{} ".join(link(c) for c in k.get("contact", []) if c) + r"}\end{center}")
    if k.get("summary"):
        out += [r"\section{Executive Summary}", esc(k["summary"]) + r"\par"]
    comps = [c for c in k.get("competencies") or [] if c]
    if comps:
        out.append(r"\section{Core Competencies}")
        rows = [comps[i:i + 3] for i in range(0, len(comps), 3)]
        out.append(r"{\small\begin{tabularx}{\linewidth}{@{}XXX@{}}")
        out += [" & ".join(esc(c) for c in r + [""] * (3 - len(r))) + r" \\" for r in rows]
        out.append(r"\end{tabularx}}")
    if k.get("highlights"):
        out += [r"\section{Selected Achievements}", r"\begin{itemize}"]
        out += [r"\item " + esc(h) for h in k["highlights"]]
        out.append(r"\end{itemize}")
    if k.get("experience"):
        out.append(r"\section{Professional Experience}")
        for job in k["experience"]:
            roles = job.get("roles") or []
            out.append(r"\needspace{5\baselineskip}\textbf{\large " + esc(job.get("org")) + r"}\hfill{\color{muted}" +
                       esc(job.get("location")) + r"}\par" +
                       (r"{\color{muted}\small " + esc(job["dates"]) + r"}\par" if job.get("dates") else r"\par"))
            for r in roles:
                out.append(r"\needspace{3\baselineskip}\vspace{3pt}\textbf{" + esc(r.get("title")) + r"}\hfill{\color{muted}\itshape " +
                           esc(r.get("dates")) + r"}\par")
                if r.get("scope"):
                    out.append(r"{\small\itshape " + esc(r["scope"]) + r"}\par")
                if r.get("bullets"):
                    out += [r"\begin{itemize}"] + [r"\item " + esc(b) for b in r["bullets"]] + [r"\end{itemize}"]
            out.append(r"\vspace{4pt}")
    for key, head in (("board", "Board and Advisory"), ("education", "Education"),
                      ("certifications", "Certifications")):
        items = [x for x in k.get(key) or [] if x]
        if items:
            out += [r"\section{" + head + "}", r"\begin{itemize}"] + [r"\item " + esc(x) for x in items] + [r"\end{itemize}"]
    skills = [s for s in k.get("skills") or [] if s]
    if skills:
        out += [r"\section{Technical Skills}", r"{\small\begin{tabularx}{\linewidth}{@{}l X@{}}"]
        out += [r"\textbf{" + esc(a) + r"} & " + esc(b) + r" \\" for a, b in skills]
        out.append(r"\end{tabularx}}")
    out.append(r"\end{document}")
    return "\n".join(out)


def letter_tex(k: dict, size="11", margin="0.9", spread="1.08") -> str:
    L = k["letter"]
    name = k["name"]
    out = [PREAMBLE % dict(size=size, margin=margin, spread=spread, secgap="8", itemsep="1.5",
                           header=r"\fancyfoot{}", title=esc(name) + " Cover Letter", name=esc(name))]
    out.append(r"\thispagestyle{empty}{\LARGE\bfseries " + esc(name) + r"}\\[2pt]")
    out.append(r"{\small\color{muted} " + r" \textbar{} ".join(link(c) for c in k.get("contact", []) if c) + r"}")
    out.append(r"\par{\color{accent}\rule{\linewidth}{0.6pt}}\par\vspace{10pt}")
    if L.get("date"):
        out.append(esc(L["date"]) + r"\par\vspace{8pt}")
    if L.get("to"):
        out.append(r"\par ".join(esc(t) for t in L["to"]) + r"\par\vspace{8pt}")
    out.append(esc(L.get("salutation", "Dear Hiring Team,")) + r"\par\vspace{6pt}")
    out += [esc(p) + r"\par\vspace{7pt}" for p in L.get("paragraphs", [])]
    out.append(esc(L.get("closing", "Sincerely,")) + r"\par\vspace{18pt}" + esc(L.get("signature", name)) + r"\par")
    out.append(r"\end{document}")
    return "\n".join(out)


def compile_tex(tex: str, path: Path) -> tuple[int, str]:
    path.write_text(tex)
    for _ in range(2):   # twice, for the page-of-N reference
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", path.name],
                           cwd=path.parent, capture_output=True, text=True, timeout=120)
    pdf = path.with_suffix(".pdf")
    if r.returncode or not pdf.exists():
        err = "\n".join(l for l in r.stdout.splitlines() if l.startswith("!") or "Error" in l)[:600]
        raise RuntimeError(f"LaTeX failed for {path.name}: {err or r.stdout[-600:]}")
    for ext in (".aux", ".log", ".out"):
        path.with_suffix(ext).unlink(missing_ok=True)
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    return pages, text


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def check(k: dict, pages: int, text: str, max_pages: int, what: str) -> list[str]:
    probs = []
    if pages > max_pages:
        probs.append(f"{what}: {pages} pages (max {max_pages}); cut content")
    flat = norm(text)
    if norm(k["name"]) not in norm(text[:400]):
        probs.append(f"{what}: name does not extract as text at the top of page 1")
    if what == "resume":
        for head in ("summary", "experience", "education"):
            if not re.search(rf"^\s*[A-Z ]*{head.upper()}", text, re.M):
                probs.append(f"resume: section heading '{head}' does not extract as a clean word")
    if what == "resume":
        for h in k.get("highlights") or []:
            words = norm(h).split()[:6]
            if words and " ".join(words) not in flat:
                probs.append(f"resume: achievement does not extract cleanly: {h[:60]}")
        lone = [l.strip() for l in text.splitlines()
                if re.fullmatch(r"\s{2,}[A-Za-z0-9().,%/-]+\.?\s*", l) and len(l.strip()) > 1]
        if lone:
            probs.append(f"resume: lone-word lines (tighten those bullets): {', '.join(lone[:5])}")
    left = re.findall(r"\[(?:VERIFY|ADD)[^\]]*\]|\bTODO\b", text)
    if left:
        probs.append(f"{what}: unfilled placeholders: {', '.join(sorted(set(left))[:4])}")
    if "—" in text:
        probs.append(f"{what}: contains an em dash")
    if not k.get("employed") and CURRENT_WORDS.search(text):
        probs.append(f"{what}: wording implies current employment: '{CURRENT_WORDS.search(text).group(0)}'")
    return probs


def build(k: dict, out: Path, stem: str) -> list[str]:
    out.mkdir(parents=True, exist_ok=True)
    problems: list[str] = []
    attempts = [dict(), dict(size="10", margin="0.55", spread="1.0", secgap="7", itemsep="1.2"),
                dict(size="10", margin="0.5", spread="0.97", secgap="6", itemsep="0.8")]
    for i, opts in enumerate(attempts):
        pages, text = compile_tex(resume_tex(k, **opts), out / f"{stem}_Resume.tex")
        if pages <= 2 or i == len(attempts) - 1:
            break
    problems += check(k, pages, text, 2, "resume")
    print(f"resume: {pages} page(s)")
    if k.get("letter"):
        for i, opts in enumerate([dict(), dict(size="10.5", margin="0.8", spread="1.03")]):
            pages, text = compile_tex(letter_tex(k, **opts), out / f"{stem}_Cover_Letter.tex")
            if pages <= 1:
                break
        words = sum(len(p.split()) for p in k["letter"].get("paragraphs", []))
        if words > 400:
            problems.append(f"letter: {words} words (keep under 350)")
        problems += check(k, pages, text, 1, "letter")
        print(f"letter: {pages} page(s), {words} words")
    return problems


def main(argv=None) -> int:
    a = list(argv if argv is not None else sys.argv[1:])
    if len(a) < 2:
        print(__doc__); return 2
    k = json.loads(Path(a[0]).read_text())
    stem = a[a.index("--first-last") + 1] if "--first-last" in a else "_".join(k["name"].split()[:1] + k["name"].split()[-1:])
    if not shutil.which("pdflatex"):
        print("pdflatex not found: install TeX Live (or MacTeX / MiKTeX), or fall back to "
              "node tools/kit/build_docs.js kit.json <folder>")
        return 1
    problems = build(k, Path(a[1]), stem)
    for p in problems:
        print("FIX:", p)
    print("READY" if not problems else "NEEDS A FIX")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
