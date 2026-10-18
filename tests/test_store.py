"""Role database: de-duplication, separate openings, reposts, closures, README."""
import json
from datetime import datetime, timedelta, timezone

from collector import readme
from collector.store import Store, dup_key, norm_title


def role(uid_id, *, source="workday", company="Capital One", title="Vice President, Cloud Engineering",
         location="Plano, TX", url=None, **kw):
    return {"source": source, "company": company, "job_id": uid_id, "uid": f"{source}:{company.lower()}:{uid_id}",
            "title": title, "location": location, "remote": False, "url": url or f"https://x/{source}/{uid_id}",
            "tier": 1, "score": 80, **kw}


def test_title_normalization():
    assert norm_title("VP, Cloud Engineering (R12345)") == norm_title("Vice President - Cloud Engineering")
    assert norm_title("Sr. Director, SRE") == norm_title("Senior Director SRE")
    assert dup_key("JPMorgan Chase & Co.", "VP Cloud", "Plano, TX, United States", False) == \
        dup_key("JPMorgan Chase", "Vice President, Cloud", "Plano, Texas", False)


def test_same_role_found_two_ways_is_merged(tmp_path):
    s = Store(tmp_path / "r.json")
    assert s.add(role("ind-1", source="board-indeed", company="Capital One, N.A.",
                      title="VP Cloud Engineering")) == "new"
    assert s.add(role("R1")) == "merged"          # company-site version replaces the board copy
    rs = s.open_roles()
    assert len(rs) == 1 and rs[0]["source"] == "workday"
    assert rs[0]["also_at"] == ["https://x/board-indeed/ind-1"]
    assert s.add(role("ind-2", source="board-google")) == "merged"  # later board copy just links
    assert len(s.open_roles()) == 1


def test_separate_openings_stay_separate(tmp_path):
    s = Store(tmp_path / "r.json")
    assert s.add(role("R1")) == "new"
    assert s.add(role("R2")) == "new"                                 # same title, second requisition
    assert s.add(role("R3", location="McLean, VA")) == "new"          # same title, other city
    assert s.add(role("R4", title="Vice President, Data Engineering")) == "new"
    rs = {r["job_id"]: r for r in s.open_roles()}
    assert len(rs) == 4
    assert rs["R2"].get("opening_no") == 2 and "opening_no" not in rs["R3"]


def test_repost_and_closures(tmp_path):
    s = Store(tmp_path / "r.json")
    s.add(role("R1", source="greenhouse"))
    # absent from a full listing once: still open; twice: closed
    s.mark_missing("Capital One", set(), full_listing=True)
    assert s.open_roles()
    s.mark_missing("Capital One", set(), full_listing=True)
    assert not s.open_roles()
    assert s.add(role("R9", source="greenhouse")) == "reposted"
    # partial listings never close on absence; they hand roles back for a direct check
    s2 = Store(tmp_path / "r2.json")
    s2.add(role("W1"))
    assert [r["uid"] for r in s2.mark_missing("Capital One", set(), full_listing=False)] == ["workday:capital one:W1"]
    assert s2.open_roles()


def test_save_load_roundtrip(tmp_path):
    s = Store(tmp_path / "r.json")
    s.add(role("R1"))
    s.add(role("R2", title="Head of SRE"))
    s.save()
    text = (tmp_path / "r.json").read_text()
    assert text.count("\n") >= 3                     # one role per line
    s2 = Store(tmp_path / "r.json")
    assert len(s2.roles) == 2 and json.loads(text)["roles"]


def test_board_aging_and_pruning(tmp_path):
    s = Store(tmp_path / "r.json")
    old = (datetime.now(timezone.utc) - timedelta(days=40)).isoformat()
    s.add(role("b1", source="board-indeed", first_seen=old, description="x" * 100))
    s.expire()
    r = list(s.roles.values())[0]
    assert r["status"] == "closed" and r["description"] == ""


def test_readme_render(tmp_path):
    s = Store(tmp_path / "r.json")
    s.add(role("R1", pay_min=250000, pay_max=320000))
    s.add(role("R2"))
    s.add(role("C1", title="Chief Information Officer", company="Acme Bank", location="Houston, TX"))
    s.add(role("G1", source="greenhouse", title="Director, AI Platform", company="Stripe", location="Remote",
               remote=True))
    md = readme.render(list(s.roles.values()), "# Title", 1400, [])
    assert "**4 open roles**" in md and "New in the last 24 hours" in md
    assert "## 👑 Executive Technology Leadership" in md and "## 🧠 Data & AI" in md
    assert '<a name="data-ai"></a>' in md and "(#data-ai)" in md
    assert "[Apply](https://x/workday/R1)" in md and "$250K–$320K" in md
    assert "(req R1)" in md and "(req R2)" in md and "🆕" in md and "⭐" in md
    # every table row has the same number of columns as the header
    for line in md.splitlines():
        if line.startswith("| ") and "---" not in line:
            assert line.count("|") == 8, line
