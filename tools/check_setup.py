"""Check a candidate's Job Search folder and this machine before a run (or during setup).

    python tools/check_setup.py "<path to Job Search folder>" [--fix] [--json]

Checks candidate.yaml (parses, no TODOs left, valid run settings), master_resume.md (filled
in, not the template), tracker.json (parses), the collector feed (reachable, fresh), and the
tools a run needs (node + the `docx` package, LibreOffice for PDFs). With --fix it installs
the `docx` package next to tools/kit/build_docs.js. Exit code 0 = ready, 1 = blocking
problems, 2 = warnings only.

The playbook runs this in Preflight; ONBOARD.md runs it at the end of setup.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[1]
KIT_DIR = REPO_ROOT / "tools" / "kit"
AUTONOMY = {"review", "submit_quick_forms", "submit_signed_in"}
DEFAULT_FEED_REPO = "heyaryansingh/exec-job-radar"

# Fields every form asks for: a TODO here blocks submission on nearly every application.
CRITICAL = {
    "name", "email", "phone", "address.city", "address.state",
    "work_authorization.authorized_to_work_in_us", "work_authorization.requires_sponsorship",
    "employment_answers.currently_employed",
}


def todo_paths(node, prefix=""):
    """Every dotted path whose value is TODO (or contains it)."""
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            out += todo_paths(v, f"{prefix}.{k}" if prefix else str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            out += todo_paths(v, f"{prefix}[{i}]")
    elif isinstance(node, str) and node.strip().upper().startswith("TODO"):
        out.append(prefix)
    return out


def feed_age_hours(repo: str):
    """Hours since the collector feed was updated, or None if unreachable."""
    import urllib.request
    for branch in ("data", "main"):
        url = f"https://raw.githubusercontent.com/{repo}/{branch}/data/apply_queue.json"
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                head = r.read(400).decode("utf-8", "replace")
            m = re.search(r'"updated"\s*:\s*"([^"]+)"', head)
            if not m:
                continue
            t = datetime.fromisoformat(m.group(1).replace("Z", "+00:00"))
            return (datetime.now(timezone.utc) - t).total_seconds() / 3600
        except Exception:
            continue
    return None


def docx_installed() -> bool:
    if not shutil.which("node"):
        return False
    r = subprocess.run(["node", "-e", "require('docx')"], cwd=KIT_DIR, capture_output=True)
    return r.returncode == 0


def check(folder: Path, fix: bool):
    blocking, warnings, info = [], [], []

    # candidate.yaml
    cy = folder / "candidate.yaml"
    cand = {}
    if not cy.exists():
        blocking.append(f"candidate.yaml is missing in {folder}. Copy it from candidate_template/.")
    elif yaml is None:
        warnings.append("PyYAML is not installed (pip install pyyaml); candidate.yaml not checked.")
    else:
        try:
            cand = yaml.safe_load(cy.read_text(encoding="utf-8")) or {}
        except Exception as e:
            blocking.append(f"candidate.yaml does not parse: {e}")
    if cand:
        todos = todo_paths(cand)
        crit = [t for t in todos if t in CRITICAL]
        if crit:
            blocking.append("candidate.yaml: fill these first, every form asks for them: " + ", ".join(crit))
        rest = [t for t in todos if t not in CRITICAL]
        if rest:
            warnings.append("candidate.yaml still has TODO (each becomes a 'needs you' flag): " + ", ".join(rest))
        run = cand.get("run") or {}
        if run.get("autonomy", "review") not in AUTONOMY:
            blocking.append(f"run.autonomy must be one of {sorted(AUTONOMY)}")
        repo = str(run.get("repo") or "")
        if not repo or repo.startswith("OWNER/") or "/" not in repo:
            warnings.append(f"run.repo is not set; using the shared feed {DEFAULT_FEED_REPO}.")
            repo = DEFAULT_FEED_REPO
        age = feed_age_hours(repo)
        if age is None:
            blocking.append(f"Can't read the feed for {repo} (data/apply_queue.json on the data branch). "
                            "Check the repo name, that it is public, and that 'Collect roles' has run.")
        elif age > 6:
            warnings.append(f"Feed for {repo} is {age:.0f} hours old; check data/STATUS.md and the Heartbeat workflow.")
        else:
            info.append(f"Feed {repo}: updated {age:.1f} h ago.")
        info.append(f"Autonomy: {run.get('autonomy', 'review')}; ramp: {bool(run.get('autonomy_ramp'))}.")

    # master_resume.md
    mr = folder / "master_resume.md"
    if not mr.exists():
        blocking.append("master_resume.md is missing. It is the only source of facts a run may use.")
    else:
        text = mr.read_text(encoding="utf-8")
        if "# FULL NAME" in text or "One line per headline result" in text or len(text) < 800:
            blocking.append("master_resume.md is still the template (or very short). Put the full, true career record in it.")

    # tracker.json
    tr = folder / "tracker.json"
    if tr.exists():
        try:
            json.loads(tr.read_text(encoding="utf-8"))
        except Exception as e:
            blocking.append(f"tracker.json does not parse ({e}); restore tracker.backup.json.")

    # tools
    if not shutil.which("node"):
        blocking.append("node is not installed, so tailored resumes can't be built. Install Node.js 18+ (nodejs.org).")
    elif not docx_installed():
        if fix:
            r = subprocess.run(["npm", "install", "--no-save", "--no-audit", "--no-fund", "docx@9"],
                               cwd=KIT_DIR, capture_output=True, text=True)
            (info if r.returncode == 0 else warnings).append(
                "Installed the docx package." if r.returncode == 0 else f"npm install docx failed: {r.stderr[-300:]}")
        else:
            warnings.append("The node 'docx' package is missing: run with --fix (or `npm install docx@9` in tools/kit).")
    if not (shutil.which("soffice") or shutil.which("libreoffice")):
        warnings.append("LibreOffice (soffice) not found: kits upload as .docx instead of .pdf (most forms accept both).")
    return blocking, warnings, info


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    folder = Path(argv[1]).expanduser()
    blocking, warnings, info = check(folder, "--fix" in argv)
    if "--json" in argv:
        print(json.dumps({"ready": not blocking, "blocking": blocking, "warnings": warnings, "info": info}, indent=1))
    else:
        for label, items in (("BLOCKING", blocking), ("WARNING", warnings), ("ok", info)):
            for x in items:
                print(f"[{label}] {x}")
        print("READY" if not blocking else "NOT READY: fix the BLOCKING items above.")
    return 1 if blocking else (2 if warnings else 0)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
