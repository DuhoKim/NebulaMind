#!/usr/bin/env python3
"""Draft-only §9 instrument identity and environment seal tooling."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from seal_gate.seal_gate import (  # noqa: E402 -- mandated shared helpers
    GateFailure, _seal_predecessor, canonical_bytes, sha256_bytes, sha256_file,
)

INSTRUMENT = ROOT.parent / "_successor_build_20260824/ref/successor_ref_v9.py"
SCHEMA = ROOT / "miniprereg_pins/env_record_schema.json"
PIN = "6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148"
TOP_KEYS = {"python_version", "package_versions", "os", "frozen_instrument_sha256"}
OS_KEYS = {"system", "release", "version", "machine"}


class InstrumentIdentityFailure(RuntimeError):
    pass


def verify_instrument(path: Path = INSTRUMENT, expected: str = PIN) -> str:
    observed = sha256_file(path)
    if observed != expected:
        raise InstrumentIdentityFailure("INSTRUMENT-INTEGRITY-FAIL: instrument sha256 mismatch")
    return observed


def capture_environment(instrument_digest: str = PIN) -> dict:
    # successor_ref_v9 imports NumPy; this module supplies the remaining runtime.
    return {
        "python_version": platform.python_version(),
        "package_versions": {"numpy": importlib.metadata.version("numpy")},
        "os": {"system": platform.system(), "release": platform.release(),
               "version": platform.version(), "machine": platform.machine()},
        "frozen_instrument_sha256": instrument_digest,
    }


def validate_environment(record: dict, schema_path: Path = SCHEMA) -> dict:
    # Closed, dependency-free validation of the pinned JSON Schema's constraints.
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    if schema.get("additionalProperties") is not False or set(record) != TOP_KEYS:
        raise InstrumentIdentityFailure("INSTRUMENT-INTEGRITY-FAIL: environment schema violation")
    if not isinstance(record["python_version"], str) or record["python_version"].count(".") < 2:
        raise InstrumentIdentityFailure("INSTRUMENT-INTEGRITY-FAIL: environment schema violation")
    packages = record["package_versions"]
    if not isinstance(packages, dict) or not packages or any(
        not isinstance(k, str) or not isinstance(v, str) or not v for k, v in packages.items()
    ):
        raise InstrumentIdentityFailure("INSTRUMENT-INTEGRITY-FAIL: environment schema violation")
    os_record = record["os"]
    if not isinstance(os_record, dict) or set(os_record) != OS_KEYS or any(
        not isinstance(os_record[k], str) or not os_record[k] for k in OS_KEYS
    ):
        raise InstrumentIdentityFailure("INSTRUMENT-INTEGRITY-FAIL: environment schema violation")
    if record["frozen_instrument_sha256"] != PIN:
        raise InstrumentIdentityFailure("INSTRUMENT-INTEGRITY-FAIL: environment schema violation")
    return record


def make_event(*, journal: Path, instrument_path: Path = INSTRUMENT,
               environment: dict | None = None, timestamp: str | None = None) -> dict:
    predecessor = _seal_predecessor(journal)
    digest = verify_instrument(instrument_path)
    env = validate_environment(environment or capture_environment(digest))
    body = {
        "timestamp": timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "operation": "instrument-identity", "path": str(instrument_path),
        "expected_digest": PIN, "observed_digest": digest,
        "byte_count": instrument_path.stat().st_size, "environment": env,
        "status": "PASS", "predecessor_receipt_digest": predecessor,
    }
    body["receipt_digest"] = sha256_bytes(canonical_bytes(body))
    return body


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--journal", type=Path, default=ROOT / "seal_journal_tierc.jsonl")
    ap.add_argument("--append", action="store_true")
    args = ap.parse_args(argv)
    try:
        event = make_event(journal=args.journal)
        if args.append:
            with args.journal.open("ab") as stream:
                stream.write(canonical_bytes(event))
        sys.stdout.buffer.write(canonical_bytes(event))
        return 0
    except (InstrumentIdentityFailure, GateFailure, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
