"""Rule filter and quick score. Everything here is driven by config/search.yaml so the
same code works for any candidate: change the YAML, not the Python."""
from __future__ import annotations

import re
from datetime import date

from .common import Posting

US_STATES = {
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
    "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT",
    "VA", "WA", "WV", "WI", "WY", "DC",
}
US_WORDS = re.compile(
    r"\b(united states|usa|u\.s\.|us-|us,|, us\b|alabama|alaska|arizona|arkansas|california|"
    r"colorado|connecticut|delaware|florida|georgia|hawaii|idaho|illinois|indiana|iowa|kansas|"
    r"kentucky|louisiana|maine|maryland|massachusetts|michigan|minnesota|mississippi|missouri|"
    r"montana|nebraska|nevada|new hampshire|new jersey|new mexico|new york|north carolina|"
    r"north dakota|ohio|oklahoma|oregon|pennsylvania|rhode island|south carolina|south dakota|"
    r"tennessee|texas|utah|vermont|virginia|washington|west virginia|wisconsin|wyoming|"
    r"houston|dallas|austin|san antonio|plano|irving|chicago|boston|seattle|atlanta|charlotte|"
    r"denver|miami|phoenix|san francisco|los angeles|jersey city|columbus|wilmington|tampa|"
    r"richmond|mclean|minneapolis|nashville|raleigh|salt lake|pittsburgh|philadelphia)\b", re.I)
NON_US = re.compile(
    r"\b(india|bengaluru|bangalore|hyderabad|pune|mumbai|chennai|gurgaon|gurugram|noida|"
    r"united kingdom|\buk\b|london|glasgow|edinburgh|ireland|dublin|canada|toronto|vancouver|"
    r"montreal|mexico|brazil|são paulo|sao paulo|argentina|germany|berlin|munich|frankfurt|"
    r"france|paris|netherlands|amsterdam|spain|madrid|barcelona|poland|warsaw|krakow|"
    r"switzerland|zurich|singapore|hong kong|japan|tokyo|china|shanghai|beijing|australia|"
    r"sydney|melbourne|philippines|manila|israel|tel aviv|uae|dubai|south africa|"
    r"luxembourg|belgium|brussels|italy|milan|sweden|stockholm|costa rica|colombia)\b", re.I)


class Rules:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        lv = cfg["levels"]
        self.level_pats = [(re.compile(x["pattern"], re.I), int(x.get("weight", 20)))
                           for x in lv["include"]]
        self.level_excl = [re.compile(p, re.I) for p in lv.get("exclude", [])]
        dm = cfg["domain"]
        self.title_kw = [re.compile(rf"\b{re.escape(k)}\b", re.I) if k.isalnum() else
                         re.compile(re.escape(k), re.I) for k in dm["title_keywords"]]
        self.desc_kw = [re.compile(rf"\b{re.escape(k)}\b", re.I) for k in dm["description_keywords"]]
        self.desc_min = int(dm.get("description_min_hits", 4))
        self.title_excl = [re.compile(rf"\b{re.escape(k)}\b", re.I) for k in dm.get("exclude_title", [])]
        pay = cfg.get("pay") or {}
        self.pay_min = int(pay.get("min_annual", 0))
        self.drop_unknown_pay = bool(pay.get("drop_if_unknown", False))
        loc = cfg.get("location") or {}
        self.allow_remote = bool(loc.get("allow_remote", True))
        self.us_only = bool(loc.get("us_only", True))
        self.allowed_places = [p.lower() for p in loc.get("allowed_places", [])]  # if set, restrict
        self.preferred = [p.lower() for p in loc.get("preferred", [])]
        self.max_age = int(cfg.get("max_age_days", 21))
        self.excluded_companies = {c.lower() for c in cfg.get("excluded_companies", [])}
        self.level_queries = cfg.get("level_queries") or ["Director", "Vice President", "Head of",
                                                          "Chief", "Executive Director"]

    # -- cheap title test used by adapters before fetching details
    def level_weight(self, title: str) -> int:
        if any(p.search(title) for p in self.level_excl):
            return 0
        return max((w for p, w in self.level_pats if p.search(title)), default=0)

    def title_ok(self, title: str) -> bool:
        if not title or self.level_weight(title) == 0:
            return False
        return not any(p.search(title) for p in self.title_excl)

    # -- full evaluation
    def evaluate(self, p: Posting) -> tuple[bool, str, int]:
        """Return (passed, reason_if_dropped, quick_score)."""
        if p.company.lower() in self.excluded_companies:
            return False, "excluded company", 0
        lw = self.level_weight(p.title)
        if lw == 0 or not self.title_ok(p.title):
            return False, "level/title", 0

        title_hits = sum(1 for k in self.title_kw if k.search(p.title))
        desc_hits = sum(1 for k in self.desc_kw if k.search(p.description)) if p.description else 0
        if title_hits == 0 and desc_hits < self.desc_min:
            # No description fetched (e.g. detail call failed): let a generic exec title through
            # only if the title itself says technology.
            return False, "domain", 0

        if p.pay_max is not None and p.pay_max < self.pay_min:
            return False, f"pay max {p.pay_max}", 0
        if p.pay_max is None and self.drop_unknown_pay:
            return False, "pay unknown", 0

        loc = (p.location or "").lower()
        remote = p.remote or "remote" in loc
        if self.us_only and loc and NON_US.search(loc) and not US_WORDS.search(loc):
            return False, "non-US location", 0
        if self.allowed_places and not (remote and self.allow_remote):
            if loc and not any(a in loc for a in self.allowed_places):
                return False, "location", 0

        age = None
        if p.posted_at:
            try:
                age = (date.today() - date.fromisoformat(p.posted_at[:10])).days
            except ValueError:
                age = None
        if age is not None and age > self.max_age:
            return False, "too old", 0

        # ---- quick score (0-100); Claude does the real ranking later
        score = lw                                   # 15-35 by seniority
        score += min(25, title_hits * 10 + desc_hits * 2)  # domain fit
        score += {1: 15, 2: 8, 3: 3}.get(p.tier, 3)  # company tier
        if p.pay_max:
            score += 10 if p.pay_max >= 300_000 else 6 if p.pay_max >= self.pay_min else 0
        if remote or any(pref in loc for pref in self.preferred):
            score += 8
        if age is not None:
            score += 7 if age <= 1 else 4 if age <= 3 else 1 if age <= 7 else 0
        return True, "", min(100, score)
