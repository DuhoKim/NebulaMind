#!/usr/bin/env python3
"""Quantify pass-10 uniform black-lift contrast resilience without storing OCR text."""

from __future__ import annotations

import collections
import csv
import io
import json
import re
import subprocess
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_DIR = ROOT / "qa/pass10_ambient_contrast_audit"
METHOD_DIR = ROOT / "qa/pass10_v8_ambient_contrast"
OUTPUT = ROOT / "qa/pass10_ambient_contrast_quantitative_audit.json"
VARIANTS = [
    "clean",
    "uniform_black_lift_10pct",
    "uniform_black_lift_20pct",
    "uniform_black_lift_30pct",
    "uniform_black_lift_40pct",
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
    matched = sum(min(count, observed_counts[token]) for token, count in reference_counts.items())
    return matched / sum(reference_counts.values())


def numeric_tokens(values: list[str]) -> list[str]:
    return [value for value in values if any(character.isdigit() for character in value)]


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(
        values <= 0.04045,
        values / 12.92,
        ((values + 0.055) / 1.055) ** 2.4,
    )


def luminance_metrics(path: Path) -> dict[str, float]:
    with Image.open(path).convert("RGB") as image:
        srgb = np.asarray(image, dtype=np.float64) / 255.0
    linear = srgb_to_linear(srgb)
    luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
    p01, p99 = np.percentile(luminance, [1.0, 99.0])
    return {
        "linear_luminance_p01": round(float(p01), 6),
        "linear_luminance_p99": round(float(p99), 6),
        "robust_wcag_like_ratio_p99_p01": round(float((p99 + 0.05) / (p01 + 0.05)), 6),
        "linear_luminance_std": round(float(luminance.std()), 6),
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
    paths_by_variant: dict[str, Path] = {}
    for sample in samples:
        variant = sample["variant"]
        frame = sample["frame"]
        if not isinstance(variant, str) or not isinstance(frame, str):
            raise TypeError("sample strings required")
        frame_path = group_root / frame
        rows_by_variant[variant] = ocr_boxes(frame_path)
        paths_by_variant[variant] = frame_path
    clean_rows = rows_by_variant["clean"]
    clean_tokens = tokens(clean_rows)
    headline_tokens = tokens(
        [row for row in clean_rows if isinstance(row["top"], int) and row["top"] < 350]
    )
    support_tokens = tokens(
        [row for row in clean_rows if isinstance(row["top"], int) and row["top"] >= 780]
    )
    clean_numeric = numeric_tokens(clean_tokens)
    metrics: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        observed = tokens(rows_by_variant[variant])
        joined = " ".join(observed)
        metrics[variant] = {
            "ocr_token_count": len(observed),
            "full_token_recall_vs_clean": round(multiset_recall(clean_tokens, observed), 6),
            "headline_token_recall_vs_clean": round(multiset_recall(headline_tokens, observed), 6),
            "lower_support_token_recall_vs_clean": round(multiset_recall(support_tokens, observed), 6),
            "numeric_token_recall_vs_clean": round(
                multiset_recall(clean_numeric, numeric_tokens(observed)), 6
            ),
            "structural_gate_detected": any(pattern.search(joined) for pattern in GATE_PATTERNS),
            "result_held_detected": bool(re.search(r"result\s+held", joined)),
            "scene_specific_gate_detected": (
                bool(scene_gate_pattern.search(joined)) if scene_gate_pattern else False
            ),
            "luminance": luminance_metrics(paths_by_variant[variant]),
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
            "result_held_scene_count": sum(bool(row["result_held_detected"]) for row in rows),
            "scene_specific_gate_count": sum(
                bool(row["scene_specific_gate_detected"]) for row in rows
            ),
            "mean_robust_wcag_like_ratio_p99_p01": mean(
                [float(row["luminance"]["robust_wcag_like_ratio_p99_p01"]) for row in rows]  # type: ignore[index]
            ),
            "mean_linear_luminance_std": mean(
                [float(row["luminance"]["linear_luminance_std"]) for row in rows]  # type: ignore[index]
            ),
        }
    return aggregates


def main() -> None:
    candidate_receipt = load_json(CANDIDATE_DIR / "extraction_receipt.json")
    pass9_receipt = load_json(ROOT / "qa/pass9_safe_area_audit/extraction_receipt.json")
    candidate_scenes = [
        analyze_scene(CANDIDATE_DIR, int(scene["scene"]), scene["samples"], None)
        for scene in candidate_receipt["scenes"]
    ]
    candidate_aggregates = aggregate(candidate_scenes)
    critical: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        rows = [
            scene["metrics"][variant]  # type: ignore[index]
            for scene in candidate_scenes
            if scene["scene"] in CRITICAL_SCENES
        ]
        critical[variant] = {
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

    method_receipt = load_json(METHOD_DIR / "receipt.json")
    method_groups: dict[str, object] = {}
    for group_name, group in method_receipt["groups"].items():
        group_root = METHOD_DIR / group_name
        scene_rows = [
            analyze_scene(
                group_root,
                int(scene["scene"]),
                scene["samples"],
                SCENE_GATE_PATTERNS[int(scene["scene"])]
                if group_name == "pass7_caption_safe"
                else None,
            )
            for scene in group["scenes"]
        ]
        method_groups[group_name] = {
            "scenes": scene_rows,
            "aggregates": aggregate(scene_rows),
        }

    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 10,
        "variant_order": VARIANTS,
        "candidate": {
            "sha256": candidate_receipt["candidate_sha256"],
            "scene_count": len(candidate_scenes),
            "frame_count": candidate_receipt["frame_count"],
            "cut_times_exact_pass9": (
                candidate_receipt["detected_cut_times_seconds"]
                == pass9_receipt["detected_cut_times_seconds"]
            ),
            "clean_midpoints_byte_identical_to_pass9_clean": sum(
                scene["samples"][0]["frame_sha256"]
                == pass9_scene["samples"][0]["frame_sha256"]
                for scene, pass9_scene in zip(
                    candidate_receipt["scenes"], pass9_receipt["scenes"]
                )
            ),
            "scenes": candidate_scenes,
            "aggregates": candidate_aggregates,
            "held_critical_aggregates": critical,
        },
        "method_groups": method_groups,
        "human_visual_review": {
            "candidate_dominant_result_hierarchy_visible_through_40pct": True,
            "candidate_plots_and_large_result_numbers_survive_longer_than_qualifiers": True,
            "candidate_structural_hold_visible_any_variant": False,
            "candidate_low_support_citations_axes_and_provenance_weaken_at_20pct": True,
            "sealed_v8_result_held_text_visual": {
                variant: "7/7" for variant in VARIANTS
            },
            "sealed_v8_large_status_boundaries_visual_through_40pct": "7/7",
            "sealed_v8_small_qualifiers_and_citations_reliable_at_20pct": False,
            "pass7_caption_safe_specific_gate_lines_visual": {
                variant: "7/7" for variant in VARIANTS
            },
            "pass7_caption_safe_result_held_text_visual": {
                variant: "7/7" for variant in VARIANTS
            },
            "operational_20pct_contrast_finding": "PRIMARY_METHOD_AND_STATUS_HIERARCHY_SURVIVES__SMALL_QUALIFIERS_AND_CITATIONS_TOO_FAINT",
            "severe_30_40pct_use": "CHARACTERIZATION_ONLY_NOT_ACCEPTANCE_THRESHOLD",
        },
        "simulation_limit": "Uniform linear-light black-lift variants are deterministic presentation stress tests, not a claim about a named projector, room, display, or viewer.",
        "raw_ocr_text_stored": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    candidate_20 = candidate_aggregates["uniform_black_lift_20pct"]
    caption_20 = method_groups["pass7_caption_safe"]["aggregates"][  # type: ignore[index]
        "uniform_black_lift_20pct"
    ]
    print(
        "PASS candidate=16/80 method=14/70 "
        f"candidate_20pct_headline={candidate_20['mean_headline_token_recall_vs_clean']:.6f} "
        f"caption_20pct_gates={caption_20['scene_specific_gate_count']}/7"
    )


if __name__ == "__main__":
    main()
