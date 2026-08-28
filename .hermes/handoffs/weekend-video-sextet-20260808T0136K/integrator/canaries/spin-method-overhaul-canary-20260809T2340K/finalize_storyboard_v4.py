#!/usr/bin/env python3
"""Bind v4 visual actions to the final PCM-derived timeline."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "narration_script_v4.json"
TIMELINE = ROOT / "audio_v4/timeline.json"
OUTPUT = ROOT / "storyboard_v4_final.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    script = json.loads(SCRIPT.read_text())
    timeline = json.loads(TIMELINE.read_text())
    sentence_by_id = {item["id"]: item for item in script["sentences"]}
    if list(sentence_by_id) != [item["id"] for item in timeline["records"]]:
        raise RuntimeError("script/timeline sentence order mismatch")
    records = []
    for timed in timeline["records"]:
        authored = sentence_by_id[timed["id"]]
        if timed["text"] != authored["text"] or timed["section"] != authored["section"]:
            raise RuntimeError(f"script/timeline content mismatch: {timed['id']}")
        records.append(
            {
                **timed,
                "beat": authored.get("beat"),
                "visual_action": authored["visual_action"],
                "display_citation": authored.get("display_citation"),
                "timing_status": "PCM_DERIVED_FINAL",
            }
        )
    output = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "revision": script["revision"],
        "status": "PCM_DERIVED_FINAL_PENDING_TORI_AND_DUHO_REVIEW",
        "video_reportable_now": False,
        "human_acceptance_conferred": False,
        "script": SCRIPT.name,
        "script_sha256": sha256(SCRIPT),
        "timeline": str(TIMELINE.relative_to(ROOT)),
        "timeline_sha256": sha256(TIMELINE),
        "sentence_count": len(records),
        "master_duration_seconds": timeline["master_duration_seconds"],
        "delivered_wpm": timeline["delivered_wpm"],
        "max_abs_audio_visual_start_delta_seconds": timeline["max_abs_audio_visual_start_delta_seconds"],
        "records": records,
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
