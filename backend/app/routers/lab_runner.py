"""NebulaMind Lab — research-run submission API (token-gated).

Accepts a run-plan from the Lab configurator, queues it to a runs directory,
and exposes status + generated artifacts. A separate worker executes the
pipeline. Intentionally has NO database dependency to keep it low-risk.
"""
import os
import json
import uuid
import datetime
from pathlib import Path

from fastapi import APIRouter, Header, HTTPException, Depends
from fastapi.responses import FileResponse
from pydantic import BaseModel, field_validator

router = APIRouter(prefix="/api/lab", tags=["lab"])

RUNS_DIR = Path(
    os.environ.get(
        "LAB_RUNS_DIR",
        "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs",
    )
)
RUNS_DIR.mkdir(parents=True, exist_ok=True)

TOPICS = {
    "simulations-vs-physics", "jwst-high-z-nebular", "cosmic-chemical-evolution",
    "main-sequence-quenching", "massive-galaxies-too-early", "custom",
}
DATA_SOURCES = {"sdss", "jwst", "tng"}
METHODS = {
    "scaling-relation-evolution", "stellar-mass-function", "mass-metallicity",
    "sf-efficiency-baryon-budget", "sim-vs-observation",
}
OUTPUTS = {"aastex-draft", "dr-review-loop"}


ENV_FILE = "/Users/duhokim/NebulaMind/NebulaMind/backend/.env"


def _lab_token() -> str:
    t = os.environ.get("LAB_RUN_TOKEN")
    if t:
        return t
    try:
        for line in open(ENV_FILE):
            if line.startswith("LAB_RUN_TOKEN="):
                return line.split("=", 1)[1].strip()
    except Exception:
        pass
    return ""


def require_lab_token(authorization: str | None = Header(None)):
    token = _lab_token()
    if not token:
        raise HTTPException(status_code=503, detail="Runner not configured")
    if authorization != f"Bearer {token}":
        raise HTTPException(status_code=401, detail="Invalid or missing run token")


class RunPlan(BaseModel):
    topic: str
    topic_source: str = "frontier-map"
    data_sources: list[str]
    method: str
    outputs: list[str] = []

    @field_validator("topic")
    @classmethod
    def _topic(cls, v):
        # allow a known key OR a free-text custom question (bounded length)
        if v in TOPICS:
            return v
        if 3 <= len(v) <= 300:
            return v.strip()
        raise ValueError("invalid topic")

    @field_validator("data_sources")
    @classmethod
    def _data(cls, v):
        v = [s for s in v if s in DATA_SOURCES]
        if not v:
            raise ValueError("at least one valid data source required")
        return v

    @field_validator("method")
    @classmethod
    def _method(cls, v):
        if v not in METHODS:
            raise ValueError("invalid method")
        return v

    @field_validator("outputs")
    @classmethod
    def _outputs(cls, v):
        return [o for o in v if o in OUTPUTS]


def _run_path(rid: str) -> Path:
    return RUNS_DIR / f"{rid}.json"


@router.post("/runs", dependencies=[Depends(require_lab_token)])
def create_run(plan: RunPlan):
    rid = uuid.uuid4().hex[:12]
    rec = {
        "id": rid,
        "spec": plan.model_dump(),
        "status": "queued",
        "created_utc": datetime.datetime.utcnow().isoformat() + "Z",
        "log": ["queued"],
        "artifacts": [],
        "result": None,
    }
    _run_path(rid).write_text(json.dumps(rec, indent=2))
    return {"run_id": rid, "status": "queued"}


@router.get("/runs")
def list_runs(limit: int = 24):
    """Public, read-only list of completed runs for the Lab studies list."""
    items = []
    for p in RUNS_DIR.glob("*.json"):
        try:
            rec = json.loads(p.read_text())
        except Exception:
            continue
        if rec.get("status") != "done":
            continue
        res = rec.get("result") or {}
        if not res.get("summary"):
            continue
        items.append({
            "id": rec.get("id"),
            "summary": res.get("summary"),
            "method": (rec.get("spec") or {}).get("method"),
            "data_sources": (rec.get("spec") or {}).get("data_sources", []),
            "figure_url": res.get("figure_url"),
            "pdf_url": res.get("pdf_url"),
            "review_url": res.get("review_url"),
            "review_verdict": res.get("review_verdict"),
            "review_cycles": res.get("review_cycles"),
            "created_utc": rec.get("created_utc"),
        })
    items.sort(key=lambda x: x.get("created_utc") or "", reverse=True)
    return {"runs": items[: max(1, min(limit, 100))]}


@router.get("/runs/{rid}")
def get_run(rid: str):
    if not rid.isalnum() or len(rid) > 32:
        raise HTTPException(status_code=400, detail="bad id")
    f = _run_path(rid)
    if not f.exists():
        raise HTTPException(status_code=404, detail="run not found")
    return json.loads(f.read_text())


@router.get("/runs/{rid}/artifact/{name}")
def get_artifact(rid: str, name: str):
    if not rid.isalnum() or "/" in name or ".." in name:
        raise HTTPException(status_code=400, detail="bad request")
    p = RUNS_DIR / rid / name
    if not p.exists() or not p.is_file():
        raise HTTPException(status_code=404, detail="artifact not found")
    return FileResponse(p)
