import json
import shutil
from pathlib import Path

from tools import check_setup, render_dashboard

ROOT = Path(__file__).resolve().parents[1]


def test_todo_paths_finds_nested_todos():
    cand = {"name": "TODO", "address": {"city": "Houston", "zip": "TODO"},
            "education": [{"degree": "TODO", "school": "Rice"}], "run": {"autonomy": "review"}}
    assert set(check_setup.todo_paths(cand)) == {"name", "address.zip", "education[0].degree"}


def test_template_folder_is_not_ready(tmp_path, monkeypatch):
    for f in ("candidate.yaml", "master_resume.md", "notes.md"):
        shutil.copy(ROOT / "candidate_template" / f, tmp_path / f)
    monkeypatch.setattr(check_setup, "feed_age_hours", lambda repo: 1.0)
    blocking, warnings, info = check_setup.check(tmp_path, fix=False)
    assert any("every form asks for them" in b for b in blocking)
    assert any("master_resume.md" in b for b in blocking)
    assert any("heyaryansingh/exec-job-radar" in i for i in info)


def test_dashboard_links_named_kit_files(tmp_path):
    folder = tmp_path / "applications" / "2026-11-27_Acme_VP"
    folder.mkdir(parents=True)
    (folder / "Jane_Doe_Resume.pdf").write_bytes(b"%PDF")
    (folder / "Jane_Doe_Cover_Letter.docx").write_bytes(b"PK")
    tracker = {"candidate": "Jane", "runs": [], "unlock": [{"company": "Chevron", "site": "x", "roles": 3, "best_score": 86}],
               "roles": {"a": {"uid": "a", "company": "Acme", "title": "VP", "status": "filled",
                               "folder": "applications/2026-11-27_Acme_VP", "url": "https://x"}}}
    (tmp_path / "tracker.json").write_text(json.dumps(tracker))
    render_dashboard.BASE = tmp_path
    page = render_dashboard.render(tracker)
    assert "Jane_Doe_Resume.pdf" in page and "Jane_Doe_Cover_Letter.docx" in page
    assert "unlock the most roles" in page
