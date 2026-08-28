#!/usr/bin/env python3
"""Measure temporal content stability across pass-4 early/mid/late encoded frames."""

from __future__ import annotations

import csv
import difflib
import hashlib
import io
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageStat

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "qa/pass4_encoded_audit"
RECEIPT = AUDIT / "extraction_receipt.json"
OUT = ROOT / "qa/pass4_temporal_content_audit.json"
OCR_CONFIDENCE_FLOOR = 50


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def token_multiset_similarity(left: str, right: str) -> float:
    left_counts = Counter(left.split())
    right_counts = Counter(right.split())
    total = sum(left_counts.values()) + sum(right_counts.values())
    if total == 0:
        return 1.0
    overlap = sum((left_counts & right_counts).values())
    return 2.0 * overlap / total


def ocr_signature(path: Path) -> dict[str, Any]:
    result = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "11", "tsv"],
        check=True,
        text=True,
        capture_output=True,
    )
    rows = []
    for row in csv.DictReader(io.StringIO(result.stdout), delimiter="\t"):
        text = (row.get("text") or "").strip()
        try:
            confidence = float(row.get("conf") or -1)
        except ValueError:
            confidence = -1
        if not text or confidence < OCR_CONFIDENCE_FLOOR:
            continue
        rows.append(
            {
                "left": int(row["left"]),
                "top": int(row["top"]),
                "width": int(row["width"]),
                "height": int(row["height"]),
                "text": text,
            }
        )
    normalized = " ".join(row["text"].casefold() for row in rows)
    width, height = Image.open(path).size
    margins = {
        "left": min((row["left"] for row in rows), default=width),
        "top": min((row["top"] for row in rows), default=height),
        "right": min(
            (width - row["left"] - row["width"] for row in rows), default=width
        ),
        "bottom": min(
            (height - row["top"] - row["height"] for row in rows), default=height
        ),
    }
    return {
        "normalized_text_sha256": sha256_text(normalized),
        "normalized_text_internal": normalized,
        "recognized_token_count": len(rows),
        "minimum_ocr_box_margins_px": margins,
    }


def image_diff(left_path: Path, right_path: Path) -> dict[str, Any]:
    with Image.open(left_path).convert("RGB") as left, Image.open(right_path).convert(
        "RGB"
    ) as right:
        diff = ImageChops.difference(left, right)
        grayscale = diff.convert("L")
        histogram = grayscale.histogram()
        pixels = left.width * left.height
        fractions = {}
        for threshold in (0, 2, 4, 8, 16, 32):
            changed = sum(histogram[threshold + 1 :])
            fractions[f"gt_{threshold}"] = round(changed / pixels, 9)
        difference_bbox = diff.getbbox()
        return {
            "equal": difference_bbox is None,
            "difference_bbox": list(difference_bbox) if difference_bbox else None,
            "mean_abs_rgb": [round(value, 6) for value in ImageStat.Stat(diff).mean],
            "changed_pixel_fraction": fractions,
        }


def main() -> None:
    receipt = json.loads(RECEIPT.read_text())
    scenes = []
    for scene in receipt["scenes"]:
        by_label = {row["sample"]: row for row in scene["samples"]}
        signatures = {
            label: ocr_signature(AUDIT / row["frame"])
            for label, row in by_label.items()
        }
        normalized = {
            label: signature.pop("normalized_text_internal")
            for label, signature in signatures.items()
        }
        hashes = {
            label: signature["normalized_text_sha256"]
            for label, signature in signatures.items()
        }
        scenes.append(
            {
                "scene": scene["scene"],
                "ocr": signatures,
                "ocr_normalized_text_stable": len(set(hashes.values())) == 1,
                "ocr_min_pairwise_sequence_similarity": round(
                    min(
                        difflib.SequenceMatcher(None, normalized[left], normalized[right]).ratio()
                        for left, right in (("early", "mid"), ("mid", "late"), ("early", "late"))
                    ),
                    6,
                ),
                "ocr_min_pairwise_token_multiset_similarity": round(
                    min(
                        token_multiset_similarity(normalized[left], normalized[right])
                        for left, right in (("early", "mid"), ("mid", "late"), ("early", "late"))
                    ),
                    6,
                ),
                "early_to_mid_diff": image_diff(
                    AUDIT / by_label["early"]["frame"],
                    AUDIT / by_label["mid"]["frame"],
                ),
                "mid_to_late_diff": image_diff(
                    AUDIT / by_label["mid"]["frame"],
                    AUDIT / by_label["late"]["frame"],
                ),
            }
        )
    output = {
        "status": "DETERMINISTIC_TEMPORAL_CONTENT_AUDIT",
        "deepening_pass": 4,
        "candidate_sha256": receipt["candidate_sha256"],
        "scene_count": len(scenes),
        "samples_checked": receipt["sample_count"],
        "ocr_engine": subprocess.run(
            ["tesseract", "--version"], check=True, text=True, capture_output=True
        ).stdout.splitlines()[0],
        "ocr_confidence_floor": OCR_CONFIDENCE_FLOOR,
        "ocr_text_not_reproduced": True,
        "all_scene_ocr_signatures_stable": all(
            row["ocr_normalized_text_stable"] for row in scenes
        ),
        "byte_static_scene_count": sum(
            scene["early_mid_late_byte_identical"] for scene in receipt["scenes"]
        ),
        "scenes": scenes,
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(
        f"PASS scenes={len(scenes)} samples={receipt['sample_count']} "
        f"ocr_stable={sum(row['ocr_normalized_text_stable'] for row in scenes)}/{len(scenes)} "
        f"byte_static={output['byte_static_scene_count']}/{len(scenes)}"
    )


if __name__ == "__main__":
    main()
