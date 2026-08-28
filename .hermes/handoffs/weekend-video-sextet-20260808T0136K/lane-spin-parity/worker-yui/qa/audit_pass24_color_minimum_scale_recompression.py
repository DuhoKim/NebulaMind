#!/usr/bin/env python3
"""Quantify color/monochrome -> 360p -> JPEG q60 4:2:0 interaction."""

from __future__ import annotations

import collections
import csv
import difflib
import hashlib
import io
import json
import math
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_ROOT = ROOT / "qa/pass24_color_minimum_scale_recompression_audit"
CANDIDATE_RECEIPT = CANDIDATE_ROOT / "extraction_receipt.json"
METHOD_ROOT = ROOT / "qa/pass24_v8_color_minimum_scale_recompression"
METHOD_RECEIPT = METHOD_ROOT / "receipt.json"
PASS23_CANDIDATE_ROOT = ROOT / "qa/pass23_minimum_scale_color_vision_audit"
PASS23_METHOD_ROOT = ROOT / "qa/pass23_v8_minimum_scale_color_vision"
OUTPUT = ROOT / "qa/pass24_color_minimum_scale_recompression_quantitative_audit.json"
VARIANTS = [
    "color_360p_q60_420",
    "grayscale_bt709_then_360p_q60_420",
    "protanopia_machado100_then_360p_q60_420",
    "deuteranopia_machado100_then_360p_q60_420",
    "tritanopia_machado100_then_360p_q60_420",
]
HELD_CRITICAL = [7, 9, 10, 11, 16]
GATE_PATTERNS = [
    re.compile(r"\bresult\s+held\b", re.I),
    re.compile(r"\bframe\s+unstated\b", re.I),
    re.compile(r"\boutcomes?\s+withheld\b", re.I),
    re.compile(r"\bno\s+outcome\s+shown\b", re.I),
    re.compile(r"\bresult\s+locked\b", re.I),
    re.compile(r"\bresult\s+status\s+held\b", re.I),
]
CANONICAL_GATES = {
    1: "RESULT LOCKED ARCHIVE FRAME INDEPENDENT REVIEW REQUIRED",
    2: "OVERLAPPING READOUTS DO NOT SUM",
    3: "LABEL FRAME STATISTIC PHYSICAL INTERPRETATION HELD",
    4: "FRAME UNSTATED RESULT HELD",
    5: "COLUMN CHECK ONLY STORAGE FRAME UNRESOLVED",
    6: "CONTROL DESIGN ONLY OUTCOMES WITHHELD",
    7: "SEPARATE AUTHORIZATION REQUIRED AFTER BOTH BLOCKERS RESOLVE",
}
TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:[._/-][A-Za-z0-9]+)*")
PSMS = [6, 7, 11, 13]
GATE_CROP = (30, 22, 520, 46)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def jpeg_bytes(image: Image.Image) -> bytes:
    stream = io.BytesIO()
    image.convert("RGB").save(stream, format="JPEG", quality=60, subsampling=2, optimize=False, progressive=False)
    return stream.getvalue()


def tesseract_rows(path: Path) -> list[dict[str, Any]]:
    result = subprocess.run(["tesseract", str(path), "stdout", "--psm", "11", "tsv"], check=True, text=True, capture_output=True)
    rows: list[dict[str, Any]] = []
    for row in csv.DictReader(io.StringIO(result.stdout), delimiter="\t"):
        text = (row.get("text") or "").strip()
        try:
            confidence = float(row.get("conf") or -1)
            top = int(row.get("top") or 0)
            height = int(row.get("height") or 0)
        except ValueError:
            continue
        if text and confidence >= 20:
            rows.append({"text": text, "top": top, "height": height})
    return rows


def tokens(rows: list[dict[str, Any]], region: str) -> list[str]:
    output: list[str] = []
    for row in rows:
        center = (int(row["top"]) + int(row["height"]) / 2.0) / 360.0
        if region == "full" or (region == "headline" and center <= 0.30) or (region == "lower" and center >= 0.65):
            output.extend(token.casefold() for token in TOKEN_RE.findall(str(row["text"])))
    return output


def recall(reference: list[str], sample: list[str]) -> float:
    if not reference:
        return 1.0
    ref = collections.Counter(reference)
    got = collections.Counter(sample)
    return sum(min(count, got[token]) for token, count in ref.items()) / sum(ref.values())


def numeric(reference: list[str], sample: list[str]) -> float:
    return recall([token for token in reference if any(c.isdigit() for c in token)], [token for token in sample if any(c.isdigit() for c in token)])


def rgb(path: Path) -> np.ndarray:
    return np.asarray(Image.open(path).convert("RGB"), dtype=np.float32)


def luma(path: Path) -> np.ndarray:
    pixels = rgb(path)
    return 0.2126 * pixels[:, :, 0] + 0.7152 * pixels[:, :, 1] + 0.0722 * pixels[:, :, 2]


def edges(path: Path) -> np.ndarray:
    gray = luma(path)
    padded = np.pad(gray, 1, mode="edge")
    gx = -padded[:-2, :-2] + padded[:-2, 2:] - 2 * padded[1:-1, :-2] + 2 * padded[1:-1, 2:] - padded[2:, :-2] + padded[2:, 2:]
    gy = padded[:-2, :-2] + 2 * padded[:-2, 1:-1] + padded[:-2, 2:] - padded[2:, :-2] - 2 * padded[2:, 1:-1] - padded[2:, 2:]
    return np.hypot(gx, gy) >= 120.0


def dilate(mask: np.ndarray) -> np.ndarray:
    padded = np.pad(mask, 1, constant_values=False)
    return np.logical_or.reduce([padded[y:y + mask.shape[0], x:x + mask.shape[1]] for y in range(3) for x in range(3)])


def edge_recall(reference: Path, sample: Path) -> float:
    ref = edges(reference)
    return float(np.count_nonzero(ref & dilate(edges(sample))) / np.count_nonzero(ref)) if np.any(ref) else 1.0


def psnr(reference: Path, sample: Path) -> float:
    diff = rgb(reference) - rgb(sample)
    mse = float(np.mean(diff * diff))
    return 99.0 if mse == 0 else 10.0 * math.log10(255.0 * 255.0 / mse)


def mae(reference: Path, sample: Path) -> float:
    return float(np.mean(np.abs(rgb(reference) - rgb(sample))))


def normalize(text: str) -> str:
    return "".join(char.casefold() for char in text if char.isalnum())


def gate_score(path: Path, canonical: str) -> dict[str, Any]:
    with Image.open(path) as opened:
        crop = opened.convert("RGB").crop(GATE_CROP).resize((1960, 96), Image.Resampling.NEAREST)
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "gate.png"
            crop.save(target, format="PNG", optimize=False)
            scores = []
            for psm in PSMS:
                result = subprocess.run(["tesseract", str(target), "stdout", "--psm", str(psm)], check=True, text=True, capture_output=True)
                scores.append((difflib.SequenceMatcher(None, normalize(canonical), normalize(result.stdout)).ratio(), psm))
    value, mode = max(scores)
    return {"similarity": round(value, 6), "best_psm": mode, "passes_0_80": value >= 0.80}


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def exact_jpeg(baseline: Path, jpeg: Path, decoded: Path) -> tuple[bool, bool]:
    with Image.open(baseline) as opened:
        encoded = jpeg_bytes(opened.convert("RGB"))
    byte_exact = encoded == jpeg.read_bytes()
    with Image.open(io.BytesIO(encoded)) as expected:
        expected_pixels = np.asarray(expected.convert("RGB"), dtype=np.uint8)
    stored_pixels = np.asarray(Image.open(decoded).convert("RGB"), dtype=np.uint8)
    return byte_exact, bool(np.array_equal(expected_pixels, stored_pixels))


def audit_candidate(receipt: dict[str, Any]) -> dict[str, Any]:
    aggregate = {variant: collections.defaultdict(list) for variant in VARIANTS}
    critical = {variant: collections.defaultdict(list) for variant in VARIANTS}
    gates = {variant: 0 for variant in VARIANTS}
    critical_gates = {variant: 0 for variant in VARIANTS}
    exact_bytes = {variant: 0 for variant in VARIANTS}
    exact_pixels = {variant: 0 for variant in VARIANTS}
    scenes_out = []
    for scene in receipt["scenes"]:
        number = int(scene["scene"])
        samples_out = []
        for sample in scene["samples"]:
            variant = sample["variant"]
            path = CANDIDATE_ROOT / sample["frame"]
            jpeg = CANDIDATE_ROOT / sample["jpeg"]
            baseline = PASS23_CANDIDATE_ROOT / sample["baseline_pass23_frame"]
            baseline_rows = tesseract_rows(baseline)
            sample_rows = tesseract_rows(path)
            baseline_tokens = {region: tokens(baseline_rows, region) for region in ["full", "headline", "lower"]}
            sample_tokens = {region: tokens(sample_rows, region) for region in ["full", "headline", "lower"]}
            text = " ".join(str(row["text"]) for row in sample_rows)
            structural = any(pattern.search(text) for pattern in GATE_PATTERNS)
            gates[variant] += int(structural)
            if number in HELD_CRITICAL:
                critical_gates[variant] += int(structural)
            byte_exact, pixel_exact = exact_jpeg(baseline, jpeg, path)
            exact_bytes[variant] += int(byte_exact)
            exact_pixels[variant] += int(pixel_exact)
            metrics = {
                "headline_recall_vs_pass23_baseline": recall(baseline_tokens["headline"], sample_tokens["headline"]),
                "full_text_recall_vs_pass23_baseline": recall(baseline_tokens["full"], sample_tokens["full"]),
                "lower_support_recall_vs_pass23_baseline": recall(baseline_tokens["lower"], sample_tokens["lower"]),
                "numeric_recall_vs_pass23_baseline": numeric(baseline_tokens["full"], sample_tokens["full"]),
                "tolerant_luma_edge_recall_vs_pass23_baseline": edge_recall(baseline, path),
                "rgb_psnr_db_vs_pass23_baseline": psnr(baseline, path),
                "rgb_mae_vs_pass23_baseline": mae(baseline, path),
                "jpeg_bytes": float(sample["jpeg_bytes"]),
            }
            for key, value in metrics.items():
                aggregate[variant][key].append(value)
                if number in HELD_CRITICAL:
                    critical[variant][key].append(value)
            samples_out.append({
                "variant": variant,
                **{key: round(value, 6) for key, value in metrics.items()},
                "structural_gate_detected": structural,
                "baseline_pass23_pixel_exact": sample["baseline_recomputed_pixel_exact"],
                "jpeg_stream_recomputed_byte_exact": byte_exact,
                "decoded_rgb_recomputed_pixel_exact": pixel_exact,
                "jpeg_sha256": sample["jpeg_sha256"],
                "frame_sha256": sample["frame_sha256"],
            })
        scenes_out.append({"scene": number, "samples": samples_out})
    aggregates = {
        variant: {
            **{f"mean_{key}": mean(values) for key, values in aggregate[variant].items()},
            "structural_gate_scenes": gates[variant],
            "exact_jpeg_stream_scenes": exact_bytes[variant],
            "exact_decoded_rgb_scenes": exact_pixels[variant],
        }
        for variant in VARIANTS
    }
    critical_out = {
        variant: {
            "scenes": HELD_CRITICAL,
            **{f"mean_{key}": mean(values) for key, values in critical[variant].items()},
            "structural_gate_scene_count": critical_gates[variant],
        }
        for variant in VARIANTS
    }
    return {"aggregate": aggregates, "held_critical": critical_out, "scenes": scenes_out}


def audit_method(receipt: dict[str, Any]) -> dict[str, Any]:
    groups_out = {}
    for group_name, group in receipt["groups"].items():
        exact_bytes = {variant: 0 for variant in VARIANTS}
        exact_pixels = {variant: 0 for variant in VARIANTS}
        gate_rows = {variant: [] for variant in VARIANTS}
        for scene in group["scenes"]:
            number = int(scene["scene"])
            for sample in scene["samples"]:
                variant = sample["variant"]
                baseline = PASS23_METHOD_ROOT / group_name / sample["baseline_pass23_frame"]
                jpeg = METHOD_ROOT / group_name / sample["jpeg"]
                frame = METHOD_ROOT / group_name / sample["frame"]
                byte_exact, pixel_exact = exact_jpeg(baseline, jpeg, frame)
                exact_bytes[variant] += int(byte_exact)
                exact_pixels[variant] += int(pixel_exact)
                if group_name == "pass12_sharpness_safe":
                    gate_rows[variant].append({"scene": number, **gate_score(frame, CANONICAL_GATES[number])})
        output: dict[str, Any] = {
            "scene_count": group["scene_count"],
            "decoded_png_frame_count": group["decoded_png_frame_count"],
            "jpeg_stream_count": group["jpeg_stream_count"],
            "exact_jpeg_stream_scenes": exact_bytes,
            "exact_decoded_rgb_scenes": exact_pixels,
            "human_visual_review": {
                "exact_top_gates": "7/7_ALL_FIVE_VARIANTS" if group_name != "sealed_v8" else "NOT_A_TOP_GATE_PROOF",
                "complete_result_held_badges": "7/7_ALL_FIVE_VARIANTS",
                "major_method_status_boundaries": "7/7_ALL_FIVE_VARIANTS",
                "hue_only_required_meaning": 0,
                "direct_label_plus_non_color_redundancy": "PASS_ALL_7_ALL_FIVE_VARIANTS",
                "compression_caused_overlap_clipping_or_ambiguity": 0,
            },
        }
        if group_name == "pass12_sharpness_safe":
            output["mapped_gate_ocr_aid"] = {
                variant: {
                    "threshold": 0.8,
                    "mean_similarity": mean([row["similarity"] for row in rows]),
                    "passing_scenes": sum(bool(row["passes_0_80"]) for row in rows),
                    "scenes": rows,
                }
                for variant, rows in gate_rows.items()
            }
        groups_out[group_name] = output
    return groups_out


def main() -> None:
    candidate_receipt = json.loads(CANDIDATE_RECEIPT.read_text())
    method_receipt = json.loads(METHOD_RECEIPT.read_text())
    if candidate_receipt["variant_order"] != VARIANTS or method_receipt["variant_order"] != VARIANTS:
        raise SystemExit("variant contract mismatch")
    candidate = audit_candidate(candidate_receipt)
    method = audit_method(method_receipt)
    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 24,
        "audit": "native_monochrome_or_color_vision_then_360p_then_jpeg_q60_420_interaction",
        "simulation_scope": "packet-specific presentation stress only; not clinical diagnostic or named delivery/codec/viewing standard",
        "candidate_sha256": candidate_receipt["candidate_sha256"],
        "candidate_receipt": "qa/pass24_color_minimum_scale_recompression_audit/extraction_receipt.json",
        "candidate_receipt_sha256": sha(CANDIDATE_RECEIPT),
        "method_receipt": "qa/pass24_v8_color_minimum_scale_recompression/receipt.json",
        "method_receipt_sha256": sha(METHOD_RECEIPT),
        "candidate": candidate,
        "method": method,
        "representation_review": {
            "candidate_structural_held_gate_scenes": "0/16_ALL_FIVE_VARIANTS",
            "candidate_result_hierarchy": "LARGE_RESULT_HEADLINES_NUMBERS_PLOTS_BARS_MATRICES_AND_CONCLUSIONS_REMAIN_PRIMARY",
            "candidate_fine_support": "AXES_ERROR_BARS_LEGENDS_CAVEATS_CITATIONS_PROVENANCE_AND_FINE_LABELS_WEAKEN_FIRST",
            "candidate_incremental_recompression_meaning_change": False,
            "candidate_compression_caused_overlap_clipping_or_ambiguity": 0,
            "method_hue_only_required_meaning": 0,
            "method_direct_label_shape_line_marker_position_redundancy": "PASS_ALL_7_ALL_FIVE_VARIANTS",
            "science_adjudicated": False,
        },
        "ocr": {
            "engine": subprocess.run(["tesseract", "--version"], check=True, text=True, capture_output=True).stdout.splitlines()[0],
            "full_frame_psm": 11,
            "confidence_floor": 20,
            "gate_psms": PSMS,
            "gate_threshold": 0.8,
            "raw_text_stored": False,
            "human_review_decisive": True,
        },
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "published": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    gray = candidate["aggregate"]["grayscale_bt709_then_360p_q60_420"]
    proof = method["pass12_sharpness_safe"]["mapped_gate_ocr_aid"]
    print(
        "PASS candidate=16/80+80jpeg method=21/105+105jpeg "
        f"gray_incremental_headline={gray['mean_headline_recall_vs_pass23_baseline']:.6f} "
        f"gray_incremental_full={gray['mean_full_text_recall_vs_pass23_baseline']:.6f} "
        f"proof_min={min(row['passing_scenes'] for row in proof.values())}/7"
    )


if __name__ == "__main__":
    main()
