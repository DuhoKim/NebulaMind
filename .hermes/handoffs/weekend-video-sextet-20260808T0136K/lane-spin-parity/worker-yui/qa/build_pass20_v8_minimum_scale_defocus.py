#!/usr/bin/env python3
"""Build deterministic method proofs for native Gaussian defocus then 360p."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import cast

import PIL
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass20_v8_minimum_scale_defocus"
OUTPUT_SIZE = (640, 360)
VARIANTS: dict[str, float | None] = {
    "clean": None,
    "downscale_360p": None,
    "defocus_r1_50_then_360p": 1.5,
    "defocus_r2_50_then_360p": 2.5,
    "defocus_r4_00_then_360p": 4.0,
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
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def derive(native: Image.Image, variant: str) -> Image.Image:
    if variant == "downscale_360p":
        return native.convert("RGB").resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)
    radius = VARIANTS[variant]
    if radius is None:
        raise ValueError(f"derivative variant has no radius: {variant}")
    blurred = native.convert("RGB").filter(ImageFilter.GaussianBlur(radius=radius))
    return blurred.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)


def get_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]:
        if Path(path).is_file():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def make_sheet(group_dir: Path, variant: str, rows: list[dict[str, object]]) -> dict[str, object]:
    tile_w, tile_h, label_h = 640, 360, 34
    sheet = Image.new("RGB", (tile_w * 2, (tile_h + label_h) * 4), (4, 8, 14))
    draw = ImageDraw.Draw(sheet)
    label_font = get_font(20)
    for index, row in enumerate(rows):
        x = (index % 2) * tile_w
        y = (index // 2) * (tile_h + label_h)
        draw.text((x + 8, y + 5), f"S{cast(int, row['scene'])} · {variant}", fill=(242, 246, 252), font=label_font)
        with Image.open(group_dir / str(row["frame"])).convert("RGB") as source:
            represented = source if source.size == OUTPUT_SIZE else source.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)
        sheet.paste(represented, (x, y + label_h))
    destination = group_dir / f"contact_sheet_{variant}.png"
    sheet.save(destination, format="PNG", optimize=False)
    with Image.open(destination) as saved:
        width, height = saved.size
    return {"path": destination.name, "sha256": sha(destination), "width": width, "height": height}


def build_group(name: str, spec: dict[str, object]) -> dict[str, object]:
    group_dir = OUT / name
    frames = group_dir / "frames"
    frames.mkdir(parents=True)
    source_paths = spec["source_paths"]
    source_receipt = spec["source_receipt"]
    if not isinstance(source_paths, list) or not all(isinstance(path, Path) for path in source_paths):
        raise TypeError("source paths invalid")
    if not isinstance(source_receipt, Path):
        raise TypeError("source receipt invalid")
    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {variant: [] for variant in VARIANTS}
    for scene, source in enumerate(source_paths, 1):
        if not source.is_file():
            raise FileNotFoundError(source)
        clean = frames / f"scene_{scene:02d}_clean.png"
        shutil.copyfile(source, clean)
        with Image.open(source) as opened:
            native = opened.convert("RGB")
        if native.size != (1920, 1080):
            raise ValueError(f"unexpected source size {native.size}")
        samples: list[dict[str, object]] = []
        for variant, radius in VARIANTS.items():
            output = frames / f"scene_{scene:02d}_{variant}.png"
            if variant != "clean":
                derive(native, variant).save(output, format="PNG", optimize=False)
            with Image.open(output) as saved:
                width, height, mode = saved.width, saved.height, saved.mode
            sample = {
                "variant": variant,
                "native_gaussian_radius_pixels": radius,
                "frame": f"frames/{output.name}",
                "sha256": sha(output),
                "width": width,
                "height": height,
                "mode": mode,
            }
            samples.append(sample)
            by_variant[variant].append({"scene": scene, **sample})
        scenes.append({
            "scene": scene,
            "source": source.relative_to(ROOT).as_posix(),
            "source_sha256": sha(source),
            "clean_copy_sha256_match": sha(source) == sha(clean),
            "samples": samples,
        })
    sheets = {variant: make_sheet(group_dir, variant, rows) for variant, rows in by_variant.items()}
    return {
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
    groups = {name: build_group(name, spec) for name, spec in GROUPS.items()}
    scene_count = sum(cast(int, group["scene_count"]) for group in groups.values())
    frame_count = sum(cast(int, group["frame_count"]) for group in groups.values())
    receipt = {
        "status": "QA_STATIC_DERIVATIVES_ONLY_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 20,
        "audit": "sealed_v8_pass7_pass12_native_gaussian_defocus_then_minimum_scale_resilience",
        "variant_order": list(VARIANTS),
        "reference_variant": "downscale_360p",
        "operational_variant": "defocus_r1_50_then_360p",
        "characterization_variants": ["defocus_r2_50_then_360p", "defocus_r4_00_then_360p"],
        "native_gaussian_radius_pixels": {key: value for key, value in VARIANTS.items() if value is not None},
        "transform_contract": "native 1920x1080 RGB -> Pillow ImageFilter.GaussianBlur(radius) -> full-canvas Pillow LANCZOS 640x360 RGB",
        "pillow": PIL.__version__,
        "scene_count": scene_count,
        "frame_count": frame_count,
        "groups": groups,
        "sealed_v8_modified": False,
        "pass7_proof_modified": False,
        "pass12_proof_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
    }
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS groups={len(groups)} scenes={scene_count} frames={frame_count}")


if __name__ == "__main__":
    main()
