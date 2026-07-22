"""G3 backend-runner revive — focused smoke (BACKEND_RUNNER_G3_APPROVAL_PACKET.md §7).

Discipline baked into this file:
- LAB_RUNS_DIR / LAB_RUN_TOKEN are preset BEFORE the router import, so the
  module-level RUNS_DIR mkdir lands in a worktree-local temp dir and the token
  fallback short-circuits on the env var (no .env file is ever opened).
- The router is mounted on a minimal fresh FastAPI app; app.main is never
  imported (the main.py wiring is verified textually), so the app DB/startup
  is never touched.
- POST /api/lab/runs is exercised only for auth-rejection paths; no authorized
  POST, no run creation, no worker spawn, no network.
- The worker module is imported by path with its save() patched to a no-op
  before any function under test runs, so no record write can escape the
  worktree temp dir.
"""
import importlib.util
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # deterministic import-purity checks, env-independent

_HERE = Path(__file__).resolve()
_BACKEND = _HERE.parents[1]
_WORKTREE = _HERE.parents[2]
_TMP_RUNS = _WORKTREE / ".tmp-lab-runs"
_PRIMARY = "/Users/duhokim/NebulaMind/NebulaMind"

os.environ.setdefault("LAB_RUNS_DIR", str(_TMP_RUNS))
os.environ.setdefault("LAB_RUN_TOKEN", "g3-revive-test-token")
assert os.environ["LAB_RUNS_DIR"] == str(_TMP_RUNS)

if str(_BACKEND) not in sys.path:
    sys.path.insert(0, str(_BACKEND))

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.routers import lab_runner

app = FastAPI()
app.include_router(lab_runner.router)
client = TestClient(app)


def _clear():
    for p in _TMP_RUNS.glob("*.json"):
        p.unlink()


def _seed(rid, **over):
    rec = {
        "id": rid,
        "spec": {
            "topic": "custom",
            "topic_source": "frontier-map",
            "data_sources": ["sdss"],
            "method": "mass-metallicity",
            "outputs": ["aastex-draft"],
        },
        "status": "done",
        "created_utc": over.pop("created_utc", "2026-07-22T00:00:00Z"),
        "log": ["queued"],
        "artifacts": [],
        "result": {"summary": "test summary"},
    }
    rec.update(over)
    (_TMP_RUNS / f"{rid}.json").write_text(json.dumps(rec, indent=2))
    return rec


def _load_worker():
    spec = importlib.util.spec_from_file_location(
        "g3_worker_under_test", _WORKTREE / "tools" / "lab_runner_worker.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.save = lambda rec: None  # hard guard: no record write can leave the test
    return mod


# ---------- isolation / wiring ----------

def test_runs_dir_is_isolated_to_worktree_temp():
    assert lab_runner.RUNS_DIR == _TMP_RUNS
    assert _TMP_RUNS.is_dir()
    assert not str(lab_runner.RUNS_DIR).startswith(_PRIMARY)
    assert not lab_runner.ENV_FILE.startswith(_PRIMARY)  # primary .env unreachable


def test_main_py_wiring_is_present_textually():
    text = (_BACKEND / "app" / "main.py").read_text()
    assert "from app.routers import lab_runner" in text
    assert "app.include_router(lab_runner.router)" in text


# ---------- GET /api/lab/runs ----------

def test_list_empty_dir_returns_empty_runs():
    _clear()
    r = client.get("/api/lab/runs")
    assert r.status_code == 200
    assert r.json() == {"runs": []}


def test_list_filters_to_done_with_summary_and_sorts_desc():
    _clear()
    _seed("aaadone000001", created_utc="2026-07-22T02:00:00Z")
    _seed("bbbdone000002", created_utc="2026-07-22T03:00:00Z")
    _seed("cccqueued0003", status="queued", created_utc="2026-07-22T04:00:00Z")
    _seed("dddnosum00004", result={"summary": ""}, created_utc="2026-07-22T05:00:00Z")
    r = client.get("/api/lab/runs")
    assert r.status_code == 200
    runs = r.json()["runs"]
    assert [x["id"] for x in runs] == ["bbbdone000002", "aaadone000001"]
    for item in runs:
        for key in ("id", "summary", "method", "data_sources", "created_utc"):
            assert key in item
        assert item["summary"] == "test summary"
        assert item["method"] == "mass-metallicity"


# ---------- GET /api/lab/runs/{rid} ----------

def test_detail_roundtrip_and_validation():
    _clear()
    seeded = _seed("eeedetail0005")
    r = client.get("/api/lab/runs/eeedetail0005")
    assert r.status_code == 200
    body = r.json()
    for k, v in seeded.items():
        assert body[k] == v
    assert client.get("/api/lab/runs/not-alnum!!").status_code == 400
    assert client.get("/api/lab/runs/" + "a" * 33).status_code == 400
    assert client.get("/api/lab/runs/fffabsent0006").status_code == 404


# ---------- POST /api/lab/runs — auth rejection only ----------

def test_post_without_or_with_wrong_bearer_is_rejected():
    plan = {"topic": "custom", "data_sources": ["sdss"], "method": "mass-metallicity"}
    before = sorted(p.name for p in _TMP_RUNS.glob("*.json"))
    r = client.post("/api/lab/runs", json=plan)
    assert r.status_code == 401
    r = client.post(
        "/api/lab/runs", json=plan, headers={"Authorization": "Bearer wrong-token"}
    )
    assert r.status_code == 401
    after = sorted(p.name for p in _TMP_RUNS.glob("*.json"))
    assert after == before  # rejected POSTs created no run records


def test_post_unconfigured_returns_503(monkeypatch):
    # Safe only because ENV_FILE is overridable: the fallback path points at a
    # nonexistent file inside the temp dir, so no real .env is ever opened.
    monkeypatch.delenv("LAB_RUN_TOKEN", raising=False)
    monkeypatch.setattr(lab_runner, "ENV_FILE", str(_TMP_RUNS / "absent.env"))
    plan = {"topic": "custom", "data_sources": ["sdss"], "method": "mass-metallicity"}
    r = client.post("/api/lab/runs", json=plan)
    assert r.status_code == 503


# ---------- worker import purity ----------

def test_worker_imports_clean_with_no_side_effects():
    before = set(_TMP_RUNS.rglob("*")) | set((_WORKTREE / "tools").rglob("*"))
    mod = _load_worker()
    after = set(_TMP_RUNS.rglob("*")) | set((_WORKTREE / "tools").rglob("*"))
    assert callable(mod.lit_context)
    assert callable(mod.process)
    assert callable(mod.sweep)
    assert after == before  # import created no files


# ---------- ACCEPTANCE (packet §6): machine-readable grounding status ----------
# A run record must expose whether fail-open literature grounding actually ran:
# grounded true only when grounding ran on >= 1 paper; false otherwise, with a
# reason. Exposed on BOTH the list items and the detail response.

def test_acceptance_grounding_status_on_list_items():
    _clear()
    _seed(
        "aaagrounded01",
        created_utc="2026-07-22T02:00:00Z",
        lit_papers=[{"bibcode": "2020ApJ...900A"}, {"bibcode": "2021MNRAS.501B"}],
        lit_refs=["[A20]"],
        lit_reflist=["[A20] Author et al. 2020, ApJ"],
    )
    _seed(
        "bbbskipped002",
        created_utc="2026-07-22T01:00:00Z",
        log=["queued", "12:00:00 lit grounding skipped: RuntimeError: ADS unavailable"],
    )
    runs = client.get("/api/lab/runs").json()["runs"]
    by_id = {x["id"]: x for x in runs}
    assert by_id["aaagrounded01"]["lit_grounded"] is True
    assert by_id["bbbskipped002"]["lit_grounded"] is False
    assert "skipped" in (by_id["bbbskipped002"]["lit_grounding"] or "")


def test_acceptance_grounding_status_on_detail():
    _clear()
    _seed(
        "aaagrounded01",
        lit_papers=[{"bibcode": "2020ApJ...900A"}],
        lit_refs=["[A20]"],
        lit_reflist=["[A20] Author et al. 2020, ApJ"],
    )
    _seed(
        "bbbskipped002",
        log=["queued", "12:00:00 lit grounding skipped: RuntimeError: ADS unavailable"],
    )
    _seed("eeenotried005")  # done, no lit fields, no skip log -> never attempted
    _seed("dddzeropap004", lit_papers=[])  # empty list is NOT grounded (>=1 rule)
    _seed(
        "cccstamped003",
        lit_grounded=False,
        lit_grounding="skipped: nm_fulltext_layer unavailable",
    )
    a = client.get("/api/lab/runs/aaagrounded01").json()
    assert a["lit_grounded"] is True
    b = client.get("/api/lab/runs/bbbskipped002").json()
    assert b["lit_grounded"] is False
    assert "skipped" in (b["lit_grounding"] or "")
    e = client.get("/api/lab/runs/eeenotried005").json()
    assert e["lit_grounded"] is False
    assert e["lit_grounding"]
    d = client.get("/api/lab/runs/dddzeropap004").json()
    assert d["lit_grounded"] is False
    c = client.get("/api/lab/runs/cccstamped003").json()
    assert c["lit_grounded"] is False
    assert c["lit_grounding"] == "skipped: nm_fulltext_layer unavailable"


def test_acceptance_worker_stamps_grounding_on_failopen_skip():
    mod = _load_worker()  # save() already patched to a no-op inside
    rec = {
        "id": "workerstamp01",
        "spec": {"topic": "custom", "method": "mass-metallicity", "data_sources": ["sdss"]},
        "result": {"summary": "test summary"},
        "log": [],
    }
    ctx = mod.lit_context(rec)  # nm_fulltext_layer absent here -> fail-open skip path
    assert ctx is None
    assert rec["lit_grounded"] is False
    assert "skipped" in rec["lit_grounding"]
