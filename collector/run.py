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

from . import aggregators, universe
from .atsurl import try_parse
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
    ap.add_argument("--no-universe", action="store_true", help="watchlist only")
    ap.add_argument("--universe-limit", type=int, default=0, help="poll at most N universe boards (tests)")
    ap.add_argument("--report", help="dry run: write a test report here")
    ap.add_argument("--test-new", action="store_true",
                    help="turn on the universe and every aggregator regardless of config (tests)")
    ap.add_argument("--budget-minutes", type=float, default=40,
                    help="stop starting new companies after this long (the hourly job must finish)")
    a = ap.parse_args(argv)

    cfg = load_yaml(Path(a.config))
    if a.test_new:
        cfg.setdefault("universe", {})["enabled"] = True
        for k in ("themuse", "adzuna"):
            cfg.setdefault("aggregators", {}).setdefault(k, {})["enabled"] = True
        sites = cfg.setdefault("boards", {}).setdefault("sites", ["indeed", "google"])
        if "zip_recruiter" not in sites:
            sites.append("zip_recruiter")
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
    hc = health.setdefault("companies", {})      # watchlist health, by company name
    hu = health.setdefault("universe", {})        # universe health, by board id
    for c in companies:
        c["board"] = universe.identity(c)

    # the universe: every other known career site (Common Crawl directory + auto-found)
    universe_on = bool((cfg.get("universe") or {}).get("enabled", False))
    uni = [] if (not universe_on or a.no_universe or a.only or a.validate) else universe.build(DATA, companies)
    if a.universe_limit:
        uni = sorted(uni, key=lambda c: hu.get(c["board"], {}).get("last_attempt", ""))[: a.universe_limit]
    if not a.only:  # forget companies removed from the watchlist / universe
        names = {c["name"] for c in companies}
        for n in [n for n in hc if n not in names]:
            del hc[n]
        if not a.no_universe and not a.universe_limit:
            ids = {c["board"] for c in uni}
            for b in [b for b in hu if b not in ids]:
                del hu[b]

    def hrec(c):
        return hu.setdefault(c["board"], {}) if c.get("universe") else hc.setdefault(c["name"], {})

    started = time.time()
    results, errors, uerrors, skipped_backoff, skipped_budget = [], 0, 0, 0, 0
    deadline = started + a.budget_minutes * 60

    # Back off from broken sites: after 6 straight failures, retry every 12 hours
    # (universe boards: after 3 failures, every 3 days). Watchlist first, then the
    # universe; stalest first within each, so a slow run never starves the same ones.
    def due(c):
        h = (hu if c.get("universe") else hc).get(c["board"] if c.get("universe") else c["name"], {})
        if a.validate or a.only:
            return True
        limit, wait = (3, 72) if c.get("universe") else (6, 12)
        return int(h.get("failures", 0)) < limit or _hours_since(h.get("last_attempt")) >= wait

    queue = []
    for c in companies + uni:
        if due(c):
            queue.append(c)
        else:
            skipped_backoff += 1
    queue.sort(key=lambda c: (bool(c.get("universe")), hrec(c).get("last_attempt", "")))

    learned_names: dict = {}

    def job(c):
        if time.time() > deadline:
            return None  # out of time; this one goes first next hour
        s = session()
        fn = ADAPTERS.get(c.get("ats", ""))
        if not fn:
            raise RuntimeError(f"unknown ats '{c.get('ats')}'")
        got = fn(c, s, ctx)
        if c.get("universe") and got and not c.get("named"):
            # first matching role on an unnamed board: learn the employer's name once,
            # then keep it forever so role ids stay stable
            name = c.get("_org") or universe.resolve_name(c, s) or c["name"]
            learned_names[c["board"]] = name
            for p in got:
                p.company = name
        for p in got:
            p.extra["board"] = c["board"]
        return got

    listed: dict = {}  # board -> (ats, company, uids listed this run), for closure detection
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(job, c): c for c in queue}
        for f in as_completed(futs):
            c = futs[f]
            h = hrec(c)
            h["ats"] = c.get("ats")
            try:
                got = f.result()
                if got is None:
                    skipped_budget += 1
                    continue
                results.extend(got)
                listed[c["board"]] = (c.get("ats"), got[0].company if got else c["name"], {p.uid for p in got})
                h.update(ok=True, matched_titles=len(got), last_ok=now_iso(), failures=0, error="",
                         last_attempt=now_iso())
            except Exception as e:
                if c.get("universe"):
                    uerrors += 1
                else:
                    errors += 1
                    log(f"  ! {c['name']}: {str(e)[:160]}")
                h.update(ok=False, error=str(e)[:200], failures=int(h.get("failures", 0)) + 1,
                         last_attempt=now_iso())

    # job boards and aggregators: catch employers no career-site feed covers, and learn
    # new career sites from their links
    source_counts, links = {}, []
    if not a.no_boards and not a.only and not a.validate:
        covered = {norm_company(c["name"]) for c in companies + uni} | {norm_company(n) for n in learned_names.values()}
        extra = []
        try:
            raw_counts: dict = {}
            board = sweep(cfg, ctx, log, links=links, counts=raw_counts) if time.time() < deadline + 300 else []
            source_counts.update({f"board-{k} (raw)": v for k, v in raw_counts.items()})
            extra += board
        except Exception as e:  # never let the optional sweep sink the run
            log(f"boards: failed ({e})")
        agg, agg_counts = aggregators.collect(cfg, ctx, log)
        source_counts.update(agg_counts)
        extra += agg
        for p in extra:
            e = try_parse(p.url)
            if e:
                e["name"] = p.company
                links.append(e)
        source_counts["senior titles from boards/aggregators"] = len(extra)
        # roles at employers whose own site we read are redundant (and less reliable)
        results.extend(p for p in extra if norm_company(p.company) not in covered)
        log(f"boards/aggregators: {json.dumps(source_counts)}; employer sites found: {len(links)}")

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
    # rule changes apply retroactively: drop listed roles the current rules reject
    refiltered = 0
    for uid, r in list(store.roles.items()):
        if not rules.title_ok(r.get("title", "")) or norm_company(r["company"]) in \
                {norm_company(x) for x in rules.excluded_companies}:
            store._drop(uid)
            seen[uid] = {"first": date.today().isoformat(), "pass": False}
            refiltered += 1
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
    for board_id, (ats, company, uids) in listed.items():
        to_check += store.mark_missing(company, uids, full_listing=ats in FULL_LISTING, board=board_id)
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
        "closed_after_check": closed_checked, "removed_by_rule_change": refiltered, "dropped": dropped,
        "open_roles": len(open_roles), "roles_in_latest": len(latest),
        "universe_boards": len(uni), "universe_polled_ok": sum(1 for c in uni if hu.get(c["board"], {}).get("ok")
                                                               and _hours_since(hu[c["board"]].get("last_attempt")) < 1),
        "universe_errors": uerrors, "names_learned": len(learned_names),
        "employer_sites_found_on_boards": len(links), "sources": source_counts,
        "companies_with_open_roles": len({r["company"] for r in open_roles}),
    }
    log(json.dumps(summary, indent=2))

    if a.dry_run:
        for d in sorted(latest, key=lambda r: -r["score"])[:40]:
            log(f"{d['score']:3d}  {d['company']:<28} {d['title'][:70]:<70} {d['location'][:30]}"
                f"  {('$' + format(d['pay_max'], ',')) if d.get('pay_max') else ''}")
        if a.report:
            write_report(Path(a.report), summary, results, store, learned_names, links, uni, hu)
        return 0

    universe.save_names(DATA, learned_names)
    new_sites = universe.add_auto_boards(DATA, links)
    summary["new_employer_sites_added"] = new_sites

    store.save()
    write_atomic(DATA / "latest.json", dump_lines({"updated": now_iso(), "roles": latest}))
    readme.write_all(ROOT, list(store.roles.values()), len(companies) + len(uni), lambda p, t: write_atomic(p, t))
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


def write_report(path: Path, summary, results, store, learned, links, uni, hu):
    """Dry-run test report: what each source and the universe would contribute."""
    from collections import Counter
    srcs = Counter(p.source for p in results)
    uni_ids = {c["board"] for c in uni}
    new_uni = [r for r in store.open_roles() if (r.get("extra") or {}).get("board") in uni_ids]
    lines = ["# Collector test report (dry run: nothing saved)", "", "```",
             json.dumps({k: v for k, v in summary.items() if k != "dropped"}, indent=1), "```", "",
             "## Senior titles seen, by source", ""] + [f"- {k}: {v}" for k, v in srcs.most_common()]
    ok = [c for c in uni if hu.get(c["board"], {}).get("ok")]
    bad = [c for c in uni if c["board"] in hu and not hu[c["board"]].get("ok")]
    lines += ["", f"## Universe boards: {len(ok)} answered, {len(bad)} failed", ""]
    errs = Counter(str(hu[c["board"]].get("error", ""))[:60] for c in bad)
    lines += [f"- {n} × {e}" for e, n in errs.most_common(8)]
    lines += ["", "## Names learned (sample)", ""] + [f"- {b} → {n}" for b, n in list(learned.items())[:40]]
    lines += ["", f"## Roles from universe boards that pass the rules ({len(new_uni)}), sample", "",
              "| Score | Company | Role | Location | Pay |", "|---:|---|---|---|---|"]
    for r in sorted(new_uni, key=lambda r: -(r.get("score") or 0))[:60]:
        lines.append(f"| {r.get('score')} | {r['company']} | [{r['title']}]({r['url']}) | {r.get('location', '')[:40]} | "
                     f"{r.get('pay_max') or ''} |")
    other = [r for r in store.open_roles() if r["source"] in ("themuse", "adzuna") or r["source"].startswith("board-")]
    lines += ["", f"## Roles from job boards / aggregators that pass ({len(other)}), sample", "",
              "| Source | Company | Role | Location |", "|---|---|---|---|"]
    for r in other[:40]:
        lines.append(f"| {r['source']} | {r['company']} | [{r['title']}]({r['url']}) | {r.get('location', '')[:40]} |")
    lines += ["", f"## Employer career sites found in board results ({len(links)}), sample", ""]
    lines += [f"- {e.get('name')}: `{json.dumps({k: v for k, v in e.items() if k != 'name'})}`" for e in links[:30]]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")
    log(f"report written to {path}")


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
             f"- Universe (all other known career sites): {run.get('universe_boards', 0)} boards, "
             f"{run.get('universe_polled_ok', 0)} checked in the last hour, {run.get('universe_errors', 0)} errors; "
             f"{run.get('names_learned', 0)} employer names learned; "
             f"{run.get('new_employer_sites_added', 0)} new employer sites found via job boards",
             f"- Job boards and aggregators: {json.dumps(run.get('sources', {}))}",
             f"- Companies with open roles: {run.get('companies_with_open_roles', '?')}",
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
