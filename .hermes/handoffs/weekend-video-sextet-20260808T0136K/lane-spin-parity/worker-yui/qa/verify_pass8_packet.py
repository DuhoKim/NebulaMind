#!/usr/bin/env python3
"""Verify pass-8 color-vision evidence, guard, blockers, and custody."""

from __future__ import annotations

import hashlib
import json
import re
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
CANDIDATE_AUDIT = ROOT / "qa/pass8_color_vision_audit"
METHOD_AUDIT = ROOT / "qa/pass8_v8_color_vision"
SNAPSHOT = ROOT / "qa/pass8_review_snapshot_v1.json"
VARIANTS = [
    "color",
    "grayscale_bt709",
    "protanopia_machado100",
    "deuteranopia_machado100",
    "tritanopia_machado100",
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
        snapshot["snapshot_id"] == "spin-worker-yui-pass8-review-v1-20260808T061653K",
        "snapshot id",
    )
    require(snapshot["supersedes"]["path"] == "qa/pass7_review_snapshot_v1.json", "supersession path")
    require(
        sha256(ROOT / snapshot["supersedes"]["path"]) == snapshot["supersedes"]["sha256"],
        "superseded snapshot hash",
    )
    for artifact in snapshot["pinned_artifacts"]:
        path = ROOT / artifact["path"]
        require(path.is_file(), f"missing pinned artifact {artifact['path']}")
        require(sha256(path) == artifact["sha256"], f"pinned hash {artifact['path']}")

    require(sha256(CANDIDATE) == CANDIDATE_SHA, "candidate closing hash")
    receipt = load_json("qa/pass8_color_vision_audit/extraction_receipt.json")
    require(receipt["deepening_pass"] == 8, "extraction pass")
    require(receipt["candidate_sha256"] == CANDIDATE_SHA, "receipt candidate")
    require(receipt["candidate_hash_match"] is True and receipt["candidate_modified"] is False, "candidate custody")
    require(receipt["detected_cut_count"] == 15 and receipt["scene_count"] == 16, "scene census")
    require(receipt["variants"] == VARIANTS, "candidate variants")
    require(receipt["variant_count"] == 5 and receipt["frame_count"] == 80, "candidate frame census")
    require(receipt["resolution"] == [1920, 1080], "candidate resolution")
    require(receipt["simulation_scope"].endswith("not a clinical diagnostic"), "simulation limit")
    pass7 = load_json("qa/pass7_obstruction_audit/extraction_receipt.json")
    require(receipt["detected_cut_times_seconds"] == pass7["detected_cut_times_seconds"], "fresh cut reproduction")
    pass7_clean = {
        int(scene["scene"]): next(
            sample["frame_sha256"] for sample in scene["samples"] if sample["variant"] == "clean"
        )
        for scene in pass7["scenes"]
    }
    frame_hashes: list[str] = []
    color_matches = 0
    for expected_scene, scene in enumerate(receipt["scenes"], start=1):
        require(scene["scene"] == expected_scene, f"candidate scene order {expected_scene}")
        require([sample["variant"] for sample in scene["samples"]] == VARIANTS, f"candidate variants scene {expected_scene}")
        for sample in scene["samples"]:
            frame = CANDIDATE_AUDIT / sample["frame"]
            require(sha256(frame) == sample["frame_sha256"], f"candidate derivative {sample['frame']}")
            frame_hashes.append(sample["frame_sha256"])
            with Image.open(frame) as image:
                require(image.mode == "RGB" and image.size == (1920, 1080), f"candidate frame shape {sample['frame']}")
            if sample["variant"] == "color":
                color_matches += sample["frame_sha256"] == pass7_clean[expected_scene]
    require(color_matches == 16, "color midpoint byte reproduction")
    require(len(frame_hashes) == 80 and len(set(frame_hashes)) == 80, "candidate frame hashes")
    for variant in VARIANTS:
        sheet = receipt["contact_sheets"][variant]
        require(sha256(CANDIDATE_AUDIT / sheet["path"]) == sheet["sha256"], f"candidate sheet {variant}")
        require(sheet["sha256"] == snapshot["pass8_encoded_evidence"]["contact_sheet_sha256"][variant], f"snapshot candidate sheet {variant}")

    quantitative = load_json("qa/pass8_color_vision_quantitative_audit.json")
    require(quantitative["scene_count"] == 16 and quantitative["frame_count"] == 80, "quantitative census")
    require(quantitative["variant_order"] == VARIANTS, "quantitative variants")
    require(quantitative["custody_reproduction"]["cut_times_exact_pass7"] is True, "quantitative cuts")
    require(quantitative["custody_reproduction"]["color_midpoints_byte_identical_to_pass7_clean"] == 16, "quantitative color reproduction")
    expected_all = {
        "grayscale_bt709": (1.0, 0.933301, 0.877063, 0.910233, 0.999942, 0.0),
        "protanopia_machado100": (1.0, 0.979962, 0.979505, 0.959358, 0.999953, 0.827857),
        "deuteranopia_machado100": (1.0, 0.93998, 0.926533, 0.962081, 0.99995, 0.909159),
        "tritanopia_machado100": (1.0, 0.982433, 0.978786, 0.952005, 0.999839, 1.040287),
    }
    for variant, expected in expected_all.items():
        row = quantitative["aggregates"][variant]
        actual = (
            row["mean_headline_token_retention_vs_color"],
            row["mean_full_token_retention_vs_color"],
            row["mean_lower_support_token_retention_vs_color"],
            row["mean_numeric_token_retention_vs_color"],
            row["mean_edge_recall_vs_color_1px_tolerance"],
            row["mean_chroma_retention_on_color_saturated_pixels"],
        )
        require(actual == expected, f"candidate aggregate {variant}")
        require(row["scenes_with_any_structural_gate"] == 0, f"candidate gates {variant}")
    gray_critical = quantitative["critical_plot_scene_aggregates"]["grayscale_bt709"]
    require(gray_critical["scenes"] == [5, 7, 9, 10, 11], "critical plot scenes")
    require(gray_critical["mean_headline_token_retention_vs_color"] == 1.0, "critical headline")
    require(gray_critical["mean_full_token_retention_vs_color"] == 0.808086, "critical full")
    require(gray_critical["mean_lower_support_token_retention_vs_color"] == 0.739935, "critical support")
    require(gray_critical["mean_numeric_token_retention_vs_color"] == 0.779412, "critical numeric")
    require(gray_critical["mean_edge_recall_vs_color_1px_tolerance"] == 0.999998, "critical edge")
    require(gray_critical["mean_chroma_retention_on_color_saturated_pixels"] == 0.0, "critical chroma")
    for variant in VARIANTS:
        held = quantitative["held_critical_gate_counts"][variant]
        require(held["scenes"] == [7, 9, 10, 11, 16], f"held critical scenes {variant}")
        require(held["structural_gate_scene_count"] == 0, f"held critical gates {variant}")

    method_receipt = load_json("qa/pass8_v8_color_vision/receipt.json")
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
            require(scene["color_copy_sha256_match"] is True, f"method color copy {group_name} scene {scene['scene']}")
            require([sample["variant"] for sample in scene["samples"]] == VARIANTS, f"method variants {group_name} scene {scene['scene']}")
            for sample in scene["samples"]:
                frame = METHOD_AUDIT / group_name / sample["frame"]
                require(sha256(frame) == sample["frame_sha256"], f"method derivative {group_name}/{sample['frame']}")
                with Image.open(frame) as image:
                    require(image.mode == "RGB" and image.size == (1920, 1080), f"method frame shape {group_name}/{sample['frame']}")
        for variant, sheet in group["contact_sheets"].items():
            require(sha256(METHOD_AUDIT / group_name / sheet["path"]) == sheet["sha256"], f"method sheet {group_name}/{variant}")

    method_audit = load_json("qa/pass8_v8_color_vision_audit.json")
    require(method_audit["source_receipt_sha256"] == sha256(ROOT / method_audit["source_receipt"]), "method audit receipt pin")
    human = method_audit["human_visual_review"]
    require(human["sealed_v8_result_held"] == "7/7_ALL_FIVE_VARIANTS", "sealed visual badge")
    require(human["sealed_v8_hue_only_semantic_distinctions"] == 0, "sealed hue-only")
    require(human["caption_safe_scene_specific_gate_lines"] == "7/7_ALL_FIVE_VARIANTS", "caption visual gates")
    require(human["caption_safe_result_held"] == "7/7_ALL_FIVE_VARIANTS", "caption visual badges")
    require(human["caption_safe_hue_only_semantic_distinctions"] == 0, "caption hue-only")
    require(human["caption_safe_overlap_or_ambiguity"] == 0, "caption ambiguity")
    caption_aggregates = method_audit["groups"]["pass7_caption_safe"]["aggregates"]
    for variant in VARIANTS:
        row = caption_aggregates[variant]
        require(row["mean_gate_line_token_retention_vs_color"] == 1.0, f"caption gate retention {variant}")
        require(row["result_held_badge_ocr_count"] == 7, f"caption badge OCR {variant}")
        require(row["scene_specific_gate_ocr_count"] == 7, f"caption gate OCR {variant}")
        require(row["mean_edge_recall_vs_color_1px_tolerance"] == 1.0, f"caption edge {variant}")
    require(caption_aggregates["grayscale_bt709"]["mean_full_token_retention_vs_color"] == 0.952297, "caption grayscale full")
    sealed_gray = method_audit["groups"]["sealed_v8"]["aggregates"]["grayscale_bt709"]
    require(sealed_gray["mean_full_token_retention_vs_color"] == 0.962894, "sealed grayscale full")
    require(sealed_gray["result_held_badge_ocr_count"] == 7, "sealed grayscale badge OCR")

    guard = load_json("REDUNDANT_ENCODING_GUARD_PASS8.json")
    require(guard["status"] == "PROPOSAL_ONLY_INTEGRATION_GUARD_NOT_V9_NOT_A_CANDIDATE", "guard status")
    require(guard["proposed_integration_guard"]["pixel_change_requested"] is False, "guard pixel request")
    require(guard["base"]["sealed_v8_modified"] is False and guard["base"]["v9_created"] is False, "guard v8 custody")
    require(guard["method_only_evidence"]["sealed_v8"]["hue_only_semantic_distinctions"] == 0, "guard sealed hue")
    require(guard["method_only_evidence"]["pass7_caption_safe_proof"]["hue_only_semantic_distinctions"] == 0, "guard caption hue")
    require(guard["science_boundary"]["video_reportable_now"] is False, "guard reportability")
    require(guard["science_boundary"]["does_not_authorize_result"] is True, "guard result authorization")

    packet = load_json("BLOCKER_PACKET_PASS8.json")
    require(packet["video_reportable_now"] is False, "packet reportability")
    require(packet["candidate"]["sha256"] == CANDIDATE_SHA, "packet candidate")
    require(packet["representation_correction"]["v9_created"] is False, "packet v9")
    require(packet["pass8_encoded_audit"]["held_critical_structural_gate_count"].startswith("0/5"), "packet gates")
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
    require(extraction_time < packet_time < snapshot_time, "pass8 chronology")

    status = load_json("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS8_V1", "status phase")
    require(status["video_reportable_now"] is False, "status reportability")
    receipt_text = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    require("SPIN_WORKER_YUI_DEEPENING_PASS8_COMPLETE" in receipt_text, "receipt marker")
    require(snapshot["snapshot_id"] in receipt_text, "receipt snapshot")
    integrator = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    require(snapshot["snapshot_id"] in integrator, "integrator snapshot")
    require("hue alone" in integrator and "grayscale" in integrator, "integrator redundant encoding")

    media = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.casefold()
        in {".mp4", ".mp3", ".wav", ".aac", ".m4a", ".mov", ".webm"}
    ]
    require(not media, f"worker media outputs present: {media}")
    print(
        "PASS pass8 snapshot/candidate/80-color-vision-frames/hierarchy/"
        "70-method-derivatives/redundant-encoding/source-blockers/status/no-media"
    )


if __name__ == "__main__":
    main()
