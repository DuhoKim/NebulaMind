#!/usr/bin/env python3
"""Verify pass-29 color/minimum-scale/represented-vertical-smear packet."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[4]
PACKET_ROOT = REPO / ".hermes/handoffs/weekend-video-sextet-20260808T0136K"
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
CAND_ROOT = ROOT / "qa/pass29_color_minimum_scale_represented_vertical_smear_audit"
CAND_RECEIPT = CAND_ROOT / "extraction_receipt.json"
METHOD_ROOT = ROOT / "qa/pass29_v8_color_minimum_scale_represented_vertical_smear"
METHOD_RECEIPT = METHOD_ROOT / "receipt.json"
QUANT = ROOT / "qa/pass29_color_minimum_scale_represented_vertical_smear_quantitative_audit.json"
SNAPSHOT = ROOT / "qa/pass29_review_snapshot_v1.json"
EXPECTED_CANDIDATE = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
WIDTH = 3
VARIANTS = {
    "color_then_360p_then_represented_vertical_smear_w03": "color_360p",
    "grayscale_bt709_then_360p_then_represented_vertical_smear_w03": "grayscale_bt709_then_360p",
    "protanopia_machado100_then_360p_then_represented_vertical_smear_w03": "protanopia_machado100_then_360p",
    "deuteranopia_machado100_then_360p_then_represented_vertical_smear_w03": "deuteranopia_machado100_then_360p",
    "tritanopia_machado100_then_360p_then_represented_vertical_smear_w03": "tritanopia_machado100_then_360p",
}
MATRICES = {
    "protanopia_machado100_then_360p": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]], dtype=np.float64),
    "deuteranopia_machado100_then_360p": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]], dtype=np.float64),
    "tritanopia_machado100_then_360p": np.array([[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]], dtype=np.float64),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def srgb_to_linear(a: np.ndarray) -> np.ndarray:
    x = a.astype(np.float64) / 255.0
    return np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(x: np.ndarray) -> np.ndarray:
    y = np.where(x <= 0.0031308, 12.92 * x, 1.055 * np.power(x, 1 / 2.4) - 0.055)
    return np.rint(np.clip(y, 0, 1) * 255.0).astype(np.uint8)


def represented(native: np.ndarray, baseline_name: str) -> np.ndarray:
    if baseline_name == "color_360p":
        prepared = native
    else:
        linear = srgb_to_linear(native)
        if baseline_name == "grayscale_bt709_then_360p":
            y = 0.2126 * linear[..., 0] + 0.7152 * linear[..., 1] + 0.0722 * linear[..., 2]
            prepared = linear_to_srgb(np.repeat(y[..., None], 3, axis=2))
        else:
            prepared = linear_to_srgb(np.clip(linear @ MATRICES[baseline_name].T, 0, 1))
    return np.asarray(Image.fromarray(prepared).resize((640, 360), Image.Resampling.LANCZOS), dtype=np.uint8)


def smear(a: np.ndarray) -> np.ndarray:
    pad = WIDTH // 2
    padded = np.pad(a.astype(np.uint64), ((pad, pad), (0, 0), (0, 0)), mode="edge")
    cumulative = np.concatenate([np.zeros((1, a.shape[1], a.shape[2]), dtype=np.uint64), np.cumsum(padded, axis=0, dtype=np.uint64)], axis=0)
    totals = cumulative[WIDTH:] - cumulative[:-WIDTH]
    return ((totals + WIDTH // 2) // WIDTH).astype(np.uint8)


def detect_cuts() -> list[float]:
    result = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "info", "-i", str(CANDIDATE), "-vf", "scale=160:90,format=gray,select='gt(scene,0.03)',showinfo", "-an", "-f", "null", "-"], check=True, capture_output=True, text=True)
    cuts = []
    for value in re.findall(r"pts_time:([0-9.]+)", result.stderr):
        stamp = round(float(value), 6)
        if stamp > 0 and (not cuts or cuts[-1] != stamp):
            cuts.append(stamp)
    return cuts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-only", action="store_true")
    args = parser.parse_args()
    candidate = json.loads(CAND_RECEIPT.read_text())
    method = json.loads(METHOD_RECEIPT.read_text())
    quant = json.loads(QUANT.read_text())
    snapshot = json.loads(SNAPSHOT.read_text())

    require(sha(CANDIDATE) == EXPECTED_CANDIDATE, "candidate closing hash")
    require(sha(ROOT / "SOURCE_STATUS_FREEZE.json") == "ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1", "source freeze")
    require(sha(ROOT / "STORYBOARD_PROPOSAL.json") == "80c91bc5513ac6268501c02cac2e8354388e43bf0094569804e4bbf54f293bce", "storyboard")
    require(sha(ROOT / "proposal_frames/v8/render_receipt.json") == "fe5a8d379e6e7e84f480263befd7a3964886f55e7795e1a7dd0c61760d3297f3", "sealed receipt")
    require(sha(PACKET_ROOT / "HWAO_WEEKEND_ORDER.md") == "ac5d35314a3af78ab2214b62105fa74afb616862aeeb2d09faa1dd6eb1c84710", "authority order")
    require(sha(PACKET_ROOT / "COORDINATION_UPDATE.md") == "2d64667f8ab95349b344c9098a4f2b8f675c71d53d1cc132a780e0ac699fde1f", "coordination")
    require(detect_cuts() == candidate["detected_cut_times_seconds"] and len(candidate["detected_cut_times_seconds"]) == 15, "fresh cuts")
    require(candidate["candidate_sha256"] == EXPECTED_CANDIDATE and candidate["scene_count"] == 16 and candidate["frame_count"] == 80, "candidate census")
    require(candidate["fresh_clean_match_count"] == 16 and candidate["pass23_baseline_match_count"] == 80 and candidate["exact_smear_recomputation_count"] == 80, "candidate custody census")

    exact_candidate = 0
    for scene in candidate["scenes"]:
        clean = ROOT / scene["native_clean"]
        require(sha(clean) == scene["native_clean_sha256"] and scene["native_clean_byte_identical_to_pass28"], f"clean S{scene['scene']}")
        with Image.open(clean) as image:
            native = np.asarray(image.convert("RGB"), dtype=np.uint8)
        require(len(scene["samples"]) == 5, f"candidate variants S{scene['scene']}")
        for sample in scene["samples"]:
            baseline = ROOT / sample["baseline_path"]
            output = CAND_ROOT / sample["frame"]
            recomputed = represented(native, sample["baseline_variant"])
            with Image.open(baseline) as image:
                baseline_pixels = np.asarray(image.convert("RGB"), dtype=np.uint8)
            with Image.open(output) as image:
                stored = np.asarray(image.convert("RGB"), dtype=np.uint8)
                size = image.size
            require(np.array_equal(recomputed, baseline_pixels), f"candidate baseline S{scene['scene']} {sample['variant']}")
            require(np.array_equal(smear(recomputed), stored), f"candidate smear S{scene['scene']} {sample['variant']}")
            require(sha(output) == sample["frame_sha256"] and sha(baseline) == sample["baseline_sha256"] and size == (640, 360), "candidate frame receipt")
            exact_candidate += 1
    require(exact_candidate == 80, "candidate exact total")

    require(method["frame_count"] == 105 and method["pass23_baseline_match_count"] == 105 and method["exact_smear_recomputation_count"] == 105, "method census")
    exact_method = 0
    for name, group in method["groups"].items():
        require(group["scene_count"] == 7 and group["frame_count"] == 35 and len(group["contact_sheets"]) == 5, f"group census {name}")
        for scene in group["scenes"]:
            source = ROOT / scene["source"]
            require(sha(source) == scene["source_sha256"], f"method source {name} S{scene['scene']}")
            with Image.open(source) as image:
                native = np.asarray(image.convert("RGB"), dtype=np.uint8)
            require(len(scene["samples"]) == 5, f"method variants {name}")
            for sample in scene["samples"]:
                baseline = ROOT / sample["baseline_path"]
                output = METHOD_ROOT / name / sample["frame"]
                recomputed = represented(native, sample["baseline_variant"])
                with Image.open(baseline) as image:
                    baseline_pixels = np.asarray(image.convert("RGB"), dtype=np.uint8)
                with Image.open(output) as image:
                    stored = np.asarray(image.convert("RGB"), dtype=np.uint8)
                    size = image.size
                require(np.array_equal(recomputed, baseline_pixels), f"method baseline {name}")
                require(np.array_equal(smear(recomputed), stored), f"method smear {name}")
                require(sha(output) == sample["frame_sha256"] and sha(baseline) == sample["baseline_sha256"] and size == (640, 360), "method frame receipt")
                exact_method += 1
    require(exact_method == 105, "method exact total")

    require(quant["deepening_pass"] == 29 and quant["human_review"]["candidate"]["structural_held_gate_scenes"] == "0/16_ALL_FIVE_VARIANTS", "quant identity")
    expected = {
        "color_then_360p_then_represented_vertical_smear_w03": (0.986207, 0.876304, 0.647887, 0.883723, 0.577560),
        "grayscale_bt709_then_360p_then_represented_vertical_smear_w03": (0.965753, 0.660911, 0.118812, 0.883852, 0.577354),
        "tritanopia_machado100_then_360p_then_represented_vertical_smear_w03": (0.954545, 0.786136, 0.391608, 0.883976, 0.577853),
    }
    for variant, values in expected.items():
        row = quant["candidate"][variant]
        require((row["headline_recall"], row["full_recall"], row["lower_recall"], row["horizontal_luma_gradient_energy_ratio"], row["vertical_luma_gradient_energy_ratio"]) == values and row["structural_gate_scenes"] == 0 and row["exact_smear_frames"] == 16, f"metrics {variant}")
    proof_expected = {
        "color_then_360p_then_represented_vertical_smear_w03": (4, 0.797493),
        "grayscale_bt709_then_360p_then_represented_vertical_smear_w03": (4, 0.765234),
        "protanopia_machado100_then_360p_then_represented_vertical_smear_w03": (4, 0.806685),
        "deuteranopia_machado100_then_360p_then_represented_vertical_smear_w03": (3, 0.779427),
        "tritanopia_machado100_then_360p_then_represented_vertical_smear_w03": (4, 0.772629),
    }
    for variant, values in proof_expected.items():
        proof = quant["method_groups"]["pass12_sharpness_safe"][variant]
        require((proof["mapped_gate_threshold_passes"], proof["mean_mapped_gate_similarity"]) == values and proof["exact_smear_frames"] == 7, f"proof {variant}")
    require(quant["human_review"]["sealed_v8"]["result_held_badges"] == "7/7_ALL_FIVE_VARIANTS", "badges")
    require(quant["human_review"]["pass12_sharpness_safe"]["exact_top_gates"] == "7/7_ALL_FIVE_VARIANTS" and quant["human_review"]["hue_only_required_meaning"] == 0, "method human")

    guard = json.loads((ROOT / "COLOR_MINIMUM_SCALE_REPRESENTED_VERTICAL_SMEAR_GUARD_PASS29.json").read_text())
    blocker = json.loads((ROOT / "BLOCKER_PACKET_PASS29.json").read_text())
    require(guard["guard_id"] == "spin-worker-yui-pass29-color-minimum-scale-represented-vertical-smear-20260808T155234K" and guard["evidence_backed_action"] == "ADOPT_GUARD_ONLY_NO_NEW_PIXEL_OR_COPY_CORRECTION", "guard")
    require(blocker["packet_id"] == "spin-worker-yui-pass29-blockers-20260808T155234K" and all(item["status"] == "OPEN_UNCHANGED" for item in blocker["blocking_facts"]), "blockers")
    require(snapshot["snapshot_id"] == "spin-worker-yui-pass29-review-v1-20260808T155234K" and snapshot["baseline_receipts"]["qa/pass28_review_snapshot_v1.json"] == "131835548fdc6062d4bcf66af45db7ca47163b7fa76b8278742839816fb75d58", "snapshot")
    for path, digest in snapshot["pass29_artifacts"].items():
        require(sha(ROOT / path) == digest, f"snapshot artifact {path}")
    prohibited = {".mp4", ".mov", ".m4a", ".mp3", ".wav", ".aac", ".webm"}
    pass29_files = [p for p in ROOT.rglob("*pass29*") if p.is_file()]
    require(not any(path.suffix.lower() in prohibited for path in pass29_files), "prohibited media")

    handoff = "skipped"
    if not args.evidence_only:
        status = json.loads((ROOT / "STATUS.json").read_text())
        receipt = (ROOT / "LANE_RECEIPT.md").read_text()
        integrator = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text()
        static = (ROOT / "STATIC_PROPOSAL_QA.md").read_text()
        require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS29_COLOR_MINIMUM_SCALE_REPRESENTED_VERTICAL_SMEAR_GUARD_V1", "status phase")
        require(status["receipt_marker"] == "SPIN_WORKER_YUI_DEEPENING_PASS29_COMPLETE" and not status["video_reportable_now"], "status marker")
        require("SPIN_WORKER_YUI_DEEPENING_PASS29_COMPLETE" in receipt and "PASS29_ENCODED_FRAME_AUDIT.md" in receipt, "lane receipt")
        require("Pass-29 latest request" in integrator and "COLOR_MINIMUM_SCALE_REPRESENTED_VERTICAL_SMEAR_GUARD_PASS29.json" in integrator, "integrator handoff")
        require("Pass-29 cumulative QA" in static and "COLOR_MINIMUM_SCALE_REPRESENTED_VERTICAL_SMEAR_GUARD_PASS29.json" in static, "static handoff")
        handoff = "verified"
    print(f"PASS pass29_packet evidence=exact transforms={exact_candidate + exact_method}/185 gates=human7/7x5 ocr_min=3/7 blockers=unchanged handoff={handoff}")


if __name__ == "__main__":
    main()

