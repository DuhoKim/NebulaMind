#!/usr/bin/env python3
"""Verify candidate, narration WAVs, QA, asset pins, and gated hashes."""
from __future__ import annotations

import json

import pipeline


def verify(item: dict) -> None:
    path = pipeline.ROOT / item["path"]
    if not path.is_file() or path.stat().st_size != item["bytes"] or pipeline.sha256(path) != item["sha256"]:
        raise RuntimeError(f"frozen record mismatch: {path}")


def main() -> int:
    manifest = json.loads((pipeline.BUILD / "FREEZE.json").read_text(encoding="utf-8"))
    if manifest["status"] != "FROZEN_LOCAL_ONLY_READY_FOR_KIMI_P2V2_RENDER_GATE":
        raise RuntimeError(f"non-passing freeze status: {manifest['status']}")
    verify(manifest["candidate"])
    for item in manifest["narration_wavs"] + manifest["gated_inputs"]:
        verify(item)
    verify(manifest["paper_figure_pins"])
    verify(manifest["qa"])
    verify(manifest["asr_qa"])
    if pipeline.DONE.read_text(encoding="utf-8").splitlines()[0] != "GPT3_P2V2_COMPLETE":
        raise RuntimeError("GPT3_DONE.md completion token mismatch")
    if len(manifest["narration_wavs"]) != 13:
        raise RuntimeError("frozen WAV count mismatch")
    print(json.dumps({"status": "PASS_P2V2_FROZEN_PROVENANCE_VERIFIED", "candidate_sha256": manifest["candidate"]["sha256"], "narration_wavs": len(manifest["narration_wavs"]), "gated_inputs": len(manifest["gated_inputs"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
