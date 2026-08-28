#!/usr/bin/env python3
"""Build pass-16 compound anisotropic-geometry-at-360p method derivatives."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass16_v8_minimum_scale_geometry"
OUTPUT_SIZE = (640, 360)
VARIANTS = [
    ("clean", 1.0, 1.0),
    ("x90_360p", 0.90, 1.0),
    ("y90_360p", 1.0, 0.90),
    ("x80_360p", 0.80, 1.0),
    ("y80_360p", 1.0, 0.80),
]
GROUPS = {
    "sealed_v8": [ROOT / f"proposal_frames/v8/scene_{index:02d}_s{index}.png" for index in range(1, 8)],
    "pass7_caption_safe": [ROOT / f"qa/pass7_caption_safe_mockup/frames/scene_{index:02d}_caption_safe.png" for index in range(1, 8)],
    "pass12_sharpness_safe": [ROOT / f"qa/pass12_sharpness_safe_mockup/frames/scene_{index:02d}_clean.png" for index in range(1, 8)],
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def transform(image: Image.Image, sx: float, sy: float) -> tuple[Image.Image, dict]:
    w, h = image.size
    nw, nh = int(round(w * sx)), int(round(h * sy))
    squeezed = image.resize((nw, nh), Image.Resampling.LANCZOS)
    native = Image.new("RGB", (w, h), (0, 0, 0))
    x0, y0 = (w - nw) // 2, (h - nh) // 2
    native.paste(squeezed, (x0, y0))
    return native.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS), {
        "source_size": [w, h],
        "anisotropic_resampled_size": [nw, nh],
        "native_offset": [x0, y0],
        "scale_x": sx,
        "scale_y": sy,
        "minimum_scale_output_size": list(OUTPUT_SIZE),
        "transform_order": "native anisotropic LANCZOS -> centered black padding -> full-canvas LANCZOS downscale to 640x360",
    }


def make_sheet(paths: list[Path], output: Path, label: str) -> tuple[int, int]:
    thumb, margin, label_h = (560, 315), 20, 42
    sheet = Image.new("RGB", (margin * 3 + thumb[0] * 2, margin * 5 + (thumb[1] + label_h) * 4), (9, 12, 20))
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    for index, path in enumerate(paths):
        with Image.open(path).convert("RGB") as source:
            resized = source.resize(thumb, Image.Resampling.NEAREST if source.size == OUTPUT_SIZE else Image.Resampling.LANCZOS)
        x = margin + (index % 2) * (thumb[0] + margin)
        y = margin + (index // 2) * (thumb[1] + label_h + margin)
        sheet.paste(resized, (x, y + label_h))
        draw.text((x, y + 8), f"scene {index + 1:02d} · {label}", fill=(235, 240, 250), font=font)
    sheet.save(output)
    with Image.open(output) as saved:
        return saved.size


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    receipt = {
        "status": "QA_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 16,
        "group_count": 3,
        "scene_count": 21,
        "frame_count": 105,
        "variants": [item[0] for item in VARIANTS],
        "operational_variants": ["x90_360p", "y90_360p"],
        "characterization_variants": ["x80_360p", "y80_360p"],
        "anisotropic_resampler": "Pillow LANCZOS",
        "minimum_scale_resampler": "Pillow LANCZOS",
        "padding": "centered black RGB",
        "minimum_scale_output": "640x360 RGB",
        "groups": {},
        "tts_invoked": False, "audio_generated": False, "video_encoded": False, "git_action": False,
    }
    for group_name, sources in GROUPS.items():
        frame_dir = OUT / group_name / "frames"
        frame_dir.mkdir(parents=True)
        rows, geometry = [], {}
        for scene, source in enumerate(sources, 1):
            with Image.open(source) as opened:
                image = opened.convert("RGB")
            if image.size != (1920, 1080):
                raise SystemExit(f"{group_name} scene {scene}: dimensions {image.size}")
            samples = []
            for variant, sx, sy in VARIANTS:
                output = frame_dir / f"scene_{scene:02d}_{variant}.png"
                if variant == "clean":
                    shutil.copyfile(source, output)
                else:
                    derived, contract = transform(image, sx, sy)
                    derived.save(output)
                    geometry[variant] = contract
                with Image.open(output) as saved:
                    width, height, mode = saved.width, saved.height, saved.mode
                samples.append({
                    "variant": variant, "scale_x": sx, "scale_y": sy,
                    "frame": f"frames/{output.name}", "frame_sha256": sha(output),
                    "width": width, "height": height, "mode": mode,
                })
            rows.append({
                "scene": scene,
                "source": str(source.relative_to(ROOT)),
                "source_sha256": sha(source),
                "samples": samples,
            })
        sheets = {}
        for variant, _, _ in VARIANTS:
            paths = [frame_dir / f"scene_{index:02d}_{variant}.png" for index in range(1, 8)]
            output = OUT / group_name / f"contact_sheet_{variant}.png"
            width, height = make_sheet(paths, output, variant)
            sheets[variant] = {"path": output.name, "sha256": sha(output), "width": width, "height": height}
        receipt["groups"][group_name] = {
            "scene_count": 7, "frame_count": 35,
            "geometry": geometry, "scenes": rows, "contact_sheets": sheets,
        }
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("PASS groups=3 scenes=21 frames=105")


if __name__ == "__main__":
    main()
