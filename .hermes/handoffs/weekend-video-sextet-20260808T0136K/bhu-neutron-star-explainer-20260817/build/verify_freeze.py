#!/usr/bin/env python3
"""Verify every path recorded by the frozen local render manifest."""
from __future__ import annotations

import json
from pathlib import Path

import pipeline


def verify_record(record: dict, base: Path) -> None:
    path = base / record["path"]
    if not path.is_file():
        raise RuntimeError(f"missing frozen file: {path}")
    if path.stat().st_size != record["bytes"]:
        raise RuntimeError(f"frozen size mismatch: {path}")
    actual = pipeline.sha256(path)
    if actual != record["sha256"]:
        raise RuntimeError(f"frozen hash mismatch: {path}: {actual}")


def main() -> int:
    manifest_path = pipeline.BUILD / "FREEZE.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["status"] != "FROZEN_LOCAL_ONLY_READY_FOR_KUN_REVIEW":
        raise RuntimeError(f"freeze status is not passing: {manifest['status']}")
    for record in manifest["gated_inputs"]:
        verify_record(record, pipeline.ROOT)
    for record in manifest["build_inventory"]:
        verify_record(record, pipeline.BUILD)
    verify_record(manifest["build_report"], pipeline.BUILD)
    candidate = pipeline.BUILD / manifest["candidate"]
    if pipeline.sha256(candidate) != manifest["candidate_sha256"]:
        raise RuntimeError("candidate hash mismatch")
    print(
        json.dumps(
            {
                "status": "PASS_FROZEN_PROVENANCE_VERIFIED",
                "candidate_sha256": manifest["candidate_sha256"],
                "gated_input_files": len(manifest["gated_inputs"]),
                "build_inventory_files": len(manifest["build_inventory"]),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
