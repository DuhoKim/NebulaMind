#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
RUN = ROOT / "footprint_variance_20260813" / "run"
QUERY_SOURCE = ROOT / "footprint_variance_20260813" / "query.adql"
RECEIPT_MD = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
ORDINARY_GUARD = ROOT / "run_aggregate_tap.py"
EXPECTED_QUERY_SHA256 = "5d4c7812331419eff0ec7dca4e40f690203cb94cc71b6309d7b8694299249ff1"
EXPECTED_COUNT = 832393
EXPECTED_COLUMNS = ["n_cut6_dered", "mean_cos_theta", "var_pop_cos_theta"]
THRESHOLD = 0.15


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    required = [
        QUERY_SOURCE,
        RUN / "query.adql",
        RUN / "submission.json",
        RUN / "job.xml",
        RUN / "result.csv",
        RUN / "receipt.json",
        RUN / "guard_lifecycle.json",
        RECEIPT_MD,
    ]
    for path in required:
        assert path.exists(), path

    query = RUN.joinpath("query.adql").read_text()
    assert sha(QUERY_SOURCE) == EXPECTED_QUERY_SHA256
    assert sha(RUN / "query.adql") == EXPECTED_QUERY_SHA256
    assert QUERY_SOURCE.read_bytes() == RUN.joinpath("query.adql").read_bytes()
    assert "WHERE t.brickid BETWEEN 1 AND 662174" in query
    assert query.count("POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551") == 1
    assert "GROUP BY" not in query.upper()
    assert not re.search(r"\b(CHIRALITY|HANDEDNESS|CLOCKWISE|COUNTERCLOCKWISE|CW_CCW|DIPOLE_AMPLITUDE)\b", query.upper())

    submission = json.loads(RUN.joinpath("submission.json").read_text())
    machine = json.loads(RUN.joinpath("receipt.json").read_text())
    lifecycle = json.loads(RUN.joinpath("guard_lifecycle.json").read_text())
    rows = list(csv.DictReader(RUN.joinpath("result.csv").read_text().splitlines()))
    assert len(rows) == 1 and list(rows[0]) == EXPECTED_COLUMNS
    assert submission["submission_attempts"] == submission["submission_limit"] == 1
    assert submission["query_sha256"] == EXPECTED_QUERY_SHA256
    assert machine["query_sha256"] == EXPECTED_QUERY_SHA256
    assert machine["result_sha256"] == sha(RUN / "result.csv")
    assert machine["job_xml_sha256"] == sha(RUN / "job.xml")
    assert machine["result_row_count"] == 1
    assert machine["result_columns"] == EXPECTED_COLUMNS
    assert machine["population_count_expected"] == EXPECTED_COUNT
    assert machine["population_count_returned"] == EXPECTED_COUNT == int(rows[0]["n_cut6_dered"])
    mean = float(rows[0]["mean_cos_theta"])
    variance = float(rows[0]["var_pop_cos_theta"])
    assert math.isfinite(mean) and -1 <= mean <= 1
    assert math.isfinite(variance) and 0 <= variance <= 1
    assert machine["mean_cos_theta"] == mean
    assert machine["var_pop_cos_theta"] == variance
    assert machine["threshold"] == THRESHOLD
    assert machine["threshold_met"] is (variance >= THRESHOLD)
    for key, expected in {
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "handedness_joined_or_referenced": False,
        "directional_outputs_beyond_authorized_moments": 0,
    }.items():
        assert machine[key] == expected, key

    assert lifecycle["exception_state"] == "CLOSED"
    assert lifecycle["submission_attempts"] == lifecycle["submission_limit"] == 1
    assert lifecycle["exception_query_sha256"] == EXPECTED_QUERY_SHA256
    assert lifecycle["ordinary_guard_verified_rejects_query_before"] is True
    assert lifecycle["ordinary_guard_verified_rejects_query_after"] is True
    assert lifecycle["ordinary_guard_unchanged"] is True
    assert lifecycle["ordinary_guard_sha256_before"] == lifecycle["ordinary_guard_sha256_after"] == sha(ORDINARY_GUARD)

    md = RECEIPT_MD.read_text()
    for literal in (
        EXPECTED_QUERY_SHA256,
        sha(RUN / "result.csv"),
        sha(RUN / "job.xml"),
        sha(RUN / "submission.json"),
        sha(RUN / "receipt.json"),
        sha(RUN / "guard_lifecycle.json"),
        submission["job_url"],
        str(EXPECTED_COUNT),
        rows[0]["mean_cos_theta"],
        rows[0]["var_pop_cos_theta"],
        "var(cos theta) >= 0.15",
        "BRICKID keyspace is not sky area",
        "sample rows exported: **0**",
        "positions exported: **0**",
        "chirality computed: **0**",
        "handedness joined or referenced: **0**",
        "exception state: **CLOSED**",
        "ordinary guard restored and verified: **YES**",
    ):
        assert literal in md, literal
    expected_word = "PASS" if variance >= THRESHOLD else "FAIL"
    assert f"**Kun BS-1 variance verdict: {expected_word}.**" in md
    if variance < THRESHOLD:
        assert "does not support the test as designed" in md
        assert "PASS" not in md.split("**Kun BS-1 variance verdict:", 1)[1].split("**", 1)[0]
    print(f"footprint_variance_receipt_verification=PASS threshold_met={variance >= THRESHOLD}")


if __name__ == "__main__":
    main()
