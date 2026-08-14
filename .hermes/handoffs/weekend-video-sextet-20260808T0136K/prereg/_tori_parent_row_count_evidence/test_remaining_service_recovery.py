#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import io
import json
import tempfile
import urllib.error
from email.message import Message
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    tap = load("tap_recovery", ROOT / "run_aggregate_tap.py")
    remaining = load("remaining_recovery", ROOT / "run_remaining_keyspace.py")
    renderer = load("remaining_renderer_recovery", ROOT / "render_remaining_receipt.py")

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        pressure = root / "service_pressure.json"
        calls = []

        class Response:
            status = 200
            headers = {}

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

            def geturl(self):
                return "https://example.invalid/phase"

            def read(self):
                return b"EXECUTING"

        def flaky_urlopen(req, timeout):
            calls.append(req.full_url)
            if len(calls) == 1:
                raise urllib.error.HTTPError(
                    req.full_url,
                    502,
                    "Bad Gateway",
                    Message(),
                    io.BytesIO(b"nginx 502 Bad Gateway"),
                )
            return Response()

        original_urlopen = tap.urllib.request.urlopen
        tap.urllib.request.urlopen = flaky_urlopen
        try:
            status, _, payload, _ = tap.request(
                "https://example.invalid/phase",
                pressure_path=pressure,
                transient_attempts=2,
                retry_seconds=0,
            )
        finally:
            tap.urllib.request.urlopen = original_urlopen
        assert status == 200 and payload == b"EXECUTING"
        assert len(calls) == 2
        pressure_data = json.loads(pressure.read_text())
        assert pressure_data["signal"] == "HTTP_502"
        assert pressure_data["request_stage"] == "poll_or_retrieval"

        dead = root / "dead"
        dead.mkdir()

        def missing_urlopen(req, timeout):
            raise urllib.error.HTTPError(
                req.full_url,
                404,
                "Not Found",
                Message(),
                io.BytesIO(b"job not found"),
            )

        tap.urllib.request.urlopen = missing_urlopen
        try:
            try:
                tap.request_phase(
                    "https://example.invalid/tap/async/dead",
                    dead,
                    transient_attempts=1,
                    retry_seconds=0,
                )
            except tap.HTTPStatusFailure as exc:
                assert exc.code == 404
            else:
                raise AssertionError("lost resumed job must remain an explicit failure signal")
        finally:
            tap.urllib.request.urlopen = original_urlopen
        lost = json.loads((dead / "remote_job_lost.json").read_text())
        assert lost["signal"] == "REMOTE_JOB_HTTP_404"
        assert lost["job_url"].endswith("/dead")

        run_dir = root / "run_181001_191000"
        tap_dir = run_dir / "tap"
        tap_dir.mkdir(parents=True)
        (tap_dir / "submission.json").write_text(
            json.dumps({"job_url": "https://example.invalid/dead", "query_sha256": "a" * 64}) + "\n"
        )
        (tap_dir / "runner_stderr.log").write_text("HTTPStatusFailure: HTTP 502 for /phase\n")
        (tap_dir / "runner_stdout.log").write_text("")
        manifest = {"entries": [{"lo": 181001, "hi": 191000, "run_dir": str(run_dir), "query_sha256": "a" * 64}]}
        prior = remaining.detect_prior_service_pressure(manifest)
        assert prior is not None
        assert prior["signal"] == "HTTP_502"
        assert prior["initial_concurrency"] == 1

        (tap_dir / "remote_job_lost.json").write_text(
            json.dumps({"signal": "REMOTE_JOB_HTTP_404", "job_url": "https://example.invalid/dead"}) + "\n"
        )
        assert remaining.classify_worker_failure(
            tap_dir,
            "HTTPStatusFailure: HTTP 502 for /phase\nHTTPStatusFailure: HTTP 404 for /phase\n",
        ) == "remote_job_lost"
        archive = remaining.archive_lost_attempt(
            tap_dir,
            manifest["entries"][0],
            "HTTPStatusFailure: HTTP 502 for /phase\nHTTPStatusFailure: HTTP 404 for /phase\n",
        )
        assert archive.parent.name == "failed_attempts"
        assert (archive / "submission.json").exists()
        assert (archive / "runner_stderr.log").exists()
        assert (archive / "remote_job_lost.json").exists()
        assert (archive / "failure_record.json").exists()
        assert not (tap_dir / "submission.json").exists()
        assert not (tap_dir / "runner_stderr.log").exists()
        archived_pressure = remaining.detect_prior_service_pressure(manifest)
        assert archived_pressure is not None
        assert archived_pressure["initial_concurrency"] == 1

        manifest_fixture = {
            "partition_count": 55,
            "remaining_key_count": 541174,
            "stop_rule": {"deadline_utc": "2026-08-12T21:00:00Z"},
        }
        totals = {
            "landed_new_partitions": 6,
            "landed_new_keys": 60000,
            "landed_total_keys": 181000,
            "contiguous_covered_hi": 181000,
            "all_landed_totals": dict(remaining.BASE_TOTALS),
        }
        status_fixture = {
            "totals": totals,
            "active_concurrency": 1,
            "stop_reason": "partition_failure_201001-211000",
        }
        event = {
            "detected_utc": "2026-08-12T14:40:53Z",
            "cause": "HTTP 502 Bad Gateway from nginx while polling three existing UWS /phase URLs",
            "runner_defect": "HTTP 502 was omitted from pressure handling; children exited and the generic hard-failure branch stopped the orchestrator",
            "landed_partitions_preserved": 6,
            "recovery_action": "resume same manifest serially; remotely lost job URLs require fresh submissions for unlanded ranges only",
        }
        text = renderer.render_text(manifest_fixture, status_fixture, [], [event])
        for needle in (
            "FAILED-STOPPED LOWER BOUND",
            "Failure and recovery history",
            "HTTP 502 Bad Gateway",
            "omitted from pressure handling",
            "same manifest serially",
            "six one-row receipts landed before the 502 incident remain authoritative",
        ):
            assert needle in text, needle

    print("remaining_service_recovery_test=PASS")


if __name__ == "__main__":
    main()
