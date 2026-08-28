#!/usr/bin/env python3
"""Verify pass-11 recompression evidence, guard, blockers, custody, and closed gates."""

from __future__ import annotations

import hashlib
import io
import json
from datetime import datetime
from pathlib import Path
from typing import Any, NoReturn

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
EXPECTED_CANDIDATE_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_FREEZE_SHA = "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1"
EXPECTED_STORYBOARD_SHA = "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce"
EXPECTED_RENDER_RECEIPT_SHA = "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3"
EXPECTED_CONTACT_SHA = "5889dfcbcb7f24afe989411b127a5c30adb9e4685513058eca9d51cc0cf32056"
EXPECTED_PASS10_SNAPSHOT_SHA = "9539d6ec4364eef14f2a4ff6566a8779d6f3dfa22cc315958c46f919baef46ab"
EXPECTED_METHOD_RECEIPT_SHA = "ddd37746c2587fad44e26d791d031ebffc7f1544ea291a7ca7a1a561d94e45c9"
EXPECTED_AUDIT_SHA = "d83c6d93c0a0d4e06d6f9531ce01c2d3de28abb8c3d4aac073f8215a2ff62684"
EXPECTED_VARIANTS: dict[str, int | None] = {
    "clean": None,
    "jpeg_q85_420": 85,
    "jpeg_q60_420": 60,
    "jpeg_q35_420": 35,
    "jpeg_q20_420": 20,
}
EXPECTED_CUTS = [
    12.133333,
    26.366667,
    47.266667,
    60.466667,
    74.666667,
    88.066667,
    102.333333,
    116.333333,
    131.033333,
    148.033333,
    162.033333,
    179.733333,
    196.8,
    213.433333,
    233.866667,
]
PROHIBITED_SUFFIXES = {".mp4", ".mp3", ".wav", ".aac", ".m4a"}


def fail(message: str) -> NoReturn:
    raise SystemExit(f"FAIL: {message}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot load {path.relative_to(ROOT)}: {error}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def recompress(source: Path, quality: int) -> tuple[bytes, np.ndarray]:
    with Image.open(source) as opened:
        image = opened.convert("RGB")
        buffer = io.BytesIO()
        image.save(
            buffer,
            format="JPEG",
            quality=quality,
            subsampling=2,
            optimize=False,
            progressive=False,
        )
    jpeg_bytes = buffer.getvalue()
    with Image.open(io.BytesIO(jpeg_bytes)) as decoded:
        pixels = np.asarray(decoded.convert("RGB"), dtype=np.uint8)
    return jpeg_bytes, pixels


def image_pixels(path: Path) -> np.ndarray:
    with Image.open(path) as opened:
        require(opened.mode == "RGB", f"non-RGB frame {path.relative_to(ROOT)}")
        require(opened.size == (1920, 1080), f"wrong frame size {path.relative_to(ROOT)}")
        return np.asarray(opened, dtype=np.uint8)


def verify_candidate_receipt() -> dict[str, Any]:
    receipt_path = ROOT / "qa/pass11_recompression_audit/extraction_receipt.json"
    receipt = load_json(receipt_path)
    require(receipt["status"] == "QA_STATIC_PNG_DERIVATIVES_NOT_A_CANDIDATE", "candidate receipt status")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE_SHA, "receipt candidate hash")
    require(receipt["candidate_modified"] is False, "candidate marked modified")
    require(receipt["scene_count"] == 16, "candidate scene count")
    require(receipt["variant_count"] == 5, "candidate variant count")
    require(receipt["frame_count"] == 80, "candidate frame count")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "candidate cuts")
    require(receipt["cut_detection"]["exact_pass10_match"] is True, "pass10 cut match")
    require(receipt["clean_reproduction"] == "16/16 pass10 clean midpoint PNGs byte-identical", "clean reproduction")
    require(receipt["video_or_audio_created"] is False, "candidate receipt media flag")
    require(receipt["tts_invoked"] is False, "candidate receipt TTS flag")
    require(receipt["git_action"] is False, "candidate receipt Git flag")

    records = receipt["records"]
    require(isinstance(records, list) and len(records) == 80, "candidate records count")
    for record in records:
        scene = record["scene"]
        variant = record["variant"]
        require(isinstance(scene, int) and 1 <= scene <= 16, "candidate record scene")
        require(variant in EXPECTED_VARIANTS, "candidate record variant")
        quality = EXPECTED_VARIANTS[variant]
        require(record["quality"] == quality, f"candidate quality {scene} {variant}")
        require(record["subsampling"] == (None if quality is None else "4:2:0"), f"candidate subsampling {scene} {variant}")
        frame_path = ROOT / record["path"]
        require(frame_path.is_file(), f"missing candidate frame {record['path']}")
        require(sha256(frame_path) == record["png_sha256"], f"candidate frame hash {scene} {variant}")
        pixels = image_pixels(frame_path)
        clean_path = ROOT / f"qa/pass11_recompression_audit/frames/clean/scene_{scene:02d}.png"
        if quality is None:
            prior = ROOT / f"qa/pass10_ambient_contrast_audit/frames/scene_{scene:02d}_clean.png"
            require(sha256(frame_path) == sha256(prior), f"candidate clean pass10 reproduction {scene}")
            require(record["jpeg_sha256"] is None and record["jpeg_bytes"] is None, "clean JPEG metadata")
        else:
            jpeg_bytes, expected_pixels = recompress(clean_path, quality)
            require(hashlib.sha256(jpeg_bytes).hexdigest() == record["jpeg_sha256"], f"candidate JPEG stream {scene} {variant}")
            require(len(jpeg_bytes) == record["jpeg_bytes"], f"candidate JPEG size {scene} {variant}")
            require(np.array_equal(pixels, expected_pixels), f"candidate decoded pixels {scene} {variant}")
    return receipt


def verify_method_receipt() -> dict[str, Any]:
    receipt_path = ROOT / "qa/pass11_v8_recompression/receipt.json"
    require(sha256(receipt_path) == EXPECTED_METHOD_RECEIPT_SHA, "method receipt closing hash")
    receipt = load_json(receipt_path)
    require(receipt["status"] == "QA_STATIC_DERIVATIVES_ONLY_NOT_V9_NOT_A_CANDIDATE", "method status")
    require(receipt["deepening_pass"] == 11, "method pass")
    require(receipt["variant_order"] == list(EXPECTED_VARIANTS), "method variants")
    require(receipt["scene_count"] == 14 and receipt["frame_count"] == 70, "method census")
    require(receipt["sealed_v8_modified"] is False, "sealed v8 method flag")
    require(receipt["pass7_mockup_modified"] is False, "pass7 method flag")
    require(receipt["v9_created"] is False, "method v9 flag")
    require(receipt["tts_invoked"] is False and receipt["video_encoded"] is False, "method media flags")
    for group_name in ["sealed_v8", "pass7_caption_safe"]:
        group = receipt["groups"][group_name]
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"method group census {group_name}")
        for scene_record in group["scenes"]:
            source = ROOT / scene_record["source"]
            require(sha256(source) == scene_record["source_sha256"], f"method source hash {group_name}")
            require(scene_record["clean_copy_sha256_match"] is True, f"method clean copy flag {group_name}")
            for sample in scene_record["samples"]:
                variant = sample["variant"]
                quality = EXPECTED_VARIANTS[variant]
                require(sample["quality"] == quality, f"method quality {group_name} {variant}")
                frame_path = ROOT / "qa/pass11_v8_recompression" / group_name / sample["frame"]
                require(sha256(frame_path) == sample["frame_sha256"], f"method frame hash {group_name} {variant}")
                pixels = image_pixels(frame_path)
                if quality is None:
                    require(sha256(frame_path) == sha256(source), f"method clean source identity {group_name}")
                else:
                    jpeg_bytes, expected_pixels = recompress(source, quality)
                    require(hashlib.sha256(jpeg_bytes).hexdigest() == sample["jpeg_sha256"], f"method JPEG stream {group_name} {variant}")
                    require(len(jpeg_bytes) == sample["jpeg_bytes"], f"method JPEG size {group_name} {variant}")
                    require(np.array_equal(pixels, expected_pixels), f"method decoded pixels {group_name} {variant}")
    return receipt


def verify_snapshot_and_metrics() -> None:
    snapshot_path = ROOT / "qa/pass11_review_snapshot_v1.json"
    snapshot = load_json(snapshot_path)
    require(snapshot["snapshot_status"] == "IMMUTABLE_REVIEW_SNAPSHOT", "snapshot status")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass11-review-v1-20260808T073740K", "snapshot id")
    require(snapshot["supersedes"]["sha256"] == EXPECTED_PASS10_SNAPSHOT_SHA, "snapshot supersession hash")
    require(sha256(ROOT / snapshot["supersedes"]["path"]) == EXPECTED_PASS10_SNAPSHOT_SHA, "pass10 snapshot custody")
    for artifact in snapshot["pinned_artifacts"]:
        path = ROOT / artifact["path"]
        require(path.is_file(), f"missing pinned artifact {artifact['path']}")
        require(sha256(path) == artifact["sha256"], f"pinned artifact hash {artifact['path']}")

    audit_path = ROOT / "qa/pass11_recompression_quantitative_audit.json"
    require(sha256(audit_path) == EXPECTED_AUDIT_SHA, "quantitative audit closing hash")
    audit = load_json(audit_path)
    require(audit["deepening_pass"] == 11, "audit pass")
    require(audit["candidate"]["frame_count"] == 80, "audit candidate census")
    require(audit["candidate"]["clean_midpoints_byte_identical_to_pass10_clean"] == 16, "audit clean reproduction")
    candidate_q60 = audit["candidate"]["aggregates"]["jpeg_q60_420"]
    require(candidate_q60["mean_headline_token_recall_vs_clean"] == 0.99569, "candidate q60 headline")
    require(candidate_q60["mean_full_token_recall_vs_clean"] == 0.970333, "candidate q60 full")
    require(candidate_q60["mean_numeric_token_recall_vs_clean"] == 0.958996, "candidate q60 numeric")
    require(candidate_q60["structural_gate_scene_count"] == 0, "candidate q60 structural gate")
    critical_q60 = audit["candidate"]["held_critical_aggregates"]["jpeg_q60_420"]
    require(critical_q60["mean_headline_token_recall_vs_clean"] == 1.0, "critical q60 headline")
    require(critical_q60["structural_gate_scene_count"] == 0, "critical q60 gate")
    sealed = audit["method_groups"]["sealed_v8"]["aggregates"]["jpeg_q60_420"]
    caption = audit["method_groups"]["pass7_caption_safe"]["aggregates"]["jpeg_q60_420"]
    require(sealed["mean_full_token_recall_vs_clean"] == 0.973906, "sealed q60 full")
    require(caption["scene_specific_gate_count"] == 7, "caption q60 gates")
    require(audit["human_visual_review"]["sealed_v8_result_held_text_visual"]["jpeg_q60_420"] == "7/7", "sealed visual badges")
    require(audit["human_visual_review"]["pass7_caption_safe_specific_gate_lines_visual"]["jpeg_q20_420"] == "7/7", "caption severe visual gates")


def verify_guard_blockers_and_status(candidate_receipt: dict[str, Any]) -> None:
    guard = load_json(ROOT / "RECOMPRESSION_RESILIENCE_GUARD_PASS11.json")
    blocker = load_json(ROOT / "BLOCKER_PACKET_PASS11.json")
    status = load_json(ROOT / "STATUS.json")
    receipt_text = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    integrator_text = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    static_text = (ROOT / "STATIC_PROPOSAL_QA.md").read_text(encoding="utf-8")

    require(guard["status"] == "PROPOSAL_ONLY_INTEGRATION_GUARD_NOT_V9_NOT_A_CANDIDATE", "guard status")
    require(guard["operational_acceptance_floor"]["variant"] == "jpeg_q60_420", "guard operational variant")
    require(guard["disposition"]["new_pixel_change_requested"] is False, "guard pixel disposition")
    require(guard["disposition"]["sealed_v8_modified"] is False, "guard sealed v8 flag")
    require(guard["disposition"]["v9_created"] is False, "guard v9 flag")
    require(guard["science_boundary"]["video_reportable_now"] is False, "guard reportability")

    require(blocker["candidate"]["sha256"] == EXPECTED_CANDIDATE_SHA, "blocker candidate")
    require(blocker["candidate"]["preserved_failed_candidate"] is True, "blocker candidate preservation")
    require(blocker["science_blocker_1"]["valid_post_run_independent_review_records"] == 0, "A3.8 blocker")
    require(blocker["science_blocker_2"]["source"]["exact_terminal_status"] == "FRAME REVIEW: AGREES FRAME_UNSTATED", "frame blocker")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    require(blocker["scientific_adjudication_performed"] is False, "blocker adjudication")

    extraction_time = parse_time(candidate_receipt["created_at"])
    packet_time = parse_time(blocker["checked_at"])
    snapshot_time = parse_time(load_json(ROOT / "qa/pass11_review_snapshot_v1.json")["created_at"])
    require(extraction_time < packet_time < snapshot_time, "pass11 chronology")

    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS11_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS11_COMPLETE", "status marker")
    require(status["video_reportable_now"] is False, "status reportability")
    require("pass11_exact_snapshot_v1" in status["quality_gates"], "status pass11 snapshot")
    require("SPIN_WORKER_YUI_DEEPENING_PASS11_COMPLETE" in receipt_text, "lane receipt marker")
    require("Isolated deepening pass 11" in receipt_text, "lane receipt pass11 section")
    require("JPEG q60" in integrator_text, "integrator pass11 request")
    require("Pass-11 recompression" in static_text, "static pass11 section")


def verify_custody_and_closed_gates() -> None:
    require(sha256(CANDIDATE) == EXPECTED_CANDIDATE_SHA, "candidate closing hash")
    require(sha256(ROOT / "SOURCE_STATUS_FREEZE.json") == EXPECTED_FREEZE_SHA, "source freeze hash")
    require(sha256(ROOT / "STORYBOARD_PROPOSAL.json") == EXPECTED_STORYBOARD_SHA, "storyboard hash")
    require(sha256(ROOT / "proposal_frames/v8/render_receipt.json") == EXPECTED_RENDER_RECEIPT_SHA, "render receipt hash")
    require(sha256(ROOT / "proposal_frames/v8/contact_sheet.png") == EXPECTED_CONTACT_SHA, "contact sheet hash")
    require(not (ROOT / "proposal_frames/v9").exists(), "v9 exists")
    prohibited = [path for path in ROOT.rglob("*") if path.is_file() and path.suffix.casefold() in PROHIBITED_SUFFIXES]
    require(not prohibited, f"prohibited media outputs: {prohibited}")

    blocker = load_json(ROOT / "BLOCKER_PACKET_PASS11.json")
    for blocker_key in ["science_blocker_1", "science_blocker_2"]:
        source = blocker[blocker_key]["frozen_quarantined_artifact"] if blocker_key == "science_blocker_1" else blocker[blocker_key]["source"]
        require(sha256(Path(source["path"])) == source["sha256"], f"source blocker custody {blocker_key}")
    review_contract = blocker["science_blocker_1"]["review_contract"]
    require(sha256(Path(review_contract["path"])) == review_contract["sha256"], "review contract custody")


def main() -> None:
    verify_custody_and_closed_gates()
    candidate_receipt = verify_candidate_receipt()
    verify_method_receipt()
    verify_snapshot_and_metrics()
    verify_guard_blockers_and_status(candidate_receipt)
    print(
        "PASS pass11 snapshot/candidate/80-recompression-frames/hierarchy/"
        "70-method-derivatives/recompression-guard/source-blockers/status/no-media"
    )


if __name__ == "__main__":
    main()
