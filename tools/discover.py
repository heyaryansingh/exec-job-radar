"""Find each company's career-site system automatically and add it to the watchlist.

    python tools/discover.py config/discover_seed.txt            # resolve every name
    python tools/discover.py config/discover_seed.txt --limit 50

Seed file: one company per line, "Name | tier | sector" (tier and sector optional).
Lines starting with # are ignored. Names already in companies.yaml are skipped, and
names that were already tried are remembered in data/discover_state.json, so the
script can be re-run (or run in batches) safely.

For each name it:
  1. probes Greenhouse, Lever, Ashby and SmartRecruiters directly with likely board
     names (exact API answers, no guessing);
  2. otherwise searches the web for the company's career site and parses any Workday,
     Greenhouse, Lever, Ashby, SmartRecruiters or Oracle URL it finds;
  3. accepts a result only if the board actually responds with jobs and its address
     plausibly belongs to that company. Doubtful matches go to
     data/discover_review.md instead of the watchlist.
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

from add_company import parse  # noqa: E402
from collector.common import session  # noqa: E402

COMPANIES = ROOT / "config" / "companies.yaml"
STATE = ROOT / "data" / "discover_state.json"
REVIEW = ROOT / "data" / "discover_review.md"

STOP = {"the", "inc", "corp", "corporation", "company", "co", "group", "holdings", "llc", "ltd",
        "plc", "and", "of", "financial", "services", "technologies", "technology", "international",
        "global", "bank", "health", "energy", "systems", "solutions", "partners", "capital"}
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
    blob = " ".join(str(entry.get(k, "")) for k in ("slug", "host", "tenant", "site")).lower()
    blob_compact = re.sub(r"[^a-z0-9]", "", blob)
    toks = norm_tokens(name) or re.findall(r"[a-z0-9]+", name.lower())
    if any(len(t) >= 3 and t in blob_compact for t in toks):
        return True
    acronym = "".join(t[0] for t in re.findall(r"[a-z0-9]+", name.lower()) if t not in ("of", "and", "the"))
    return len(acronym) >= 2 and acronym in blob_compact


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
                        if board and not set(norm_tokens(board)) & set(norm_tokens(name)):
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


def resolve(name: str, use_search: bool):
    s = session()
    e = probe_direct(s, name)
    if e:
        return e, True
    if use_search:
        return probe_search(s, name)
    return None, False


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
    ap.add_argument("--no-search", action="store_true", help="direct API probes only")
    ap.add_argument("--workers", type=int, default=12)
    a = ap.parse_args()

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
        if name.lower() in existing or name in tried:
            continue
        rows.append((name, tier, sector))
    if a.limit:
        rows = rows[: a.limit]
    print(f"{len(rows)} companies to resolve", flush=True)

    known_ids = {identity(c) for c in (yaml.safe_load(COMPANIES.read_text()) or [])}
    added, review, missed = [], [], []
    done = 0
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(resolve, name, not a.no_search): (name, tier, sector) for name, tier, sector in rows}
        for f in as_completed(futs):
            name, tier, sector = futs[f]
            done += 1
            try:
                e, ok = f.result()
            except Exception as exc:
                e, ok = None, False
                print(f"  ! {name}: {exc}", flush=True)
            if e and identity(e) in known_ids:
                tried[name] = {"duplicate_of": identity(e)}
                status = "already covered"
            elif e and ok:
                known_ids.add(identity(e))
                added.append(yaml_line(name, e, tier, sector))
                tried[name] = e
                status = f"{e['ats']} {e.get('slug') or e.get('host')}"
            elif e:
                review.append(f"- {name}: {yaml_line(name, e, tier, sector)}")
                tried[name] = {"review": e}
                status = "REVIEW " + json.dumps(e)
            else:
                missed.append(name)
                tried[name] = None
                status = "not found"
            print(f"[{done}/{len(rows)}] {name}: {status}", flush=True)
            if done % 25 == 0:  # checkpoint so a timeout loses little work
                flush(added, review, state)
                added, review = [], []
    flush(added, review, state)
    print(f"\nnot found ({len(missed)}): " + ", ".join(missed))


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
