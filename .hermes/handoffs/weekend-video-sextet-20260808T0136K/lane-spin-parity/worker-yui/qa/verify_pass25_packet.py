#!/usr/bin/env python3
"""Verify pass-25 color/minimum-scale/represented-black-lift packet."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT.parents[1]
REPO = HANDOFF.parents[2]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
CAND_ROOT = ROOT / "qa/pass25_color_minimum_scale_black_lift_audit"
CAND_RECEIPT = CAND_ROOT / "extraction_receipt.json"
METHOD_ROOT = ROOT / "qa/pass25_v8_color_minimum_scale_black_lift"
METHOD_RECEIPT = METHOD_ROOT / "receipt.json"
QUANT = ROOT / "qa/pass25_color_minimum_scale_black_lift_quantitative_audit.json"
SNAPSHOT = ROOT / "qa/pass25_review_snapshot_v1.json"
GUARD = ROOT / "COLOR_MINIMUM_SCALE_BLACK_LIFT_GUARD_PASS25.json"
BLOCKER = ROOT / "BLOCKER_PACKET_PASS25.json"
AUDIT = ROOT / "PASS25_ENCODED_FRAME_AUDIT.md"
BLACK_LIFT = 0.20
EXPECTED_VARIANTS = [
    "color_then_360p_then_black_lift20",
    "grayscale_bt709_then_360p_then_black_lift20",
    "protanopia_machado100_then_360p_then_black_lift20",
    "deuteranopia_machado100_then_360p_then_black_lift20",
    "tritanopia_machado100_then_360p_then_black_lift20",
]
MATRICES = {
    "protanopia_machado100": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]], dtype=np.float64),
    "deuteranopia_machado100": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]], dtype=np.float64),
    "tritanopia_machado100": np.array([[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]], dtype=np.float64),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL {message}")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, 1.0)
    return np.where(clipped <= 0.0031308, 12.92 * clipped, 1.055 * clipped ** (1.0 / 2.4) - 0.055)


def represented(native: Image.Image, baseline_variant: str) -> np.ndarray:
    if baseline_variant == "color_360p":
        transformed = native.convert("RGB")
    else:
        label = baseline_variant.removesuffix("_then_360p")
        linear = srgb_to_linear(np.asarray(native.convert("RGB"), dtype=np.float64) / 255.0)
        if label == "grayscale_bt709":
            luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
            transformed_linear = np.repeat(luminance[:, :, None], 3, axis=2)
        else:
            transformed_linear = np.einsum("...c,rc->...r", linear, MATRICES[label])
        transformed = Image.fromarray(np.rint(linear_to_srgb(transformed_linear) * 255.0).astype(np.uint8))
    return np.asarray(transformed.resize((640, 360), Image.Resampling.LANCZOS), dtype=np.uint8)


def lift(pixels: np.ndarray) -> np.ndarray:
    linear = srgb_to_linear(pixels.astype(np.float64) / 255.0)
    return np.rint(linear_to_srgb(BLACK_LIFT + (1.0 - BLACK_LIFT) * linear) * 255.0).astype(np.uint8)


def verify_candidate(receipt: dict) -> None:
    require(sha(CANDIDATE) == EXPECTED_CANDIDATE == receipt["candidate_sha256"], "candidate custody")
    require(receipt["deepening_pass"] == 25 and receipt["scene_count"] == 16, "candidate census")
    require(receipt["variant_order"] == EXPECTED_VARIANTS and receipt["frame_count"] == 80, "candidate variant/frame census")
    require(receipt["detected_cut_count"] == 15 and receipt["fresh_clean_match_count"] == 16, "cuts/native custody")
    require(receipt["baseline_pass23_pixel_match_count"] == 80, "candidate pass23 baseline custody")
    pass24 = load(ROOT / "qa/pass24_color_minimum_scale_recompression_audit/extraction_receipt.json")
    require(receipt["detected_cut_times_seconds"] == pass24["detected_cut_times_seconds"], "cut timestamps")
    pass24_scenes = {int(row["scene"]): row for row in pass24["scenes"]}
    exact_derivatives = 0
    for scene in receipt["scenes"]:
        number = int(scene["scene"])
        clean = CAND_ROOT / scene["native_clean"]
        previous_clean = ROOT / "qa/pass24_color_minimum_scale_recompression_audit" / pass24_scenes[number]["native_clean"]
        require(sha(clean) == sha(previous_clean) == scene["native_clean_sha256"], f"candidate clean S{number}")
        with Image.open(clean) as opened:
            native = opened.convert("RGB")
            for sample in scene["samples"]:
                baseline = represented(native, sample["baseline_variant"])
                pass23 = ROOT / "qa/pass23_minimum_scale_color_vision_audit" / sample["baseline_pass23_frame"]
                with Image.open(pass23) as opened23:
                    require(np.array_equal(baseline, np.asarray(opened23.convert("RGB"), dtype=np.uint8)), f"candidate baseline S{number} {sample['variant']}")
                frame = CAND_ROOT / sample["frame"]
                with Image.open(frame) as output:
                    stored = np.asarray(output.convert("RGB"), dtype=np.uint8)
                require(np.array_equal(lift(baseline), stored), f"candidate lift S{number} {sample['variant']}")
                require(sha(frame) == sample["frame_sha256"] and output.size == (640, 360), f"candidate frame receipt S{number}")
                exact_derivatives += 1
    require(exact_derivatives == 80, "candidate exact derivative total")
    require(len(receipt["contact_sheets"]) == 5, "candidate contact sheets")
    for sheet in receipt["contact_sheets"].values():
        path = CAND_ROOT / sheet["path"]
        require(sha(path) == sheet["sha256"], "candidate contact-sheet hash")


def verify_method(receipt: dict) -> None:
    require(receipt["deepening_pass"] == 25 and receipt["variant_order"] == EXPECTED_VARIANTS, "method contract")
    require(receipt["scene_count"] == 21 and receipt["frame_count"] == 105, "method census")
    require(receipt["baseline_pass23_pixel_match_count"] == 105, "method baseline custody")
    require(not receipt["sealed_v8_modified"] and not receipt["pass7_proof_modified"] and not receipt["pass12_proof_modified"] and not receipt["v9_created"], "method source immutability")
    exact = 0
    for name, group in receipt["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35, f"method group census {name}")
        for scene in group["scenes"]:
            source = ROOT / scene["source"]
            require(sha(source) == scene["source_sha256"], f"method source {name} S{scene['scene']}")
            with Image.open(source) as opened:
                native = opened.convert("RGB")
                for sample in scene["samples"]:
                    baseline = represented(native, sample["baseline_variant"])
                    prior = ROOT / "qa/pass23_v8_minimum_scale_color_vision" / name / sample["baseline_pass23_frame"]
                    with Image.open(prior) as prior_opened:
                        require(np.array_equal(baseline, np.asarray(prior_opened.convert("RGB"), dtype=np.uint8)), f"method baseline {name} S{scene['scene']}")
                    frame = METHOD_ROOT / name / sample["frame"]
                    with Image.open(frame) as output:
                        stored = np.asarray(output.convert("RGB"), dtype=np.uint8)
                    require(np.array_equal(lift(baseline), stored), f"method lift {name} S{scene['scene']} {sample['variant']}")
                    require(sha(frame) == sample["frame_sha256"] and output.size == (640, 360), f"method receipt {name}")
                    exact += 1
        require(len(group["contact_sheets"]) == 5, f"method sheets {name}")
        for sheet in group["contact_sheets"].values():
            require(sha(METHOD_ROOT / name / sheet["path"]) == sheet["sha256"], f"method sheet hash {name}")
    require(exact == 105, "method exact derivative total")


def verify_evidence() -> None:
    candidate, method, quant, snapshot, guard, blocker = load(CAND_RECEIPT), load(METHOD_RECEIPT), load(QUANT), load(SNAPSHOT), load(GUARD), load(BLOCKER)
    verify_candidate(candidate)
    verify_method(method)
    require(quant["deepening_pass"] == 25 and quant["candidate_sha256"] == EXPECTED_CANDIDATE, "quant identity")
    require(quant["representation_review"]["candidate_structural_held_gate_scenes"] == "0/16_ALL_FIVE_VARIANTS", "candidate held-gate verdict")
    require(not quant["representation_review"]["candidate_black_lift_repairs_or_authorizes"], "no candidate repair")
    for variant, data in quant["candidate"]["aggregate"].items():
        require(data["structural_gate_scenes"] == 0 and data["exact_black_lift_scenes"] == 16, f"candidate aggregate {variant}")
        require(quant["candidate"]["held_critical"][variant]["structural_gate_scene_count"] == 0, f"critical gate {variant}")
    proof = quant["method"]["pass12_sharpness_safe"]["mapped_gate_ocr_aid"]
    require(all(row["passing_scenes"] == 7 and row["mean_similarity"] == 1.0 for row in proof.values()), "pass12 mapped gates")
    require(snapshot["status"] == "IMMUTABLE_REVIEW_SNAPSHOT" and snapshot["deepening_pass"] == 25, "snapshot identity")
    for item in snapshot["evidence"].values():
        require(sha(ROOT / item["path"]) == item["sha256"], f"snapshot pin {item['path']}")
    require(guard["status"] == "PROPOSAL_ONLY_INTEGRATION_GUARD_NOT_V9_NOT_A_CANDIDATE", "guard status")
    require(not guard["disposition"]["pixel_or_copy_correction_requested"], "guard disposition")
    require(blocker["candidate"]["sha256"] == EXPECTED_CANDIDATE and not blocker["pass25_representation_finding"]["candidate_repaired_or_authorized"], "blocker candidate")
    external = {
        "T4_PAIRED_FLIP.json": "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873",
        "AMENDMENT_A4_DRAFT.md": "8343c1947384cdb36355a0fe2f6965d4445ab013fda25e3f33b4d8300ce58974",
        "KUN_FRAME_REVIEW.md": "ccedf6846391a8f0661a88b2eec0ce21fbfd7c44ad16201080bb196f56d258e5",
    }
    source = REPO / ".hermes/handoffs/spin-parity-census-20260805T1922K"
    for name, expected in external.items():
        require(sha(source / name) == expected, f"external blocker custody {name}")
    require("FRAME REVIEW: AGREES FRAME_UNSTATED" in (source / "KUN_FRAME_REVIEW.md").read_text(), "frame terminal status")
    require(sha(AUDIT) == snapshot["evidence"]["encoded_frame_audit"]["sha256"], "audit pin")
    prohibited = [path for path in ROOT.rglob("pass25*") if path.suffix.lower() in {".mp4", ".mov", ".mkv", ".mp3", ".wav", ".m4a", ".aac"}]
    require(not prohibited, "pass25 prohibited audio/video output")


def verify_handoff() -> None:
    status = load(ROOT / "STATUS.json")
    require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS25_COMPLETE", "status marker")
    require(status["pass25_color_minimum_scale_black_lift_audit_completed"], "status audit flag")
    require(status["pass25_review_snapshot_id"] == "spin-worker-yui-pass25-review-v1-20260808T142621K", "status snapshot")
    lane = (ROOT / "LANE_RECEIPT.md").read_text()
    integrator = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
    static = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
    for text, marker in [(lane, "SPIN_WORKER_YUI_DEEPENING_PASS25_COMPLETE"), (integrator, "## Pass-25 latest request"), (static, "## Pass-25 cumulative QA")]:
        require(marker in text, f"handoff marker {marker}")
    require("PASS25_ENCODED_FRAME_AUDIT.md" in status["allowed_next_action"], "status next-action pointer")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-only", action="store_true")
    args = parser.parse_args()
    verify_evidence()
    if not args.evidence_only:
        verify_handoff()
    print("PASS pass25_packet evidence=exact transforms=185/185 gates=7/7x5 blockers=unchanged handoff=" + ("skipped" if args.evidence_only else "verified"))


if __name__ == "__main__":
    main()
