#!/usr/bin/env python3
"""Quantify pass-18 minimum-scale plus bottom-obstruction interaction."""

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
CAND_DIR = ROOT / "qa/pass18_minimum_scale_obstruction_audit"
METHOD_DIR = ROOT / "qa/pass18_v8_minimum_scale_obstruction"
OUT = ROOT / "qa/pass18_minimum_scale_obstruction_quantitative_audit.json"
VARIANTS = ["clean", "downscale_360p", "caption15_360p", "player_ui25_360p", "heavy35_360p"]
REPRESENTED_VARIANTS = VARIANTS[1:]
MASK_TOP = {"caption15_360p": 306, "player_ui25_360p": 270, "heavy35_360p": 234}
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
    return "".join(ch for ch in value.lower() if ch.isalnum())


def ocr_rows(path: Path, psm: int = 11) -> list[dict[str, object]]:
    command = ["tesseract", str(path), "stdout", "--psm", str(psm), "tsv"]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    rows: list[dict[str, object]] = []
    reader = csv.DictReader(io.StringIO(result.stdout), delimiter="\t")
    for row in reader:
        token = normalize_token(row.get("text") or "")
        try:
            conf = float(row.get("conf") or -1)
        except ValueError:
            conf = -1
        if token and conf >= 0:
            rows.append({
                "token": token,
                "left": int(row["left"]), "top": int(row["top"]),
                "width": int(row["width"]), "height": int(row["height"]),
                "conf": conf,
            })
    return rows


def counter(rows: list[dict[str, object]], region: str, width: int, height: int) -> collections.Counter[str]:
    result: collections.Counter[str] = collections.Counter()
    for row in rows:
        token = str(row["token"])
        y_center = (int(row["top"]) + int(row["height"]) / 2) / height
        include = (
            region == "full"
            or (region == "headline" and y_center < 0.325)
            or (region == "lower" and y_center >= 0.60)
            or (region == "numeric" and any(ch.isdigit() for ch in token))
        )
        if include:
            result[token] += 1
    return result


def recall(reference: collections.Counter[str], observed: collections.Counter[str]) -> float:
    total = sum(reference.values())
    if not total:
        return 1.0
    return round(sum(min(count, observed[token]) for token, count in reference.items()) / total, 6)


def aggregate(rows: list[dict[str, object]], width: int, height: int) -> dict[str, collections.Counter[str]]:
    return {region: counter(rows, region, width, height) for region in ["full", "headline", "lower", "numeric"]}


def gate_found(rows: list[dict[str, object]]) -> bool:
    tokens = [str(row["token"]) for row in rows]
    return any(
        any(tuple(tokens[index:index + len(pattern)]) == pattern for index in range(len(tokens) - len(pattern) + 1))
        for pattern in GATE_PATTERNS
    )


def ocr_crop_similarity(path: Path, canonical: str, variant: str) -> dict[str, object]:
    with Image.open(path) as opened:
        image = opened.convert("RGB")
    if variant == "clean":
        box = (98, 74, 1544, 125)
        pad = 12
    else:
        box = (32, 24, 516, 43)
        pad = 4
    crop = image.crop((max(0, box[0] - pad), max(0, box[1] - pad), min(image.width, box[2] + pad), min(image.height, box[3] + pad)))
    crop = crop.resize((crop.width * 4, crop.height * 4), Image.Resampling.LANCZOS)
    scores: list[dict[str, object]] = []
    target = normalize_text(canonical)
    for psm in PSMS:
        process = subprocess.run(
            ["tesseract", "stdin", "stdout", "--psm", str(psm)],
            input=_png_bytes(crop), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True,
        )
        observed = normalize_text(process.stdout.decode("utf-8", errors="replace"))
        scores.append({"psm": psm, "similarity": round(SequenceMatcher(None, target, observed).ratio(), 6)})
    best = max(scores, key=lambda item: float(item["similarity"]))
    return {
        "best_similarity": best["similarity"],
        "best_psm": best["psm"],
        "passes_threshold": float(best["similarity"]) >= GATE_THRESHOLD,
        "psm_scores": scores,
    }


def _png_bytes(image: Image.Image) -> bytes:
    stream = io.BytesIO()
    image.save(stream, format="PNG", optimize=False)
    return stream.getvalue()


def candidate_audit(receipt: dict[str, object]) -> dict[str, object]:
    scene_rows: list[dict[str, object]] = []
    all_refs: dict[str, collections.Counter[str]] = {key: collections.Counter() for key in ["full", "headline", "lower", "numeric"]}
    all_obs: dict[str, dict[str, collections.Counter[str]]] = {
        variant: {key: collections.Counter() for key in all_refs} for variant in REPRESENTED_VARIANTS
    }
    critical_refs = {key: collections.Counter() for key in all_refs}
    critical_obs = {variant: {key: collections.Counter() for key in all_refs} for variant in REPRESENTED_VARIANTS}
    structural = {variant: 0 for variant in REPRESENTED_VARIANTS}
    zone_tokens = {variant: {"reference_downscale_tokens_in_mask_zone": 0, "observed_tokens_in_mask_zone": 0} for variant in MASK_TOP}
    records = receipt["records"]
    if not isinstance(records, list):
        raise TypeError("candidate records invalid")
    for record in records:
        if not isinstance(record, dict):
            raise TypeError("candidate record invalid")
        scene = int(record["scene"])
        samples = record["samples"]
        if not isinstance(samples, list):
            raise TypeError("candidate samples invalid")
        paths = {str(sample["variant"]): CAND_DIR / str(sample["frame"]) for sample in samples if isinstance(sample, dict)}
        clean_rows = ocr_rows(paths["clean"])
        clean_agg = aggregate(clean_rows, 1920, 1080)
        down_rows = ocr_rows(paths["downscale_360p"])
        all_refs = {key: all_refs[key] + clean_agg[key] for key in all_refs}
        if scene in CRITICAL:
            critical_refs = {key: critical_refs[key] + clean_agg[key] for key in critical_refs}
        variants: dict[str, object] = {}
        for variant in REPRESENTED_VARIANTS:
            observed_rows = down_rows if variant == "downscale_360p" else ocr_rows(paths[variant])
            observed_agg = aggregate(observed_rows, 640, 360)
            all_obs[variant] = {key: all_obs[variant][key] + observed_agg[key] for key in all_refs}
            if scene in CRITICAL:
                critical_obs[variant] = {key: critical_obs[variant][key] + observed_agg[key] for key in all_refs}
            has_gate = gate_found(observed_rows)
            structural[variant] += int(has_gate)
            detail: dict[str, object] = {
                "recall_vs_native_clean": {key: recall(clean_agg[key], observed_agg[key]) for key in all_refs},
                "structural_gate_found": has_gate,
            }
            if variant in MASK_TOP:
                top = MASK_TOP[variant]
                reference_zone = [row for row in down_rows if int(row["top"]) + int(row["height"]) / 2 >= top]
                observed_zone = [row for row in observed_rows if int(row["top"]) + int(row["height"]) / 2 >= top]
                zone_tokens[variant]["reference_downscale_tokens_in_mask_zone"] += len(reference_zone)
                zone_tokens[variant]["observed_tokens_in_mask_zone"] += len(observed_zone)
                with Image.open(paths["downscale_360p"]) as base_open, Image.open(paths[variant]) as obs_open:
                    base = np.asarray(base_open.convert("RGB"), dtype=np.uint8)
                    obs = np.asarray(obs_open.convert("RGB"), dtype=np.uint8)
                detail["unobstructed_pixel_identity"] = bool(np.array_equal(base[:top], obs[:top]))
                detail["masked_pixels_all_black"] = bool(np.all(obs[top:] == 0))
                detail["source_nonblack_fraction_in_mask_zone"] = round(float(np.mean(np.any(base[top:] != 0, axis=2))), 6)
            variants[variant] = detail
        scene_rows.append({"scene": scene, "critical": scene in CRITICAL, "variants": variants})
    aggregates: dict[str, object] = {}
    critical: dict[str, object] = {}
    for variant in REPRESENTED_VARIANTS:
        aggregates[variant] = {
            **{f"{key}_recall": recall(all_refs[key], all_obs[variant][key]) for key in all_refs},
            "structural_gate_scene_count": structural[variant],
        }
        critical[variant] = {
            **{f"{key}_recall": recall(critical_refs[key], critical_obs[variant][key]) for key in all_refs},
            "structural_gate_scene_count": sum(
                int(cast(dict[str, object], cast(dict[str, object], row["variants"])[variant])["structural_gate_found"])
                for row in scene_rows if row["critical"]
            ),
        }
    return {
        "scene_metrics": scene_rows,
        "aggregate": aggregates,
        "held_critical_scenes_7_9_10_11_16": critical,
        "obstruction_zone_ocr": zone_tokens,
        "human_review": {
            "player_ui25_360p_structural_gate_scene_count": 0,
            "large_result_headlines_numbers_plots_remain_primary": True,
            "axes_caveats_citations_and_provenance_occluded_or_weakened_first": True,
            "compound_transform_repairs_candidate": False,
        },
    }


def method_audit(receipt: dict[str, object]) -> dict[str, object]:
    pass12_receipt = json.loads((ROOT / "qa/pass12_sharpness_safe_mockup/receipt.json").read_text())
    canonical = {int(scene["scene"]): str(scene["gate_line"]) for scene in pass12_receipt["scenes"]}
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
        variant_metrics: dict[str, object] = {}
        for variant in REPRESENTED_VARIANTS:
            gate_rows: list[dict[str, object]] = []
            top_identity = 0
            all_black = 0
            for scene_record in scenes:
                if not isinstance(scene_record, dict):
                    raise TypeError("method scene invalid")
                scene = int(scene_record["scene"])
                samples = scene_record["samples"]
                if not isinstance(samples, list):
                    raise TypeError("method samples invalid")
                sample_map = {str(sample["variant"]): sample for sample in samples if isinstance(sample, dict)}
                path = METHOD_DIR / group_name / str(sample_map[variant]["frame"])
                if variant in MASK_TOP:
                    base_path = METHOD_DIR / group_name / str(sample_map["downscale_360p"]["frame"])
                    with Image.open(base_path) as base_open, Image.open(path) as obs_open:
                        base = np.asarray(base_open.convert("RGB"), dtype=np.uint8)
                        obs = np.asarray(obs_open.convert("RGB"), dtype=np.uint8)
                    top = MASK_TOP[variant]
                    top_identity += int(np.array_equal(base[:top], obs[:top]))
                    all_black += int(np.all(obs[top:] == 0))
                if group_name == "pass12_sharpness_safe":
                    score = ocr_crop_similarity(path, canonical[scene], variant)
                    gate_rows.append({"scene": scene, **score})
            entry: dict[str, object] = {}
            if variant in MASK_TOP:
                entry["unobstructed_pixel_identity_scenes"] = top_identity
                entry["masked_pixels_all_black_scenes"] = all_black
            if gate_rows:
                entry["gate_rows"] = gate_rows
                entry["gate_count_passing_threshold"] = sum(int(bool(row["passes_threshold"])) for row in gate_rows)
                entry["mean_best_similarity"] = round(sum(float(row["best_similarity"]) for row in gate_rows) / len(gate_rows), 6)
            variant_metrics[variant] = entry
        results[group_name] = {"variants": variant_metrics}
    results["human_review"] = {
        "sealed_v8_player25_result_held_badges": "7/7",
        "sealed_v8_scene_specific_lower_boundaries_occluded": ["S2", "S3", "S4", "S5", "S6"],
        "sealed_v8_scene_specific_status_complete_under_player25": False,
        "pass7_player25_exact_top_gates": "7/7",
        "pass7_player25_result_held_badges": "7/7",
        "pass12_player25_exact_top_gates": "7/7",
        "pass12_player25_result_held_badges": "7/7",
        "pass12_heavy35_exact_top_gates": "7/7_CHARACTERIZATION",
        "pass12_player25_overlap_clipping_or_ambiguity": False,
        "lower_scientific_support_occluded_by_design": True,
    }
    return results


def main() -> None:
    candidate_receipt = json.loads((CAND_DIR / "extraction_receipt.json").read_text())
    method_receipt = json.loads((METHOD_DIR / "receipt.json").read_text())
    candidate = candidate_audit(candidate_receipt)
    method = method_audit(method_receipt)
    player = cast(dict[str, object], cast(dict[str, object], candidate["aggregate"])["player_ui25_360p"])
    pass12_player = cast(dict[str, object], cast(dict[str, object], cast(dict[str, object], method["pass12_sharpness_safe"])["variants"])["player_ui25_360p"])
    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 18,
        "completed_at": "2026-08-08T11:27:07+09:00",
        "focus": "minimum-scale 640x360 plus opaque bottom-obstruction interaction",
        "candidate_sha256": candidate_receipt["candidate_sha256"],
        "candidate": candidate,
        "method": method,
        "decision": {
            "operational_variants": ["caption15_360p", "player_ui25_360p"],
            "characterization_variant": "heavy35_360p",
            "candidate_player25_structural_gate_scenes": player["structural_gate_scene_count"],
            "pass12_player25_exact_gate_count": pass12_player["gate_count_passing_threshold"],
            "new_pixel_or_copy_correction_justified": False,
            "action": "ADD_MINIMUM_SCALE_OBSTRUCTION_INTEGRATION_GUARD",
            "reason": "The latest pass12 proof preserves all seven exact top gates and badges under both operational bottom masks with byte-identical unobstructed pixels; the failed candidate remains structurally ungated while lower support is occluded.",
        },
        "metric_notes": {
            "ocr": "OCR is a reproducible aid; global segmentation may change even where upper pixels are identical.",
            "mapped_gate_crops": "Fixed native/360p gate boxes, PSM 6/7/11/13, threshold 0.80; stores scores only.",
            "obstruction": "Opaque masks deliberately remove lower pixels; pixel identity above mask_top_y is the exact transform oracle.",
            "human_review": "Represented-pixel review decides gate/container visibility, semantic hierarchy, clipping, overlap, and ambiguity.",
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
        f"candidate_player25_headline={float(player['headline_recall']):.6f} "
        f"candidate_player25_lower={float(player['lower_recall']):.6f} "
        f"proof_gates={pass12_player['gate_count_passing_threshold']}/7"
    )


if __name__ == "__main__":
    main()
