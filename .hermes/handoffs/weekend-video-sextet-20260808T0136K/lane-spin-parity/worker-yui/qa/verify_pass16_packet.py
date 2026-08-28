#!/usr/bin/env python3
"""Verify pass-16 compound minimum-scale/geometry evidence, custody, and handoff."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
VARIANTS = {
    "clean": (1.0, 1.0),
    "x90_360p": (0.9, 1.0),
    "y90_360p": (1.0, 0.9),
    "x80_360p": (0.8, 1.0),
    "y80_360p": (1.0, 0.8),
}
PINNED = {
    "SOURCE_STATUS_FREEZE.json": "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1",
    "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
    "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
    "proposal_frames/v8/contact_sheet.png": "5889dfcbcb7f24afe989411b127a5c30adb9e4685513058eca9d51cc0cf32056",
    "SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json": "1312ea54aa860473ff57e3c47e8305ecca8630ba1f6a998a6e02d9aea9999422",
    "qa/pass12_sharpness_safe_mockup/receipt.json": "35f526a60b053f8c203278b3c205c1e0145f9a6dcd6da309541eb57b6399e92c",
    "qa/pass15_review_snapshot_v1.json": "8d911cc0d6abbf12e95be30420fd33018e18668ba5907edd990bc1f34e599428",
    "qa/extract_pass16_minimum_scale_geometry_frames.py": "61b3b8566c7610bfe6cd46b644b69aaff34b9f36bd8d60689256aa0df78710a1",
    "qa/pass16_minimum_scale_geometry_audit/extraction_receipt.json": "c8667ff898e65d0b73eb4c5d64311b834354b693e8dd92879fad5336d65764b7",
    "qa/build_pass16_v8_minimum_scale_geometry.py": "2a3c034743c13b7068e8c88d55eecb57225f8f610fbeb70e16952de95cf33b3e",
    "qa/pass16_v8_minimum_scale_geometry/receipt.json": "88b491d3cfa542dac2ea328ce07c207a0901d83570aa175b26b360018fcff42d",
    "qa/audit_pass16_minimum_scale_geometry.py": "5965fe1a77890307b28c6890b7e49c9aef43bbdbccd86e058c78ebda6629de8c",
    "qa/pass16_minimum_scale_geometry_quantitative_audit.json": "fdc613e9dd0b949ae52a8d07a32460835b4d6895ba522f7d6836701448091dcc",
    "MINIMUM_SCALE_GEOMETRY_GUARD_PASS16.json": "290f738abc390a5fb1b43354819c032b9a8446d559d0c5fcb783330196d90e5d",
    "PASS16_ENCODED_FRAME_AUDIT.md": "474e720480c3ac3f48260fea698476dfc18b44c464ee726bf21776bd326bae28",
    "BLOCKER_PACKET_PASS16.json": "a82ce693b176d9d137af9f355d70417a35d056d80356a261b42606e230a7ca51",
    "qa/pass16_review_snapshot_v1.json": "1205b66b3ccf7080d1f3c5c1eaf9856a2bedc7f14ba2924a7591cd8a48577d40",
}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {label}")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(rel: str):
    return json.loads((ROOT / rel).read_text())


def transform(image: Image.Image, sx: float, sy: float) -> Image.Image:
    w, h = image.size
    nw, nh = round(w * sx), round(h * sy)
    squeezed = image.resize((nw, nh), Image.Resampling.LANCZOS)
    native = Image.new("RGB", (w, h), (0, 0, 0))
    native.paste(squeezed, ((w - nw) // 2, (h - nh) // 2))
    return native.resize((640, 360), Image.Resampling.LANCZOS)


def image_equal(a: Image.Image, b: Image.Image) -> bool:
    return ImageChops.difference(a.convert("RGB"), b.convert("RGB")).getbbox() is None


def check_pins() -> None:
    require(sha(CANDIDATE) == EXPECTED_CANDIDATE, "candidate custody")
    for rel, expected in PINNED.items():
        require((ROOT / rel).is_file(), f"missing {rel}")
        require(sha(ROOT / rel) == expected, f"hash {rel}")


def check_extraction() -> None:
    receipt = load("qa/pass16_minimum_scale_geometry_audit/extraction_receipt.json")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE, "extraction candidate")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "fresh cuts")
    require(receipt["scene_count"] == 16 and receipt["variant_count"] == 5 and receipt["frame_count"] == 80, "candidate census")
    require(receipt["fresh_clean_match"] == "16/16_BYTE_IDENTICAL_TO_PASS15", "clean reproduction marker")
    require(receipt["operational_variants"] == ["x90_360p", "y90_360p"], "operational pair")
    require(receipt["characterization_variants"] == ["x80_360p", "y80_360p"], "characterization pair")
    require(len(receipt["records"]) == 16, "record count")
    for record in receipt["records"]:
        scene = int(record["scene"])
        samples = {sample["variant"]: sample for sample in record["samples"]}
        require(set(samples) == set(VARIANTS), f"candidate variants scene {scene}")
        clean_path = ROOT / "qa/pass16_minimum_scale_geometry_audit" / samples["clean"]["frame"]
        prior = ROOT / record["prior_pass15_clean_path"]
        require(sha(clean_path) == sha(prior) == record["prior_pass15_clean_sha256"], f"candidate clean scene {scene}")
        with Image.open(clean_path).convert("RGB") as clean:
            require(clean.size == (1920, 1080), f"candidate clean dimensions {scene}")
            for variant, (sx, sy) in VARIANTS.items():
                path = ROOT / "qa/pass16_minimum_scale_geometry_audit" / samples[variant]["frame"]
                require(sha(path) == samples[variant]["sha256"], f"candidate frame hash {scene}/{variant}")
                with Image.open(path).convert("RGB") as observed:
                    expected = clean if variant == "clean" else transform(clean, sx, sy)
                    expected_size = (1920, 1080) if variant == "clean" else (640, 360)
                    require(observed.size == expected_size, f"candidate dimensions {scene}/{variant}")
                    require(image_equal(expected, observed), f"candidate transform {scene}/{variant}")
    for variant, sheet in receipt["contact_sheets"].items():
        path = ROOT / "qa/pass16_minimum_scale_geometry_audit" / sheet["path"]
        require(sha(path) == sheet["sha256"], f"candidate contact sheet {variant}")
        with Image.open(path) as image:
            require(image.size == (1892, 1276), f"candidate contact dimensions {variant}")


def check_method() -> None:
    receipt = load("qa/pass16_v8_minimum_scale_geometry/receipt.json")
    require(receipt["group_count"] == 3 and receipt["scene_count"] == 21 and receipt["frame_count"] == 105, "method census")
    require(set(receipt["groups"]) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method groups")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"group census {group_name}")
        for row in group["scenes"]:
            scene = int(row["scene"])
            source = ROOT / row["source"]
            require(sha(source) == row["source_sha256"], f"method source {group_name}/{scene}")
            with Image.open(source).convert("RGB") as clean:
                require(clean.size == (1920, 1080), f"method source dimensions {group_name}/{scene}")
                for sample in row["samples"]:
                    variant = sample["variant"]
                    path = ROOT / "qa/pass16_v8_minimum_scale_geometry" / group_name / sample["frame"]
                    require(sha(path) == sample["frame_sha256"], f"method hash {group_name}/{scene}/{variant}")
                    with Image.open(path).convert("RGB") as observed:
                        expected = clean if variant == "clean" else transform(clean, *VARIANTS[variant])
                        require(image_equal(expected, observed), f"method transform {group_name}/{scene}/{variant}")
        for variant, sheet in group["contact_sheets"].items():
            path = ROOT / "qa/pass16_v8_minimum_scale_geometry" / group_name / sheet["path"]
            require(sha(path) == sheet["sha256"], f"method sheet {group_name}/{variant}")
            with Image.open(path) as image:
                require(image.size == (1180, 1528), f"method sheet dimensions {group_name}/{variant}")


def near(actual, expected, label: str) -> None:
    require(math.isclose(float(actual), expected, abs_tol=1e-6), label)


def check_audit_and_packets() -> None:
    audit = load("qa/pass16_minimum_scale_geometry_quantitative_audit.json")
    require(audit["deepening_pass"] == 16 and audit["raw_ocr_text_stored"] is False, "audit contract")
    candidate = audit["candidate"]["aggregates"]
    expected = {
        "x90_360p": (0.92055, 0.72607, 0.682688, 0.449145),
        "y90_360p": (0.912103, 0.75736, 0.717162, 0.461298),
        "x80_360p": (0.910056, 0.673028, 0.618756, 0.437099),
        "y80_360p": (0.89803, 0.729645, 0.687699, 0.438835),
    }
    for variant, values in expected.items():
        row = candidate[variant]
        for key, value in zip([
            "mean_headline_token_recall_vs_clean", "mean_full_token_recall_vs_clean",
            "mean_lower_support_token_recall_vs_clean", "mean_numeric_token_recall_vs_clean",
        ], values):
            near(row[key], value, f"candidate {variant} {key}")
        require(row["structural_gate_scene_count"] == 0, f"candidate gates {variant}")
    proof = audit["method_groups"]["pass12_sharpness_safe"]["aggregates"]
    similarities = {"x90_360p": 1.0, "y90_360p": 0.973463, "x80_360p": 1.0, "y80_360p": 0.979486}
    for variant, expected_similarity in similarities.items():
        require(proof[variant]["scene_specific_gate_count"] == 7, f"proof gates {variant}")
        near(proof[variant]["mean_gate_character_similarity_best_of_psm_6_7_11_13"], expected_similarity, f"proof similarity {variant}")
    visual = audit["human_visual_review"]
    require(visual["candidate_structural_gate_scenes"]["x90_360p"] == "0/16", "visual candidate gates")
    require(visual["pass12_no_overlap_clipping_or_semantic_ambiguity"] is True, "proof visual ambiguity")
    require(visual["pass12_operational_specific_gate_lines_visual"]["x90_360p"] == "7/7_EXACT", "proof visual gates")
    guard = load("MINIMUM_SCALE_GEOMETRY_GUARD_PASS16.json")
    require(guard["guard_id"] == "spin-worker-yui-pass16-minimum-scale-geometry-20260808T103416K", "guard id")
    require(guard["action"]["type"] == "INTEGRATION_GUARD_NOT_PIXEL_CORRECTION", "guard action")
    require(guard["scope"]["v9_created"] is False and guard["scope"]["sealed_v8_modified"] is False, "guard custody")
    blocker = load("BLOCKER_PACKET_PASS16.json")
    require(blocker["packet_id"] == "spin-worker-yui-pass16-blockers-20260808T103416K", "blocker id")
    require(blocker["blockers"][0]["status"] == "BLOCKING" and blocker["blockers"][1]["status"] == "BLOCKING", "science blockers")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    snapshot = load("qa/pass16_review_snapshot_v1.json")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass16-review-v1-20260808T103709K", "snapshot id")
    require(snapshot["pass16"]["video_reportable_now"] is False, "snapshot reportability")
    require(snapshot["safety"]["writes_confined_to_worker_lane"] is True, "snapshot lane custody")
    require(not any([
        snapshot["safety"]["tts_invoked"], snapshot["safety"]["audio_generated"],
        snapshot["safety"]["video_encoded"], snapshot["safety"]["published"],
        snapshot["safety"]["shared_or_public_assets_modified"], snapshot["safety"]["git_action"],
    ]), "snapshot negative actions")


def check_static_and_no_media() -> None:
    freeze = load("SOURCE_STATUS_FREEZE.json")
    require(freeze["video_reportable_now"] is False, "freeze reportability")
    story = load("STORYBOARD_PROPOSAL.json")
    require(story["status"] == "PROPOSAL_ONLY_NOT_A_CANDIDATE" and story["video_reportable_now"] is False, "story status")
    static = load("qa/static_proposal_validation.json")
    require(static.get("verdict") == "PASS", "static validation")
    snapshot = load("qa/pass16_review_snapshot_v1.json")
    require(snapshot["representation_boundary"]["required_header"] == "GALAXY SPIN", "required header")
    require(snapshot["representation_boundary"]["forbidden_audience_topics_absent_from_method_frames"] is True, "forbidden audience topics")
    media = [
        path for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.casefold() in {".mp4", ".mp3", ".wav", ".aac", ".m4a"}
    ]
    require(not media, "no encoded media in lane")


def check_handoff() -> None:
    status = load("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS16_MINIMUM_SCALE_GEOMETRY_GUARD_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS16_COMPLETE", "status marker")
    require(status["video_reportable_now"] is False, "status reportability")
    require(status["pass16_minimum_scale_geometry_guard_added"] is True, "status guard")
    require(status["pass16_new_pixel_or_copy_correction_requested"] is False, "status action")
    lane = (ROOT / "LANE_RECEIPT.md").read_text()
    require("PASS16_DEEPENING_MARKER_V1" in lane, "lane marker")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
    require("Pass 16 adds the compound minimum-scale/geometry integration guard" in request, "integrator request")
    qa = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
    require("Pass-16 compound minimum-scale/geometry stress QA" in qa, "static QA")


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
    print(f"PASS pass16 snapshot/candidate/80-compound-frames/hierarchy/105-method-derivatives/minimum-scale-geometry-guard/source-blockers/{suffix}/no-media")


if __name__ == "__main__":
    main()
