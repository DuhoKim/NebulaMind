#!/usr/bin/env python3
"""Freeze v3 authority, predecessor, script, storyboard, and renderer identities."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT.parents[2]
PREDECESSOR = ROOT.parent / "spin-method-overhaul-canary-20260808T1312K"
OUTPUT = ROOT / "source_manifest_v3.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(label: str, path: Path) -> dict:
    return {
        "label": label,
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def main() -> int:
    authorities = [
        ("Hwao introduction order", HANDOFF / "reviews/HWAO_INTRODUCTION_ORDER.md", ROOT / "sources/HWAO_INTRODUCTION_ORDER.md"),
        ("Hwao narrative correction", HANDOFF / "reviews/HWAO_NARRATIVE_CORRECTION.md", ROOT / "sources/HWAO_NARRATIVE_CORRECTION.md"),
        ("Lana narrative and boundary review", HANDOFF / "reviews/LANA_OVERHAUL.md", ROOT / "sources/LANA_OVERHAUL.md"),
        ("Spin status", HANDOFF / "lanes/spin/STATUS.json", ROOT / "sources/STATUS.json"),
        ("Spin source freeze", HANDOFF / "lanes/spin/SOURCE_FREEZE.json", ROOT / "sources/SOURCE_FREEZE.json"),
    ]
    authority_records = []
    for label, origin, frozen in authorities:
        origin_record = record(label + " origin", origin)
        frozen_record = record(label + " frozen copy", frozen)
        if origin_record["sha256"] != frozen_record["sha256"]:
            raise RuntimeError(f"authority drift while freezing {label}")
        authority_records.append({"label": label, "origin": origin_record, "frozen_copy": frozen_record})

    predecessor = {
        "mp4": record("accepted-with-incident predecessor MP4", PREDECESSOR / "spin-method-overhaul-canary-20260808T1312K.mp4"),
        "script": record("accepted predecessor narration v2", PREDECESSOR / "narration_script_v2.json"),
    }
    if predecessor["mp4"]["sha256"] != "40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9":
        raise RuntimeError("predecessor MP4 changed")
    if predecessor["script"]["sha256"] != "3f033dd02d00767c6bb4cc1baf8b7197a78847bad076411cbaed9aab732cd416":
        raise RuntimeError("predecessor narration script changed")

    manifest = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": ROOT.name,
        "status": "FINAL_INPUTS_FROZEN_AFTER_GATEWAY_RESTORATION",
        "authorities": authority_records,
        "predecessor": predecessor,
        "candidate_inputs": [
            record("v3 narration script", ROOT / "narration_script_v3.json"),
            record("provisional storyboard", ROOT / "storyboard_v3.json"),
            record("isolated renderer", ROOT / "build.py"),
            record("Alloy synthesis script", ROOT / "synthesize_v3.py"),
            record("PCM timeline assembly script", ROOT / "assemble_audio_v3.py"),
        ],
        "closed_gates": {
            "video_reportable_now": False,
            "audio_fallback_permitted": False,
            "cockpit_or_public_copy_permitted": False,
        },
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n")
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
