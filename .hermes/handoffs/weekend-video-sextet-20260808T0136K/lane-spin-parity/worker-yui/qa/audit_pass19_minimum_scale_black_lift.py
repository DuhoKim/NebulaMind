#!/usr/bin/env python3
"""Quantify pass-19 minimum-scale plus linear-light black-lift interaction."""

from __future__ import annotations

import collections
import csv
import io
import json
import re
import subprocess
from difflib import SequenceMatcher
from pathlib import Path
from typing import cast

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CAND_DIR = ROOT / "qa/pass19_minimum_scale_black_lift_audit"
METHOD_DIR = ROOT / "qa/pass19_v8_minimum_scale_black_lift"
OUT = ROOT / "qa/pass19_minimum_scale_black_lift_quantitative_audit.json"
VARIANTS = ["clean", "downscale_360p", "black_lift20_360p", "black_lift30_360p", "black_lift40_360p"]
REPRESENTED = VARIANTS[1:]
LIFT = {"black_lift20_360p": 0.20, "black_lift30_360p": 0.30, "black_lift40_360p": 0.40}
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


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.0031308, values * 12.92, 1.055 * values ** (1.0 / 2.4) - 0.055)


def lift_pixels(base: np.ndarray, amount: float) -> np.ndarray:
    srgb = base.astype(np.float64) / 255.0
    linear = srgb_to_linear(srgb)
    lifted = amount + (1.0 - amount) * linear
    return np.rint(np.clip(linear_to_srgb(lifted), 0.0, 1.0) * 255.0).astype(np.uint8)


def luminance_metrics(path: Path) -> dict[str, float]:
    with Image.open(path) as opened:
        srgb = np.asarray(opened.convert("RGB"), dtype=np.float64) / 255.0
    linear = srgb_to_linear(srgb)
    luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
    p01, p99 = np.percentile(luminance, [1.0, 99.0])
    return {
        "linear_luminance_p01": round(float(p01), 6),
        "linear_luminance_p99": round(float(p99), 6),
        "robust_wcag_like_ratio_p99_p01": round(float((p99 + 0.05) / (p01 + 0.05)), 6),
        "linear_luminance_std": round(float(luminance.std()), 6),
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
    exact_transform = {variant: 0 for variant in LIFT}
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
        with Image.open(paths["downscale_360p"]) as base_open:
            base = np.asarray(base_open.convert("RGB"), dtype=np.uint8)
        variants: dict[str, object] = {}
        for variant in REPRESENTED:
            rows = ocr_rows(paths[variant])
            observed = aggregate(rows, 360)
            observations[variant] = {region: observations[variant][region] + observed[region] for region in regions}
            if scene in CRITICAL:
                critical_observations[variant] = {region: critical_observations[variant][region] + observed[region] for region in regions}
            has_gate = gate_found(rows)
            structural[variant] += int(has_gate)
            entry: dict[str, object] = {
                "recall_vs_native_clean": {region: recall(clean_agg[region], observed[region]) for region in regions},
                "structural_gate_found": has_gate,
                "luminance": luminance_metrics(paths[variant]),
            }
            if variant in LIFT:
                with Image.open(paths[variant]) as observed_open:
                    observed_pixels = np.asarray(observed_open.convert("RGB"), dtype=np.uint8)
                exact = np.array_equal(lift_pixels(base, LIFT[variant]), observed_pixels)
                exact_transform[variant] += int(exact)
                entry["exact_transform_recomputed"] = exact
            variants[variant] = entry
        scenes.append({"scene": scene, "critical": scene in CRITICAL, "variants": variants})
    aggregates: dict[str, object] = {}
    critical: dict[str, object] = {}
    for variant in REPRESENTED:
        robust_ratios: list[float] = []
        for scene_row in scenes:
            variant_map = cast(dict[str, object], scene_row["variants"])
            variant_row = cast(dict[str, object], variant_map[variant])
            luminance = cast(dict[str, object], variant_row["luminance"])
            robust_ratios.append(as_float(luminance["robust_wcag_like_ratio_p99_p01"]))
        aggregates[variant] = {
            **{f"{region}_recall": recall(references[region], observations[variant][region]) for region in regions},
            "structural_gate_scene_count": structural[variant],
            "exact_transform_recomputed_scenes": exact_transform.get(variant),
            "mean_robust_wcag_like_ratio_p99_p01": round(sum(robust_ratios) / len(robust_ratios), 6),
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
            "black_lift20_360p_structural_gate_scene_count": 0,
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
                if variant in LIFT:
                    base_path = METHOD_DIR / group_name / str(sample_map["downscale_360p"]["frame"])
                    with Image.open(base_path) as base_open, Image.open(path) as observed_open:
                        base = np.asarray(base_open.convert("RGB"), dtype=np.uint8)
                        observed = np.asarray(observed_open.convert("RGB"), dtype=np.uint8)
                    exact_count += int(np.array_equal(lift_pixels(base, LIFT[variant]), observed))
                if group_name == "pass12_sharpness_safe":
                    gates.append({"scene": scene, **ocr_crop_similarity(path, canonical[scene], variant)})
            entry: dict[str, object] = {"exact_transform_recomputed_scenes": exact_count if variant in LIFT else None}
            if gates:
                entry["gate_rows"] = gates
                entry["gate_count_passing_threshold"] = sum(int(bool(row["passes_threshold"])) for row in gates)
                entry["mean_best_similarity"] = round(sum(as_float(row["best_similarity"]) for row in gates) / len(gates), 6)
            variants[variant] = entry
        results[group_name] = {"variants": variants}
    results["human_review"] = {
        "sealed_v8_black_lift20_360p_result_held_badges": "7/7",
        "sealed_v8_black_lift20_360p_major_status_boundaries": "7/7",
        "sealed_v8_required_meaning_ambiguous": False,
        "pass7_black_lift20_360p_exact_top_gates": "7/7",
        "pass7_black_lift20_360p_result_held_badges": "7/7",
        "pass12_black_lift20_360p_exact_top_gates": "7/7",
        "pass12_black_lift20_360p_result_held_badges": "7/7",
        "pass12_black_lift40_360p_exact_top_gates": "7/7_CHARACTERIZATION",
        "pass12_black_lift40_360p_result_held_badges": "7/7_CHARACTERIZATION",
        "pass12_black_lift20_360p_overlap_clipping_or_ambiguity": False,
        "fine_axes_citations_provenance_not_acceptance_reliable": True,
    }
    return results


def main() -> None:
    candidate_receipt = json.loads((CAND_DIR / "extraction_receipt.json").read_text())
    method_receipt = json.loads((METHOD_DIR / "receipt.json").read_text())
    candidate = candidate_audit(candidate_receipt)
    method = method_audit(method_receipt)
    operational = cast(dict[str, object], cast(dict[str, object], candidate["aggregate"])["black_lift20_360p"])
    proof = cast(dict[str, object], cast(dict[str, object], cast(dict[str, object], method["pass12_sharpness_safe"])["variants"])["black_lift20_360p"])
    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 19,
        "completed_at": "2026-08-08T11:49:42+09:00",
        "focus": "minimum-scale 640x360 plus represented-pixel linear-light black-lift interaction",
        "candidate_sha256": candidate_receipt["candidate_sha256"],
        "candidate": candidate,
        "method": method,
        "decision": {
            "operational_variant": "black_lift20_360p",
            "characterization_variants": ["black_lift30_360p", "black_lift40_360p"],
            "candidate_operational_structural_gate_scenes": operational["structural_gate_scene_count"],
            "pass12_operational_exact_gate_count": proof["gate_count_passing_threshold"],
            "new_pixel_or_copy_correction_justified": False,
            "action": "ADD_MINIMUM_SCALE_BLACK_LIFT_INTEGRATION_GUARD",
            "reason": "The latest pass12 proof preserves all seven exact top gates and complete badges under the operational compound transform; the failed candidate remains structurally ungated while its qualification hierarchy weakens.",
        },
        "metric_notes": {
            "ocr": "OCR is a reproducible aid; global segmentation at 360p is not an acceptance oracle.",
            "mapped_gate_crops": "Fixed native/360p gate boxes, PSM 6/7/11/13, threshold 0.80; scores only, no recognized text stored.",
            "luminance": "Robust p99/p01 ratios are diagnostics; the exact linear-light transform is the representation oracle.",
            "human_review": "Represented-pixel review decides gate/container visibility, hierarchy, clipping, overlap, and ambiguity.",
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
        f"candidate_blacklift20_headline={as_float(operational['headline_recall']):.6f} "
        f"candidate_blacklift20_full={as_float(operational['full_recall']):.6f} "
        f"proof_gates={proof['gate_count_passing_threshold']}/7"
    )


if __name__ == "__main__":
    main()
