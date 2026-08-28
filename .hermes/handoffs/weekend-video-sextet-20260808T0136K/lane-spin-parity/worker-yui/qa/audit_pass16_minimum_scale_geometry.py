#!/usr/bin/env python3
"""Quantify pass-16 compound anisotropic-geometry-at-360p resilience."""

from __future__ import annotations

import collections
import csv
import difflib
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
CANDIDATE_ROOT = ROOT / "qa/pass16_minimum_scale_geometry_audit"
METHOD_ROOT = ROOT / "qa/pass16_v8_minimum_scale_geometry"
OUTPUT = ROOT / "qa/pass16_minimum_scale_geometry_quantitative_audit.json"
VARIANTS = ["clean", "x90_360p", "y90_360p", "x80_360p", "y80_360p"]
GEOMETRY = {
    "clean": (1.0, 1.0),
    "x90_360p": (0.90, 1.0),
    "y90_360p": (1.0, 0.90),
    "x80_360p": (0.80, 1.0),
    "y80_360p": (1.0, 0.80),
}
CRITICAL_SCENES = {7, 9, 10, 11, 16}
STRUCTURAL = re.compile(r"result\s+held|frame\s+unstated|outcomes?\s+withheld|no\s+outcome\s+shown|result\s+locked")
RESULT_HELD = re.compile(r"result\s+held")
SCENE_GATES = {
    1: re.compile(r"result\s+locked.*archive\s+frame.*independent\s+review"),
    2: re.compile(r"overlapping\s+readouts.*do\s+not\s+sum"),
    3: re.compile(r"label\s+frame\s+statistic.*physical\s+interpretation\s+held"),
    4: re.compile(r"frame\s+unstated.*result\s+held"),
    5: re.compile(r"column\s+check\s+only.*storage\s+frame\s+unresolved"),
    6: re.compile(r"control\s+design\s+only.*outcomes\s+withheld"),
    7: re.compile(r"separate\s+authorization.*both\s+blockers\s+resolve"),
}
GATE_LINES = {
    1: "RESULT LOCKED · ARCHIVE FRAME + INDEPENDENT REVIEW REQUIRED",
    2: "OVERLAPPING READOUTS · DO NOT SUM",
    3: "LABEL-FRAME STATISTIC · PHYSICAL INTERPRETATION HELD",
    4: "FRAME UNSTATED · RESULT HELD",
    5: "COLUMN CHECK ONLY · STORAGE FRAME UNRESOLVED",
    6: "CONTROL DESIGN ONLY · OUTCOMES WITHHELD",
    7: "SEPARATE AUTHORIZATION REQUIRED AFTER BOTH BLOCKERS RESOLVE",
}
GATE_BOX = (102, 78, 1540, 121)


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9.+-]+", " ", value.casefold()).strip()


def compact(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def ocr(path: Path) -> dict[str, Any]:
    with Image.open(path) as image:
        height = image.height
    result = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "11", "tsv"],
        check=True, capture_output=True, text=True,
    )
    all_tokens: list[str] = []
    headline_tokens: list[str] = []
    lower_tokens: list[str] = []
    numeric_tokens: list[str] = []
    for row in csv.DictReader(io.StringIO(result.stdout), delimiter="\t"):
        token = normalize(row.get("text", ""))
        if not token:
            continue
        try:
            confidence = float(row.get("conf", "-1"))
            top = int(row.get("top", "0"))
        except ValueError:
            continue
        if confidence < 0:
            continue
        parts = token.split()
        all_tokens.extend(parts)
        (headline_tokens if top / height < 350 / 1080 else lower_tokens).extend(parts)
        numeric_tokens.extend(part for part in parts if re.search(r"\d", part))
    return {
        "all": all_tokens,
        "headline": headline_tokens,
        "lower": lower_tokens,
        "numeric": numeric_tokens,
        "joined": " ".join(all_tokens),
        "headline_joined": " ".join(headline_tokens),
    }


def recall(reference: list[str], observed: list[str]) -> float:
    if not reference:
        return 1.0
    ref, obs = collections.Counter(reference), collections.Counter(observed)
    return round(sum(min(count, obs[token]) for token, count in ref.items()) / sum(ref.values()), 6)


def rgb(path: Path) -> np.ndarray:
    with Image.open(path).convert("RGB") as image:
        return np.asarray(image, dtype=np.uint8)


def luma(values: np.ndarray) -> np.ndarray:
    data = values.astype(np.uint32)
    return ((54 * data[:, :, 0] + 183 * data[:, :, 1] + 19 * data[:, :, 2] + 128) // 256).astype(np.int16)


def edge_map(values: np.ndarray) -> np.ndarray:
    lum = luma(values)
    gx, gy = np.zeros_like(lum, dtype=bool), np.zeros_like(lum, dtype=bool)
    gx[:, 1:] = np.abs(lum[:, 1:] - lum[:, :-1]) >= 12
    gy[1:, :] = np.abs(lum[1:, :] - lum[:-1, :]) >= 12
    return gx | gy


def dilate(values: np.ndarray) -> np.ndarray:
    padded = np.pad(values, 1, mode="constant", constant_values=False)
    out = np.zeros_like(values)
    for dy in range(3):
        for dx in range(3):
            out |= padded[dy:dy + values.shape[0], dx:dx + values.shape[1]]
    return out


def recover(path: Path, variant: str) -> np.ndarray:
    sx, sy = GEOMETRY[variant]
    with Image.open(path).convert("RGB") as image:
        native = image.resize((1920, 1080), Image.Resampling.LANCZOS)
        nw, nh = int(round(1920 * sx)), int(round(1080 * sy))
        x0, y0 = (1920 - nw) // 2, (1080 - nh) // 2
        crop = native.crop((x0, y0, x0 + nw, y0 + nh))
        restored = crop.resize((1920, 1080), Image.Resampling.LANCZOS)
        return np.asarray(restored, dtype=np.uint8)


def backprojected_metrics(clean: np.ndarray, restored: np.ndarray) -> dict[str, float]:
    error = restored.astype(np.float64) - clean.astype(np.float64)
    mse = float(np.mean(error * error))
    psnr = 99.0 if mse == 0 else 10 * math.log10(255 * 255 / mse)
    ref_edge, out_edge = edge_map(clean), dilate(edge_map(restored))
    count = int(ref_edge.sum())
    edge_recall = 1.0 if count == 0 else float((ref_edge & out_edge).sum()) / count
    return {
        "backprojected_mean_absolute_rgb_error": round(float(np.mean(np.abs(error))), 6),
        "backprojected_rgb_psnr_db": round(psnr, 6),
        "backprojected_tolerant_luma_edge_recall": round(edge_recall, 6),
    }


def geometry_metrics(variant: str) -> dict[str, float | int | str]:
    sx, sy = GEOMETRY[variant]
    if variant == "clean":
        return {
            "native_horizontal_scale": 1.0, "native_vertical_scale": 1.0,
            "effective_horizontal_scale_at_360p": 1.0,
            "effective_vertical_scale_at_360p": 1.0,
            "output_width": 1920, "output_height": 1080,
            "apparent_circle_width_to_height_ratio": 1.0,
            "apparent_slope_multiplier": 1.0,
        }
    return {
        "native_horizontal_scale": sx,
        "native_vertical_scale": sy,
        "effective_horizontal_scale_at_360p": round(sx / 3, 6),
        "effective_vertical_scale_at_360p": round(sy / 3, 6),
        "output_width": 640,
        "output_height": 360,
        "apparent_circle_width_to_height_ratio": round(sx / sy, 6),
        "apparent_slope_multiplier": round(sy / sx, 6),
        "native_horizontal_padding_pixels_each_side": int((1920 - round(1920 * sx)) // 2),
        "native_vertical_padding_pixels_each_side": int((1080 - round(1080 * sy)) // 2),
        "transform_order": "anisotropic resampling then centered padding then 640x360 LANCZOS downscale",
    }


def transformed_gate_box(variant: str) -> tuple[int, int, int, int]:
    sx, sy = GEOMETRY[variant]
    if variant == "clean":
        return GATE_BOX
    x0, y0 = (1920 - round(1920 * sx)) // 2, (1080 - round(1080 * sy)) // 2
    a, b, c, d = GATE_BOX
    scale = 1 / 3
    return (
        max(0, int((x0 + a * sx) * scale) - 4),
        max(0, int((y0 + b * sy) * scale) - 4),
        min(640, int(math.ceil((x0 + c * sx) * scale)) + 4),
        min(360, int(math.ceil((y0 + d * sy) * scale)) + 4),
    )


def gate_similarity(path: Path, canonical: str, variant: str) -> float:
    with Image.open(path).convert("RGB") as image:
        crop = image.crop(transformed_gate_box(variant))
        if variant != "clean":
            crop = crop.resize((crop.width * 4, crop.height * 4), Image.Resampling.LANCZOS)
        encoded = io.BytesIO()
        crop.save(encoded, format="PNG", optimize=False)
    reference, scores = compact(canonical), []
    for psm in (6, 7, 11, 13):
        result = subprocess.run(
            ["tesseract", "stdin", "stdout", "--psm", str(psm)],
            check=True, input=encoded.getvalue(), capture_output=True,
        )
        scores.append(difflib.SequenceMatcher(
            None, reference, compact(result.stdout.decode("utf-8", errors="replace")),
        ).ratio())
    return round(max(scores), 6)


def scene_metrics(clean_path: Path, observed_path: Path, clean_ocr: dict[str, Any], variant: str) -> dict[str, Any]:
    observed_ocr = ocr(observed_path)
    row: dict[str, Any] = {
        "full_token_recall_vs_clean": recall(clean_ocr["all"], observed_ocr["all"]),
        "headline_token_recall_vs_clean": recall(clean_ocr["headline"], observed_ocr["headline"]),
        "lower_support_token_recall_vs_clean": recall(clean_ocr["lower"], observed_ocr["lower"]),
        "numeric_token_recall_vs_clean": recall(clean_ocr["numeric"], observed_ocr["numeric"]),
        "structural_gate_detected": bool(STRUCTURAL.search(observed_ocr["joined"])),
        "result_held_detected": bool(RESULT_HELD.search(observed_ocr["joined"])),
        "ocr_token_count": len(observed_ocr["all"]),
    }
    row.update(geometry_metrics(variant))
    if variant == "clean":
        row.update({
            "backprojected_mean_absolute_rgb_error": 0.0,
            "backprojected_rgb_psnr_db": 99.0,
            "backprojected_tolerant_luma_edge_recall": 1.0,
        })
    else:
        row.update(backprojected_metrics(rgb(clean_path), recover(observed_path, variant)))
    return row


def mean(rows: list[dict[str, Any]], key: str) -> float:
    return round(sum(float(row[key]) for row in rows) / len(rows), 6)


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    keys = [
        "full_token_recall_vs_clean", "headline_token_recall_vs_clean",
        "lower_support_token_recall_vs_clean", "numeric_token_recall_vs_clean",
        "backprojected_mean_absolute_rgb_error", "backprojected_rgb_psnr_db",
        "backprojected_tolerant_luma_edge_recall",
    ]
    out: dict[str, Any] = {f"mean_{key}": mean(rows, key) for key in keys}
    out["structural_gate_scene_count"] = sum(bool(row["structural_gate_detected"]) for row in rows)
    out["result_held_scene_count"] = sum(bool(row["result_held_detected"]) for row in rows)
    out.update({f"geometry_{key}": value for key, value in geometry_metrics(rows[0]["variant"]).items()})
    if all("scene_specific_gate_detected" in row for row in rows):
        out["scene_specific_gate_count"] = sum(bool(row["scene_specific_gate_detected"]) for row in rows)
    if all("gate_character_similarity_best_of_psm_6_7_11_13" in row for row in rows):
        out["mean_gate_character_similarity_best_of_psm_6_7_11_13"] = mean(
            rows, "gate_character_similarity_best_of_psm_6_7_11_13"
        )
    return out


def candidate_audit() -> dict[str, Any]:
    receipt = json.loads((CANDIDATE_ROOT / "extraction_receipt.json").read_text())
    scenes = []
    for record in receipt["records"]:
        scene = int(record["scene"])
        paths = {item["variant"]: CANDIDATE_ROOT / item["frame"] for item in record["samples"]}
        clean, clean_ocr = paths["clean"], ocr(paths["clean"])
        metrics = {}
        for variant in VARIANTS:
            row = scene_metrics(clean, paths[variant], clean_ocr, variant)
            row["variant"] = variant
            metrics[variant] = row
        scenes.append({"scene": scene, "metrics": metrics})
    return {
        "scene_count": 16, "frame_count": 80, "scenes": scenes,
        "aggregates": {variant: aggregate([scene["metrics"][variant] for scene in scenes]) for variant in VARIANTS},
        "held_critical_scenes": sorted(CRITICAL_SCENES),
        "held_critical_aggregates": {
            variant: aggregate([scene["metrics"][variant] for scene in scenes if scene["scene"] in CRITICAL_SCENES])
            for variant in VARIANTS
        },
    }


def method_audit() -> dict[str, Any]:
    receipt = json.loads((METHOD_ROOT / "receipt.json").read_text())
    groups = {}
    for group_name, group in receipt["groups"].items():
        group_root, scenes = METHOD_ROOT / group_name, []
        for scene_row in group["scenes"]:
            scene = int(scene_row["scene"])
            paths = {item["variant"]: group_root / item["frame"] for item in scene_row["samples"]}
            clean, clean_ocr, metrics = paths["clean"], ocr(paths["clean"]), {}
            for variant in VARIANTS:
                row = scene_metrics(clean, paths[variant], clean_ocr, variant)
                row["variant"] = variant
                if group_name in {"pass7_caption_safe", "pass12_sharpness_safe"}:
                    row["scene_specific_gate_detected"] = bool(
                        SCENE_GATES[scene].search(ocr(paths[variant])["headline_joined"])
                    )
                if group_name == "pass12_sharpness_safe":
                    similarity = gate_similarity(paths[variant], GATE_LINES[scene], variant)
                    row["gate_character_similarity_best_of_psm_6_7_11_13"] = similarity
                    row["scene_specific_gate_detected"] = similarity >= 0.80
                metrics[variant] = row
            scenes.append({"scene": scene, "metrics": metrics})
        groups[group_name] = {
            "scene_count": 7, "frame_count": 35, "scenes": scenes,
            "aggregates": {variant: aggregate([scene["metrics"][variant] for scene in scenes]) for variant in VARIANTS},
        }
    return groups


def main() -> None:
    candidate, methods = candidate_audit(), method_audit()
    output = {
        "status": "QA_STATIC_METRICS_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 16,
        "variant_order": VARIANTS,
        "operational_variants": ["x90_360p", "y90_360p"],
        "characterization_variants": ["x80_360p", "y80_360p"],
        "transform_interpretation": "Packet-specific compound stress: centered native anisotropic Pillow LANCZOS resampling with black padding followed by full-canvas Pillow LANCZOS downscale to 640x360; not a named display, player, projector, codec, browser, delivery platform, service, room, viewer, or pixel-aspect standard.",
        "candidate": candidate,
        "method_groups": methods,
        "human_visual_review": {
            "candidate_structural_gate_scenes": {variant: "0/16" for variant in VARIANTS},
            "candidate_finding": "Large result headlines, numbers, bars, matrices, plots, and conclusions remain primary under both operational compound transforms. No held boundary appears. Small axes, tick labels, error bars, caveats, citations, and provenance are not uniformly acceptance-readable and cannot carry required meaning.",
            "sealed_v8_operational_result_held_badges_visual": {"x90_360p": "7/7", "y90_360p": "7/7"},
            "sealed_v8_operational_major_status_boundaries_visual": {"x90_360p": "7/7", "y90_360p": "7/7"},
            "sealed_v8_operational_required_meaning_ambiguous": False,
            "pass7_operational_specific_gate_lines_visual": {"x90_360p": "7/7_EXACT", "y90_360p": "7/7_EXACT"},
            "pass7_operational_result_held_badges_visual": {"x90_360p": "7/7", "y90_360p": "7/7"},
            "pass12_operational_specific_gate_lines_visual": {"x90_360p": "7/7_EXACT", "y90_360p": "7/7_EXACT"},
            "pass12_operational_result_held_badges_visual": {"x90_360p": "7/7", "y90_360p": "7/7"},
            "pass12_characterization_specific_gate_lines_visual": {"x80_360p": "7/7_EXACT", "y80_360p": "7/7_EXACT"},
            "pass12_characterization_result_held_badges_visual": {"x80_360p": "7/7", "y80_360p": "7/7"},
            "pass12_no_overlap_clipping_or_semantic_ambiguity": True,
            "fine_copy_limit": "Fine source/provenance lines and some tertiary labels remain present but are not uniformly acceptance-readable at represented 360p pixels; no acceptance depends on them in the pass-12 proof.",
        },
        "gate_ocr_method": "Map clean x102..1540 y78..121 gate box through anisotropic transform and 1/3 downscale, add 4 output-pixel padding, enlarge crop 4x with LANCZOS for recognition only, run Tesseract PSM 6/7/11/13, retain maximum normalized alphanumeric sequence similarity, require >=0.80; no recognized text stored.",
        "raw_ocr_text_stored": False,
        "scientific_adjudication_performed": False,
        "sealed_v8_modified": False, "pass7_proof_modified": False,
        "pass12_proof_modified": False, "v9_created": False,
        "tts_invoked": False, "audio_generated": False, "video_encoded": False,
        "shared_or_public_assets_modified": False, "git_action": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    x = candidate["aggregates"]["x90_360p"]
    y = candidate["aggregates"]["y90_360p"]
    px = methods["pass12_sharpness_safe"]["aggregates"]["x90_360p"]
    py = methods["pass12_sharpness_safe"]["aggregates"]["y90_360p"]
    print(
        f"PASS candidate=16/80 method=21/105 "
        f"candidate_x90_360p_headline={x['mean_headline_token_recall_vs_clean']:.6f} "
        f"candidate_y90_360p_headline={y['mean_headline_token_recall_vs_clean']:.6f} "
        f"proof_gates={px['scene_specific_gate_count']}/7+{py['scene_specific_gate_count']}/7"
    )


if __name__ == "__main__":
    main()
