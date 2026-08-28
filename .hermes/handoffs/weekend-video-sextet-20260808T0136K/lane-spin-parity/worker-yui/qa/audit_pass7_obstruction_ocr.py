#!/usr/bin/env python3
"""Quantify scientific text hierarchy under caption/player obstruction."""

from __future__ import annotations

import collections
import csv
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
AUDIT_ROOT = ROOT / "qa/pass7_obstruction_audit"
RECEIPT = AUDIT_ROOT / "extraction_receipt.json"
OUTPUT = ROOT / "qa/pass7_obstruction_ocr_audit.json"
CRITICAL_SCENES = {7, 9, 10, 11, 16}
VARIANTS = ["clean", "caption_15pct", "player_ui_25pct"]


def normalize(text: str) -> str:
    return "".join(re.findall(r"[a-z0-9]+", text.casefold()))


def token_hash(tokens: list[str]) -> str:
    return hashlib.sha256("\n".join(tokens).encode("utf-8")).hexdigest()


def phrase_present(tokens: list[str], phrase: tuple[str, ...]) -> bool:
    if len(tokens) < len(phrase):
        return False
    return any(tuple(tokens[index : index + len(phrase)]) == phrase for index in range(len(tokens) - len(phrase) + 1))


def ocr_frame(path: Path) -> dict[str, Any]:
    process = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "6", "tsv"],
        check=True,
        text=True,
        capture_output=True,
    )
    rows = csv.DictReader(io.StringIO(process.stdout), delimiter="\t")
    with Image.open(path) as image:
        width, height = image.size
    tokens: list[dict[str, Any]] = []
    for row in rows:
        text = normalize(row.get("text", ""))
        if not text:
            continue
        try:
            confidence = float(row.get("conf", "-1"))
        except ValueError:
            continue
        if confidence < 20.0:
            continue
        left = int(row.get("left", "0"))
        top = int(row.get("top", "0"))
        box_width = int(row.get("width", "0"))
        box_height = int(row.get("height", "0"))
        center_y = (top + box_height / 2.0) / height
        tokens.append(
            {
                "token": text,
                "confidence": confidence,
                "left": left,
                "top": top,
                "width": box_width,
                "height": box_height,
                "center_y_fraction": center_y,
            }
        )
    return {"width": width, "height": height, "tokens": tokens}


def region_tokens(result: dict[str, Any], region: str) -> list[str]:
    tokens: list[str] = []
    for row in result["tokens"]:
        y = float(row["center_y_fraction"])
        include = {
            "full": True,
            "headline": y < 0.30,
            "middle": 0.30 <= y < 0.65,
            "lower_support": y >= 0.65,
            "bottom_25pct": y >= 0.75,
            "bottom_15pct": y >= 0.85,
        }[region]
        if include:
            tokens.append(str(row["token"]))
    return tokens


def multiset_retention(reference: list[str], sample: list[str]) -> float:
    if not reference:
        return 1.0 if not sample else 0.0
    reference_counts = collections.Counter(reference)
    sample_counts = collections.Counter(sample)
    matched = sum(min(count, sample_counts[token]) for token, count in reference_counts.items())
    return matched / len(reference)


def numeric_count(tokens: list[str]) -> int:
    return sum(any(character.isdigit() for character in token) for token in tokens)


def crop_hash(path: Path, bottom_fraction: float) -> str:
    with Image.open(path).convert("RGB") as image:
        bottom = round(image.height * (1.0 - bottom_fraction))
        crop = image.crop((0, 0, image.width, bottom))
        return hashlib.sha256(crop.tobytes()).hexdigest()


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def main() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    if receipt["scene_count"] != 16 or receipt["frame_count"] != 48:
        raise SystemExit("unexpected pass-7 receipt census")
    scenes: list[dict[str, Any]] = []
    aggregate_rows: dict[str, list[dict[str, Any]]] = {variant: [] for variant in VARIANTS}
    for scene in receipt["scenes"]:
        scene_number = int(scene["scene"])
        sample_map = {sample["variant"]: sample for sample in scene["samples"]}
        if list(sample_map) != VARIANTS:
            raise SystemExit(f"variant order mismatch scene {scene_number}")
        ocr = {
            variant: ocr_frame(AUDIT_ROOT / sample_map[variant]["frame"])
            for variant in VARIANTS
        }
        reference_regions = {
            region: region_tokens(ocr["clean"], region)
            for region in ("full", "headline", "middle", "lower_support", "bottom_25pct", "bottom_15pct")
        }
        sample_rows: list[dict[str, Any]] = []
        for variant in VARIANTS:
            full_tokens = region_tokens(ocr[variant], "full")
            regions: dict[str, Any] = {}
            for region, reference_tokens in reference_regions.items():
                current_tokens = region_tokens(ocr[variant], region)
                regions[region] = {
                    "token_count": len(current_tokens),
                    "token_multiset_sha256": token_hash(current_tokens),
                    "retention_vs_clean": round(multiset_retention(reference_tokens, current_tokens), 6),
                    "numeric_token_count": numeric_count(current_tokens),
                }
            obstruction = float(sample_map[variant]["occluded_bottom_fraction"])
            if variant == "clean":
                top_region_identical_to_clean = True
            else:
                top_region_identical_to_clean = crop_hash(
                    AUDIT_ROOT / sample_map[variant]["frame"], obstruction
                ) == crop_hash(AUDIT_ROOT / sample_map["clean"]["frame"], obstruction)
            structural_gate = {
                "result_held": phrase_present(full_tokens, ("result", "held")),
                "frame_unstated": phrase_present(full_tokens, ("frame", "unstated")),
                "outcomes_withheld": phrase_present(full_tokens, ("outcomes", "withheld")),
                "no_outcome_shown": phrase_present(full_tokens, ("no", "outcome", "shown")),
            }
            row = {
                "variant": variant,
                "occluded_bottom_fraction": obstruction,
                "full_token_multiset_sha256": token_hash(full_tokens),
                "top_region_pixel_identical_to_clean": top_region_identical_to_clean,
                "regions": regions,
                "structural_gate_detected": structural_gate,
                "any_structural_gate_detected": any(structural_gate.values()),
            }
            sample_rows.append(row)
            aggregate_rows[variant].append({"scene": scene_number, **row})
        scenes.append({"scene": scene_number, "critical": scene_number in CRITICAL_SCENES, "samples": sample_rows})

    aggregates: dict[str, Any] = {}
    critical_metrics: dict[str, Any] = {}
    for variant in VARIANTS:
        rows = aggregate_rows[variant]
        aggregates[variant] = {
            "scene_count": len(rows),
            "mean_full_token_retention_vs_clean": mean([row["regions"]["full"]["retention_vs_clean"] for row in rows]),
            "mean_headline_token_retention_vs_clean": mean([row["regions"]["headline"]["retention_vs_clean"] for row in rows]),
            "mean_middle_token_retention_vs_clean": mean([row["regions"]["middle"]["retention_vs_clean"] for row in rows]),
            "mean_lower_support_token_retention_vs_clean": mean([row["regions"]["lower_support"]["retention_vs_clean"] for row in rows]),
            "mean_bottom_25pct_token_retention_vs_clean": mean([row["regions"]["bottom_25pct"]["retention_vs_clean"] for row in rows]),
            "mean_bottom_15pct_token_retention_vs_clean": mean([row["regions"]["bottom_15pct"]["retention_vs_clean"] for row in rows]),
            "scenes_with_any_structural_gate": sum(row["any_structural_gate_detected"] for row in rows),
            "scenes_with_top_region_pixel_identity": sum(row["top_region_pixel_identical_to_clean"] for row in rows),
            "mean_full_numeric_token_count": mean([float(row["regions"]["full"]["numeric_token_count"]) for row in rows]),
        }
        critical = [row for row in rows if row["scene"] in CRITICAL_SCENES]
        critical_metrics[variant] = {
            "scenes": sorted(CRITICAL_SCENES),
            "mean_full_token_retention_vs_clean": mean([row["regions"]["full"]["retention_vs_clean"] for row in critical]),
            "mean_headline_token_retention_vs_clean": mean([row["regions"]["headline"]["retention_vs_clean"] for row in critical]),
            "mean_lower_support_token_retention_vs_clean": mean([row["regions"]["lower_support"]["retention_vs_clean"] for row in critical]),
            "mean_bottom_25pct_token_retention_vs_clean": mean([row["regions"]["bottom_25pct"]["retention_vs_clean"] for row in critical]),
            "structural_gate_scene_count": sum(row["any_structural_gate_detected"] for row in critical),
        }

    obstruction_zone_loss: dict[str, Any] = {}
    for variant, region in (
        ("caption_15pct", "bottom_15pct"),
        ("player_ui_25pct", "bottom_25pct"),
    ):
        reference_scene_count = 0
        reference_token_count = 0
        surviving_token_count = 0
        zero_retention_scene_count = 0
        for scene in scenes:
            sample_map = {sample["variant"]: sample for sample in scene["samples"]}
            reference_count = sample_map["clean"]["regions"][region]["token_count"]
            if reference_count:
                reference_scene_count += 1
                reference_token_count += reference_count
                surviving_token_count += sample_map[variant]["regions"][region]["token_count"]
                zero_retention_scene_count += (
                    sample_map[variant]["regions"][region]["retention_vs_clean"] == 0.0
                )
        obstruction_zone_loss[variant] = {
            "region": region,
            "scenes_with_reference_copy": reference_scene_count,
            "reference_token_count": reference_token_count,
            "surviving_token_count": surviving_token_count,
            "scenes_with_zero_token_retention": zero_retention_scene_count,
        }

    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 7,
        "audit": "caption_and_player_ui_obstruction_ocr_hierarchy",
        "candidate_sha256": receipt["candidate_sha256"],
        "scene_count": 16,
        "frame_count": 48,
        "variant_order": VARIANTS,
        "regions": {
            "headline": "token center y < 0.30",
            "middle": "0.30 <= token center y < 0.65",
            "lower_support": "token center y >= 0.65",
            "bottom_25pct": "token center y >= 0.75",
            "bottom_15pct": "token center y >= 0.85",
        },
        "ocr": {
            "engine": subprocess.run(["tesseract", "--version"], check=True, text=True, capture_output=True).stdout.splitlines()[0],
            "page_segmentation_mode": 6,
            "minimum_confidence": 20.0,
            "normalization": "casefold alphanumeric",
            "comparison": "token-multiset retention against clean frame at same midpoint",
            "raw_ocr_text_stored": False,
        },
        "aggregates": aggregates,
        "critical_scene_metrics": critical_metrics,
        "obstruction_zone_loss": obstruction_zone_loss,
        "scenes": scenes,
        "interpretation_boundary": {
            "metric_is_presentation_only": True,
            "does_not_validate_science": True,
            "does_not_authorize_result": True,
            "human_visual_review_required": True,
        },
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    c15 = aggregates["caption_15pct"]
    ui25 = aggregates["player_ui_25pct"]
    print(
        "PASS scenes=16 frames=48 "
        f"caption15_full={c15['mean_full_token_retention_vs_clean']:.6f} "
        f"caption15_lower={c15['mean_lower_support_token_retention_vs_clean']:.6f} "
        f"ui25_full={ui25['mean_full_token_retention_vs_clean']:.6f} "
        f"ui25_lower={ui25['mean_lower_support_token_retention_vs_clean']:.6f} "
        f"gates={ui25['scenes_with_any_structural_gate']}"
    )


if __name__ == "__main__":
    main()
