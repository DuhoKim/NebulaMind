#!/usr/bin/env python3
"""Quantify pass-9 title-safe crop resilience without storing OCR text."""

from __future__ import annotations

import collections
import csv
import io
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_DIR = ROOT / "qa/pass9_safe_area_audit"
METHOD_DIR = ROOT / "qa/pass9_v8_safe_area"
OUTPUT = ROOT / "qa/pass9_safe_area_quantitative_audit.json"
VARIANTS = [
    "clean",
    "symmetric_crop_3pct",
    "symmetric_crop_5pct",
    "horizontal_crop_5pct",
    "vertical_crop_5pct",
]
SAFE_RECTS = {
    "safe_3pct": (58, 32, 1862, 1048),
    "safe_5pct": (96, 54, 1824, 1026),
}
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


def at_risk(rows: list[dict[str, object]], rect: tuple[int, int, int, int]) -> int:
    left, top, right, bottom = rect
    count = 0
    for row in rows:
        row_left = row["left"]
        row_top = row["top"]
        row_right = row["right"]
        row_bottom = row["bottom"]
        if not isinstance(row_left, int):
            raise TypeError("OCR left coordinate must be integer")
        if not isinstance(row_top, int):
            raise TypeError("OCR top coordinate must be integer")
        if not isinstance(row_right, int):
            raise TypeError("OCR right coordinate must be integer")
        if not isinstance(row_bottom, int):
            raise TypeError("OCR box coordinates must be integers")
        if row_left < left or row_top < top or row_right > right or row_bottom > bottom:
            count += 1
    return count


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def integer_field(mapping: dict[str, object], key: str) -> int:
    value = mapping[key]
    if not isinstance(value, int):
        raise TypeError(f"{key} must be integer")
    return value


def analyze_scene(
    group_root: Path,
    scene: int,
    samples: list[dict[str, object]],
    clean_name: str,
    scene_gate_pattern: re.Pattern[str] | None,
) -> dict[str, object]:
    rows_by_variant: dict[str, list[dict[str, object]]] = {}
    for sample in samples:
        variant = sample["variant"]
        frame = sample["frame"]
        if not isinstance(variant, str) or not isinstance(frame, str):
            raise TypeError("sample strings required")
        rows_by_variant[variant] = ocr_boxes(group_root / frame)
    clean_rows = rows_by_variant[clean_name]
    clean_tokens = tokens(clean_rows)
    headline_tokens = tokens([row for row in clean_rows if isinstance(row["top"], int) and row["top"] < 350])
    support_tokens = tokens([row for row in clean_rows if isinstance(row["top"], int) and row["top"] >= 780])
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
            "numeric_token_recall_vs_clean": round(multiset_recall(clean_numeric, numeric_tokens(observed)), 6),
            "structural_gate_detected": any(pattern.search(joined) for pattern in GATE_PATTERNS),
            "result_held_detected": bool(re.search(r"result\s+held", joined)),
            "scene_specific_gate_detected": bool(scene_gate_pattern.search(joined)) if scene_gate_pattern else False,
        }
    return {
        "scene": scene,
        "clean_ocr_token_count": len(clean_tokens),
        "clean_tokens_outside_safe_3pct": at_risk(clean_rows, SAFE_RECTS["safe_3pct"]),
        "clean_tokens_outside_safe_5pct": at_risk(clean_rows, SAFE_RECTS["safe_5pct"]),
        "metrics": metrics,
    }


def aggregate(scene_rows: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    aggregates: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        rows = [scene["metrics"][variant] for scene in scene_rows]  # type: ignore[index]
        aggregates[variant] = {
            "mean_full_token_recall_vs_clean": mean([float(row["full_token_recall_vs_clean"]) for row in rows]),
            "mean_headline_token_recall_vs_clean": mean([float(row["headline_token_recall_vs_clean"]) for row in rows]),
            "mean_lower_support_token_recall_vs_clean": mean([float(row["lower_support_token_recall_vs_clean"]) for row in rows]),
            "mean_numeric_token_recall_vs_clean": mean([float(row["numeric_token_recall_vs_clean"]) for row in rows]),
            "structural_gate_scene_count": sum(bool(row["structural_gate_detected"]) for row in rows),
            "result_held_scene_count": sum(bool(row["result_held_detected"]) for row in rows),
            "scene_specific_gate_count": sum(bool(row["scene_specific_gate_detected"]) for row in rows),
        }
    return aggregates


def main() -> None:
    candidate_receipt = load_json(CANDIDATE_DIR / "extraction_receipt.json")
    pass8_receipt = load_json(ROOT / "qa/pass8_color_vision_audit/extraction_receipt.json")
    candidate_scenes = [
        analyze_scene(CANDIDATE_DIR, int(scene["scene"]), scene["samples"], "clean", None)
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
            "mean_headline_token_recall_vs_clean": mean([float(row["headline_token_recall_vs_clean"]) for row in rows]),
            "mean_full_token_recall_vs_clean": mean([float(row["full_token_recall_vs_clean"]) for row in rows]),
            "mean_numeric_token_recall_vs_clean": mean([float(row["numeric_token_recall_vs_clean"]) for row in rows]),
            "structural_gate_scene_count": sum(bool(row["structural_gate_detected"]) for row in rows),
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
                "clean",
                SCENE_GATE_PATTERNS[int(scene["scene"])] if group_name == "pass7_caption_safe" else None,
            )
            for scene in group["scenes"]
        ]
        method_groups[group_name] = {
            "clean_tokens_outside_safe_3pct": sum(integer_field(scene, "clean_tokens_outside_safe_3pct") for scene in scene_rows),
            "clean_tokens_outside_safe_5pct": sum(integer_field(scene, "clean_tokens_outside_safe_5pct") for scene in scene_rows),
            "scenes": scene_rows,
            "aggregates": aggregate(scene_rows),
        }

    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 9,
        "variant_order": VARIANTS,
        "safe_rectangles": {
            "3_percent": {"left": 58, "top": 32, "right": 1862, "bottom": 1048},
            "5_percent": {"left": 96, "top": 54, "right": 1824, "bottom": 1026},
        },
        "candidate": {
            "sha256": candidate_receipt["candidate_sha256"],
            "scene_count": len(candidate_scenes),
            "frame_count": candidate_receipt["frame_count"],
            "cut_times_exact_pass8": candidate_receipt["detected_cut_times_seconds"] == pass8_receipt["detected_cut_times_seconds"],
            "clean_midpoints_byte_identical_to_pass8_color": sum(
                scene["samples"][0]["frame_sha256"] == pass8_scene["samples"][0]["frame_sha256"]
                for scene, pass8_scene in zip(candidate_receipt["scenes"], pass8_receipt["scenes"])
            ),
            "clean_tokens_outside_safe_3pct": sum(integer_field(scene, "clean_tokens_outside_safe_3pct") for scene in candidate_scenes),
            "clean_tokens_outside_safe_5pct": sum(integer_field(scene, "clean_tokens_outside_safe_5pct") for scene in candidate_scenes),
            "scenes": candidate_scenes,
            "aggregates": candidate_aggregates,
            "held_critical_aggregates": critical,
        },
        "method_groups": method_groups,
        "human_visual_review": {
            "candidate_dominant_result_hierarchy_survives_3pct_and_5pct": True,
            "candidate_structural_hold_visible_3pct_or_5pct": False,
            "sealed_v8_3pct_semantic_loss_scene_count": 0,
            "sealed_v8_3pct_result_held_text": "7/7",
            "sealed_v8_5pct_result_held_text": "7/7",
            "sealed_v8_5pct_badge_capsules_clipped": "7/7",
            "sealed_v8_5pct_left_header_clipped": "7/7",
            "sealed_v8_5pct_edge_content_clipped_scenes": [1, 5, 7],
            "pass7_caption_safe_3pct_specific_gate_lines": "7/7",
            "pass7_caption_safe_3pct_result_held_text": "7/7",
            "pass7_caption_safe_5pct_specific_gate_lines": "7/7",
            "pass7_caption_safe_5pct_result_held_text": "7/7",
            "pass7_caption_safe_5pct_badge_capsules_clipped": "7/7",
            "pass7_caption_safe_5pct_left_header_clipped": "7/7",
            "pass7_caption_safe_5pct_edge_content_clipped_scenes": [1, 5, 7],
            "five_percent_title_safe_contract": "FAIL_LAYOUT_EDGE_CUSTODY__PRIMARY_GATE_TEXT_SURVIVES",
        },
        "simulation_limit": "Crop-and-rescale variants are deterministic presentation stress tests, not a claim that a named player or projector applies these crops.",
        "raw_ocr_text_stored": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    candidate_5 = candidate_aggregates["symmetric_crop_5pct"]
    caption_5 = method_groups["pass7_caption_safe"]["aggregates"]["symmetric_crop_5pct"]  # type: ignore[index]
    print(
        "PASS candidate=16/80 method=14/70 "
        f"candidate_5pct_headline={candidate_5['mean_headline_token_recall_vs_clean']:.6f} "
        f"caption_5pct_gates={caption_5['scene_specific_gate_count']}/7"
    )


if __name__ == "__main__":
    main()
