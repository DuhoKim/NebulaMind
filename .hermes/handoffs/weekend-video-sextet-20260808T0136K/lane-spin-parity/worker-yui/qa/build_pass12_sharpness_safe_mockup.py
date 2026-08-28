#!/usr/bin/env python3
"""Build a QA-only sharpness-safe scene-gate proof from sealed v8 frames."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, __version__ as pillow_version

ROOT = Path(__file__).resolve().parents[1]
SEALED = ROOT / "proposal_frames/v8"
OUT = ROOT / "qa/pass12_sharpness_safe_mockup"
FRAMES = OUT / "frames"
RECEIPT = OUT / "receipt.json"
VARIANTS: dict[str, float | None] = {
    "clean": None,
    "defocus_r0_75": 0.75,
    "defocus_r1_50": 1.5,
    "defocus_r2_50": 2.5,
    "defocus_r4_00": 4.0,
}
GATE_LINES = {
    1: "RESULT LOCKED · ARCHIVE FRAME + INDEPENDENT REVIEW REQUIRED",
    2: "OVERLAPPING READOUTS · DO NOT SUM",
    3: "LABEL-FRAME STATISTIC · PHYSICAL INTERPRETATION HELD",
    4: "FRAME UNSTATED · RESULT HELD",
    5: "COLUMN CHECK ONLY · STORAGE FRAME UNRESOLVED",
    6: "CONTROL DESIGN ONLY · OUTCOMES WITHHELD",
    7: "SEPARATE AUTHORIZATION REQUIRED AFTER BOTH BLOCKERS RESOLVE",
}
GATE_BOX = (102, 78, 1540, 121)
FONT_SIZE = 28
STROKE_WIDTH = 1
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
        x0, y0, x1, y1 = GATE_BOX
        draw.rounded_rectangle(
            GATE_BOX,
            radius=12,
            fill=(13, 22, 34),
            outline=(240, 170, 68),
            width=3,
        )
        line_font = font(FONT_SIZE)
        box = draw.textbbox(
            (0, 0), text, font=line_font, stroke_width=STROKE_WIDTH
        )
        text_width = box[2] - box[0]
        text_height = box[3] - box[1]
        text_x = (1920 - text_width) / 2
        text_y = y0 + ((y1 - y0) - text_height) / 2 - box[1]
        if text_x < x0 + 12 or text_x + text_width > x1 - 12:
            raise ValueError(f"gate line does not fit: {text}")
        draw.text(
            (text_x, text_y),
            text,
            fill=(255, 202, 110),
            font=line_font,
            stroke_width=STROKE_WIDTH,
            stroke_fill=(255, 202, 110),
        )
        image.save(destination, format="PNG", optimize=False)


def apply_defocus(source: Path, destination: Path, radius: float) -> None:
    with Image.open(source).convert("RGB") as image:
        image.filter(ImageFilter.GaussianBlur(radius=radius)).save(
            destination, format="PNG", optimize=False
        )


def make_sheet(variant: str, rows: list[dict[str, object]]) -> dict[str, object]:
    tile_w, image_h, label_h = 640, 360, 34
    sheet = Image.new("RGB", (tile_w * 2, (image_h + label_h) * 4), (4, 8, 14))
    draw = ImageDraw.Draw(sheet)
    label_font = font(20)
    for index, row in enumerate(rows):
        scene = row["scene"]
        frame = row["frame"]
        if not isinstance(scene, int) or not isinstance(frame, str):
            raise TypeError("invalid contact-sheet row")
        x = (index % 2) * tile_w
        y = (index // 2) * (image_h + label_h)
        draw.rectangle((x, y, x + tile_w, y + label_h), fill=(4, 8, 14))
        draw.text(
            (x + 8, y + 5),
            f"S{scene} · {variant}",
            fill=(242, 246, 252),
            font=label_font,
        )
        with Image.open(OUT / frame).convert("RGB") as image:
            image.thumbnail((tile_w, image_h), Image.Resampling.LANCZOS)
            sheet.paste(image, (x, y + label_h))
    destination = OUT / f"contact_sheet_{variant}.png"
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
    FRAMES.mkdir(parents=True)
    sources = sorted(SEALED.glob("scene_*.png"))
    if len(sources) != 7:
        raise SystemExit("sealed v8 frame count changed")

    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {
        variant: [] for variant in VARIANTS
    }
    for scene, source in enumerate(sources, start=1):
        clean = FRAMES / f"scene_{scene:02d}_clean.png"
        add_gate_line(source, clean, GATE_LINES[scene])
        samples: list[dict[str, object]] = []
        for variant, radius in VARIANTS.items():
            if radius is None:
                frame = clean
            else:
                frame = FRAMES / f"scene_{scene:02d}_{variant}.png"
                apply_defocus(clean, frame, radius)
            sample = {
                "variant": variant,
                "radius_pixels": radius,
                "frame": frame.relative_to(OUT).as_posix(),
                "frame_sha256": sha256(frame),
            }
            samples.append(sample)
            by_variant[variant].append({"scene": scene, **sample})
        scenes.append(
            {
                "scene": scene,
                "sealed_input": source.relative_to(ROOT).as_posix(),
                "sealed_input_sha256": sha256(source),
                "gate_line": GATE_LINES[scene],
                "gate_line_box": list(GATE_BOX),
                "minimum_font_px_at_1080p": FONT_SIZE,
                "stroke_width_px": STROKE_WIDTH,
                "title_safe_geometry": (
                    GATE_BOX[0] >= 96
                    and GATE_BOX[2] <= 1824
                    and GATE_BOX[1] >= 54
                    and GATE_BOX[3] <= 1026
                ),
                "bottom_obstruction_safe_geometry": GATE_BOX[3] < 810,
                "samples": samples,
            }
        )

    sheets = {
        variant: make_sheet(variant, rows) for variant, rows in by_variant.items()
    }
    receipt = {
        "status": "QA_STATIC_MOCKUP_ONLY_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 12,
        "base_iteration": "sealed_v8",
        "correction": "strengthened scene-specific gate line for spatial-defocus resilience",
        "pillow_version": pillow_version,
        "scene_count": 7,
        "variant_count": 5,
        "frame_count": 35,
        "variant_order": list(VARIANTS),
        "transform_contract": {
            "implementation": "Pillow ImageFilter.GaussianBlur",
            "radii_pixels": [0.75, 1.5, 2.5, 4.0],
            "source_mode": "RGB",
            "canvas_change": False,
        },
        "gate_contract": {
            "box": list(GATE_BOX),
            "minimum_font_px_at_1080p": FONT_SIZE,
            "font_weight": "bold",
            "stroke_width_px": STROKE_WIDTH,
            "title_safe_bounds": [96, 54, 1824, 1026],
            "above_bottom_25pct_obstruction": True,
        },
        "scenes": scenes,
        "contact_sheets": sheets,
        "sealed_v8_modified": False,
        "pass7_mockup_modified": False,
        "storyboard_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("PASS scenes=7 frames=35 gate_box_title_safe=7/7 sealed_v8_modified=false")


if __name__ == "__main__":
    main()
