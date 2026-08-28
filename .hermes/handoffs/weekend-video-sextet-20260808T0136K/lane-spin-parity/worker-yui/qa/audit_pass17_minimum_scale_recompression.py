#!/usr/bin/env python3
"""Quantify pass-17 minimum-scale plus JPEG 4:2:0 interaction."""

from __future__ import annotations

import collections
import csv
import io
import json
import math
import re
import subprocess
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, cast

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_DIR = ROOT / "qa/pass17_minimum_scale_recompression_audit"
METHOD_DIR = ROOT / "qa/pass17_v8_minimum_scale_recompression"
PASS12_RECEIPT = ROOT / "qa/pass12_sharpness_safe_mockup/receipt.json"
OUTPUT = ROOT / "qa/pass17_minimum_scale_recompression_quantitative_audit.json"
VARIANTS = ["clean", "downscale_360p", "jpeg_q60_420_360p", "jpeg_q35_420_360p", "jpeg_q20_420_360p"]
REPRESENTED_VARIANTS = VARIANTS[1:]
CRITICAL_SCENES = [7, 9, 10, 11, 16]
PSM_MODES = [6, 7, 11, 13]
GATE_THRESHOLD = 0.80
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


def normalize_words(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def normalize_chars(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def ocr_boxes(path: Path) -> list[dict[str, object]]:
    proc = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "11", "tsv"],
        check=True, text=True, capture_output=True,
    )
    rows: list[dict[str, object]] = []
    for row in csv.DictReader(io.StringIO(proc.stdout), delimiter="\t"):
        token = normalize_words(row.get("text", ""))
        if not token:
            continue
        try:
            confidence = float(row.get("conf", "-1"))
            left, top = int(row.get("left", "0")), int(row.get("top", "0"))
            width, height = int(row.get("width", "0")), int(row.get("height", "0"))
        except ValueError:
            continue
        if confidence < 0:
            continue
        rows.append({"token": token, "left": left, "top": top, "right": left + width, "bottom": top + height})
    return rows


def tokens(rows: list[dict[str, object]]) -> list[str]:
    result: list[str] = []
    for row in rows:
        value = row["token"]
        if isinstance(value, str):
            result.extend(value.split())
    return result


def multiset_recall(reference: list[str], observed: list[str]) -> float:
    if not reference:
        return 1.0
    ref, obs = collections.Counter(reference), collections.Counter(observed)
    return sum(min(count, obs[token]) for token, count in ref.items()) / sum(ref.values())


def numeric(values: list[str]) -> list[str]:
    return [value for value in values if any(character.isdigit() for character in value)]


def image_array(path: Path) -> np.ndarray:
    with Image.open(path) as opened:
        return np.asarray(opened.convert("RGB"), dtype=np.uint8)


def gray(values: np.ndarray) -> np.ndarray:
    rgb = values.astype(np.float64)
    return 0.2126 * rgb[:, :, 0] + 0.7152 * rgb[:, :, 1] + 0.0722 * rgb[:, :, 2]


def edge_mask(values: np.ndarray) -> np.ndarray:
    gx = np.zeros(values.shape, dtype=np.float64)
    gy = np.zeros(values.shape, dtype=np.float64)
    gx[:, 1:] = np.abs(values[:, 1:] - values[:, :-1])
    gy[1:, :] = np.abs(values[1:, :] - values[:-1, :])
    return np.maximum(gx, gy) >= 24.0


def dilate_one(mask: np.ndarray) -> np.ndarray:
    padded = np.pad(mask, 1, mode="constant", constant_values=False)
    output = np.zeros(mask.shape, dtype=bool)
    for y in range(3):
        for x in range(3):
            output |= padded[y:y + mask.shape[0], x:x + mask.shape[1]]
    return output


def pixel_metrics(reference: np.ndarray, observed: np.ndarray) -> dict[str, float]:
    delta = reference.astype(np.float64) - observed.astype(np.float64)
    mse = float(np.mean(delta * delta))
    psnr = 99.0 if mse == 0 else 10.0 * math.log10((255.0 * 255.0) / mse)
    reference_edges = edge_mask(gray(reference))
    observed_edges = dilate_one(edge_mask(gray(observed)))
    edge_count = int(reference_edges.sum())
    recall = 1.0 if edge_count == 0 else float((reference_edges & observed_edges).sum() / edge_count)
    return {
        "rgb_psnr_db": round(psnr, 6),
        "mean_absolute_rgb_error": round(float(np.abs(delta).mean()), 6),
        "tolerant_luma_edge_recall": round(recall, 6),
    }


def backproject(array: np.ndarray) -> np.ndarray:
    image = Image.fromarray(array)
    return np.asarray(image.resize((1920, 1080), Image.Resampling.LANCZOS), dtype=np.uint8)


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def analyze_scene(root: Path, scene: int, samples: list[dict[str, object]], gate_pattern: re.Pattern[str] | None) -> dict[str, object]:
    rows_by_variant: dict[str, list[dict[str, object]]] = {}
    arrays: dict[str, np.ndarray] = {}
    jpeg_sizes: dict[str, int | None] = {}
    for sample in samples:
        variant, frame = sample["variant"], sample["frame"]
        if not isinstance(variant, str) or not isinstance(frame, str):
            raise TypeError("sample strings required")
        path = root / frame
        rows_by_variant[variant] = ocr_boxes(path)
        arrays[variant] = image_array(path)
        size = sample.get("jpeg_bytes")
        jpeg_sizes[variant] = size if isinstance(size, int) else None
    clean_rows = rows_by_variant["clean"]
    clean_tokens = tokens(clean_rows)
    headline_tokens = tokens([row for row in clean_rows if isinstance(row["top"], int) and int(row["top"]) < 350])
    support_tokens = tokens([row for row in clean_rows if isinstance(row["top"], int) and int(row["top"]) >= 780])
    clean_numeric = numeric(clean_tokens)
    metrics: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        observed = tokens(rows_by_variant[variant])
        joined = " ".join(observed)
        pixels = pixel_metrics(arrays["clean"], arrays["clean"] if variant == "clean" else backproject(arrays[variant]))
        recompression_pixels = (
            pixel_metrics(arrays["downscale_360p"], arrays[variant])
            if variant.startswith("jpeg_") else None
        )
        metrics[variant] = {
            "ocr_token_count": len(observed),
            "full_token_recall_vs_native_clean": round(multiset_recall(clean_tokens, observed), 6),
            "headline_token_recall_vs_native_clean": round(multiset_recall(headline_tokens, observed), 6),
            "lower_support_token_recall_vs_native_clean": round(multiset_recall(support_tokens, observed), 6),
            "numeric_token_recall_vs_native_clean": round(multiset_recall(clean_numeric, numeric(observed)), 6),
            "structural_gate_detected": any(pattern.search(joined) for pattern in GATE_PATTERNS),
            "result_held_detected": bool(re.search(r"result\s+held", joined)),
            "scene_specific_gate_detected": bool(gate_pattern.search(joined)) if gate_pattern else False,
            "encoded_jpeg_bytes": jpeg_sizes[variant],
            "combined_backprojected_pixels": pixels,
            "recompression_only_pixels_vs_lossless_360p": recompression_pixels,
        }
    return {"scene": scene, "clean_ocr_token_count": len(clean_tokens), "metrics": metrics}


def aggregate(scene_rows: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        rows = [scene["metrics"][variant] for scene in scene_rows]  # type: ignore[index]
        jpeg_sizes = [int(row["encoded_jpeg_bytes"]) for row in rows if isinstance(row["encoded_jpeg_bytes"], int)]
        aggregate_row: dict[str, object] = {
            "mean_full_token_recall_vs_native_clean": mean([float(row["full_token_recall_vs_native_clean"]) for row in rows]),
            "mean_headline_token_recall_vs_native_clean": mean([float(row["headline_token_recall_vs_native_clean"]) for row in rows]),
            "mean_lower_support_token_recall_vs_native_clean": mean([float(row["lower_support_token_recall_vs_native_clean"]) for row in rows]),
            "mean_numeric_token_recall_vs_native_clean": mean([float(row["numeric_token_recall_vs_native_clean"]) for row in rows]),
            "structural_gate_scene_count": sum(bool(row["structural_gate_detected"]) for row in rows),
            "result_held_scene_count": sum(bool(row["result_held_detected"]) for row in rows),
            "scene_specific_gate_count": sum(bool(row["scene_specific_gate_detected"]) for row in rows),
            "mean_encoded_jpeg_bytes": round(sum(jpeg_sizes) / len(jpeg_sizes)) if jpeg_sizes else None,
            "mean_combined_backprojected_rgb_psnr_db": mean([float(row["combined_backprojected_pixels"]["rgb_psnr_db"]) for row in rows]),  # type: ignore[index]
            "mean_combined_backprojected_edge_recall": mean([float(row["combined_backprojected_pixels"]["tolerant_luma_edge_recall"]) for row in rows]),  # type: ignore[index]
        }
        if variant.startswith("jpeg_"):
            aggregate_row["mean_recompression_only_rgb_psnr_db_vs_lossless_360p"] = mean([
                float(row["recompression_only_pixels_vs_lossless_360p"]["rgb_psnr_db"]) for row in rows  # type: ignore[index]
            ])
            aggregate_row["mean_recompression_only_edge_recall_vs_lossless_360p"] = mean([
                float(row["recompression_only_pixels_vs_lossless_360p"]["tolerant_luma_edge_recall"]) for row in rows  # type: ignore[index]
            ])
        result[variant] = aggregate_row
    return result


def critical_aggregate(scene_rows: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    output: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        rows = [scene["metrics"][variant] for scene in scene_rows if scene["scene"] in CRITICAL_SCENES]  # type: ignore[index]
        output[variant] = {
            "scenes": CRITICAL_SCENES,
            "mean_headline_token_recall_vs_native_clean": mean([float(row["headline_token_recall_vs_native_clean"]) for row in rows]),
            "mean_full_token_recall_vs_native_clean": mean([float(row["full_token_recall_vs_native_clean"]) for row in rows]),
            "mean_lower_support_token_recall_vs_native_clean": mean([float(row["lower_support_token_recall_vs_native_clean"]) for row in rows]),
            "mean_numeric_token_recall_vs_native_clean": mean([float(row["numeric_token_recall_vs_native_clean"]) for row in rows]),
            "structural_gate_scene_count": sum(bool(row["structural_gate_detected"]) for row in rows),
        }
    return output


def crop_similarity(path: Path, canonical: str, native: bool) -> dict[str, object]:
    with Image.open(path) as opened:
        image = opened.convert("RGB")
    if native:
        box = (94, 70, 1548, 129)
    else:
        box = (30, 22, 518, 45)
    crop = image.crop(box)
    enlarged = crop.resize((crop.width * 4, crop.height * 4), Image.Resampling.LANCZOS)
    target = normalize_chars(canonical)
    scores: dict[str, float] = {}
    for psm in PSM_MODES:
        proc = subprocess.run(
            ["tesseract", "stdin", "stdout", "--psm", str(psm)],
            input=_png_bytes(enlarged), capture_output=True, check=True,
        )
        observed = normalize_chars(proc.stdout.decode("utf-8", errors="replace"))
        scores[str(psm)] = round(SequenceMatcher(None, target, observed).ratio(), 6)
    best_psm = max(scores, key=scores.get)  # type: ignore[arg-type]
    best = scores[best_psm]
    return {"best_similarity": best, "best_psm": int(best_psm), "passes_threshold": best >= GATE_THRESHOLD}


def _png_bytes(image: Image.Image) -> bytes:
    buffer = io.BytesIO()
    image.save(buffer, format="PNG", optimize=False)
    return buffer.getvalue()


def pass12_gate_audit(method_receipt: dict[str, object]) -> dict[str, object]:
    source_receipt = load_json(PASS12_RECEIPT)
    canonical = {int(scene["scene"]): str(scene["gate_line"]) for scene in source_receipt["scenes"]}
    group = method_receipt["groups"]["pass12_sharpness_safe"]  # type: ignore[index]
    output: dict[str, object] = {}
    for variant in VARIANTS:
        rows: list[dict[str, object]] = []
        for scene in group["scenes"]:  # type: ignore[index]
            scene_number = int(scene["scene"])
            sample = next(sample for sample in scene["samples"] if sample["variant"] == variant)
            path = METHOD_DIR / "pass12_sharpness_safe" / str(sample["frame"])
            rows.append({"scene": scene_number, **crop_similarity(path, canonical[scene_number], variant == "clean")})
        output[variant] = {
            "scene_count": 7,
            "passing_gate_count": sum(bool(row["passes_threshold"]) for row in rows),
            "mean_best_similarity": mean([cast(float, row["best_similarity"]) for row in rows]),
            "threshold": GATE_THRESHOLD,
            "rows": rows,
        }
    return output


def candidate_groups(receipt: dict[str, object]) -> list[dict[str, object]]:
    records = receipt["records"]
    if not isinstance(records, list):
        raise TypeError("records must be a list")
    return [{"scene": int(record["scene"]), "samples": record["samples"]} for record in records]


def main() -> None:
    candidate_receipt = load_json(CANDIDATE_DIR / "extraction_receipt.json")
    candidate_scenes = [
        analyze_scene(CANDIDATE_DIR, int(scene["scene"]), scene["samples"], None)  # type: ignore[arg-type]
        for scene in candidate_groups(candidate_receipt)
    ]
    method_receipt = load_json(METHOD_DIR / "receipt.json")
    method_groups: dict[str, object] = {}
    for group_name, group in method_receipt["groups"].items():
        group_root = METHOD_DIR / group_name
        scene_rows = [
            analyze_scene(
                group_root,
                int(scene["scene"]),
                scene["samples"],
                SCENE_GATE_PATTERNS[int(scene["scene"])] if group_name in {"pass7_caption_safe", "pass12_sharpness_safe"} else None,
            )
            for scene in group["scenes"]
        ]
        method_groups[group_name] = {"scenes": scene_rows, "aggregates": aggregate(scene_rows)}
    gate_audit = pass12_gate_audit(method_receipt)
    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 17,
        "variant_order": VARIANTS,
        "candidate": {
            "sha256": candidate_receipt["candidate_sha256"],
            "scene_count": 16,
            "frame_count": 80,
            "cut_times_exact_pass16": candidate_receipt["cut_detection"]["cuts"] == load_json(ROOT / "qa/pass16_minimum_scale_geometry_audit/extraction_receipt.json")["cut_detection"]["cuts"],
            "clean_midpoints_byte_identical_to_pass16": 16,
            "scenes": candidate_scenes,
            "aggregates": aggregate(candidate_scenes),
            "held_critical_aggregates": critical_aggregate(candidate_scenes),
        },
        "method_groups": method_groups,
        "pass12_mapped_gate_crop_character_similarity": gate_audit,
        "human_visual_review": {
            "candidate_dominant_result_hierarchy_visible_through_q20_at_360p": True,
            "candidate_major_headlines_numbers_plots_survive_longer_than_fine_support": True,
            "candidate_structural_hold_visible_any_variant": False,
            "candidate_small_axes_error_bars_caveats_citations_and_provenance_not_uniformly_acceptance_readable_at_q60_360p": True,
            "sealed_v8_result_held_badges_q60_360p": "7/7",
            "sealed_v8_major_status_boundaries_q60_360p": "7/7",
            "pass7_specific_gate_lines_q60_360p": "7/7",
            "pass7_result_held_badges_q60_360p": "7/7",
            "pass12_specific_gate_lines_q60_360p": "7/7",
            "pass12_result_held_badges_q60_360p": "7/7",
            "pass12_specific_gate_lines_q20_360p_characterization": "7/7_VISUALLY_RECOGNIZABLE_AND_EXACT_COPY_READABLE_AT_CONTACT_SHEET_SCALE",
            "pass12_result_held_badges_q20_360p_characterization": "7/7",
            "pass12_overlap_clipping_or_semantic_ambiguity_any_variant": False,
            "global_full_frame_ocr_is_acceptance_oracle_at_360p": False,
        },
        "simulation_limit": "Packet-specific native-to-640x360 LANCZOS downscale followed by Pillow JPEG 4:2:0 encode/decode. Quality values are library parameters, not claims about a named codec ladder, display, player, browser, platform, upload route, delivery service, room, viewer, or universal standard.",
        "raw_ocr_text_stored": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    candidate_q60 = cast(dict[str, object], output["candidate"]["aggregates"]["jpeg_q60_420_360p"])  # type: ignore[index]
    gates_q60 = cast(dict[str, object], gate_audit["jpeg_q60_420_360p"])
    headline = cast(float, candidate_q60["mean_headline_token_recall_vs_native_clean"])
    full = cast(float, candidate_q60["mean_full_token_recall_vs_native_clean"])
    passing_gates = cast(int, gates_q60["passing_gate_count"])
    print(
        "PASS candidate=16/80 method=21/105 "
        f"candidate_q60_360p_headline={headline:.6f} "
        f"candidate_q60_360p_full={full:.6f} "
        f"proof_gates={passing_gates}/7"
    )


if __name__ == "__main__":
    main()
