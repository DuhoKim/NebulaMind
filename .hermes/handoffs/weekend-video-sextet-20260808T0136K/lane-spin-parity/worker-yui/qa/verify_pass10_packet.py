#!/usr/bin/env python3
"""Verify pass-10 ambient-contrast evidence, guard, blockers, and custody."""

from __future__ import annotations

import hashlib
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
EXPECTED_V8_RECEIPT_SHA = "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3"
EXPECTED_PASS7_SHA = "f12b26ac1fb70b39696f9d02e7da8baf82ffb06c3ebc9e1434d7e79fc9030d3f"
EXPECTED_PASS8_SHA = "597b591da0f32325d8b764df23b7a5c9a088c666bac433a2ccd2e9a7b31d53da"
EXPECTED_PASS9_SHA = "7ef8c7e4f8a16b26b9b833cc19a9f5b5424e8afbb3d866892be8b1d869e92a11"
EXPECTED_METHOD_RECEIPT_SHA = "775582a2aac5fa71149c03693a58149bd7f8a465a90a486a674aae37f94b0d4a"
EXPECTED_AUDIT_SHA = "eda4e8cc2fe805123e203c3723746f0cd9c87b680a02c33ecd1ff66275b31592"
VARIANTS = [
    "clean",
    "uniform_black_lift_10pct",
    "uniform_black_lift_20pct",
    "uniform_black_lift_30pct",
    "uniform_black_lift_40pct",
]
BLACK_LIFT = {
    "uniform_black_lift_10pct": 0.10,
    "uniform_black_lift_20pct": 0.20,
    "uniform_black_lift_30pct": 0.30,
    "uniform_black_lift_40pct": 0.40,
}


def fail(message: str) -> NoReturn:
    raise SystemExit(f"FAIL: {message}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(
        values <= 0.04045,
        values / 12.92,
        ((values + 0.055) / 1.055) ** 2.4,
    )


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    return np.where(
        values <= 0.0031308,
        values * 12.92,
        1.055 * (values ** (1.0 / 2.4)) - 0.055,
    )


def transformed_pixels(clean_path: Path, amount: float) -> np.ndarray:
    with Image.open(clean_path).convert("RGB") as image:
        srgb = np.asarray(image, dtype=np.float64) / 255.0
    linear = srgb_to_linear(srgb)
    washed_linear = amount + (1.0 - amount) * linear
    washed_srgb = np.clip(linear_to_srgb(washed_linear), 0.0, 1.0)
    return np.rint(washed_srgb * 255.0).astype(np.uint8)


def verify_sample_set(root: Path, samples: list[dict[str, object]]) -> None:
    if [sample["variant"] for sample in samples] != VARIANTS:
        fail(f"variant order: {root}")
    paths: dict[str, Path] = {}
    for sample in samples:
        variant = sample["variant"]
        frame = sample["frame"]
        expected_sha = sample["frame_sha256"]
        if not isinstance(variant, str) or not isinstance(frame, str) or not isinstance(expected_sha, str):
            fail("invalid sample fields")
        path = root / frame
        if not path.is_file() or sha256(path) != expected_sha:
            fail(f"sample hash: {path}")
        with Image.open(path) as image:
            if image.mode != "RGB" or image.size != (1920, 1080):
                fail(f"sample mode/size: {path}")
        paths[variant] = path
    clean_path = paths["clean"]
    for variant, amount in BLACK_LIFT.items():
        expected = transformed_pixels(clean_path, amount)
        with Image.open(paths[variant]).convert("RGB") as image:
            observed = np.asarray(image)
        if not np.array_equal(expected, observed):
            fail(f"transform parity: {paths[variant]}")


def assert_close(observed: object, expected: float, name: str) -> None:
    if not isinstance(observed, (int, float)) or abs(float(observed) - expected) > 0.0000005:
        fail(f"metric {name}: {observed} != {expected}")


def main() -> None:
    if sha256(CANDIDATE) != EXPECTED_CANDIDATE_SHA:
        fail("candidate closing hash")
    if sha256(ROOT / "SOURCE_STATUS_FREEZE.json") != EXPECTED_FREEZE_SHA:
        fail("source freeze hash")
    if sha256(ROOT / "STORYBOARD_PROPOSAL.json") != EXPECTED_STORYBOARD_SHA:
        fail("storyboard hash")
    if sha256(ROOT / "proposal_frames/v8/render_receipt.json") != EXPECTED_V8_RECEIPT_SHA:
        fail("v8 receipt hash")
    if sha256(ROOT / "CAPTION_SAFE_STORYBOARD_CORRECTION_PASS7.json") != EXPECTED_PASS7_SHA:
        fail("pass7 correction hash")
    if sha256(ROOT / "REDUNDANT_ENCODING_GUARD_PASS8.json") != EXPECTED_PASS8_SHA:
        fail("pass8 guard hash")
    if sha256(ROOT / "TITLE_SAFE_STORYBOARD_CORRECTION_PASS9.json") != EXPECTED_PASS9_SHA:
        fail("pass9 correction hash")

    snapshot = load_json(ROOT / "qa/pass10_review_snapshot_v1.json")
    if snapshot["snapshot_status"] != "IMMUTABLE_REVIEW_SNAPSHOT":
        fail("snapshot status")
    if snapshot["snapshot_id"] != "spin-worker-yui-pass10-review-v1-20260808T070805K":
        fail("snapshot id")
    if snapshot["candidate"]["sha256"] != EXPECTED_CANDIDATE_SHA:
        fail("snapshot candidate")
    for pin in snapshot["pinned_artifacts"]:
        path = ROOT / pin["path"]
        if not path.is_file() or sha256(path) != pin["sha256"]:
            fail(f"snapshot pin: {pin['path']}")

    candidate_dir = ROOT / "qa/pass10_ambient_contrast_audit"
    extraction = load_json(candidate_dir / "extraction_receipt.json")
    pass9 = load_json(ROOT / "qa/pass9_safe_area_audit/extraction_receipt.json")
    if extraction["candidate_sha256"] != EXPECTED_CANDIDATE_SHA:
        fail("extraction candidate")
    if extraction["detected_cut_count"] != 15 or extraction["scene_count"] != 16:
        fail("candidate cut/scene census")
    if extraction["variant_count"] != 5 or extraction["frame_count"] != 80:
        fail("candidate variant/frame census")
    if extraction["variants"] != VARIANTS:
        fail("candidate variants")
    if extraction["detected_cut_times_seconds"] != pass9["detected_cut_times_seconds"]:
        fail("cut times vs pass9")
    if extraction["black_lift_fraction"] != BLACK_LIFT:
        fail("black-lift fractions")
    if extraction["maximum_white_to_black_wcag_like_ratio"] != {
        "clean_ideal": 21.0,
        "uniform_black_lift_10pct": 7.0,
        "uniform_black_lift_20pct": 4.2,
        "uniform_black_lift_30pct": 3.0,
        "uniform_black_lift_40pct": 2.333333,
    }:
        fail("ideal contrast ratios")
    for scene, previous_scene in zip(extraction["scenes"], pass9["scenes"]):
        verify_sample_set(candidate_dir, scene["samples"])
        if scene["samples"][0]["frame_sha256"] != previous_scene["samples"][0]["frame_sha256"]:
            fail(f"clean reproduction scene {scene['scene']}")
    for sheet in extraction["contact_sheets"].values():
        path = candidate_dir / sheet["path"]
        if sha256(path) != sheet["sha256"]:
            fail(f"candidate contact sheet {path}")

    method_dir = ROOT / "qa/pass10_v8_ambient_contrast"
    if sha256(method_dir / "receipt.json") != EXPECTED_METHOD_RECEIPT_SHA:
        fail("method receipt hash")
    method = load_json(method_dir / "receipt.json")
    if method["variant_order"] != VARIANTS or method["scene_count"] != 14 or method["frame_count"] != 70:
        fail("method census")
    if method["black_lift_fraction"] != BLACK_LIFT:
        fail("method transform fractions")
    for group_name, group in method["groups"].items():
        group_root = method_dir / group_name
        if group["scene_count"] != 7 or group["frame_count"] != 35:
            fail(f"method group census {group_name}")
        for scene in group["scenes"]:
            verify_sample_set(group_root, scene["samples"])
            if not scene["clean_copy_sha256_match"]:
                fail(f"method clean copy {group_name} scene {scene['scene']}")
        for sheet in group["contact_sheets"].values():
            path = group_root / sheet["path"]
            if sha256(path) != sheet["sha256"]:
                fail(f"method contact sheet {path}")

    if sha256(ROOT / "qa/pass10_ambient_contrast_quantitative_audit.json") != EXPECTED_AUDIT_SHA:
        fail("quantitative audit hash")
    audit = load_json(ROOT / "qa/pass10_ambient_contrast_quantitative_audit.json")
    if audit["candidate"]["clean_midpoints_byte_identical_to_pass9_clean"] != 16:
        fail("audit clean reproduction")
    candidate20 = audit["candidate"]["aggregates"]["uniform_black_lift_20pct"]
    for key, expected in {
        "mean_headline_token_recall_vs_clean": 0.997845,
        "mean_full_token_recall_vs_clean": 0.875962,
        "mean_lower_support_token_recall_vs_clean": 0.467116,
        "mean_numeric_token_recall_vs_clean": 0.648508,
    }.items():
        assert_close(candidate20[key], expected, f"candidate20 {key}")
    if candidate20["structural_gate_scene_count"] != 0:
        fail("candidate20 gate count")
    critical20 = audit["candidate"]["held_critical_aggregates"]["uniform_black_lift_20pct"]
    for key, expected in {
        "mean_headline_token_recall_vs_clean": 1.0,
        "mean_full_token_recall_vs_clean": 0.810953,
        "mean_lower_support_token_recall_vs_clean": 0.786754,
        "mean_numeric_token_recall_vs_clean": 0.768558,
    }.items():
        assert_close(critical20[key], expected, f"critical20 {key}")
    if critical20["structural_gate_scene_count"] != 0:
        fail("critical20 gate count")
    sealed20 = audit["method_groups"]["sealed_v8"]["aggregates"]["uniform_black_lift_20pct"]
    caption20 = audit["method_groups"]["pass7_caption_safe"]["aggregates"]["uniform_black_lift_20pct"]
    for row, expected_values, name in [
        (sealed20, [0.961405, 1.0, 0.980952, 1.0], "sealed20"),
        (caption20, [0.952633, 1.0, 0.945022, 1.0], "caption20"),
    ]:
        for key, expected in zip(
            [
                "mean_full_token_recall_vs_clean",
                "mean_headline_token_recall_vs_clean",
                "mean_lower_support_token_recall_vs_clean",
                "mean_numeric_token_recall_vs_clean",
            ],
            expected_values,
        ):
            assert_close(row[key], expected, f"{name} {key}")
    if caption20["scene_specific_gate_count"] != 7:
        fail("caption20 scene-specific gate count")
    visual = audit["human_visual_review"]
    if visual["sealed_v8_result_held_text_visual"]["uniform_black_lift_20pct"] != "7/7":
        fail("sealed visual badges")
    if visual["pass7_caption_safe_specific_gate_lines_visual"]["uniform_black_lift_40pct"] != "7/7":
        fail("caption severe visual gates")

    guard = load_json(ROOT / "AMBIENT_CONTRAST_GUARD_PASS10.json")
    if guard["disposition"]["new_pixel_change_requested"] is not False:
        fail("guard pixel disposition")
    if guard["operational_acceptance_floor"]["maximum_white_to_black_wcag_like_ratio"] != 4.2:
        fail("guard operational ratio")
    blocker = load_json(ROOT / "BLOCKER_PACKET_PASS10.json")
    if blocker["video_reportable_now"] is not False:
        fail("blocker reportability")
    if blocker["science_blocker_1"]["valid_post_run_independent_review_records"] != 0:
        fail("blocker A3.8 count")
    if blocker["science_blocker_2"]["source"]["exact_terminal_status"] != "FRAME REVIEW: AGREES FRAME_UNSTATED":
        fail("blocker frame terminal status")

    extracted_at = parse_time(extraction["extracted_at_utc"])
    guard_at = parse_time(guard["created_at"])
    snapshot_at = parse_time(snapshot["created_at"])
    if not extracted_at < guard_at < snapshot_at:
        fail("chronology")

    status = load_json(ROOT / "STATUS.json")
    if status["phase"] != "SEALED_ISOLATED_DEEPENING_PASS10_V1":
        fail("status phase")
    if status["receipt_marker"] != "SPIN_WORKER_YUI_DEEPENING_PASS10_COMPLETE":
        fail("status receipt marker")
    if status["video_reportable_now"] is not False:
        fail("status reportability")
    receipt_text = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    if "SPIN_WORKER_YUI_DEEPENING_PASS10_COMPLETE" not in receipt_text:
        fail("lane receipt marker")
    integrator_text = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    if "20%" not in integrator_text or "AMBIENT_CONTRAST_GUARD_PASS10.json" not in integrator_text:
        fail("integrator pass10 handoff")

    if (ROOT / "proposal_frames/v9").exists():
        fail("unexpected v9")
    prohibited_suffixes = {".mp4", ".mp3", ".wav", ".aac", ".m4a"}
    media = [path for path in ROOT.rglob("*") if path.is_file() and path.suffix.casefold() in prohibited_suffixes]
    if media:
        fail(f"prohibited media under worker root: {media}")

    print(
        "PASS pass10 snapshot/candidate/80-contrast-frames/hierarchy/"
        "70-method-derivatives/contrast-guard/source-blockers/status/no-media"
    )


if __name__ == "__main__":
    main()
