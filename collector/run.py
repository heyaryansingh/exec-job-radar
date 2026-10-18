"""Collector entry point.

    python -m collector.run                 # normal hourly run
    python -m collector.run --validate      # check every company entry, write data/health.json
    python -m collector.run --only "Capital One" --dry-run

Outputs (committed back to the repo by the GitHub Action):
    data/latest.json      roles that passed the rules, first seen in the last `keep_days`
    data/latest.md        the same, as a readable table
    data/new/YYYY-MM-DD.jsonl   append-only log of newly found roles
    data/state.json       uids already processed (so details are fetched once)
    data/health.json      per-company status, so broken entries are easy to spot
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta
from pathlib import Path

import yaml

from .boards import sweep
from .common import now_iso, session
from .filters import Rules
from .sources import ADAPTERS, Ctx

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DESC_LIMIT = 5000


def log(msg: str):
    print(msg, flush=True)


def write_atomic(p: Path, text: str):
    """Write via a temp file so a crash never leaves half-written JSON behind."""
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(text)
    tmp.replace(p)


def _hours_since(iso) -> float:
    if not iso:
        return 1e9
    try:
        from datetime import datetime, timezone
        t = datetime.fromisoformat(iso)
        return (datetime.now(timezone.utc) - t).total_seconds() / 3600
    except ValueError:
        return 1e9


def load_yaml(p: Path):
    return yaml.safe_load(p.read_text()) if p.exists() else None


def load_json(p: Path, default):
    try:
        return json.loads(p.read_text())
    except Exception:
        return default


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(ROOT / "config" / "search.yaml"))
    ap.add_argument("--companies", default=str(ROOT / "config" / "companies.yaml"))
    ap.add_argument("--only", help="run a single company by name")
    ap.add_argument("--no-boards", action="store_true")
    ap.add_argument("--validate", action="store_true", help="report on every company entry")
    ap.add_argument("--dry-run", action="store_true", help="print results, write nothing")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--budget-minutes", type=float, default=40,
                    help="stop starting new companies after this long (the hourly job must finish)")
    a = ap.parse_args(argv)

    cfg = load_yaml(Path(a.config))
    companies = [c for c in (load_yaml(Path(a.companies)) or []) if c and not c.get("disabled")]
    if a.only:
        companies = [c for c in companies if c["name"].lower() == a.only.lower()]
    rules = Rules(cfg)

    state = load_json(DATA / "state.json", {"seen": {}})
    seen: dict = state.get("seen", {})
    class _All(set):  # validation only lists jobs; it never fetches details
        def __contains__(self, _):
            return True
    known = _All() if a.validate else set(seen)
    ctx = Ctx(title_ok=rules.title_ok, known=known, level_queries=rules.level_queries,
              max_age_days=rules.max_age)
    health = load_json(DATA / "health.json", {"companies": {}})
    hc = health.setdefault("companies", {})

    started = time.time()
    results, errors, skipped_backoff, skipped_budget = [], 0, 0, 0
    deadline = started + a.budget_minutes * 60

    # Back off from broken sites: after 6 straight failures, only retry every 12 hours.
    # Stalest companies go first so a slow run never starves the same ones twice.
    def due(c):
        h = hc.get(c["name"], {})
        if a.validate or a.only or int(h.get("failures", 0)) < 6:
            return True
        return _hours_since(h.get("last_attempt")) >= 12

    queue = []
    for c in companies:
        if due(c):
            queue.append(c)
        else:
            skipped_backoff += 1
    queue.sort(key=lambda c: hc.get(c["name"], {}).get("last_attempt", ""))

    def job(c):
        if time.time() > deadline:
            return None  # out of time; this company goes first next hour
        s = session()
        fn = ADAPTERS.get(c.get("ats", ""))
        if not fn:
            raise RuntimeError(f"unknown ats '{c.get('ats')}'")
        return fn(c, s, ctx)

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(job, c): c for c in queue}
        for f in as_completed(futs):
            c = futs[f]
            h = hc.setdefault(c["name"], {})
            h["ats"] = c.get("ats")
            try:
                got = f.result()
                if got is None:
                    skipped_budget += 1
                    continue
                results.extend(got)
                h.update(ok=True, matched_titles=len(got), last_ok=now_iso(), failures=0, error="",
                         last_attempt=now_iso())
            except Exception as e:
                errors += 1
                h.update(ok=False, error=str(e)[:300], failures=int(h.get("failures", 0)) + 1,
                         last_attempt=now_iso())
                log(f"  ! {c['name']}: {str(e)[:160]}")

    if not a.no_boards and not a.only and not a.validate:
        try:
            board = sweep(cfg, ctx, log) if time.time() < deadline + 300 else []
        except Exception as e:  # never let the optional sweep sink the run
            log(f"boards: failed ({e})")
            board = []
        log(f"boards: {len(board)} senior titles")
        # skip board hits for companies already covered by their own ATS feed
        covered = {c["name"].lower() for c in companies}
        results.extend(p for p in board if p.company.lower() not in covered)

    # ---- evaluate
    today = date.today().isoformat()
    new_pass, dropped = [], {}
    for p in results:
        if p.uid in seen and not a.validate:
            continue  # already judged on an earlier run
        ok, why, score = rules.evaluate(p)
        if not ok:
            dropped[why] = dropped.get(why, 0) + 1
            seen[p.uid] = {"first": today, "pass": False}
            continue
        d = p.to_dict()
        d["score"] = score
        d["first_seen"] = now_iso()
        d["description"] = d["description"][:DESC_LIMIT]
        new_pass.append(d)
        seen[p.uid] = {"first": today, "pass": True}

    # de-duplicate the same role posted in several places (company + title + city)
    def key(d):
        return (d["company"].lower(), d["title"].lower(), (d["location"] or "").lower()[:30])

    latest = load_json(DATA / "latest.json", {"roles": []}).get("roles", [])
    keep_days = int(cfg.get("keep_days", 10))
    cutoff = (date.today() - timedelta(days=keep_days)).isoformat()
    latest = [r for r in latest if r.get("first_seen", "")[:10] >= cutoff]
    have = {key(r) for r in latest}
    fresh = [d for d in new_pass if key(d) not in have]
    latest.extend(fresh)
    latest.sort(key=lambda r: (r.get("score", 0), r.get("first_seen", "")), reverse=True)

    summary = {
        "run_at": now_iso(), "seconds": round(time.time() - started),
        "companies": len(companies), "company_errors": errors,
        "skipped_backoff": skipped_backoff, "skipped_out_of_time": skipped_budget,
        "senior_titles_seen": len(results), "new_roles": len(fresh),
        "dropped": dropped, "roles_in_latest": len(latest),
    }
    log(json.dumps(summary, indent=2))

    if a.validate:
        health["last_validate"] = summary
        DATA.mkdir(exist_ok=True)
        write_atomic(DATA / "health.json", json.dumps(health, indent=1, sort_keys=True))
        bad = {n: h for n, h in hc.items() if not h.get("ok")}
        log(f"\nVALIDATION: {len(companies) - len(bad)} ok, {len(bad)} failing")
        for n, h in sorted(bad.items()):
            log(f"  FAIL {n} [{h.get('ats')}]: {h.get('error', '')[:120]}")
        return 0

    if a.dry_run:
        for d in sorted(fresh, key=lambda r: -r["score"])[:40]:
            log(f"{d['score']:3d}  {d['company']:<28} {d['title'][:70]:<70} {d['location'][:30]}"
                f"  {('$' + format(d['pay_max'], ',')) if d.get('pay_max') else ''}")
        return 0

    DATA.mkdir(exist_ok=True)
    (DATA / "new").mkdir(exist_ok=True)
    if fresh:
        with open(DATA / "new" / f"{today}.jsonl", "a") as fh:
            for d in fresh:
                fh.write(json.dumps(d) + "\n")
    write_atomic(DATA / "latest.json", json.dumps({"updated": now_iso(), "roles": latest}, indent=1))
    write_markdown(latest)
    # prune processed-uid memory after 120 days
    old = (date.today() - timedelta(days=120)).isoformat()
    seen = {k: v for k, v in seen.items() if v.get("first", today) >= old}
    write_atomic(DATA / "state.json", json.dumps({"seen": seen}))
    health["last_run"] = summary
    write_status(health, latest)
    write_atomic(DATA / "health.json", json.dumps(health, indent=1, sort_keys=True))
    attempted = len(companies) - skipped_backoff - skipped_budget
    if attempted >= 10 and errors > attempted * 0.5:
        # Most sites failing at once points to something systemic (network, blocking, a
        # code bug). Results are still saved, but the run is marked failed so GitHub emails
        # the repo owner.
        log(f"ERROR: {errors} of {attempted} companies failed")
        return 1
    return 0


def write_status(health, latest):
    """data/STATUS.md: one glance at whether the collector is healthy."""
    hc = health.get("companies", {})
    ok = sum(1 for h in hc.values() if h.get("ok"))
    failing = sorted(((n, h) for n, h in hc.items() if not h.get("ok")), key=lambda t: -int(t[1].get("failures", 0)))
    run = health.get("last_run", {})
    lines = ["# Collector status", "",
             f"- Last run: {run.get('run_at', '?')} UTC, {run.get('seconds', '?')}s",
             f"- Companies working: {ok} of {len(hc)}",
             f"- New roles last run: {run.get('new_roles', 0)}; roles in feed: {len(latest)}",
             f"- Skipped (backing off broken sites): {run.get('skipped_backoff', 0)}; "
             f"ran out of time: {run.get('skipped_out_of_time', 0)}", ""]
    if failing:
        lines += ["## Failing companies", "", "| Company | Failures in a row | Last error |", "|---|---:|---|"]
        for n, h in failing[:100]:
            lines.append(f"| {n} | {h.get('failures', 0)} | {str(h.get('error', ''))[:100].replace('|', '/')} |")
        lines += ["", "Fix an entry with tools/add_company.py, or add `disabled: true` to it in "
                  "config/companies.yaml."]
    write_atomic(DATA / "STATUS.md", "\n".join(lines) + "\n")


def write_markdown(latest):
    lines = ["# Latest matching roles", "",
             f"Updated {now_iso()} UTC. Sorted by quick score (the Claude run re-ranks).", "",
             "| Score | Company | Role | Location | Pay | First seen |",
             "|---:|---|---|---|---|---|"]
    for r in latest[:200]:
        pay = f"${r['pay_max']:,}" if r.get("pay_max") else ""
        title = r["title"].replace("|", "/")
        loc = (r.get("location") or "").replace("|", "/")[:40]
        lines.append(f"| {r.get('score', 0)} | {r['company']} | [{title}]({r['url']}) | {loc} | "
                     f"{pay} | {r.get('first_seen', '')[:10]} |")
    write_atomic(DATA / "latest.md", "\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.exit(main())
