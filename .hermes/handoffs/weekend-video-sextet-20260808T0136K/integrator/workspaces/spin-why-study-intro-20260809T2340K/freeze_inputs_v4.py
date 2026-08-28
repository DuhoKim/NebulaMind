#!/usr/bin/env python3
"""Freeze v4 authority, primary abstracts, predecessor, script, and renderer identities."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT.parents[2]
PREDECESSOR = HANDOFF / "integrator/canaries/spin-method-overhaul-canary-20260808T1959K"
OUTPUT = ROOT / "source_manifest_v4.json"


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
        ("Hwao why-study order", HANDOFF / "HWAO_SPIN_WHY_INTRO_ORDER_20260809T2125K.md", ROOT / "sources/HWAO_SPIN_WHY_INTRO_ORDER_20260809T2125K.md"),
        ("Lana motivation and claim boundary", HANDOFF / "reviews/LANA_SPIN_WHY_MOTIVATION.md", ROOT / "sources/LANA_SPIN_WHY_MOTIVATION.md"),
        ("Goru mechanical motivation pass", HANDOFF / "reviews/GORU_SPIN_WHY_INTRO_PASS_20260809T2140K.md", ROOT / "sources/GORU_SPIN_WHY_INTRO_PASS_20260809T2140K.md"),
        ("Kun adversarial motivation pass", HANDOFF / "reviews/KUN_SPIN_WHY_INTRO_REOPEN_20260809T2125K.md", ROOT / "sources/KUN_SPIN_WHY_INTRO_REOPEN_20260809T2125K.md"),
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
        "mp4": record("Duho-watched predecessor with reopened presentation gate", PREDECESSOR / "spin-method-overhaul-canary-20260808T1959K.mp4"),
        "script": record("predecessor narration v3", PREDECESSOR / "narration_script_v3.json"),
    }
    if predecessor["mp4"]["sha256"] != "c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240":
        raise RuntimeError("predecessor MP4 changed")
    if predecessor["script"]["sha256"] != "1865f96b334a44499c58b6fdf545e140110bde2680ed202593dda2bd3a121f8b":
        raise RuntimeError("predecessor narration script changed")

    manifest = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": ROOT.name,
        "status": "V4_INPUTS_FROZEN_BEFORE_FRESH_SYNTHESIS",
        "build_release": "Duho explicitly released Yui to build in the active conversation; Kun review may continue in parallel and no current block exists.",
        "authorities": authority_records,
        "predecessor": predecessor,
        "primary_abstract_anchors": [
            record("Longo 2011 exact conditional abstract sentence", ROOT / "sources/LONGO_2011_ABSTRACT_EXACT.md"),
            record("Land et al. 2008 exact abstract", ROOT / "sources/LAND_2008_ABSTRACT_EXACT.md"),
            record("White 1984 exact ADS abstract", ROOT / "sources/WHITE_1984_ABSTRACT_EXACT.md"),
        ],
        "candidate_inputs": [
            record("v4 narration script", ROOT / "narration_script_v4.json"),
            record("v4 provisional storyboard", ROOT / "storyboard_v4.json"),
            record("isolated renderer", ROOT / "build.py"),
            record("Alloy synthesis script", ROOT / "synthesize_v4.py"),
            record("PCM timeline assembly script", ROOT / "assemble_audio_v4.py"),
        ],
        "closed_gates": {
            "video_reportable_now": False,
            "audio_fallback_permitted": False,
            "cockpit_or_public_copy_permitted": False,
            "human_watch_listen_acceptance_conferred": False,
        },
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n")
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
