#!/usr/bin/env python3
"""Build deterministic JPEG 4:2:0 recompression derivatives from sealed v8 and pass-7 proof."""

from __future__ import annotations

import hashlib
import io
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, __version__ as pillow_version

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass11_v8_recompression"
WIDTH, HEIGHT = 1920, 1080
VARIANTS: dict[str, int | None] = {
    "clean": None,
    "jpeg_q85_420": 85,
    "jpeg_q60_420": 60,
    "jpeg_q35_420": 35,
    "jpeg_q20_420": 20,
}
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
GROUPS = {
    "sealed_v8": {
        "source_root": ROOT / "proposal_frames/v8",
        "source_receipt": ROOT / "proposal_frames/v8/render_receipt.json",
        "source_paths": [
            ROOT / "proposal_frames/v8" / f"scene_{scene:02d}_s{scene}.png"
            for scene in range(1, 8)
        ],
    },
    "pass7_caption_safe": {
        "source_root": ROOT / "qa/pass7_caption_safe_mockup",
        "source_receipt": ROOT / "qa/pass7_caption_safe_mockup/receipt.json",
        "source_paths": [
            ROOT / "qa/pass7_caption_safe_mockup/frames" / f"scene_{scene:02d}_caption_safe.png"
            for scene in range(1, 8)
        ],
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def recompress(source: Path, destination: Path, quality: int) -> tuple[str, int]:
    with Image.open(source) as opened:
        image = opened.convert("RGB")
        if image.size != (WIDTH, HEIGHT):
            raise ValueError(f"unexpected source size: {source}: {image.size}")
        buffer = io.BytesIO()
        image.save(
            buffer,
            format="JPEG",
            quality=quality,
            subsampling=2,
            optimize=False,
            progressive=False,
        )
    jpeg_bytes = buffer.getvalue()
    with Image.open(io.BytesIO(jpeg_bytes)) as decoded:
        decoded.convert("RGB").save(destination, format="PNG", optimize=False)
    return hashlib.sha256(jpeg_bytes).hexdigest(), len(jpeg_bytes)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_sheet(group_dir: Path, variant: str, rows: list[dict[str, object]]) -> dict[str, object]:
    tile_w, image_h, label_h = 640, 360, 34
    sheet = Image.new("RGB", (tile_w * 2, (image_h + label_h) * 4), (4, 8, 14))
    draw = ImageDraw.Draw(sheet)
    label_font = font(20)
    for index, row in enumerate(rows):
        scene_value = row["scene"]
        if not isinstance(scene_value, int):
            raise TypeError("scene number must be integer")
        x = (index % 2) * tile_w
        y = (index // 2) * (image_h + label_h)
        draw.rectangle((x, y, x + tile_w, y + label_h), fill=(4, 8, 14))
        draw.text((x + 8, y + 5), f"S{scene_value} · {variant}", fill=(242, 246, 252), font=label_font)
        with Image.open(group_dir / str(row["frame"])) as opened:
            image = opened.convert("RGB")
            image.thumbnail((tile_w, image_h), Image.Resampling.LANCZOS)
        sheet.paste(image, (x, y + label_h))
    destination = group_dir / f"contact_sheet_{variant}.png"
    sheet.save(destination, format="PNG", optimize=False)
    return {
        "path": destination.relative_to(group_dir).as_posix(),
        "sha256": sha256(destination),
        "width": sheet.width,
        "height": sheet.height,
    }


def build_group(group_name: str, spec: dict[str, object]) -> dict[str, object]:
    group_dir = OUT / group_name
    frames_dir = group_dir / "frames"
    group_dir.mkdir(parents=True)
    frames_dir.mkdir()
    source_root = spec["source_root"]
    source_receipt = spec["source_receipt"]
    source_paths = spec["source_paths"]
    if not isinstance(source_root, Path) or not isinstance(source_receipt, Path):
        raise TypeError("source paths must be Path objects")
    if not isinstance(source_paths, list) or not all(isinstance(path, Path) for path in source_paths):
        raise TypeError("source path list invalid")

    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {variant: [] for variant in VARIANTS}
    for scene, source in enumerate(source_paths, start=1):
        if not source.is_file():
            raise FileNotFoundError(source)
        clean_rel = Path("frames") / f"scene_{scene:02d}_clean.png"
        clean_path = group_dir / clean_rel
        shutil.copyfile(source, clean_path)
        samples: list[dict[str, object]] = []
        for variant, quality in VARIANTS.items():
            jpeg_hash: str | None = None
            jpeg_bytes: int | None = None
            if quality is None:
                frame_rel = clean_rel
            else:
                frame_rel = Path("frames") / f"scene_{scene:02d}_{variant}.png"
                jpeg_hash, jpeg_bytes = recompress(source, group_dir / frame_rel, quality)
            frame_path = group_dir / frame_rel
            sample: dict[str, object] = {
                "variant": variant,
                "quality": quality,
                "subsampling": None if quality is None else "4:2:0",
                "frame": frame_rel.as_posix(),
                "frame_sha256": sha256(frame_path),
                "jpeg_sha256": jpeg_hash,
                "jpeg_bytes": jpeg_bytes,
            }
            samples.append(sample)
            by_variant[variant].append({"scene": scene, **sample})
        scenes.append(
            {
                "scene": scene,
                "source": source.relative_to(ROOT).as_posix(),
                "source_sha256": sha256(source),
                "clean_copy_sha256_match": sha256(source) == sha256(clean_path),
                "samples": samples,
            }
        )
    sheets = {variant: make_sheet(group_dir, variant, rows) for variant, rows in by_variant.items()}
    return {
        "source_root": source_root.relative_to(ROOT).as_posix(),
        "source_receipt": source_receipt.relative_to(ROOT).as_posix(),
        "source_receipt_sha256": sha256(source_receipt),
        "scene_count": len(scenes),
        "frame_count": len(scenes) * len(VARIANTS),
        "scenes": scenes,
        "contact_sheets": sheets,
    }


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    groups: dict[str, dict[str, object]] = {
        name: build_group(name, spec) for name, spec in GROUPS.items()
    }
    scene_count = 0
    frame_count = 0
    for group in groups.values():
        group_scene_count = group["scene_count"]
        group_frame_count = group["frame_count"]
        if not isinstance(group_scene_count, int) or not isinstance(group_frame_count, int):
            raise TypeError("group counts must be integers")
        scene_count += group_scene_count
        frame_count += group_frame_count
    receipt = {
        "status": "QA_STATIC_DERIVATIVES_ONLY_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 11,
        "audit": "sealed_v8_and_caption_safe_jpeg_420_recompression_resilience",
        "simulation_scope": "deterministic Pillow JPEG recompression/decode stress; quality values are library parameters, not claims about a named platform or delivery path",
        "pillow_version": pillow_version,
        "variant_order": list(VARIANTS),
        "variants": {
            name: {"quality": quality, "subsampling": None if quality is None else "4:2:0"}
            for name, quality in VARIANTS.items()
        },
        "transform_contract": {
            "encoder": "Pillow JPEG",
            "color_mode": "RGB",
            "subsampling": "4:2:0 (Pillow subsampling=2)",
            "optimize": False,
            "progressive": False,
            "decode": "Pillow JPEG decode to RGB",
            "storage": "decoded pixels saved as non-optimized RGB PNG",
        },
        "scene_count": scene_count,
        "frame_count": frame_count,
        "groups": groups,
        "sealed_v8_modified": False,
        "pass7_mockup_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    receipt_path = OUT / "receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS groups={len(groups)} scenes={scene_count} frames={frame_count}")


if __name__ == "__main__":
    main()
