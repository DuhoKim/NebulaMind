#!/usr/bin/env python3
"""Verify pass-14 shadow-floor evidence, guard, blockers, custody, and handoff."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_CANDIDATE_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_FREEZE_SHA = "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
VARIANTS: dict[str, int | None] = {
    "clean": None,
    "shadow_floor_08": 8,
    "shadow_floor_16": 16,
    "shadow_floor_32": 32,
    "shadow_floor_48": 48,
}
EXPECTED_HASHES = {
    "SOURCE_STATUS_FREEZE.json": "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1",
    "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
    "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
    "proposal_frames/v8/contact_sheet.png": "5889dfcbcb7f24afe989411b127a5c30adb9e4685513058eca9d51cc0cf32056",
    "qa/pass13_review_snapshot_v1.json": "de5c5c79a164576af1ff83114bd976dda4e91ebabae674d9b0fb98b2270d1803",
    "SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json": "1312ea54aa860473ff57e3c47e8305ecca8630ba1f6a998a6e02d9aea9999422",
    "qa/pass12_sharpness_safe_mockup/receipt.json": "35f526a60b053f8c203278b3c205c1e0145f9a6dcd6da309541eb57b6399e92c",
    "qa/extract_pass14_shadow_floor_frames.py": "78ec23b1ecdb591b6d5b49b12c7946bdd20ca33760b1a157991c7f7759d0ffb0",
    "qa/pass14_shadow_floor_audit/extraction_receipt.json": "b5d897cfbff6153204f8efa71540afdd6b1cee94c0c03050386309b4e35e8c36",
    "qa/pass14_shadow_floor_audit/contact_sheet_shadow_floor_16.png": "2028ae8b7cca25a81d7d47e53bdc090d0b12d5f5895a749473f4903f706c32f5",
    "qa/pass14_shadow_floor_audit/contact_sheet_shadow_floor_32.png": "95bd3aa72d41a3f55af9a583276fb56235ac07cc969ed5ae815631b3c8651dc1",
    "qa/pass14_shadow_floor_audit/contact_sheet_shadow_floor_48.png": "b4c32d96ed98365b801c7617a403c91ac51165f89d7f8464b040d8cb9fd7632d",
    "qa/build_pass14_v8_shadow_floor.py": "41241146794720b6619364e5e4a73f73c185bcba29f3ad277c229cbc08e4bf52",
    "qa/pass14_v8_shadow_floor/receipt.json": "5e1b5c2ced02c2e081ecf7c49c9cdc4946844cbe6fd9e674288dfd3e913cd0f4",
    "qa/audit_pass14_shadow_floor.py": "492269b45b30d6e751f149a2628bfb13dce9039f8e87b9002cbc9b77fff574ae",
    "qa/pass14_shadow_floor_quantitative_audit.json": "2917cafd30a68a2c7fa89f13911721867b64949ee6b7f27be9cf2b5659c5c022",
    "DARK_TONE_RESILIENCE_GUARD_PASS14.json": "e25d00e204f41406d0d6da33f01f5447d2ceda74c2f5b4385c1919bf2f819e12",
    "PASS14_ENCODED_FRAME_AUDIT.md": "81bf052493d6ba469733afc232d2f9debab4903b44eec84c81dbe09c23b943ed",
    "BLOCKER_PACKET_PASS14.json": "b2816a4c55fe89dba8650277e91ac265e2d41912da8e1a42cd8efe242956c627",
    "qa/pass14_review_snapshot_v1.json": "3edbfe6a46c18821f388c0556131c05bc97f4334fc99dcd55cec64062da0b63f",
}
PROHIBITED_MEDIA = {".mp4", ".mp3", ".wav", ".aac", ".m4a", ".mov", ".webm"}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(data, dict), f"object expected: {path}")
    return data


def rgb(path: Path) -> np.ndarray:
    with Image.open(path).convert("RGB") as image:
        require(image.size == (1920, 1080), f"frame dimensions: {path}")
        return np.asarray(image, dtype=np.uint8)


def shadow_floor(values: np.ndarray, floor: int) -> np.ndarray:
    data = values.astype(np.uint32)
    lum = ((54 * data[:, :, 0] + 183 * data[:, :, 1] + 19 * data[:, :, 2] + 128) // 256).astype(np.uint32)
    numerator = np.maximum(lum.astype(np.int32) - floor, 0).astype(np.uint32) * 255
    remapped = (numerator + (255 - floor) // 2) // (255 - floor)
    output = np.zeros_like(values, dtype=np.uint8)
    nonzero = lum > 0
    for channel in range(3):
        scaled = np.zeros_like(lum, dtype=np.uint32)
        scaled[nonzero] = (data[:, :, channel][nonzero] * remapped[nonzero] + lum[nonzero] // 2) // lum[nonzero]
        output[:, :, channel] = np.clip(scaled, 0, 255).astype(np.uint8)
    return output


def approx(actual: Any, expected: float, message: str) -> None:
    require(isinstance(actual, (int, float)), f"number expected: {message}")
    require(abs(float(actual) - expected) <= 0.0000005, message)


def verify_pinned_hashes() -> None:
    for rel, expected in EXPECTED_HASHES.items():
        path = ROOT / rel
        require(path.is_file(), f"missing pinned artifact: {rel}")
        require(sha256(path) == expected, f"pinned hash: {rel}")
    require(CANDIDATE.is_file(), "candidate missing")
    require(sha256(CANDIDATE) == EXPECTED_CANDIDATE_SHA, "candidate hash")


def verify_candidate_frames() -> None:
    receipt = load_json(ROOT / "qa/pass14_shadow_floor_audit/extraction_receipt.json")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE_SHA, "extraction candidate")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "fresh cut list")
    require(receipt["cut_detection"]["exact_pass13_match"] is True, "fresh cut reproduction")
    require(receipt["fresh_clean_match"] == "16/16_PASS13_BYTE_IDENTICAL", "clean reproduction")
    require(receipt["scene_count"] == 16 and receipt["variant_count"] == 5 and receipt["frame_count"] == 80, "candidate census")
    require(receipt["variant_order"] == list(VARIANTS), "candidate variants")
    records = receipt["records"]
    require(isinstance(records, list) and len(records) == 80, "candidate records")
    by_scene: dict[int, dict[str, dict[str, Any]]] = {}
    for record in records:
        scene = int(record["scene"])
        variant = record["variant"]
        require(1 <= scene <= 16 and variant in VARIANTS, "candidate record identity")
        path = ROOT / record["path"]
        require(path.is_file() and sha256(path) == record["png_sha256"], f"candidate frame hash {scene} {variant}")
        require(record["luma_floor_code_value"] == VARIANTS[variant], "candidate floor metadata")
        by_scene.setdefault(scene, {})[variant] = record
    require(set(by_scene) == set(range(1, 17)), "candidate scenes")
    for scene, variants in by_scene.items():
        require(set(variants) == set(VARIANTS), f"candidate variants scene {scene}")
        clean_path = ROOT / variants["clean"]["path"]
        pass13 = ROOT / f"qa/pass13_directional_smear_audit/frames/clean/scene_{scene:02d}.png"
        require(sha256(clean_path) == sha256(pass13), f"candidate clean scene {scene}")
        clean = rgb(clean_path)
        for variant, floor in VARIANTS.items():
            if floor is not None:
                require(np.array_equal(rgb(ROOT / variants[variant]["path"]), shadow_floor(clean, floor)), f"candidate transform {scene} {variant}")
    require(len(list((ROOT / "qa/pass14_shadow_floor_audit/frames").rglob("*.png"))) == 80, "candidate png census")
    sheets = receipt["contact_sheet_sha256"]
    require(set(sheets) == set(VARIANTS), "candidate sheets")
    for variant, expected in sheets.items():
        path = ROOT / "qa/pass14_shadow_floor_audit" / f"contact_sheet_{variant}.png"
        require(path.is_file() and sha256(path) == expected, f"candidate sheet {variant}")
        with Image.open(path) as image:
            require(image.size == (1920, 1224), f"candidate sheet geometry {variant}")


def verify_method_frames() -> None:
    receipt = load_json(ROOT / "qa/pass14_v8_shadow_floor/receipt.json")
    require(receipt["status"] == "QA_STATIC_PNG_DERIVATIVES_NOT_V9_NOT_A_CANDIDATE", "method status")
    require(receipt["deepening_pass"] == 14, "method pass")
    require(receipt["group_count"] == 3 and receipt["scene_count"] == 21 and receipt["variant_count"] == 5 and receipt["frame_count"] == 105, "method census")
    require(receipt["variant_order"] == list(VARIANTS), "method variants")
    require(set(receipt["groups"]) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method groups")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35 and len(group["scenes"]) == 7, f"method group census {group_name}")
        source_receipt = ROOT / group["source_receipt"]
        require(source_receipt.is_file() and sha256(source_receipt) == group["source_receipt_sha256"], f"source receipt {group_name}")
        group_root = ROOT / "qa/pass14_v8_shadow_floor" / group_name
        for scene_row in group["scenes"]:
            scene = int(scene_row["scene"])
            source = ROOT / scene_row["source"]
            require(source.is_file() and sha256(source) == scene_row["source_sha256"], f"source frame {group_name} {scene}")
            samples = {sample["variant"]: sample for sample in scene_row["samples"]}
            require(set(samples) == set(VARIANTS), f"method variants {group_name} {scene}")
            clean_path = group_root / samples["clean"]["frame"]
            require(np.array_equal(rgb(source), rgb(clean_path)), f"method clean {group_name} {scene}")
            clean = rgb(clean_path)
            for variant, floor in VARIANTS.items():
                sample = samples[variant]
                path = group_root / sample["frame"]
                require(path.is_file() and sha256(path) == sample["frame_sha256"], f"method hash {group_name} {scene} {variant}")
                require(sample["luma_floor_code_value"] == floor, "method floor metadata")
                if floor is not None:
                    require(np.array_equal(rgb(path), shadow_floor(clean, floor)), f"method transform {group_name} {scene} {variant}")
        require(len(list((group_root / "frames").glob("*.png"))) == 35, f"method png census {group_name}")
        require(set(group["contact_sheets"]) == set(VARIANTS), f"method sheets {group_name}")
        for variant, row in group["contact_sheets"].items():
            path = group_root / row["path"]
            require(path.is_file() and sha256(path) == row["sha256"], f"method sheet {group_name} {variant}")
            require(row["width"] == 1280 and row["height"] == 1576, f"method sheet geometry {group_name}")
    for key in ["sealed_v8_modified", "pass7_mockup_modified", "pass12_proof_modified", "v9_created", "tts_invoked", "audio_generated", "video_encoded", "shared_or_public_assets_modified", "git_action"]:
        require(receipt[key] is False, f"method negative {key}")


def verify_metrics() -> None:
    audit = load_json(ROOT / "qa/pass14_shadow_floor_quantitative_audit.json")
    require(audit["deepening_pass"] == 14 and audit["variant_order"] == list(VARIANTS), "audit identity")
    require(audit["operational_variant"] == "shadow_floor_16", "operational variant")
    candidate = audit["candidate"]["aggregates"]["shadow_floor_16"]
    for key, value in {"mean_headline_token_recall_vs_clean": 0.997845, "mean_full_token_recall_vs_clean": 0.978241, "mean_lower_support_token_recall_vs_clean": 0.974119, "mean_numeric_token_recall_vs_clean": 0.967361, "mean_additional_black_pixel_fraction": 0.689215, "mean_nonzero_dark_pixel_survival_below_64": 0.26762}.items():
        approx(candidate[key], value, f"candidate {key}")
    require(candidate["structural_gate_scene_count"] == 0, "candidate gates")
    critical = audit["candidate"]["held_critical_aggregates"]["shadow_floor_16"]
    approx(critical["mean_headline_token_recall_vs_clean"], 1.0, "critical headline")
    approx(critical["mean_additional_black_pixel_fraction"], 0.796146, "critical black pixels")
    require(critical["structural_gate_scene_count"] == 0, "critical gates")
    severe = audit["candidate"]["aggregates"]["shadow_floor_48"]
    approx(severe["mean_headline_token_recall_vs_clean"], 0.99569, "severe headline")
    approx(severe["mean_nonzero_dark_pixel_survival_below_64"], 0.003571, "severe dark survival")
    require(severe["structural_gate_scene_count"] == 0, "severe gates")
    groups = audit["method_groups"]
    require(set(groups) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "audit groups")
    sealed = groups["sealed_v8"]["aggregates"]["shadow_floor_16"]
    approx(sealed["mean_headline_token_recall_vs_clean"], 1.0, "sealed headline")
    approx(sealed["mean_full_token_recall_vs_clean"], 0.98062, "sealed full")
    proof7 = groups["pass7_caption_safe"]["aggregates"]["shadow_floor_16"]
    require(proof7["scene_specific_gate_count"] == 6, "pass7 OCR gate count")
    proof12 = groups["pass12_sharpness_safe"]["aggregates"]["shadow_floor_16"]
    require(proof12["scene_specific_gate_count"] == 7, "pass12 gate count")
    approx(proof12["mean_gate_character_similarity_best_of_psm_6_7_11_13"], 1.0, "pass12 gate similarity")
    proof12_severe = groups["pass12_sharpness_safe"]["aggregates"]["shadow_floor_48"]
    require(proof12_severe["scene_specific_gate_count"] == 7, "pass12 severe gate count")
    visual = audit["human_visual_review"]
    require(visual["candidate_structural_gate_scenes"]["shadow_floor_16"] == "0/16", "visual candidate gates")
    require(visual["sealed_v8_result_held_badges_visual"]["shadow_floor_16"] == "7/7", "visual sealed badges")
    require(visual["pass12_operational_specific_gate_lines_visual"] == "7/7_EXACT", "visual proof gates")
    require(visual["pass12_operational_no_overlap_clipping_or_semantic_ambiguity"] is True, "visual proof safe")
    for key in ["raw_ocr_text_stored", "scientific_adjudication_performed", "sealed_v8_modified", "pass7_proof_modified", "pass12_proof_modified", "v9_created", "tts_invoked", "audio_generated", "video_encoded", "shared_or_public_assets_modified", "git_action"]:
        require(audit[key] is False, f"audit negative {key}")


def verify_packet() -> None:
    guard = load_json(ROOT / "DARK_TONE_RESILIENCE_GUARD_PASS14.json")
    require(guard["status"] == "PROPOSAL_ONLY_INTEGRATION_GUARD_NOT_V9_NOT_A_CANDIDATE", "guard status")
    require(guard["guard_id"] == "spin-worker-yui-pass14-dark-tone-20260808T092829K", "guard id")
    require(guard["transform_contract"]["operational_floor_code_value"] == 16, "guard floor")
    require(len(guard["operational_acceptance_floor"]["requirements"]) == 8, "guard requirements")
    require(guard["disposition"]["new_pixel_change_requested"] is False and guard["disposition"]["new_copy_change_requested"] is False, "guard no correction")
    require(guard["disposition"]["non_pixel_integration_guard_added"] is True, "guard added")
    require(guard["science_boundary"]["video_reportable_now"] is False, "guard reportability")
    blocker = load_json(ROOT / "BLOCKER_PACKET_PASS14.json")
    require(blocker["packet_id"] == "spin-worker-yui-pass14-blockers-20260808T092829K", "blocker id")
    require({row["blocker_id"] for row in blocker["exact_blockers"]} == {"A3.8_INDEPENDENT_REVIEW_MISSING_FOR_FROZEN_T4", "FRAME_REVIEW_REMAINS_FRAME_UNSTATED"}, "blocker identities")
    require(all(row["state"] == "BLOCKED" for row in blocker["exact_blockers"]), "blocker states")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    snapshot = load_json(ROOT / "qa/pass14_review_snapshot_v1.json")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass14-review-v1-20260808T092915K", "snapshot id")
    require(snapshot["custody"]["candidate_sha256"] == EXPECTED_CANDIDATE_SHA and snapshot["custody"]["source_freeze_sha256"] == EXPECTED_FREEZE_SHA, "snapshot custody")
    require(snapshot["fresh_candidate_extraction"]["frame_count"] == 80 and snapshot["method_derivatives"]["frame_count"] == 105, "snapshot census")
    require(snapshot["method_derivatives"]["byte_identical_rerun"] is True and snapshot["quantitative_audit"]["byte_identical_rerun"] is True, "snapshot determinism")
    chronology = snapshot["chronology"]
    require(datetime.fromisoformat(chronology["extraction_created_at"]) < datetime.fromisoformat(chronology["packet_completed_at"]) < datetime.fromisoformat(chronology["snapshot_created_at"]), "snapshot chronology")
    require(snapshot["science_blockers"]["video_reportable_now"] is False and snapshot["negative_actions"]["v9_created"] is False, "snapshot boundary")


def verify_status_handoff_boundary() -> None:
    status = load_json(ROOT / "STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS14_DARK_TONE_RESILIENCE_GUARD_V1", "status phase")
    require(status["video_reportable_now"] is False and status["worker_scope"]["official_storyboard_modified"] is False, "status boundary")
    require(status["pass14_dark_tone_audit_completed"] is True and status["pass14_dark_tone_guard_added"] is True, "status completion")
    require(status["pass14_new_pixel_or_copy_correction_requested"] is False, "status no correction")
    require(status["pass14_candidate_frame_count"] == 80 and status["pass14_method_frame_count"] == 105, "status census")
    require(status["pass14_operational_floor_code_value"] == 16, "status floor")
    require(status["pass14_candidate_floor16_structural_gate_scenes"] == "0/16" and status["pass14_pass12_proof_floor16_specific_gates"] == "7/7", "status gates")
    require(status["pass14_guard_id"] == "spin-worker-yui-pass14-dark-tone-20260808T092829K", "status guard id")
    require(status["pass14_blocker_packet_id"] == "spin-worker-yui-pass14-blockers-20260808T092829K", "status blocker id")
    require(status["pass14_review_snapshot_id"] == "spin-worker-yui-pass14-review-v1-20260808T092915K", "status snapshot id")
    receipt = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    require("PASS14_DEEPENING_MARKER_V1" in receipt and "dark-tone" in receipt.casefold() and "0.997845" in receipt, "lane receipt")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    require("floor-16" in request and "DARK_TONE_RESILIENCE_GUARD_PASS14.json" in request, "integrator request")
    static = (ROOT / "STATIC_PROPOSAL_QA.md").read_text(encoding="utf-8")
    require("Pass-14 dark-tone-floor deepening" in static and "80 candidate" in static and "105 method" in static, "static QA")
    audit_md = (ROOT / "PASS14_ENCODED_FRAME_AUDIT.md").read_text(encoding="utf-8")
    require("0.997845" in audit_md and "1.000000" in audit_md and "video_reportable_now` remains `false" in audit_md, "audit handoff")
    visible: list[str] = []
    for scene in range(1, 8):
        frame = ROOT / f"proposal_frames/v8/scene_{scene:02d}_s{scene}.png"
        result = subprocess.run(["tesseract", str(frame), "stdout", "--psm", "11"], check=True, capture_output=True, text=True)
        normalized = re.sub(r"[^a-z0-9]+", " ", result.stdout.casefold()).strip()
        require("galaxy spin" in normalized and "method only" in normalized, f"representation boundary scene {scene}")
        visible.append(normalized)
    combined = " ".join(visible)
    for topic in ["cosmology", "cosmological", "dipole", "parity anomaly", "h0", "black hole"]:
        require(topic not in combined, f"prohibited visible topic {topic}")
    media = [path for path in ROOT.rglob("*") if path.is_file() and path.suffix.casefold() in PROHIBITED_MEDIA]
    require(not media, f"prohibited media in lane: {media[:3]}")


def main() -> None:
    verify_pinned_hashes()
    verify_candidate_frames()
    verify_method_frames()
    verify_metrics()
    verify_packet()
    verify_status_handoff_boundary()
    print("PASS pass14 snapshot/candidate/80-shadow-floor-frames/hierarchy/105-method-derivatives/dark-tone-guard/source-blockers/status/no-media")


if __name__ == "__main__":
    main()
