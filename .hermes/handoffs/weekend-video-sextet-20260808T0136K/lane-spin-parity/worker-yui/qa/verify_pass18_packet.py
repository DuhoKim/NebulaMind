#!/usr/bin/env python3
"""Verify pass-18 minimum-scale/obstruction evidence, custody, and handoff."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
VARIANTS: dict[str, float | None] = {
    "clean": None,
    "downscale_360p": None,
    "caption15_360p": 0.15,
    "player_ui25_360p": 0.25,
    "heavy35_360p": 0.35,
}
PINNED = {
    "SOURCE_STATUS_FREEZE.json": "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1",
    "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
    "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
    "proposal_frames/v8/contact_sheet.png": "5889dfcbcb7f24afe989411b127a5c30adb9e4685513058eca9d51cc0cf32056",
    "SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json": "1312ea54aa860473ff57e3c47e8305ecca8630ba1f6a998a6e02d9aea9999422",
    "qa/pass12_sharpness_safe_mockup/receipt.json": "35f526a60b053f8c203278b3c205c1e0145f9a6dcd6da309541eb57b6399e92c",
    "qa/pass17_review_snapshot_v1.json": "2c17757ef56a94cc0cacb29d8eebfc3e682eb2c34042ca012b18efb7ffc700be",
    "qa/extract_pass18_minimum_scale_obstruction_frames.py": "98e548514a9c1c0479209187aeb28fcb521e60492aadb7cecae6f8a155ba4afa",
    "qa/pass18_minimum_scale_obstruction_audit/extraction_receipt.json": "cd4d24f3152e054906caecd7918c6c9c6d0bcf02f18648b2f7b0b17e25837eca",
    "qa/build_pass18_v8_minimum_scale_obstruction.py": "c72f8f8d1adcf9fb5e007800359789cc9ef5ce9235688f17e9effbe8a47b923b",
    "qa/pass18_v8_minimum_scale_obstruction/receipt.json": "50adb21a297b109d0156554cc10b68b935ce2580699139c76f737dc0d5c9cde7",
    "qa/audit_pass18_minimum_scale_obstruction.py": "92de8d63bf8fafe63aca7323d2a9cb0d822d2c04f762b35b6f8469b314ca63d7",
    "qa/pass18_minimum_scale_obstruction_quantitative_audit.json": "4ea190e438f348635ffeb735d852ba08993b8eddcc53843b9e622db6b9b55ba1",
    "MINIMUM_SCALE_OBSTRUCTION_GUARD_PASS18.json": "8d0740776fc847e577185cfddefba741804b3c0a6403721a0de41f7c169345d3",
    "PASS18_ENCODED_FRAME_AUDIT.md": "6848f1dfc0451c555b1b33eb1d04e273f2c3956eb4fedb8fd9ad6174ad1d1266",
    "BLOCKER_PACKET_PASS18.json": "07e51c3648859986911bd4c9fc843a20b97a28bc4cc2280db07ed7aec6715a80",
    "qa/pass18_review_snapshot_v1.json": "777c7f75596042d723a714d3e0f157fa216ee5aa5a4ac51fa89cda55b06f5259",
}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {label}")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(rel: str):
    return json.loads((ROOT / rel).read_text())


def derive(clean: Image.Image, variant: str) -> tuple[Image.Image, int | None]:
    if variant == "clean":
        return clean.convert("RGB"), None
    represented = clean.convert("RGB").resize((640, 360), Image.Resampling.LANCZOS)
    fraction = VARIANTS[variant]
    if fraction is None:
        return represented, None
    top_y = int(round(360 * (1.0 - fraction)))
    output = represented.copy()
    ImageDraw.Draw(output).rectangle((0, top_y, 639, 359), fill=(0, 0, 0))
    return output, top_y


def image_equal(a: Image.Image, b: Image.Image) -> bool:
    return ImageChops.difference(a.convert("RGB"), b.convert("RGB")).getbbox() is None


def check_pins() -> None:
    require(sha(CANDIDATE) == EXPECTED_CANDIDATE, "candidate custody")
    for rel, expected in PINNED.items():
        require((ROOT / rel).is_file(), f"missing {rel}")
        require(sha(ROOT / rel) == expected, f"hash {rel}")


def check_sample(clean: Image.Image, sample: dict[str, object], path: Path, label: str) -> None:
    variant = str(sample["variant"])
    require(variant in VARIANTS, f"variant {label}")
    require(sha(path) == sample["sha256"], f"frame hash {label}")
    expected, top_y = derive(clean, variant)
    with Image.open(path).convert("RGB") as observed:
        expected_size = (1920, 1080) if variant == "clean" else (640, 360)
        require(observed.size == expected_size, f"dimensions {label}")
        require(image_equal(expected, observed), f"transform pixels {label}")
    require(sample["mask_top_y"] == top_y, f"mask top {label}")
    require(sample["obstruction_fraction"] == VARIANTS[variant], f"mask fraction {label}")
    if top_y is not None:
        require(sample["mask_color_rgb"] == [0, 0, 0], f"mask color {label}")
        require(sample["unobstructed_pixels_identical_to_downscale"] is True, f"unobstructed marker {label}")


def check_extraction() -> None:
    receipt = load("qa/pass18_minimum_scale_obstruction_audit/extraction_receipt.json")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE, "extraction candidate")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "fresh cuts")
    require(receipt["cut_detection"]["cuts"] == load("qa/pass17_minimum_scale_recompression_audit/extraction_receipt.json")["cut_detection"]["cuts"], "pass17 cut match")
    require(receipt["scene_count"] == 16 and receipt["variant_count"] == 5 and receipt["frame_count"] == 80, "candidate census")
    require(receipt["fresh_clean_match"] == "16/16_BYTE_IDENTICAL_TO_PASS17", "clean reproduction marker")
    require(receipt["operational_variants"] == ["caption15_360p", "player_ui25_360p"], "operational variants")
    require(receipt["characterization_variants"] == ["heavy35_360p"], "characterization variants")
    require(len(receipt["records"]) == 16, "record count")
    for record in receipt["records"]:
        scene = int(record["scene"])
        samples = {sample["variant"]: sample for sample in record["samples"]}
        require(set(samples) == set(VARIANTS), f"candidate variants scene {scene}")
        clean_path = ROOT / "qa/pass18_minimum_scale_obstruction_audit" / samples["clean"]["frame"]
        prior = ROOT / record["prior_pass17_clean_path"]
        require(sha(clean_path) == sha(prior) == record["prior_pass17_clean_sha256"], f"candidate clean scene {scene}")
        with Image.open(clean_path).convert("RGB") as clean:
            require(clean.size == (1920, 1080), f"candidate clean dimensions {scene}")
            for variant in VARIANTS:
                path = ROOT / "qa/pass18_minimum_scale_obstruction_audit" / samples[variant]["frame"]
                check_sample(clean, samples[variant], path, f"candidate/{scene}/{variant}")
    for variant, sheet in receipt["contact_sheets"].items():
        path = ROOT / "qa/pass18_minimum_scale_obstruction_audit" / sheet["path"]
        require(sha(path) == sheet["sha256"], f"candidate sheet {variant}")
        with Image.open(path) as image:
            require(image.size == (1892, 1276), f"candidate sheet dimensions {variant}")


def check_method() -> None:
    receipt = load("qa/pass18_v8_minimum_scale_obstruction/receipt.json")
    require(receipt["group_count"] == 3 and receipt["scene_count"] == 21 and receipt["frame_count"] == 105, "method census")
    require(set(receipt["groups"]) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method groups")
    require(receipt["operational_variants"] == ["caption15_360p", "player_ui25_360p"], "method operational variants")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"group census {group_name}")
        for row in group["scenes"]:
            scene = int(row["scene"])
            source = ROOT / row["source"]
            require(sha(source) == row["source_sha256"], f"method source {group_name}/{scene}")
            with Image.open(source).convert("RGB") as clean:
                require(clean.size == (1920, 1080), f"method source dimensions {group_name}/{scene}")
                for sample in row["samples"]:
                    path = ROOT / "qa/pass18_v8_minimum_scale_obstruction" / group_name / sample["frame"]
                    check_sample(clean, sample, path, f"method/{group_name}/{scene}/{sample['variant']}")
        for variant, sheet in group["contact_sheets"].items():
            path = ROOT / "qa/pass18_v8_minimum_scale_obstruction" / group_name / sheet["path"]
            require(sha(path) == sheet["sha256"], f"method sheet {group_name}/{variant}")
            with Image.open(path) as image:
                require(image.size == (1280, 1576), f"method sheet dimensions {group_name}/{variant}")


def near(actual, expected: float, label: str) -> None:
    require(math.isclose(float(actual), expected, abs_tol=1e-6), label)


def check_audit_and_packets() -> None:
    audit = load("qa/pass18_minimum_scale_obstruction_quantitative_audit.json")
    require(audit["deepening_pass"] == 18 and audit["video_reportable_now"] is False, "audit contract")
    candidate = audit["candidate"]["aggregate"]
    expected = {
        "downscale_360p": (0.894444, 0.668251, 0.32809, 0.288889),
        "caption15_360p": (0.894444, 0.565589, 0.089888, 0.244444),
        "player_ui25_360p": (0.894444, 0.548479, 0.049438, 0.233333),
        "heavy35_360p": (0.894444, 0.527567, 0.006742, 0.166667),
    }
    keys = ["headline_recall", "full_recall", "lower_recall", "numeric_recall"]
    for variant, values in expected.items():
        row = candidate[variant]
        for key, value in zip(keys, values):
            near(row[key], value, f"candidate {variant} {key}")
        require(row["structural_gate_scene_count"] == 0, f"candidate gates {variant}")
    zones = audit["candidate"]["obstruction_zone_ocr"]
    require(zones["caption15_360p"] == {"reference_downscale_tokens_in_mask_zone": 124, "observed_tokens_in_mask_zone": 0}, "caption zone")
    require(zones["player_ui25_360p"] == {"reference_downscale_tokens_in_mask_zone": 148, "observed_tokens_in_mask_zone": 0}, "player zone")
    require(zones["heavy35_360p"] == {"reference_downscale_tokens_in_mask_zone": 188, "observed_tokens_in_mask_zone": 0}, "heavy zone")
    proof = audit["method"]["pass12_sharpness_safe"]["variants"]
    for variant in ["downscale_360p", "caption15_360p", "player_ui25_360p", "heavy35_360p"]:
        require(proof[variant]["gate_count_passing_threshold"] == 7, f"proof gates {variant}")
        near(proof[variant]["mean_best_similarity"], 0.985159, f"proof similarity {variant}")
        if variant in {"caption15_360p", "player_ui25_360p", "heavy35_360p"}:
            require(proof[variant]["unobstructed_pixel_identity_scenes"] == 7, f"proof top identity {variant}")
            require(proof[variant]["masked_pixels_all_black_scenes"] == 7, f"proof mask black {variant}")
    visual = audit["method"]["human_review"]
    require(visual["pass12_player25_exact_top_gates"] == "7/7", "proof visual gates")
    require(visual["pass12_player25_overlap_clipping_or_ambiguity"] is False, "proof visual ambiguity")
    require(visual["sealed_v8_scene_specific_status_complete_under_player25"] is False, "sealed lower boundary loss")
    guard = load("MINIMUM_SCALE_OBSTRUCTION_GUARD_PASS18.json")
    require(guard["guard_id"] == "spin-worker-yui-pass18-minimum-scale-obstruction-20260808T112707K", "guard id")
    require(guard["disposition"] == "INTEGRATION_GUARD_NOT_PIXEL_CORRECTION", "guard action")
    require(guard["pixel_action"]["new_pixel_or_copy_correction_requested"] is False, "guard correction")
    require(guard["pixel_action"]["sealed_v8_modified"] is False and guard["pixel_action"]["v9_created"] is False, "guard custody")
    blocker = load("BLOCKER_PACKET_PASS18.json")
    require(blocker["packet_id"] == "spin-worker-yui-pass18-blockers-20260808T112707K", "blocker id")
    require(blocker["blockers"][0]["status"] == "OPEN" and blocker["blockers"][1]["status"] == "OPEN", "science blockers")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    snapshot = load("qa/pass18_review_snapshot_v1.json")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass18-review-v1-20260808T112928K", "snapshot id")
    require(snapshot["pass18"]["video_reportable_now"] is False, "snapshot reportability")
    require(snapshot["safety"]["writes_confined_to_worker_lane"] is True, "snapshot lane custody")
    require(not any([
        snapshot["safety"]["tts_invoked"], snapshot["safety"]["audio_generated"],
        snapshot["safety"]["video_encoded"], snapshot["safety"]["published"],
        snapshot["safety"]["shared_or_public_assets_modified"], snapshot["safety"]["git_action"],
    ]), "snapshot negative actions")
    extraction_time = datetime.fromisoformat(load("qa/pass18_minimum_scale_obstruction_audit/extraction_receipt.json")["created_at"])
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
    snapshot = load("qa/pass18_review_snapshot_v1.json")
    require(snapshot["representation_boundary"]["required_header"] == "GALAXY SPIN", "required header")
    require(snapshot["representation_boundary"]["forbidden_audience_topics_absent_from_method_frames"] is True, "forbidden audience topics")
    media = [
        path for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.casefold() in {".mp4", ".mp3", ".wav", ".aac", ".m4a"}
    ]
    require(not media, "no encoded media in lane")


def check_handoff() -> None:
    status = load("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS18_MINIMUM_SCALE_OBSTRUCTION_GUARD_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS18_COMPLETE", "status marker")
    require(status["video_reportable_now"] is False, "status reportability")
    require(status["pass18_minimum_scale_obstruction_guard_added"] is True, "status guard")
    require(status["pass18_new_pixel_or_copy_correction_requested"] is False, "status action")
    lane = (ROOT / "LANE_RECEIPT.md").read_text()
    require("PASS18_DEEPENING_MARKER_V1" in lane, "lane marker")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
    require("Pass 18 adds the compound minimum-scale/obstruction integration guard" in request, "integrator request")
    qa = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
    require("Pass-18 compound minimum-scale/obstruction stress QA" in qa, "static QA")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-only", action="store_true")
    args = parser.parse_args()
    check_pins()
    check_extraction()
    check_method()
    check_audit_and_packets()
    check_static_and_no_media()
    if not args.evidence_only:
        check_handoff()
    suffix = "evidence-only" if args.evidence_only else "status-handoff"
    print(f"PASS pass18 snapshot/candidate/80-compound-frames/hierarchy/105-method-derivatives/minimum-scale-obstruction-guard/source-blockers/{suffix}/no-media")


if __name__ == "__main__":
    main()
