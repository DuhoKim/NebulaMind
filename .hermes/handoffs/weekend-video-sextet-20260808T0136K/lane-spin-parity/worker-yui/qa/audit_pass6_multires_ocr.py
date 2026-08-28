#!/usr/bin/env python3
"""Quantify text-hierarchy survival across pass-6 playback resolutions."""

from __future__ import annotations

import collections
import csv
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path
from statistics import mean
from typing import Any

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
AUDIT_ROOT = ROOT / "qa/pass6_resolution_audit"
OUT = ROOT / "qa/pass6_multires_ocr_audit.json"
RESOLUTION_ORDER = ["1080p", "720p", "540p", "360p"]
RESULT_BEARING_SCENES = [7, 9, 10, 11]
CLOSE_SCENE = 16


def normalize_token(value: str) -> str:
    return "".join(re.findall(r"[a-z0-9]+", value.casefold()))


def multiset_retention(reference: list[str], observed: list[str]) -> float:
    reference_counts = collections.Counter(reference)
    if not reference_counts:
        return 1.0
    observed_counts = collections.Counter(observed)
    retained = sum((reference_counts & observed_counts).values())
    return round(retained / sum(reference_counts.values()), 6)


def token_hash(tokens: list[str]) -> str:
    payload = "\n".join(tokens).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def phrase_present(tokens: list[str], phrase: list[str]) -> bool:
    return any(
        tokens[index : index + len(phrase)] == phrase
        for index in range(len(tokens) - len(phrase) + 1)
    )


def ocr_frame(path: Path) -> dict[str, Any]:
    with Image.open(path) as image:
        width, height = image.size
    result = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "6", "tsv"],
        check=True,
        text=True,
        capture_output=True,
    )
    rows = csv.DictReader(io.StringIO(result.stdout), delimiter="\t")
    full: list[str] = []
    headline: list[str] = []
    support: list[str] = []
    numeric = 0
    for row in rows:
        raw = row.get("text", "")
        try:
            confidence = float(row.get("conf", "-1"))
        except (TypeError, ValueError):
            continue
        token = normalize_token(raw)
        if confidence < 30 or not token:
            continue
        full.append(token)
        if any(character.isdigit() for character in token):
            numeric += 1
        centre_y = (
            int(row.get("top", "0")) + int(row.get("height", "0")) / 2
        ) / height
        if centre_y <= 0.30:
            headline.append(token)
        if centre_y >= 0.65:
            support.append(token)
    searchable = " ".join(full)
    return {
        "width": width,
        "height": height,
        "token_count": len(full),
        "headline_token_count": len(headline),
        "support_token_count": len(support),
        "numeric_token_count": numeric,
        "token_sequence_sha256": token_hash(full),
        "headline_token_sequence_sha256": token_hash(headline),
        "support_token_sequence_sha256": token_hash(support),
        "structural_gate_detected": {
            "result_held": phrase_present(full, ["result", "held"]),
            "frame_unstated": phrase_present(full, ["frame", "unstated"]),
            "outcomes_withheld": phrase_present(full, ["outcomes", "withheld"]),
        },
        "_tokens": full,
        "_headline_tokens": headline,
        "_support_tokens": support,
    }


def main() -> None:
    receipt = json.loads(
        (AUDIT_ROOT / "extraction_receipt.json").read_text(encoding="utf-8")
    )
    scenes = []
    for scene in receipt["scenes"]:
        raw_by_resolution: dict[str, dict[str, Any]] = {}
        for sample in scene["samples"]:
            raw_by_resolution[sample["resolution"]] = ocr_frame(
                AUDIT_ROOT / sample["frame"]
            )
        baseline = raw_by_resolution["1080p"]
        samples = []
        for label in RESOLUTION_ORDER:
            raw = raw_by_resolution[label]
            sample = {
                key: value for key, value in raw.items() if not key.startswith("_")
            }
            sample["resolution"] = label
            sample["full_token_retention_vs_1080p"] = multiset_retention(
                baseline["_tokens"], raw["_tokens"]
            )
            sample["headline_token_retention_vs_1080p"] = multiset_retention(
                baseline["_headline_tokens"], raw["_headline_tokens"]
            )
            sample["support_token_retention_vs_1080p"] = multiset_retention(
                baseline["_support_tokens"], raw["_support_tokens"]
            )
            samples.append(sample)
        scenes.append(
            {
                "scene": scene["scene"],
                "result_bearing": scene["scene"] in RESULT_BEARING_SCENES,
                "close_scene": scene["scene"] == CLOSE_SCENE,
                "samples": samples,
            }
        )

    aggregates = {}
    for label in RESOLUTION_ORDER:
        rows = [
            next(sample for sample in scene["samples"] if sample["resolution"] == label)
            for scene in scenes
        ]
        aggregates[label] = {
            "mean_full_token_retention_vs_1080p": round(
                mean(row["full_token_retention_vs_1080p"] for row in rows), 6
            ),
            "mean_headline_token_retention_vs_1080p": round(
                mean(row["headline_token_retention_vs_1080p"] for row in rows), 6
            ),
            "mean_support_token_retention_vs_1080p": round(
                mean(row["support_token_retention_vs_1080p"] for row in rows), 6
            ),
            "scenes_with_any_structural_gate": sum(
                any(row["structural_gate_detected"].values()) for row in rows
            ),
            "mean_numeric_token_count": round(
                mean(row["numeric_token_count"] for row in rows), 6
            ),
        }

    critical_resolution_metrics = {}
    for label in RESOLUTION_ORDER:
        rows = [
            next(sample for sample in scene["samples"] if sample["resolution"] == label)
            for scene in scenes
            if scene["result_bearing"] or scene["close_scene"]
        ]
        critical_resolution_metrics[label] = {
            "scenes": [*RESULT_BEARING_SCENES, CLOSE_SCENE],
            "mean_full_token_retention_vs_1080p": round(
                mean(row["full_token_retention_vs_1080p"] for row in rows), 6
            ),
            "mean_headline_token_retention_vs_1080p": round(
                mean(row["headline_token_retention_vs_1080p"] for row in rows), 6
            ),
            "mean_support_token_retention_vs_1080p": round(
                mean(row["support_token_retention_vs_1080p"] for row in rows), 6
            ),
            "structural_gate_scene_count": sum(
                any(row["structural_gate_detected"].values()) for row in rows
            ),
        }

    output = {
        "status": "DETERMINISTIC_MULTI_RESOLUTION_OCR_HIERARCHY_AUDIT",
        "deepening_pass": 6,
        "candidate_sha256": receipt["candidate_sha256"],
        "scene_count": receipt["scene_count"],
        "frame_count": receipt["frame_count"],
        "resolutions": RESOLUTION_ORDER,
        "ocr": {
            "engine": subprocess.run(
                ["tesseract", "--version"],
                check=True,
                text=True,
                capture_output=True,
            ).stdout.splitlines()[0],
            "page_segmentation_mode": 6,
            "minimum_confidence": 30,
            "normalization": "casefolded ASCII alphanumeric tokens",
            "raw_ocr_text_stored": False,
        },
        "region_definition": {
            "headline": "token centre y <= 30% frame height",
            "support": "token centre y >= 65% frame height",
        },
        "result_bearing_scenes": RESULT_BEARING_SCENES,
        "close_scene": CLOSE_SCENE,
        "aggregates": aggregates,
        "critical_resolution_metrics": critical_resolution_metrics,
        "scenes": scenes,
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    low = aggregates["360p"]
    critical = critical_resolution_metrics["360p"]
    print(
        "PASS scenes=16 frames=64 360p_full="
        f"{low['mean_full_token_retention_vs_1080p']} headline="
        f"{low['mean_headline_token_retention_vs_1080p']} support="
        f"{low['mean_support_token_retention_vs_1080p']} critical_support="
        f"{critical['mean_support_token_retention_vs_1080p']} gates="
        f"{low['scenes_with_any_structural_gate']}"
    )


if __name__ == "__main__":
    main()
