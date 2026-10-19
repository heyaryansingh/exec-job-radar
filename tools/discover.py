"""Find each company's career-site system automatically and add it to the watchlist.

    python tools/discover.py config/discover_seed.txt            # resolve every name
    python tools/discover.py config/discover_seed.txt --limit 50

Seed file: one company per line, "Name | tier | sector" (tier and sector optional).
Lines starting with # are ignored. Names already in companies.yaml are skipped, and
names that were already tried are remembered in data/discover_state.json, so the
script can be re-run (or run in batches) safely.

For each name it tries, in order, and stops at the first board that really returns jobs:
  1. direct probes of Greenhouse, Lever, Ashby and SmartRecruiters with likely board names;
  2. the Common Crawl directory of known career sites (tools/ats_directory.py), matched
     on the company name, short name, acronym and any aliases in the seed file;
  3. the company's own careers page (www.<name>.com/careers, careers.<name>.com, ...),
     reading off whichever career-site system it links or redirects to;
  4. optionally (--web-search) a web search, which search engines often block from servers.
Matches whose address doesn't clearly belong to the company go to data/discover_review.md.
Names not found are retried on later runs, so coverage grows as the directory refreshes.
Runs on GitHub Actions (see .github/workflows/discover.yml), which has full internet.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

import yaml  # noqa: E402

import ats_directory  # noqa: E402
from add_company import parse  # noqa: E402
from collector.common import session  # noqa: E402

COMPANIES = ROOT / "config" / "companies.yaml"
STATE = ROOT / "data" / "discover_state.json"
REVIEW = ROOT / "data" / "discover_review.md"

STOP = {"the", "inc", "corp", "corporation", "company", "co", "group", "holdings", "llc", "ltd",
        "plc", "and", "of", "financial", "services", "technologies", "technology", "international",
        "global", "bank", "health", "energy", "systems", "solutions", "partners", "capital"}
# words too common to identify a company on their own
LEGAL = {"the", "inc", "corp", "corporation", "company", "co", "llc", "ltd", "plc", "holdings", "group"}
GENERIC = STOP | {"first", "american", "national", "united", "general", "new", "york", "texas", "north",
                  "south", "east", "west", "central", "federal", "life", "insurance", "trust", "mutual",
                  "investment", "investments", "management", "asset", "advisors", "markets", "data", "labs",
                  "ai", "software", "networks", "network", "communications", "media", "foods", "brands",
                  "industries", "resources", "products", "healthcare", "medical", "care", "pharmaceuticals",
                  "sciences", "bio", "motors", "airlines", "electric", "power", "gas", "oil", "chemical",
                  "realty", "properties", "entertainment", "interactive", "digital", "cloud", "security"}
ATS_URL = re.compile(
    r"https?://[^\s\"'<>]*(myworkdayjobs\.com|myworkdaysite\.com|greenhouse\.io|jobs\.lever\.co|"
    r"jobs\.ashbyhq\.com|smartrecruiters\.com|oraclecloud\.com/hcmUI)[^\s\"'<>]*", re.I)


def norm_tokens(name: str) -> list[str]:
    toks = re.findall(r"[a-z0-9]+", name.lower().replace("&", " and "))
    return [t for t in toks if t not in STOP]


def slug_candidates(name: str) -> list[str]:
    """Likely board names, longest/most specific first; never shorter than 4 characters."""
    plain = re.findall(r"[a-z0-9]+", name.lower().replace("&", " "))
    anded = re.findall(r"[a-z0-9]+", name.lower().replace("&", " and "))
    core = norm_tokens(name)
    c = ["".join(plain), "".join(anded), "-".join(plain)]
    if len(core) >= 2:
        c += ["".join(core), "-".join(core)]
    if len(plain) >= 3 and plain[1] not in STOP and plain[0] not in STOP:
        c.append("".join(plain[:2]))
    if len(plain) == 2 and len(plain[0]) >= 5:
        c.append(plain[0])
    seen, out = set(), []
    for x in c:
        if x and len(x.replace("-", "")) >= 4 and x not in seen:
            seen.add(x)
            out.append(x)
    return out


def plausible(name: str, entry: dict) -> bool:
    """Does the board address look like it belongs to this company?"""
    keys = [compact(k) for k in board_keys(entry) if k]
    toks = [t for t in re.findall(r"[a-z0-9]+", name.lower()) if t not in GENERIC and t not in LEGAL]
    if any(len(t) >= 3 and any(t in k for k in keys) for t in toks):
        return True
    acronym = "".join(t[0] for t in re.findall(r"[a-z0-9]+", name.lower()) if t not in ("of", "and", "the"))
    return len(acronym) >= 2 and any(k.startswith(acronym) for k in keys)


def count_jobs(s, e: dict) -> int:
    """Cheap liveness check; returns number of jobs seen on the first page."""
    ats = e["ats"]
    if ats == "greenhouse":
        r = s.get(f"https://boards-api.greenhouse.io/v1/boards/{e['slug']}/jobs", timeout=20)
        return len(r.json().get("jobs", [])) if r.ok else -1
    if ats == "lever":
        r = s.get(f"https://api.lever.co/v0/postings/{e['slug']}", params={"mode": "json", "limit": 5}, timeout=20)
        return len(r.json()) if r.ok and isinstance(r.json(), list) else -1
    if ats == "ashby":
        r = s.get(f"https://api.ashbyhq.com/posting-api/job-board/{e['slug']}", timeout=20)
        return len(r.json().get("jobs", [])) if r.ok else -1
    if ats == "smartrecruiters":
        r = s.get(f"https://api.smartrecruiters.com/v1/companies/{e['slug']}/postings", params={"limit": 5}, timeout=20)
        return int(r.json().get("totalFound", 0)) if r.ok else -1
    if ats == "workday":
        tenant = e.get("tenant") or e["host"].split(".")[0]
        r = s.post(f"https://{e['host']}/wday/cxs/{tenant}/{e['site']}/jobs",
                   json={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": ""}, timeout=20)
        return int(r.json().get("total", 0)) if r.ok else -1
    if ats == "oracle":
        r = s.get(f"https://{e['host']}/hcmRestApi/resources/latest/recruitingCEJobRequisitions",
                  params={"onlyData": "true", "finder": f"findReqs;siteNumber={e['site']},limit=1"}, timeout=20)
        return int(((r.json().get("items") or [{}])[0]).get("TotalJobsCount", 1)) if r.ok else -1
    return -1


def names_agree(board: str, name: str, strict: bool) -> bool:
    """Does a board's own company name match ours? ("Charles River" is not "Charles Schwab")."""
    if not board:
        return not strict  # no name to compare: only trust exact full-name slugs
    b = compact(re.sub(r"\b(inc|corp|corporation|llc|ltd|plc|careers|jobs)\b", "", board.lower()))
    n = compact(" ".join(w for w in re.findall(r"[a-z0-9]+", name.lower()) if w not in LEGAL))
    if not b or not n:
        return False
    if b == n:
        return True
    # The board's name may add words ("Cheniere Energy, Inc." for "Cheniere Energy"), but a
    # board name that is only a fragment of ours ("Charles" for Charles Schwab) is not proof.
    return len(n) >= 5 and b.startswith(n)


def probe_direct(s, name: str):
    full = {re.sub(r"[^a-z0-9-]", "", x) for x in (
        "".join(re.findall(r"[a-z0-9]+", name.lower().replace("&", " "))),
        "".join(re.findall(r"[a-z0-9]+", name.lower().replace("&", " and "))),
        "-".join(re.findall(r"[a-z0-9]+", name.lower().replace("&", " "))))}
    for slug in slug_candidates(name):
        # shortened guesses ("morgan") only on Greenhouse, whose boards report their
        # company name so a collision can be rejected below
        for ats in (("greenhouse", "lever", "ashby") if slug in full else ("greenhouse",)):
            e = {"ats": ats, "slug": slug}
            try:
                if count_jobs(s, e) > 0:
                    if ats == "greenhouse":  # boards report their company name; reject collisions
                        r = s.get(f"https://boards-api.greenhouse.io/v1/boards/{slug}", timeout=20)
                        board = (r.json().get("name") or "") if r.ok else ""
                        if not names_agree(board, name, strict=slug not in full):
                            continue
                    return e
            except Exception:
                pass
    # SmartRecruiters slugs are usually the CamelCase company name
    for slug in {re.sub(r"[^A-Za-z0-9]", "", name), re.sub(r"[^A-Za-z0-9]", "", name.title())}:
        e = {"ats": "smartrecruiters", "slug": slug}
        try:
            if count_jobs(s, e) > 0:
                return e
        except Exception:
            pass
    return None


def compact(x: str) -> str:
    return re.sub(r"[^a-z0-9]", "", x.lower().replace("&", ""))


def name_keys(name: str, aliases: list[str]) -> dict:
    """Ways a board might be named for this company, strongest first."""
    words = re.findall(r"[a-z0-9]+", name.lower().replace("&", " "))
    core = [w for w in words if w not in STOP]
    # only legal suffixes are dropped for a strong key; "Cadence Bank" must not become "cadence"
    legal = [w for w in words if w not in LEGAL]
    strong = {compact(name), compact(name.replace("&", "and")), "".join(legal)}
    strong |= {compact(a) for a in aliases}
    distinctive = {w for w in core if len(w) >= 5 and w not in GENERIC}
    acronym = "".join(w[0] for w in words if w not in ("of", "and", "the"))
    return {"strong": {k for k in strong if len(k) >= 3}, "words": distinctive, "all_words": words,
            "acronym": acronym if len(acronym) >= 3 else ""}


def board_keys(e: dict) -> list[str]:
    if e["ats"] in ("workday", "oracle"):
        tenant = e.get("tenant") or e["host"].split(".")[0]
        return [compact(tenant), compact(e.get("site", ""))]
    return [compact(e.get("slug", ""))]


def match_score(keys: dict, e: dict) -> int:
    """5-4 exact, 3 confident prefix, 2 plausible (review), 1 weak, 0 none."""
    bks = board_keys(e)
    main, site = bks[0], (bks[1] if len(bks) > 1 else "")
    best = 0
    for bk, weight in ((main, 1), (site, 0)):
        if not bk:
            continue
        if bk in keys["strong"]:
            best = max(best, 4 + weight)
            continue
        for k in keys["strong"]:
            if len(k) < 5:
                continue
            if bk.startswith(k):            # board name extends the company name
                best = max(best, 3 + weight)
            elif k.startswith(bk) and len(bk) >= 5:
                # board name is a shortened company name ("regions" for Regions Financial,
                # but also "cadence" for Cadence Bank vs Cadence Design). Confident only if
                # it spans 2+ words or the Workday site name repeats it.
                spans_words = sum(1 for w in keys["all_words"] if w in bk) >= 2
                echoed = bool(site) and bk is main and bk in site
                best = max(best, 3 + weight if (spans_words or echoed) else 2)
        if keys["words"] and any(w == bk or (bk.startswith(w) and len(w) >= 6) for w in keys["words"]):
            best = max(best, 2)  # one distinctive word: plausible, goes to review
        elif keys["acronym"] and bk == keys["acronym"]:
            best = max(best, 2)
        elif keys["words"] and any(w in bk for w in keys["words"] if len(w) >= 6):
            best = max(best, 1)
    return best


_DIRECTORY = None
REBUILD_DIRECTORY = False
_dir_lock = threading.Lock()


def directory_entries() -> list[dict]:
    global _DIRECTORY
    with _dir_lock:
        if _DIRECTORY is None:
            try:
                d = ats_directory.load(max_pages=0, n_crawls=2, rebuild=REBUILD_DIRECTORY)
                _DIRECTORY = [e for v in d.get("boards", {}).values() for e in v]
            except Exception as exc:
                print(f"  ! directory unavailable: {exc}", flush=True)
                _DIRECTORY = []
    return _DIRECTORY


def probe_directory(s, name: str, aliases: list[str]):
    keys = name_keys(name, aliases)
    scored = []
    for e in directory_entries():
        sc = match_score(keys, e)
        if sc >= 2:
            scored.append((sc, e.get("seen", 0), e))
    scored.sort(key=lambda t: (-t[0], -t[1]))
    for sc, _, e in scored[:6]:
        e = {k: v for k, v in e.items() if k != "seen"}
        try:
            if count_jobs(s, e) > 0:
                return e, sc >= 3
        except Exception:
            continue
    return None, False


def full_domains(name: str, aliases: list[str]) -> set[str]:
    words = re.findall(r"[a-z0-9]+", name.lower().replace("&", " "))
    legal = [w for w in words if w not in LEGAL]
    out = {x + ".com" for x in ("".join(words), "".join(legal)) if x} | {compact(a) + ".com" for a in aliases}
    if len(words) == 2 and words[1] in STOP | GENERIC and len(words[0]) >= 5:
        out.add(words[0] + ".com")  # "Cheniere Energy" -> cheniere.com
    return out


def guess_domains(name: str, aliases: list[str]) -> list[str]:
    words = re.findall(r"[a-z0-9]+", name.lower().replace("&", " "))
    core = [w for w in words if w not in STOP]
    c = ["".join(words), "".join(core), "".join(w for w in words if w not in ("the",))]
    if len(words) == 2 and words[1] in STOP | GENERIC and len(words[0]) >= 5:
        c.append(words[0])
    c += [compact(a) for a in aliases]
    out = []
    for x in c:
        if x and x + ".com" not in out:
            out.append(x + ".com")
    return out[:4]


def probe_careers_page(s, name: str, aliases: list[str]):
    for d in guess_domains(name, aliases):
        for url in (f"https://www.{d}/careers", f"https://careers.{d}", f"https://jobs.{d}",
                    f"https://www.{d}/en/careers", f"https://www.{d}/about/careers"):
            try:
                r = s.get(url, timeout=15, headers={"Accept": "text/html"}, allow_redirects=True)
            except Exception:
                continue
            if r.status_code >= 400:
                continue
            urls = [r.url] + [m.group(0) for m in ATS_URL.finditer(r.text[:400000])]
            for u in urls[:15]:
                try:
                    e = parse(u)
                except ValueError:
                    continue
                if e["ats"] == "workday" and e.get("site", "").lower() in BAD_WD_SITES:
                    continue
                try:
                    if count_jobs(s, e) > 0:
                        # The guessed domain may belong to another company with a similar name
                        # (fidelity.com for Fidelity National Financial). Confident only when the
                        # domain is the full company name and the board echoes that name.
                        ok = d in full_domains(name, aliases) and (
                            plausible(name, e) or match_score(name_keys(name, aliases), e) >= 3)
                        return e, ok
                except Exception:
                    continue
    return None, False


BAD_WD_SITES = {"job", "jobs", "wday", "login"}


def web_search_urls(s, query: str) -> list[str]:
    """DuckDuckGo's no-JavaScript results page; returns result URLs."""
    try:
        r = s.post("https://html.duckduckgo.com/html/", data={"q": query}, timeout=25,
                   headers={"Accept": "text/html"})
        if not r.ok:
            return []
    except Exception:
        return []
    urls = []
    for m in re.finditer(r'href="([^"]+)"', r.text):
        u = m.group(1)
        if "uddg=" in u:
            u = urllib.parse.unquote(urllib.parse.parse_qs(urllib.parse.urlparse(u).query).get("uddg", [""])[0])
        if ATS_URL.search(u):
            urls.append(ATS_URL.search(u).group(0))
    return urls


_search_lock = threading.Lock()


def probe_search(s, name: str):
    queries = [f'"{name}" careers myworkdayjobs', f'"{name}" jobs greenhouse OR lever OR ashbyhq OR oraclecloud']
    for q in queries:
        with _search_lock:  # one search at a time, spaced out
            urls = web_search_urls(s, q)[:8]
            time.sleep(2.5)
        for u in urls:
            try:
                e = parse(u)
            except ValueError:
                continue
            if e["ats"] == "workday" and e.get("site", "").lower() in ("job", "jobs", "wday"):
                continue
            try:
                n = count_jobs(s, e)
            except Exception:
                n = -1
            if n > 0:
                return e, plausible(name, e)
    return None, False


def identity(e: dict) -> str:
    return "|".join(str(e.get(k, "")).lower() for k in ("ats", "slug", "host", "site"))


def resolve(name: str, aliases: list[str], use_search: bool):
    """Return (entry, confident, method)."""
    s = session()
    e = probe_direct(s, name)
    if e:
        return e, True, "direct"
    for alias in aliases:
        e = probe_direct(s, alias)
        if e:
            return e, True, "direct"
    e, ok = probe_directory(s, name, aliases)
    if e:
        return e, ok, "directory"
    e, ok = probe_careers_page(s, name, aliases)
    if e:
        return e, ok, "careers page"
    if use_search:
        e, ok = probe_search(s, name)
        if e:
            return e, ok, "web search"
    return None, False, ""


def yaml_line(name: str, e: dict, tier: int, sector: str) -> str:
    fields = [f"name: {json.dumps(name)}"]
    for k, v in e.items():
        fields.append(f"{k}: {json.dumps(v)}")
    fields.append(f"tier: {tier}")
    if sector:
        fields.append(f"sector: {json.dumps(sector)}")
    return "- {" + ", ".join(fields) + "}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("seed")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--web-search", action="store_true", help="also try web search (often blocked)")
    ap.add_argument("--retry-review", action="store_true", help="re-resolve names sent to review")
    ap.add_argument("--dry-run", action="store_true",
                    help="test mode: change nothing, write a report of what would happen")
    ap.add_argument("--report", default=str(ROOT / "data" / "test_reports" / "discover.md"))
    ap.add_argument("--rebuild-directory", action="store_true")
    ap.add_argument("--workers", type=int, default=12)
    a = ap.parse_args()
    global REBUILD_DIRECTORY
    REBUILD_DIRECTORY = a.rebuild_directory

    existing = {c["name"].lower() for c in (yaml.safe_load(COMPANIES.read_text()) or [])}
    state = json.loads(STATE.read_text()) if STATE.exists() else {"tried": {}}
    tried = state["tried"]
    rows = []
    for line in Path(a.seed).read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        name = parts[0]
        tier = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 2
        sector = parts[2] if len(parts) > 2 else ""
        aliases = [x.strip() for x in parts[3].split(";")] if len(parts) > 3 and parts[3] else []
        prev = None if a.dry_run else tried.get(name)
        if name.lower() in existing and not a.dry_run:
            continue
        # skip names already resolved; names never found are retried every run
        if prev and not (a.retry_review and "review" in prev):
            continue
        rows.append((name, tier, sector, aliases))
    if a.limit:
        rows = rows[: a.limit]
    print(f"{len(rows)} companies to resolve", flush=True)
    if rows:
        directory_entries()  # build or load the directory once, up front

    known_ids = {identity(c) for c in (yaml.safe_load(COMPANIES.read_text()) or [])}
    added, review, missed = [], [], []
    report = []
    done = 0
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(resolve, name, aliases, a.web_search): (name, tier, sector)
                for name, tier, sector, aliases in rows}
        for f in as_completed(futs):
            name, tier, sector = futs[f]
            done += 1
            try:
                e, ok, how = f.result()
            except Exception as exc:
                e, ok, how = None, False, ""
                print(f"  ! {name}: {exc}", flush=True)
            if e and identity(e) in known_ids:
                tried[name] = {"duplicate_of": identity(e)}
                status = "already covered"
            elif e and ok:
                known_ids.add(identity(e))
                added.append(yaml_line(name, e, tier, sector))
                tried[name] = e
                status = f"{e['ats']} {e.get('slug') or e.get('host')} ({how})"
            elif e:
                review.append(f"- {name}: {yaml_line(name, e, tier, sector)}")
                tried[name] = {"review": e}
                status = "REVIEW " + json.dumps(e)
            else:
                missed.append(name)
                tried[name] = None
                status = "not found"
            print(f"[{done}/{len(rows)}] {name}: {status}", flush=True)
            report.append((name, status, how if e else "", json.dumps(e) if e else ""))
            if a.dry_run:
                continue
            if done % 25 == 0:  # checkpoint so a timeout loses little work
                flush(added, review, state)
                added, review = [], []
    if a.dry_run:
        write_report(Path(a.report), report)
        return
    flush(added, review, state)
    found = sum(1 for v in tried.values() if v and "review" not in v and "duplicate_of" not in v)
    print(f"\nresolved this run: {done - len(missed)}  |  not found: {len(missed)}  |  "
          f"total resolved so far: {found}")
    print("not found: " + ", ".join(sorted(missed)))


def write_report(path: Path, rows):
    from collections import Counter
    def kind(st):
        for pre, k in (("REVIEW", "review"), ("not found", "not found"), ("already", "already covered")):
            if st.startswith(pre):
                return k
        return "found"
    kinds = Counter(kind(st) for _, st, _, _ in rows)
    d = directory_entries()
    by_ats = Counter(e["ats"] for e in d)
    lines = ["# Discovery test report", "",
             f"Test run, nothing was changed. {len(rows)} names: " + ", ".join(f"{k} {v}" for k, v in kinds.items()), "",
             "Directory: " + (", ".join(f"{k} {v}" for k, v in sorted(by_ats.items())) or "EMPTY"), "",
             "| Company | Result | How | Board |", "|---|---|---|---|"]
    for name, st, how, e in sorted(rows):
        lines.append(f"| {name} | {st.replace('|', '/')[:60]} | {how} | `{e[:110]}` |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")
    print(f"report written to {path}")


def flush(added, review, state):
    if added:
        text = COMPANIES.read_text()
        if "# ---- discovered automatically" not in text:
            text += "\n# ---- discovered automatically (tools/discover.py)\n"
        COMPANIES.write_text(text + "\n".join(added) + "\n")
    if review:
        head = "" if REVIEW.exists() else ("# Possible matches to check by hand\n\nThese responded with jobs but "
                                          "the address didn't clearly match the company name. If one is right, "
                                          "copy its line into config/companies.yaml.\n\n")
        with open(REVIEW, "a") as fh:
            fh.write(head + "\n".join(review) + "\n")
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state, indent=1))


if __name__ == "__main__":
    main()
