#!/usr/bin/env python3
"""Verify pass-13 directional-smear evidence, guard, blockers, and custody."""

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
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
EXPECTED_CANDIDATE_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_FREEZE_SHA = "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1"
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
VARIANTS: dict[str, int | None] = {
    "clean": None,
    "smear_w03": 3,
    "smear_w07": 7,
    "smear_w13": 13,
    "smear_w21": 21,
}
EXPECTED_HASHES = {
    "SOURCE_STATUS_FREEZE.json": "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1",
    "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
    "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
    "proposal_frames/v8/contact_sheet.png": "5889dfcbcb7f24afe989411b127a5c30adb9e4685513058eca9d51cc0cf32056",
    "qa/pass12_review_snapshot_v1.json": "6471fcd37c2e854119557727d62edfe3025b8cc277e3ae25686070c7cc23fb13",
    "SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json": "1312ea54aa860473ff57e3c47e8305ecca8630ba1f6a998a6e02d9aea9999422",
    "qa/pass12_sharpness_safe_mockup/receipt.json": "35f526a60b053f8c203278b3c205c1e0145f9a6dcd6da309541eb57b6399e92c",
    "qa/pass13_directional_smear_audit/extract_directional_smear_frames.py": "da76b1fa9292c3a76a1ec401c47ce034e6fff39e0d4a0221a3c43865e3713d68",
    "qa/pass13_directional_smear_audit/extraction_receipt.json": "a5dfc83d95cbfac3ef9b6959be07ae34733684a1339dfda760c6e67569dfc94a",
    "qa/pass13_directional_smear_audit/contact_sheet_smear_w07.png": "4d47a18fc1478aa7e63fe898d63149f835525a3d18230d140ae9706779eecf93",
    "qa/pass13_directional_smear_audit/contact_sheet_smear_w13.png": "7e7bc3bfd049bb15ea29e590a2d6caf348afecae140d962af53f0f6735ed2ac2",
    "qa/pass13_directional_smear_audit/contact_sheet_smear_w21.png": "7fe8ecc694890a06126789f850472a6eb4d2f9d38a58946ebbb979676d1fc11e",
    "qa/build_pass13_v8_directional_smear.py": "4d96b58df62af08c631a37eff33f97e7deb58a873fbcfba17516046a45a223fd",
    "qa/pass13_v8_directional_smear/receipt.json": "3742a8a7a75f142de1d4fa0525bade9cc0b10e5f9c8e2da40194ec8ad216cd9e",
    "qa/audit_pass13_directional_smear.py": "2e00955d003d04e33b4c0fabb950ed993b070db5b3ffb0b44c61f4b87ed8673f",
    "qa/pass13_directional_smear_quantitative_audit.json": "d4bac9f7182b00732d1bb142cc66a5113a00a2dd274fd2271db2cfb8b3da28d4",
    "DIRECTIONAL_SMEAR_GUARD_PASS13.json": "84235eaa229f529453c5551100882f30afb80cbee1be2f2dd75301bb09d5bf53",
    "PASS13_ENCODED_FRAME_AUDIT.md": "5ea0e5bf48b668457946e085ffebf7fc28040bc8e94a4c43558ff9b1bd9f2edb",
    "BLOCKER_PACKET_PASS13.json": "3a87280c808d9d583b740799f96cd68c671e44519b7a139bbfd3cae276d7ee1f",
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


def horizontal_smear(values: np.ndarray, width: int) -> np.ndarray:
    require(width > 0 and width % 2 == 1, "invalid smear width")
    radius = width // 2
    padded = np.pad(values, ((0, 0), (radius, radius), (0, 0)), mode="edge")
    cumulative = np.cumsum(padded, axis=1, dtype=np.uint64)
    cumulative = np.concatenate(
        [np.zeros((values.shape[0], 1, 3), dtype=np.uint64), cumulative], axis=1
    )
    sums = cumulative[:, width:, :] - cumulative[:, :-width, :]
    output = ((sums + width // 2) // width).astype(np.uint8)
    require(output.shape == values.shape, "smear shape")
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
    receipt = load_json(ROOT / "qa/pass13_directional_smear_audit/extraction_receipt.json")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE_SHA, "extraction candidate hash")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "fresh cut list")
    require(receipt["cut_detection"]["exact_pass12_match"] is True, "fresh cut reproduction")
    require(len(receipt["cut_detection"]["cuts"]) == 15, "cut count")
    require(receipt["scene_count"] == 16, "scene count")
    require(receipt["variant_count"] == 5, "variant count")
    require(receipt["frame_count"] == 80, "candidate frame count")
    require(receipt["variant_order"] == list(VARIANTS), "candidate variant order")
    records = receipt["records"]
    require(isinstance(records, list) and len(records) == 80, "candidate records")
    by_scene: dict[int, dict[str, dict[str, Any]]] = {}
    for record in records:
        scene = int(record["scene"])
        variant = record["variant"]
        require(1 <= scene <= 16, "candidate scene range")
        require(variant in VARIANTS, "candidate variant")
        path = ROOT / record["path"]
        require(path.is_file(), f"candidate frame missing: {path}")
        require(sha256(path) == record["png_sha256"], f"candidate frame hash: {path}")
        require(record["kernel_width_pixels"] == VARIANTS[variant], "candidate width metadata")
        by_scene.setdefault(scene, {})[variant] = record
    require(set(by_scene) == set(range(1, 17)), "candidate scene census")
    for scene, variants in by_scene.items():
        require(set(variants) == set(VARIANTS), f"candidate variant census scene {scene}")
        clean_path = ROOT / variants["clean"]["path"]
        pass12 = ROOT / f"qa/pass12_spatial_defocus_audit/frames/clean/scene_{scene:02d}.png"
        require(sha256(clean_path) == sha256(pass12), f"clean reproduction scene {scene}")
        clean = rgb(clean_path)
        for variant, width in VARIANTS.items():
            if width is None:
                continue
            observed = rgb(ROOT / variants[variant]["path"])
            expected = horizontal_smear(clean, width)
            require(np.array_equal(observed, expected), f"candidate smear pixels scene {scene} {variant}")
    frames = list((ROOT / "qa/pass13_directional_smear_audit/frames").rglob("*.png"))
    require(len(frames) == 80, "candidate png census")
    sheets = receipt["contact_sheet_sha256"]
    require(set(sheets) == set(VARIANTS), "candidate contact sheets")
    for variant, expected_hash in sheets.items():
        path = ROOT / "qa/pass13_directional_smear_audit" / f"contact_sheet_{variant}.png"
        require(path.is_file() and sha256(path) == expected_hash, f"candidate sheet {variant}")
        with Image.open(path) as image:
            require(image.size == (1920, 1224), f"candidate sheet geometry {variant}")


def verify_method_frames() -> None:
    receipt = load_json(ROOT / "qa/pass13_v8_directional_smear/receipt.json")
    require(receipt["status"] == "QA_STATIC_PNG_DERIVATIVES_NOT_V9_NOT_A_CANDIDATE", "method status")
    require(receipt["deepening_pass"] == 13, "method pass")
    require(receipt["group_count"] == 3, "method groups")
    require(receipt["scene_count"] == 21, "method scenes")
    require(receipt["variant_count"] == 5, "method variants")
    require(receipt["frame_count"] == 105, "method frames")
    require(receipt["variant_order"] == list(VARIANTS), "method variant order")
    require(set(receipt["groups"]) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method group names")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"method counts {group_name}")
        source_receipt = ROOT / group["source_receipt"]
        require(source_receipt.is_file(), f"source receipt {group_name}")
        require(sha256(source_receipt) == group["source_receipt_sha256"], f"source receipt hash {group_name}")
        require(len(group["scenes"]) == 7, f"method scene records {group_name}")
        group_root = ROOT / "qa/pass13_v8_directional_smear" / group_name
        for scene_row in group["scenes"]:
            scene = int(scene_row["scene"])
            source = ROOT / scene_row["source"]
            require(source.is_file() and sha256(source) == scene_row["source_sha256"], f"method source {group_name} {scene}")
            samples = scene_row["samples"]
            require(len(samples) == 5, f"method samples {group_name} {scene}")
            by_variant = {sample["variant"]: sample for sample in samples}
            require(set(by_variant) == set(VARIANTS), f"method variants {group_name} {scene}")
            clean_path = group_root / by_variant["clean"]["frame"]
            require(np.array_equal(rgb(source), rgb(clean_path)), f"method clean pixels {group_name} {scene}")
            clean = rgb(clean_path)
            for variant, width in VARIANTS.items():
                sample = by_variant[variant]
                path = group_root / sample["frame"]
                require(path.is_file(), f"method frame {group_name} {scene} {variant}")
                require(sha256(path) == sample["frame_sha256"], f"method frame hash {group_name} {scene} {variant}")
                require(sample["kernel_width_pixels"] == width, f"method width {group_name} {scene} {variant}")
                if width is not None:
                    require(
                        np.array_equal(rgb(path), horizontal_smear(clean, width)),
                        f"method smear pixels {group_name} {scene} {variant}",
                    )
        pngs = list((group_root / "frames").glob("*.png"))
        require(len(pngs) == 35, f"method png census {group_name}")
        require(set(group["contact_sheets"]) == set(VARIANTS), f"method sheets {group_name}")
        for variant, row in group["contact_sheets"].items():
            path = group_root / row["path"]
            require(path.is_file() and sha256(path) == row["sha256"], f"method sheet {group_name} {variant}")
            require(row["width"] == 1280 and row["height"] == 1576, f"method sheet geometry {group_name}")
    for key in [
        "sealed_v8_modified",
        "pass7_mockup_modified",
        "pass12_proof_modified",
        "v9_created",
        "tts_invoked",
        "audio_generated",
        "video_encoded",
        "shared_or_public_assets_modified",
        "git_action",
    ]:
        require(receipt[key] is False, f"method negative action {key}")


def verify_metrics() -> None:
    audit = load_json(ROOT / "qa/pass13_directional_smear_quantitative_audit.json")
    require(audit["deepening_pass"] == 13, "audit pass")
    require(audit["variant_order"] == list(VARIANTS), "audit variants")
    require(audit["operational_variant"] == "smear_w07", "operational variant")
    require(audit["candidate"]["scene_count"] == 16, "audit candidate scenes")
    require(audit["candidate"]["frame_count"] == 80, "audit candidate frames")
    candidate = audit["candidate"]["aggregates"]["smear_w07"]
    approx(candidate["mean_headline_token_recall_vs_clean"], 0.938201, "candidate headline")
    approx(candidate["mean_full_token_recall_vs_clean"], 0.66952, "candidate full")
    approx(candidate["mean_lower_support_token_recall_vs_clean"], 0.623122, "candidate support")
    approx(candidate["mean_numeric_token_recall_vs_clean"], 0.467254, "candidate numeric")
    approx(candidate["mean_rgb_psnr_db"], 27.208633, "candidate psnr")
    approx(candidate["mean_tolerant_luma_edge_recall"], 0.914601, "candidate edge")
    approx(candidate["mean_x_gradient_energy_ratio"], 0.566164, "candidate x gradient")
    approx(candidate["mean_y_gradient_energy_ratio"], 0.87837, "candidate y gradient")
    require(candidate["structural_gate_scene_count"] == 0, "candidate gates")
    critical = audit["candidate"]["held_critical_aggregates"]["smear_w07"]
    approx(critical["mean_headline_token_recall_vs_clean"], 0.871209, "critical headline")
    approx(critical["mean_full_token_recall_vs_clean"], 0.375481, "critical full")
    approx(critical["mean_lower_support_token_recall_vs_clean"], 0.281031, "critical support")
    require(critical["structural_gate_scene_count"] == 0, "critical gates")
    severe = audit["candidate"]["aggregates"]["smear_w21"]
    approx(severe["mean_headline_token_recall_vs_clean"], 0.18527, "severe headline")
    approx(severe["mean_full_token_recall_vs_clean"], 0.046657, "severe full")
    require(severe["structural_gate_scene_count"] == 0, "severe gates")
    groups = audit["method_groups"]
    require(set(groups) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "audit method groups")
    sealed = groups["sealed_v8"]["aggregates"]["smear_w07"]
    approx(sealed["mean_full_token_recall_vs_clean"], 0.550579, "sealed full")
    approx(sealed["mean_headline_token_recall_vs_clean"], 0.728767, "sealed headline")
    proof7 = groups["pass7_caption_safe"]["aggregates"]["smear_w07"]
    require(proof7["scene_specific_gate_count"] == 6, "pass7 single-PSM gate count")
    proof12 = groups["pass12_sharpness_safe"]["aggregates"]["smear_w07"]
    require(proof12["scene_specific_gate_count"] == 7, "pass12 gate count")
    approx(
        proof12["mean_gate_character_similarity_best_of_psm_6_7_11_13"],
        0.987813,
        "pass12 gate similarity",
    )
    visual = audit["human_visual_review"]
    require(visual["candidate_structural_gate_scenes"]["smear_w07"] == "0/16", "visual candidate gates")
    require(visual["sealed_v8_result_held_badges_visual"]["smear_w07"] == "7/7", "visual sealed badges")
    require(visual["pass7_specific_gate_lines_visual"]["smear_w07"] == "7/7_EXACT", "visual pass7 gates")
    require(visual["pass12_specific_gate_lines_visual"]["smear_w07"] == "7/7_EXACT", "visual pass12 gates")
    require(visual["pass12_operational_no_overlap_clipping_or_semantic_ambiguity"] is True, "visual pass12 safe")
    for key in [
        "raw_ocr_text_stored",
        "scientific_adjudication_performed",
        "sealed_v8_modified",
        "pass7_proof_modified",
        "pass12_proof_modified",
        "v9_created",
        "tts_invoked",
        "audio_generated",
        "video_encoded",
        "shared_or_public_assets_modified",
        "git_action",
    ]:
        require(audit[key] is False, f"audit negative action {key}")


def verify_guard_blockers_snapshot() -> None:
    guard = load_json(ROOT / "DIRECTIONAL_SMEAR_GUARD_PASS13.json")
    require(guard["status"] == "PROPOSAL_ONLY_INTEGRATION_GUARD_NOT_V9_NOT_A_CANDIDATE", "guard status")
    require(guard["guard_id"] == "spin-worker-yui-pass13-directional-smear-20260808T084049K", "guard id")
    require(guard["fresh_candidate_evidence"]["candidate_sha256"] == EXPECTED_CANDIDATE_SHA, "guard candidate")
    floor = guard["operational_acceptance_floor"]
    require("width 7 pixels" in floor["variant"], "guard operational width")
    require(len(floor["requirements"]) == 7, "guard requirement count")
    require(guard["disposition"]["new_pixel_change_requested"] is False, "guard no pixel request")
    require(guard["disposition"]["new_copy_change_requested"] is False, "guard no copy request")
    require(guard["disposition"]["non_pixel_integration_guard_added"] is True, "guard added")
    require(guard["science_boundary"]["video_reportable_now"] is False, "guard reportability")
    blocker = load_json(ROOT / "BLOCKER_PACKET_PASS13.json")
    require(blocker["status"] == "PROPOSAL_ONLY_NOT_A_CANDIDATE", "blocker status")
    require(blocker["packet_id"] == "spin-worker-yui-pass13-blockers-20260808T084049K", "blocker id")
    require(len(blocker["exact_blockers"]) == 2, "blocker count")
    require({row["blocker_id"] for row in blocker["exact_blockers"]} == {
        "A3.8_INDEPENDENT_REVIEW_MISSING_FOR_FROZEN_T4",
        "FRAME_REVIEW_REMAINS_FRAME_UNSTATED",
    }, "blocker identities")
    require(all(row["state"] == "BLOCKED" for row in blocker["exact_blockers"]), "blocker states")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    snapshot = load_json(ROOT / "qa/pass13_review_snapshot_v1.json")
    require(snapshot["snapshot_status"] == "IMMUTABLE_REVIEW_SNAPSHOT", "snapshot status")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass13-review-v1-20260808T084634K", "snapshot id")
    require(snapshot["custody"]["candidate_sha256"] == EXPECTED_CANDIDATE_SHA, "snapshot candidate")
    require(snapshot["custody"]["source_freeze_sha256"] == EXPECTED_FREEZE_SHA, "snapshot freeze")
    require(snapshot["fresh_candidate_extraction"]["frame_count"] == 80, "snapshot candidate frames")
    require(snapshot["method_derivatives"]["frame_count"] == 105, "snapshot method frames")
    require(snapshot["method_derivatives"]["byte_identical_rerun"] is True, "snapshot method deterministic")
    require(snapshot["quantitative_audit"]["byte_identical_rerun"] is True, "snapshot audit deterministic")
    chronology = snapshot["chronology"]
    extraction = datetime.fromisoformat(chronology["extraction_created_at"])
    packet = datetime.fromisoformat(chronology["packet_completed_at"])
    created = datetime.fromisoformat(chronology["snapshot_created_at"])
    require(extraction < packet < created, "snapshot chronology")
    require(snapshot["science_blockers"]["video_reportable_now"] is False, "snapshot reportability")
    require(snapshot["negative_actions"]["v9_created"] is False, "snapshot no v9")


def verify_status_handoff_and_boundary() -> None:
    status = load_json(ROOT / "STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS13_DIRECTIONAL_SMEAR_GUARD_V1", "status phase")
    require(status["video_reportable_now"] is False, "status reportability")
    require(status["worker_scope"]["official_storyboard_modified"] is False, "status storyboard unchanged")
    require(status["pass13_directional_smear_audit_completed"] is True, "status audit")
    require(status["pass13_directional_smear_guard_added"] is True, "status guard")
    require(status["pass13_new_pixel_or_copy_correction_requested"] is False, "status no correction")
    require(status["pass13_candidate_frame_count"] == 80, "status candidate frames")
    require(status["pass13_method_frame_count"] == 105, "status method frames")
    require(status["pass13_operational_width_pixels"] == 7, "status width")
    require(status["pass13_candidate_w07_structural_gate_scenes"] == "0/16", "status candidate gates")
    require(status["pass13_pass12_proof_w07_specific_gates"] == "7/7", "status proof gates")
    require(status["pass13_guard_id"] == "spin-worker-yui-pass13-directional-smear-20260808T084049K", "status guard id")
    require(status["pass13_blocker_packet_id"] == "spin-worker-yui-pass13-blockers-20260808T084049K", "status packet id")
    require(status["pass13_review_snapshot_id"] == "spin-worker-yui-pass13-review-v1-20260808T084634K", "status snapshot id")
    receipt = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    require("PASS13_DEEPENING_MARKER_V1" in receipt, "receipt pass13 marker")
    require("directional-smear" in receipt.casefold(), "receipt pass13 axis")
    require("0.987813" in receipt, "receipt proof metric")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    require("centered horizontal width-7" in request, "integrator pass13 request")
    require("DIRECTIONAL_SMEAR_GUARD_PASS13.json" in request, "integrator guard")
    static = (ROOT / "STATIC_PROPOSAL_QA.md").read_text(encoding="utf-8")
    require("Pass-13 directional-smear deepening" in static, "static QA pass13")
    require("80 candidate" in static and "105 method" in static, "static QA census")
    audit_md = (ROOT / "PASS13_ENCODED_FRAME_AUDIT.md").read_text(encoding="utf-8")
    require("0.938201" in audit_md and "0.987813" in audit_md, "audit metrics")
    require("video_reportable_now` remains `false" in audit_md, "audit reportability")
    visible_text: list[str] = []
    for scene in range(1, 8):
        frame = ROOT / f"proposal_frames/v8/scene_{scene:02d}_s{scene}.png"
        result = subprocess.run(
            ["tesseract", str(frame), "stdout", "--psm", "11"],
            check=True,
            capture_output=True,
            text=True,
        )
        normalized = re.sub(r"[^a-z0-9]+", " ", result.stdout.casefold()).strip()
        require("galaxy spin" in normalized, f"representation header scene {scene}")
        require("method only" in normalized, f"method boundary scene {scene}")
        visible_text.append(normalized)
    combined_visible = " ".join(visible_text)
    for topic in ["cosmology", "cosmological", "dipole", "parity anomaly", "h0", "black hole"]:
        require(topic not in combined_visible, f"prohibited visible topic: {topic}")
    media = [path for path in ROOT.rglob("*") if path.is_file() and path.suffix.casefold() in PROHIBITED_MEDIA]
    require(not media, f"prohibited media inside lane: {media[:3]}")


def main() -> None:
    verify_pinned_hashes()
    verify_candidate_frames()
    verify_method_frames()
    verify_metrics()
    verify_guard_blockers_snapshot()
    verify_status_handoff_and_boundary()
    print(
        "PASS pass13 snapshot/candidate/80-smear-frames/hierarchy/105-method-derivatives/"
        "directional-smear-guard/source-blockers/status/no-media"
    )


if __name__ == "__main__":
    main()
