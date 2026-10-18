"""Shared helpers: HTTP session, HTML to text, pay parsing, the normalized Posting record."""
from __future__ import annotations

import html
import re
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional

import requests

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/129.0 Safari/537.36"
)


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json"})
    return s


def get_json(s: requests.Session, url: str, *, params=None, method="GET", body=None,
             tries: int = 3, timeout: int = 25):
    """GET/POST with small retry/backoff. Raises on final failure."""
    last = None
    for i in range(tries):
        try:
            if method == "POST":
                r = s.post(url, json=body, params=params, timeout=timeout,
                           headers={"Content-Type": "application/json"})
            else:
                r = s.get(url, params=params, timeout=timeout)
            if r.status_code == 429 or r.status_code >= 500:
                last = RuntimeError(f"HTTP {r.status_code} for {url}")
                time.sleep(2 * (i + 1))
                continue
            r.raise_for_status()
            return r.json()
        except (requests.RequestException, ValueError) as e:  # ValueError: bad JSON
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(str(last))


_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"[ \t\r\f\v]+")
_NL = re.compile(r"\n{3,}")


def html_to_text(s: Optional[str]) -> str:
    if not s:
        return ""
    s = html.unescape(s)  # Greenhouse double-escapes
    s = re.sub(r"(?i)<\s*(br|/p|/div|/li|/h\d|/tr)\s*/?>", "\n", s)
    s = re.sub(r"(?i)<\s*li[^>]*>", "\n- ", s)
    s = _TAG.sub(" ", s)
    s = html.unescape(s)
    s = _WS.sub(" ", s)
    s = "\n".join(line.strip() for line in s.split("\n"))
    s = re.sub(r"\n\s*\n(- )", r"\n\1", s)  # keep list items on consecutive lines
    return _NL.sub("\n\n", s).strip()


# ---------------------------------------------------------------- pay parsing
_MONEY = r"\$\s?(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)\s*([kKmM])?"
_RANGE = re.compile(_MONEY + r"\s*(?:-|–|—|to)\s*" + _MONEY)
_SINGLE = re.compile(_MONEY)


def _amt(num: str, suffix: Optional[str]) -> float:
    v = float(num.replace(",", ""))
    if suffix and suffix.lower() == "k":
        v *= 1_000
    elif suffix and suffix.lower() == "m":
        v *= 1_000_000
    return v


def _annualize(v: float) -> float:
    # Hourly rates appear as $60-$95; treat anything < 1000 as hourly.
    return v * 2080 if v < 1000 else v


def parse_pay(text: str) -> tuple[Optional[int], Optional[int], str]:
    """Return (min, max, snippet) in annual USD from free text, or (None, None, '')."""
    if not text:
        return None, None, ""
    best = None
    for m in _RANGE.finditer(text):
        lo = _annualize(_amt(m.group(1), m.group(2)))
        hi = _annualize(_amt(m.group(3), m.group(4)))
        if lo > hi:
            lo, hi = hi, lo
        if hi < 30_000 or hi > 5_000_000:  # not a salary (e.g. "$5 billion")
            continue
        if best is None or hi > best[1]:
            start = max(0, m.start() - 60)
            best = (int(lo), int(hi), text[start:m.end() + 20].replace("\n", " ").strip())
    if best:
        return best
    return None, None, ""


# ---------------------------------------------------------------- record
@dataclass
class Posting:
    source: str            # ats name, e.g. "workday"
    company: str
    job_id: str            # id within the source
    title: str
    url: str               # public posting page (where a human applies)
    location: str = ""
    remote: bool = False
    posted_at: Optional[str] = None   # ISO date if known
    description: str = ""
    pay_min: Optional[int] = None
    pay_max: Optional[int] = None
    pay_text: str = ""
    tier: int = 2
    sector: str = ""
    extra: dict = field(default_factory=dict)

    @property
    def uid(self) -> str:
        return f"{self.source}:{self.company.lower()}:{self.job_id}"

    def fill_pay_from_text(self):
        if self.pay_max is None:
            lo, hi, snip = parse_pay(self.description)
            if hi:
                self.pay_min, self.pay_max, self.pay_text = lo, hi, snip

    def to_dict(self) -> dict:
        d = asdict(self)
        d["uid"] = self.uid
        return d


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def iso_from_ms(ms) -> Optional[str]:
    try:
        return datetime.fromtimestamp(int(ms) / 1000, tz=timezone.utc).date().isoformat()
    except Exception:
        return None
