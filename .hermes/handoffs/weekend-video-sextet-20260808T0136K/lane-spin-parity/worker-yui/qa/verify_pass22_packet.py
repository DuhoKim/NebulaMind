#!/usr/bin/env python3
"""Verify pass-22 native-dark-tone/minimum-scale evidence and handoff."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
CAND_DIR = ROOT / "qa/pass22_minimum_scale_dark_tone_audit"
METHOD_DIR = ROOT / "qa/pass22_v8_minimum_scale_dark_tone"
EXPECTED_CANDIDATE_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
FLOORS = {"floor16_then_360p": 16, "floor32_then_360p": 32, "floor48_then_360p": 48}
EXPECTED = {
    "extractor": "7d5865dbedb6c90e11638456d0085e50b73c5be9da49d821a0868ba74020a3d6",
    "candidate_receipt": "760f3ffb4772e8a911106694031f990776615e5d340987533bcbef4c48cb6d12",
    "builder": "c776e5fd231ca486b1a7b0233dc4fced73d11a8e59cb2e2f03868f62d685cf40",
    "method_receipt": "5b59cf6db01d18acfc02513725af4c2c41c172524de2ba7e67edfa857b8533ba",
    "auditor": "848ef4d7b7a114b17c041b001878866567be6b6587429cfdf88e76efbcc430a2",
    "audit": "119e08e5c91d02f8dc4adf8041ed62bcb24f25090151dc07de80955db237f07d",
    "guard": "0ab14f9dc005b573cd637465a4ca7b04e301d0a4fa895f4be891cfc4172af6d8",
    "narrative": "05e3c5663344c1e21a89cabc2c63bfdf9d8872552e5948983e78a6692f8a377c",
    "blocker": "f0f564a4910aa9fbe415b554125ec3dfe3654cbeb9e3f555427c055a96d30500",
}
PATHS = {
    "extractor": ROOT / "qa/extract_pass22_minimum_scale_dark_tone_frames.py",
    "candidate_receipt": CAND_DIR / "extraction_receipt.json",
    "builder": ROOT / "qa/build_pass22_v8_minimum_scale_dark_tone.py",
    "method_receipt": METHOD_DIR / "receipt.json",
    "auditor": ROOT / "qa/audit_pass22_minimum_scale_dark_tone.py",
    "audit": ROOT / "qa/pass22_minimum_scale_dark_tone_quantitative_audit.json",
    "guard": ROOT / "MINIMUM_SCALE_DARK_TONE_GUARD_PASS22.json",
    "narrative": ROOT / "PASS22_ENCODED_FRAME_AUDIT.md",
    "blocker": ROOT / "BLOCKER_PACKET_PASS22.json",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL {message}")


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def integer_luma(values: np.ndarray) -> np.ndarray:
    data = values.astype(np.uint32)
    return ((54 * data[:, :, 0] + 183 * data[:, :, 1] + 19 * data[:, :, 2] + 128) // 256).astype(np.uint16)


def derive(native: Image.Image, floor: int) -> np.ndarray:
    values = np.asarray(native.convert("RGB"), dtype=np.uint8)
    lum = integer_luma(values).astype(np.uint32)
    numerator = np.maximum(lum.astype(np.int32) - floor, 0).astype(np.uint32) * 255
    remapped = (numerator + (255 - floor) // 2) // (255 - floor)
    output = np.zeros_like(values, dtype=np.uint8)
    nonzero = lum > 0
    for channel in range(3):
        scaled = np.zeros_like(lum, dtype=np.uint32)
        scaled[nonzero] = (
            values[:, :, channel].astype(np.uint32)[nonzero] * remapped[nonzero]
            + lum[nonzero] // 2
        ) // lum[nonzero]
        output[:, :, channel] = np.clip(scaled, 0, 255).astype(np.uint8)
    represented = Image.fromarray(output).resize((640, 360), Image.Resampling.LANCZOS)
    return np.asarray(represented, dtype=np.uint8)


def check_pins() -> None:
    require(sha(CANDIDATE) == EXPECTED_CANDIDATE_SHA, "candidate hash")
    for name, path in PATHS.items():
        require(path.is_file(), f"missing {name}")
        require(sha(path) == EXPECTED[name], f"pinned hash {name}")
    authority = {
        ROOT.parent.parent / "HWAO_WEEKEND_ORDER.md": "ac5d35314a3af78ab2214b62105fa74afb616862aeeb2d09faa1dd6eb1c84710",
        ROOT.parent.parent / "COORDINATION_UPDATE.md": "2d64667f8ab95349b344c9098a4f2b8f675c71d53d1cc132a780e0ac699fde1f",
        ROOT.parent.parent / "lanes/spin/BRIEF.md": "af91d7a84ddfce470500189546cb7b8d109d4eaaf2c3451f468807c0b5cd4aec",
        ROOT / "SOURCE_STATUS_FREEZE.json": "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1",
        ROOT / "STORYBOARD_PROPOSAL.json": "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce",
        ROOT / "proposal_frames/v8/render_receipt.json": "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3",
        ROOT / "qa/pass21_review_snapshot_v1.json": "f2cb324f1d55a1710b9debd865d73ab02c10735076f040c2dee22ee0b2af81c5",
    }
    for path, expected in authority.items():
        require(sha(path) == expected, f"authority/custody {path.name}")


def check_candidate() -> None:
    receipt = json.loads(PATHS["candidate_receipt"].read_text())
    require(receipt["candidate_sha256"] == EXPECTED_CANDIDATE_SHA, "receipt candidate")
    require(receipt["cut_times_seconds"] == EXPECTED_CUTS, "cuts")
    require(receipt["scene_count"] == 16 and receipt["frame_count"] == 80 and receipt["variant_count"] == 5, "candidate census")
    require(receipt["fresh_clean_match"] == "16/16_BYTE_IDENTICAL_TO_PASS21", "fresh clean custody")
    require(receipt["operational_variants"] == ["floor16_then_360p"], "operational variant")
    exact = {variant: 0 for variant in FLOORS}
    for record in receipt["records"]:
        require(len(record["samples"]) == 5 and record["fresh_clean_byte_identical"], "candidate row")
        sample_map = {sample["variant"]: sample for sample in record["samples"]}
        clean_path = CAND_DIR / sample_map["clean"]["frame"]
        require(sha(clean_path) == sample_map["clean"]["sha256"], "clean frame hash")
        require(sha(clean_path) == record["prior_pass21_clean_sha256"], "prior clean frame")
        with Image.open(clean_path) as opened:
            native = opened.convert("RGB")
        require(native.size == (1920, 1080), "native dimensions")
        for variant, floor in FLOORS.items():
            sample = sample_map[variant]
            path = CAND_DIR / sample["frame"]
            require(sha(path) == sample["sha256"], "candidate derivative hash")
            with Image.open(path) as observed:
                pixels = np.asarray(observed.convert("RGB"), dtype=np.uint8)
                require(observed.size == (640, 360), "candidate represented dimensions")
            exact[variant] += int(np.array_equal(derive(native, floor), pixels))
    require(all(count == 16 for count in exact.values()), "candidate exact transform")
    require(len(receipt["contact_sheets"]) == 5, "candidate sheets")


def check_method() -> None:
    receipt = json.loads(PATHS["method_receipt"].read_text())
    require(receipt["group_count"] if "group_count" in receipt else len(receipt["groups"]) == 3, "method groups")
    require(receipt["scene_count"] == 21 and receipt["frame_count"] == 105, "method census")
    require(receipt["operational_variant"] == "floor16_then_360p", "method operational")
    for group_name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, "method group census")
        require(len(group["contact_sheets"]) == 5, "method sheets")
        for scene in group["scenes"]:
            source = ROOT / scene["source"]
            require(sha(source) == scene["source_sha256"] and scene["clean_copy_sha256_match"], "method clean custody")
            with Image.open(source) as opened:
                native = opened.convert("RGB")
            sample_map = {sample["variant"]: sample for sample in scene["samples"]}
            for variant, floor in FLOORS.items():
                sample = sample_map[variant]
                path = METHOD_DIR / group_name / sample["frame"]
                require(sha(path) == sample["sha256"], "method derivative hash")
                with Image.open(path) as observed:
                    pixels = np.asarray(observed.convert("RGB"), dtype=np.uint8)
                require(np.array_equal(derive(native, floor), pixels), "method exact transform")


def check_audit_and_boundary() -> None:
    audit = json.loads(PATHS["audit"].read_text())
    operational = audit["candidate"]["aggregate"]["floor16_then_360p"]
    critical = audit["candidate"]["held_critical_scenes_7_9_10_11_16"]["floor16_then_360p"]
    proof = audit["method"]["pass12_sharpness_safe"]["variants"]["floor16_then_360p"]
    require(operational["headline_recall"] == 0.894444 and operational["full_recall"] == 0.635932, "candidate OCR metrics")
    require(operational["lower_recall"] == 0.25618 and operational["numeric_recall"] == 0.288889, "candidate support metrics")
    require(operational["structural_gate_scene_count"] == 0 and critical["structural_gate_scene_count"] == 0, "candidate structural gates")
    require(operational["exact_transform_recomputed_scenes"] == 16, "audit exact candidate")
    require(proof["gate_count_passing_threshold"] == 7 and proof["exact_transform_recomputed_scenes"] == 7, "proof gates")
    require(proof["mean_best_similarity"] == 0.967458, "proof similarity")
    human = audit["method"]["human_review"]
    require(human["sealed_v8_floor16_then_360p_result_held_badges"] == "7/7", "sealed badges")
    require(human["pass12_floor16_then_360p_exact_top_gates"] == "7/7", "visual gates")
    require(not human["pass12_floor16_then_360p_overlap_clipping_or_ambiguity"], "no visual defect")
    guard = json.loads(PATHS["guard"].read_text())
    require(guard["status"] == "PROPOSAL_ONLY_INTEGRATION_GUARD_NOT_V9_NOT_A_CANDIDATE", "guard status")
    require(not guard["pixel_action"]["new_pixel_or_copy_correction_requested"], "no cosmetic correction")
    blocker = json.loads(PATHS["blocker"].read_text())
    require([row["status"] for row in blocker["blockers"]] == ["OPEN", "OPEN", "OPEN"], "blockers open")
    require(blocker["blockers"][1]["authority"]["terminal_status"] == "FRAME REVIEW: AGREES FRAME_UNSTATED", "frame terminal status")
    snapshot = json.loads((ROOT / "qa/pass22_review_snapshot_v1.json").read_text())
    require(snapshot["pass22"]["action"] == "INTEGRATION_GUARD_NOT_PIXEL_CORRECTION", "snapshot action")
    require(snapshot["representation_boundary"]["required_header"] == "GALAXY SPIN", "header boundary")
    require(snapshot["representation_boundary"]["forbidden_audience_topics_absent_from_method_frames"], "forbidden topics")
    require(not snapshot["representation_boundary"]["science_adjudicated"], "no science adjudication")
    prohibited = {".mp4", ".mov", ".mkv", ".webm", ".mp3", ".wav", ".m4a", ".aac"}
    require(not [path for path in ROOT.rglob("*pass22*") if path.suffix.lower() in prohibited], "no prohibited media")


def check_handoff() -> None:
    status = json.loads((ROOT / "STATUS.json").read_text())
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS22_COMPLETE", "status marker")
    require(status["pass22_review_snapshot_id"] == "spin-worker-yui-pass22-review-v1-20260808T130921K", "status snapshot")
    receipt = (ROOT / "LANE_RECEIPT.md").read_text()
    require("SPIN_WORKER_YUI_DEEPENING_PASS22_COMPLETE" in receipt, "lane receipt marker")
    require("## Exact Hwao action requested after pass 22" in receipt, "lane action")
    request = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
    require("Final pass-22 custody" in request, "integrator request")
    static = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
    require("Pass-22 minimum-scale dark-tone guard" in static, "static QA")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-only", action="store_true")
    args = parser.parse_args()
    check_pins()
    check_candidate()
    check_method()
    check_audit_and_boundary()
    if not args.evidence_only:
        check_handoff()
    suffix = "evidence-only/no-media" if args.evidence_only else "status-handoff/no-media"
    print(f"PASS pass22 snapshot/candidate/80-compound-frames/hierarchy/105-method-derivatives/minimum-scale-dark-tone-guard/source-blockers/{suffix}")


if __name__ == "__main__":
    main()
