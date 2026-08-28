#!/usr/bin/env python3
"""Build deterministic shadow-floor derivatives for method-only frame groups."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass14_v8_shadow_floor"
VARIANTS: dict[str, int | None] = {
    "clean": None,
    "shadow_floor_08": 8,
    "shadow_floor_16": 16,
    "shadow_floor_32": 32,
    "shadow_floor_48": 48,
}
GROUPS = {
    "sealed_v8": {
        "source_receipt": ROOT / "proposal_frames/v8/render_receipt.json",
        "frames": [
            ROOT / "proposal_frames/v8" / f"scene_{scene:02d}_s{scene}.png"
            for scene in range(1, 8)
        ],
    },
    "pass7_caption_safe": {
        "source_receipt": ROOT / "qa/pass7_caption_safe_mockup/receipt.json",
        "frames": [
            ROOT
            / "qa/pass7_caption_safe_mockup/frames"
            / f"scene_{scene:02d}_caption_safe.png"
            for scene in range(1, 8)
        ],
    },
    "pass12_sharpness_safe": {
        "source_receipt": ROOT / "qa/pass12_sharpness_safe_mockup/receipt.json",
        "frames": [
            ROOT
            / "qa/pass12_sharpness_safe_mockup/frames"
            / f"scene_{scene:02d}_clean.png"
            for scene in range(1, 8)
        ],
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integer_luma(values: np.ndarray) -> np.ndarray:
    data = values.astype(np.uint32)
    return ((54 * data[:, :, 0] + 183 * data[:, :, 1] + 19 * data[:, :, 2] + 128) // 256).astype(np.uint16)


def shadow_floor(image: Image.Image, floor: int) -> Image.Image:
    if not 0 < floor < 255:
        raise ValueError("shadow floor must be between 1 and 254")
    values = np.asarray(image.convert("RGB"), dtype=np.uint8)
    lum = integer_luma(values).astype(np.uint32)
    numerator = np.maximum(lum.astype(np.int32) - floor, 0).astype(np.uint32) * 255
    remapped = (numerator + (255 - floor) // 2) // (255 - floor)
    output = np.zeros_like(values, dtype=np.uint8)
    nonzero = lum > 0
    for channel in range(3):
        scaled = np.zeros_like(lum, dtype=np.uint32)
        scaled[nonzero] = (
            values[:, :, channel].astype(np.uint32)[nonzero] * remapped[nonzero]
            + lum[nonzero] // 2
        ) // lum[nonzero]
        output[:, :, channel] = np.clip(scaled, 0, 255).astype(np.uint8)
    return Image.fromarray(output)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def contact_sheet(paths: list[Path], labels: list[str], output: Path) -> None:
    thumb_w, thumb_h, label_h = 640, 360, 34
    columns = 2
    rows = (len(paths) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * thumb_w, rows * (thumb_h + label_h)), (5, 9, 15))
    draw = ImageDraw.Draw(sheet)
    label_font = font(18)
    for index, (path, label) in enumerate(zip(paths, labels)):
        with Image.open(path).convert("RGB") as image:
            thumb = image.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = (index % columns) * thumb_w
        y = (index // columns) * (thumb_h + label_h)
        sheet.paste(thumb, (x, y + label_h))
        draw.text((x + 8, y + 7), label, fill=(240, 244, 250), font=label_font)
    sheet.save(output, format="PNG", optimize=False)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    receipt_groups: dict[str, object] = {}
    total_frames = 0

    for group_name, config in GROUPS.items():
        group_root = OUT / group_name
        (group_root / "frames").mkdir(parents=True)
        source_receipt = config["source_receipt"]
        sources = config["frames"]
        if not isinstance(source_receipt, Path) or not isinstance(sources, list):
            raise TypeError("group configuration")
        scene_rows: list[dict[str, object]] = []
        sheets: dict[str, list[Path]] = {variant: [] for variant in VARIANTS}
        for scene, source in enumerate(sources, start=1):
            if not isinstance(source, Path) or not source.is_file():
                raise FileNotFoundError(source)
            with Image.open(source).convert("RGB") as opened:
                image = opened.copy()
            if image.size != (1920, 1080):
                raise ValueError(f"unexpected source size {source}")
            samples: list[dict[str, object]] = []
            for variant, floor in VARIANTS.items():
                output = group_root / "frames" / f"scene_{scene:02d}_{variant}.png"
                derived = image if floor is None else shadow_floor(image, floor)
                derived.save(output, format="PNG", optimize=False)
                samples.append(
                    {
                        "variant": variant,
                        "luma_floor_code_value": floor,
                        "frame": output.relative_to(group_root).as_posix(),
                        "frame_sha256": sha256(output),
                    }
                )
                sheets[variant].append(output)
                total_frames += 1
            scene_rows.append(
                {
                    "scene": scene,
                    "source": source.relative_to(ROOT).as_posix(),
                    "source_sha256": sha256(source),
                    "samples": samples,
                }
            )
        sheet_rows: dict[str, object] = {}
        for variant, paths in sheets.items():
            sheet = group_root / f"contact_sheet_{variant}.png"
            contact_sheet(paths, [f"S{scene} · {variant}" for scene in range(1, 8)], sheet)
            sheet_rows[variant] = {
                "path": sheet.relative_to(group_root).as_posix(),
                "sha256": sha256(sheet),
                "width": 1280,
                "height": 1576,
            }
        receipt_groups[group_name] = {
            "source_receipt": source_receipt.relative_to(ROOT).as_posix(),
            "source_receipt_sha256": sha256(source_receipt),
            "scene_count": 7,
            "frame_count": 35,
            "scenes": scene_rows,
            "contact_sheets": sheet_rows,
        }

    receipt = {
        "status": "QA_STATIC_PNG_DERIVATIVES_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 14,
        "groups": receipt_groups,
        "group_count": 3,
        "scene_count": 21,
        "variant_count": 5,
        "frame_count": total_frames,
        "variant_order": list(VARIANTS),
        "transform_contract": {
            "implementation": "integer-luma-preserving dark-tone floor and full-range remap",
            "luma_weights_integer_over_256": [54, 183, 19],
            "luma_rounding": "add 128 then floor divide by 256",
            "floors_srgb_code_value": [8, 16, 32, 48],
            "remap": "Y2=max(Y-floor,0)*255/(255-floor), integer round-half-up; RGB2=RGB*Y2/Y, integer round-half-up",
            "source_mode": "RGB",
            "canvas_change": False,
        },
        "sealed_v8_modified": False,
        "pass7_mockup_modified": False,
        "pass12_proof_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    (OUT / "receipt.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"PASS groups=3 scenes=21 frames={total_frames}")


if __name__ == "__main__":
    main()
