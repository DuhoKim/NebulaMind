#!/usr/bin/env python3
"""Build deterministic pass-15 anisotropic-resampling derivatives for method-only groups."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass15_v8_geometry"
VARIANTS = [
    ("clean", 1.0, 1.0),
    ("squeeze_x90", 0.90, 1.0),
    ("squeeze_y90", 1.0, 0.90),
    ("squeeze_x80", 0.80, 1.0),
    ("squeeze_y80", 1.0, 0.80),
]
GROUPS = {
    "sealed_v8": [ROOT / f"proposal_frames/v8/scene_{i:02d}_s{i}.png" for i in range(1, 8)],
    "pass7_caption_safe": [ROOT / f"qa/pass7_caption_safe_mockup/frames/scene_{i:02d}_caption_safe.png" for i in range(1, 8)],
    "pass12_sharpness_safe": [ROOT / f"qa/pass12_sharpness_safe_mockup/frames/scene_{i:02d}_clean.png" for i in range(1, 8)],
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def squeeze(image: Image.Image, sx: float, sy: float) -> tuple[Image.Image, dict]:
    w, h = image.size
    nw, nh = int(round(w * sx)), int(round(h * sy))
    resized = image.resize((nw, nh), Image.Resampling.LANCZOS)
    out = Image.new("RGB", (w, h), (0, 0, 0))
    x0, y0 = (w - nw) // 2, (h - nh) // 2
    out.paste(resized, (x0, y0))
    return out, {"source_size": [w, h], "resampled_size": [nw, nh], "offset": [x0, y0], "scale_x": sx, "scale_y": sy}


def sheet(paths: list[Path], output: Path, label: str) -> None:
    thumb, margin, label_h = (560, 315), 20, 42
    result = Image.new("RGB", (margin * 3 + thumb[0] * 2, margin * 5 + (thumb[1] + label_h) * 4), (9, 12, 20))
    draw = ImageDraw.Draw(result)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    for i, path in enumerate(paths):
        im = Image.open(path).convert("RGB").resize(thumb, Image.Resampling.LANCZOS)
        x = margin + (i % 2) * (thumb[0] + margin)
        y = margin + (i // 2) * (thumb[1] + label_h + margin)
        result.paste(im, (x, y + label_h))
        draw.text((x, y + 8), f"scene {i + 1:02d} · {label}", fill=(235, 240, 250), font=font)
    result.save(output)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    receipt = {
        "status": "QA_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 15,
        "group_count": 3,
        "scene_count": 21,
        "frame_count": 105,
        "variants": [v[0] for v in VARIANTS],
        "operational_variants": ["squeeze_x90", "squeeze_y90"],
        "characterization_variants": ["squeeze_x80", "squeeze_y80"],
        "resampler": "Pillow LANCZOS",
        "padding": "centered black RGB",
        "groups": {},
        "tts_invoked": False, "audio_generated": False, "video_encoded": False, "git_action": False,
    }
    for group, sources in GROUPS.items():
        frame_dir = OUT / group / "frames"
        frame_dir.mkdir(parents=True)
        rows, geometry = [], {}
        for scene, source in enumerate(sources, 1):
            with Image.open(source) as im:
                image = im.convert("RGB")
            if image.size != (1920, 1080):
                raise SystemExit(f"{group} scene {scene}: dimensions {image.size}")
            samples = []
            for variant, sx, sy in VARIANTS:
                output = frame_dir / f"scene_{scene:02d}_{variant}.png"
                if variant == "clean":
                    shutil.copyfile(source, output)
                else:
                    derived, geom = squeeze(image, sx, sy)
                    derived.save(output)
                    geometry[variant] = geom
                samples.append({"variant": variant, "scale_x": sx, "scale_y": sy, "frame": f"frames/{output.name}", "frame_sha256": sha(output)})
            rows.append({"scene": scene, "source": str(source.relative_to(ROOT)), "source_sha256": sha(source), "samples": samples})
        sheets = {}
        for variant, _, _ in VARIANTS:
            paths = [frame_dir / f"scene_{i:02d}_{variant}.png" for i in range(1, 8)]
            output = OUT / group / f"contact_sheet_{variant}.png"
            sheet(paths, output, variant)
            sheets[variant] = {"path": output.name, "sha256": sha(output), "width": 1180, "height": 1528}
        receipt["groups"][group] = {"scene_count": 7, "frame_count": 35, "geometry": geometry, "scenes": rows, "contact_sheets": sheets}
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("PASS groups=3 scenes=21 frames=105")


if __name__ == "__main__":
    main()
