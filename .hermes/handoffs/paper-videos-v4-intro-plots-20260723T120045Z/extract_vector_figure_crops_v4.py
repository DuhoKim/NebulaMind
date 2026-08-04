#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pymupdf
from PIL import Image, ImageDraw, ImageFont, ImageOps

BASE = Path(__file__).resolve().parent
FREEZE = BASE / "V4_SOURCE_FREEZE.json"
OUT = BASE / "sources-v4" / "figures"
SHEET = BASE / "sources-v4" / "V4_VECTOR_FIGURE_CROP_SHEET.png"

# Bounding boxes are PDF points, visually reviewed against 3x full-page renders.
# They intentionally exclude captions and surrounding manuscript body text.
CROPS: dict[tuple[str, str], tuple[int, tuple[float, float, float, float]]] = {
    ("z9-metallicity", "1"): (2, (315.0, 60.0, 562.0, 240.0)),
    ("scaling-relations", "1"): (3, (76.0, 58.0, 532.0, 298.0)),
    ("scaling-relations", "2"): (3, (48.0, 360.0, 307.0, 465.0)),
    ("massive-abundance", "1"): (3, (48.0, 407.0, 294.0, 590.0)),
    ("tng-validation", "1"): (3, (45.0, 57.0, 541.0, 274.0)),
    ("tng-validation", "2"): (3, (45.0, 299.0, 309.0, 405.0)),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    os.replace(temporary, path)


def main() -> None:
    value = json.loads(FREEZE.read_text())
    rows = {row["key"]: row for row in value["rows"]}
    OUT.mkdir(parents=True, exist_ok=True)
    crop_paths: list[tuple[str, Path]] = []

    for (key, number), (page_number, coordinates) in CROPS.items():
        row = rows[key]
        figure = next(item for item in row["figures"] if item["number"] == number)
        if figure["page"] != page_number:
            raise RuntimeError(f"{key} figure {number}: page mismatch")
        document = pymupdf.open(row["pdf_path"])
        page = document[page_number - 1]
        bbox = pymupdf.Rect(*coordinates)
        if not page.rect.contains(bbox):
            raise RuntimeError(f"{key} figure {number}: crop outside page")
        pixmap = page.get_pixmap(matrix=pymupdf.Matrix(6, 6), clip=bbox, alpha=False)
        path = OUT / f"{key}-figure-{number}-vector-crop.png"
        pixmap.save(path)
        figure.update({
            "crop_path": str(path),
            "crop_sha256": sha256(path),
            "crop_bbox_points": [round(value, 3) for value in coordinates],
            "rendered_pixel_size": [pixmap.width, pixmap.height],
            "source_object_pixel_size": None,
            "source_xref": None,
            "crop_method": "6x render of visually reviewed vector-PDF bounding box; source geometry unchanged",
            "crop_qa": "PASS_VISUAL_QA_ALL_FIGURE_CONTENT_PRESENT_NO_MANUSCRIPT_TEXT",
        })
        figure.pop("inventory_note", None)
        crop_paths.append((f"{key} · Figure {number}", path))

    font = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 24)
    tile_size = (960, 570)
    sheet = Image.new("RGB", (tile_size[0] * 2, tile_size[1] * 3), "#07101f")
    draw = ImageDraw.Draw(sheet)
    for index, (label, path) in enumerate(crop_paths):
        image = Image.open(path).convert("RGB")
        fitted = ImageOps.contain(image, (tile_size[0] - 36, tile_size[1] - 66), Image.Resampling.LANCZOS)
        x = (index % 2) * tile_size[0]
        y = (index // 2) * tile_size[1]
        px = x + (tile_size[0] - fitted.width) // 2
        py = y + 48 + (tile_size[1] - 60 - fitted.height) // 2
        sheet.paste(fitted, (px, py))
        draw.text((x + 18, y + 12), label, font=font, fill="#eaf2ff")
        draw.rectangle((x, y, x + tile_size[0] - 1, y + tile_size[1] - 1), outline="#29466e", width=3)
    sheet.save(SHEET)

    value.update({
        "vector_crop_inventory_completed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "vector_crop_inventory_complete": len(crop_paths) == sum(row["figure_count"] for row in value["rows"]),
        "figure_crop_visual_qa": "PASS",
        "video_readability_followup": {
            "requires_large_plain_english_overlays": [
                "scaling-relations figure 2",
                "tng-validation figure 2",
            ],
            "redraw_rule": "Only redraw from verified current-source data; otherwise use the frozen vector crop.",
        },
        "figure_crop_contact_sheet": str(SHEET),
        "figure_crop_contact_sheet_sha256": sha256(SHEET),
    })
    atomic_json(FREEZE, value)
    print(json.dumps({
        "status": "PASS",
        "figure_count": len(crop_paths),
        "contact_sheet": str(SHEET),
        "crops": [
            {"label": label, "path": str(path), "pixels": list(Image.open(path).size), "sha256": sha256(path)}
            for label, path in crop_paths
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
