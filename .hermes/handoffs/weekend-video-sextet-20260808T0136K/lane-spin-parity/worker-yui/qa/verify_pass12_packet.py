#!/usr/bin/env python3
"""Verify pass-12 defocus evidence, scene-gate correction, blockers, and custody."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any, NoReturn

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
EXPECTED_CANDIDATE_SHA = (
    "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
)
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
VARIANTS: dict[str, float | None] = {
    "clean": None,
    "defocus_r0_75": 0.75,
    "defocus_r1_50": 1.5,
    "defocus_r2_50": 2.5,
    "defocus_r4_00": 4.0,
}
GATE_LINES = {
    1: "RESULT LOCKED · ARCHIVE FRAME + INDEPENDENT REVIEW REQUIRED",
    2: "OVERLAPPING READOUTS · DO NOT SUM",
    3: "LABEL-FRAME STATISTIC · PHYSICAL INTERPRETATION HELD",
    4: "FRAME UNSTATED · RESULT HELD",
    5: "COLUMN CHECK ONLY · STORAGE FRAME UNRESOLVED",
    6: "CONTROL DESIGN ONLY · OUTCOMES WITHHELD",
    7: "SEPARATE AUTHORIZATION REQUIRED AFTER BOTH BLOCKERS RESOLVE",
}
GATE_BOX = (102, 78, 1540, 121)


def fail(message: str) -> NoReturn:
    raise SystemExit(f"FAIL: {message}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def image_array(path: Path) -> np.ndarray:
    with Image.open(path) as image:
        require(image.mode == "RGB", f"frame mode {path}")
        require(image.size == (1920, 1080), f"frame size {path}")
        return np.asarray(image, dtype=np.uint8)


def apply_defocus(values: np.ndarray, radius: float) -> np.ndarray:
    image = Image.fromarray(values)
    return np.asarray(
        image.filter(ImageFilter.GaussianBlur(radius=radius)), dtype=np.uint8
    )


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def draw_gate(source: Path, text: str) -> np.ndarray:
    with Image.open(source).convert("RGB") as opened:
        image = opened.copy()
    draw = ImageDraw.Draw(image)
    x0, y0, x1, y1 = GATE_BOX
    draw.rounded_rectangle(
        GATE_BOX,
        radius=12,
        fill=(13, 22, 34),
        outline=(240, 170, 68),
        width=3,
    )
    line_font = font(28)
    box = draw.textbbox((0, 0), text, font=line_font, stroke_width=1)
    text_width = box[2] - box[0]
    text_height = box[3] - box[1]
    text_x = (1920 - text_width) / 2
    text_y = y0 + ((y1 - y0) - text_height) / 2 - box[1]
    require(
        text_x >= x0 + 12 and text_x + text_width <= x1 - 12,
        "proof gate line fit",
    )
    draw.text(
        (text_x, text_y),
        text,
        fill=(255, 202, 110),
        font=line_font,
        stroke_width=1,
        stroke_fill=(255, 202, 110),
    )
    return np.asarray(image, dtype=np.uint8)


def verify_snapshot() -> dict[str, Any]:
    snapshot = load(ROOT / "qa/pass12_review_snapshot_v1.json")
    require(
        snapshot["snapshot_id"]
        == "spin-worker-yui-pass12-review-v1-20260808T081221K",
        "snapshot id",
    )
    require(
        snapshot["supersedes"]["sha256"]
        == sha256(ROOT / "qa/pass11_review_snapshot_v1.json"),
        "pass11 supersession hash",
    )
    for item in snapshot["pinned_artifacts"]:
        path = ROOT / item["path"]
        require(path.is_file(), f"missing pinned artifact {item['path']}")
        require(sha256(path) == item["sha256"], f"pinned hash {item['path']}")
    return snapshot


def verify_candidate_receipt() -> dict[str, Any]:
    receipt = load(ROOT / "qa/pass12_spatial_defocus_audit/extraction_receipt.json")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE_SHA, "receipt candidate")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "cut list")
    require(receipt["cut_detection"]["exact_pass11_match"] is True, "pass11 cut match")
    require(receipt["scene_count"] == 16, "candidate scene count")
    require(receipt["variant_count"] == 5, "candidate variant count")
    require(receipt["frame_count"] == 80, "candidate frame count")
    require(receipt["variant_order"] == list(VARIANTS), "candidate variant order")
    records = receipt["records"]
    require(len(records) == 80, "candidate record count")
    for scene in range(1, 17):
        rows = [row for row in records if row["scene"] == scene]
        require(len(rows) == 5, f"candidate scene samples {scene}")
        by_variant = {row["variant"]: row for row in rows}
        require(set(by_variant) == set(VARIANTS), f"candidate variants {scene}")
        clean_path = ROOT / by_variant["clean"]["path"]
        prior = (
            ROOT
            / "qa/pass11_recompression_audit/frames/clean"
            / f"scene_{scene:02d}.png"
        )
        require(sha256(clean_path) == sha256(prior), f"clean reproduction {scene}")
        clean = image_array(clean_path)
        for variant, radius in VARIANTS.items():
            row = by_variant[variant]
            path = ROOT / row["path"]
            require(sha256(path) == row["png_sha256"], f"candidate png hash {scene} {variant}")
            observed = image_array(path)
            expected = clean if radius is None else apply_defocus(clean, radius)
            require(np.array_equal(observed, expected), f"candidate pixels {scene} {variant}")
            require(row["radius_pixels"] == radius, f"candidate radius {scene} {variant}")
    return receipt


def verify_method_receipt() -> dict[str, Any]:
    receipt = load(ROOT / "qa/pass12_v8_spatial_defocus/receipt.json")
    require(receipt["deepening_pass"] == 12, "method pass")
    require(receipt["scene_count"] == 14, "method scenes")
    require(receipt["frame_count"] == 70, "method frames")
    require(receipt["variant_order"] == list(VARIANTS), "method variants")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7, f"method group scenes {group_name}")
        require(group["frame_count"] == 35, f"method group frames {group_name}")
        require(
            sha256(ROOT / group["source_receipt"])
            == group["source_receipt_sha256"],
            f"source receipt {group_name}",
        )
        group_root = ROOT / "qa/pass12_v8_spatial_defocus" / group_name
        for scene in group["scenes"]:
            source = ROOT / scene["source"]
            require(sha256(source) == scene["source_sha256"], f"source hash {group_name}")
            clean = image_array(source)
            for sample in scene["samples"]:
                variant = sample["variant"]
                radius = VARIANTS[variant]
                frame = group_root / sample["frame"]
                require(sha256(frame) == sample["frame_sha256"], f"method hash {group_name}")
                observed = image_array(frame)
                expected = clean if radius is None else apply_defocus(clean, radius)
                require(
                    np.array_equal(observed, expected),
                    f"method pixels {group_name} scene {scene['scene']} {variant}",
                )
    require(receipt["sealed_v8_modified"] is False, "sealed v8 method flag")
    require(receipt["pass7_mockup_modified"] is False, "pass7 method flag")
    require(receipt["v9_created"] is False, "method v9")
    return receipt


def verify_proof_receipt() -> dict[str, Any]:
    receipt = load(ROOT / "qa/pass12_sharpness_safe_mockup/receipt.json")
    require(receipt["scene_count"] == 7, "proof scenes")
    require(receipt["frame_count"] == 35, "proof frames")
    require(receipt["variant_count"] == 5, "proof variants")
    require(tuple(receipt["gate_contract"]["box"]) == GATE_BOX, "proof gate box")
    require(receipt["gate_contract"]["minimum_font_px_at_1080p"] == 28, "proof font")
    require(receipt["gate_contract"]["stroke_width_px"] == 1, "proof stroke")
    require(GATE_BOX[0] >= 96 and GATE_BOX[2] <= 1824, "proof horizontal title safe")
    require(GATE_BOX[1] >= 54 and GATE_BOX[3] < 125, "proof vertical geometry")
    for scene_row in receipt["scenes"]:
        scene = int(scene_row["scene"])
        require(scene_row["gate_line"] == GATE_LINES[scene], f"proof gate copy {scene}")
        require(scene_row["title_safe_geometry"] is True, f"proof title safe {scene}")
        require(
            scene_row["bottom_obstruction_safe_geometry"] is True,
            f"proof obstruction geometry {scene}",
        )
        source = ROOT / scene_row["sealed_input"]
        require(sha256(source) == scene_row["sealed_input_sha256"], f"proof source {scene}")
        clean_expected = draw_gate(source, GATE_LINES[scene])
        for sample in scene_row["samples"]:
            variant = sample["variant"]
            radius = VARIANTS[variant]
            frame = ROOT / "qa/pass12_sharpness_safe_mockup" / sample["frame"]
            require(sha256(frame) == sample["frame_sha256"], f"proof hash {scene} {variant}")
            observed = image_array(frame)
            expected = (
                clean_expected
                if radius is None
                else apply_defocus(clean_expected, radius)
            )
            require(np.array_equal(observed, expected), f"proof pixels {scene} {variant}")
    require(receipt["sealed_v8_modified"] is False, "proof sealed flag")
    require(receipt["pass7_mockup_modified"] is False, "proof pass7 flag")
    require(receipt["v9_created"] is False, "proof v9")
    return receipt


def verify_metrics_and_packets() -> None:
    audit = load(ROOT / "qa/pass12_spatial_defocus_quantitative_audit.json")
    candidate = audit["candidate"]
    require(candidate["frame_count"] == 80, "audit candidate frames")
    operational = candidate["aggregates"]["defocus_r1_50"]
    require(operational["mean_headline_token_recall_vs_clean"] == 0.976652, "candidate headline")
    require(operational["mean_full_token_recall_vs_clean"] == 0.790847, "candidate full")
    require(operational["mean_lower_support_token_recall_vs_clean"] == 0.373819, "candidate support")
    require(operational["mean_numeric_token_recall_vs_clean"] == 0.572167, "candidate numeric")
    require(operational["structural_gate_scene_count"] == 0, "candidate gates")
    critical = candidate["held_critical_aggregates"]["defocus_r1_50"]
    require(critical["mean_headline_token_recall_vs_clean"] == 0.966667, "critical headline")
    require(critical["structural_gate_scene_count"] == 0, "critical gates")
    sealed = audit["method_groups"]["sealed_v8"]["aggregates"]["defocus_r1_50"]
    require(sealed["mean_full_token_recall_vs_clean"] == 0.805395, "sealed full")
    pass7 = audit["method_groups"]["pass7_caption_safe"]["aggregates"]["defocus_r1_50"]
    require(pass7["scene_specific_gate_count"] == 5, "pass7 auxiliary gate count")
    require(
        audit["human_visual_review"]["pass7_caption_safe_specific_gate_lines_visual"]["defocus_r1_50"]
        == "7/7",
        "pass7 visual gates",
    )

    proof = load(ROOT / "qa/pass12_sharpness_safe_quantitative_audit.json")
    proof_operational = proof["aggregates"]["defocus_r1_50"]
    require(proof_operational["scene_specific_gate_count"] == 7, "proof gate count")
    require(
        proof_operational["mean_gate_character_similarity_best_of_psm_6_7_11_13"]
        == 0.990148,
        "proof gate similarity",
    )
    require(proof_operational["mean_headline_token_recall_vs_clean"] == 0.976327, "proof headline")
    require(proof["aggregates"]["defocus_r2_50"]["scene_specific_gate_count"] == 7, "proof r2.5 gates")
    require(proof["aggregates"]["defocus_r4_00"]["scene_specific_gate_count"] == 0, "proof r4 gates")

    correction = load(ROOT / "SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json")
    require(correction["proposed_storyboard_correction"]["qa_proof_geometry_at_1920x1080"]["box"] == list(GATE_BOX), "correction box")
    require(correction["disposition"]["new_pixel_change_requested"] is True, "correction disposition")
    require(correction["disposition"]["sealed_v8_modified"] is False, "correction sealed")
    require(correction["disposition"]["v9_created"] is False, "correction v9")

    blocker = load(ROOT / "BLOCKER_PACKET_PASS12.json")
    require(blocker["candidate"]["sha256"] == EXPECTED_CANDIDATE_SHA, "blocker candidate")
    require(blocker["science_blocker_1"]["valid_post_run_independent_review_records"] == 0, "A3.8 blocker")
    require(
        blocker["science_blocker_2"]["source"]["exact_terminal_status"]
        == "FRAME REVIEW: AGREES FRAME_UNSTATED",
        "frame blocker",
    )
    require(blocker["video_reportable_now"] is False, "blocker reportability")


def verify_sources() -> None:
    paths = {
        "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/spin-parity-census-20260805T1922K/T4_PAIRED_FLIP.json": "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873",
        "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/spin-parity-census-20260805T1922K/AMENDMENT_A3.8_DRAFT.md": "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0",
        "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/spin-parity-census-20260805T1922K/KUN_FRAME_REVIEW.md": "ccedf6846391a8f0661a88b2eec0ce21fbfd7c44ad16201080bb196f56d258e5",
    }
    for path, expected in paths.items():
        require(sha256(Path(path)) == expected, f"source hash {path}")
    terminal = Path(next(path for path in paths if path.endswith("KUN_FRAME_REVIEW.md")))
    require(
        terminal.read_text(encoding="utf-8").rstrip().endswith(
            "FRAME REVIEW: AGREES FRAME_UNSTATED"
        ),
        "frame terminal status",
    )


def verify_chronology_and_status() -> None:
    extraction = load(ROOT / "qa/pass12_spatial_defocus_audit/extraction_receipt.json")
    blocker = load(ROOT / "BLOCKER_PACKET_PASS12.json")
    snapshot = load(ROOT / "qa/pass12_review_snapshot_v1.json")
    extraction_time = datetime.fromisoformat(extraction["created_at"])
    blocker_time = datetime.fromisoformat(blocker["checked_at"])
    snapshot_time = datetime.fromisoformat(snapshot["created_at"])
    require(extraction_time < blocker_time < snapshot_time, "chronology")

    status = load(ROOT / "STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS12_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS12_COMPLETE", "status marker")
    require(status["video_reportable_now"] is False, "status reportability")
    receipt_text = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    require("SPIN_WORKER_YUI_DEEPENING_PASS12_COMPLETE" in receipt_text, "receipt marker")
    require("SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json" in receipt_text, "receipt correction")
    require("BLOCKER_PACKET_PASS12.json" in receipt_text, "receipt blocker")
    integrator = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    require("Gaussian defocus radius 1.5" in integrator, "integrator request")
    static = (ROOT / "STATIC_PROPOSAL_QA.md").read_text(encoding="utf-8")
    require("Pass-12 spatial-defocus" in static, "static QA")


def verify_no_media() -> None:
    prohibited = {".mp4", ".mp3", ".wav", ".aac", ".m4a"}
    found = [path for path in ROOT.rglob("*") if path.is_file() and path.suffix.lower() in prohibited]
    require(not found, f"prohibited media: {found}")
    require(not (ROOT / "proposal_frames/v9").exists(), "v9 directory")


def main() -> None:
    require(sha256(CANDIDATE) == EXPECTED_CANDIDATE_SHA, "candidate closing hash")
    verify_snapshot()
    verify_candidate_receipt()
    verify_method_receipt()
    verify_proof_receipt()
    verify_metrics_and_packets()
    verify_sources()
    verify_chronology_and_status()
    verify_no_media()
    print(
        "PASS pass12 snapshot/candidate/80-defocus-frames/hierarchy/70-method-derivatives/"
        "35-sharpness-proof/storyboard-correction/source-blockers/status/no-media"
    )


if __name__ == "__main__":
    main()
