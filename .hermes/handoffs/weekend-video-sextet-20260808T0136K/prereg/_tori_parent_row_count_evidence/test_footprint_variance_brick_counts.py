#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import importlib.util
import math
import tempfile
from pathlib import Path

from astropy.io import fits

ROOT = Path(__file__).resolve().parent
WORKER = ROOT / "run_grouped_brick_count_tap.py"
ORCHESTRATOR = ROOT / "run_footprint_variance_brick_counts.py"
RECONSTRUCTOR = ROOT / "reconstruct_footprint_variance_brick_counts.py"
ORDINARY_GUARD = ROOT / "run_aggregate_tap.py"
EXPECTED_ORDINARY_GUARD_SHA = "228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51"
EXPECTED_SOURCE_MANIFEST_SHA = "076131fff15c0338cce689b4742cd64631f855e2a04398dc2d527b0962edda93"
EXPECTED_STATIC_SHA = "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a"
CUT6 = "POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551"
BANNED_QUERY_TOKENS = (
    "sin(", "cos(", "tan(", "radians(", "degrees(", "axis", "theta", "dipole",
    "chirality", "handedness", "clockwise", "counterclockwise", " cw", "ccw", "spin",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path, name: str):
    assert path.exists(), f"missing implementation: {path}"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def must_reject(function, value, contains: str) -> None:
    try:
        function(value)
    except (ValueError, RuntimeError) as exc:
        assert contains.lower() in str(exc).lower(), str(exc)
    else:
        raise AssertionError(f"expected rejection containing {contains!r}")


def main() -> None:
    assert sha(ORDINARY_GUARD) == EXPECTED_ORDINARY_GUARD_SHA
    worker = load(WORKER, "grouped_worker")
    orchestrator = load(ORCHESTRATOR, "brick_orchestrator")
    recon = load(RECONSTRUCTOR, "brick_reconstructor")

    assert orchestrator.START == 1
    assert orchestrator.STOP == 662174
    assert orchestrator.WIDTH == 10000
    assert orchestrator.MAX_CONCURRENT == 3
    assert orchestrator.POLL_SECONDS == 15
    assert orchestrator.QUEUE_STALL_SECONDS == 1800
    assert orchestrator.DEADLINE_UTC == "2026-08-14T13:00:00Z"
    assert orchestrator.DEADLINE_KST == "2026-08-14T22:00:00+09:00"
    assert orchestrator.EXPECTED_POPULATION == 832393
    assert orchestrator.ORDINARY_GUARD_SHA256 == EXPECTED_ORDINARY_GUARD_SHA
    assert orchestrator.SOURCE_MANIFEST_SHA256 == EXPECTED_SOURCE_MANIFEST_SHA
    assert orchestrator.STATIC_PRODUCT_SHA256 == EXPECTED_STATIC_SHA

    static_product = orchestrator.STATIC_PRODUCT_PATH
    assert sha(static_product) == EXPECTED_STATIC_SHA
    with fits.open(static_product, memmap=False) as hdul:
        table = getattr(hdul[1], "data", None)
        assert table is not None
        assert len(table) == 366912
        assert {"brickid", "ra", "dec"}.issubset({name.lower() for name in table.names})
        assert len(set(map(int, table["brickid"]))) == 366912

    manifest = orchestrator.build_manifest(dry_run=True)
    entries = manifest["entries"]
    assert len(entries) == 67
    assert manifest["coverage"] == {"lo": 1, "hi": 662174}
    assert manifest["partition_count"] == 67
    assert manifest["columns"] == ["brickid", "n_cut6_dered"]
    assert manifest["ordinary_guard_state"] == "ARMED_AND_BYTE_IDENTICAL"
    assert manifest["guard_exception_opened"] is False
    assert manifest["max_concurrent"] == 3
    assert manifest["service_pressure_backoff"] == "serial"
    assert manifest["queue_stall_seconds"] == 1800
    assert manifest["stop_rule"]["first_of"] is True
    assert manifest["stop_rule"]["deadline_utc"] == orchestrator.DEADLINE_UTC

    cursor = 1
    query_hashes: set[str] = set()
    for entry in entries:
        assert entry["lo"] == cursor
        assert entry["hi"] == min(cursor + 9999, 662174)
        query = orchestrator.render_query(entry["lo"], entry["hi"])
        normalized = " ".join(query.split()).lower()
        assert normalized.startswith("select t.brickid as brickid, count(*) as n_cut6_dered from ")
        assert "group by t.brickid" in normalized
        assert "order by t.brickid" in normalized
        assert query.count(CUT6) == 1
        assert f"t.brickid BETWEEN {entry['lo']} AND {entry['hi']}" in query
        assert "t.ra" not in normalized and "t.dec" not in normalized
        for token in BANNED_QUERY_TOKENS:
            assert token not in normalized, (token, entry["lo"], entry["hi"])
        worker.validate_grouped_count_query(query)
        orchestrator.validate_query(query, entry["lo"], entry["hi"])
        query_hashes.add(entry["query_sha256"])
        cursor = entry["hi"] + 1
    assert cursor == 662175
    assert len(query_hashes) == 67

    valid = orchestrator.render_query(1, 10000)
    must_reject(worker.validate_grouped_count_query, valid.replace("COUNT(*)", "COUNT(*) + COS(t.ra)"), "trigonometric")
    must_reject(worker.validate_grouped_count_query, valid.replace("COUNT(*) AS n_cut6_dered", "COUNT(*) AS n_cut6_dered, t.ra AS ra"), "projection")
    must_reject(worker.validate_grouped_count_query, valid.replace("GROUP BY t.brickid", "GROUP BY t.type"), "group")
    must_reject(worker.validate_grouped_count_query, valid.replace("ORDER BY t.brickid", "ORDER BY t.ra"), "order")
    must_reject(worker.validate_grouped_count_query, valid.replace("t.brickid AS brickid", "t.objid AS brickid"), "projection")
    must_reject(worker.validate_grouped_count_query, valid.replace("COUNT(*) AS n_cut6_dered", "COUNT(*) AS n"), "projection")

    assert worker.parse_grouped_result("brickid,n_cut6_dered\n1,2\n4,3\n", 1, 10) == [(1, 2), (4, 3)]
    assert worker.parse_grouped_result("brickid,n_cut6_dered\n", 1, 10) == []
    malformed = (
        ("brickid,n_cut6_dered\n1,2\n1,3\n", "strictly increasing"),
        ("brickid,n_cut6_dered\n0,2\n", "outside"),
        ("brickid,n_cut6_dered\n1,0\n", "positive"),
        ("brickid,n_cut6_dered,ra\n1,2,4.0\n", "columns"),
        ("brickid,n_cut6_dered\n1,2.5\n", "integer"),
    )
    for text, fragment in malformed:
        try:
            worker.parse_grouped_result(text, 1, 10)
        except (ValueError, RuntimeError) as exc:
            assert fragment in str(exc).lower(), str(exc)
        else:
            raise AssertionError(f"malformed grouped result accepted: {text!r}")

    counts = {1: 2, 2: 1, 3: 1}
    centers = {1: (0.0, 0.0), 2: (180.0, 0.0), 3: (90.0, 0.0)}
    result = recon.compute_weighted_geometry(counts, centers, axis_ra_deg=0.0, axis_dec_deg=0.0)
    assert result["population"] == 4
    assert result["nonempty_bricks"] == 3
    assert math.isclose(result["mean_cos_theta_center"], 0.25, abs_tol=1e-15)
    assert math.isclose(result["mean_cos2_theta_center"], 0.75, abs_tol=1e-15)
    assert math.isclose(result["variance_cos_theta_center"], 0.6875, abs_tol=1e-15)
    assert recon.classify(0.1748) == "PASS"
    assert recon.classify(0.174799999) == "INCONCLUSIVE"
    assert recon.classify(0.15) == "INCONCLUSIVE"
    assert recon.classify(0.1376) == "INCONCLUSIVE"
    assert recon.classify(0.137599999) == "FAIL"

    with tempfile.TemporaryDirectory() as temp:
        count_path = Path(temp) / "counts.csv"
        count_path.write_text("brickid,n_cut6_dered\n1,2\n4,3\n")
        loaded = recon.load_count_csvs([count_path])
        assert loaded == {1: 2, 4: 3}

    worker_source = WORKER.read_text().lower()
    orchestrator_source = ORCHESTRATOR.read_text().lower()
    for source in (worker_source, orchestrator_source):
        assert "guard_lift" not in source
        assert "open_guard" not in source
        assert "restore_guard" not in source
        assert "guard_lifecycle" not in source
    assert orchestrator_source.index('elif phase in {"error", "aborted"}') < orchestrator_source.index(
        'elif (tap / "service_pressure.json").exists()'
    )
    assert "run_aggregate_tap.py" not in orchestrator.runner_command(entries[0])[1]
    print("footprint_variance_brick_counts_contract=PASS partitions=67 query_trig=0 guard=ARMED error_bracket=0.0124")


if __name__ == "__main__":
    main()
