#!/usr/bin/env python3
"""Quantify text/edge survival under monochrome and CVD stress transforms."""

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

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
AUDIT_ROOT = ROOT / "qa/pass8_color_vision_audit"
RECEIPT = AUDIT_ROOT / "extraction_receipt.json"
PASS7_RECEIPT = ROOT / "qa/pass7_obstruction_audit/extraction_receipt.json"
OUTPUT = ROOT / "qa/pass8_color_vision_quantitative_audit.json"
VARIANTS = [
    "color",
    "grayscale_bt709",
    "protanopia_machado100",
    "deuteranopia_machado100",
    "tritanopia_machado100",
]
CRITICAL_SCENES = [5, 7, 9, 10, 11]
HELD_CRITICAL_SCENES = [7, 9, 10, 11, 16]
GATE_PATTERNS = {
    "result_held": re.compile(r"\bresult\s+held\b", re.IGNORECASE),
    "frame_unstated": re.compile(r"\bframe\s+unstated\b", re.IGNORECASE),
    "outcomes_withheld": re.compile(r"\boutcomes?\s+withheld\b", re.IGNORECASE),
    "no_outcome_shown": re.compile(r"\bno\s+outcome\s+shown\b", re.IGNORECASE),
    "result_locked": re.compile(r"\bresult\s+locked\b", re.IGNORECASE),
}
TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:[._/-][A-Za-z0-9]+)*")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tesseract_tsv(path: Path) -> list[dict[str, Any]]:
    completed = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "11", "tsv"],
        check=True,
        text=True,
        capture_output=True,
    )
    rows: list[dict[str, Any]] = []
    for row in csv.DictReader(io.StringIO(completed.stdout), delimiter="\t"):
        text = (row.get("text") or "").strip()
        try:
            confidence = float(row.get("conf") or -1)
            left = int(row.get("left") or 0)
            top = int(row.get("top") or 0)
            width = int(row.get("width") or 0)
            height = int(row.get("height") or 0)
        except ValueError:
            continue
        if text and confidence >= 20:
            rows.append(
                {
                    "text": text,
                    "confidence": confidence,
                    "left": left,
                    "top": top,
                    "width": width,
                    "height": height,
                }
            )
    return rows


def normalize_tokens(rows: list[dict[str, Any]], height: int, region: str) -> list[str]:
    tokens: list[str] = []
    for row in rows:
        center_y = (row["top"] + row["height"] / 2.0) / height
        keep = (
            region == "full"
            or (region == "headline" and center_y <= 0.30)
            or (region == "middle" and 0.30 < center_y < 0.65)
            or (region == "lower_support" and center_y >= 0.65)
        )
        if not keep:
            continue
        tokens.extend(token.casefold() for token in TOKEN_RE.findall(row["text"]))
    return tokens


def multiset_retention(reference: list[str], sample: list[str]) -> float:
    if not reference:
        return 1.0
    reference_counter = collections.Counter(reference)
    sample_counter = collections.Counter(sample)
    overlap = sum(min(count, sample_counter[token]) for token, count in reference_counter.items())
    return overlap / sum(reference_counter.values())


def numeric_retention(reference: list[str], sample: list[str]) -> float:
    return multiset_retention(
        [token for token in reference if any(char.isdigit() for char in token)],
        [token for token in sample if any(char.isdigit() for char in token)],
    )


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


def edge_recall(reference_path: Path, sample_path: Path) -> float:
    reference_edges = sobel_edges(reference_path)
    sample_edges = sobel_edges(sample_path)
    if not np.any(reference_edges):
        return 1.0
    sample_tolerant = dilate_one_pixel(sample_edges)
    return float(np.count_nonzero(reference_edges & sample_tolerant) / np.count_nonzero(reference_edges))


def chroma_retention(reference_path: Path, sample_path: Path) -> tuple[float, float]:
    reference = np.asarray(Image.open(reference_path).convert("RGB"), dtype=np.float32)
    sample = np.asarray(Image.open(sample_path).convert("RGB"), dtype=np.float32)
    reference_chroma = reference.max(axis=2) - reference.min(axis=2)
    sample_chroma = sample.max(axis=2) - sample.min(axis=2)
    mask = reference_chroma >= 30.0
    if not np.any(mask):
        return 1.0, 0.0
    retention = float(sample_chroma[mask].mean() / reference_chroma[mask].mean())
    return retention, float(np.count_nonzero(mask) / mask.size)


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def main() -> None:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    pass7_receipt = json.loads(PASS7_RECEIPT.read_text(encoding="utf-8"))
    if receipt["variants"] != VARIANTS:
        raise SystemExit("variant contract mismatch")
    scenes: list[dict[str, Any]] = []
    aggregate_values: dict[str, dict[str, list[float]]] = {
        variant: collections.defaultdict(list) for variant in VARIANTS
    }
    gate_counts = {variant: 0 for variant in VARIANTS}
    critical_values: dict[str, dict[str, list[float]]] = {
        variant: collections.defaultdict(list) for variant in VARIANTS
    }
    held_gate_counts = {variant: 0 for variant in VARIANTS}

    for scene in receipt["scenes"]:
        scene_number = int(scene["scene"])
        sample_map = {sample["variant"]: sample for sample in scene["samples"]}
        color_path = AUDIT_ROOT / sample_map["color"]["frame"]
        ocr_rows: dict[str, list[dict[str, Any]]] = {}
        tokens: dict[str, dict[str, list[str]]] = {}
        for variant in VARIANTS:
            frame = AUDIT_ROOT / sample_map[variant]["frame"]
            rows = tesseract_tsv(frame)
            ocr_rows[variant] = rows
            tokens[variant] = {
                region: normalize_tokens(rows, int(sample_map[variant]["height"]), region)
                for region in ("full", "headline", "middle", "lower_support")
            }

        scene_samples: list[dict[str, Any]] = []
        for variant in VARIANTS:
            frame = AUDIT_ROOT / sample_map[variant]["frame"]
            row_tokens = tokens[variant]
            full_text = " ".join(row["text"] for row in ocr_rows[variant])
            gate_map = {key: bool(pattern.search(full_text)) for key, pattern in GATE_PATTERNS.items()}
            has_gate = any(gate_map.values())
            gate_counts[variant] += int(has_gate)
            if scene_number in HELD_CRITICAL_SCENES:
                held_gate_counts[variant] += int(has_gate)
            edge = edge_recall(color_path, frame)
            chroma, saturated_fraction = chroma_retention(color_path, frame)
            metrics = {
                "full_token_retention_vs_color": round(multiset_retention(tokens["color"]["full"], row_tokens["full"]), 6),
                "headline_token_retention_vs_color": round(multiset_retention(tokens["color"]["headline"], row_tokens["headline"]), 6),
                "middle_token_retention_vs_color": round(multiset_retention(tokens["color"]["middle"], row_tokens["middle"]), 6),
                "lower_support_token_retention_vs_color": round(multiset_retention(tokens["color"]["lower_support"], row_tokens["lower_support"]), 6),
                "numeric_token_retention_vs_color": round(numeric_retention(tokens["color"]["full"], row_tokens["full"]), 6),
                "edge_recall_vs_color_1px_tolerance": round(edge, 6),
                "chroma_retention_on_color_saturated_pixels": round(chroma, 6),
                "color_saturated_pixel_fraction": round(saturated_fraction, 6),
            }
            for key, value in metrics.items():
                aggregate_values[variant][key].append(value)
                if scene_number in CRITICAL_SCENES:
                    critical_values[variant][key].append(value)
            scene_samples.append(
                {
                    "variant": variant,
                    "frame": sample_map[variant]["frame"],
                    "frame_sha256": sample_map[variant]["frame_sha256"],
                    "ocr_text_sha256": hashlib.sha256(full_text.encode("utf-8")).hexdigest(),
                    "ocr_token_count": len(row_tokens["full"]),
                    **metrics,
                    "structural_gate_detected": has_gate,
                    "structural_gate_phrases": gate_map,
                }
            )
        scenes.append({"scene": scene_number, "samples": scene_samples})

    aggregates: dict[str, Any] = {}
    critical_aggregates: dict[str, Any] = {}
    for variant in VARIANTS:
        aggregates[variant] = {
            **{f"mean_{key}": mean(values) for key, values in aggregate_values[variant].items()},
            "scenes_with_any_structural_gate": gate_counts[variant],
        }
        critical_aggregates[variant] = {
            "scenes": CRITICAL_SCENES,
            **{f"mean_{key}": mean(values) for key, values in critical_values[variant].items()},
        }
    held_critical = {
        variant: {
            "scenes": HELD_CRITICAL_SCENES,
            "structural_gate_scene_count": held_gate_counts[variant],
        }
        for variant in VARIANTS
    }

    pass7_clean_hashes = {
        int(scene["scene"]): next(
            sample["frame_sha256"] for sample in scene["samples"] if sample["variant"] == "clean"
        )
        for scene in pass7_receipt["scenes"]
    }
    pass8_color_hashes = {
        int(scene["scene"]): next(
            sample["frame_sha256"] for sample in scene["samples"] if sample["variant"] == "color"
        )
        for scene in receipt["scenes"]
    }
    output = {
        "status": "QA_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 8,
        "audit": "monochrome_and_color_vision_text_edge_chroma",
        "candidate_sha256": receipt["candidate_sha256"],
        "extraction_receipt": "qa/pass8_color_vision_audit/extraction_receipt.json",
        "extraction_receipt_sha256": sha256(RECEIPT),
        "scene_count": receipt["scene_count"],
        "frame_count": receipt["frame_count"],
        "variant_order": VARIANTS,
        "custody_reproduction": {
            "pass7_receipt": "qa/pass7_obstruction_audit/extraction_receipt.json",
            "pass7_receipt_sha256": sha256(PASS7_RECEIPT),
            "cut_times_exact_pass7": receipt["detected_cut_times_seconds"]
            == pass7_receipt["detected_cut_times_seconds"],
            "color_midpoints_byte_identical_to_pass7_clean": sum(
                pass8_color_hashes[scene] == pass7_clean_hashes[scene] for scene in range(1, 17)
            ),
        },
        "critical_plot_scenes": CRITICAL_SCENES,
        "held_critical_scenes": HELD_CRITICAL_SCENES,
        "ocr": {
            "engine": subprocess.run(["tesseract", "--version"], text=True, capture_output=True, check=True).stdout.splitlines()[0],
            "psm": 11,
            "confidence_floor": 20,
            "raw_ocr_text_stored": False,
            "token_multiset_retention_note": "Values compare transformed-frame OCR tokens with exact scene color-frame tokens.",
        },
        "edge_metric": "Sobel magnitude >=120 reference-edge recall with one-pixel dilation tolerance",
        "chroma_metric": "Mean RGB max-minus-min retention on baseline pixels with chroma >=30",
        "aggregates": aggregates,
        "critical_plot_scene_aggregates": critical_aggregates,
        "held_critical_gate_counts": held_critical,
        "scenes": scenes,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "PASS "
        f"scenes={output['scene_count']} frames={output['frame_count']} "
        f"gray_full={aggregates['grayscale_bt709']['mean_full_token_retention_vs_color']:.6f} "
        f"gray_edge={aggregates['grayscale_bt709']['mean_edge_recall_vs_color_1px_tolerance']:.6f} "
        f"held_gates={sum(row['structural_gate_scene_count'] for row in held_critical.values())}"
    )


if __name__ == "__main__":
    main()
