#!/usr/bin/env python3
"""Build a QA-only caption-safe gate-line mockup from sealed v8 frames."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SEALED = ROOT / "proposal_frames/v8"
OUT = ROOT / "qa/pass7_caption_safe_mockup"
FRAMES = OUT / "frames"
RECEIPT = OUT / "receipt.json"
GATE_LINES = {
    1: "RESULT LOCKED · ARCHIVE FRAME + INDEPENDENT REVIEW REQUIRED",
    2: "OVERLAPPING READOUTS · DO NOT SUM",
    3: "LABEL-FRAME STATISTIC · PHYSICAL INTERPRETATION HELD",
    4: "FRAME UNSTATED · RESULT HELD",
    5: "COLUMN CHECK ONLY · STORAGE FRAME UNRESOLVED",
    6: "CONTROL DESIGN ONLY · OUTCOMES WITHHELD",
    7: "SEPARATE AUTHORIZATION REQUIRED AFTER BOTH BLOCKERS RESOLVE",
}
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def add_gate_line(source: Path, destination: Path, text: str) -> None:
    with Image.open(source).convert("RGB") as image:
        draw = ImageDraw.Draw(image)
        x0, y0, x1, y1 = 38, 83, 1882, 129
        draw.rounded_rectangle(
            (x0, y0, x1, y1),
            radius=12,
            fill=(13, 22, 34),
            outline=(240, 170, 68),
            width=2,
        )
        line_font = font(25)
        box = draw.textbbox((0, 0), text, font=line_font)
        text_width = box[2] - box[0]
        draw.text(
            ((1920 - text_width) / 2, y0 + 8),
            text,
            fill=(255, 193, 92),
            font=line_font,
        )
        image.save(destination, format="PNG", optimize=False)


def mask_bottom_25(source: Path, destination: Path) -> None:
    with Image.open(source).convert("RGB") as image:
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 810, 1920, 1080), fill=(4, 8, 14))
        image.save(destination, format="PNG", optimize=False)


def make_sheet(label: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    tile_w, tile_h = 480, 270
    sheet = Image.new("RGB", (tile_w * 4, tile_h * 2), (4, 8, 14))
    draw = ImageDraw.Draw(sheet)
    label_font = font(22)
    for index, row in enumerate(rows):
        with Image.open(OUT / row["frame"]).convert("RGB") as image:
            image.thumbnail((tile_w, tile_h), Image.Resampling.LANCZOS)
            x = (index % 4) * tile_w
            y = (index // 4) * tile_h
            sheet.paste(image, (x, y))
        label_y = y + tile_h - 28
        draw.rectangle((x, label_y, x + 275, label_y + 28), fill=(4, 8, 14))
        draw.text((x + 8, label_y + 3), f"S{row['scene']:02d} · {label}", fill=(242, 246, 252), font=label_font)
    destination = OUT / f"contact_sheet_{label}.png"
    sheet.save(destination, format="PNG", optimize=False)
    return {
        "path": destination.relative_to(OUT).as_posix(),
        "sha256": sha256(destination),
        "width": sheet.width,
        "height": sheet.height,
    }


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    FRAMES.mkdir(parents=True, exist_ok=True)
    sources = sorted(SEALED.glob("scene_*.png"))
    if len(sources) != 7:
        raise SystemExit("sealed v8 frame count changed")
    scenes: list[dict[str, Any]] = []
    clean_rows: list[dict[str, Any]] = []
    masked_rows: list[dict[str, Any]] = []
    for scene_number, source in enumerate(sources, start=1):
        clean = FRAMES / f"scene_{scene_number:02d}_caption_safe.png"
        masked = FRAMES / f"scene_{scene_number:02d}_caption_safe_player_ui_25pct.png"
        add_gate_line(source, clean, GATE_LINES[scene_number])
        mask_bottom_25(clean, masked)
        with Image.open(clean) as clean_image, Image.open(masked) as masked_image:
            if clean_image.size != (1920, 1080) or masked_image.size != (1920, 1080):
                raise SystemExit("mockup dimensions changed")
            top_clean = clean_image.convert("RGB").crop((0, 0, 1920, 810))
            top_masked = masked_image.convert("RGB").crop((0, 0, 1920, 810))
            top_identical = hashlib.sha256(top_clean.tobytes()).hexdigest() == hashlib.sha256(top_masked.tobytes()).hexdigest()
        clean_row = {
            "scene": scene_number,
            "frame": clean.relative_to(OUT).as_posix(),
            "sha256": sha256(clean),
        }
        masked_row = {
            "scene": scene_number,
            "frame": masked.relative_to(OUT).as_posix(),
            "sha256": sha256(masked),
        }
        clean_rows.append(clean_row)
        masked_rows.append(masked_row)
        scenes.append(
            {
                "scene": scene_number,
                "sealed_input": source.name,
                "sealed_input_sha256": sha256(source),
                "gate_line": GATE_LINES[scene_number],
                "gate_line_box": [38, 83, 1882, 129],
                "gate_line_max_y_fraction": round(129 / 1080, 6),
                "clean": clean_row,
                "player_ui_25pct": masked_row,
                "top_75pct_pixel_identical_clean_to_masked": top_identical,
            }
        )
    sheets = {
        "caption_safe": make_sheet("caption_safe", clean_rows),
        "caption_safe_player_ui_25pct": make_sheet("caption_safe_player_ui_25pct", masked_rows),
    }
    receipt = {
        "status": "QA_STATIC_MOCKUP_ONLY_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 7,
        "base_iteration": "sealed_v8",
        "sealed_v8_modified": False,
        "storyboard_modified": False,
        "frame_count": 14,
        "scene_count": 7,
        "semantic_correction": "scene-specific gate line above bottom-25-percent obstruction zone",
        "protected_region": "gate-line bottom y=129/1080=0.119444",
        "scenes": scenes,
        "contact_sheets": sheets,
        "tts_invoked": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS scenes=7 frames=14 top75_identity=7/7 sealed_v8_modified=false")


if __name__ == "__main__":
    main()
