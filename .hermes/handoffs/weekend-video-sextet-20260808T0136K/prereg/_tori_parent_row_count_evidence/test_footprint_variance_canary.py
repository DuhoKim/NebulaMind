#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parent
SUBMITTER = ROOT / "run_footprint_variance_canary.py"
MONITOR = ROOT / "monitor_footprint_variance_canary.py"
MANIFEST = ROOT / "footprint_variance_partitioned_20260813/manifest.json"
QUERY = ROOT / "footprint_variance_partitioned_20260813/queries/query_000001_010000.adql"
GUARD = ROOT / "run_aggregate_tap.py"
EXPECTED_QUERY_SHA = "0d626704d44d8be36f6f3de45c57ad3eb377e9e5ec53608f01b11393560cbd98"
EXPECTED_GUARD_SHA = "228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FakeResponse:
    def __init__(self, *, status: int = 200, url: str, body: bytes = b"", location: str | None = None):
        self.status = status
        self._url = url
        self._body = body
        self.headers = {"Location": location} if location else {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def geturl(self) -> str:
        return self._url

    def read(self) -> bytes:
        return self._body


def main() -> None:
    submitter = load(SUBMITTER, "canary_submitter")
    monitor = load(MONITOR, "canary_monitor")
    manifest = json.loads(MANIFEST.read_text())

    entry = submitter.validate_canary_query(QUERY, MANIFEST, GUARD)
    assert entry["lo"] == 1 and entry["hi"] == 10000
    assert entry["query_sha256"] == EXPECTED_QUERY_SHA
    assert submitter.sha(QUERY) == EXPECTED_QUERY_SHA
    assert submitter.sha(GUARD) == EXPECTED_GUARD_SHA

    form = parse_qs(submitter.submission_form(QUERY.read_text()).decode())
    assert form == {
        "REQUEST": ["doQuery"],
        "LANG": ["ADQL"],
        "FORMAT": ["csv"],
        "phase": ["RUN"],
        "QUERY": [QUERY.read_text()],
    }

    mutated = QUERY.read_text().replace("BETWEEN 1 AND 10000", "BETWEEN 10001 AND 20000")
    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "bad.adql"
        bad.write_text(mutated)
        try:
            submitter.validate_canary_query(bad, MANIFEST, GUARD)
        except ValueError as exc:
            assert "one authorized canary query" in str(exc) or "hash" in str(exc)
        else:
            raise AssertionError("mutated range was accepted")

    submitted: list[object] = []

    def fake_submit(request, timeout):
        submitted.append(request)
        assert request.method == "POST"
        assert request.data is not None
        return FakeResponse(
            status=200,
            url="https://datalab.noirlab.edu/tap/async/canaryjob",
            location="https://datalab.noirlab.edu/tap/async/canaryjob",
        )

    with tempfile.TemporaryDirectory() as td:
        output = Path(td)
        result = submitter.run(QUERY, MANIFEST, GUARD, output, opener=fake_submit)
        assert result["job_url"].endswith("/canaryjob")
        assert len(submitted) == 1
        lifecycle = json.loads((output / "guard_lifecycle.json").read_text())
        assert lifecycle["exception_state"] == "CLOSED"
        assert lifecycle["submission_limit"] == 1
        assert lifecycle["submissions_made"] == 1
        assert lifecycle["ordinary_guard_sha256_before"] == EXPECTED_GUARD_SHA
        assert lifecycle["ordinary_guard_sha256_after"] == EXPECTED_GUARD_SHA
        assert lifecycle["ordinary_guard_unchanged"] is True
        assert lifecycle["ordinary_guard_verified_rejects_query_before"] is True
        assert lifecycle["ordinary_guard_verified_rejects_query_after"] is True
        assert lifecycle["submitter_sha256"] == submitter.sha(SUBMITTER)
        assert json.loads((output / "submission.json").read_text())["query_sha256"] == EXPECTED_QUERY_SHA
        assert not (output / "result.csv").exists()
        try:
            submitter.run(QUERY, MANIFEST, GUARD, output, opener=fake_submit)
        except RuntimeError as exc:
            assert "occupied" in str(exc) or "already" in str(exc)
        else:
            raise AssertionError("second submission was accepted")
        assert len(submitted) == 1

    assert monitor.classify_phase("PENDING") == "WAIT"
    assert monitor.classify_phase("QUEUED") == "WAIT"
    assert monitor.classify_phase("EXECUTING") == "QUEUE_OPEN"
    assert monitor.classify_phase("COMPLETED") == "QUEUE_OPEN"
    assert monitor.classify_phase("ERROR") == "TERMINAL_FAILURE"
    assert monitor.classify_phase("ABORTED") == "TERMINAL_FAILURE"

    get_requests: list[object] = []

    def fake_get(request, timeout):
        get_requests.append(request)
        assert request.method == "GET"
        assert request.data is None
        return FakeResponse(url=request.full_url, body=b"EXECUTING")

    with tempfile.TemporaryDirectory() as td:
        output = Path(td)
        (output / "submission.json").write_text(json.dumps({
            "job_url": "https://datalab.noirlab.edu/tap/async/canaryjob",
            "query_sha256": EXPECTED_QUERY_SHA,
        }))
        (output / "guard_lifecycle.json").write_text(json.dumps({
            "exception_state": "CLOSED",
            "ordinary_guard_unchanged": True,
            "ordinary_guard_verified_rejects_query_after": True,
        }))
        outcome = monitor.monitor(output, poll_seconds=300, max_wait_seconds=10800, opener=fake_get, sleeper=lambda _: None)
        assert outcome["monitor_result"] == "QUEUE_OPEN"
        assert outcome["observed_phase"] == "EXECUTING"
        assert outcome["full_manifest_auto_launches"] == 0
        assert len(get_requests) == 1
        assert json.loads((output / "queue_signal.json").read_text())["observed_phase"] == "EXECUTING"

    source = MONITOR.read_text()
    assert "run_partitioned_footprint_variance.py" not in source
    assert "doQuery" not in source
    assert 'method="POST"' not in source
    print("footprint_variance_canary_contract=PASS one_submission=1 poll_seconds=300 full_auto_launches=0")


if __name__ == "__main__":
    main()
