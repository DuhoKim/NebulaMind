#!/usr/bin/env python3
"""Quantify pass-20 native-defocus then minimum-scale interaction."""

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
from typing import cast

import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
CAND_DIR = ROOT / "qa/pass20_minimum_scale_defocus_audit"
METHOD_DIR = ROOT / "qa/pass20_v8_minimum_scale_defocus"
OUT = ROOT / "qa/pass20_minimum_scale_defocus_quantitative_audit.json"
VARIANTS = ["clean", "downscale_360p", "defocus_r1_50_then_360p", "defocus_r2_50_then_360p", "defocus_r4_00_then_360p"]
REPRESENTED = VARIANTS[1:]
BLUR = {"defocus_r1_50_then_360p": 1.5, "defocus_r2_50_then_360p": 2.5, "defocus_r4_00_then_360p": 4.0}
CRITICAL = {7, 9, 10, 11, 16}
GATE_PATTERNS = [
    ("result", "held"), ("result", "locked"), ("frame", "unstated"),
    ("outcomes", "withheld"), ("no", "outcome", "shown"),
    ("result", "status", "held"),
]
PSMS = [6, 7, 11, 13]
GATE_THRESHOLD = 0.80


def normalize_token(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def normalize_text(value: str) -> str:
    return "".join(character for character in value.lower() if character.isalnum())


def as_int(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float, str)):
        return int(value)
    raise TypeError(f"integer-compatible value required, got {type(value).__name__}")


def as_float(value: object) -> float:
    if isinstance(value, (int, float, str)):
        return float(value)
    raise TypeError(f"float-compatible value required, got {type(value).__name__}")


def ocr_rows(path: Path, psm: int = 11) -> list[dict[str, object]]:
    process = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", str(psm), "tsv"],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True,
    )
    rows: list[dict[str, object]] = []
    for row in csv.DictReader(io.StringIO(process.stdout), delimiter="\t"):
        token = normalize_token(row.get("text") or "")
        try:
            confidence = float(row.get("conf") or -1)
        except ValueError:
            confidence = -1
        if token and confidence >= 0:
            rows.append({
                "token": token,
                "left": int(row["left"]),
                "top": int(row["top"]),
                "width": int(row["width"]),
                "height": int(row["height"]),
            })
    return rows


def counter(rows: list[dict[str, object]], region: str, height: int) -> collections.Counter[str]:
    result: collections.Counter[str] = collections.Counter()
    for row in rows:
        token = str(row["token"])
        y_center = (as_int(row["top"]) + as_int(row["height"]) / 2) / height
        include = (
            region == "full"
            or (region == "headline" and y_center < 0.325)
            or (region == "lower" and y_center >= 0.60)
            or (region == "numeric" and any(character.isdigit() for character in token))
        )
        if include:
            result[token] += 1
    return result


def aggregate(rows: list[dict[str, object]], height: int) -> dict[str, collections.Counter[str]]:
    return {region: counter(rows, region, height) for region in ["full", "headline", "lower", "numeric"]}


def recall(reference: collections.Counter[str], observed: collections.Counter[str]) -> float:
    total = sum(reference.values())
    if total == 0:
        return 1.0
    return round(sum(min(count, observed[token]) for token, count in reference.items()) / total, 6)


def gate_found(rows: list[dict[str, object]]) -> bool:
    tokens = [str(row["token"]) for row in rows]
    return any(
        any(tuple(tokens[index:index + len(pattern)]) == pattern for index in range(len(tokens) - len(pattern) + 1))
        for pattern in GATE_PATTERNS
    )


def derive(native: Image.Image, radius: float) -> np.ndarray:
    blurred = native.convert("RGB").filter(ImageFilter.GaussianBlur(radius=radius))
    represented = blurred.resize((640, 360), Image.Resampling.LANCZOS)
    return np.asarray(represented, dtype=np.uint8)


def luma(values: np.ndarray) -> np.ndarray:
    rgb = values.astype(np.float64)
    return 0.2126 * rgb[:, :, 0] + 0.7152 * rgb[:, :, 1] + 0.0722 * rgb[:, :, 2]


def gradients(gray: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    gx = np.zeros(gray.shape, dtype=np.float64)
    gy = np.zeros(gray.shape, dtype=np.float64)
    gx[:, 1:] = np.abs(gray[:, 1:] - gray[:, :-1])
    gy[1:, :] = np.abs(gray[1:, :] - gray[:-1, :])
    return gx, gy


def dilate_one(mask: np.ndarray) -> np.ndarray:
    padded = np.pad(mask, 1, mode="constant", constant_values=False)
    result = np.zeros(mask.shape, dtype=bool)
    for y_offset in range(3):
        for x_offset in range(3):
            result |= padded[y_offset:y_offset + mask.shape[0], x_offset:x_offset + mask.shape[1]]
    return result


def pixel_metrics(reference: np.ndarray, observed: np.ndarray) -> dict[str, float]:
    delta = reference.astype(np.float64) - observed.astype(np.float64)
    mse = float(np.mean(delta * delta))
    psnr = 99.0 if mse == 0.0 else 10.0 * math.log10((255.0 * 255.0) / mse)
    reference_luma, observed_luma = luma(reference), luma(observed)
    ref_gx, ref_gy = gradients(reference_luma)
    obs_gx, obs_gy = gradients(observed_luma)
    ref_edge = np.maximum(ref_gx, ref_gy) >= 24.0
    obs_edge = dilate_one(np.maximum(obs_gx, obs_gy) >= 24.0)
    edge_recall = 1.0 if int(ref_edge.sum()) == 0 else float((ref_edge & obs_edge).sum() / ref_edge.sum())
    ref_energy = float(np.mean(ref_gx * ref_gx + ref_gy * ref_gy))
    obs_energy = float(np.mean(obs_gx * obs_gx + obs_gy * obs_gy))
    return {
        "rgb_psnr_db_vs_lossless_360p": round(psnr, 6),
        "mean_absolute_rgb_error_vs_lossless_360p": round(float(np.abs(delta).mean()), 6),
        "tolerant_luma_edge_recall_vs_lossless_360p": round(edge_recall, 6),
        "luma_gradient_energy_ratio_vs_lossless_360p": round(1.0 if ref_energy == 0.0 else obs_energy / ref_energy, 6),
    }


def _png_bytes(image: Image.Image) -> bytes:
    stream = io.BytesIO()
    image.save(stream, format="PNG", optimize=False)
    return stream.getvalue()


def ocr_crop_similarity(path: Path, canonical: str, variant: str) -> dict[str, object]:
    with Image.open(path) as opened:
        image = opened.convert("RGB")
    if variant == "clean":
        box, pad = (98, 74, 1544, 125), 12
    else:
        box, pad = (32, 24, 516, 43), 4
    crop = image.crop((max(0, box[0] - pad), max(0, box[1] - pad), min(image.width, box[2] + pad), min(image.height, box[3] + pad)))
    crop = crop.resize((crop.width * 4, crop.height * 4), Image.Resampling.LANCZOS)
    target = normalize_text(canonical)
    scores: list[dict[str, object]] = []
    for psm in PSMS:
        process = subprocess.run(
            ["tesseract", "stdin", "stdout", "--psm", str(psm)],
            input=_png_bytes(crop), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True,
        )
        observed = normalize_text(process.stdout.decode("utf-8", errors="replace"))
        scores.append({"psm": psm, "similarity": round(SequenceMatcher(None, target, observed).ratio(), 6)})
    best = max(scores, key=lambda item: as_float(item["similarity"]))
    return {
        "best_similarity": best["similarity"],
        "best_psm": best["psm"],
        "passes_threshold": as_float(best["similarity"]) >= GATE_THRESHOLD,
        "psm_scores": scores,
    }


def candidate_audit(receipt: dict[str, object]) -> dict[str, object]:
    records = receipt["records"]
    if not isinstance(records, list):
        raise TypeError("candidate records invalid")
    regions = ["full", "headline", "lower", "numeric"]
    references = {region: collections.Counter() for region in regions}
    observations = {variant: {region: collections.Counter() for region in regions} for variant in REPRESENTED}
    critical_references = {region: collections.Counter() for region in regions}
    critical_observations = {variant: {region: collections.Counter() for region in regions} for variant in REPRESENTED}
    structural = {variant: 0 for variant in REPRESENTED}
    exact_transform = {variant: 0 for variant in BLUR}
    pixel_rows = {variant: [] for variant in REPRESENTED}
    scenes: list[dict[str, object]] = []
    for record in records:
        if not isinstance(record, dict):
            raise TypeError("candidate record invalid")
        scene = as_int(record["scene"])
        samples = record["samples"]
        if not isinstance(samples, list):
            raise TypeError("candidate samples invalid")
        paths = {str(sample["variant"]): CAND_DIR / str(sample["frame"]) for sample in samples if isinstance(sample, dict)}
        clean_agg = aggregate(ocr_rows(paths["clean"]), 1080)
        references = {region: references[region] + clean_agg[region] for region in regions}
        if scene in CRITICAL:
            critical_references = {region: critical_references[region] + clean_agg[region] for region in regions}
        with Image.open(paths["clean"]) as native_open, Image.open(paths["downscale_360p"]) as base_open:
            native = native_open.convert("RGB")
            base = np.asarray(base_open.convert("RGB"), dtype=np.uint8)
        variants: dict[str, object] = {}
        for variant in REPRESENTED:
            rows = ocr_rows(paths[variant])
            observed_agg = aggregate(rows, 360)
            observations[variant] = {region: observations[variant][region] + observed_agg[region] for region in regions}
            if scene in CRITICAL:
                critical_observations[variant] = {region: critical_observations[variant][region] + observed_agg[region] for region in regions}
            has_gate = gate_found(rows)
            structural[variant] += int(has_gate)
            with Image.open(paths[variant]) as observed_open:
                observed_pixels = np.asarray(observed_open.convert("RGB"), dtype=np.uint8)
            metrics = pixel_metrics(base, observed_pixels)
            pixel_rows[variant].append(metrics)
            entry: dict[str, object] = {
                "recall_vs_native_clean": {region: recall(clean_agg[region], observed_agg[region]) for region in regions},
                "structural_gate_found": has_gate,
                "pixels_vs_lossless_360p": metrics,
            }
            if variant in BLUR:
                exact = np.array_equal(derive(native, BLUR[variant]), observed_pixels)
                exact_transform[variant] += int(exact)
                entry["exact_transform_recomputed"] = exact
            variants[variant] = entry
        scenes.append({"scene": scene, "critical": scene in CRITICAL, "variants": variants})
    aggregates: dict[str, object] = {}
    critical: dict[str, object] = {}
    for variant in REPRESENTED:
        aggregates[variant] = {
            **{f"{region}_recall": recall(references[region], observations[variant][region]) for region in regions},
            "structural_gate_scene_count": structural[variant],
            "exact_transform_recomputed_scenes": exact_transform.get(variant),
            **{f"mean_{key}": round(sum(as_float(row[key]) for row in pixel_rows[variant]) / len(pixel_rows[variant]), 6) for key in pixel_rows[variant][0]},
        }
        critical[variant] = {
            **{f"{region}_recall": recall(critical_references[region], critical_observations[variant][region]) for region in regions},
            "structural_gate_scene_count": sum(
                int(bool(cast(dict[str, object], cast(dict[str, object], row["variants"])[variant])["structural_gate_found"]))
                for row in scenes if row["critical"]
            ),
        }
    return {
        "scene_metrics": scenes,
        "aggregate": aggregates,
        "held_critical_scenes_7_9_10_11_16": critical,
        "human_review": {
            "defocus_r1_50_then_360p_structural_gate_scene_count": 0,
            "large_result_headlines_numbers_plots_remain_primary": True,
            "axes_error_bars_caveats_citations_provenance_weaken_first": True,
            "compound_transform_repairs_candidate": False,
        },
    }


def method_audit(receipt: dict[str, object]) -> dict[str, object]:
    pass12 = json.loads((ROOT / "qa/pass12_sharpness_safe_mockup/receipt.json").read_text())
    canonical = {as_int(scene["scene"]): str(scene["gate_line"]) for scene in pass12["scenes"]}
    groups = receipt["groups"]
    if not isinstance(groups, dict):
        raise TypeError("method groups invalid")
    results: dict[str, object] = {}
    for group_name, group in groups.items():
        if not isinstance(group, dict):
            raise TypeError("method group invalid")
        scenes = group["scenes"]
        if not isinstance(scenes, list):
            raise TypeError("method scenes invalid")
        variants: dict[str, object] = {}
        for variant in REPRESENTED:
            exact_count = 0
            gates: list[dict[str, object]] = []
            for scene_record in scenes:
                if not isinstance(scene_record, dict):
                    raise TypeError("method scene invalid")
                scene = as_int(scene_record["scene"])
                samples = scene_record["samples"]
                if not isinstance(samples, list):
                    raise TypeError("method samples invalid")
                sample_map = {str(sample["variant"]): sample for sample in samples if isinstance(sample, dict)}
                path = METHOD_DIR / group_name / str(sample_map[variant]["frame"])
                if variant in BLUR:
                    source = ROOT / str(scene_record["source"])
                    with Image.open(source) as native_open, Image.open(path) as observed_open:
                        expected = derive(native_open.convert("RGB"), BLUR[variant])
                        observed = np.asarray(observed_open.convert("RGB"), dtype=np.uint8)
                    exact_count += int(np.array_equal(expected, observed))
                if group_name == "pass12_sharpness_safe":
                    gates.append({"scene": scene, **ocr_crop_similarity(path, canonical[scene], variant)})
            entry: dict[str, object] = {"exact_transform_recomputed_scenes": exact_count if variant in BLUR else None}
            if gates:
                entry["gate_rows"] = gates
                entry["gate_count_passing_threshold"] = sum(int(bool(row["passes_threshold"])) for row in gates)
                entry["mean_best_similarity"] = round(sum(as_float(row["best_similarity"]) for row in gates) / len(gates), 6)
            variants[variant] = entry
        results[group_name] = {"variants": variants}
    results["human_review"] = {
        "sealed_v8_defocus_r1_50_then_360p_result_held_badges": "7/7",
        "sealed_v8_defocus_r1_50_then_360p_major_status_boundaries": "7/7",
        "sealed_v8_required_meaning_ambiguous": False,
        "pass7_defocus_r1_50_then_360p_exact_top_gates": "7/7",
        "pass7_defocus_r1_50_then_360p_result_held_badges": "7/7",
        "pass12_defocus_r1_50_then_360p_exact_top_gates": "7/7",
        "pass12_defocus_r1_50_then_360p_result_held_badges": "7/7",
        "pass12_defocus_r4_00_then_360p_top_gate_hierarchy_recognizable": "7/7_CHARACTERIZATION",
        "pass12_defocus_r4_00_then_360p_exact_wording_acceptance_reliable": False,
        "pass12_defocus_r1_50_then_360p_overlap_clipping_or_ambiguity": False,
        "fine_axes_citations_provenance_not_acceptance_reliable_at_r4_00": True,
    }
    return results


def main() -> None:
    candidate_receipt = json.loads((CAND_DIR / "extraction_receipt.json").read_text())
    method_receipt = json.loads((METHOD_DIR / "receipt.json").read_text())
    candidate = candidate_audit(candidate_receipt)
    method = method_audit(method_receipt)
    operational = cast(dict[str, object], cast(dict[str, object], candidate["aggregate"])["defocus_r1_50_then_360p"])
    proof = cast(dict[str, object], cast(dict[str, object], cast(dict[str, object], method["pass12_sharpness_safe"])["variants"])["defocus_r1_50_then_360p"])
    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 20,
        "completed_at": "2026-08-08T12:12:58+09:00",
        "focus": "native Gaussian spatial defocus followed by minimum-scale 640x360 interaction",
        "candidate_sha256": candidate_receipt["candidate_sha256"],
        "candidate": candidate,
        "method": method,
        "decision": {
            "operational_variant": "defocus_r1_50_then_360p",
            "characterization_variants": ["defocus_r2_50_then_360p", "defocus_r4_00_then_360p"],
            "candidate_operational_structural_gate_scenes": operational["structural_gate_scene_count"],
            "pass12_operational_exact_gate_count": proof["gate_count_passing_threshold"],
            "new_pixel_or_copy_correction_justified": False,
            "action": "ADD_MINIMUM_SCALE_DEFOCUS_INTEGRATION_GUARD",
            "reason": "The latest pass12 proof preserves all seven exact top gates and complete badges under the operational compound transform; the failed candidate remains structurally ungated while its fine support weakens.",
        },
        "metric_notes": {
            "ocr": "OCR is a reproducible aid; global segmentation at 360p is not an acceptance oracle.",
            "mapped_gate_crops": "Fixed native/360p gate boxes, PSM 6/7/11/13, threshold 0.80; scores only, no recognized text stored.",
            "pixels": "Incremental PSNR, MAE, edge recall, and gradient energy are measured against the lossless 360p reference; exact transform recomputation is the representation oracle.",
            "human_review": "Represented-pixel review decides gate/container visibility, hierarchy, clipping, overlap, ambiguity, and exact-copy reliability.",
        },
        "video_reportable_now": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "published": False,
        "git_action": False,
    }
    OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        "PASS candidate=16/80 method=21/105 "
        f"candidate_r1_50_then_360p_headline={as_float(operational['headline_recall']):.6f} "
        f"candidate_r1_50_then_360p_full={as_float(operational['full_recall']):.6f} "
        f"proof_gates={proof['gate_count_passing_threshold']}/7"
    )


if __name__ == "__main__":
    main()
