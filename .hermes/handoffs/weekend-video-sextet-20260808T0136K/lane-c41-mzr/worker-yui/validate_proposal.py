#!/usr/bin/env python3
"""Validate the worker-Yui proposal without rendering media or invoking TTS."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

LANE = Path(__file__).resolve().parent
PROPOSAL_PATH = LANE / "STORYBOARD_PROPOSAL.json"
EVIDENCE_PATH = LANE / "EVIDENCE_FREEZE.json"
OUTPUT_PATH = LANE / "PROPOSAL_VALIDATION.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text)


def main() -> None:
    proposal = json.loads(PROPOSAL_PATH.read_text())
    evidence = json.loads(EVIDENCE_PATH.read_text())
    errors: list[str] = []
    warnings: list[str] = []

    if proposal["evidence_freeze_sha256"] != sha256(EVIDENCE_PATH):
        errors.append("evidence freeze hash mismatch")
    if proposal["status"] != "PROPOSAL_ONLY_HWAO_INTEGRATION_REQUIRED":
        errors.append("proposal status is not integration-gated")

    citations = proposal["display_citations"]
    beats = proposal["beats"]
    for beat in beats:
        if not beat.get("visual_action"):
            errors.append(f"{beat['id']}: missing visual action")
        if not beat.get("narration"):
            errors.append(f"{beat['id']}: missing narration proposal")
        for citation_id in beat.get("display_citations", []):
            if citation_id not in citations:
                errors.append(f"{beat['id']}: unknown citation {citation_id}")
        rendered = " ".join(beat.get("on_screen_copy", []))
        if "/Users/" in rendered or ".json" in rendered or ".tex" in rendered:
            errors.append(f"{beat['id']}: internal verification path leaked into audience copy")

    stage_expectations = {
        "b02_79_tables": ("79", "ARCHIVE TABLES"),
        "b03_23_candidate_tables": ("23", "CANDIDATE TABLES"),
        "b04_11_fetched_tables": ("11", "TABLES"),
        "b05_95_rows": ("95", "ROWS"),
        "b07_5_anchors": ("5", "ANCHORS"),
    }
    by_id = {beat["id"]: beat for beat in beats}
    for beat_id, tokens in stage_expectations.items():
        rendered = " ".join(by_id[beat_id]["on_screen_copy"])
        for token in tokens:
            if token not in rendered:
                errors.append(f"{beat_id}: missing primary token {token}")

    if evidence["funnel"]["stages"][-1]["count"] != 5:
        errors.append("evidence anchor count changed")
    if evidence["mass_bin_null"]["shared_minimum_per_bin"] != 3:
        errors.append("evidence bin threshold changed")

    total_seconds = sum(float(beat["duration_floor_seconds"]) for beat in beats)
    narration_words = sum(len(words(beat["narration"])) for beat in beats)
    delivered_wpm_at_floors = narration_words / total_seconds * 60
    if delivered_wpm_at_floors > 130:
        warnings.append("floor-timing WPM exceeds 130; Hwao must let actual Alloy durations expand the cards")

    safety = proposal["safety"]
    for key in ("shared_tools_modified", "storyboard_of_record_modified", "tts_invoked", "candidate_bundle_written", "public_artifact_modified"):
        if safety.get(key) is not False:
            errors.append(f"closed-gate safety field is not false: {key}")

    result = {
        "verdict": "PASS_PROPOSAL_ONLY" if not errors else "FAIL",
        "errors": errors,
        "warnings": warnings,
        "proposal_sha256": sha256(PROPOSAL_PATH),
        "evidence_freeze_sha256": sha256(EVIDENCE_PATH),
        "beat_count": len(beats),
        "beats_with_visual_actions": sum(bool(beat.get("visual_action")) for beat in beats),
        "duration_floor_seconds": total_seconds,
        "narration_word_count": narration_words,
        "estimated_delivered_wpm_at_duration_floors": round(delivered_wpm_at_floors, 2),
        "note": "This validates a visual/storyboard proposal only. It does not authorize TTS, candidate rendering, upload, or publication.",
    }
    OUTPUT_PATH.write_text(json.dumps(result, indent=2) + "\n")
    if errors:
        raise SystemExit(1)
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
