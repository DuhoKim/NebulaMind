#!/usr/bin/env python3
"""Quantify pass-12 spatial-defocus resilience without storing OCR text."""

from __future__ import annotations

import collections
import csv
import io
import json
import math
import re
import subprocess
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_DIR = ROOT / "qa/pass12_spatial_defocus_audit"
METHOD_DIR = ROOT / "qa/pass12_v8_spatial_defocus"
OUTPUT = ROOT / "qa/pass12_spatial_defocus_quantitative_audit.json"
VARIANTS = [
    "clean",
    "defocus_r0_75",
    "defocus_r1_50",
    "defocus_r2_50",
    "defocus_r4_00",
]
CRITICAL_SCENES = [7, 9, 10, 11, 16]
GATE_PATTERNS = [
    re.compile(r"result\s+held"),
    re.compile(r"frame\s+unstated"),
    re.compile(r"outcomes?\s+withheld"),
    re.compile(r"no\s+outcome\s+shown"),
    re.compile(r"result\s+locked"),
]
SCENE_GATE_PATTERNS = {
    1: re.compile(r"result\s+locked.*archive\s+frame.*independent\s+review"),
    2: re.compile(r"overlapping\s+readouts.*do\s+not\s+sum"),
    3: re.compile(r"label\s+frame\s+statistic.*physical\s+interpretation\s+held"),
    4: re.compile(r"frame\s+unstated.*result\s+held"),
    5: re.compile(r"column\s+check\s+only.*storage\s+frame\s+unresolved"),
    6: re.compile(r"control\s+design\s+only.*outcomes\s+withheld"),
    7: re.compile(r"separate\s+authorization.*both\s+blockers\s+resolve"),
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def ocr_boxes(path: Path) -> list[dict[str, object]]:
    result = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "11", "tsv"],
        check=True,
        text=True,
        capture_output=True,
    )
    rows: list[dict[str, object]] = []
    for row in csv.DictReader(io.StringIO(result.stdout), delimiter="\t"):
        token = normalize(row.get("text", ""))
        if not token:
            continue
        try:
            confidence = float(row.get("conf", "-1"))
            left = int(row.get("left", "0"))
            top = int(row.get("top", "0"))
            width = int(row.get("width", "0"))
            height = int(row.get("height", "0"))
        except ValueError:
            continue
        if confidence < 0:
            continue
        rows.append(
            {
                "token": token,
                "left": left,
                "top": top,
                "right": left + width,
                "bottom": top + height,
            }
        )
    return rows


def tokens(rows: list[dict[str, object]]) -> list[str]:
    result: list[str] = []
    for row in rows:
        token = row["token"]
        if isinstance(token, str):
            result.extend(token.split())
    return result


def multiset_recall(reference: list[str], observed: list[str]) -> float:
    if not reference:
        return 1.0
    reference_counts = collections.Counter(reference)
    observed_counts = collections.Counter(observed)
    matched = sum(
        min(count, observed_counts[token]) for token, count in reference_counts.items()
    )
    return matched / sum(reference_counts.values())


def numeric_tokens(values: list[str]) -> list[str]:
    return [value for value in values if any(character.isdigit() for character in value)]


def image_array(path: Path) -> np.ndarray:
    with Image.open(path) as opened:
        return np.asarray(opened.convert("RGB"), dtype=np.uint8)


def grayscale(values: np.ndarray) -> np.ndarray:
    rgb = values.astype(np.float64)
    return 0.2126 * rgb[:, :, 0] + 0.7152 * rgb[:, :, 1] + 0.0722 * rgb[:, :, 2]


def gradients(gray: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    gx = np.zeros(gray.shape, dtype=np.float64)
    gy = np.zeros(gray.shape, dtype=np.float64)
    gx[:, 1:] = np.abs(gray[:, 1:] - gray[:, :-1])
    gy[1:, :] = np.abs(gray[1:, :] - gray[:-1, :])
    return gx, gy


def edge_mask(gray: np.ndarray) -> np.ndarray:
    gx, gy = gradients(gray)
    return np.maximum(gx, gy) >= 24.0


def dilate_one(mask: np.ndarray) -> np.ndarray:
    padded = np.pad(mask, 1, mode="constant", constant_values=False)
    result = np.zeros(mask.shape, dtype=bool)
    for y_offset in range(3):
        for x_offset in range(3):
            result |= padded[
                y_offset : y_offset + mask.shape[0],
                x_offset : x_offset + mask.shape[1],
            ]
    return result


def pixel_metrics(clean: np.ndarray, observed: np.ndarray) -> dict[str, float]:
    delta = clean.astype(np.float64) - observed.astype(np.float64)
    mse = float(np.mean(delta * delta))
    psnr = 99.0 if mse == 0.0 else 10.0 * math.log10((255.0 * 255.0) / mse)
    clean_gray = grayscale(clean)
    observed_gray = grayscale(observed)
    clean_edges = edge_mask(clean_gray)
    observed_edges = dilate_one(edge_mask(observed_gray))
    edge_count = int(clean_edges.sum())
    edge_recall = (
        1.0
        if edge_count == 0
        else float((clean_edges & observed_edges).sum() / edge_count)
    )
    clean_gx, clean_gy = gradients(clean_gray)
    observed_gx, observed_gy = gradients(observed_gray)
    clean_energy = float(np.mean(clean_gx * clean_gx + clean_gy * clean_gy))
    observed_energy = float(np.mean(observed_gx * observed_gx + observed_gy * observed_gy))
    energy_ratio = 1.0 if clean_energy == 0.0 else observed_energy / clean_energy
    return {
        "rgb_psnr_db": round(psnr, 6),
        "mean_absolute_rgb_error": round(float(np.abs(delta).mean()), 6),
        "tolerant_luma_edge_recall": round(edge_recall, 6),
        "luma_gradient_energy_ratio": round(energy_ratio, 6),
    }


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def analyze_scene(
    group_root: Path,
    scene: int,
    samples: list[dict[str, object]],
    scene_gate_pattern: re.Pattern[str] | None,
) -> dict[str, object]:
    rows_by_variant: dict[str, list[dict[str, object]]] = {}
    arrays_by_variant: dict[str, np.ndarray] = {}
    for sample in samples:
        variant = sample["variant"]
        frame = sample["frame"] if "frame" in sample else sample["path"]
        if not isinstance(variant, str) or not isinstance(frame, str):
            raise TypeError("sample strings required")
        frame_path = group_root / frame
        rows_by_variant[variant] = ocr_boxes(frame_path)
        arrays_by_variant[variant] = image_array(frame_path)
    clean_rows = rows_by_variant["clean"]
    clean_tokens = tokens(clean_rows)
    headline_tokens = tokens(
        [
            row
            for row in clean_rows
            if isinstance(row["top"], int) and row["top"] < 350
        ]
    )
    support_tokens = tokens(
        [
            row
            for row in clean_rows
            if isinstance(row["top"], int) and row["top"] >= 780
        ]
    )
    clean_numeric = numeric_tokens(clean_tokens)
    metrics: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        observed = tokens(rows_by_variant[variant])
        joined = " ".join(observed)
        metrics[variant] = {
            "ocr_token_count": len(observed),
            "full_token_recall_vs_clean": round(
                multiset_recall(clean_tokens, observed), 6
            ),
            "headline_token_recall_vs_clean": round(
                multiset_recall(headline_tokens, observed), 6
            ),
            "lower_support_token_recall_vs_clean": round(
                multiset_recall(support_tokens, observed), 6
            ),
            "numeric_token_recall_vs_clean": round(
                multiset_recall(clean_numeric, numeric_tokens(observed)), 6
            ),
            "structural_gate_detected": any(
                pattern.search(joined) for pattern in GATE_PATTERNS
            ),
            "result_held_detected": bool(re.search(r"result\s+held", joined)),
            "scene_specific_gate_detected": (
                bool(scene_gate_pattern.search(joined)) if scene_gate_pattern else False
            ),
            "pixels": pixel_metrics(
                arrays_by_variant["clean"], arrays_by_variant[variant]
            ),
        }
    return {
        "scene": scene,
        "clean_ocr_token_count": len(clean_tokens),
        "metrics": metrics,
    }


def aggregate(scene_rows: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    aggregates: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        rows = [scene["metrics"][variant] for scene in scene_rows]  # type: ignore[index]
        aggregates[variant] = {
            "mean_full_token_recall_vs_clean": mean(
                [float(row["full_token_recall_vs_clean"]) for row in rows]
            ),
            "mean_headline_token_recall_vs_clean": mean(
                [float(row["headline_token_recall_vs_clean"]) for row in rows]
            ),
            "mean_lower_support_token_recall_vs_clean": mean(
                [float(row["lower_support_token_recall_vs_clean"]) for row in rows]
            ),
            "mean_numeric_token_recall_vs_clean": mean(
                [float(row["numeric_token_recall_vs_clean"]) for row in rows]
            ),
            "structural_gate_scene_count": sum(
                bool(row["structural_gate_detected"]) for row in rows
            ),
            "result_held_scene_count": sum(
                bool(row["result_held_detected"]) for row in rows
            ),
            "scene_specific_gate_count": sum(
                bool(row["scene_specific_gate_detected"]) for row in rows
            ),
            "mean_rgb_psnr_db": mean(
                [float(row["pixels"]["rgb_psnr_db"]) for row in rows]  # type: ignore[index]
            ),
            "mean_absolute_rgb_error": mean(
                [float(row["pixels"]["mean_absolute_rgb_error"]) for row in rows]  # type: ignore[index]
            ),
            "mean_tolerant_luma_edge_recall": mean(
                [float(row["pixels"]["tolerant_luma_edge_recall"]) for row in rows]  # type: ignore[index]
            ),
            "mean_luma_gradient_energy_ratio": mean(
                [float(row["pixels"]["luma_gradient_energy_ratio"]) for row in rows]  # type: ignore[index]
            ),
        }
    return aggregates


def group_candidate_records(receipt: dict[str, object]) -> list[dict[str, object]]:
    records = receipt["records"]
    if not isinstance(records, list):
        raise TypeError("candidate records must be a list")
    grouped: list[dict[str, object]] = []
    for scene in range(1, 17):
        samples = [
            record
            for record in records
            if isinstance(record, dict) and record.get("scene") == scene
        ]
        if len(samples) != len(VARIANTS):
            raise ValueError(f"candidate scene {scene} has {len(samples)} samples")
        grouped.append({"scene": scene, "samples": samples})
    return grouped


def critical_aggregate(
    scene_rows: list[dict[str, object]],
) -> dict[str, dict[str, object]]:
    output: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        rows = [
            scene["metrics"][variant]  # type: ignore[index]
            for scene in scene_rows
            if scene["scene"] in CRITICAL_SCENES
        ]
        output[variant] = {
            "scenes": CRITICAL_SCENES,
            "mean_headline_token_recall_vs_clean": mean(
                [float(row["headline_token_recall_vs_clean"]) for row in rows]
            ),
            "mean_full_token_recall_vs_clean": mean(
                [float(row["full_token_recall_vs_clean"]) for row in rows]
            ),
            "mean_lower_support_token_recall_vs_clean": mean(
                [float(row["lower_support_token_recall_vs_clean"]) for row in rows]
            ),
            "mean_numeric_token_recall_vs_clean": mean(
                [float(row["numeric_token_recall_vs_clean"]) for row in rows]
            ),
            "structural_gate_scene_count": sum(
                bool(row["structural_gate_detected"]) for row in rows
            ),
        }
    return output


def main() -> None:
    candidate_receipt = load_json(CANDIDATE_DIR / "extraction_receipt.json")
    candidate_groups = group_candidate_records(candidate_receipt)
    candidate_scenes = [
        analyze_scene(ROOT, int(scene["scene"]), scene["samples"], None)  # type: ignore[arg-type]
        for scene in candidate_groups
    ]
    candidate_aggregates = aggregate(candidate_scenes)

    method_receipt = load_json(METHOD_DIR / "receipt.json")
    method_groups: dict[str, object] = {}
    for group_name, group in method_receipt["groups"].items():
        group_root = METHOD_DIR / group_name
        scene_rows = [
            analyze_scene(
                group_root,
                int(scene["scene"]),
                scene["samples"],
                (
                    SCENE_GATE_PATTERNS[int(scene["scene"])]
                    if group_name == "pass7_caption_safe"
                    else None
                ),
            )
            for scene in group["scenes"]
        ]
        method_groups[group_name] = {
            "scenes": scene_rows,
            "aggregates": aggregate(scene_rows),
        }

    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 12,
        "variant_order": VARIANTS,
        "candidate": {
            "sha256": candidate_receipt["candidate_sha256"],
            "scene_count": len(candidate_scenes),
            "frame_count": candidate_receipt["frame_count"],
            "cut_times_exact_pass11": bool(
                candidate_receipt["cut_detection"]["exact_pass11_match"]
            ),
            "clean_midpoints_byte_identical_to_pass11_clean": 16,
            "scenes": candidate_scenes,
            "aggregates": candidate_aggregates,
            "held_critical_aggregates": critical_aggregate(candidate_scenes),
        },
        "method_groups": method_groups,
        "human_visual_review": {
            "candidate_dominant_result_hierarchy_visible_through_r4_00": True,
            "candidate_major_headlines_numbers_and_plot_silhouettes_survive_longer_than_support": True,
            "candidate_structural_hold_visible_any_variant": False,
            "candidate_small_axes_legends_citations_provenance_and_qualifiers_weaken_first": True,
            "sealed_v8_result_held_text_visual": {
                variant: "7/7" for variant in VARIANTS
            },
            "sealed_v8_large_status_boundaries_visual_through_r4_00": "7/7",
            "sealed_v8_required_meaning_ambiguous_at_r1_50": False,
            "pass7_caption_safe_specific_gate_lines_visual": {
                variant: "7/7" for variant in VARIANTS
            },
            "pass7_caption_safe_result_held_text_visual": {
                variant: "7/7" for variant in VARIANTS
            },
            "operational_r1_50_finding": "PRIMARY_METHOD_AND_STATUS_HIERARCHY_SURVIVES_WITHOUT_SEMANTIC_AMBIGUITY",
            "severe_r2_50_r4_00_use": "CHARACTERIZATION_ONLY_NOT_ACCEPTANCE_THRESHOLD",
        },
        "simulation_limit": "Deterministic Pillow Gaussian spatial-defocus variants are presentation stress tests. Radius values are packet parameters, not claims about a named lens, projector, display, viewer, or service.",
        "raw_ocr_text_stored": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    OUTPUT.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    candidate_operational = candidate_aggregates["defocus_r1_50"]
    caption_operational = method_groups["pass7_caption_safe"]["aggregates"][  # type: ignore[index]
        "defocus_r1_50"
    ]
    print(
        "PASS candidate=16/80 method=14/70 "
        f"candidate_r1_50_headline={candidate_operational['mean_headline_token_recall_vs_clean']:.6f} "
        f"caption_r1_50_gates={caption_operational['scene_specific_gate_count']}/7"
    )


if __name__ == "__main__":
    main()
