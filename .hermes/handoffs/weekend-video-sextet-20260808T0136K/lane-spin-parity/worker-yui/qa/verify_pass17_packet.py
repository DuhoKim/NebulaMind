#!/usr/bin/env python3
"""Verify pass-17 minimum-scale/recompression evidence, custody, and handoff."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
VARIANTS: dict[str, int | None] = {
    "clean": None,
    "downscale_360p": None,
    "jpeg_q60_420_360p": 60,
    "jpeg_q35_420_360p": 35,
    "jpeg_q20_420_360p": 20,
}
PINNED = {
    "SOURCE_STATUS_FREEZE.json": "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1",
    "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
    "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
    "proposal_frames/v8/contact_sheet.png": "5889dfcbcb7f24afe989411b127a5c30adb9e4685513058eca9d51cc0cf32056",
    "SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json": "1312ea54aa860473ff57e3c47e8305ecca8630ba1f6a998a6e02d9aea9999422",
    "qa/pass12_sharpness_safe_mockup/receipt.json": "35f526a60b053f8c203278b3c205c1e0145f9a6dcd6da309541eb57b6399e92c",
    "qa/pass16_review_snapshot_v1.json": "1205b66b3ccf7080d1f3c5c1eaf9856a2bedc7f14ba2924a7591cd8a48577d40",
    "qa/extract_pass17_minimum_scale_recompression_frames.py": "1c4f1f984e7067545b3cf045610951f936d25256db3e3f0d807ae99073e990a2",
    "qa/pass17_minimum_scale_recompression_audit/extraction_receipt.json": "ab7d1cdee0f5e82fb5d8b51cbcab324bb24036975606ac3a2a7f1833f0468d47",
    "qa/build_pass17_v8_minimum_scale_recompression.py": "782252eacedbeba545574d88c6b4381618d7db63596e42804785c92593ffbbad",
    "qa/pass17_v8_minimum_scale_recompression/receipt.json": "388e244eff1e399d153dcb8be7c0916291e3b5d11bd4fb1ad902abb8e8c8e6e9",
    "qa/audit_pass17_minimum_scale_recompression.py": "7125d465a4d17ff650d55ee75cd1229c13c5e2e4c84dbc50bb5ce5ab84f97edd",
    "qa/pass17_minimum_scale_recompression_quantitative_audit.json": "d21b50e9aded285a089367ce48504c87e0930aa2528a025cbb729d636ac76dde",
    "MINIMUM_SCALE_RECOMPRESSION_GUARD_PASS17.json": "a7849a58105145f9d7f62c8c795758e3bfba59cfbb32b60de8057cdb7bff217d",
    "PASS17_ENCODED_FRAME_AUDIT.md": "e48d02506eeef4507c409b0cddd747d016168c453aa94e71f212406942a38d90",
    "BLOCKER_PACKET_PASS17.json": "c3de86e4cf83d86eacabfdec3888480ccc934b75e63f3c58409a58dafb2dbb04",
    "qa/pass17_review_snapshot_v1.json": "2c17757ef56a94cc0cacb29d8eebfc3e682eb2c34042ca012b18efb7ffc700be",
}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {label}")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(rel: str):
    return json.loads((ROOT / rel).read_text())


def derive(clean: Image.Image, variant: str) -> tuple[Image.Image, str | None, int | None]:
    if variant == "clean":
        return clean.convert("RGB"), None, None
    represented = clean.convert("RGB").resize((640, 360), Image.Resampling.LANCZOS)
    quality = VARIANTS[variant]
    if quality is None:
        return represented, None, None
    buffer = io.BytesIO()
    represented.save(
        buffer,
        format="JPEG",
        quality=quality,
        subsampling=2,
        optimize=False,
        progressive=False,
    )
    jpeg_bytes = buffer.getvalue()
    with Image.open(io.BytesIO(jpeg_bytes)) as decoded:
        output = decoded.convert("RGB")
    return output, hashlib.sha256(jpeg_bytes).hexdigest(), len(jpeg_bytes)


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
    expected, jpeg_hash, jpeg_bytes = derive(clean, variant)
    with Image.open(path).convert("RGB") as observed:
        expected_size = (1920, 1080) if variant == "clean" else (640, 360)
        require(observed.size == expected_size, f"dimensions {label}")
        require(image_equal(expected, observed), f"transform pixels {label}")
    require(sample["jpeg_sha256"] == jpeg_hash, f"jpeg hash {label}")
    require(sample["jpeg_bytes"] == jpeg_bytes, f"jpeg bytes {label}")


def check_extraction() -> None:
    receipt = load("qa/pass17_minimum_scale_recompression_audit/extraction_receipt.json")
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE, "extraction candidate")
    require(receipt["cut_detection"]["cuts"] == EXPECTED_CUTS, "fresh cuts")
    require(receipt["cut_detection"]["cuts"] == load("qa/pass16_minimum_scale_geometry_audit/extraction_receipt.json")["cut_detection"]["cuts"], "pass16 cut match")
    require(receipt["scene_count"] == 16 and receipt["variant_count"] == 5 and receipt["frame_count"] == 80, "candidate census")
    require(receipt["fresh_clean_match"] == "16/16_BYTE_IDENTICAL_TO_PASS16", "clean reproduction marker")
    require(receipt["operational_variants"] == ["downscale_360p", "jpeg_q60_420_360p"], "operational variants")
    require(receipt["characterization_variants"] == ["jpeg_q35_420_360p", "jpeg_q20_420_360p"], "characterization variants")
    require(len(receipt["records"]) == 16, "record count")
    for record in receipt["records"]:
        scene = int(record["scene"])
        samples = {sample["variant"]: sample for sample in record["samples"]}
        require(set(samples) == set(VARIANTS), f"candidate variants scene {scene}")
        clean_path = ROOT / "qa/pass17_minimum_scale_recompression_audit" / samples["clean"]["frame"]
        prior = ROOT / record["prior_pass16_clean_path"]
        require(sha(clean_path) == sha(prior) == record["prior_pass16_clean_sha256"], f"candidate clean scene {scene}")
        with Image.open(clean_path).convert("RGB") as clean:
            require(clean.size == (1920, 1080), f"candidate clean dimensions {scene}")
            for variant in VARIANTS:
                path = ROOT / "qa/pass17_minimum_scale_recompression_audit" / samples[variant]["frame"]
                check_sample(clean, samples[variant], path, f"candidate/{scene}/{variant}")
    for variant, sheet in receipt["contact_sheets"].items():
        path = ROOT / "qa/pass17_minimum_scale_recompression_audit" / sheet["path"]
        require(sha(path) == sheet["sha256"], f"candidate sheet {variant}")
        with Image.open(path) as image:
            require(image.size == (1892, 1276), f"candidate sheet dimensions {variant}")


def check_method() -> None:
    receipt = load("qa/pass17_v8_minimum_scale_recompression/receipt.json")
    require(receipt["group_count"] == 3 and receipt["scene_count"] == 21 and receipt["frame_count"] == 105, "method census")
    require(set(receipt["groups"]) == {"sealed_v8", "pass7_caption_safe", "pass12_sharpness_safe"}, "method groups")
    require(receipt["operational_variants"] == ["downscale_360p", "jpeg_q60_420_360p"], "method operational variants")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"group census {group_name}")
        for row in group["scenes"]:
            scene = int(row["scene"])
            source = ROOT / row["source"]
            require(sha(source) == row["source_sha256"], f"method source {group_name}/{scene}")
            with Image.open(source).convert("RGB") as clean:
                require(clean.size == (1920, 1080), f"method source dimensions {group_name}/{scene}")
                for sample in row["samples"]:
                    path = ROOT / "qa/pass17_v8_minimum_scale_recompression" / group_name / sample["frame"]
                    check_sample(clean, sample, path, f"method/{group_name}/{scene}/{sample['variant']}")
        for variant, sheet in group["contact_sheets"].items():
            path = ROOT / "qa/pass17_v8_minimum_scale_recompression" / group_name / sheet["path"]
            require(sha(path) == sheet["sha256"], f"method sheet {group_name}/{variant}")
            with Image.open(path) as image:
                require(image.size == (1280, 1576), f"method sheet dimensions {group_name}/{variant}")


def near(actual, expected: float, label: str) -> None:
    require(math.isclose(float(actual), expected, abs_tol=1e-6), label)


def check_audit_and_packets() -> None:
    audit = load("qa/pass17_minimum_scale_recompression_quantitative_audit.json")
    require(audit["deepening_pass"] == 17 and audit["raw_ocr_text_stored"] is False, "audit contract")
    candidate = audit["candidate"]["aggregates"]
    expected = {
        "downscale_360p": (0.957977, 0.76231, 0.355206, 0.508145),
        "jpeg_q60_420_360p": (0.936728, 0.7522, 0.340235, 0.480409),
        "jpeg_q35_420_360p": (0.936728, 0.733435, 0.332694, 0.458181),
        "jpeg_q20_420_360p": (0.944572, 0.680946, 0.290992, 0.458181),
    }
    keys = [
        "mean_headline_token_recall_vs_native_clean", "mean_full_token_recall_vs_native_clean",
        "mean_lower_support_token_recall_vs_native_clean", "mean_numeric_token_recall_vs_native_clean",
    ]
    for variant, values in expected.items():
        row = candidate[variant]
        for key, value in zip(keys, values):
            near(row[key], value, f"candidate {variant} {key}")
        require(row["structural_gate_scene_count"] == 0, f"candidate gates {variant}")
    proof = audit["pass12_mapped_gate_crop_character_similarity"]
    similarities = {"downscale_360p": 1.0, "jpeg_q60_420_360p": 1.0, "jpeg_q35_420_360p": 1.0, "jpeg_q20_420_360p": 0.988874}
    for variant, similarity in similarities.items():
        require(proof[variant]["passing_gate_count"] == 7, f"proof gates {variant}")
        near(proof[variant]["mean_best_similarity"], similarity, f"proof similarity {variant}")
    visual = audit["human_visual_review"]
    require(visual["candidate_structural_hold_visible_any_variant"] is False, "visual candidate gates")
    require(visual["pass12_overlap_clipping_or_semantic_ambiguity_any_variant"] is False, "proof visual ambiguity")
    require(visual["pass12_specific_gate_lines_q60_360p"] == "7/7", "proof visual gates")
    guard = load("MINIMUM_SCALE_RECOMPRESSION_GUARD_PASS17.json")
    require(guard["guard_id"] == "spin-worker-yui-pass17-minimum-scale-recompression-20260808T110306K", "guard id")
    require(guard["action"]["type"] == "INTEGRATION_GUARD_NOT_PIXEL_CORRECTION", "guard action")
    require(guard["scope"]["v9_created"] is False and guard["scope"]["sealed_v8_modified"] is False, "guard custody")
    blocker = load("BLOCKER_PACKET_PASS17.json")
    require(blocker["packet_id"] == "spin-worker-yui-pass17-blockers-20260808T110306K", "blocker id")
    require(blocker["blockers"][0]["status"] == "BLOCKING" and blocker["blockers"][1]["status"] == "BLOCKING", "science blockers")
    require(blocker["video_reportable_now"] is False, "blocker reportability")
    snapshot = load("qa/pass17_review_snapshot_v1.json")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass17-review-v1-20260808T110626K", "snapshot id")
    require(snapshot["pass17"]["video_reportable_now"] is False, "snapshot reportability")
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
    snapshot = load("qa/pass17_review_snapshot_v1.json")
    require(snapshot["representation_boundary"]["required_header"] == "GALAXY SPIN", "required header")
    require(snapshot["representation_boundary"]["forbidden_audience_topics_absent_from_method_frames"] is True, "forbidden audience topics")
    media = [
        path for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.casefold() in {".mp4", ".mp3", ".wav", ".aac", ".m4a"}
    ]
    require(not media, "no encoded media in lane")


def check_handoff() -> None:
    status = load("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS17_MINIMUM_SCALE_RECOMPRESSION_GUARD_V1", "status phase")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS17_COMPLETE", "status marker")
    require(status["video_reportable_now"] is False, "status reportability")
    require(status["pass17_minimum_scale_recompression_guard_added"] is True, "status guard")
    require(status["pass17_new_pixel_or_copy_correction_requested"] is False, "status action")
    lane = (ROOT / "LANE_RECEIPT.md").read_text()
    require("PASS17_DEEPENING_MARKER_V1" in lane, "lane marker")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
    require("Pass 17 adds the compound minimum-scale/recompression integration guard" in request, "integrator request")
    qa = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
    require("Pass-17 compound minimum-scale/recompression stress QA" in qa, "static QA")


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
    print(f"PASS pass17 snapshot/candidate/80-compound-frames/hierarchy/105-method-derivatives/minimum-scale-recompression-guard/source-blockers/{suffix}/no-media")


if __name__ == "__main__":
    main()
