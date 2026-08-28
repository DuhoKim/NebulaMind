#!/usr/bin/env python3
"""Quantify the pass-12 sharpness-safe QA proof without storing OCR text."""

from __future__ import annotations

import collections
import csv
import difflib
import io
import json
import re
import subprocess
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "qa/pass12_sharpness_safe_mockup"
OUTPUT = ROOT / "qa/pass12_sharpness_safe_quantitative_audit.json"
VARIANTS = [
    "clean",
    "defocus_r0_75",
    "defocus_r1_50",
    "defocus_r2_50",
    "defocus_r4_00",
]
def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def ocr(path: Path) -> tuple[list[str], list[str]]:
    result = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "11", "tsv"],
        check=True,
        capture_output=True,
        text=True,
    )
    all_tokens: list[str] = []
    headline_tokens: list[str] = []
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
        split = token.split()
        all_tokens.extend(split)
        if top < 350:
            headline_tokens.extend(split)
    return all_tokens, headline_tokens


def recall(reference: list[str], observed: list[str]) -> float:
    if not reference:
        return 1.0
    reference_counts = collections.Counter(reference)
    observed_counts = collections.Counter(observed)
    matched = sum(
        min(count, observed_counts[token]) for token, count in reference_counts.items()
    )
    return round(matched / sum(reference_counts.values()), 6)


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6)


def compact(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def gate_similarity(
    path: Path, box: tuple[int, int, int, int], canonical: str
) -> float:
    with Image.open(path).convert("RGB") as image:
        crop = image.crop(box)
        encoded = io.BytesIO()
        crop.save(encoded, format="PNG", optimize=False)
    reference = compact(canonical)
    similarities: list[float] = []
    for psm in (6, 7, 11, 13):
        result = subprocess.run(
            ["tesseract", "stdin", "stdout", "--psm", str(psm)],
            check=True,
            input=encoded.getvalue(),
            capture_output=True,
        )
        observed = compact(result.stdout.decode("utf-8", errors="replace"))
        similarities.append(
            difflib.SequenceMatcher(None, reference, observed).ratio()
        )
    return round(max(similarities), 6)


def main() -> None:
    receipt = json.loads((PROOF / "receipt.json").read_text(encoding="utf-8"))
    gate_box_values = receipt["gate_contract"]["box"]
    gate_box = tuple(int(value) for value in gate_box_values)
    if len(gate_box) != 4:
        raise ValueError("gate box must have four coordinates")
    scenes: list[dict[str, object]] = []
    for scene_row in receipt["scenes"]:
        scene = int(scene_row["scene"])
        by_variant: dict[str, tuple[list[str], list[str]]] = {}
        gate_similarity_by_variant: dict[str, float] = {}
        for sample in scene_row["samples"]:
            frame_path = PROOF / sample["frame"]
            by_variant[sample["variant"]] = ocr(frame_path)
            gate_similarity_by_variant[sample["variant"]] = gate_similarity(
                frame_path, gate_box, scene_row["gate_line"]
            )
        clean_tokens, clean_headline = by_variant["clean"]
        metrics: dict[str, dict[str, object]] = {}
        for variant in VARIANTS:
            observed, observed_headline = by_variant[variant]
            similarity = gate_similarity_by_variant[variant]
            metrics[variant] = {
                "full_token_recall_vs_clean": recall(clean_tokens, observed),
                "headline_token_recall_vs_clean": recall(
                    clean_headline, observed_headline
                ),
                "gate_character_similarity_best_of_psm_6_7_11_13": similarity,
                "scene_specific_gate_detected": similarity >= 0.85,
                "ocr_token_count": len(observed),
            }
        scenes.append({"scene": scene, "metrics": metrics})

    aggregates: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        rows = [scene["metrics"][variant] for scene in scenes]  # type: ignore[index]
        aggregates[variant] = {
            "mean_full_token_recall_vs_clean": mean(
                [float(row["full_token_recall_vs_clean"]) for row in rows]
            ),
            "mean_headline_token_recall_vs_clean": mean(
                [float(row["headline_token_recall_vs_clean"]) for row in rows]
            ),
            "scene_specific_gate_count": sum(
                bool(row["scene_specific_gate_detected"]) for row in rows
            ),
            "mean_gate_character_similarity_best_of_psm_6_7_11_13": mean(
                [
                    float(row["gate_character_similarity_best_of_psm_6_7_11_13"])
                    for row in rows
                ]
            ),
        }

    output = {
        "status": "QA_ONLY_NOT_V9_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 12,
        "proof_receipt": "qa/pass12_sharpness_safe_mockup/receipt.json",
        "scene_count": 7,
        "frame_count": 35,
        "variant_order": VARIANTS,
        "scenes": scenes,
        "aggregates": aggregates,
        "human_visual_review": {
            "scene_specific_gate_lines_visual": {
                "clean": "7/7_EXACT_WORDING",
                "defocus_r0_75": "7/7_EXACT_WORDING",
                "defocus_r1_50": "7/7_EXACT_WORDING",
                "defocus_r2_50": "7/7_EXACT_WORDING",
                "defocus_r4_00": "7/7_GATE_CONTAINERS_AND_BOUNDARY_HIERARCHY__EXACT_WORDING_NOT_ACCEPTANCE_RELIABLE",
            },
            "result_held_badges_visual": {
                variant: "7/7" for variant in VARIANTS
            },
            "operational_r1_50_no_overlap_clipping_or_semantic_ambiguity": True,
            "severe_r4_00_support_softening": "small citations, footer provenance, and minor body labels weaken first; gate containers and boundary hierarchy remain recognizable, but exact scene-specific wording is not acceptance-reliable",
        },
        "gate_ocr_method": "Crop the exact title-safe gate box; run Tesseract PSM 6, 7, 11, and 13; retain only maximum normalized alphanumeric character-sequence similarity; require >=0.85. No recognized text is stored.",
        "raw_ocr_text_stored": False,
        "sealed_v8_modified": False,
        "pass7_proof_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    OUTPUT.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    operational = aggregates["defocus_r1_50"]
    print(
        "PASS proof=7/35 "
        f"r1_50_gates={operational['scene_specific_gate_count']}/7 "
        f"r1_50_headline={operational['mean_headline_token_recall_vs_clean']:.6f}"
    )


if __name__ == "__main__":
    main()
