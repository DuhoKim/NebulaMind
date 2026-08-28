#!/usr/bin/env python3
"""Verify pass-23 minimum-scale color-redundancy evidence and handoff."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT.parent.parent
REPO = HANDOFF.parents[2]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
SOURCE_FREEZE = "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1"
VARIANTS = [
    "color_360p",
    "grayscale_bt709_then_360p",
    "protanopia_machado100_then_360p",
    "deuteranopia_machado100_then_360p",
    "tritanopia_machado100_then_360p",
]
MATRICES = {
    "protanopia_machado100": np.array(
        [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]], dtype=np.float64
    ),
    "deuteranopia_machado100": np.array(
        [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]], dtype=np.float64
    ),
    "tritanopia_machado100": np.array(
        [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]], dtype=np.float64
    ),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def require(condition: bool, label: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL {label}")


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, 1.0)
    return np.where(clipped <= 0.0031308, 12.92 * clipped, 1.055 * clipped ** (1.0 / 2.4) - 0.055)


def recompute(source: Path, variant: str) -> np.ndarray:
    with Image.open(source) as opened:
        native = opened.convert("RGB")
        if variant == "color_360p":
            transformed = native
        else:
            label = variant.removesuffix("_then_360p")
            rgb = np.asarray(native, dtype=np.float64) / 255.0
            linear = srgb_to_linear(rgb)
            if label == "grayscale_bt709":
                luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
                transformed_linear = np.repeat(luminance[:, :, None], 3, axis=2)
            else:
                transformed_linear = np.einsum("...c,rc->...r", linear, MATRICES[label])
            transformed = Image.fromarray(np.rint(np.clip(linear_to_srgb(transformed_linear), 0.0, 1.0) * 255.0).astype(np.uint8))
        return np.asarray(transformed.resize((640, 360), Image.Resampling.LANCZOS), dtype=np.uint8)


def verify_authority(snapshot: dict[str, Any]) -> None:
    require(sha(HANDOFF / "HWAO_WEEKEND_ORDER.md") == "ac5d35314a3af78ab2214b62105fa74afb616862aeeb2d09faa1dd6eb1c84710", "authority order")
    require(sha(HANDOFF / "COORDINATION_UPDATE.md") == "2d64667f8ab95349b344c9098a4f2b8f675c71d53d1cc132a780e0ac699fde1f", "authority coordination")
    require(sha(HANDOFF / "lanes/spin/BRIEF.md") == "af91d7a84ddfce470500189546cb7b8d109d4eaaf2c3451f468807c0b5cd4aec", "authority brief")
    require(sha(ROOT / "SOURCE_STATUS_FREEZE.json") == SOURCE_FREEZE, "source freeze")
    require(sha(ROOT / "STORYBOARD_PROPOSAL.json") == "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce", "storyboard custody")
    require(sha(ROOT / "proposal_frames/v8/render_receipt.json") == "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3", "v8 receipt custody")
    require(sha(ROOT / "qa/pass22_review_snapshot_v1.json") == snapshot["custody"]["prior_pass_snapshot"]["sha256"], "prior snapshot")
    require(sha(CANDIDATE) == EXPECTED_CANDIDATE, "candidate hash")


def verify_candidate(receipt: dict[str, Any]) -> None:
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE, "candidate receipt hash")
    require(receipt["created_at"] == "2026-08-08T13:28:02+09:00", "candidate chronology")
    require(receipt["detected_cut_count"] == 15 and receipt["scene_count"] == 16, "candidate census")
    require(receipt["fresh_clean_match_count"] == 16, "clean custody")
    require(receipt["frame_count"] == 80 and receipt["variant_order"] == VARIANTS, "candidate derivative census")
    require(receipt["represented_resolution"] == [640, 360], "represented dimensions")
    exact = 0
    frame_count = 0
    for scene in receipt["scenes"]:
        source = ROOT / "qa/pass23_minimum_scale_color_vision_audit" / scene["native_clean"]
        require(sha(source) == scene["native_clean_sha256"] == scene["previous_clean_sha256"], "candidate clean hash")
        require(scene["native_clean_byte_identical_to_pass22"] is True, "candidate clean match")
        for sample in scene["samples"]:
            frame = ROOT / "qa/pass23_minimum_scale_color_vision_audit" / sample["frame"]
            require(sha(frame) == sample["frame_sha256"], "candidate frame hash")
            with Image.open(frame) as image:
                require(image.mode == "RGB" and image.size == (640, 360), "candidate frame mode/dimensions")
                stored = np.asarray(image.convert("RGB"), dtype=np.uint8)
            require(np.array_equal(stored, recompute(source, sample["variant"])), "candidate exact transform")
            exact += 1
            frame_count += 1
    require(exact == frame_count == 80, "candidate exact total")
    require(all(sheet["width"] == 2560 and sheet["height"] == 1552 for sheet in receipt["contact_sheets"].values()), "candidate sheets dimensions")


def verify_method(receipt: dict[str, Any]) -> None:
    require(receipt["status"] == "QA_STATIC_DERIVATIVES_ONLY_NOT_V9_NOT_A_CANDIDATE", "method status")
    require(receipt["variant_order"] == VARIANTS and receipt["scene_count"] == 21 and receipt["frame_count"] == 105, "method census")
    require(set(receipt["groups"]) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method groups")
    total = 0
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, "method group census")
        for scene in group["scenes"]:
            source = ROOT / scene["source"]
            require(sha(source) == scene["source_sha256"], "method source hash")
            for sample in scene["samples"]:
                frame = ROOT / "qa/pass23_v8_minimum_scale_color_vision" / group_name / sample["frame"]
                require(sha(frame) == sample["frame_sha256"], "method frame hash")
                with Image.open(frame) as image:
                    require(image.mode == "RGB" and image.size == (640, 360), "method frame dimensions")
                    stored = np.asarray(image.convert("RGB"), dtype=np.uint8)
                require(np.array_equal(stored, recompute(source, sample["variant"])), "method exact transform")
                total += 1
        require(all(sheet["width"] == 1280 and sheet["height"] == 1552 for sheet in group["contact_sheets"].values()), "method sheets dimensions")
    require(total == 105, "method exact total")
    for key in ["sealed_v8_modified", "pass7_proof_modified", "pass12_proof_modified", "v9_created", "tts_invoked", "audio_generated", "video_encoded", "shared_or_public_assets_modified", "git_action"]:
        require(receipt[key] is False, f"method safety {key}")


def verify_audit(audit: dict[str, Any]) -> None:
    require(audit["candidate_sha256"] == EXPECTED_CANDIDATE, "audit candidate")
    aggregates = audit["candidate"]["aggregate"]
    expected = {
        "grayscale_bt709_then_360p": (0.988533, 0.930353, 0.732388, 0.828125, 0.0),
        "protanopia_machado100_then_360p": (0.988533, 0.939875, 0.759153, 0.848958, 0.818706),
        "deuteranopia_machado100_then_360p": (0.985408, 0.954081, 0.851875, 0.880208, 0.907247),
        "tritanopia_machado100_then_360p": (0.988533, 0.94753, 0.787202, 0.854167, 1.065977),
    }
    for variant, values in expected.items():
        row = aggregates[variant]
        actual = (
            row["mean_headline_recall_vs_color_360p"], row["mean_full_text_recall_vs_color_360p"],
            row["mean_lower_support_recall_vs_color_360p"], row["mean_numeric_recall_vs_color_360p"],
            row["mean_chroma_retention_on_color_saturated_pixels"],
        )
        require(actual == values, f"audit aggregate {variant}")
        require(row["structural_gate_scenes"] == 0 and row["exact_transform_match_scenes"] == 16, f"audit gate/exact {variant}")
        require(audit["candidate"]["held_critical"][variant]["structural_gate_scene_count"] == 0, f"critical gates {variant}")
    for group_name, group in audit["method"].items():
        require(all(value == 7 for value in group["exact_transform_match_scenes"].values()), f"method audit exact {group_name}")
        require(group["human_visual_review"]["hue_only_required_meaning"] == 0, f"method hue only {group_name}")
    proof = audit["method"]["pass12_sharpness_safe"]["mapped_gate_ocr_aid"]
    require(all(row["passing_scenes"] == 7 and row["mean_similarity"] == 1.0 for row in proof.values()), "proof mapped gates")
    require(audit["representation_review"]["science_adjudicated"] is False, "no science adjudication")


def verify_packets(snapshot: dict[str, Any]) -> None:
    evidence = snapshot["evidence"]
    for key, row in evidence.items():
        require(sha(ROOT / row["path"]) == row["sha256"], f"snapshot evidence {key}")
    guard = load(ROOT / "MINIMUM_SCALE_COLOR_REDUNDANCY_GUARD_PASS23.json")
    require(guard["status"] == "PROPOSAL_ONLY_INTEGRATION_GUARD_NOT_V9_NOT_A_CANDIDATE", "guard status")
    require(guard["pixel_action"]["new_pixel_or_copy_correction_requested"] is False, "guard no correction")
    require(guard["evidence"]["method"]["pass12_sharpness_safe"]["hue_only_required_meaning"] == 0, "guard hue redundancy")
    blocker = load(ROOT / "BLOCKER_PACKET_PASS23.json")
    require([row["status"] for row in blocker["blockers"]] == ["OPEN", "OPEN", "OPEN"], "blocker open states")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    kun = REPO / ".hermes/handoffs/spin-parity-census-20260805T1922K/KUN_FRAME_REVIEW.md"
    require(sha(kun) == "ccedf6846391a8f0661a88b2eec0ce21fbfd7c44ad16201080bb196f56d258e5", "KUN hash")
    require("FRAME REVIEW: AGREES FRAME_UNSTATED" in kun.read_text(), "KUN terminal status")


def verify_no_media() -> None:
    forbidden = {".mp4", ".mp3", ".wav", ".m4a", ".aac"}
    paths = list((ROOT / "qa/pass23_minimum_scale_color_vision_audit").rglob("*")) + list((ROOT / "qa/pass23_v8_minimum_scale_color_vision").rglob("*"))
    require(not any(path.is_file() and path.suffix.lower() in forbidden for path in paths), "no prohibited media")


def verify_handoff() -> None:
    status = load(ROOT / "STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS23_MINIMUM_SCALE_COLOR_REDUNDANCY_GUARD_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS23_COMPLETE", "status marker")
    require(status["video_reportable_now"] is False, "status reportability")
    receipt = (ROOT / "LANE_RECEIPT.md").read_text()
    require("SPIN_WORKER_YUI_DEEPENING_PASS23_COMPLETE" in receipt, "lane receipt marker")
    require("## Exact Hwao action requested after pass 23" in receipt, "lane action")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
    require("Final pass-23 custody" in request, "integrator request")
    static = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
    require("Pass-23 minimum-scale color-redundancy guard" in static, "static QA")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-only", action="store_true")
    args = parser.parse_args()
    snapshot = load(ROOT / "qa/pass23_review_snapshot_v1.json")
    require(snapshot["status"] == "IMMUTABLE_REVIEW_SNAPSHOT" and snapshot["deepening_pass"] == 23, "snapshot identity")
    verify_authority(snapshot)
    candidate_receipt = load(ROOT / "qa/pass23_minimum_scale_color_vision_audit/extraction_receipt.json")
    method_receipt = load(ROOT / "qa/pass23_v8_minimum_scale_color_vision/receipt.json")
    audit = load(ROOT / "qa/pass23_minimum_scale_color_vision_quantitative_audit.json")
    verify_candidate(candidate_receipt)
    verify_method(method_receipt)
    verify_audit(audit)
    verify_packets(snapshot)
    verify_no_media()
    if not args.evidence_only:
        verify_handoff()
    suffix = "evidence-only" if args.evidence_only else "status-handoff"
    print(f"PASS pass23 snapshot/candidate/80-compound-frames/hierarchy/105-method-derivatives/minimum-scale-color-redundancy-guard/source-blockers/{suffix}/no-media")


if __name__ == "__main__":
    main()
