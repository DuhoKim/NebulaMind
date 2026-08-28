#!/usr/bin/env python3
"""Verify pass-20 native-defocus/minimum-scale evidence, custody, and handoff."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
VARIANTS: dict[str, float | None] = {
    "clean": None,
    "downscale_360p": None,
    "defocus_r1_50_then_360p": 1.5,
    "defocus_r2_50_then_360p": 2.5,
    "defocus_r4_00_then_360p": 4.0,
}
PINNED = {
    "SOURCE_STATUS_FREEZE.json": "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1",
    "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
    "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
    "proposal_frames/v8/contact_sheet.png": "5889dfcbcb7f24afe989411b127a5c30adb9e4685513058eca9d51cc0cf32056",
    "SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json": "1312ea54aa860473ff57e3c47e8305ecca8630ba1f6a998a6e02d9aea9999422",
    "qa/pass12_sharpness_safe_mockup/receipt.json": "35f526a60b053f8c203278b3c205c1e0145f9a6dcd6da309541eb57b6399e92c",
    "qa/pass19_review_snapshot_v1.json": "6a55b10f1835e5859466f25915ba295bb2c4a6c19c081013fde1872f3bd544ed",
    "qa/extract_pass20_minimum_scale_defocus_frames.py": "0ec4ea4dd610cc22a9e28491d81d73a48096748f09b0ce70fa14fd7dc4bc88f7",
    "qa/pass20_minimum_scale_defocus_audit/extraction_receipt.json": "a827fa51fb67577953378e3a6e8e651056acaacf5c44a903dbf9ce129fdbd120",
    "qa/build_pass20_v8_minimum_scale_defocus.py": "1c60316d5e160795ae1e781f19b5edd00dd077ae53ac489c7f5ed9ad96670139",
    "qa/pass20_v8_minimum_scale_defocus/receipt.json": "1d591a131719c63111151292b340e0a763828da68a79d2896cf02fba9ac647ce",
    "qa/audit_pass20_minimum_scale_defocus.py": "20898ff49f41b47e47e3438ce1a1f74e4e4db4f000087ee7d044d359db574362",
    "qa/pass20_minimum_scale_defocus_quantitative_audit.json": "73a7c54ca6752d8d04c2c4f00ff48e028cfba8382e40cf54b14d2c4901469401",
    "MINIMUM_SCALE_DEFOCUS_GUARD_PASS20.json": "51d4fafe6b4379685758c89e003ed04d3fdd18249a7d65db924495c97ffe888c",
    "PASS20_ENCODED_FRAME_AUDIT.md": "da89038c15c7e146b53915b5fa3ba45a49151b15c94855a12a48f38c6d0d9056",
    "BLOCKER_PACKET_PASS20.json": "d53990fb4b7169e6418853398e78890bcea87150c0bd10450bd06175067770b9",
    "qa/pass20_review_snapshot_v1.json": "63ff67da70a52b3175bb8ddb5803c07c2121d5b9a5e5bfeb247a5f03518fddea",
}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {label}")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(relative: str):
    return json.loads((ROOT / relative).read_text())


def derive(clean: Image.Image, variant: str) -> Image.Image:
    if variant == "clean":
        return clean.convert("RGB")
    if variant == "downscale_360p":
        return clean.convert("RGB").resize((640, 360), Image.Resampling.LANCZOS)
    radius = VARIANTS[variant]
    if radius is None:
        raise ValueError(f"missing radius for {variant}")
    blurred = clean.convert("RGB").filter(ImageFilter.GaussianBlur(radius=radius))
    return blurred.resize((640, 360), Image.Resampling.LANCZOS)


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
    require(sample["native_gaussian_radius_pixels"] == VARIANTS[variant], f"radius {label}")


def check_extraction() -> None:
    receipt = load("qa/pass20_minimum_scale_defocus_audit/extraction_receipt.json")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE, "extraction candidate")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "fresh cuts")
    require(receipt["cut_detection"]["cuts"] == load("qa/pass19_minimum_scale_black_lift_audit/extraction_receipt.json")["cut_detection"]["cuts"], "pass19 cut match")
    require(receipt["scene_count"] == 16 and receipt["variant_count"] == 5 and receipt["frame_count"] == 80, "candidate census")
    require(receipt["fresh_clean_match"] == "16/16_BYTE_IDENTICAL_TO_PASS19", "clean reproduction marker")
    require(receipt["operational_variants"] == ["defocus_r1_50_then_360p"], "operational variants")
    require(receipt["characterization_variants"] == ["defocus_r2_50_then_360p", "defocus_r4_00_then_360p"], "characterization variants")
    require(len(receipt["records"]) == 16, "record count")
    for record in receipt["records"]:
        scene = int(record["scene"])
        samples = {sample["variant"]: sample for sample in record["samples"]}
        require(set(samples) == set(VARIANTS), f"candidate variants scene {scene}")
        clean_path = ROOT / "qa/pass20_minimum_scale_defocus_audit" / samples["clean"]["frame"]
        prior = ROOT / record["prior_pass19_clean_path"]
        require(sha(clean_path) == sha(prior) == record["prior_pass19_clean_sha256"], f"candidate clean scene {scene}")
        with Image.open(clean_path).convert("RGB") as clean:
            require(clean.size == (1920, 1080), f"candidate clean dimensions {scene}")
            for variant in VARIANTS:
                path = ROOT / "qa/pass20_minimum_scale_defocus_audit" / samples[variant]["frame"]
                check_sample(clean, samples[variant], path, f"candidate/{scene}/{variant}")
    for variant, sheet in receipt["contact_sheets"].items():
        path = ROOT / "qa/pass20_minimum_scale_defocus_audit" / sheet["path"]
        require(sha(path) == sheet["sha256"], f"candidate sheet {variant}")
        with Image.open(path) as image:
            require(image.size == (1892, 1276), f"candidate sheet dimensions {variant}")


def check_method() -> None:
    receipt = load("qa/pass20_v8_minimum_scale_defocus/receipt.json")
    require(receipt["scene_count"] == 21 and receipt["frame_count"] == 105, "method census")
    require(set(receipt["groups"]) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method groups")
    require(receipt["operational_variant"] == "defocus_r1_50_then_360p", "method operational variant")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"group census {group_name}")
        for row in group["scenes"]:
            scene = int(row["scene"])
            source = ROOT / row["source"]
            require(sha(source) == row["source_sha256"], f"method source {group_name}/{scene}")
            with Image.open(source).convert("RGB") as clean:
                require(clean.size == (1920, 1080), f"method source dimensions {group_name}/{scene}")
                for sample in row["samples"]:
                    path = ROOT / "qa/pass20_v8_minimum_scale_defocus" / group_name / sample["frame"]
                    check_sample(clean, sample, path, f"method/{group_name}/{scene}/{sample['variant']}")
        for variant, sheet in group["contact_sheets"].items():
            path = ROOT / "qa/pass20_v8_minimum_scale_defocus" / group_name / sheet["path"]
            require(sha(path) == sheet["sha256"], f"method sheet {group_name}/{variant}")
            with Image.open(path) as image:
                require(image.size == (1280, 1576), f"method sheet dimensions {group_name}/{variant}")


def near(actual, expected: float, label: str) -> None:
    require(math.isclose(float(actual), expected, abs_tol=1e-6), label)


def check_audit_and_packets() -> None:
    audit = load("qa/pass20_minimum_scale_defocus_quantitative_audit.json")
    require(audit["deepening_pass"] == 20 and audit["video_reportable_now"] is False, "audit contract")
    candidate = audit["candidate"]["aggregate"]
    expected = {
        "downscale_360p": (0.894444, 0.668251, 0.32809, 0.288889, 1.0),
        "defocus_r1_50_then_360p": (0.877778, 0.675856, 0.375281, 0.177778, 0.467665),
        "defocus_r2_50_then_360p": (0.866667, 0.601711, 0.211236, 0.111111, 0.206202),
        "defocus_r4_00_then_360p": (0.727778, 0.36692, 0.029213, 0.133333, 0.077428),
    }
    keys = ["headline_recall", "full_recall", "lower_recall", "numeric_recall", "mean_luma_gradient_energy_ratio_vs_lossless_360p"]
    for variant, values in expected.items():
        row = candidate[variant]
        for key, value in zip(keys, values):
            near(row[key], value, f"candidate {variant} {key}")
        require(row["structural_gate_scene_count"] == 0, f"candidate gates {variant}")
        if variant in BLURRED:
            require(row["exact_transform_recomputed_scenes"] == 16, f"candidate exact transform {variant}")
    proof = audit["method"]["pass12_sharpness_safe"]["variants"]
    similarities = {
        "downscale_360p": (0.985159, 7),
        "defocus_r1_50_then_360p": (0.954273, 7),
        "defocus_r2_50_then_360p": (0.782872, 5),
        "defocus_r4_00_then_360p": (0.260468, 0),
    }
    for variant, (similarity, gate_count) in similarities.items():
        require(proof[variant]["gate_count_passing_threshold"] == gate_count, f"proof gates {variant}")
        near(proof[variant]["mean_best_similarity"], similarity, f"proof similarity {variant}")
        if variant != "downscale_360p":
            require(proof[variant]["exact_transform_recomputed_scenes"] == 7, f"proof exact transform {variant}")
    visual = audit["method"]["human_review"]
    require(visual["pass12_defocus_r1_50_then_360p_exact_top_gates"] == "7/7", "proof visual gates")
    require(visual["pass12_defocus_r1_50_then_360p_overlap_clipping_or_ambiguity"] is False, "proof visual ambiguity")
    require(visual["sealed_v8_defocus_r1_50_then_360p_major_status_boundaries"] == "7/7", "sealed status boundaries")
    guard = load("MINIMUM_SCALE_DEFOCUS_GUARD_PASS20.json")
    require(guard["guard_id"] == "spin-worker-yui-pass20-minimum-scale-defocus-20260808T121840K", "guard id")
    require(guard["disposition"] == "INTEGRATION_GUARD_NOT_PIXEL_CORRECTION", "guard action")
    require(guard["pixel_action"]["new_pixel_or_copy_correction_requested"] is False, "guard correction")
    require(guard["pixel_action"]["sealed_v8_modified"] is False and guard["pixel_action"]["v9_created"] is False, "guard custody")
    blocker = load("BLOCKER_PACKET_PASS20.json")
    require(blocker["packet_id"] == "spin-worker-yui-pass20-blockers-20260808T121840K", "blocker id")
    require(blocker["exact_science_blockers"][0]["state"] == "OPEN" and blocker["exact_science_blockers"][1]["state"] == "OPEN", "science blockers")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    snapshot = load("qa/pass20_review_snapshot_v1.json")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass20-review-v1-20260808T122059K", "snapshot id")
    require(snapshot["pass20"]["video_reportable_now"] is False, "snapshot reportability")
    require(snapshot["safety"]["writes_confined_to_worker_lane"] is True, "snapshot lane custody")
    require(not any([
        snapshot["safety"]["tts_invoked"], snapshot["safety"]["audio_generated"],
        snapshot["safety"]["video_encoded"], snapshot["safety"]["published"],
        snapshot["safety"]["shared_or_public_assets_modified"], snapshot["safety"]["git_action"],
    ]), "snapshot negative actions")
    extraction_time = datetime.fromisoformat(load("qa/pass20_minimum_scale_defocus_audit/extraction_receipt.json")["created_at"])
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
    snapshot = load("qa/pass20_review_snapshot_v1.json")
    require(snapshot["representation_boundary"]["required_header"] == "GALAXY SPIN", "required header")
    require(snapshot["representation_boundary"]["forbidden_audience_topics_absent_from_method_frames"] is True, "forbidden audience topics")
    media = [path for path in ROOT.rglob("*") if path.is_file() and path.suffix.casefold() in {".mp4", ".mp3", ".wav", ".aac", ".m4a"}]
    require(not media, "no encoded media in lane")


def check_handoff() -> None:
    status = load("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS20_MINIMUM_SCALE_DEFOCUS_GUARD_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS20_COMPLETE", "status marker")
    require(status["video_reportable_now"] is False, "status reportability")
    require(status["pass20_minimum_scale_defocus_guard_added"] is True, "status guard")
    require(status["pass20_new_pixel_or_copy_correction_requested"] is False, "status action")
    lane = (ROOT / "LANE_RECEIPT.md").read_text()
    require("PASS20_DEEPENING_MARKER_V1" in lane, "lane marker")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
    require("Pass 20 adds the compound native-defocus/minimum-scale integration guard" in request, "integrator request")
    qa = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
    require("Pass-20 compound native-defocus/minimum-scale stress QA" in qa, "static QA")


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
    print(f"PASS pass20 snapshot/candidate/80-compound-frames/hierarchy/105-method-derivatives/minimum-scale-defocus-guard/source-blockers/{suffix}/no-media")


BLURRED = set(BLUR for BLUR, radius in VARIANTS.items() if radius is not None)


if __name__ == "__main__":
    main()
