#!/usr/bin/env python3
"""Verify pass-19 minimum-scale/black-lift evidence, custody, and handoff."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
VARIANTS: dict[str, float | None] = {
    "clean": None,
    "downscale_360p": None,
    "black_lift20_360p": 0.20,
    "black_lift30_360p": 0.30,
    "black_lift40_360p": 0.40,
}
PINNED = {
    "SOURCE_STATUS_FREEZE.json": "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1",
    "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
    "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
    "proposal_frames/v8/contact_sheet.png": "5889dfcbcb7f24afe989411b127a5c30adb9e4685513058eca9d51cc0cf32056",
    "SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json": "1312ea54aa860473ff57e3c47e8305ecca8630ba1f6a998a6e02d9aea9999422",
    "qa/pass12_sharpness_safe_mockup/receipt.json": "35f526a60b053f8c203278b3c205c1e0145f9a6dcd6da309541eb57b6399e92c",
    "qa/pass18_review_snapshot_v1.json": "777c7f75596042d723a714d3e0f157fa216ee5aa5a4ac51fa89cda55b06f5259",
    "qa/extract_pass19_minimum_scale_black_lift_frames.py": "f23f3ea895211b835dbecd7d91cf1677ef9962e509ed2785edc535fb9f2cc8cb",
    "qa/pass19_minimum_scale_black_lift_audit/extraction_receipt.json": "6b716c0c07c59e8650d4fc2fbb13204b1e9c01140c5a1248181e7f638f873be4",
    "qa/build_pass19_v8_minimum_scale_black_lift.py": "da535ce840aa70249f8b6c04dfee1e046b6f2be77fca16f26712d5049e3d446a",
    "qa/pass19_v8_minimum_scale_black_lift/receipt.json": "9c2a5623c22afefe77597f2af61905cc0207ca5e7a0ad019844dc7c43dcbd497",
    "qa/audit_pass19_minimum_scale_black_lift.py": "ef5c85e071af701cd88c1f6514e1dc53489832618fce1add25ae653c808a7a77",
    "qa/pass19_minimum_scale_black_lift_quantitative_audit.json": "2e6b2eeca5b34000938d196ed1cacbd54bcb0e7df86c55c92b99172f0038d6e4",
    "MINIMUM_SCALE_BLACK_LIFT_GUARD_PASS19.json": "17cf6c431019e3fbaa59093196b90fd16012bc991afc2950d900860ee30d8db8",
    "PASS19_ENCODED_FRAME_AUDIT.md": "9e6e381a83c61280f0306e6f3689b4476d6941180231f95d24a2359bf90c520f",
    "BLOCKER_PACKET_PASS19.json": "151ee0e6f8557be79cc5acb3b8b8350def26247f86a4370823c877b15a3eb723",
    "qa/pass19_review_snapshot_v1.json": "6a55b10f1835e5859466f25915ba295bb2c4a6c19c081013fde1872f3bd544ed",
}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {label}")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(relative: str):
    return json.loads((ROOT / relative).read_text())


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.0031308, values * 12.92, 1.055 * values ** (1.0 / 2.4) - 0.055)


def derive(clean: Image.Image, variant: str) -> Image.Image:
    if variant == "clean":
        return clean.convert("RGB")
    represented = clean.convert("RGB").resize((640, 360), Image.Resampling.LANCZOS)
    amount = VARIANTS[variant]
    if amount is None:
        return represented
    srgb = np.asarray(represented, dtype=np.float64) / 255.0
    linear = srgb_to_linear(srgb)
    lifted = amount + (1.0 - amount) * linear
    pixels = np.rint(np.clip(linear_to_srgb(lifted), 0.0, 1.0) * 255.0).astype(np.uint8)
    return Image.fromarray(pixels)


def image_equal(first: Image.Image, second: Image.Image) -> bool:
    return ImageChops.difference(first.convert("RGB"), second.convert("RGB")).getbbox() is None


def check_pins() -> None:
    require(sha(CANDIDATE) == EXPECTED_CANDIDATE, "candidate custody")
    for relative, expected in PINNED.items():
        require((ROOT / relative).is_file(), f"missing {relative}")
        require(sha(ROOT / relative) == expected, f"hash {relative}")


def check_sample(clean: Image.Image, sample: dict[str, object], path: Path, label: str) -> None:
    variant = str(sample["variant"])
    require(variant in VARIANTS, f"variant {label}")
    require(sha(path) == sample["sha256"], f"frame hash {label}")
    expected = derive(clean, variant)
    with Image.open(path).convert("RGB") as observed:
        require(observed.size == ((1920, 1080) if variant == "clean" else (640, 360)), f"dimensions {label}")
        require(image_equal(expected, observed), f"transform pixels {label}")
    require(sample["black_lift_fraction"] == VARIANTS[variant], f"lift fraction {label}")


def check_extraction() -> None:
    receipt = load("qa/pass19_minimum_scale_black_lift_audit/extraction_receipt.json")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE, "extraction candidate")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "fresh cuts")
    require(receipt["cut_detection"]["cuts"] == load("qa/pass18_minimum_scale_obstruction_audit/extraction_receipt.json")["cut_detection"]["cuts"], "pass18 cut match")
    require(receipt["scene_count"] == 16 and receipt["variant_count"] == 5 and receipt["frame_count"] == 80, "candidate census")
    require(receipt["fresh_clean_match"] == "16/16_BYTE_IDENTICAL_TO_PASS18", "clean reproduction marker")
    require(receipt["operational_variants"] == ["black_lift20_360p"], "operational variants")
    require(receipt["characterization_variants"] == ["black_lift30_360p", "black_lift40_360p"], "characterization variants")
    require(len(receipt["records"]) == 16, "record count")
    for record in receipt["records"]:
        scene = int(record["scene"])
        samples = {sample["variant"]: sample for sample in record["samples"]}
        require(set(samples) == set(VARIANTS), f"candidate variants scene {scene}")
        clean_path = ROOT / "qa/pass19_minimum_scale_black_lift_audit" / samples["clean"]["frame"]
        prior = ROOT / record["prior_pass18_clean_path"]
        require(sha(clean_path) == sha(prior) == record["prior_pass18_clean_sha256"], f"candidate clean scene {scene}")
        with Image.open(clean_path).convert("RGB") as clean:
            require(clean.size == (1920, 1080), f"candidate clean dimensions {scene}")
            for variant in VARIANTS:
                path = ROOT / "qa/pass19_minimum_scale_black_lift_audit" / samples[variant]["frame"]
                check_sample(clean, samples[variant], path, f"candidate/{scene}/{variant}")
    for variant, sheet in receipt["contact_sheets"].items():
        path = ROOT / "qa/pass19_minimum_scale_black_lift_audit" / sheet["path"]
        require(sha(path) == sheet["sha256"], f"candidate sheet {variant}")
        with Image.open(path) as image:
            require(image.size == (1892, 1276), f"candidate sheet dimensions {variant}")


def check_method() -> None:
    receipt = load("qa/pass19_v8_minimum_scale_black_lift/receipt.json")
    require(receipt["scene_count"] == 21 and receipt["frame_count"] == 105, "method census")
    require(set(receipt["groups"]) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method groups")
    require(receipt["operational_variant"] == "black_lift20_360p", "method operational variant")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"group census {group_name}")
        for row in group["scenes"]:
            scene = int(row["scene"])
            source = ROOT / row["source"]
            require(sha(source) == row["source_sha256"], f"method source {group_name}/{scene}")
            with Image.open(source).convert("RGB") as clean:
                require(clean.size == (1920, 1080), f"method source dimensions {group_name}/{scene}")
                for sample in row["samples"]:
                    path = ROOT / "qa/pass19_v8_minimum_scale_black_lift" / group_name / sample["frame"]
                    check_sample(clean, sample, path, f"method/{group_name}/{scene}/{sample['variant']}")
        for variant, sheet in group["contact_sheets"].items():
            path = ROOT / "qa/pass19_v8_minimum_scale_black_lift" / group_name / sheet["path"]
            require(sha(path) == sheet["sha256"], f"method sheet {group_name}/{variant}")
            with Image.open(path) as image:
                require(image.size == (1280, 1576), f"method sheet dimensions {group_name}/{variant}")


def near(actual, expected: float, label: str) -> None:
    require(math.isclose(float(actual), expected, abs_tol=1e-6), label)


def check_audit_and_packets() -> None:
    audit = load("qa/pass19_minimum_scale_black_lift_quantitative_audit.json")
    require(audit["deepening_pass"] == 19 and audit["video_reportable_now"] is False, "audit contract")
    candidate = audit["candidate"]["aggregate"]
    expected = {
        "downscale_360p": (0.894444, 0.668251, 0.32809, 0.288889, 10.194278),
        "black_lift20_360p": (0.883333, 0.621673, 0.289888, 0.155556, 2.522387),
        "black_lift30_360p": (0.877778, 0.576046, 0.262921, 0.166667, 1.956003),
        "black_lift40_360p": (0.877778, 0.511407, 0.235955, 0.155556, 1.633905),
    }
    keys = ["headline_recall", "full_recall", "lower_recall", "numeric_recall", "mean_robust_wcag_like_ratio_p99_p01"]
    for variant, values in expected.items():
        row = candidate[variant]
        for key, value in zip(keys, values):
            near(row[key], value, f"candidate {variant} {key}")
        require(row["structural_gate_scene_count"] == 0, f"candidate gates {variant}")
        if variant in {"black_lift20_360p", "black_lift30_360p", "black_lift40_360p"}:
            require(row["exact_transform_recomputed_scenes"] == 16, f"candidate exact transform {variant}")
    proof = audit["method"]["pass12_sharpness_safe"]["variants"]
    similarities = {
        "downscale_360p": 0.985159,
        "black_lift20_360p": 0.996825,
        "black_lift30_360p": 0.990873,
        "black_lift40_360p": 0.996825,
    }
    for variant, similarity in similarities.items():
        require(proof[variant]["gate_count_passing_threshold"] == 7, f"proof gates {variant}")
        near(proof[variant]["mean_best_similarity"], similarity, f"proof similarity {variant}")
        if variant != "downscale_360p":
            require(proof[variant]["exact_transform_recomputed_scenes"] == 7, f"proof exact transform {variant}")
    visual = audit["method"]["human_review"]
    require(visual["pass12_black_lift20_360p_exact_top_gates"] == "7/7", "proof visual gates")
    require(visual["pass12_black_lift20_360p_overlap_clipping_or_ambiguity"] is False, "proof visual ambiguity")
    require(visual["sealed_v8_black_lift20_360p_major_status_boundaries"] == "7/7", "sealed status boundaries")
    guard = load("MINIMUM_SCALE_BLACK_LIFT_GUARD_PASS19.json")
    require(guard["guard_id"] == "spin-worker-yui-pass19-minimum-scale-black-lift-20260808T114942K", "guard id")
    require(guard["disposition"] == "INTEGRATION_GUARD_NOT_PIXEL_CORRECTION", "guard action")
    require(guard["pixel_action"]["new_pixel_or_copy_correction_requested"] is False, "guard correction")
    require(guard["pixel_action"]["sealed_v8_modified"] is False and guard["pixel_action"]["v9_created"] is False, "guard custody")
    blocker = load("BLOCKER_PACKET_PASS19.json")
    require(blocker["packet_id"] == "spin-worker-yui-pass19-blockers-20260808T114942K", "blocker id")
    require(blocker["exact_science_blockers"][0]["state"] == "OPEN" and blocker["exact_science_blockers"][1]["state"] == "OPEN", "science blockers")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    snapshot = load("qa/pass19_review_snapshot_v1.json")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass19-review-v1-20260808T115617K", "snapshot id")
    require(snapshot["pass19"]["video_reportable_now"] is False, "snapshot reportability")
    require(snapshot["safety"]["writes_confined_to_worker_lane"] is True, "snapshot lane custody")
    require(not any([
        snapshot["safety"]["tts_invoked"], snapshot["safety"]["audio_generated"],
        snapshot["safety"]["video_encoded"], snapshot["safety"]["published"],
        snapshot["safety"]["shared_or_public_assets_modified"], snapshot["safety"]["git_action"],
    ]), "snapshot negative actions")
    extraction_time = datetime.fromisoformat(load("qa/pass19_minimum_scale_black_lift_audit/extraction_receipt.json")["created_at"])
    guard_time = datetime.fromisoformat(guard["created_at"])
    snapshot_time = datetime.fromisoformat(snapshot["created_at"])
    require(extraction_time < guard_time < snapshot_time, "chronology")


def check_static_and_no_media() -> None:
    freeze = load("SOURCE_STATUS_FREEZE.json")
    require(freeze["video_reportable_now"] is False, "freeze reportability")
    story = load("STORYBOARD_PROPOSAL.json")
    require(story["status"] == "PROPOSAL_ONLY_NOT_A_CANDIDATE" and story["video_reportable_now"] is False, "story status")
    static = load("qa/static_proposal_validation.json")
    require(static.get("verdict") == "PASS", "static validation")
    snapshot = load("qa/pass19_review_snapshot_v1.json")
    require(snapshot["representation_boundary"]["required_header"] == "GALAXY SPIN", "required header")
    require(snapshot["representation_boundary"]["forbidden_audience_topics_absent_from_method_frames"] is True, "forbidden audience topics")
    media = [path for path in ROOT.rglob("*") if path.is_file() and path.suffix.casefold() in {".mp4", ".mp3", ".wav", ".aac", ".m4a"}]
    require(not media, "no encoded media in lane")


def check_handoff() -> None:
    status = load("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS19_MINIMUM_SCALE_BLACK_LIFT_GUARD_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS19_COMPLETE", "status marker")
    require(status["video_reportable_now"] is False, "status reportability")
    require(status["pass19_minimum_scale_black_lift_guard_added"] is True, "status guard")
    require(status["pass19_new_pixel_or_copy_correction_requested"] is False, "status action")
    lane = (ROOT / "LANE_RECEIPT.md").read_text()
    require("PASS19_DEEPENING_MARKER_V1" in lane, "lane marker")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
    require("Pass 19 adds the compound minimum-scale/black-lift integration guard" in request, "integrator request")
    qa = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
    require("Pass-19 compound minimum-scale/black-lift stress QA" in qa, "static QA")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-only", action="store_true")
    arguments = parser.parse_args()
    check_pins()
    check_extraction()
    check_method()
    check_audit_and_packets()
    check_static_and_no_media()
    if not arguments.evidence_only:
        check_handoff()
    suffix = "evidence-only" if arguments.evidence_only else "status-handoff"
    print(f"PASS pass19 snapshot/candidate/80-compound-frames/hierarchy/105-method-derivatives/minimum-scale-black-lift-guard/source-blockers/{suffix}/no-media")


if __name__ == "__main__":
    main()
