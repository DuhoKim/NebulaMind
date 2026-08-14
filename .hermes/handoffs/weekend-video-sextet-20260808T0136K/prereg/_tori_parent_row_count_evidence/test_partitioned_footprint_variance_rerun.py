#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import urllib.parse
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORCH = ROOT / "run_partitioned_footprint_variance_rerun.py"
WORKER = ROOT / "run_footprint_variance_partition_rerun.py"
ORDINARY = ROOT / "run_aggregate_tap.py"
SOURCE_SCOPE = ROOT / "footprint_variance_partitioned_20260813"
SOURCE_MANIFEST = SOURCE_SCOPE / "manifest.json"
SCOPE = ROOT / "footprint_variance_partitioned_rerun_20260814"
PREREG = ROOT.parent
EXPECTED_SOURCE_MANIFEST_SHA256 = "076131fff15c0338cce689b4742cd64631f855e2a04398dc2d527b0962edda93"
EXPECTED_COLUMNS = ["n_cut6_dered", "sum_cos_theta", "sum_cos2_theta"]
FORBIDDEN_QUERY_TERMS = (
    "CHIRALITY", "HANDEDNESS", "CLOCKWISE", "COUNTERCLOCKWISE", "CW_CCW",
    "DIPOLE_AMPLITUDE", " SPIN ",
)


def load(path: Path, name: str):
    assert path.exists(), f"missing new rerun implementation: {path}"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    assert sha(SOURCE_MANIFEST) == EXPECTED_SOURCE_MANIFEST_SHA256
    assert sha(PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md") == "ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e"
    assert sha(PREREG / "TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md") == "f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289"
    assert not SCOPE.exists(), "rerun state exists before contract freeze"

    ordinary = load(ORDINARY, "ordinary_guard")
    orch = load(ORCH, "variance_rerun")
    worker = load(WORKER, "variance_rerun_worker")

    assert orch.SOURCE_MANIFEST_PATH == SOURCE_MANIFEST
    assert orch.SOURCE_MANIFEST_SHA256 == EXPECTED_SOURCE_MANIFEST_SHA256
    assert orch.SCOPE == SCOPE
    assert orch.MAX_CONCURRENT == 3
    assert orch.QUEUE_STALL_SECONDS == 45 * 60
    assert orch.DEADLINE_UTC == "2026-08-14T09:00:00Z"
    assert orch.DEADLINE_KST == "2026-08-14T18:00:00+09:00"
    assert orch.EXPECTED_POPULATION_COUNT == 832393
    assert orch.EXPECTED_COLUMNS == EXPECTED_COLUMNS
    assert orch.PARTITION_ORDER == "ascending_contiguous"

    source = json.loads(SOURCE_MANIFEST.read_text())
    manifest = orch.build_manifest(dry_run=True)
    assert manifest["source_manifest_sha256"] == EXPECTED_SOURCE_MANIFEST_SHA256
    assert manifest["partition_count"] == 67
    assert manifest["coverage"] == {"lo": 1, "hi": 662174}
    assert manifest["columns"] == EXPECTED_COLUMNS
    assert manifest["queue_stall_seconds"] == 2700
    assert manifest["partial_threshold_verdict"] is None
    assert manifest["partition_order"] == "ascending_contiguous"
    assert manifest["deadline_utc"] == orch.DEADLINE_UTC
    assert manifest["deadline_kst"] == orch.DEADLINE_KST
    assert manifest["max_concurrent"] == 3
    assert len(manifest["entries"]) == len(source["entries"]) == 67

    cursor = 1
    for old, new in zip(source["entries"], manifest["entries"]):
        assert new["lo"] == old["lo"] == cursor
        assert new["hi"] == old["hi"]
        assert new["key_count"] == old["key_count"]
        assert new["query_path"] == old["query_path"]
        assert new["query_sha256"] == old["query_sha256"]
        assert Path(new["run_dir"]).parent == SCOPE / "runs"
        query_path = Path(new["query_path"])
        assert sha(query_path) == new["query_sha256"]
        query = query_path.read_text()
        assert orch.projected_aliases(query) == EXPECTED_COLUMNS
        assert query.upper().count("SELECT") == 1
        assert query.upper().count("COUNT(") == 1
        assert query.upper().count("SUM(") == 2
        assert "AVG(" not in query.upper() and "GROUP BY" not in query.upper()
        for term in FORBIDDEN_QUERY_TERMS:
            assert term not in f" {query.upper()} "
        try:
            ordinary.validate_aggregate_only(query)
        except ValueError as exc:
            assert "sky-statistic/trigonometric construct forbidden" in str(exc)
        else:
            raise AssertionError("ordinary guard accepted rerun query")
        cursor = new["hi"] + 1
    assert cursor == 662175

    assert orch.queue_stalled(1000.0, 1000.0 - 2699.0, {"a": "PENDING", "b": "QUEUED"}) is False
    assert orch.queue_stalled(1000.0, 1000.0 - 2700.0, {"a": "PENDING", "b": "QUEUED"}) is True
    assert orch.queue_stalled(1000.0, 1000.0 - 9000.0, {"a": "EXECUTING", "b": "PENDING"}) is False
    assert orch.queue_stalled(1000.0, 1000.0 - 9000.0, {}) is False

    partial = orch.partial_summary(
        manifest["entries"][:2],
        [
            {"n_cut6_dered": 2, "sum_cos_theta": Decimal("1.0"), "sum_cos2_theta": Decimal("0.58")},
            {"n_cut6_dered": 3, "sum_cos_theta": Decimal("-0.5"), "sum_cos2_theta": Decimal("1.12")},
        ],
    )
    assert partial["label"] == "PARTIAL"
    assert partial["completed_partitions"] == 2
    assert partial["coverage_is_full_footprint"] is False
    assert partial["threshold_verdict"] is None
    assert partial["mean_cos_theta"] == "0.1"
    assert partial["var_pop_cos_theta"] == "0.33"

    submission_form = urllib.parse.parse_qs(worker.submission_form("SELECT 1").decode())
    assert submission_form["phase"] == ["RUN"]
    assert "PHASE" not in submission_form
    assert "QUERY" in submission_form

    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / "manifest.json"
        path.write_text("{}\n")
        lifecycle = path.parent / "guard_lifecycle.json"
        lifecycle.write_text(json.dumps({
            "exception_state": "OPEN",
            "manifest_sha256": sha(path),
        }) + "\n")
        worker.require_open_lifecycle(path)
        lifecycle.write_text(json.dumps({
            "exception_state": "CLOSED",
            "manifest_sha256": sha(path),
        }) + "\n")
        try:
            worker.require_open_lifecycle(path)
        except RuntimeError as exc:
            assert "not OPEN" in str(exc)
        else:
            raise AssertionError("closed lifecycle accepted worker")

    worker_source = WORKER.read_text()
    orch_source = ORCH.read_text()
    assert "atomic_json(poll_history_path" in worker_source
    assert "queue_stalled_45m" in orch_source
    assert "ordinary_guard_verified_rejects_query_after" in orch_source
    assert "partial_threshold_verdict" in orch_source
    assert "429, 502, 503, 504" in worker_source
    assert "fcntl.flock" in orch_source
    print("partitioned_variance_rerun_contract=PASS partitions=67 queue_stall_seconds=2700")


if __name__ == "__main__":
    main()
