"""The role database: every matching role ever found, with its full lifecycle.

data/roles.json holds one record per distinct opening:
    uid           source:company:job_id (the posting's own identity)
    dup_key       company|title|place, used to merge the same role found two ways
    status        open | closed
    first_seen, last_seen, closed_at, posted_at
    also_at       other URLs where the same role was found (merged duplicates)
    reposted      true if it reopened under a new id after closing
    opening_no    2, 3... when one company posts several separate openings with the
                  same title in the same place (different requisitions)

Rules
- Same source, different job id  -> different openings, even with identical titles
  (big employers post one requisition per opening). Shown as "opening #2" etc.
- Different source (job board vs the company's own site), same company+title+place
  -> one role; the company-site version wins and the other URL goes to also_at.
- A role whose company+title+place matches a role closed in the last 60 days -> "reposted".
"""
from __future__ import annotations

import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

LEGAL = r"\b(inc|incorporated|corp|corporation|co|company|llc|ltd|plc|n\.?a|holdings|group|the|& co)\b"
ATS_SOURCES = {"workday", "greenhouse", "lever", "ashby", "smartrecruiters", "oracle"}
KEEP_CLOSED_DAYS = 60
STALE_OPEN_DAYS = 120


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def norm_company(name: str) -> str:
    s = (name or "").lower()
    s = re.sub(r"\s*(&|\band)\s*co\.?(?=\s|,|$)", " ", s)  # "& Co." is a legal suffix
    s = s.replace("&", " and ")
    s = re.sub(LEGAL, " ", s)
    return re.sub(r"[^a-z0-9]", "", s)


_REQ = re.compile(r"\b(req|requisition|job)\s*#?\s*[:\-]?\s*[a-z]*\d[\w\-]*\b|\(\s*[a-z]*\d{4,}[\w\-]*\s*\)|\b[a-z]{0,3}\d{5,}\b", re.I)


def norm_title(title: str) -> str:
    s = (title or "").lower()
    s = _REQ.sub(" ", s)
    s = re.sub(r"\((remote|hybrid|onsite|on-site)[^)]*\)", " ", s)
    s = s.replace("sr.", "senior").replace("sr ", "senior ").replace("vp", "vice president")
    s = s.replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def norm_place(location: str, remote: bool) -> str:
    loc = (location or "").lower()
    if not loc:
        return "remote" if remote else ""
    first = re.split(r"[;|/]| or ", loc)[0]
    city = first.split(",")[0].strip()
    city = re.sub(r"[^a-z ]", "", city).strip()
    if city in ("", "us", "usa", "united states") or "remote" in city:
        return "remote" if (remote or "remote" in loc) else "us"
    return city


def dup_key(company: str, title: str, location: str, remote: bool) -> str:
    return f"{norm_company(company)}|{norm_title(title)}|{norm_place(location, remote)}"


class Store:
    def __init__(self, path: Path):
        self.path = path
        try:
            self.roles: dict = json.loads(path.read_text()).get("roles", {})
        except Exception:
            self.roles = {}
        self._by_dup: dict = {}
        for r in self.roles.values():
            self._by_dup.setdefault(r["dup_key"], []).append(r["uid"])

    # ------------------------------------------------------------------ add
    def add(self, d: dict) -> str:
        """Add a role that passed the rules. Returns 'new', 'merged' or 'reposted'."""
        now = now_iso()
        key = dup_key(d["company"], d["title"], d.get("location", ""), d.get("remote", False))
        d = {**d, "dup_key": key, "status": "open", "first_seen": d.get("first_seen") or now,
             "last_seen": now, "also_at": [], "reposted": False}
        twins = [self.roles[u] for u in self._by_dup.get(key, []) if u in self.roles]
        open_twins = [t for t in twins if t["status"] == "open"]
        new_is_ats = d["source"] in ATS_SOURCES

        for t in open_twins:
            same_source = t["source"] == d["source"]
            if same_source and new_is_ats:
                continue  # a separate requisition with the same title: a real second opening
            # same role found another way: keep the company-site version
            if new_is_ats and t["source"] not in ATS_SOURCES:
                d["also_at"] = sorted(set(t.get("also_at", []) + [t["url"]]))
                d["first_seen"] = t["first_seen"]
                self._drop(t["uid"])
                self._put(d)
                return "merged"
            if d["url"] not in t.get("also_at", []) and d["url"] != t["url"]:
                t.setdefault("also_at", []).append(d["url"])
            t["last_seen"] = now
            return "merged"

        same_source_open = [t for t in open_twins if t["source"] == d["source"]]
        if same_source_open:
            d["opening_no"] = 1 + max(t.get("opening_no", 1) for t in same_source_open)
        if any(t["status"] == "closed" for t in twins):
            d["reposted"] = True
        self._put(d)
        return "reposted" if d["reposted"] else "new"

    def _put(self, d):
        self.roles[d["uid"]] = d
        self._by_dup.setdefault(d["dup_key"], []).append(d["uid"])

    def _drop(self, uid):
        r = self.roles.pop(uid, None)
        if r:
            self._by_dup[r["dup_key"]] = [u for u in self._by_dup.get(r["dup_key"], []) if u != uid]

    # ------------------------------------------------------------------ lifecycle
    def touch(self, uid: str):
        """Still listed. Stored as a date so an hourly run doesn't rewrite every role."""
        r = self.roles.get(uid)
        if r and r["status"] == "open":
            today = date.today().isoformat()
            if r.get("last_seen", "")[:10] != today:
                r["last_seen"] = today
            r.pop("missing", None)

    def has(self, uid: str) -> bool:
        return uid in self.roles

    def mark_missing(self, company: str, listed_uids: set, full_listing: bool, board: str = "") -> list[dict]:
        """Called for a company whose site was read successfully this run.

        full_listing=True (Greenhouse/Lever/Ashby list every job): a role absent twice in a
        row is closed. Otherwise the listing is partial (search-based), so absent roles are
        returned for a direct check instead of being closed on absence alone."""
        to_check = []
        for r in self.roles.values():
            if r["status"] != "open" or r["source"] not in ATS_SOURCES:
                continue
            rb = (r.get("extra") or {}).get("board")
            if (rb != board) if (rb and board) else (r["company"] != company):
                continue
            if r["uid"] in listed_uids:
                continue
            if full_listing:
                r["missing"] = int(r.get("missing", 0)) + 1
                if r["missing"] >= 2:
                    self.close(r["uid"], "no longer listed")
            else:
                to_check.append(r)
        return to_check

    def close(self, uid: str, why: str):
        r = self.roles.get(uid)
        if r and r["status"] == "open":
            r.update(status="closed", closed_at=now_iso(), closed_why=why)

    def expire(self, desc_days: int = 14):
        """Close job-board roles nobody can re-check after 30 days; prune old closed roles;
        close roles open for an implausibly long time (stale postings)."""
        today = date.today()
        for uid, r in list(self.roles.items()):
            first = _d(r.get("first_seen"))
            # descriptions are only needed while the daily run may still pick the role
            if r.get("description") and (r["status"] != "open" or (first and (today - first).days > desc_days)):
                r["description"] = ""
            if r["status"] == "open":
                if r["source"] not in ATS_SOURCES and first and (today - first).days > 30:
                    self.close(uid, "job-board listing aged out")
                elif first and (today - first).days > STALE_OPEN_DAYS:
                    self.close(uid, "stale (open over 4 months)")
            else:
                closed = _d(r.get("closed_at"))
                if closed and (today - closed).days > KEEP_CLOSED_DAYS:
                    self._drop(uid)

    # ------------------------------------------------------------------ views
    def open_roles(self) -> list[dict]:
        return [r for r in self.roles.values() if r["status"] == "open"]

    def save(self):
        """One role per line, sorted, so each hourly commit stores only a small diff."""
        lines = ",\n".join(f"{json.dumps(u)}:{json.dumps(self.roles[u], separators=(',', ':'), sort_keys=True)}"
                           for u in sorted(self.roles))
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text('{"updated":%s,"roles":{\n%s\n}}\n' % (json.dumps(now_iso()), lines))
        tmp.replace(self.path)


def _d(iso):
    try:
        return date.fromisoformat((iso or "")[:10])
    except ValueError:
        return None


def age_days(r: dict) -> int:
    d = _d(r.get("posted_at")) or _d(r.get("first_seen"))
    return (date.today() - d).days if d else 0


def since(iso: str, hours: float) -> bool:
    try:
        t = datetime.fromisoformat(iso)
        return datetime.now(timezone.utc) - t <= timedelta(hours=hours)
    except Exception:
        return False
