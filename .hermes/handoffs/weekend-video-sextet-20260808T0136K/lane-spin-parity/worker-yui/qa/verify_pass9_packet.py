#!/usr/bin/env python3
"""Verify pass-9 title-safe evidence, correction, blockers, and custody."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "spin-parity-census-20260805T1922K"
)
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
CANDIDATE_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
T4_SHA = "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873"
A38_SHA = "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0"
KUN_SHA = "ccedf6846391a8f0661a88b2eec0ce21fbfd7c44ad16201080bb196f56d258e5"
CANDIDATE_AUDIT = ROOT / "qa/pass9_safe_area_audit"
METHOD_AUDIT = ROOT / "qa/pass9_v8_safe_area"
SNAPSHOT = ROOT / "qa/pass9_review_snapshot_v1.json"
VARIANTS = [
    "clean",
    "symmetric_crop_3pct",
    "symmetric_crop_5pct",
    "horizontal_crop_5pct",
    "vertical_crop_5pct",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(relative: str) -> Any:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> None:
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    require(snapshot["snapshot_status"] == "IMMUTABLE_REVIEW_SNAPSHOT", "snapshot status")
    require(
        snapshot["snapshot_id"] == "spin-worker-yui-pass9-review-v1-20260808T064214K",
        "snapshot id",
    )
    require(snapshot["supersedes"]["path"] == "qa/pass8_review_snapshot_v1.json", "supersession path")
    require(
        sha256(ROOT / snapshot["supersedes"]["path"]) == snapshot["supersedes"]["sha256"],
        "superseded snapshot hash",
    )
    for artifact in snapshot["pinned_artifacts"]:
        path = ROOT / artifact["path"]
        require(path.is_file(), f"missing pinned artifact {artifact['path']}")
        require(sha256(path) == artifact["sha256"], f"pinned hash {artifact['path']}")

    require(sha256(CANDIDATE) == CANDIDATE_SHA, "candidate closing hash")
    receipt = load_json("qa/pass9_safe_area_audit/extraction_receipt.json")
    require(receipt["deepening_pass"] == 9, "extraction pass")
    require(receipt["candidate_sha256"] == CANDIDATE_SHA, "receipt candidate")
    require(receipt["candidate_hash_match"] is True and receipt["candidate_modified"] is False, "candidate custody")
    require(receipt["detected_cut_count"] == 15 and receipt["scene_count"] == 16, "scene census")
    require(receipt["variants"] == VARIANTS, "candidate variants")
    require(receipt["variant_count"] == 5 and receipt["frame_count"] == 80, "candidate frame census")
    require(receipt["resolution"] == [1920, 1080], "candidate resolution")
    require(receipt["crop_insets_pixels"] == {
        "horizontal_crop_5pct": [96, 0],
        "symmetric_crop_3pct": [58, 32],
        "symmetric_crop_5pct": [96, 54],
        "vertical_crop_5pct": [0, 54],
    }, "candidate crop insets")
    pass8 = load_json("qa/pass8_color_vision_audit/extraction_receipt.json")
    require(receipt["detected_cut_times_seconds"] == pass8["detected_cut_times_seconds"], "fresh cut reproduction")
    pass8_color = {
        int(scene["scene"]): next(
            sample["frame_sha256"] for sample in scene["samples"] if sample["variant"] == "color"
        )
        for scene in pass8["scenes"]
    }
    frame_hashes: list[str] = []
    clean_matches = 0
    for expected_scene, scene in enumerate(receipt["scenes"], start=1):
        require(scene["scene"] == expected_scene, f"candidate scene order {expected_scene}")
        require([sample["variant"] for sample in scene["samples"]] == VARIANTS, f"candidate variants scene {expected_scene}")
        for sample in scene["samples"]:
            frame = CANDIDATE_AUDIT / sample["frame"]
            require(sha256(frame) == sample["frame_sha256"], f"candidate derivative {sample['frame']}")
            frame_hashes.append(sample["frame_sha256"])
            with Image.open(frame) as image:
                require(image.mode == "RGB" and image.size == (1920, 1080), f"candidate frame shape {sample['frame']}")
            if sample["variant"] == "clean":
                clean_matches += sample["frame_sha256"] == pass8_color[expected_scene]
    require(clean_matches == 16, "clean midpoint byte reproduction")
    require(len(frame_hashes) == 80 and len(set(frame_hashes)) == 80, "candidate frame hashes")
    for variant in VARIANTS:
        sheet = receipt["contact_sheets"][variant]
        require(sha256(CANDIDATE_AUDIT / sheet["path"]) == sheet["sha256"], f"candidate sheet {variant}")
        require(sheet["sha256"] == snapshot["pass9_encoded_evidence"]["contact_sheet_sha256"][variant], f"snapshot candidate sheet {variant}")

    quantitative = load_json("qa/pass9_safe_area_quantitative_audit.json")
    require(quantitative["variant_order"] == VARIANTS, "quantitative variants")
    require(quantitative["candidate"]["scene_count"] == 16 and quantitative["candidate"]["frame_count"] == 80, "quantitative candidate census")
    require(quantitative["candidate"]["cut_times_exact_pass8"] is True, "quantitative cuts")
    require(quantitative["candidate"]["clean_midpoints_byte_identical_to_pass8_color"] == 16, "quantitative clean reproduction")
    expected_candidate = {
        "symmetric_crop_3pct": (0.980399, 1.0, 0.987756, 0.972159),
        "symmetric_crop_5pct": (0.981884, 0.99569, 0.994975, 0.973861),
        "horizontal_crop_5pct": (0.981868, 0.993606, 0.994174, 0.980586),
        "vertical_crop_5pct": (0.985634, 1.0, 0.993373, 0.977452),
    }
    for variant, expected in expected_candidate.items():
        row = quantitative["candidate"]["aggregates"][variant]
        actual = (
            row["mean_full_token_recall_vs_clean"],
            row["mean_headline_token_recall_vs_clean"],
            row["mean_lower_support_token_recall_vs_clean"],
            row["mean_numeric_token_recall_vs_clean"],
        )
        require(actual == expected, f"candidate aggregate {variant}")
        require(row["structural_gate_scene_count"] == 0, f"candidate gates {variant}")
    critical = quantitative["candidate"]["held_critical_aggregates"]["symmetric_crop_5pct"]
    require(critical["scenes"] == [7, 9, 10, 11, 16], "critical scenes")
    require(critical["mean_headline_token_recall_vs_clean"] == 1.0, "critical headline")
    require(critical["mean_full_token_recall_vs_clean"] == 0.965485, "critical full")
    require(critical["mean_numeric_token_recall_vs_clean"] == 0.916356, "critical numeric")
    require(critical["structural_gate_scene_count"] == 0, "critical gates")

    method_receipt = load_json("qa/pass9_v8_safe_area/receipt.json")
    require(method_receipt["status"] == "QA_STATIC_DERIVATIVES_ONLY_NOT_V9_NOT_A_CANDIDATE", "method receipt status")
    require(method_receipt["variant_order"] == VARIANTS, "method variants")
    require(method_receipt["scene_count"] == 14 and method_receipt["frame_count"] == 70, "method census")
    require(method_receipt["sealed_v8_modified"] is False, "sealed v8 modified")
    require(method_receipt["pass7_mockup_modified"] is False, "pass7 proof modified")
    require(method_receipt["v9_created"] is False, "v9 disposition")
    for group_name in ("sealed_v8", "pass7_caption_safe"):
        group = method_receipt["groups"][group_name]
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"group census {group_name}")
        for scene in group["scenes"]:
            source = ROOT / scene["source"]
            require(sha256(source) == scene["source_sha256"], f"method source {group_name} scene {scene['scene']}")
            require(scene["clean_copy_sha256_match"] is True, f"method clean copy {group_name} scene {scene['scene']}")
            require([sample["variant"] for sample in scene["samples"]] == VARIANTS, f"method variants {group_name} scene {scene['scene']}")
            for sample in scene["samples"]:
                frame = METHOD_AUDIT / group_name / sample["frame"]
                require(sha256(frame) == sample["frame_sha256"], f"method derivative {group_name}/{sample['frame']}")
                with Image.open(frame) as image:
                    require(image.mode == "RGB" and image.size == (1920, 1080), f"method frame shape {group_name}/{sample['frame']}")
        for variant, sheet in group["contact_sheets"].items():
            require(sha256(METHOD_AUDIT / group_name / sheet["path"]) == sheet["sha256"], f"method sheet {group_name}/{variant}")

    sealed = quantitative["method_groups"]["sealed_v8"]
    caption = quantitative["method_groups"]["pass7_caption_safe"]
    require(sealed["clean_tokens_outside_safe_3pct"] == 7, "sealed 3pct risk")
    require(sealed["clean_tokens_outside_safe_5pct"] == 44, "sealed 5pct risk")
    require(caption["clean_tokens_outside_safe_3pct"] == 7, "caption 3pct risk")
    require(caption["clean_tokens_outside_safe_5pct"] == 44, "caption 5pct risk")
    sealed_3 = sealed["aggregates"]["symmetric_crop_3pct"]
    sealed_5 = sealed["aggregates"]["symmetric_crop_5pct"]
    caption_3 = caption["aggregates"]["symmetric_crop_3pct"]
    caption_5 = caption["aggregates"]["symmetric_crop_5pct"]
    require(sealed_3["mean_full_token_recall_vs_clean"] == 0.939553, "sealed 3pct full")
    require(sealed_3["mean_headline_token_recall_vs_clean"] == 0.979692, "sealed 3pct headline")
    require(sealed_5["mean_full_token_recall_vs_clean"] == 0.899783, "sealed 5pct full")
    require(sealed_5["mean_headline_token_recall_vs_clean"] == 0.946693, "sealed 5pct headline")
    require(sealed_5["mean_numeric_token_recall_vs_clean"] == 0.705597, "sealed 5pct numeric")
    require(caption_3["mean_full_token_recall_vs_clean"] == 0.932761, "caption 3pct full")
    require(caption_5["mean_full_token_recall_vs_clean"] == 0.89602, "caption 5pct full")
    require(caption_5["mean_headline_token_recall_vs_clean"] == 0.957313, "caption 5pct headline")
    require(caption_5["mean_numeric_token_recall_vs_clean"] == 0.705597, "caption 5pct numeric")
    require(caption_5["scene_specific_gate_count"] == 7, "caption 5pct specific gates")
    human = quantitative["human_visual_review"]
    require(human["candidate_dominant_result_hierarchy_survives_3pct_and_5pct"] is True, "candidate visual hierarchy")
    require(human["candidate_structural_hold_visible_3pct_or_5pct"] is False, "candidate visual gate")
    require(human["sealed_v8_3pct_semantic_loss_scene_count"] == 0, "sealed 3pct semantic loss")
    require(human["sealed_v8_5pct_badge_capsules_clipped"] == "7/7", "sealed badge clipping")
    require(human["sealed_v8_5pct_left_header_clipped"] == "7/7", "sealed header clipping")
    require(human["sealed_v8_5pct_edge_content_clipped_scenes"] == [1, 5, 7], "sealed edge scenes")
    require(human["pass7_caption_safe_5pct_specific_gate_lines"] == "7/7", "caption visual gates")
    require(human["pass7_caption_safe_5pct_badge_capsules_clipped"] == "7/7", "caption badge clipping")
    require(human["five_percent_title_safe_contract"] == "FAIL_LAYOUT_EDGE_CUSTODY__PRIMARY_GATE_TEXT_SURVIVES", "title-safe verdict")

    correction = load_json("TITLE_SAFE_STORYBOARD_CORRECTION_PASS9.json")
    require(correction["status"] == "PROPOSAL_ONLY_LAYOUT_CORRECTION_NOT_V9_NOT_A_CANDIDATE", "correction status")
    proposed = correction["proposed_storyboard_integration_correction"]
    require(proposed["type"] == "TITLE_SAFE_LAYOUT_CONTRACT", "correction type")
    require(proposed["required_safe_rectangle"] == {
        "left": 96,
        "top": 54,
        "right": 1824,
        "bottom": 1026,
        "definition": "Every semantic or audience-readable element, including its border or marker, must fit fully inside this rectangle. The outer five percent is decorative-only.",
    }, "safe rectangle")
    require(proposed["future_pixel_layout_change_requested"] is True, "future layout request")
    require(proposed["worker_pixel_change_performed"] is False, "worker pixel action")
    require(correction["base"]["sealed_v8_modified"] is False and correction["base"]["v9_created"] is False, "correction v8 custody")
    require(correction["science_boundary"]["video_reportable_now"] is False, "correction reportability")
    require(correction["science_boundary"]["does_not_authorize_result"] is True, "correction result authorization")

    packet = load_json("BLOCKER_PACKET_PASS9.json")
    require(packet["video_reportable_now"] is False, "packet reportability")
    require(packet["candidate"]["sha256"] == CANDIDATE_SHA, "packet candidate")
    require(packet["representation_correction"]["v9_created"] is False, "packet v9")
    require(packet["representation_correction"]["worker_pixel_change_performed"] is False, "packet worker pixels")
    require(packet["pass9_encoded_audit"]["held_critical_scenes_7_9_10_11_16_symmetric_crop_5pct"]["structural_gate_scene_count"] == 0, "packet gates")
    packet_text = json.dumps(packet, sort_keys=True)
    for raw_result_field in ("primary_pairs_read", "control_pairs_reported_never_read", '"cells"', '"reading"', '"reading_why"'):
        require(raw_result_field not in packet_text, f"raw result field leaked: {raw_result_field}")

    require(sha256(SOURCE / "T4_PAIRED_FLIP.json") == T4_SHA, "T4 source hash")
    require(sha256(SOURCE / "AMENDMENT_A3.8_DRAFT.md") == A38_SHA, "A3.8 contract hash")
    frame_review = SOURCE / "KUN_FRAME_REVIEW.md"
    require(sha256(frame_review) == KUN_SHA, "frame review hash")
    require(frame_review.read_text(encoding="utf-8").rstrip().endswith("FRAME REVIEW: AGREES FRAME_UNSTATED"), "frame review terminal status")
    require(load_json("SOURCE_STATUS_FREEZE.json")["video_reportable_now"] is False, "freeze reportability")
    require(load_json("qa/static_proposal_validation.json")["verdict"] == "PASS", "v8 static validation")

    extraction_time = parse_time(receipt["extracted_at_utc"])
    packet_time = parse_time(packet["checked_at"])
    snapshot_time = parse_time(snapshot["created_at"])
    require(extraction_time < packet_time < snapshot_time, "pass9 chronology")

    status = load_json("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS9_V1", "status phase")
    require(status["video_reportable_now"] is False, "status reportability")
    receipt_text = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    require("SPIN_WORKER_YUI_DEEPENING_PASS9_COMPLETE" in receipt_text, "receipt marker")
    require(snapshot["snapshot_id"] in receipt_text, "receipt snapshot")
    integrator = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    require(snapshot["snapshot_id"] in integrator, "integrator snapshot")
    require("inner 5%" in integrator and "decorative-only" in integrator, "integrator title-safe contract")

    media = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.casefold()
        in {".mp4", ".mp3", ".wav", ".aac", ".m4a", ".mov", ".webm"}
    ]
    require(not media, f"worker media outputs present: {media}")
    print(
        "PASS pass9 snapshot/candidate/80-safe-area-frames/hierarchy/"
        "70-method-derivatives/title-safe-correction/source-blockers/status/no-media"
    )


if __name__ == "__main__":
    main()
