#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORCH = ROOT / "resume_partitioned_footprint_variance_rerun.py"


def load():
    spec = importlib.util.spec_from_file_location("rerun_recovery", ORCH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load()
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        a = root / "a"
        b = root / "b"
        a.mkdir()
        b.mkdir()
        (a / "submission.json").write_text(json.dumps({
            "recorded_utc": "2026-08-14T00:00:00Z",
            "job_url": "https://example/a",
        }) + "\n")
        (b / "submission.json").write_text(json.dumps({
            "recorded_utc": "2026-08-14T00:05:00Z",
            "job_url": "https://example/b",
        }) + "\n")
        manifest = {"entries": [{"run_dir": str(a)}, {"run_dir": str(b)}]}
        current = datetime(2026, 8, 14, 1, 0, tzinfo=timezone.utc)
        anchor_mono, anchor_utc, seen = module.progress_anchor(
            manifest,
            current_utc=current,
            current_monotonic=3600.0,
        )
        assert anchor_mono == 0.0
        assert anchor_utc == "2026-08-14T00:00:00Z"
        assert seen == set()

        (b / "poll_history.json").write_text(json.dumps({
            "job_url": "https://example/b",
            "phases": [
                {"timestamp_utc": "2026-08-14T00:10:00Z", "phase": "PENDING"},
                {"timestamp_utc": "2026-08-14T00:20:00Z", "phase": "EXECUTING"},
            ],
            "partial": True,
        }) + "\n")
        anchor_mono, anchor_utc, seen = module.progress_anchor(
            manifest,
            current_utc=current,
            current_monotonic=3600.0,
        )
        assert anchor_mono == 1200.0
        assert anchor_utc == "2026-08-14T00:20:00Z"
        assert seen == {"https://example/b"}
    print("partitioned_variance_recovery_clock=PASS")


if __name__ == "__main__":
    main()
