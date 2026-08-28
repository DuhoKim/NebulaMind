#!/usr/bin/env python3
"""Build deterministic directional-smear derivatives for method-only frame groups."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass13_v8_directional_smear"
VARIANTS: dict[str, int | None] = {
    "clean": None,
    "smear_w03": 3,
    "smear_w07": 7,
    "smear_w13": 13,
    "smear_w21": 21,
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


def horizontal_smear(image: Image.Image, width: int) -> Image.Image:
    if width <= 0 or width % 2 != 1:
        raise ValueError("smear width must be a positive odd integer")
    values = np.asarray(image.convert("RGB"), dtype=np.uint8)
    radius = width // 2
    padded = np.pad(values, ((0, 0), (radius, radius), (0, 0)), mode="edge")
    cumulative = np.cumsum(padded, axis=1, dtype=np.uint64)
    cumulative = np.concatenate(
        [np.zeros((values.shape[0], 1, 3), dtype=np.uint64), cumulative], axis=1
    )
    sums = cumulative[:, width:, :] - cumulative[:, :-width, :]
    output = ((sums + width // 2) // width).astype(np.uint8)
    if output.shape != values.shape:
        raise ValueError("smear shape mismatch")
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
            for variant, width in VARIANTS.items():
                output = group_root / "frames" / f"scene_{scene:02d}_{variant}.png"
                derived = image if width is None else horizontal_smear(image, width)
                derived.save(output, format="PNG", optimize=False)
                samples.append(
                    {
                        "variant": variant,
                        "kernel_width_pixels": width,
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
            contact_sheet(
                paths,
                [f"S{scene} · {variant}" for scene in range(1, 8)],
                sheet,
            )
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
        "deepening_pass": 13,
        "groups": receipt_groups,
        "group_count": 3,
        "scene_count": 21,
        "variant_count": 5,
        "frame_count": total_frames,
        "variant_order": list(VARIANTS),
        "transform_contract": {
            "implementation": "centered horizontal box smear with edge replication, uint64 summed, round-half-up integer division",
            "kernel_widths_pixels": [3, 7, 13, 21],
            "axis": "horizontal",
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
