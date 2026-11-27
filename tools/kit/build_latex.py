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


def compile_tex(tex: str, path: Path) -> dict:
    """Compile twice; return pages, layout text, overflow warnings and how full each page is."""
    path.write_text(tex)
    for _ in range(2):   # twice, for the page-of-N reference
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", path.name],
                           cwd=path.parent, capture_output=True, text=True, timeout=120)
    pdf = path.with_suffix(".pdf")
    if r.returncode or not pdf.exists():
        err = "\n".join(l for l in r.stdout.splitlines() if l.startswith("!") or "Error" in l)[:600]
        raise RuntimeError(f"LaTeX failed for {path.name}: {err or r.stdout[-600:]}")
    log = path.with_suffix(".log").read_text(errors="ignore")
    overfull = [float(m) for m in re.findall(r"Overfull \\hbox \((\d+\.?\d*)pt too wide\)", log)]
    for ext in (".aux", ".log", ".out"):
        path.with_suffix(ext).unlink(missing_ok=True)
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    return {"pages": pages, "text": text, "overfull": [o for o in overfull if o > 1.0],
            "fill": page_fill(pdf), "pdf": pdf}


def page_fill(pdf: Path) -> list[float]:
    """Fraction of each page's height used by text (0-1), from word bounding boxes.
    The running header on page 2+ is ignored."""
    html = subprocess.run(["pdftotext", "-bbox", str(pdf), "-"], capture_output=True, text=True).stdout
    fills = []
    for page in re.findall(r'<page width="[\d.]+" height="([\d.]+)">(.*?)</page>', html, re.S):
        h = float(page[0])
        ys = [(float(a), float(b)) for a, b in re.findall(r'yMin="([\d.]+)" xMax="[\d.]+" yMax="([\d.]+)"', page[1])]
        body = [y for y in ys if y[0] > 0.07 * h] or ys          # drop the running header
        if not body:
            fills.append(0.0); continue
        top, bottom = min(y[0] for y in body), max(y[1] for y in body)
        fills.append(round(max(0.0, bottom - min(top, 0.08 * h)) / (0.86 * h), 2))
    return fills


def render_pages(pdf: Path, prefix: str) -> list[Path]:
    """PNG of every page, for the required visual check (Claude must open each one)."""
    stem = pdf.parent / f"{prefix}_page"
    for old in pdf.parent.glob(f"{prefix}_page-*.png"):
        old.unlink()
    subprocess.run(["pdftoppm", "-png", "-r", "110", str(pdf), str(stem)], capture_output=True)
    return sorted(pdf.parent.glob(f"{prefix}_page-*.png"))


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


STOP = set("""a an the and or of to in for with on at by from as is are be been this that these those
our we you your will can may must should would their they it its into across within over per more most
other than such using use including include includes experience years year work working team teams
role ability strong skills skill knowledge required preferred plus well also all any new who what
how about through ensure lead leading leader leaders business company job position candidate""".split())


def job_keywords(job_text: str, top: int = 25) -> list[str]:
    """Terms a parser would match: capitalized tech terms and repeated two-word phrases."""
    t = re.sub(r"\s+", " ", job_text)
    words = re.findall(r"[A-Za-z][A-Za-z0-9+/#.&-]*[A-Za-z0-9+#]", t)
    counts: dict[str, int] = {}
    for w in words:
        if w.lower() in STOP or len(w) < 3:
            continue
        key = w if (w.isupper() or re.search(r"[A-Z].*[A-Z]|\d|[+#/]", w)) else w.lower()
        counts[key] = counts.get(key, 0) + 1
    low = [w.lower() for w in words]
    pairs: dict[str, int] = {}
    for a, b in zip(low, low[1:]):
        if a not in STOP and b not in STOP and len(a) > 2 and len(b) > 2:
            pairs[f"{a} {b}"] = pairs.get(f"{a} {b}", 0) + 1
    for ph, n in pairs.items():            # a phrase counts only if the posting repeats it
        if n >= 2:
            counts[ph] = n * 2
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    out = []
    for k, n in ranked:
        tech = k.isupper() or bool(re.search(r"[A-Z].*[A-Z]|\d|[+#/]", k))
        if n < 2 or k in out or (not tech and any(k.lower() in o.lower() for o in out)):
            continue
        out.append(k)
        if len(out) == top:
            break
    return out


DATE_STYLES = [r"[A-Z][a-z]{2} \d{4}", r"\d{4}", r"\d{1,2}/\d{4}"]


def check(k: dict, r: dict, max_pages: int, what: str) -> tuple[list[str], list[str]]:
    """Return (problems that must be fixed, notes worth a look)."""
    pages, text = r["pages"], r["text"]
    probs, notes = [], []
    if pages > max_pages:
        probs.append(f"{what}: {pages} pages (max {max_pages}); cut content")
    if r["overfull"]:
        probs.append(f"{what}: {len(r['overfull'])} line(s) run past the margin "
                     f"(worst {max(r['overfull']):.0f}pt); shorten them")
    if norm(k["name"]) not in norm(text[:400]):
        probs.append(f"{what}: name does not extract as text at the top of page 1")
    fills = r["fill"]
    if what == "resume":
        for head in ("summary", "experience", "education"):
            if not re.search(rf"^\s*[A-Z ]*{head.upper()}", text, re.M):
                probs.append(f"resume: section heading '{head}' does not extract as a clean word")
        flat = norm(text)
        for h in k.get("highlights") or []:
            words = norm(h).split()[:6]
            if words and " ".join(words) not in flat:
                probs.append(f"resume: achievement does not extract cleanly: {h[:60]}")
        if fills and fills[0] < 0.88 and pages == 1:
            notes.append(f"resume: page 1 is only {fills[0]:.0%} full; add strong content from the record")
        if pages == 2 and len(fills) > 1:
            if fills[1] < 0.30:
                probs.append(f"resume: page 2 is only {fills[1]:.0%} full; trim to one page or add real content")
            elif fills[1] < 0.5:
                notes.append(f"resume: page 2 is {fills[1]:.0%} full; consider adding depth to recent roles")
        # bullets that end in a near-empty line look uneven
        lines = text.splitlines()
        short = []
        for prev, cur in zip(lines, lines[1:]):
            c = cur.strip()
            if (c and re.match(r"^\s{2,}\S", cur)
                    and len(c) <= 18 and not re.search(r"\d{4}|[|]", c) and len(prev.strip()) > 60):
                short.append(c)
        if short:
            probs.append(f"resume: bullets ending in a nearly empty line (tighten): {', '.join(short[:5])}")
        long_b = [b for job in k.get("experience", []) for role in job.get("roles", [])
                  for b in role.get("bullets", []) if len(b) > 260]
        if long_b:
            notes.append(f"resume: {len(long_b)} bullet(s) over ~3 lines; split or tighten: {long_b[0][:50]}...")
        dates = [d for job in k.get("experience", []) for d in
                 [job.get("dates")] + [ro.get("dates") for ro in job.get("roles", [])] if d]
        styles = {next((i for i, pat in enumerate(DATE_STYLES) if re.match(pat, d.strip())), -1) for d in dates}
        if len(styles - {-1}) > 1 and not styles <= {0, 1}:
            notes.append("resume: date formats are mixed; use one style (e.g. 'Jun 2005 - Feb 2013')")
        if k.get("job_text"):
            kws = job_keywords(k["job_text"])
            missing = [w for w in kws if norm(w) not in flat]
            cover = 1 - len(missing) / max(1, len(kws))
            notes.append(f"resume: covers {cover:.0%} of the posting's top terms")
            if missing:
                notes.append("resume: posting terms not on the resume (add ONLY if the record supports them): "
                             + ", ".join(missing[:15]))
    else:
        if fills and not 0.35 <= fills[0] <= 0.92:
            notes.append(f"letter: page is {fills[0]:.0%} full; aim for a balanced page (40-90%)")
    left = re.findall(r"\[(?:VERIFY|ADD)[^\]]*\]|\bTODO\b|\[Company\]|\[Role\]", text)
    if left:
        probs.append(f"{what}: unfilled placeholders: {', '.join(sorted(set(left))[:4])}")
    if "—" in text:
        probs.append(f"{what}: contains an em dash")
    if re.search(r"\b(\w+) \1\b", text, re.I):
        probs.append(f"{what}: repeated word: '{re.search(r'\b(\w+) \1\b', text, re.I).group(0)}'")
    if not k.get("employed") and CURRENT_WORDS.search(text):
        probs.append(f"{what}: wording implies current employment: '{CURRENT_WORDS.search(text).group(0)}'")
    return probs, notes


def build(k: dict, out: Path, stem: str) -> dict:
    """Build, check and render both documents. Writes review.json next to them."""
    out.mkdir(parents=True, exist_ok=True)
    report = {"problems": [], "notes": [], "pages_to_view": []}
    attempts = [dict(), dict(size="10", margin="0.55", spread="1.0", secgap="7", itemsep="1.2"),
                dict(size="10", margin="0.5", spread="0.97", secgap="6", itemsep="0.8")]
    for i, opts in enumerate(attempts):
        r = compile_tex(resume_tex(k, **opts), out / f"{stem}_Resume.tex")
        if r["pages"] <= 2 or i == len(attempts) - 1:
            break
    p, n = check(k, r, 2, "resume")
    report["problems"] += p; report["notes"] += n
    report["resume"] = {"pages": r["pages"], "fill": r["fill"], "settings": opts or "default"}
    report["pages_to_view"] += [str(x) for x in render_pages(r["pdf"], "resume")]
    print(f"resume: {r['pages']} page(s), fill {', '.join(f'{f:.0%}' for f in r['fill'])}")
    if k.get("letter"):
        for i, opts in enumerate([dict(), dict(size="10.5", margin="0.8", spread="1.03")]):
            r = compile_tex(letter_tex(k, **opts), out / f"{stem}_Cover_Letter.tex")
            if r["pages"] <= 1:
                break
        if not k["letter"].get("date"):
            report["problems"].append("letter: no date; add today's date")
        if not any(t and "hiring" not in t.lower() for t in k["letter"].get("to", [])):
            report["notes"].append("letter: not addressed to the company by name")
        words = sum(len(x.split()) for x in k["letter"].get("paragraphs", []))
        if words > 400:
            report["problems"].append(f"letter: {words} words (keep under 350)")
        p, n = check(k, r, 1, "letter")
        report["problems"] += p; report["notes"] += n
        report["letter"] = {"pages": r["pages"], "fill": r["fill"], "words": words}
        report["pages_to_view"] += [str(x) for x in render_pages(r["pdf"], "letter")]
        print(f"letter: {r['pages']} page(s), {words} words, fill {r['fill'][0]:.0%}")
    report["ready"] = not report["problems"]
    report["visual_check"] = "pending"   # Claude sets this after opening every page image
    (out / "review.json").write_text(json.dumps(report, indent=1))
    return report


def main(argv=None) -> int:
    a = list(argv if argv is not None else sys.argv[1:])
    if len(a) < 2:
        print(__doc__); return 2
    k = json.loads(Path(a[0]).read_text())
    if "--job" in a:
        k["job_text"] = Path(a[a.index("--job") + 1]).read_text(errors="ignore")
    stem = a[a.index("--first-last") + 1] if "--first-last" in a else "_".join(k["name"].split()[:1] + k["name"].split()[-1:])
    if not shutil.which("pdflatex"):
        print("pdflatex not found: install TeX Live (or MacTeX / MiKTeX), or fall back to "
              "node tools/kit/build_docs.js kit.json <folder>")
        return 1
    rep = build(k, Path(a[1]), stem)
    for p in rep["problems"]:
        print("FIX:", p)
    for n in rep["notes"]:
        print("NOTE:", n)
    print("Now open every page image and review it (REVIEW.md):")
    for v in rep["pages_to_view"]:
        print("  VIEW:", v)
    print("READY (after the visual check)" if rep["ready"] else "NEEDS A FIX")
    return 0 if rep["ready"] else 1


if __name__ == "__main__":
    sys.exit(main())
