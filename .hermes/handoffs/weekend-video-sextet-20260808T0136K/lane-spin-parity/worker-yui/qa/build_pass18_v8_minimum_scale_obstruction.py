#!/usr/bin/env python3
"""Build deterministic method proofs for 360p plus bottom-obstruction interaction."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import cast

import PIL
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass18_v8_minimum_scale_obstruction"
OUTPUT_SIZE = (640, 360)
VARIANTS: dict[str, float | None] = {
    "clean": None,
    "downscale_360p": None,
    "caption15_360p": 0.15,
    "player_ui25_360p": 0.25,
    "heavy35_360p": 0.35,
}
GROUPS = {
    "sealed_v8": {
        "source_receipt": ROOT / "proposal_frames/v8/render_receipt.json",
        "sources": [ROOT / "proposal_frames/v8" / f"scene_{scene:02d}_s{scene}.png" for scene in range(1, 8)],
    },
    "pass7_caption_safe": {
        "source_receipt": ROOT / "qa/pass7_caption_safe_mockup/receipt.json",
        "sources": [ROOT / "qa/pass7_caption_safe_mockup/frames" / f"scene_{scene:02d}_caption_safe.png" for scene in range(1, 8)],
    },
    "pass12_sharpness_safe": {
        "source_receipt": ROOT / "qa/pass12_sharpness_safe_mockup/receipt.json",
        "sources": [ROOT / "qa/pass12_sharpness_safe_mockup/frames" / f"scene_{scene:02d}_clean.png" for scene in range(1, 8)],
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def downscale(image: Image.Image) -> Image.Image:
    return image.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)


def obstruction(image: Image.Image, fraction: float) -> tuple[Image.Image, int]:
    top_y = int(round(image.height * (1.0 - fraction)))
    output = image.copy()
    ImageDraw.Draw(output).rectangle((0, top_y, image.width - 1, image.height - 1), fill=(0, 0, 0))
    if output.crop((0, 0, image.width, top_y)).tobytes() != image.crop((0, 0, image.width, top_y)).tobytes():
        raise AssertionError("unobstructed pixels changed")
    return output, top_y


def make_sheet(group_dir: Path, variant: str, samples: list[dict[str, object]]) -> dict[str, object]:
    tile_w, tile_h, label_h = 640, 360, 34
    sheet = Image.new("RGB", (tile_w * 2, (tile_h + label_h) * 4), (4, 8, 14))
    draw = ImageDraw.Draw(sheet)
    label_font = font(20)
    for index, sample in enumerate(samples):
        scene_value = sample["scene"]
        if not isinstance(scene_value, int):
            raise TypeError("scene must be an integer")
        x = (index % 2) * tile_w
        y = (index // 2) * (tile_h + label_h)
        draw.rectangle((x, y, x + tile_w, y + label_h), fill=(4, 8, 14))
        draw.text((x + 8, y + 5), f"S{scene_value} · {variant}", fill=(242, 246, 252), font=label_font)
        with Image.open(group_dir / str(sample["frame"])) as opened:
            image = opened.convert("RGB")
            if image.size != OUTPUT_SIZE:
                image = image.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)
        sheet.paste(image, (x, y + label_h))
    destination = group_dir / f"contact_sheet_{variant}.png"
    sheet.save(destination, format="PNG", optimize=False)
    with Image.open(destination) as saved:
        width, height = saved.size
    return {"path": destination.name, "sha256": sha(destination), "width": width, "height": height}


def build_group(name: str, spec: dict[str, object]) -> dict[str, object]:
    group_dir = OUT / name
    frames_dir = group_dir / "frames"
    frames_dir.mkdir(parents=True)
    sources = spec["sources"]
    source_receipt = spec["source_receipt"]
    if not isinstance(sources, list) or not all(isinstance(path, Path) for path in sources):
        raise TypeError("sources invalid")
    if not isinstance(source_receipt, Path):
        raise TypeError("source receipt invalid")
    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {variant: [] for variant in VARIANTS}
    for scene, source in enumerate(sources, 1):
        with Image.open(source) as opened:
            clean = opened.convert("RGB")
        if clean.size != (1920, 1080):
            raise SystemExit(f"unexpected source dimensions {source}: {clean.size}")
        scaled = downscale(clean)
        samples: list[dict[str, object]] = []
        for variant, fraction in VARIANTS.items():
            destination = frames_dir / f"scene_{scene:02d}_{variant}.png"
            top_y: int | None = None
            if variant == "clean":
                shutil.copyfile(source, destination)
            elif variant == "downscale_360p":
                scaled.save(destination, format="PNG", optimize=False)
            else:
                if fraction is None:
                    raise AssertionError("fraction missing")
                derived, top_y = obstruction(scaled, fraction)
                derived.save(destination, format="PNG", optimize=False)
            with Image.open(destination) as saved:
                width, height, mode = saved.width, saved.height, saved.mode
            sample = {
                "scene": scene,
                "variant": variant,
                "obstruction_fraction": fraction,
                "mask_top_y": top_y,
                "mask_color_rgb": [0, 0, 0] if fraction is not None else None,
                "frame": f"frames/{destination.name}",
                "sha256": sha(destination),
                "width": width,
                "height": height,
                "mode": mode,
                "unobstructed_pixels_identical_to_downscale": True if fraction is not None else None,
            }
            samples.append(sample)
            by_variant[variant].append(sample)
        scenes.append({
            "scene": scene,
            "source": source.relative_to(ROOT).as_posix(),
            "source_sha256": sha(source),
            "samples": samples,
        })
    sheets = {variant: make_sheet(group_dir, variant, samples) for variant, samples in by_variant.items()}
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
    frame_count = scene_count * len(VARIANTS)
    receipt = {
        "status": "QA_STATIC_DERIVATIVES_ONLY_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 18,
        "audit": "sealed_v8_pass7_pass12_minimum_scale_bottom_obstruction_interaction",
        "simulation_scope": "packet-specific native RGB to Pillow LANCZOS 640x360 then opaque bottom obstruction; not a named player or delivery path",
        "pillow_version": PIL.__version__,
        "variant_order": list(VARIANTS),
        "reference_variant": "downscale_360p",
        "operational_variants": ["caption15_360p", "player_ui25_360p"],
        "characterization_variants": ["heavy35_360p"],
        "variants": {
            name: {
                "obstruction_fraction": fraction,
                "mask_top_y": int(round(360 * (1.0 - fraction))) if fraction is not None else None,
            }
            for name, fraction in VARIANTS.items()
        },
        "transform_contract": {
            "input": "native 1920x1080 RGB",
            "downscale": "Pillow LANCZOS to 640x360",
            "mask": "opaque RGB(0,0,0) rectangle from mask_top_y through row 359",
            "unobstructed_pixels": "byte-identical to lossless downscale above mask_top_y",
            "storage": "non-optimized RGB PNG",
            "transform_order": "native RGB -> LANCZOS 640x360 -> opaque bottom mask",
        },
        "group_count": 3,
        "scene_count": scene_count,
        "frame_count": frame_count,
        "groups": groups,
        "sealed_v8_modified": False,
        "pass7_mockup_modified": False,
        "pass12_mockup_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS groups=3 scenes={receipt['scene_count']} frames={receipt['frame_count']}")


if __name__ == "__main__":
    main()
