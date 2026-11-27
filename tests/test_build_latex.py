import json
import shutil
from pathlib import Path

import pytest

from tools.kit import build_latex as bl

KIT = {
    "name": "Pat Example", "employed": False,
    "contact": ["Austin, TX", "pat@example.com", "+1 (512) 555-0100", "linkedin.com/in/pat"],
    "headline": "Technology Executive | Cloud & Platform Engineering",
    "summary": "Technology leader with 20 years running large platforms in regulated industries.",
    "competencies": ["Cloud Strategy", "Site Reliability Engineering", "Enterprise Architecture"],
    "highlights": ["Migrated 3,000 servers to AWS in 18 months.", "Cut incident resolution from 10 hours to 1 hour."],
    "experience": [{"org": "Big Bank & Co", "location": "Dallas, TX", "dates": "2005 - 2024",
                    "roles": [{"title": "VP, Infrastructure", "dates": "Jan 2015 - Mar 2024",
                               "scope": "400 engineers, $60M budget",
                               "bullets": ["Led the 100% migration of the trading platform to cloud."]}]}],
    "education": ["M.S., Computer Science, Example University"],
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
    assert "400 engineers" in tex and r"\href{mailto:pat@example.com}" in tex


def test_check_flags_problems():
    text = "Pat Example\nEXECUTIVE SUMMARY\nI am currently leading [VERIFY: end] — x\nEXPERIENCE\nEDUCATION\n"
    probs = bl.check(KIT, 3, text, 2, "resume")
    joined = " | ".join(probs)
    assert "3 pages" in joined and "placeholders" in joined and "em dash" in joined
    assert "current employment" in joined and "achievement" in joined


@pytest.mark.skipif(not all(shutil.which(t) for t in ("pdflatex", "pdftotext", "pdfinfo")), reason="no LaTeX")
def test_builds_ready_pdfs(tmp_path: Path):
    problems = bl.build(KIT, tmp_path, "Pat_Example")
    assert (tmp_path / "Pat_Example_Resume.pdf").exists() and (tmp_path / "Pat_Example_Cover_Letter.pdf").exists()
    assert not [p for p in problems if "placeholder" not in p], problems
