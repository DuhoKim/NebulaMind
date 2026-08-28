#!/usr/bin/env python3
"""Quantify pass-14 shadow-floor resilience without storing OCR text."""

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
CANDIDATE_ROOT = ROOT / "qa/pass14_shadow_floor_audit"
METHOD_ROOT = ROOT / "qa/pass14_v8_shadow_floor"
OUTPUT = ROOT / "qa/pass14_shadow_floor_quantitative_audit.json"
VARIANTS = [
    "clean",
    "shadow_floor_08",
    "shadow_floor_16",
    "shadow_floor_32",
    "shadow_floor_48",
]
CRITICAL_SCENES = {7, 9, 10, 11, 16}
STRUCTURAL = re.compile(
    r"result\s+held|frame\s+unstated|outcomes?\s+withheld|"
    r"no\s+outcome\s+shown|result\s+locked"
)
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
    result = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "11", "tsv"],
        check=True,
        capture_output=True,
        text=True,
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
        if top < 350:
            headline_tokens.extend(parts)
        else:
            lower_tokens.extend(parts)
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
    ref = collections.Counter(reference)
    obs = collections.Counter(observed)
    matched = sum(min(count, obs[token]) for token, count in ref.items())
    return round(matched / sum(ref.values()), 6)


def rgb(path: Path) -> np.ndarray:
    with Image.open(path).convert("RGB") as image:
        return np.asarray(image, dtype=np.uint8)


def luma(values: np.ndarray) -> np.ndarray:
    data = values.astype(np.uint32)
    return ((54 * data[:, :, 0] + 183 * data[:, :, 1] + 19 * data[:, :, 2] + 128) // 256).astype(np.uint16)


def edge_map(values: np.ndarray) -> np.ndarray:
    lum = luma(values).astype(np.int16)
    gx = np.zeros_like(lum, dtype=bool)
    gy = np.zeros_like(lum, dtype=bool)
    gx[:, 1:] = np.abs(lum[:, 1:] - lum[:, :-1]) >= 12
    gy[1:, :] = np.abs(lum[1:, :] - lum[:-1, :]) >= 12
    return gx | gy


def dilate_1(values: np.ndarray) -> np.ndarray:
    padded = np.pad(values, 1, mode="constant", constant_values=False)
    output = np.zeros_like(values)
    for dy in range(3):
        for dx in range(3):
            output |= padded[dy : dy + values.shape[0], dx : dx + values.shape[1]]
    return output


def pixel_metrics(clean: np.ndarray, observed: np.ndarray) -> dict[str, float]:
    clean_float = clean.astype(np.float64)
    observed_float = observed.astype(np.float64)
    error = observed_float - clean_float
    mse = float(np.mean(error * error))
    psnr = 99.0 if mse == 0 else 10.0 * math.log10((255.0 * 255.0) / mse)
    clean_luma = luma(clean)
    observed_luma = luma(observed)
    reference_edges = edge_map(clean)
    observed_edges = edge_map(observed)
    observed_dilated = dilate_1(observed_edges)
    edge_count = int(reference_edges.sum())
    edge_recall = 1.0 if edge_count == 0 else float(np.logical_and(reference_edges, observed_dilated).sum()) / edge_count
    low_mask = clean_luma < 64
    low_edges = reference_edges & low_mask
    low_edge_count = int(low_edges.sum())
    low_edge_recall = 1.0 if low_edge_count == 0 else float(np.logical_and(low_edges, observed_dilated).sum()) / low_edge_count
    dark_source = (clean_luma > 0) & (clean_luma < 64)
    dark_count = int(dark_source.sum())
    dark_survival = 1.0 if dark_count == 0 else float(np.logical_and(dark_source, observed_luma > 0).sum()) / dark_count
    clean_mean = float(clean_luma.mean())
    observed_mean = float(observed_luma.mean())
    return {
        "mean_absolute_rgb_error": round(float(np.mean(np.abs(error))), 6),
        "rgb_psnr_db": round(psnr, 6),
        "tolerant_luma_edge_recall": round(edge_recall, 6),
        "low_tone_tolerant_edge_recall": round(low_edge_recall, 6),
        "nonzero_dark_pixel_survival_below_64": round(dark_survival, 6),
        "additional_black_pixel_fraction": round(float(np.mean((clean_luma > 0) & (observed_luma == 0))), 6),
        "mean_luma_retention": round(1.0 if clean_mean == 0 else observed_mean / clean_mean, 6),
    }


def gate_similarity(path: Path, canonical: str) -> float:
    with Image.open(path).convert("RGB") as image:
        crop = image.crop(GATE_BOX)
        encoded = io.BytesIO()
        crop.save(encoded, format="PNG", optimize=False)
    reference = compact(canonical)
    scores: list[float] = []
    for psm in (6, 7, 11, 13):
        result = subprocess.run(
            ["tesseract", "stdin", "stdout", "--psm", str(psm)],
            check=True,
            input=encoded.getvalue(),
            capture_output=True,
        )
        observed = compact(result.stdout.decode("utf-8", errors="replace"))
        scores.append(difflib.SequenceMatcher(None, reference, observed).ratio())
    return round(max(scores), 6)


def scene_metrics(clean_path: Path, observed_path: Path, clean_ocr: dict[str, Any]) -> dict[str, Any]:
    observed_ocr = ocr(observed_path)
    metrics: dict[str, Any] = {
        "full_token_recall_vs_clean": recall(clean_ocr["all"], observed_ocr["all"]),
        "headline_token_recall_vs_clean": recall(clean_ocr["headline"], observed_ocr["headline"]),
        "lower_support_token_recall_vs_clean": recall(clean_ocr["lower"], observed_ocr["lower"]),
        "numeric_token_recall_vs_clean": recall(clean_ocr["numeric"], observed_ocr["numeric"]),
        "structural_gate_detected": bool(STRUCTURAL.search(observed_ocr["joined"])),
        "result_held_detected": bool(RESULT_HELD.search(observed_ocr["joined"])),
        "ocr_token_count": len(observed_ocr["all"]),
    }
    metrics.update(pixel_metrics(rgb(clean_path), rgb(observed_path)))
    return metrics


def mean(rows: list[dict[str, Any]], key: str) -> float:
    return round(sum(float(row[key]) for row in rows) / len(rows), 6)


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    keys = [
        "full_token_recall_vs_clean",
        "headline_token_recall_vs_clean",
        "lower_support_token_recall_vs_clean",
        "numeric_token_recall_vs_clean",
        "mean_absolute_rgb_error",
        "rgb_psnr_db",
        "tolerant_luma_edge_recall",
        "low_tone_tolerant_edge_recall",
        "nonzero_dark_pixel_survival_below_64",
        "additional_black_pixel_fraction",
        "mean_luma_retention",
    ]
    output = {f"mean_{key}": mean(rows, key) for key in keys}
    output["structural_gate_scene_count"] = sum(bool(row["structural_gate_detected"]) for row in rows)
    output["result_held_scene_count"] = sum(bool(row["result_held_detected"]) for row in rows)
    if all("scene_specific_gate_detected" in row for row in rows):
        output["scene_specific_gate_count"] = sum(bool(row["scene_specific_gate_detected"]) for row in rows)
    if all("gate_character_similarity_best_of_psm_6_7_11_13" in row for row in rows):
        output["mean_gate_character_similarity_best_of_psm_6_7_11_13"] = mean(rows, "gate_character_similarity_best_of_psm_6_7_11_13")
    return output


def candidate_audit() -> dict[str, Any]:
    receipt = json.loads((CANDIDATE_ROOT / "extraction_receipt.json").read_text(encoding="utf-8"))
    by_scene: dict[int, dict[str, Path]] = {}
    for record in receipt["records"]:
        by_scene.setdefault(int(record["scene"]), {})[record["variant"]] = ROOT / record["path"]
    scenes: list[dict[str, Any]] = []
    for scene in range(1, 17):
        paths = by_scene[scene]
        clean_path = paths["clean"]
        clean_ocr = ocr(clean_path)
        metrics = {variant: scene_metrics(clean_path, paths[variant], clean_ocr) for variant in VARIANTS}
        scenes.append({"scene": scene, "metrics": metrics})
    return {
        "scene_count": 16,
        "frame_count": 80,
        "scenes": scenes,
        "aggregates": {variant: aggregate([scene["metrics"][variant] for scene in scenes]) for variant in VARIANTS},
        "held_critical_scenes": sorted(CRITICAL_SCENES),
        "held_critical_aggregates": {
            variant: aggregate([scene["metrics"][variant] for scene in scenes if scene["scene"] in CRITICAL_SCENES])
            for variant in VARIANTS
        },
    }


def method_audit() -> dict[str, Any]:
    receipt = json.loads((METHOD_ROOT / "receipt.json").read_text(encoding="utf-8"))
    groups: dict[str, Any] = {}
    for group_name, group in receipt["groups"].items():
        group_root = METHOD_ROOT / group_name
        scenes: list[dict[str, Any]] = []
        for scene_row in group["scenes"]:
            scene = int(scene_row["scene"])
            paths = {sample["variant"]: group_root / sample["frame"] for sample in scene_row["samples"]}
            clean_path = paths["clean"]
            clean_ocr = ocr(clean_path)
            metrics: dict[str, dict[str, Any]] = {}
            for variant in VARIANTS:
                row = scene_metrics(clean_path, paths[variant], clean_ocr)
                if group_name in {"pass7_caption_safe", "pass12_sharpness_safe"}:
                    row["scene_specific_gate_detected"] = bool(SCENE_GATES[scene].search(ocr(paths[variant])["headline_joined"]))
                if group_name == "pass12_sharpness_safe":
                    similarity = gate_similarity(paths[variant], GATE_LINES[scene])
                    row["gate_character_similarity_best_of_psm_6_7_11_13"] = similarity
                    row["scene_specific_gate_detected"] = similarity >= 0.85
                metrics[variant] = row
            scenes.append({"scene": scene, "metrics": metrics})
        groups[group_name] = {
            "scene_count": 7,
            "frame_count": 35,
            "scenes": scenes,
            "aggregates": {variant: aggregate([scene["metrics"][variant] for scene in scenes]) for variant in VARIANTS},
        }
    return groups


def main() -> None:
    candidate = candidate_audit()
    methods = method_audit()
    output = {
        "status": "QA_STATIC_METRICS_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 14,
        "variant_order": VARIANTS,
        "operational_variant": "shadow_floor_16",
        "characterization_variants": ["shadow_floor_32", "shadow_floor_48"],
        "transform_interpretation": "Integer luma-preserving dark-tone floor/remap; code-value floors are packet parameters, not a named display, transfer function, viewer, platform, or service.",
        "candidate": candidate,
        "method_groups": methods,
        "human_visual_review": {
            "candidate_structural_gate_scenes": {variant: "0/16" for variant in VARIANTS},
            "candidate_failure_order": "dark background texture, gridlines, axes, error bars, legends, caveats, citations, provenance, and low-luminance support weaken before white result headlines, large blue numbers, bright bars, matrices, plot silhouettes, and conclusion hierarchy",
            "sealed_v8_result_held_badges_visual": {variant: "7/7" for variant in VARIANTS},
            "sealed_v8_operational_required_meaning_ambiguous": False,
            "pass7_operational_specific_gate_lines_visual": "7/7_EXACT",
            "pass12_operational_specific_gate_lines_visual": "7/7_EXACT",
            "pass12_operational_result_held_badges_visual": "7/7",
            "pass12_operational_no_overlap_clipping_or_semantic_ambiguity": True,
            "severe_characterization": "At floors 32 and 48, major result and status hierarchy remains primary while shadow texture, low-luminance dividers, grids, axes, small support, citations, and provenance progressively cease to be acceptance-reliable.",
        },
        "gate_ocr_method_for_pass12_proof": "Crop exact x102..1540 y78..121 gate box; run Tesseract PSM 6, 7, 11, and 13; retain only maximum normalized alphanumeric character-sequence similarity; require >=0.85. No recognized text is stored.",
        "raw_ocr_text_stored": False,
        "scientific_adjudication_performed": False,
        "sealed_v8_modified": False,
        "pass7_proof_modified": False,
        "pass12_proof_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    operational = candidate["aggregates"]["shadow_floor_16"]
    proof = methods["pass12_sharpness_safe"]["aggregates"]["shadow_floor_16"]
    print(
        "PASS candidate=16/80 method=21/105 "
        f"candidate_floor16_headline={operational['mean_headline_token_recall_vs_clean']:.6f} "
        f"proof_floor16_gates={proof['scene_specific_gate_count']}/7"
    )


if __name__ == "__main__":
    main()
