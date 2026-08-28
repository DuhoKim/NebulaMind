#!/usr/bin/env python3
"""Freeze v5 live order, literature anchors, predecessor, script, and renderer identities."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT.parents[2]
PREDECESSOR = HANDOFF / "integrator/canaries/spin-method-overhaul-canary-20260809T2340K"
OUTPUT = ROOT / "source_manifest_v5.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(label: str, path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return {
        "label": label,
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def checked_pair(label: str, origin: Path, frozen: Path) -> dict:
    origin_record = record(label + " origin", origin)
    frozen_record = record(label + " frozen copy", frozen)
    if origin_record["sha256"] != frozen_record["sha256"]:
        raise RuntimeError(f"authority drift while freezing {label}")
    return {"label": label, "origin": origin_record, "frozen_copy": frozen_record}


def main() -> int:
    authorities = [
        checked_pair(
            "Lana revised literature Beat 4 Part 1",
            HANDOFF / "reviews/LANA_SPIN_BEAT4_AND_BHU_ASSESSMENT_20260810.md",
            ROOT / "sources/LANA_SPIN_BEAT4_AND_BHU_ASSESSMENT_20260810.md",
        ),
        checked_pair(
            "withdrawn source-freeze amendment",
            HANDOFF / "lanes/spin/SOURCE_FREEZE_AMENDMENT_A1_WITHDRAWN_20260810T1424K.md",
            ROOT / "sources/SOURCE_FREEZE_AMENDMENT_A1_WITHDRAWN_20260810T1424K.md",
        ),
    ]
    predecessor = {
        "mp4": record(
            "Duho-watched 4d230cc0 predecessor",
            PREDECESSOR / "spin-method-overhaul-canary-20260809T2340K.mp4",
        ),
        "script": record("predecessor narration v4", PREDECESSOR / "narration_script_v4.json"),
    }
    if predecessor["mp4"]["sha256"] != "4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078":
        raise RuntimeError("predecessor MP4 changed")
    if predecessor["script"]["sha256"] != "5df1d0a20e1feede746a82cd784ecd43c5cd1f21ebcc74d5418cbb87d69e90f1":
        raise RuntimeError("predecessor narration script changed")

    manifest = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": ROOT.name,
        "status": "V5_INPUTS_FROZEN_BEFORE_FRESH_SYNTHESIS",
        "build_release": "Duho directly ordered the literature-only Spin revision in the active conversation.",
        "authorities": authorities,
        "live_order_binding": record("live order binding", ROOT / "LIVE_ORDER_BINDING.json"),
        "predecessor": predecessor,
        "primary_abstract_anchors": [
            record("Longo 2011 abstract", ROOT / "sources/LONGO_2011_ABSTRACT_EXACT.md"),
            record("Shamir 2012 abstract", ROOT / "sources/SHAMIR_2012_ABSTRACT_EXACT.md"),
            record("Land et al. 2008 abstract", ROOT / "sources/LAND_2008_ABSTRACT_EXACT.md"),
            record("White 1984 abstract", ROOT / "sources/WHITE_1984_ABSTRACT_EXACT.md"),
        ],
        "candidate_inputs": [
            record("v5 narration script", ROOT / "narration_script_v5.json"),
            record("v5 provisional storyboard", ROOT / "storyboard_v5.json"),
            record("isolated renderer", ROOT / "build.py"),
            record("Alloy 1.18 synthesis", ROOT / "synthesize_v5.py"),
            record("PCM timeline assembly", ROOT / "assemble_audio_v5.py"),
            record("post-encode guardrail QA", ROOT / "qa_encoded.py"),
        ],
        "excluded_input": {
            "path": str(HANDOFF / "reviews/LANA_SPIN_BHU_BEAT_DRAFT_20260810.md"),
            "sha256": "228be3deb9ef8d8f233d162a5a4cb5b084911d8d41f3896d703a84765a40c090",
            "used": False,
        },
        "closed_gates": {
            "video_reportable_now": False,
            "audio_fallback_permitted": False,
            "cockpit_or_public_copy_permitted": False,
            "human_watch_acceptance_conferred": False,
        },
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n")
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
