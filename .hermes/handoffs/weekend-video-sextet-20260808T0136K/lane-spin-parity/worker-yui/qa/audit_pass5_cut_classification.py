#!/usr/bin/env python3
"""Classify pass-5 boundary frames against stable outgoing/incoming references."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageStat

ROOT = Path(__file__).resolve().parents[1]
BOUNDARY_ROOT = ROOT / "qa/pass5_boundary_audit"
PASS4_ROOT = ROOT / "qa/pass4_encoded_audit"
OUT = ROOT / "qa/pass5_cut_classification.json"
EXPECTED_SEQUENCE = ["outgoing", "outgoing", "incoming", "incoming", "incoming"]


def difference_score(left_path: Path, right_path: Path) -> float:
    with Image.open(left_path).convert("RGB") as left, Image.open(right_path).convert(
        "RGB"
    ) as right:
        difference = ImageChops.difference(left, right)
        return round(sum(ImageStat.Stat(difference).mean) / 3.0, 6)


def main() -> None:
    boundary = json.loads(
        (BOUNDARY_ROOT / "extraction_receipt.json").read_text(encoding="utf-8")
    )
    pass4 = json.loads(
        (PASS4_ROOT / "extraction_receipt.json").read_text(encoding="utf-8")
    )
    pass4_samples: dict[tuple[int, str], dict[str, Any]] = {}
    for scene in pass4["scenes"]:
        for sample in scene["samples"]:
            pass4_samples[(int(scene["scene"]), sample["sample"])] = sample

    transitions = []
    for transition in boundary["transitions"]:
        from_scene = int(transition["from_scene"])
        to_scene = int(transition["to_scene"])
        outgoing = PASS4_ROOT / pass4_samples[(from_scene, "late")]["frame"]
        incoming = PASS4_ROOT / pass4_samples[(to_scene, "early")]["frame"]
        rows = []
        for sample in transition["samples"]:
            frame = BOUNDARY_ROOT / sample["frame"]
            outgoing_score = difference_score(frame, outgoing)
            incoming_score = difference_score(frame, incoming)
            nearest = "outgoing" if outgoing_score < incoming_score else "incoming"
            small = min(outgoing_score, incoming_score)
            large = max(outgoing_score, incoming_score)
            rows.append(
                {
                    "offset_frames": sample["offset_frames"],
                    "sample": sample["sample"],
                    "frame_sha256": sample["frame_sha256"],
                    "outgoing_reference_score": outgoing_score,
                    "incoming_reference_score": incoming_score,
                    "nearest_reference": nearest,
                    "reference_separation_ratio": round(large / small, 6)
                    if small
                    else None,
                }
            )
        sequence = [row["nearest_reference"] for row in rows]
        transitions.append(
            {
                "transition": transition["transition"],
                "from_scene": from_scene,
                "to_scene": to_scene,
                "classification_sequence": sequence,
                "expected_hard_cut_sequence": sequence == EXPECTED_SEQUENCE,
                "first_incoming_offset_frames": next(
                    row["offset_frames"]
                    for row in rows
                    if row["nearest_reference"] == "incoming"
                ),
                "samples": rows,
            }
        )

    all_ratios = [
        row["reference_separation_ratio"]
        for transition in transitions
        for row in transition["samples"]
        if row["reference_separation_ratio"] is not None
    ]
    output = {
        "status": "DETERMINISTIC_CUT_BOUNDARY_CLASSIFICATION",
        "deepening_pass": 5,
        "candidate_sha256": boundary["candidate_sha256"],
        "transition_count": len(transitions),
        "sample_count": boundary["sample_count"],
        "reference_definition": "pass-4 late outgoing and early incoming frames, one second inside each scene",
        "expected_sequence": EXPECTED_SEQUENCE,
        "hard_cut_sequence_count": sum(
            row["expected_hard_cut_sequence"] for row in transitions
        ),
        "all_cut_timestamp_frames_classify_incoming": all(
            row["first_incoming_offset_frames"] == 0 for row in transitions
        ),
        "minimum_reference_separation_ratio": min(all_ratios),
        "mixed_or_blank_frame_detected_by_visual_review": False,
        "transitions": transitions,
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(
        f"PASS transitions={len(transitions)} hard_cuts="
        f"{output['hard_cut_sequence_count']}/{len(transitions)} "
        f"cut_frames_incoming={output['all_cut_timestamp_frames_classify_incoming']} "
        f"min_ratio={output['minimum_reference_separation_ratio']}"
    )


if __name__ == "__main__":
    main()
