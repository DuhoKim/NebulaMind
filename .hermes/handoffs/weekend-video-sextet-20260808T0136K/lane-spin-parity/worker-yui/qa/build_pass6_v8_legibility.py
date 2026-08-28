#!/usr/bin/env python3
"""Derive and OCR-check sealed-v8 frames at four playback resolutions."""

from __future__ import annotations

import hashlib
from io import BytesIO
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
V8_ROOT = ROOT / "proposal_frames/v8"
OUT_ROOT = ROOT / "qa/pass6_v8_legibility"
FRAMES = OUT_ROOT / "frames"
OUT = ROOT / "qa/pass6_v8_legibility_audit.json"
RESOLUTIONS = {
    "1080p": (1920, 1080),
    "720p": (1280, 720),
    "540p": (960, 540),
    "360p": (640, 360),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.casefold())


def phrase_present(tokens: list[str], phrase: list[str]) -> bool:
    return any(
        tokens[index : index + len(phrase)] == phrase
        for index in range(len(tokens) - len(phrase) + 1)
    )


def ocr_image(image: Image.Image, psm: int) -> tuple[list[str], str]:
    buffer = BytesIO()
    image.convert("RGB").save(buffer, format="PNG")
    result = subprocess.run(
        ["tesseract", "stdin", "stdout", "--psm", str(psm)],
        input=buffer.getvalue(),
        check=True,
        capture_output=True,
    )
    text = result.stdout.decode("utf-8", errors="replace")
    tokens = normalize_tokens(text)
    return tokens, hashlib.sha256(text.encode("utf-8")).hexdigest()


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/SFNS.ttf",
    ):
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_contact_sheet(label: str, rows: list[dict[str, Any]], output: Path) -> None:
    tile_w, tile_h, label_h, gap = 640, 360, 38, 12
    cols, grid_rows = 2, 4
    sheet = Image.new(
        "RGB",
        (
            gap + cols * (tile_w + gap),
            gap + grid_rows * (tile_h + label_h + gap),
        ),
        "#07111f",
    )
    draw = ImageDraw.Draw(sheet)
    label_font = font(20)
    for index, row in enumerate(rows):
        col, grid_row = index % cols, index // cols
        x = gap + col * (tile_w + gap)
        y = gap + grid_row * (tile_h + label_h + gap)
        with Image.open(OUT_ROOT / row["frame"]).convert("RGB") as image:
            tile = image.resize((tile_w, tile_h), Image.Resampling.LANCZOS)
            sheet.paste(tile, (x, y))
        state = "badge OCR PASS" if row["result_held_badge_detected"] else "badge OCR MISS"
        draw.text(
            (x, y + tile_h + 6),
            f"S{row['scene']} · {label} · {state}",
            fill="#c8d7ef",
            font=label_font,
        )
    sheet.save(output)


def main() -> None:
    receipt = json.loads(
        (V8_ROOT / "render_receipt.json").read_text(encoding="utf-8")
    )
    inputs = [Path(path) for path in receipt["outputs"]]
    if len(inputs) != 7:
        raise SystemExit("expected seven sealed-v8 inputs")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    for old in FRAMES.glob("*.png"):
        old.unlink()

    scenes = []
    by_resolution: dict[str, list[dict[str, Any]]] = {label: [] for label in RESOLUTIONS}
    for scene_number, input_path in enumerate(inputs, start=1):
        input_hash = sha256(input_path)
        samples = []
        with Image.open(input_path).convert("RGB") as source:
            for label, (width, height) in RESOLUTIONS.items():
                image = source.resize((width, height), Image.Resampling.LANCZOS)
                relative = f"frames/scene_{scene_number:02d}_{label}.png"
                output = OUT_ROOT / relative
                image.save(output)
                full_tokens, full_hash = ocr_image(image, 6)
                badge_crop = image.crop(
                    (int(width * 0.70), 0, width, int(height * 0.16))
                ).resize(
                    (int(width * 0.30) * 4, int(height * 0.16) * 4),
                    Image.Resampling.LANCZOS,
                )
                badge_tokens, badge_hash = ocr_image(badge_crop, 7)
                row = {
                    "scene": scene_number,
                    "resolution": label,
                    "width": width,
                    "height": height,
                    "frame": relative,
                    "frame_sha256": sha256(output),
                    "full_ocr_sha256": full_hash,
                    "badge_crop_ocr_sha256": badge_hash,
                    "full_ocr_token_count": len(full_tokens),
                    "badge_crop_ocr_token_count": len(badge_tokens),
                    "result_held_badge_detected": phrase_present(
                        badge_tokens, ["result", "held"]
                    ),
                    "any_large_boundary_phrase_detected": any(
                        phrase_present(full_tokens, phrase)
                        for phrase in (
                            ["result", "locked"],
                            ["frame", "unstated"],
                            ["outcomes", "withheld"],
                            ["result", "status", "held"],
                        )
                    ),
                }
                samples.append(row)
                by_resolution[label].append(row)
        scenes.append(
            {
                "scene": scene_number,
                "sealed_input": input_path.name,
                "sealed_input_sha256": input_hash,
                "samples": samples,
            }
        )

    contact_sheets = {}
    aggregates = {}
    for label, rows in by_resolution.items():
        relative = f"contact_sheet_{label}.png"
        output = OUT_ROOT / relative
        make_contact_sheet(label, rows, output)
        contact_sheets[label] = {"path": relative, "sha256": sha256(output)}
        aggregates[label] = {
            "result_held_badge_detected": sum(
                row["result_held_badge_detected"] for row in rows
            ),
            "large_boundary_phrase_detected": sum(
                row["any_large_boundary_phrase_detected"] for row in rows
            ),
            "scene_count": len(rows),
        }

    output = {
        "status": "DETERMINISTIC_SEALED_V8_PLAYBACK_RESOLUTION_AUDIT",
        "deepening_pass": 6,
        "sealed_v8_modified": False,
        "storyboard_sha256": receipt["storyboard_sha256"],
        "renderer_sha256": receipt["lane_renderer_sha256"],
        "resolution_order": list(RESOLUTIONS),
        "badge_crop": "rightmost 30% by top 16%, upscaled 4x before psm-7 OCR",
        "ocr_raw_text_stored": False,
        "aggregates": aggregates,
        "contact_sheets": contact_sheets,
        "scenes": scenes,
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(
        "PASS v8=7 badge="
        + " ".join(
            f"{label}:{aggregates[label]['result_held_badge_detected']}/7"
            for label in RESOLUTIONS
        )
    )


if __name__ == "__main__":
    main()
