#!/usr/bin/env python3
"""Build method proofs for color/monochrome -> 360p -> represented-pixel vertical width-3 smear."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, __version__ as pillow_version

ROOT = Path(__file__).resolve().parents[1]
PASS23_ROOT = ROOT / "qa/pass23_v8_minimum_scale_color_vision"
PASS23 = PASS23_ROOT / "receipt.json"
OUT = ROOT / "qa/pass29_v8_color_minimum_scale_represented_vertical_smear"
PACKET_CREATED_AT = "2026-08-08T15:47:50+09:00"
WIDTH = 3
VARIANTS = {
    "color_then_360p_then_represented_vertical_smear_w03": "color_360p",
    "grayscale_bt709_then_360p_then_represented_vertical_smear_w03": "grayscale_bt709_then_360p",
    "protanopia_machado100_then_360p_then_represented_vertical_smear_w03": "protanopia_machado100_then_360p",
    "deuteranopia_machado100_then_360p_then_represented_vertical_smear_w03": "deuteranopia_machado100_then_360p",
    "tritanopia_machado100_then_360p_then_represented_vertical_smear_w03": "tritanopia_machado100_then_360p",
}
MATRICES = {
    "protanopia_machado100_then_360p": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]], dtype=np.float64),
    "deuteranopia_machado100_then_360p": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]], dtype=np.float64),
    "tritanopia_machado100_then_360p": np.array([[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]], dtype=np.float64),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def srgb_to_linear(a: np.ndarray) -> np.ndarray:
    x = a.astype(np.float64) / 255.0
    return np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(x: np.ndarray) -> np.ndarray:
    y = np.where(x <= 0.0031308, 12.92 * x, 1.055 * np.power(x, 1 / 2.4) - 0.055)
    return np.rint(np.clip(y, 0, 1) * 255.0).astype(np.uint8)


def represented(native: np.ndarray, baseline_name: str) -> np.ndarray:
    if baseline_name == "color_360p":
        prepared = native
    else:
        linear = srgb_to_linear(native)
        if baseline_name == "grayscale_bt709_then_360p":
            y = 0.2126 * linear[..., 0] + 0.7152 * linear[..., 1] + 0.0722 * linear[..., 2]
            prepared = linear_to_srgb(np.repeat(y[..., None], 3, axis=2))
        else:
            prepared = linear_to_srgb(np.clip(linear @ MATRICES[baseline_name].T, 0, 1))
    return np.asarray(Image.fromarray(prepared).resize((640, 360), Image.Resampling.LANCZOS), dtype=np.uint8)


def smear(a: np.ndarray) -> np.ndarray:
    pad = WIDTH // 2
    padded = np.pad(a.astype(np.uint64), ((pad, pad), (0, 0), (0, 0)), mode="edge")
    cumulative = np.concatenate([np.zeros((1, a.shape[1], a.shape[2]), dtype=np.uint64), np.cumsum(padded, axis=0, dtype=np.uint64)], axis=0)
    totals = cumulative[WIDTH:] - cumulative[:-WIDTH]
    return ((totals + WIDTH // 2) // WIDTH).astype(np.uint8)


def contact_sheet(paths: list[Path], labels: list[str], out: Path) -> tuple[int, int]:
    cols, tile_w, label_h = 2, 640, 28
    rows = (len(paths) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tile_w, rows * (360 + label_h)), (10, 12, 18))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for idx, (path, label) in enumerate(zip(paths, labels)):
        x, y = (idx % cols) * tile_w, (idx // cols) * (360 + label_h)
        with Image.open(path) as image:
            sheet.paste(image.convert("RGB"), (x, y + label_h))
        draw.text((x + 8, y + 8), label, fill=(240, 240, 240), font=font)
    sheet.save(out, optimize=False)
    return sheet.size


def main() -> None:
    pass23 = json.loads(PASS23.read_text())
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True)
    groups = {}
    baseline_matches = 0
    exact_smears = 0
    for name, prior_group in pass23["groups"].items():
        group_out = OUT / name
        frames_out = group_out / "frames"
        frames_out.mkdir(parents=True)
        by_variant: dict[str, list[Path]] = {key: [] for key in VARIANTS}
        labels: dict[str, list[str]] = {key: [] for key in VARIANTS}
        scenes = []
        for prior_scene in prior_group["scenes"]:
            scene = prior_scene["scene"]
            source = ROOT / prior_scene["source"]
            if sha(source) != prior_scene["source_sha256"]:
                raise SystemExit(f"source mismatch {name} S{scene}")
            with Image.open(source) as image:
                native = np.asarray(image.convert("RGB"), dtype=np.uint8)
            prior_samples = {item["variant"]: item for item in prior_scene["samples"]}
            samples = []
            for variant, baseline_name in VARIANTS.items():
                baseline = represented(native, baseline_name)
                prior_path = PASS23_ROOT / name / prior_samples[baseline_name]["frame"]
                with Image.open(prior_path) as image:
                    prior_pixels = np.asarray(image.convert("RGB"), dtype=np.uint8)
                if not np.array_equal(baseline, prior_pixels):
                    raise SystemExit(f"baseline mismatch {name} S{scene} {baseline_name}")
                baseline_matches += 1
                derived = smear(baseline)
                output = frames_out / f"scene_{scene:02d}_{variant}.png"
                Image.fromarray(derived).save(output, optimize=False)
                with Image.open(output) as image:
                    stored = np.asarray(image.convert("RGB"), dtype=np.uint8)
                if not np.array_equal(derived, stored):
                    raise SystemExit(f"smear mismatch {name} S{scene}")
                exact_smears += 1
                by_variant[variant].append(output)
                labels[variant].append(f"S{scene:02d} · {name} · {variant}")
                samples.append({"variant": variant, "baseline_variant": baseline_name, "baseline_path": str(prior_path.relative_to(ROOT)), "baseline_sha256": sha(prior_path), "frame": str(output.relative_to(group_out)), "frame_sha256": sha(output), "width": 640, "height": 360})
            scenes.append({"scene": scene, "source": str(source.relative_to(ROOT)), "source_sha256": sha(source), "samples": samples})
        sheets = {}
        for variant, paths in by_variant.items():
            path = group_out / f"contact_sheet_{variant}.png"
            width, height = contact_sheet(paths, labels[variant], path)
            sheets[variant] = {"path": path.name, "sha256": sha(path), "width": width, "height": height}
        groups[name] = {"group": name, "source_receipt": prior_group["source_receipt"], "source_receipt_sha256": prior_group["source_receipt_sha256"], "scene_count": len(scenes), "frame_count": len(scenes) * 5, "contact_sheets": sheets, "scenes": scenes}
    receipt = {
        "audit": "method_proofs_native_monochrome_and_color_vision_then_minimum_scale_then_represented_pixel_vertical_smear",
        "deepening_pass": 29,
        "created_at": PACKET_CREATED_AT,
        "frame_count": exact_smears,
        "pass23_baseline_match_count": baseline_matches,
        "exact_smear_recomputation_count": exact_smears,
        "transform": {"order": ["native color/monochrome presentation", "Pillow LANCZOS 640x360", "centered vertical width-3 box smear on represented pixels"], "axis": "vertical", "width_pixels_at_640x360": WIDTH, "edge_handling": "edge replication", "accumulator": "uint64", "rounding": "integer round half up", "pillow_version": pillow_version, "numpy_version": np.__version__, "png_optimize": False},
        "source_receipt": str(PASS23.relative_to(ROOT)),
        "source_receipt_sha256": sha(PASS23),
        "groups": groups,
        "audio_generated": False,
        "video_encoded": False,
        "git_action": False,
    }
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS groups={len(groups)} scenes={sum(g['scene_count'] for g in groups.values())} frames={exact_smears} baseline={baseline_matches}/105 smear={exact_smears}/105")


if __name__ == "__main__":
    main()

