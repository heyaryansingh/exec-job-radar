"""Collector entry point.

    python -m collector.run                 # normal hourly run
    python -m collector.run --validate      # check every company entry, write data/health.json
    python -m collector.run --only "Capital One" --dry-run

Outputs (committed back to the repo by the GitHub Action):
    data/latest.json      roles that passed the rules, first seen in the last `keep_days`
    data/roles.json       the role database: every matching role with its lifecycle
    README.md             the public role list (rendered from roles.json)
    data/daily/DATE.md    roles first found on each day
    data/STATUS.md        collector health at a glance
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
from . import readme
from .sources import ADAPTERS, Ctx, check_open
from .store import Store, norm_company

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DESC_LIMIT = 3000


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

    listed: dict = {}  # company -> uids its site listed this run (for closure detection)
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
                listed[c["name"]] = (c.get("ats"), {p.uid for p in got})
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
        # board hits for companies we read directly are redundant (and less reliable)
        covered = {norm_company(c["name"]) for c in companies}
        results.extend(p for p in board if norm_company(p.company) not in covered)

    if a.validate:
        summary = {"run_at": now_iso(), "seconds": round(time.time() - started),
                   "companies": len(companies), "company_errors": errors,
                   "senior_titles_seen": len(results)}
        health["last_validate"] = summary
        DATA.mkdir(exist_ok=True)
        write_atomic(DATA / "health.json", json.dumps(health, indent=1, sort_keys=True))
        bad = {n: h for n, h in hc.items() if not h.get("ok")}
        log(json.dumps(summary, indent=2))
        log(f"\nVALIDATION: {len(companies) - len(bad)} ok, {len(bad)} failing")
        for n, h in sorted(bad.items()):
            log(f"  FAIL {n} [{h.get('ats')}]: {h.get('error', '')[:120]}")
        return 0

    # ---- evaluate new postings and update the role database
    DATA.mkdir(exist_ok=True)
    store = Store(DATA / "roles.json")
    _migrate_latest(store)
    today = date.today().isoformat()
    outcome, dropped = {"new": 0, "merged": 0, "reposted": 0}, {}
    for p in results:
        if store.has(p.uid):
            store.touch(p.uid)          # still listed: keep it open
            continue
        if p.uid in seen:
            continue                    # judged (and dropped) on an earlier run
        ok, why, score = rules.evaluate(p)
        if not ok:
            dropped[why] = dropped.get(why, 0) + 1
            seen[p.uid] = {"first": today, "pass": False}
            continue
        d = p.to_dict()
        d["score"] = score
        d["first_seen"] = now_iso()
        d["description"] = d["description"][:DESC_LIMIT]
        outcome[store.add(d)] += 1
        seen[p.uid] = {"first": today, "pass": True}

    # ---- closed roles: absent from a full listing twice, or confirmed gone on a direct check
    to_check = []
    for company, (ats, uids) in listed.items():
        to_check += store.mark_missing(company, uids, full_listing=ats in FULL_LISTING)
    closed_checked = 0
    check_session = session()
    for r in sorted(to_check, key=lambda r: r.get("last_checked", ""))[:CHECKS_PER_RUN]:
        if time.time() > deadline + 600:
            break
        state_ = check_open(r, check_session)
        r["last_checked"] = now_iso()
        if state_ is False:
            store.close(r["uid"], "posting removed")
            closed_checked += 1
        elif state_ is True:
            store.touch(r["uid"])
    store.expire()

    open_roles = store.open_roles()
    keep_days = int(cfg.get("keep_days", 10))
    cutoff = (date.today() - timedelta(days=keep_days)).isoformat()
    latest = [r for r in open_roles if r.get("first_seen", "")[:10] >= cutoff]
    latest.sort(key=lambda r: (-(r.get("score") or 0), r.get("first_seen", ""), r["uid"]))

    summary = {
        "run_at": now_iso(), "seconds": round(time.time() - started),
        "companies": len(companies), "company_errors": errors,
        "skipped_backoff": skipped_backoff, "skipped_out_of_time": skipped_budget,
        "senior_titles_seen": len(results), "new_roles": outcome["new"] + outcome["reposted"],
        "merged_duplicates": outcome["merged"], "reposted": outcome["reposted"],
        "closed_after_check": closed_checked, "dropped": dropped,
        "open_roles": len(open_roles), "roles_in_latest": len(latest),
    }
    log(json.dumps(summary, indent=2))

    if a.dry_run:
        for d in sorted(latest, key=lambda r: -r["score"])[:40]:
            log(f"{d['score']:3d}  {d['company']:<28} {d['title'][:70]:<70} {d['location'][:30]}"
                f"  {('$' + format(d['pay_max'], ',')) if d.get('pay_max') else ''}")
        return 0

    store.save()
    write_atomic(DATA / "latest.json", dump_lines({"updated": now_iso(), "roles": latest}))
    readme.write_all(ROOT, list(store.roles.values()), len(companies), lambda p, t: write_atomic(p, t))
    old = (date.today() - timedelta(days=120)).isoformat()
    seen = {k: v for k, v in seen.items() if v.get("first", today) >= old}
    write_atomic(DATA / "state.json", json.dumps({"seen": seen}, separators=(",", ":"), sort_keys=True))
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


FULL_LISTING = {"greenhouse", "lever", "ashby"}   # these APIs list every open job
CHECKS_PER_RUN = 400


def dump_lines(obj: dict) -> str:
    """JSON with one role per line, so hourly commits store small diffs."""
    roles = obj["roles"]
    body = ",\n".join(json.dumps(r, separators=(",", ":"), sort_keys=True) for r in roles)
    return '{"updated":%s,"roles":[\n%s\n]}\n' % (json.dumps(obj["updated"]), body)


def _migrate_latest(store: Store):
    """One-time import of roles found before the role database existed."""
    if store.roles:
        return
    for r in load_json(DATA / "latest.json", {"roles": []}).get("roles", []):
        if r.get("uid") and r.get("company"):
            store.add(r)


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


if __name__ == "__main__":
    sys.exit(main())
