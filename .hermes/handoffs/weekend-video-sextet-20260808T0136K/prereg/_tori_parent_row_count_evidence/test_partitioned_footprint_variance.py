#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import tempfile
import urllib.parse
from decimal import Decimal, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORCH = ROOT / "run_partitioned_footprint_variance.py"
WORKER = ROOT / "run_footprint_variance_partition.py"
ORDINARY = ROOT / "run_aggregate_tap.py"
GLOBAL_QUERY = ROOT / "footprint_variance_20260813/query.adql"
SCOPE = ROOT / "footprint_variance_partitioned_20260813"
EXPECTED_COLUMNS = ["n_cut6_dered", "sum_cos_theta", "sum_cos2_theta"]
CUT6 = "POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551"
AXIS = ("-0.6769717798726208", "-0.5098465358556549", "0.5308160878610257")
FORBIDDEN = ("CHIRALITY", "HANDEDNESS", "CLOCKWISE", "COUNTERCLOCKWISE", "CW_CCW", "DIPOLE_AMPLITUDE")


def load(path: Path, name: str):
    assert path.exists(), f"missing {path}"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    ordinary = load(ORDINARY, "ordinary")
    module = load(ORCH, "partitioned_variance")
    worker_source = WORKER.read_text()
    orch_source = ORCH.read_text()

    assert module.ORDINARY_GUARD_PATH == ORDINARY
    assert module.EXPECTED_POPULATION_COUNT == 832393
    assert module.START == 1 and module.STOP == 662174 and module.WIDTH == 10000
    assert module.MAX_CONCURRENT == 3
    assert module.EXPECTED_COLUMNS == EXPECTED_COLUMNS
    assert module.DEADLINE_UTC == "2026-08-13T21:00:00Z"
    assert module.DEADLINE_KST == "2026-08-14T06:00:00+09:00"
    assert module.GLOBAL_QUERY_SHA256 == hashlib.sha256(GLOBAL_QUERY.read_bytes()).hexdigest()
    assert hashlib.sha256(module.COS_EXPR.encode()).hexdigest() == module.COS_EXPR_SHA256

    ranges = module.ranges()
    assert len(ranges) == 67
    assert ranges[0] == (1, 10000)
    assert ranges[-2] == (650001, 660000)
    assert ranges[-1] == (660001, 662174)
    cursor = 1
    for lo, hi in ranges:
        assert lo == cursor and hi >= lo
        cursor = hi + 1
    assert cursor == 662175

    manifest = module.build_manifest(dry_run=True)
    assert manifest["partition_count"] == 67
    assert manifest["coverage"] == {"lo": 1, "hi": 662174}
    assert manifest["columns"] == EXPECTED_COLUMNS
    assert manifest["combination"] == "variance = sum(sum_x2)/sum(n) - (sum(sum_x)/sum(n))^2"
    assert manifest["server_pressure_backoff"] == "serial"
    assert manifest["deadline_utc"] == module.DEADLINE_UTC
    assert manifest["deadline_kst"] == module.DEADLINE_KST
    assert manifest["max_concurrent"] == 3
    assert manifest["cos_expression_sha256"] == module.COS_EXPR_SHA256
    assert manifest["global_query_sha256"] == module.GLOBAL_QUERY_SHA256
    assert manifest["orchestrator_sha256"] == hashlib.sha256(ORCH.read_bytes()).hexdigest()
    assert manifest["worker_sha256"] == hashlib.sha256(WORKER.read_bytes()).hexdigest()
    assert module.COS_EXPR in GLOBAL_QUERY.read_text()

    worker = load(WORKER, "partition_worker")
    submission_form = urllib.parse.parse_qs(worker.submission_form("SELECT 1").decode())
    assert submission_form["phase"] == ["RUN"]
    assert "PHASE" not in submission_form
    assert submission_form["QUERY"] == ["SELECT 1"]
    with tempfile.TemporaryDirectory() as temporary:
        temporary_path = Path(temporary)
        manifest_path = temporary_path / "manifest.json"
        manifest_path.write_text("{}\n")
        lifecycle_path = temporary_path / "guard_lifecycle.json"
        manifest_hash = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
        lifecycle_path.write_text(json.dumps({"exception_state": "OPEN", "manifest_sha256": manifest_hash}) + "\n")
        worker.require_open_lifecycle(manifest_path)
        lifecycle_path.write_text(json.dumps({"exception_state": "CLOSED", "manifest_sha256": manifest_hash}) + "\n")
        try:
            worker.require_open_lifecycle(manifest_path)
        except RuntimeError as exc:
            assert "not OPEN" in str(exc)
        else:
            raise AssertionError("closed exception still permits worker invocation")

    seen_hashes = set()
    for entry in manifest["entries"]:
        query = module.render_query(entry["lo"], entry["hi"])
        query_bytes = query.encode()
        assert hashlib.sha256(query_bytes).hexdigest() == entry["query_sha256"]
        assert entry["query_sha256"] not in seen_hashes
        seen_hashes.add(entry["query_sha256"])
        try:
            ordinary.validate_aggregate_only(query)
        except ValueError as exc:
            assert "sky-statistic/trigonometric construct forbidden" in str(exc)
        else:
            raise AssertionError("ordinary guard accepted variance partition")
        module.validate_exception_query(query_bytes, entry)
        assert module.projected_aliases(query) == EXPECTED_COLUMNS
        assert query.upper().count("SELECT") == 1
        assert query.upper().count("COUNT(") == 1
        assert query.upper().count("SUM(") == 2
        assert "AVG(" not in query.upper()
        assert "GROUP BY" not in query.upper()
        assert query.count(CUT6) == 1
        assert f"WHERE t.brickid BETWEEN {entry['lo']} AND {entry['hi']}" in query
        for literal in AXIS:
            assert literal in query
        for drift in ("t.ra IS NOT NULL", "t.dec IS NOT NULL", "t.ra >=", "t.dec >="):
            assert drift not in query
        for term in FORBIDDEN:
            assert term not in query.upper()

    mutated = module.render_query(1, 10000).encode().replace(b"0.15", b"0.16", 1)
    try:
        module.validate_exception_query(mutated, manifest["entries"][0])
    except ValueError as exc:
        assert "hash" in str(exc)
    else:
        raise AssertionError("mutated query accepted")

    getcontext().prec = 50
    rows = [
        {"n_cut6_dered": 2, "sum_cos_theta": Decimal("1.0"), "sum_cos2_theta": Decimal("0.58")},
        {"n_cut6_dered": 3, "sum_cos_theta": Decimal("-0.5"), "sum_cos2_theta": Decimal("1.12")},
    ]
    combined = module.combine_rows(rows, require_expected_count=False)
    expected_mean = Decimal("0.5") / Decimal(5)
    expected_var = Decimal("1.70") / Decimal(5) - expected_mean * expected_mean
    assert combined["n_cut6_dered"] == 5
    assert combined["mean_cos_theta"] == expected_mean
    assert combined["var_pop_cos_theta"] == expected_var

    for source in (worker_source, orch_source):
        for term in FORBIDDEN:
            assert term not in source.upper()
    assert "429, 502, 503, 504" in worker_source
    assert "--resume-job-url" in worker_source
    assert "require_open_lifecycle" in worker_source
    assert "fcntl.flock" in orch_source
    assert "guard_lifecycle.json" in orch_source
    assert '"CLOSED"' in orch_source and '"OPEN"' in orch_source
    assert "deadline_reached" in orch_source
    assert "partial" in orch_source.lower()
    assert "abort" in orch_source.lower()
    assert "archive_lost_attempt" in orch_source
    assert "remote_job_lost" in orch_source

    with tempfile.TemporaryDirectory() as temporary:
        run_dir = Path(temporary)
        (run_dir / "submission.json").write_text(json.dumps({
            "job_url": "https://datalab.noirlab.edu/tap/async/lostjob",
            "query_sha256": manifest["entries"][0]["query_sha256"],
            "submission_attempts": 1,
        }) + "\n")
        (run_dir / "service_pressure.json").write_text(json.dumps({"signal": "HTTP_502", "events": []}) + "\n")
        (run_dir / "worker_stderr.log").write_text("RemoteHTTP: HTTP 404 for /phase\n")
        archive = module.archive_lost_attempt(run_dir, manifest["entries"][0])
        assert archive.exists()
        assert (archive / "submission.json").exists()
        assert (archive / "service_pressure.json").exists()
        failure = json.loads((archive / "failure_record.json").read_text())
        assert failure["classification"] == "remote_job_lost"
        assert failure["replacement_scope"] == "same immutable unlanded partition only"
        assert not (run_dir / "submission.json").exists()

    with tempfile.TemporaryDirectory() as temporary:
        run_dir = Path(temporary)
        (run_dir / "submission.json").write_text("{}\n")
        (run_dir / "receipt.json").write_text("{}\n")
        (run_dir / "result.csv").write_text("n_cut6_dered,sum_cos_theta,sum_cos2_theta\n1,0,0\n")
        try:
            module.archive_lost_attempt(run_dir, manifest["entries"][0])
        except RuntimeError as exc:
            assert "landed" in str(exc)
        else:
            raise AssertionError("landed partition was archiveable")

    with tempfile.TemporaryDirectory() as temporary:
        temporary_path = Path(temporary)
        run_dir = temporary_path / "run"
        run_dir.mkdir()
        control = temporary_path / "concurrency_control.json"
        setattr(module, "CONCURRENCY_CONTROL_PATH", control)
        control.write_text(json.dumps({
            "mode": "CONCURRENT_UNTIL_NEW_PRESSURE",
            "activated_utc": "2026-08-13T16:20:00Z",
            "max_concurrent": 3,
        }) + "\n")
        test_manifest = {"entries": [{"run_dir": str(run_dir)}]}
        old_archive = run_dir / "failed_attempts" / "old"
        old_archive.mkdir(parents=True)
        (old_archive / "service_pressure.json").write_text(json.dumps({
            "events": [{"detected_utc": "2026-08-13T14:00:46Z", "signal": "HTTP_502"}],
        }) + "\n")
        assert module.pressure_detected(test_manifest) is False
        (run_dir / "service_pressure.json").write_text(json.dumps({
            "events": [{"detected_utc": "2026-08-13T16:21:00Z", "signal": "HTTP_503"}],
        }) + "\n")
        assert module.pressure_detected(test_manifest) is True
    print("partitioned_footprint_variance_contract=PASS partitions=67")


if __name__ == "__main__":
    main()
