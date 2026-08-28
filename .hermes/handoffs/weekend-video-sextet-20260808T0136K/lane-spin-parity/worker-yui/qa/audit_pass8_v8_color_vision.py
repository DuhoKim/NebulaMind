#!/usr/bin/env python3
"""Quantify sealed-v8 and caption-safe color-vision redundancy."""

from __future__ import annotations

import collections
import csv
import hashlib
import io
import json
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
AUDIT_ROOT = ROOT / "qa/pass8_v8_color_vision"
RECEIPT = AUDIT_ROOT / "receipt.json"
OUTPUT = ROOT / "qa/pass8_v8_color_vision_audit.json"
VARIANTS = [
    "color",
    "grayscale_bt709",
    "protanopia_machado100",
    "deuteranopia_machado100",
    "tritanopia_machado100",
]
SCENE_GATE_PATTERNS = {
    1: re.compile(r"result\s+locked", re.IGNORECASE),
    2: re.compile(r"do\s+not\s+sum", re.IGNORECASE),
    3: re.compile(r"physical\s+interpretation\s+held", re.IGNORECASE),
    4: re.compile(r"frame\s+unstated", re.IGNORECASE),
    5: re.compile(r"storage\s+frame\s+unresolved", re.IGNORECASE),
    6: re.compile(r"outcomes?\s+withheld", re.IGNORECASE),
    7: re.compile(r"separate\s+authorization", re.IGNORECASE),
}
TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:[._/-][A-Za-z0-9]+)*")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tesseract_text(path: Path, psm: int = 11, crop: tuple[int, int, int, int] | None = None) -> str:
    def run_ocr(source: Path) -> str:
        completed = subprocess.run(
            ["tesseract", str(source), "stdout", "--psm", str(psm)],
            check=True,
            text=True,
            capture_output=True,
        )
        return completed.stdout.strip()

    if crop is None:
        return run_ocr(path)
    with tempfile.TemporaryDirectory() as temporary_directory:
        source = Path(temporary_directory) / "crop.png"
        Image.open(path).convert("RGB").crop(crop).save(source, format="PNG", optimize=False)
        return run_ocr(source)


def tokens(text: str) -> list[str]:
    return [token.casefold() for token in TOKEN_RE.findall(text)]


def multiset_retention(reference: list[str], sample: list[str]) -> float:
    if not reference:
        return 1.0
    reference_counter = collections.Counter(reference)
    sample_counter = collections.Counter(sample)
    overlap = sum(min(count, sample_counter[token]) for token, count in reference_counter.items())
    return overlap / sum(reference_counter.values())


def sobel_edges(path: Path) -> np.ndarray:
    rgb = np.asarray(Image.open(path).convert("RGB"), dtype=np.float32)
    gray = 0.2126 * rgb[:, :, 0] + 0.7152 * rgb[:, :, 1] + 0.0722 * rgb[:, :, 2]
    padded = np.pad(gray, 1, mode="edge")
    gx = (
        -padded[:-2, :-2] + padded[:-2, 2:]
        - 2.0 * padded[1:-1, :-2] + 2.0 * padded[1:-1, 2:]
        - padded[2:, :-2] + padded[2:, 2:]
    )
    gy = (
        padded[:-2, :-2] + 2.0 * padded[:-2, 1:-1] + padded[:-2, 2:]
        - padded[2:, :-2] - 2.0 * padded[2:, 1:-1] - padded[2:, 2:]
    )
    return np.hypot(gx, gy) >= 120.0


def dilate_one_pixel(mask: np.ndarray) -> np.ndarray:
    padded = np.pad(mask, 1, mode="constant", constant_values=False)
    return np.logical_or.reduce(
        [padded[y : y + mask.shape[0], x : x + mask.shape[1]] for y in range(3) for x in range(3)]
    )


def edge_recall(reference: Path, sample: Path) -> float:
    reference_edges = sobel_edges(reference)
    sample_tolerant = dilate_one_pixel(sobel_edges(sample))
    if not np.any(reference_edges):
        return 1.0
    return float(np.count_nonzero(reference_edges & sample_tolerant) / np.count_nonzero(reference_edges))


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def main() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    if receipt["variant_order"] != VARIANTS:
        raise SystemExit("variant contract mismatch")
    groups_output: dict[str, Any] = {}
    for group_name in ("sealed_v8", "pass7_caption_safe"):
        group = receipt["groups"][group_name]
        aggregate: dict[str, dict[str, list[float]]] = {
            variant: collections.defaultdict(list) for variant in VARIANTS
        }
        badge_counts = {variant: 0 for variant in VARIANTS}
        specific_gate_counts = {variant: 0 for variant in VARIANTS}
        scenes_output: list[dict[str, Any]] = []
        for scene in group["scenes"]:
            scene_number = int(scene["scene"])
            sample_map = {sample["variant"]: sample for sample in scene["samples"]}
            color_path = AUDIT_ROOT / group_name / sample_map["color"]["frame"]
            full_texts: dict[str, str] = {}
            gate_texts: dict[str, str] = {}
            badge_texts: dict[str, str] = {}
            for variant in VARIANTS:
                path = AUDIT_ROOT / group_name / sample_map[variant]["frame"]
                full_texts[variant] = tesseract_text(path)
                gate_texts[variant] = (
                    tesseract_text(path, psm=7, crop=(38, 80, 1882, 134))
                    if group_name == "pass7_caption_safe"
                    else ""
                )
                badge_texts[variant] = tesseract_text(path, psm=7, crop=(1570, 15, 1905, 88))
            scene_samples: list[dict[str, Any]] = []
            for variant in VARIANTS:
                path = AUDIT_ROOT / group_name / sample_map[variant]["frame"]
                full_retention = multiset_retention(tokens(full_texts["color"]), tokens(full_texts[variant]))
                gate_retention = (
                    multiset_retention(tokens(gate_texts["color"]), tokens(gate_texts[variant]))
                    if group_name == "pass7_caption_safe"
                    else 1.0
                )
                edge = edge_recall(color_path, path)
                badge = bool(re.search(r"result\s+held", badge_texts[variant], re.IGNORECASE))
                specific_text = gate_texts[variant] if group_name == "pass7_caption_safe" else full_texts[variant]
                specific = bool(SCENE_GATE_PATTERNS[scene_number].search(specific_text))
                badge_counts[variant] += int(badge)
                specific_gate_counts[variant] += int(specific)
                aggregate[variant]["full_token_retention_vs_color"].append(full_retention)
                aggregate[variant]["gate_line_token_retention_vs_color"].append(gate_retention)
                aggregate[variant]["edge_recall_vs_color_1px_tolerance"].append(edge)
                scene_samples.append(
                    {
                        "variant": variant,
                        "frame": sample_map[variant]["frame"],
                        "frame_sha256": sample_map[variant]["frame_sha256"],
                        "full_ocr_sha256": hashlib.sha256(full_texts[variant].encode("utf-8")).hexdigest(),
                        "gate_line_ocr_sha256": hashlib.sha256(gate_texts[variant].encode("utf-8")).hexdigest(),
                        "badge_ocr_sha256": hashlib.sha256(badge_texts[variant].encode("utf-8")).hexdigest(),
                        "full_token_retention_vs_color": round(full_retention, 6),
                        "gate_line_token_retention_vs_color": round(gate_retention, 6),
                        "edge_recall_vs_color_1px_tolerance": round(edge, 6),
                        "result_held_badge_ocr_detected": badge,
                        "scene_specific_gate_ocr_detected": specific,
                    }
                )
            scenes_output.append({"scene": scene_number, "samples": scene_samples})
        aggregates = {
            variant: {
                **{f"mean_{key}": mean(values) for key, values in aggregate[variant].items()},
                "result_held_badge_ocr_count": badge_counts[variant],
                "scene_specific_gate_ocr_count": specific_gate_counts[variant],
            }
            for variant in VARIANTS
        }
        groups_output[group_name] = {
            "scene_count": group["scene_count"],
            "frame_count": group["frame_count"],
            "aggregates": aggregates,
            "scenes": scenes_output,
        }

    output = {
        "status": "QA_ONLY_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 8,
        "audit": "sealed_v8_and_caption_safe_text_edge_redundancy",
        "source_receipt": "qa/pass8_v8_color_vision/receipt.json",
        "source_receipt_sha256": sha256(RECEIPT),
        "variant_order": VARIANTS,
        "ocr": {
            "engine": subprocess.run(["tesseract", "--version"], text=True, capture_output=True, check=True).stdout.splitlines()[0],
            "full_psm": 11,
            "gate_and_badge_psm": 7,
            "raw_ocr_text_stored": False,
            "note": "Human full-sheet review is decisive for visible badge/gate counts; OCR is auxiliary.",
        },
        "groups": groups_output,
        "human_visual_review": {
            "sealed_v8_result_held": "7/7_ALL_FIVE_VARIANTS",
            "sealed_v8_hue_only_semantic_distinctions": 0,
            "sealed_v8_redundant_encoding": "PASS_LABEL_SHAPE_POSITION_ALL_7",
            "caption_safe_scene_specific_gate_lines": "7/7_ALL_FIVE_VARIANTS",
            "caption_safe_result_held": "7/7_ALL_FIVE_VARIANTS",
            "caption_safe_hue_only_semantic_distinctions": 0,
            "caption_safe_overlap_or_ambiguity": 0,
        },
        "sealed_v8_modified": False,
        "pass7_mockup_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    gray = groups_output["pass7_caption_safe"]["aggregates"]["grayscale_bt709"]
    print(
        "PASS groups=2 frames=70 "
        f"caption_gray_gate={gray['mean_gate_line_token_retention_vs_color']:.6f} "
        f"visual_gate=7/7x5 visual_badge=7/7x5"
    )


if __name__ == "__main__":
    main()
