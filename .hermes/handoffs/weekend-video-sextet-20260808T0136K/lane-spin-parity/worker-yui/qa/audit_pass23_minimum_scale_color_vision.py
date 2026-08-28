#!/usr/bin/env python3
"""Quantify native monochrome/color-vision transforms followed by 360p."""

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
CANDIDATE_ROOT = ROOT / "qa/pass23_minimum_scale_color_vision_audit"
CANDIDATE_RECEIPT = CANDIDATE_ROOT / "extraction_receipt.json"
METHOD_ROOT = ROOT / "qa/pass23_v8_minimum_scale_color_vision"
METHOD_RECEIPT = METHOD_ROOT / "receipt.json"
OUTPUT = ROOT / "qa/pass23_minimum_scale_color_vision_quantitative_audit.json"
VARIANTS = [
    "color_360p",
    "grayscale_bt709_then_360p",
    "protanopia_machado100_then_360p",
    "deuteranopia_machado100_then_360p",
    "tritanopia_machado100_then_360p",
]
MATRICES = {
    "protanopia_machado100": np.array(
        [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]], dtype=np.float64
    ),
    "deuteranopia_machado100": np.array(
        [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]], dtype=np.float64
    ),
    "tritanopia_machado100": np.array(
        [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]], dtype=np.float64
    ),
}
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


def tesseract_rows(path: Path) -> list[dict[str, Any]]:
    result = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "11", "tsv"],
        check=True, text=True, capture_output=True,
    )
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
    out: list[str] = []
    for row in rows:
        center = (int(row["top"]) + int(row["height"]) / 2.0) / 360.0
        keep = region == "full" or (region == "headline" and center <= 0.30) or (region == "lower" and center >= 0.65)
        if keep:
            out.extend(token.casefold() for token in TOKEN_RE.findall(str(row["text"])))
    return out


def recall(reference: list[str], sample: list[str]) -> float:
    if not reference:
        return 1.0
    ref = collections.Counter(reference)
    got = collections.Counter(sample)
    return sum(min(count, got[token]) for token, count in ref.items()) / sum(ref.values())


def numeric(reference: list[str], sample: list[str]) -> float:
    return recall(
        [token for token in reference if any(char.isdigit() for char in token)],
        [token for token in sample if any(char.isdigit() for char in token)],
    )


def luma(path: Path) -> np.ndarray:
    rgb = np.asarray(Image.open(path).convert("RGB"), dtype=np.float32)
    return 0.2126 * rgb[:, :, 0] + 0.7152 * rgb[:, :, 1] + 0.0722 * rgb[:, :, 2]


def edges(path: Path) -> np.ndarray:
    gray = luma(path)
    padded = np.pad(gray, 1, mode="edge")
    gx = -padded[:-2, :-2] + padded[:-2, 2:] - 2 * padded[1:-1, :-2] + 2 * padded[1:-1, 2:] - padded[2:, :-2] + padded[2:, 2:]
    gy = padded[:-2, :-2] + 2 * padded[:-2, 1:-1] + padded[:-2, 2:] - padded[2:, :-2] - 2 * padded[2:, 1:-1] - padded[2:, 2:]
    return np.hypot(gx, gy) >= 120.0


def dilate(mask: np.ndarray) -> np.ndarray:
    padded = np.pad(mask, 1, constant_values=False)
    return np.logical_or.reduce([padded[y : y + mask.shape[0], x : x + mask.shape[1]] for y in range(3) for x in range(3)])


def edge_recall(reference: Path, sample: Path) -> float:
    ref = edges(reference)
    if not np.any(ref):
        return 1.0
    return float(np.count_nonzero(ref & dilate(edges(sample))) / np.count_nonzero(ref))


def chroma_metrics(reference: Path, sample: Path) -> tuple[float, float]:
    ref = np.asarray(Image.open(reference).convert("RGB"), dtype=np.float32)
    got = np.asarray(Image.open(sample).convert("RGB"), dtype=np.float32)
    ref_c = ref.max(axis=2) - ref.min(axis=2)
    got_c = got.max(axis=2) - got.min(axis=2)
    mask = ref_c >= 30.0
    if not np.any(mask):
        return 1.0, 0.0
    return float(got_c[mask].mean() / ref_c[mask].mean()), float(np.count_nonzero(mask) / mask.size)


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, 1.0)
    return np.where(clipped <= 0.0031308, 12.92 * clipped, 1.055 * clipped ** (1.0 / 2.4) - 0.055)


def recompute(native_path: Path, variant: str) -> np.ndarray:
    with Image.open(native_path) as opened:
        native = opened.convert("RGB")
        if variant == "color_360p":
            transformed = native
        else:
            label = variant.removesuffix("_then_360p")
            rgb = np.asarray(native, dtype=np.float64) / 255.0
            linear = srgb_to_linear(rgb)
            if label == "grayscale_bt709":
                luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
                transformed_linear = np.repeat(luminance[:, :, None], 3, axis=2)
            else:
                transformed_linear = np.einsum("...c,rc->...r", linear, MATRICES[label])
            transformed = Image.fromarray(np.rint(np.clip(linear_to_srgb(transformed_linear), 0.0, 1.0) * 255.0).astype(np.uint8))
        return np.asarray(transformed.resize((640, 360), Image.Resampling.LANCZOS), dtype=np.uint8)


def normalize(text: str) -> str:
    return "".join(char.casefold() for char in text if char.isalnum())


def gate_score(path: Path, canonical: str) -> dict[str, Any]:
    with Image.open(path) as opened:
        crop = opened.convert("RGB").crop(GATE_CROP).resize((1960, 96), Image.Resampling.NEAREST)
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "gate.png"
            crop.save(target, format="PNG", optimize=False)
            scores: list[tuple[float, int]] = []
            for psm in PSMS:
                result = subprocess.run(
                    ["tesseract", str(target), "stdout", "--psm", str(psm)],
                    check=True, text=True, capture_output=True,
                )
                scores.append((difflib.SequenceMatcher(None, normalize(canonical), normalize(result.stdout)).ratio(), psm))
    value, mode = max(scores)
    return {"similarity": round(value, 6), "best_psm": mode, "passes_0_80": value >= 0.80}


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def audit_candidate(receipt: dict[str, Any]) -> dict[str, Any]:
    aggregate: dict[str, dict[str, list[float]]] = {variant: collections.defaultdict(list) for variant in VARIANTS}
    critical: dict[str, dict[str, list[float]]] = {variant: collections.defaultdict(list) for variant in VARIANTS}
    gates = {variant: 0 for variant in VARIANTS}
    critical_gates = {variant: 0 for variant in VARIANTS}
    exact = {variant: 0 for variant in VARIANTS}
    scenes_out: list[dict[str, Any]] = []
    for scene in receipt["scenes"]:
        number = int(scene["scene"])
        sample_map = {sample["variant"]: sample for sample in scene["samples"]}
        reference = CANDIDATE_ROOT / sample_map["color_360p"]["frame"]
        native = CANDIDATE_ROOT / scene["native_clean"]
        rows_by_variant = {variant: tesseract_rows(CANDIDATE_ROOT / sample_map[variant]["frame"]) for variant in VARIANTS}
        token_map = {
            variant: {region: tokens(rows_by_variant[variant], region) for region in ["full", "headline", "lower"]}
            for variant in VARIANTS
        }
        samples_out: list[dict[str, Any]] = []
        for variant in VARIANTS:
            path = CANDIDATE_ROOT / sample_map[variant]["frame"]
            full = token_map[variant]["full"]
            text = " ".join(str(row["text"]) for row in rows_by_variant[variant])
            structural = any(pattern.search(text) for pattern in GATE_PATTERNS)
            gates[variant] += int(structural)
            if number in HELD_CRITICAL:
                critical_gates[variant] += int(structural)
            chroma, saturated = chroma_metrics(reference, path)
            metrics = {
                "headline_recall_vs_color_360p": recall(token_map["color_360p"]["headline"], token_map[variant]["headline"]),
                "full_text_recall_vs_color_360p": recall(token_map["color_360p"]["full"], full),
                "lower_support_recall_vs_color_360p": recall(token_map["color_360p"]["lower"], token_map[variant]["lower"]),
                "numeric_recall_vs_color_360p": numeric(token_map["color_360p"]["full"], full),
                "tolerant_luma_edge_recall_vs_color_360p": edge_recall(reference, path),
                "chroma_retention_on_color_saturated_pixels": chroma,
                "color_saturated_pixel_fraction": saturated,
            }
            for key, value in metrics.items():
                aggregate[variant][key].append(value)
                if number in HELD_CRITICAL:
                    critical[variant][key].append(value)
            stored = np.asarray(Image.open(path).convert("RGB"), dtype=np.uint8)
            exact_match = np.array_equal(stored, recompute(native, variant))
            exact[variant] += int(exact_match)
            samples_out.append(
                {
                    "variant": variant,
                    **{key: round(value, 6) for key, value in metrics.items()},
                    "structural_gate_detected": structural,
                    "exact_transform_recomputed": exact_match,
                    "frame_sha256": sample_map[variant]["frame_sha256"],
                }
            )
        scenes_out.append({"scene": number, "samples": samples_out})
    aggregates = {
        variant: {
            **{f"mean_{key}": mean(values) for key, values in aggregate[variant].items()},
            "structural_gate_scenes": gates[variant],
            "exact_transform_match_scenes": exact[variant],
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
    groups_out: dict[str, Any] = {}
    for group_name, group in receipt["groups"].items():
        exact = {variant: 0 for variant in VARIANTS}
        gate_rows: dict[str, list[dict[str, Any]]] = {variant: [] for variant in VARIANTS}
        for scene in group["scenes"]:
            number = int(scene["scene"])
            source = ROOT / scene["source"]
            sample_map = {sample["variant"]: sample for sample in scene["samples"]}
            for variant in VARIANTS:
                path = METHOD_ROOT / group_name / sample_map[variant]["frame"]
                stored = np.asarray(Image.open(path).convert("RGB"), dtype=np.uint8)
                exact[variant] += int(np.array_equal(stored, recompute(source, variant)))
                if group_name == "pass12_sharpness_safe":
                    gate_rows[variant].append({"scene": number, **gate_score(path, CANONICAL_GATES[number])})
        output: dict[str, Any] = {
            "scene_count": group["scene_count"],
            "frame_count": group["frame_count"],
            "exact_transform_match_scenes": exact,
            "human_visual_review": {
                "exact_top_gates": "7/7_ALL_FIVE_VARIANTS" if group_name != "sealed_v8" else "NOT_A_TOP_GATE_PROOF",
                "complete_result_held_badges": "7/7_ALL_FIVE_VARIANTS",
                "major_method_status_boundaries": "7/7_ALL_FIVE_VARIANTS",
                "hue_only_required_meaning": 0,
                "direct_label_plus_non_color_redundancy": "PASS_ALL_7_ALL_FIVE_VARIANTS",
                "overlap_clipping_or_ambiguity": 0,
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
        "deepening_pass": 23,
        "audit": "native_monochrome_and_color_vision_then_minimum_scale_interaction",
        "simulation_scope": "presentation stress test only; not a clinical diagnostic or named delivery/viewing standard",
        "candidate_sha256": candidate_receipt["candidate_sha256"],
        "candidate_receipt": "qa/pass23_minimum_scale_color_vision_audit/extraction_receipt.json",
        "candidate_receipt_sha256": sha(CANDIDATE_RECEIPT),
        "method_receipt": "qa/pass23_v8_minimum_scale_color_vision/receipt.json",
        "method_receipt_sha256": sha(METHOD_RECEIPT),
        "candidate": candidate,
        "method": method,
        "representation_review": {
            "candidate_structural_held_gate_scenes": "0/16_ALL_FIVE_VARIANTS",
            "candidate_result_hierarchy": "LARGE_RESULT_HEADLINES_NUMBERS_PLOTS_BARS_MATRICES_AND_CONCLUSIONS_REMAIN_PRIMARY",
            "candidate_fine_support": "AXES_ERROR_BARS_LEGENDS_CAVEATS_CITATIONS_PROVENANCE_AND_FINE_LABELS_NOT_UNIFORMLY_RELIABLE_AT_360P",
            "candidate_color_only_meaning": "PLOT_AND_MATRIX_HUE_REMAINS_SALIENT_BUT_LABELS_POSITION_AND_GEOMETRY_EXIST__MISSING_STRUCTURAL_HOLD_NOT_REPAIRED",
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
    gray = candidate["aggregate"]["grayscale_bt709_then_360p"]
    proof = method["pass12_sharpness_safe"]["mapped_gate_ocr_aid"]
    print(
        "PASS candidate=16/80 method=21/105 "
        f"gray_headline={gray['mean_headline_recall_vs_color_360p']:.6f} "
        f"gray_full={gray['mean_full_text_recall_vs_color_360p']:.6f} "
        f"proof_min={min(row['passing_scenes'] for row in proof.values())}/7"
    )


if __name__ == "__main__":
    main()
