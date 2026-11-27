import json
import shutil
from pathlib import Path

import pytest

from tools.kit import build_latex as bl

KIT = {
    "name": "Pat Example", "employed": False,
    "contact": ["Austin, TX", "pat@mailbox.test", "+1 (512) 555-0100", "linkedin.com/in/pat"],
    "headline": "Technology Executive | Cloud & Platform Engineering",
    "summary": "Technology leader with 20 years running large platforms in regulated industries.",
    "competencies": ["Cloud Strategy", "Site Reliability Engineering", "Enterprise Architecture"],
    "highlights": ["Migrated 3,000 servers to AWS in 18 months.", "Cut incident resolution from 10 hours to 1 hour."],
    "experience": [{"org": "Big Bank & Co", "location": "Dallas, TX", "dates": "2005 - 2024",
                    "roles": [{"title": "VP, Infrastructure", "dates": "Jan 2015 - Mar 2024",
                               "scope": "400 engineers, $60M budget",
                               "bullets": ["Led the 100% migration of the trading platform to cloud."]}]}],
    "education": ["M.S., Computer Science, Test University"],
    "skills": [["Cloud", "AWS, GCP"]],
    "letter": {"date": "Nov 1, 2026", "to": ["Hiring Team", "[Company]"], "salutation": "Dear Hiring Team,",
               "paragraphs": ["I led the migration of 3,000 servers to AWS."], "signature": "Pat Example"},
}


def test_escape_and_dashes():
    assert bl.esc("R&D 100% $5M #1 a_b") == r"R\&D 100\% \$5M \#1 a\_b"
    assert bl.esc("2019-2022") == "2019--2022"
    assert bl.esc("Jan 2015 - Mar 2024") == "Jan 2015 -- Mar 2024"
    assert bl.esc("+1 (512) 555-0100") == "+1 (512) 555-0100"     # phone numbers keep the hyphen


def test_tex_has_ats_settings_and_no_small_caps():
    tex = bl.resume_tex(KIT)
    assert r"\pdfgentounicode=1" in tex and r"\hyphenpenalty=10000" in tex
    assert r"\scshape" not in tex                                  # small caps extract as "P AT"
    assert "400 engineers" in tex and r"\href{mailto:pat@mailbox.test}" in tex


def test_check_flags_problems():
    text = ("Pat Example\nEXECUTIVE SUMMARY\nI am currently leading [VERIFY: end] — the the x\n"
            "EXPERIENCE\nEDUCATION\n")
    r = {"pages": 3, "text": text, "overfull": [12.0], "fill": [1.0, 1.0, 0.2]}
    probs, notes = bl.check(dict(KIT, job_text="Kubernetes Kubernetes Terraform Terraform"), r, 2, "resume")
    joined = " | ".join(probs)
    assert "3 pages" in joined and "placeholders" in joined and "em dash" in joined
    assert "current employment" in joined and "achievement" in joined
    assert "past the margin" in joined and "repeated word" in joined
    assert any("kubernetes" in n.lower() for n in notes)


def test_job_keywords_prefers_repeated_terms():
    kws = bl.job_keywords("Lead AWS cloud migration. AWS cloud migration at scale. Partner with finance once.")
    assert "AWS" in kws and "cloud migration" in kws and "partner finance" not in kws


@pytest.mark.skipif(not all(shutil.which(t) for t in ("pdflatex", "pdftotext", "pdfinfo")), reason="no LaTeX")
def test_builds_ready_pdfs(tmp_path: Path):
    rep = bl.build(KIT, tmp_path, "Pat_Example")
    assert (tmp_path / "Pat_Example_Resume.pdf").exists() and (tmp_path / "Pat_Example_Cover_Letter.pdf").exists()
    assert not [p for p in rep["problems"] if "placeholder" not in p], rep["problems"]
    assert rep["pages_to_view"] and all(Path(p).exists() for p in rep["pages_to_view"])
    assert json.loads((tmp_path / "review.json").read_text())["visual_check"] == "pending"


def test_tailor_maps_terms_to_evidence(tmp_path: Path, capsys):
    from tools.kit import tailor
    (tmp_path / "job.md").write_text("AWS cloud migration. Kubernetes Kubernetes. AWS cloud migration again.")
    (tmp_path / "rec.md").write_text("- Migrated 5,000+ servers to AWS through a cloud migration program.\n")
    tailor.main([str(tmp_path / "job.md"), str(tmp_path / "rec.md")])
    out = capsys.readouterr().out
    assert "| kubernetes | no evidence" in out.lower() and "Migrated 5,000+" in out


def test_app_index(tmp_path: Path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("ai", Path(__file__).resolve().parents[1] / "tools" / "app_index.py")
    ai = importlib.util.module_from_spec(spec); spec.loader.exec_module(ai)
    (tmp_path / "tracker.json").write_text(json.dumps({"candidate": "Pat", "roles": {
        "a": {"status": "submitted", "status_at": "2026-11-02T10:00", "company": "B", "title": "VP", "url": "u"},
        "b": {"status": "submitted", "status_at": "2026-11-05T10:00", "company": "C", "title": "Dir", "url": "v"},
        "c": {"status": "skipped", "status_at": "2026-11-06T10:00", "company": "D", "title": "X"}}}))
    idx, csv_path = ai.write(tmp_path)
    md = idx.read_text()
    assert md.index("## Submitted") < md.index("## Passed on") and md.index("| C |") < md.index("| B |")
    assert csv_path.read_text().splitlines()[0].startswith("status,")
