#!/usr/bin/env python3
"""Verify pass-24 compound color/minimum-scale/recompression packet."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT.parent.parent
REPO = HANDOFF.parents[2]
SNAPSHOT = ROOT / "qa/pass24_review_snapshot_v1.json"
CANDIDATE_RECEIPT = ROOT / "qa/pass24_color_minimum_scale_recompression_audit/extraction_receipt.json"
METHOD_RECEIPT = ROOT / "qa/pass24_v8_color_minimum_scale_recompression/receipt.json"
AUDIT = ROOT / "qa/pass24_color_minimum_scale_recompression_quantitative_audit.json"
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
VARIANTS = [
    "color_360p_q60_420",
    "grayscale_bt709_then_360p_q60_420",
    "protanopia_machado100_then_360p_q60_420",
    "deuteranopia_machado100_then_360p_q60_420",
    "tritanopia_machado100_then_360p_q60_420",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise AssertionError(f"not object: {path}")
    return value


def resolve_snapshot_path(value: str) -> Path:
    if value.startswith("../../"):
        return ROOT / value
    return ROOT / value


def verify_authority_and_custody(snapshot: dict[str, Any]) -> None:
    assert snapshot["status"] == "IMMUTABLE_REVIEW_SNAPSHOT"
    assert snapshot["deepening_pass"] == 24
    for record in snapshot["authority"].values():
        path = resolve_snapshot_path(record["path"])
        assert path.is_file(), path
        assert sha(path) == record["sha256"], f"authority {path}"
    for key in ["source_freeze", "storyboard_proposal", "sealed_v8_render_receipt", "prior_pass_snapshot"]:
        record = snapshot["custody"][key]
        path = ROOT / record["path"]
        assert path.is_file(), path
        assert sha(path) == record["sha256"], f"custody {path}"
    assert snapshot["custody"]["source_freeze"]["modified"] is False
    assert snapshot["custody"]["storyboard_proposal"]["iteration"] == "v8"
    candidate = snapshot["custody"]["preserved_failed_candidate"]
    assert candidate["media_sha256"] == EXPECTED_CANDIDATE
    assert candidate["modified"] is False and candidate["re_dispatched"] is False


def verify_snapshot_evidence(snapshot: dict[str, Any]) -> None:
    for record in snapshot["evidence"].values():
        path = ROOT / record["path"]
        assert path.is_file(), path
        assert sha(path) == record["sha256"], f"evidence {path}"


def verify_candidate(receipt: dict[str, Any], audit: dict[str, Any]) -> None:
    assert receipt["deepening_pass"] == 24
    assert receipt["candidate_sha256"] == EXPECTED_CANDIDATE
    assert receipt["candidate_modified"] is False
    assert receipt["detected_cut_count"] == 15
    assert receipt["fresh_clean_match_count"] == 16
    assert receipt["baseline_pass23_pixel_match_count"] == 80
    assert receipt["scene_count"] == 16
    assert receipt["decoded_png_frame_count"] == 80
    assert receipt["jpeg_stream_count"] == 80
    assert receipt["represented_resolution"] == [640, 360]
    assert receipt["variant_order"] == VARIANTS
    assert receipt["transform_contract"]["jpeg_quality"] == 60
    assert receipt["transform_contract"]["jpeg_subsampling"] == 2
    assert receipt["transform_contract"]["jpeg_optimize"] is False
    assert receipt["transform_contract"]["jpeg_progressive"] is False
    for scene in receipt["scenes"]:
        assert scene["native_clean_byte_identical_to_pass23"] is True
        assert len(scene["samples"]) == 5
        for sample in scene["samples"]:
            assert sample["baseline_recomputed_pixel_exact"] is True
            jpeg = CANDIDATE_RECEIPT.parent / sample["jpeg"]
            frame = CANDIDATE_RECEIPT.parent / sample["frame"]
            assert jpeg.suffix.lower() == ".jpg" and frame.suffix.lower() == ".png"
            assert jpeg.stat().st_size == sample["jpeg_bytes"]
            assert sha(jpeg) == sample["jpeg_sha256"]
            assert sha(frame) == sample["frame_sha256"]
    candidate = audit["candidate"]
    for variant in VARIANTS:
        aggregate = candidate["aggregate"][variant]
        assert aggregate["structural_gate_scenes"] == 0
        assert aggregate["exact_jpeg_stream_scenes"] == 16
        assert aggregate["exact_decoded_rgb_scenes"] == 16
        assert candidate["held_critical"][variant]["structural_gate_scene_count"] == 0
    assert audit["representation_review"]["candidate_incremental_recompression_meaning_change"] is False
    assert audit["representation_review"]["candidate_compression_caused_overlap_clipping_or_ambiguity"] == 0


def verify_method(receipt: dict[str, Any], audit: dict[str, Any]) -> None:
    assert receipt["deepening_pass"] == 24
    assert receipt["variant_order"] == VARIANTS
    assert receipt["scene_count"] == 21
    assert receipt["decoded_png_frame_count"] == 105
    assert receipt["jpeg_stream_count"] == 105
    assert receipt["baseline_pass23_pixel_match_count"] == 105
    assert receipt["sealed_v8_modified"] is False
    assert receipt["pass7_proof_modified"] is False
    assert receipt["pass12_proof_modified"] is False
    assert receipt["v9_created"] is False
    for group_name, group in receipt["groups"].items():
        assert group["scene_count"] == 7
        assert group["decoded_png_frame_count"] == 35
        assert group["jpeg_stream_count"] == 35
        assert group["baseline_pass23_pixel_match_count"] == 35
        for scene in group["scenes"]:
            assert len(scene["samples"]) == 5
            for sample in scene["samples"]:
                assert sample["baseline_recomputed_pixel_exact"] is True
                jpeg = METHOD_RECEIPT.parent / group_name / sample["jpeg"]
                frame = METHOD_RECEIPT.parent / group_name / sample["frame"]
                assert jpeg.stat().st_size == sample["jpeg_bytes"]
                assert sha(jpeg) == sample["jpeg_sha256"]
                assert sha(frame) == sample["frame_sha256"]
    for group_name, group in audit["method"].items():
        for variant in VARIANTS:
            assert group["exact_jpeg_stream_scenes"][variant] == 7
            assert group["exact_decoded_rgb_scenes"][variant] == 7
        visual = group["human_visual_review"]
        assert visual["complete_result_held_badges"] == "7/7_ALL_FIVE_VARIANTS"
        assert visual["major_method_status_boundaries"] == "7/7_ALL_FIVE_VARIANTS"
        assert visual["hue_only_required_meaning"] == 0
        assert visual["compression_caused_overlap_clipping_or_ambiguity"] == 0
    pass12 = audit["method"]["pass12_sharpness_safe"]
    assert pass12["human_visual_review"]["exact_top_gates"] == "7/7_ALL_FIVE_VARIANTS"
    gates = pass12["mapped_gate_ocr_aid"]
    assert gates["color_360p_q60_420"]["passing_scenes"] == 7
    assert gates["grayscale_bt709_then_360p_q60_420"]["passing_scenes"] == 7
    assert gates["protanopia_machado100_then_360p_q60_420"]["passing_scenes"] == 7
    assert gates["deuteranopia_machado100_then_360p_q60_420"]["passing_scenes"] == 7
    assert gates["tritanopia_machado100_then_360p_q60_420"]["passing_scenes"] == 6
    miss = [row for row in gates["tritanopia_machado100_then_360p_q60_420"]["scenes"] if not row["passes_0_80"]]
    assert len(miss) == 1 and miss[0]["scene"] == 2 and miss[0]["similarity"] == 0.72973


def verify_boundary_and_sources(snapshot: dict[str, Any]) -> None:
    assert snapshot["representation_boundary"]["required_header"] == "GALAXY SPIN"
    assert snapshot["representation_boundary"]["forbidden_audience_topics_absent_from_method_frames"] is True
    assert snapshot["representation_boundary"]["science_adjudicated"] is False
    assert snapshot["blockers"]["video_reportable_now"] is False
    blocker = load(ROOT / "BLOCKER_PACKET_PASS24.json")
    assert blocker["video_reportable_now"] is False
    assert [item["status"] for item in blocker["blockers"]] == ["OPEN", "OPEN", "OPEN"]
    source_root = REPO / ".hermes/handoffs/spin-parity-census-20260805T1922K"
    expected = {
        "T4_PAIRED_FLIP.json": "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873",
        "AMENDMENT_A4_DRAFT.md": "8343c1947384cdb36355a0fe2f6965d4445ab013fda25e3f33b4d8300ce58974",
        "KUN_FRAME_REVIEW.md": "ccedf6846391a8f0661a88b2eec0ce21fbfd7c44ad16201080bb196f56d258e5",
    }
    for name, digest in expected.items():
        assert sha(source_root / name) == digest
    assert (source_root / "KUN_FRAME_REVIEW.md").read_text().rstrip().endswith("FRAME REVIEW: AGREES FRAME_UNSTATED")


def verify_safety(snapshot: dict[str, Any]) -> None:
    for key in ["tts_invoked", "audio_generated", "video_encoded", "published", "shared_or_public_assets_modified", "git_action"]:
        assert snapshot["safety"][key] is False
    assert snapshot["safety"]["writes_confined_to_worker_lane"] is True
    forbidden = {".mp4", ".mov", ".mkv", ".webm", ".mp3", ".wav", ".m4a", ".aac"}
    pass24_paths = [path for path in ROOT.rglob("*pass24*") if path.is_file() or path.is_dir()]
    media = [path for path in pass24_paths if path.is_file() and path.suffix.lower() in forbidden]
    assert not media, media


def verify_handoff() -> None:
    status = load(ROOT / "STATUS.json")
    assert status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS24_COMPLETE"
    assert status["phase"].startswith("SEALED_ISOLATED_DEEPENING_PASS24")
    assert status["video_reportable_now"] is False
    receipt = (ROOT / "LANE_RECEIPT.md").read_text()
    assert "SPIN_WORKER_YUI_DEEPENING_PASS24_COMPLETE" in receipt
    assert "PASS24_ENCODED_FRAME_AUDIT.md" in receipt
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
    assert "Final pass-24 custody and exact decision rule" in request
    static = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
    assert "Pass 24 compound color/minimum-scale/recompression QA" in static


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-only", action="store_true")
    args = parser.parse_args()
    snapshot = load(SNAPSHOT)
    candidate_receipt = load(CANDIDATE_RECEIPT)
    method_receipt = load(METHOD_RECEIPT)
    audit = load(AUDIT)
    verify_authority_and_custody(snapshot)
    verify_snapshot_evidence(snapshot)
    verify_candidate(candidate_receipt, audit)
    verify_method(method_receipt, audit)
    verify_boundary_and_sources(snapshot)
    verify_safety(snapshot)
    if not args.evidence_only:
        verify_handoff()
    suffix = "evidence-only" if args.evidence_only else "status-handoff"
    print(f"PASS pass24 snapshot/candidate/80png+80jpeg/method/105png+105jpeg/exact-bytes-and-pixels/color-minimum-scale-recompression-guard/source-blockers/{suffix}/no-audio-video")


if __name__ == "__main__":
    main()
