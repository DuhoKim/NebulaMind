#!/usr/bin/env python3
"""Build method proofs for native color-vision transforms then 360p."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass23_v8_minimum_scale_color_vision"
OUTPUT_SIZE = (640, 360)
VARIANTS = [
    "color_360p",
    "grayscale_bt709_then_360p",
    "protanopia_machado100_then_360p",
    "deuteranopia_machado100_then_360p",
    "tritanopia_machado100_then_360p",
]
MATRICES = {
    "protanopia_machado100": np.array(
        [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]], dtype=np.float64
    ),
    "deuteranopia_machado100": np.array(
        [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]], dtype=np.float64
    ),
    "tritanopia_machado100": np.array(
        [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]], dtype=np.float64
    ),
}
GROUPS: dict[str, dict[str, object]] = {
    "sealed_v8": {
        "source_receipt": ROOT / "proposal_frames/v8/render_receipt.json",
        "source_paths": [ROOT / "proposal_frames/v8" / f"scene_{scene:02d}_s{scene}.png" for scene in range(1, 8)],
    },
    "pass7_caption_safe": {
        "source_receipt": ROOT / "qa/pass7_caption_safe_mockup/receipt.json",
        "source_paths": [ROOT / "qa/pass7_caption_safe_mockup/frames" / f"scene_{scene:02d}_caption_safe.png" for scene in range(1, 8)],
    },
    "pass12_sharpness_safe": {
        "source_receipt": ROOT / "qa/pass12_sharpness_safe_mockup/receipt.json",
        "source_paths": [ROOT / "qa/pass12_sharpness_safe_mockup/frames" / f"scene_{scene:02d}_clean.png" for scene in range(1, 8)],
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, 1.0)
    return np.where(clipped <= 0.0031308, 12.92 * clipped, 1.055 * clipped ** (1.0 / 2.4) - 0.055)


def transform(native: Image.Image, variant: str) -> Image.Image:
    if variant == "color_360p":
        transformed = native.convert("RGB")
    else:
        label = variant.removesuffix("_then_360p")
        rgb = np.asarray(native.convert("RGB"), dtype=np.float64) / 255.0
        linear = srgb_to_linear(rgb)
        if label == "grayscale_bt709":
            luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
            transformed_linear = np.repeat(luminance[:, :, None], 3, axis=2)
        else:
            transformed_linear = np.einsum("...c,rc->...r", linear, MATRICES[label])
        pixels = np.rint(np.clip(linear_to_srgb(transformed_linear), 0.0, 1.0) * 255.0).astype(np.uint8)
        transformed = Image.fromarray(pixels)
    return transformed.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def contact_sheet(group_root: Path, variant: str, records: list[dict[str, object]]) -> dict[str, object]:
    tile_w, tile_h, label_h = 640, 360, 28
    canvas = Image.new("RGB", (tile_w * 2, (tile_h + label_h) * 4), (4, 8, 14))
    draw = ImageDraw.Draw(canvas)
    face = font(18)
    for index, record in enumerate(records):
        x = index % 2 * tile_w
        y = index // 2 * (tile_h + label_h)
        scene_value = record["scene"]
        if not isinstance(scene_value, int):
            raise TypeError("scene must be int")
        draw.text((x + 8, y + 3), f"S{scene_value} · {variant}", fill=(240, 244, 250), font=face)
        with Image.open(group_root / str(record["frame"])) as image:
            canvas.paste(image.convert("RGB"), (x, y + label_h))
    target = group_root / f"contact_sheet_{variant}.png"
    canvas.save(target, format="PNG", optimize=False)
    return {"path": target.relative_to(group_root).as_posix(), "sha256": sha(target), "width": canvas.width, "height": canvas.height}


def build_group(name: str, source_paths: list[Path], source_receipt: Path) -> dict[str, object]:
    group_root = OUT / name
    if group_root.exists():
        shutil.rmtree(group_root)
    frames = group_root / "frames"
    frames.mkdir(parents=True)
    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {variant: [] for variant in VARIANTS}
    for scene, source in enumerate(source_paths, start=1):
        samples: list[dict[str, object]] = []
        with Image.open(source) as opened:
            native = opened.convert("RGB")
            if native.size != (1920, 1080):
                raise SystemExit(f"native source dimensions changed: {source}")
            for variant in VARIANTS:
                target = frames / f"scene_{scene:02d}_{variant}.png"
                transform(native, variant).save(target, format="PNG", optimize=False)
                with Image.open(target) as check:
                    if check.mode != "RGB" or check.size != OUTPUT_SIZE:
                        raise SystemExit(f"invalid derivative {target}")
                sample = {
                    "variant": variant,
                    "frame": target.relative_to(group_root).as_posix(),
                    "frame_sha256": sha(target),
                    "width": 640,
                    "height": 360,
                }
                samples.append(sample)
                by_variant[variant].append({"scene": scene, **sample})
        scenes.append(
            {
                "scene": scene,
                "source": source.relative_to(ROOT).as_posix(),
                "source_sha256": sha(source),
                "samples": samples,
            }
        )
    sheets = {variant: contact_sheet(group_root, variant, rows) for variant, rows in by_variant.items()}
    return {
        "group": name,
        "source_receipt": source_receipt.relative_to(ROOT).as_posix(),
        "source_receipt_sha256": sha(source_receipt),
        "scene_count": len(scenes),
        "frame_count": len(scenes) * len(VARIANTS),
        "scenes": scenes,
        "contact_sheets": sheets,
    }


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    groups: dict[str, object] = {}
    for name, spec in GROUPS.items():
        paths = spec["source_paths"]
        receipt = spec["source_receipt"]
        if not isinstance(paths, list) or not isinstance(receipt, Path):
            raise TypeError("invalid group specification")
        if not all(isinstance(path, Path) for path in paths):
            raise TypeError("source path must be Path")
        groups[name] = build_group(name, paths, receipt)
    receipt = {
        "status": "QA_STATIC_DERIVATIVES_ONLY_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 23,
        "audit": "method_proofs_native_monochrome_and_color_vision_then_minimum_scale",
        "variant_order": VARIANTS,
        "scene_count": 21,
        "frame_count": 105,
        "represented_resolution": [640, 360],
        "groups": groups,
        "transform_contract": {
            "transform_order": "native RGB -> linear-light BT.709 grayscale or Machado severity-100 color-vision matrix -> sRGB np.rint uint8 -> Pillow LANCZOS 640x360",
            "matrices": {key: value.tolist() for key, value in MATRICES.items()},
            "simulation_scope": "presentation stress test only; not a clinical diagnostic or named delivery/viewing standard",
            "numpy": np.__version__,
            "pillow": PIL.__version__,
        },
        "sealed_v8_modified": False,
        "pass7_proof_modified": False,
        "pass12_proof_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("PASS groups=3 scenes=21 frames=105")


if __name__ == "__main__":
    main()
