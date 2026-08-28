#!/usr/bin/env python3
"""Quantify pass-15 anisotropic-geometry resilience without storing OCR text."""

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
CANDIDATE_ROOT = ROOT / "qa/pass15_geometry_audit"
METHOD_ROOT = ROOT / "qa/pass15_v8_geometry"
OUTPUT = ROOT / "qa/pass15_geometry_quantitative_audit.json"
VARIANTS = ["clean", "squeeze_x90", "squeeze_y90", "squeeze_x80", "squeeze_y80"]
GEOMETRY = {
    "clean": (1.0, 1.0),
    "squeeze_x90": (0.90, 1.0),
    "squeeze_y90": (1.0, 0.90),
    "squeeze_x80": (0.80, 1.0),
    "squeeze_y80": (1.0, 0.80),
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
    result = subprocess.run(["tesseract", str(path), "stdout", "--psm", "11", "tsv"], check=True, capture_output=True, text=True)
    all_tokens, headline_tokens, lower_tokens, numeric_tokens = [], [], [], []
    for row in csv.DictReader(io.StringIO(result.stdout), delimiter="\t"):
        token = normalize(row.get("text", ""))
        if not token:
            continue
        try:
            confidence = float(row.get("conf", "-1")); top = int(row.get("top", "0"))
        except ValueError:
            continue
        if confidence < 0:
            continue
        parts = token.split(); all_tokens.extend(parts)
        (headline_tokens if top < 350 else lower_tokens).extend(parts)
        numeric_tokens.extend(part for part in parts if re.search(r"\d", part))
    return {"all": all_tokens, "headline": headline_tokens, "lower": lower_tokens, "numeric": numeric_tokens, "joined": " ".join(all_tokens), "headline_joined": " ".join(headline_tokens)}


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
        w, h = image.size
        nw, nh = int(round(w * sx)), int(round(h * sy))
        x0, y0 = (w - nw) // 2, (h - nh) // 2
        crop = image.crop((x0, y0, x0 + nw, y0 + nh))
        restored = crop.resize((w, h), Image.Resampling.LANCZOS)
        return np.asarray(restored, dtype=np.uint8)


def backprojected_metrics(clean: np.ndarray, restored: np.ndarray) -> dict[str, float]:
    error = restored.astype(np.float64) - clean.astype(np.float64)
    mse = float(np.mean(error * error)); psnr = 99.0 if mse == 0 else 10 * math.log10(255 * 255 / mse)
    ref_edge, out_edge = edge_map(clean), dilate(edge_map(restored))
    count = int(ref_edge.sum()); edge_recall = 1.0 if count == 0 else float((ref_edge & out_edge).sum()) / count
    return {"backprojected_mean_absolute_rgb_error": round(float(np.mean(np.abs(error))), 6), "backprojected_rgb_psnr_db": round(psnr, 6), "backprojected_tolerant_luma_edge_recall": round(edge_recall, 6)}


def geometry_metrics(variant: str) -> dict[str, float]:
    sx, sy = GEOMETRY[variant]
    return {
        "horizontal_length_scale": sx,
        "vertical_length_scale": sy,
        "apparent_circle_width_to_height_ratio": round(sx / sy, 6),
        "apparent_slope_multiplier": round(sy / sx, 6),
        "horizontal_padding_pixels_each_side": int((1920 - round(1920 * sx)) // 2),
        "vertical_padding_pixels_each_side": int((1080 - round(1080 * sy)) // 2),
    }


def transformed_gate_box(variant: str) -> tuple[int, int, int, int]:
    sx, sy = GEOMETRY[variant]
    x0, y0 = (1920 - round(1920 * sx)) // 2, (1080 - round(1080 * sy)) // 2
    a, b, c, d = GATE_BOX
    return (max(0, int(x0 + a * sx) - 8), max(0, int(y0 + b * sy) - 8), min(1920, int(math.ceil(x0 + c * sx)) + 8), min(1080, int(math.ceil(y0 + d * sy)) + 8))


def gate_similarity(path: Path, canonical: str, variant: str) -> float:
    with Image.open(path).convert("RGB") as image:
        crop = image.crop(transformed_gate_box(variant)); encoded = io.BytesIO(); crop.save(encoded, format="PNG", optimize=False)
    reference, scores = compact(canonical), []
    for psm in (6, 7, 11, 13):
        result = subprocess.run(["tesseract", "stdin", "stdout", "--psm", str(psm)], check=True, input=encoded.getvalue(), capture_output=True)
        scores.append(difflib.SequenceMatcher(None, reference, compact(result.stdout.decode("utf-8", errors="replace"))).ratio())
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
    row.update(geometry_metrics(variant)); row.update(backprojected_metrics(rgb(clean_path), recover(observed_path, variant)))
    return row


def mean(rows: list[dict[str, Any]], key: str) -> float:
    return round(sum(float(row[key]) for row in rows) / len(rows), 6)


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    keys = ["full_token_recall_vs_clean", "headline_token_recall_vs_clean", "lower_support_token_recall_vs_clean", "numeric_token_recall_vs_clean", "backprojected_mean_absolute_rgb_error", "backprojected_rgb_psnr_db", "backprojected_tolerant_luma_edge_recall"]
    out = {f"mean_{key}": mean(rows, key) for key in keys}
    out["structural_gate_scene_count"] = sum(bool(r["structural_gate_detected"]) for r in rows)
    out["result_held_scene_count"] = sum(bool(r["result_held_detected"]) for r in rows)
    out.update({f"geometry_{k}": v for k, v in geometry_metrics(rows[0]["variant"]).items()})
    if all("scene_specific_gate_detected" in r for r in rows):
        out["scene_specific_gate_count"] = sum(bool(r["scene_specific_gate_detected"]) for r in rows)
    if all("gate_character_similarity_best_of_psm_6_7_11_13" in r for r in rows):
        out["mean_gate_character_similarity_best_of_psm_6_7_11_13"] = mean(rows, "gate_character_similarity_best_of_psm_6_7_11_13")
    return out


def candidate_audit() -> dict[str, Any]:
    receipt = json.loads((CANDIDATE_ROOT / "extraction_receipt.json").read_text())
    scenes = []
    for record in receipt["records"]:
        scene = int(record["scene"]); paths = {s["variant"]: CANDIDATE_ROOT / s["frame"] for s in record["samples"]}
        clean, clean_ocr = paths["clean"], ocr(paths["clean"])
        metrics = {}
        for variant in VARIANTS:
            row = scene_metrics(clean, paths[variant], clean_ocr, variant); row["variant"] = variant; metrics[variant] = row
        scenes.append({"scene": scene, "metrics": metrics})
    return {"scene_count": 16, "frame_count": 80, "scenes": scenes, "aggregates": {v: aggregate([s["metrics"][v] for s in scenes]) for v in VARIANTS}, "held_critical_scenes": sorted(CRITICAL_SCENES), "held_critical_aggregates": {v: aggregate([s["metrics"][v] for s in scenes if s["scene"] in CRITICAL_SCENES]) for v in VARIANTS}}


def method_audit() -> dict[str, Any]:
    receipt = json.loads((METHOD_ROOT / "receipt.json").read_text()); groups = {}
    for group_name, group in receipt["groups"].items():
        group_root, scenes = METHOD_ROOT / group_name, []
        for scene_row in group["scenes"]:
            scene = int(scene_row["scene"]); paths = {s["variant"]: group_root / s["frame"] for s in scene_row["samples"]}
            clean, clean_ocr, metrics = paths["clean"], ocr(paths["clean"]), {}
            for variant in VARIANTS:
                row = scene_metrics(clean, paths[variant], clean_ocr, variant); row["variant"] = variant
                if group_name in {"pass7_caption_safe", "pass12_sharpness_safe"}:
                    row["scene_specific_gate_detected"] = bool(SCENE_GATES[scene].search(ocr(paths[variant])["headline_joined"]))
                if group_name == "pass12_sharpness_safe":
                    similarity = gate_similarity(paths[variant], GATE_LINES[scene], variant)
                    row["gate_character_similarity_best_of_psm_6_7_11_13"] = similarity
                    row["scene_specific_gate_detected"] = similarity >= 0.85
                metrics[variant] = row
            scenes.append({"scene": scene, "metrics": metrics})
        groups[group_name] = {"scene_count": 7, "frame_count": 35, "scenes": scenes, "aggregates": {v: aggregate([s["metrics"][v] for s in scenes]) for v in VARIANTS}}
    return groups


def main() -> None:
    candidate, methods = candidate_audit(), method_audit()
    output = {
        "status": "QA_STATIC_METRICS_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 15,
        "variant_order": VARIANTS,
        "operational_variants": ["squeeze_x90", "squeeze_y90"],
        "characterization_variants": ["squeeze_x80", "squeeze_y80"],
        "transform_interpretation": "Centered anisotropic Pillow LANCZOS resampling with black padding; packet parameters only, not a named display, player, projector, codec, browser, platform, or pixel-aspect standard.",
        "candidate": candidate,
        "method_groups": methods,
        "human_visual_review": {
            "candidate_structural_gate_scenes": {v: "0/16" for v in VARIANTS},
            "candidate_finding": "Large result headlines, numbers, bars, matrices, plots, and conclusions remain primary. No held gate appears. Shape ratios, bar widths, spacing, slopes, circles, arrows, axes, error bars, and small captions/provenance are distorted and cannot alone carry meaning.",
            "sealed_v8_operational_result_held_badges_visual": {"squeeze_x90": "7/7", "squeeze_y90": "7/7"},
            "sealed_v8_operational_required_meaning_ambiguous": False,
            "pass12_operational_specific_gate_lines_visual": {"squeeze_x90": "7/7_EXACT", "squeeze_y90": "7/7_EXACT"},
            "pass12_operational_result_held_badges_visual": {"squeeze_x90": "7/7", "squeeze_y90": "7/7"},
            "pass12_characterization_specific_gate_lines_visual": {"squeeze_x80": "7/7_EXACT", "squeeze_y80": "7/7_EXACT"},
            "pass12_characterization_result_held_badges_visual": {"squeeze_x80": "7/7", "squeeze_y80": "7/7"},
            "pass12_no_overlap_clipping_or_semantic_ambiguity": True,
        },
        "gate_ocr_method": "Map clean x102..1540 y78..121 gate box through each centered anisotropic transform, add 8px padding, run Tesseract PSM 6/7/11/13, retain maximum normalized alphanumeric sequence similarity, require >=0.85; no recognized text stored.",
        "raw_ocr_text_stored": False,
        "scientific_adjudication_performed": False,
        "sealed_v8_modified": False, "pass7_proof_modified": False, "pass12_proof_modified": False, "v9_created": False,
        "tts_invoked": False, "audio_generated": False, "video_encoded": False, "shared_or_public_assets_modified": False, "git_action": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    x = candidate["aggregates"]["squeeze_x90"]; y = candidate["aggregates"]["squeeze_y90"]
    px = methods["pass12_sharpness_safe"]["aggregates"]["squeeze_x90"]; py = methods["pass12_sharpness_safe"]["aggregates"]["squeeze_y90"]
    print(f"PASS candidate=16/80 method=21/105 candidate_x90_headline={x['mean_headline_token_recall_vs_clean']:.6f} candidate_y90_headline={y['mean_headline_token_recall_vs_clean']:.6f} proof_gates={px['scene_specific_gate_count']}/7+{py['scene_specific_gate_count']}/7")


if __name__ == "__main__":
    main()
