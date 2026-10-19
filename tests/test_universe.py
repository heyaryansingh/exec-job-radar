"""Universe: board de-duplication against the watchlist, name learning, stable ids."""
import json

from collector import run, sources, universe


def test_build_skips_watchlist_and_limits_tenant_sites(tmp_path):
    (tmp_path / "ats_directory.json").write_text(json.dumps({"boards": {
        "workday": [
            {"ats": "workday", "host": "capitalone.wd12.myworkdayjobs.com", "site": "Capital_One_Internal", "seen": 5},
            {"ats": "workday", "host": "acme.wd5.myworkdayjobs.com", "site": "Ext", "seen": 50},
            {"ats": "workday", "host": "acme.wd5.myworkdayjobs.com", "site": "Intl", "seen": 20},
            {"ats": "workday", "host": "acme.wd5.myworkdayjobs.com", "site": "Test", "seen": 1}],
        "greenhouse": [{"ats": "greenhouse", "slug": "spacex", "seen": 9},
                       {"ats": "greenhouse", "slug": "stripe", "seen": 9}]}}))
    (tmp_path / "auto_boards.json").write_text(json.dumps({"boards": [
        {"ats": "lever", "slug": "newco", "name": "NewCo Inc"}]}))
    watch = [{"name": "Capital One", "ats": "workday", "host": "capitalone.wd12.myworkdayjobs.com", "site": "Capital_One"},
             {"name": "Stripe", "ats": "greenhouse", "slug": "stripe"}]
    u = universe.build(tmp_path, watch)
    ids = {c["board"] for c in u}
    assert not any("capitalone" in i for i in ids)          # tenant already on the watchlist
    assert not any(i.endswith(":stripe") for i in ids)
    assert sum("acme" in i for i in ids) == 2 and not any(i.endswith(":test") for i in ids)
    names = {c["board"]: c["name"] for c in u}
    assert names["greenhouse:spacex"] == "Spacex" and names["lever:newco"] == "NewCo Inc"
    assert all(c["universe"] and c["tier"] == 3 for c in u)


def test_auto_boards_dedupe(tmp_path):
    e = {"ats": "greenhouse", "slug": "acme", "name": "Acme"}
    assert universe.add_auto_boards(tmp_path, [e, dict(e)]) == 1
    assert universe.add_auto_boards(tmp_path, [e]) == 0


DESC = "Cloud infrastructure AWS Azure Kubernetes SRE observability incident management. $250,000 - $320,000"


def test_end_to_end_universe_names_are_learned_and_stable(tmp_path, monkeypatch):
    data = tmp_path / "data"
    data.mkdir()
    (tmp_path / "config").mkdir()
    import shutil
    for f in ("search.yaml", "readme_header.md"):
        shutil.copy(f"config/{f}", tmp_path / "config" / f)
    (tmp_path / "config" / "companies.yaml").write_text("- {name: Stripe, ats: greenhouse, slug: stripe, tier: 1}\n")
    (data / "ats_directory.json").write_text(json.dumps({"boards": {"greenhouse": [
        {"ats": "greenhouse", "slug": "spacex", "seen": 5}, {"ats": "greenhouse", "slug": "deadboard", "seen": 1}]}}))
    calls = {"name": 0}

    def gj(s, url, **kw):
        if url.endswith("/boards/spacex"):
            calls["name"] += 1
            return {"name": "Space Exploration Technologies"}
        if "/boards/spacex/jobs/" in url:
            return {"content": DESC}
        if url.endswith("/boards/spacex/jobs"):
            return {"jobs": [{"id": 11, "title": "Vice President, Infrastructure", "absolute_url": "https://sx/11",
                              "location": {"name": "Hawthorne, CA"}}]}
        if "/boards/stripe/jobs" in url:
            return {"jobs": []}
        raise RuntimeError("404 Not Found")
    monkeypatch.setattr(sources, "get_json", gj)
    monkeypatch.setattr(universe, "get_json", gj)
    monkeypatch.setattr(run, "DATA", data)
    monkeypatch.setattr(run, "ROOT", tmp_path)
    args = ["--no-boards", "--test-new", "--workers", "2", "--config", str(tmp_path / "config/search.yaml"),
            "--companies", str(tmp_path / "config/companies.yaml")]
    run.main(args)
    run.main(args)
    roles = json.loads((data / "roles.json").read_text())["roles"]
    assert len(roles) == 1
    r = list(roles.values())[0]
    assert r["company"] == "Space Exploration Technologies" and r["extra"]["board"] == "greenhouse:spacex"
    assert calls["name"] == 1                                      # learned once, then cached
    h = json.loads((data / "health.json").read_text())
    assert h["universe"]["greenhouse:deadboard"]["ok"] is False
    assert h["last_run"]["universe_boards"] == 2
    assert "Space Exploration Technologies" in (tmp_path / "README.md").read_text()
