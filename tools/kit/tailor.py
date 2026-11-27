"""Map a job posting to the candidate's record, so every resume is tailored from evidence.

    python tools/kit/tailor.py <job.md> <master_resume.md> [<base kit.json>] > tailor.md

Writes a Markdown worksheet:
  1. The posting's top terms (what a recruiter and an ATS will look for), each with the
     record lines that support it, or "no evidence" (never claim those).
  2. The record's bullets ranked by relevance to this posting (lead with the top ones).
  3. Base-kit competencies that match the posting, and posting terms worth turning into
     competencies because the record supports them.
Claude uses it to rewrite the headline, summary, competencies, achievements order, bullet
wording and skills order for this role (PLAYBOOK.md Step 5, "Tailor").
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_latex import job_keywords, norm  # noqa: E402

SYNONYMS = {
    "site reliability": ["sre"], "reliability engineering": ["sre", "reliability"],
    "platform engineering": ["platform"], "cloud infrastructure": ["cloud", "infrastructure"], "sre": ["site reliability"], "kubernetes": ["k8s", "containers"],
    "cloud migration": ["migrated", "migration to aws", "migration to gcp"],
    "observability": ["monitoring"], "incident management": ["incident", "major incident"],
    "cost optimization": ["cost", "cutting cost", "reduction in operating costs", "savings"],
    "governance": ["data governance"], "artificial intelligence": ["ai"], "genai": ["ai", "agentic"],
    "machine learning": ["ai"], "digital transformation": ["transformation", "modernization"],
    "vendor management": ["vendor", "contracts"], "stakeholder": ["executive", "leadership"],
    "regulatory": ["regulated", "regulatory"], "risk": ["risk management", "credit risk"],
}


def record_lines(md: str) -> list[str]:
    out = []
    for line in md.splitlines():
        t = line.strip().lstrip("-*").strip()
        if len(t) > 25 and not t.startswith(("#", "<!--", "[ADD", "[VERIFY")):
            out.append(re.sub(r"\*\*", "", t))
    return out


def evidence(term: str, lines: list[str]) -> list[str]:
    keys = [norm(term)] + [norm(s) for s in SYNONYMS.get(term.lower(), [])]
    words = norm(term).split()
    hits = []
    for l in lines:
        nl = norm(l)
        if any(k and re.search(rf"\b{re.escape(k)}\b", nl) for k in keys) or (
                len(words) > 1 and all(re.search(rf"\b{re.escape(w)}", nl) for w in words)):
            hits.append(l)
    return hits


def main(argv=None) -> int:
    a = list(argv if argv is not None else sys.argv[1:])
    if len(a) < 2:
        print(__doc__); return 2
    job = Path(a[0]).read_text(errors="ignore")
    lines = record_lines(Path(a[1]).read_text(errors="ignore"))
    kit = json.loads(Path(a[2]).read_text()) if len(a) > 2 and Path(a[2]).exists() else {}
    terms = job_keywords(job, top=30)

    out = ["# Tailoring worksheet", "", "## 1. Posting terms and the record's evidence", "",
           "| Term | Evidence in the record | Use |", "|---|---|---|"]
    supported, unsupported = [], []
    for t in terms:
        ev = evidence(t, lines)
        if ev:
            supported.append(t)
            out.append(f"| {t} | {ev[0][:110]}{' (+%d more)' % (len(ev) - 1) if len(ev) > 1 else ''} | use the posting's wording |")
        else:
            unsupported.append(t)
            out.append(f"| {t} | no evidence | do not claim; mention nothing |")
    cover = len(supported) / max(1, len(terms))
    out += ["", f"Supported: {len(supported)}/{len(terms)} ({cover:.0%}). "
            "Rule: only supported terms may appear on the resume or letter.", ""]

    out += ["## 2. Record bullets ranked for this role (lead with the top ones)", ""]
    scored = []
    for l in lines:
        nl = norm(l)
        s = sum(2 if " " in t else 1 for t in supported if norm(t) in nl or evidence(t, [l]))
        if s:
            s += 1 if re.search(r"\d", l) else 0      # quantified results first among equals
            scored.append((s, l))
    for s, l in sorted(scored, key=lambda x: -x[0])[:15]:
        out.append(f"- ({s}) {l[:160]}")

    if kit.get("competencies"):
        out += ["", "## 3. Core competencies", ""]
        keep = [c for c in kit["competencies"] if any(norm(t) in norm(c) or norm(c) in norm(job) for t in supported)]
        out.append("- Base competencies that match the posting (put first): " + (", ".join(keep) or "none"))
        new = [t for t in supported if not any(norm(t) in norm(c) for c in kit["competencies"])]
        out.append("- Supported posting terms to add as competencies (posting's wording): " + (", ".join(new[:8]) or "none"))
    out += ["", "## 4. Tailoring checklist", "",
            "- Headline: target level + the posting's domain words.",
            "- Summary: 3-4 lines answering the posting's top 3 needs with record results.",
            "- Competencies: 9-12, posting's wording first, all supported.",
            "- Achievements: reorder so the 3 most relevant (section 2) lead; rephrase in the posting's terms.",
            "- Experience: reorder and reword bullets toward the posting; keep every fact exact.",
            "- Skills: put the posting's tools first; drop irrelevant ones if space is tight.",
            "- Letter: open with this company's priority; prove 2-3 needs with numbers from section 2."]
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
