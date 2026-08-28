#!/usr/bin/env python3
"""Derive deterministic monochrome/CVD QA frames from sealed v8 and pass-7 proof."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass8_v8_color_vision"
SEALED = ROOT / "proposal_frames/v8"
PASS7_ROOT = ROOT / "qa/pass7_caption_safe_mockup"
PASS7_RECEIPT = PASS7_ROOT / "receipt.json"
VARIANTS = [
    "color",
    "grayscale_bt709",
    "protanopia_machado100",
    "deuteranopia_machado100",
    "tritanopia_machado100",
]
MATRICES = {
    "protanopia_machado100": np.array(
        [
            [0.152286, 1.052583, -0.204868],
            [0.114503, 0.786281, 0.099216],
            [-0.003882, -0.048116, 1.051998],
        ],
        dtype=np.float64,
    ),
    "deuteranopia_machado100": np.array(
        [
            [0.367322, 0.860646, -0.227968],
            [0.280085, 0.672501, 0.047413],
            [-0.011820, 0.042940, 0.968881],
        ],
        dtype=np.float64,
    ),
    "tritanopia_machado100": np.array(
        [
            [1.255528, -0.076749, -0.178779],
            [-0.078411, 0.930809, 0.147602],
            [0.004733, 0.691367, 0.303900],
        ],
        dtype=np.float64,
    ),
}
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, 1.0)
    return np.where(clipped <= 0.0031308, 12.92 * clipped, 1.055 * clipped ** (1.0 / 2.4) - 0.055)


def transform(source: Path, label: str, destination: Path) -> None:
    with Image.open(source).convert("RGB") as image:
        rgb = np.asarray(image, dtype=np.float64) / 255.0
    if label == "grayscale_bt709":
        linear = srgb_to_linear(rgb)
        luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
        transformed = linear_to_srgb(np.repeat(luminance[:, :, None], 3, axis=2))
    elif label in MATRICES:
        linear = srgb_to_linear(rgb)
        transformed_linear = np.einsum("...c,rc->...r", linear, MATRICES[label])
        transformed = linear_to_srgb(transformed_linear)
    else:
        raise ValueError(f"unknown transform: {label}")
    pixels = np.rint(np.clip(transformed, 0.0, 1.0) * 255.0).astype(np.uint8)
    Image.fromarray(pixels).save(destination, format="PNG", optimize=False)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_sheet(group_root: Path, label: str, rows: list[dict[str, object]]) -> dict[str, object]:
    tile_w, image_h, label_h = 640, 360, 32
    tile_h = image_h + label_h
    sheet = Image.new("RGB", (tile_w * 2, tile_h * 4), (4, 8, 14))
    draw = ImageDraw.Draw(sheet)
    label_font = font(20)
    for index, row in enumerate(rows):
        frame = group_root / str(row["frame"])
        scene_value = row["scene"]
        if not isinstance(scene_value, int):
            raise TypeError("scene number must be integer")
        scene = scene_value
        x = (index % 2) * tile_w
        y = (index // 2) * tile_h
        draw.text((x + 8, y + 4), f"S{scene} · {label}", fill=(242, 246, 252), font=label_font)
        with Image.open(frame).convert("RGB") as image:
            image.thumbnail((tile_w, image_h), Image.Resampling.LANCZOS)
            sheet.paste(image, (x, y + label_h))
    destination = group_root / f"contact_sheet_{label}.png"
    sheet.save(destination, format="PNG", optimize=False)
    return {
        "path": destination.relative_to(group_root).as_posix(),
        "sha256": sha256(destination),
        "width": sheet.width,
        "height": sheet.height,
    }


def build_group(group: str, sources: list[tuple[int, Path]]) -> dict[str, object]:
    group_root = OUT / group
    frames_root = group_root / "frames"
    if group_root.exists():
        shutil.rmtree(group_root)
    frames_root.mkdir(parents=True)
    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {variant: [] for variant in VARIANTS}
    for scene, source in sources:
        source_sha = sha256(source)
        samples: list[dict[str, object]] = []
        for variant in VARIANTS:
            frame_rel = Path("frames") / f"scene_{scene:02d}_{variant}.png"
            destination = group_root / frame_rel
            if variant == "color":
                shutil.copyfile(source, destination)
            else:
                transform(source, variant, destination)
            with Image.open(destination) as image:
                if image.mode != "RGB" or image.size != (1920, 1080):
                    raise SystemExit(f"invalid derivative {destination}: {image.mode} {image.size}")
            sample = {
                "variant": variant,
                "frame": frame_rel.as_posix(),
                "frame_sha256": sha256(destination),
                "width": 1920,
                "height": 1080,
            }
            samples.append(sample)
            by_variant[variant].append({"scene": scene, **sample})
        scenes.append(
            {
                "scene": scene,
                "source": source.relative_to(ROOT).as_posix(),
                "source_sha256": source_sha,
                "color_copy_sha256_match": samples[0]["frame_sha256"] == source_sha,
                "samples": samples,
            }
        )
    sheets = {variant: make_sheet(group_root, variant, rows) for variant, rows in by_variant.items()}
    return {
        "group": group,
        "scene_count": len(scenes),
        "frame_count": len(scenes) * len(VARIANTS),
        "scenes": scenes,
        "contact_sheets": sheets,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for path in OUT.glob("*.json"):
        path.unlink()
    sealed_sources = [
        (scene, SEALED / f"scene_{scene:02d}_s{scene}.png") for scene in range(1, 8)
    ]
    pass7 = json.loads(PASS7_RECEIPT.read_text(encoding="utf-8"))
    pass7_sources = [
        (int(scene["scene"]), PASS7_ROOT / scene["clean"]["frame"])
        for scene in pass7["scenes"]
    ]
    groups = {
        "sealed_v8": build_group("sealed_v8", sealed_sources),
        "pass7_caption_safe": build_group("pass7_caption_safe", pass7_sources),
    }
    receipt = {
        "status": "QA_STATIC_DERIVATIVES_ONLY_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 8,
        "audit": "sealed_v8_and_caption_safe_monochrome_color_vision",
        "variant_order": VARIANTS,
        "scene_count": 14,
        "frame_count": 70,
        "groups": groups,
        "transform_contract": {
            "grayscale_bt709": "linear-light BT.709 luminance copied to RGB",
            "cvd_simulations": "Machado severity-100 matrices in linear RGB, clipped then converted to sRGB",
            "matrices": {key: value.tolist() for key, value in MATRICES.items()},
            "simulation_scope": "presentation stress test only; not a clinical diagnostic",
        },
        "sealed_v8_modified": False,
        "pass7_mockup_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
    }
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "PASS groups=2 scenes=14 frames=70 "
        f"sealed={groups['sealed_v8']['frame_count']} pass7={groups['pass7_caption_safe']['frame_count']}"
    )


if __name__ == "__main__":
    main()
