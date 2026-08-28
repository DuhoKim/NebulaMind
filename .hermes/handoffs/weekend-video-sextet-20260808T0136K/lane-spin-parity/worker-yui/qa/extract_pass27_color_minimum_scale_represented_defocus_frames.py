#!/usr/bin/env python3
"""Fresh native color/monochrome -> 360p -> represented-pixel Gaussian r0.5 audit."""

from __future__ import annotations

import hashlib
import json
import platform
import re
import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, __version__ as pillow_version

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[4]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
OUT = ROOT / "qa/pass27_color_minimum_scale_represented_defocus_audit"
FRAMES = OUT / "frames"
PASS26 = ROOT / "qa/pass26_color_minimum_scale_obstruction_audit/extraction_receipt.json"
PASS23 = ROOT / "qa/pass23_minimum_scale_color_vision_audit/extraction_receipt.json"
PACKET_CREATED_AT = "2026-08-08T15:03:55+09:00"
EXPECTED_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
DURATION = 243.3
RADIUS = 0.5
VARIANTS = {
    "color_then_360p_then_represented_gaussian_r0_50": "color_360p",
    "grayscale_bt709_then_360p_then_represented_gaussian_r0_50": "grayscale_bt709_then_360p",
    "protanopia_machado100_then_360p_then_represented_gaussian_r0_50": "protanopia_machado100_then_360p",
    "deuteranopia_machado100_then_360p_then_represented_gaussian_r0_50": "deuteranopia_machado100_then_360p",
    "tritanopia_machado100_then_360p_then_represented_gaussian_r0_50": "tritanopia_machado100_then_360p",
}
MATRICES = {
    "protanopia_machado100_then_360p": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]], dtype=np.float64),
    "deuteranopia_machado100_then_360p": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]], dtype=np.float64),
    "tritanopia_machado100_then_360p": np.array([[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]], dtype=np.float64),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def detect_cuts() -> list[float]:
    result = run(["ffmpeg", "-hide_banner", "-loglevel", "info", "-i", str(CANDIDATE), "-vf", "scale=160:90,format=gray,select='gt(scene,0.03)',showinfo", "-an", "-f", "null", "-"])
    cuts = []
    for value in re.findall(r"pts_time:([0-9.]+)", result.stderr):
        stamp = round(float(value), 6)
        if stamp > 0 and (not cuts or stamp != cuts[-1]):
            cuts.append(stamp)
    return cuts


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
    image = Image.fromarray(prepared)
    return np.asarray(image.resize((640, 360), Image.Resampling.LANCZOS), dtype=np.uint8)


def blur(a: np.ndarray) -> np.ndarray:
    return np.asarray(Image.fromarray(a).filter(ImageFilter.GaussianBlur(radius=RADIUS)), dtype=np.uint8)


def contact_sheet(paths: list[Path], labels: list[str], out: Path) -> tuple[int, int]:
    cols, tile_w, label_h = 4, 640, 28
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
    if sha(CANDIDATE) != EXPECTED_SHA:
        raise SystemExit("candidate hash mismatch")
    pass26 = json.loads(PASS26.read_text())
    pass23 = json.loads(PASS23.read_text())
    cuts = detect_cuts()
    expected = pass23["detected_cut_times_seconds"]
    if cuts != expected or cuts != pass26["detected_cut_times_seconds"] or len(cuts) != 15:
        raise SystemExit(f"cut mismatch: {cuts}")
    shutil.rmtree(OUT, ignore_errors=True)
    FRAMES.mkdir(parents=True)
    boundaries = [0.0, *cuts, DURATION]
    scenes = []
    fresh_clean = 0
    baseline_matches = 0
    exact_blurs = 0
    by_variant: dict[str, list[Path]] = {key: [] for key in VARIANTS}
    labels: dict[str, list[str]] = {key: [] for key in VARIANTS}
    for index in range(16):
        number = index + 1
        midpoint = round((boundaries[index] + boundaries[index + 1]) / 2, 6)
        clean = FRAMES / f"scene_{number:02d}_clean_native.png"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{midpoint:.6f}", "-i", str(CANDIDATE), "-frames:v", "1", "-pix_fmt", "rgb24", "-y", str(clean)])
        prior_clean = PASS26.parent / pass26["scenes"][index]["native_clean"]
        identical = clean.read_bytes() == prior_clean.read_bytes()
        if not identical or sha(clean) != pass26["scenes"][index]["native_clean_sha256"]:
            raise SystemExit(f"native mismatch scene {number}")
        fresh_clean += 1
        with Image.open(clean) as image:
            native = np.asarray(image.convert("RGB"), dtype=np.uint8)
        samples = []
        pass23_samples = {item["variant"]: item for item in pass23["scenes"][index]["samples"]}
        for variant, baseline_name in VARIANTS.items():
            baseline = represented(native, baseline_name)
            baseline_path = ROOT / "qa/pass23_minimum_scale_color_vision_audit" / pass23_samples[baseline_name]["frame"]
            with Image.open(baseline_path) as image:
                stored_baseline = np.asarray(image.convert("RGB"), dtype=np.uint8)
            if not np.array_equal(baseline, stored_baseline):
                raise SystemExit(f"baseline mismatch scene {number} {baseline_name}")
            baseline_matches += 1
            derived = blur(baseline)
            output = FRAMES / f"scene_{number:02d}_{variant}.png"
            Image.fromarray(derived).save(output, optimize=False)
            with Image.open(output) as image:
                saved = np.asarray(image.convert("RGB"), dtype=np.uint8)
            if not np.array_equal(derived, saved):
                raise SystemExit(f"blur mismatch scene {number} {variant}")
            exact_blurs += 1
            by_variant[variant].append(output)
            labels[variant].append(f"S{number:02d} · {variant}")
            samples.append({"variant": variant, "baseline_variant": baseline_name, "baseline_path": str(baseline_path.relative_to(ROOT)), "baseline_sha256": sha(baseline_path), "frame": str(output.relative_to(OUT)), "frame_sha256": sha(output), "width": 640, "height": 360})
        scenes.append({"scene": number, "start_seconds": boundaries[index], "end_seconds": boundaries[index + 1], "midpoint_seconds": midpoint, "native_clean": str(clean.relative_to(ROOT)), "native_clean_sha256": sha(clean), "native_clean_byte_identical_to_pass26": identical, "samples": samples})
    sheets = {}
    for variant, paths in by_variant.items():
        path = OUT / f"contact_sheet_{variant}.png"
        width, height = contact_sheet(paths, labels[variant], path)
        sheets[variant] = {"path": path.name, "sha256": sha(path), "width": width, "height": height}
    receipt = {
        "audit": "native_monochrome_and_color_vision_then_minimum_scale_then_represented_pixel_gaussian_defocus",
        "deepening_pass": 27,
        "created_at": PACKET_CREATED_AT,
        "candidate_path": str(CANDIDATE),
        "candidate_sha256": sha(CANDIDATE),
        "candidate_modified": False,
        "duration_seconds": DURATION,
        "detected_cut_count": len(cuts),
        "detected_cut_times_seconds": cuts,
        "scene_count": 16,
        "fresh_clean_match_count": fresh_clean,
        "pass23_baseline_match_count": baseline_matches,
        "frame_count": exact_blurs,
        "exact_blur_recomputation_count": exact_blurs,
        "native_resolution": [1920, 1080],
        "represented_resolution": [640, 360],
        "transform": {"order": ["native color/monochrome presentation", "Pillow LANCZOS 640x360", "Pillow GaussianBlur on represented pixels"], "radius_pixels_at_640x360": RADIUS, "pillow_version": pillow_version, "numpy_version": np.__version__, "python_version": platform.python_version(), "png_optimize": False},
        "source_receipts": {"pass26": str(PASS26.relative_to(ROOT)), "pass26_sha256": sha(PASS26), "pass23": str(PASS23.relative_to(ROOT)), "pass23_sha256": sha(PASS23)},
        "contact_sheets": sheets,
        "scenes": scenes,
        "audio_generated": False,
        "video_encoded": False,
        "git_action": False,
    }
    (OUT / "extraction_receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS candidate={sha(CANDIDATE)} cuts={len(cuts)} scenes=16 frames={exact_blurs} clean={fresh_clean}/16 baseline={baseline_matches}/80 blur={exact_blurs}/80")


if __name__ == "__main__":
    main()
