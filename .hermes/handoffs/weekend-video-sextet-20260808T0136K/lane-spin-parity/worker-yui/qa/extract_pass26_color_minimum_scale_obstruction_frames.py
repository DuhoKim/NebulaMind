#!/usr/bin/env python3
"""Fresh native color/monochrome -> 360p -> opaque bottom-25% obstruction audit."""

from __future__ import annotations

import hashlib
import json
import platform
import re
import shutil
import subprocess
from pathlib import Path

import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass26_color_minimum_scale_obstruction_audit"
FRAMES = OUT / "frames"
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
PASS25 = ROOT / "qa/pass25_color_minimum_scale_black_lift_audit/extraction_receipt.json"
PASS23 = ROOT / "qa/pass23_minimum_scale_color_vision_audit/extraction_receipt.json"
EXPECTED_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
PACKET_CREATED_AT = "2026-08-08T14:43:01+09:00"
NATIVE = (1920, 1080)
REPRESENTED = (640, 360)
MASK_FRACTION = 0.25
MASK_TOP_Y = 270
MASK_RGB = np.array([0, 0, 0], dtype=np.uint8)
VARIANTS = [
    "color_then_360p_then_bottom25",
    "grayscale_bt709_then_360p_then_bottom25",
    "protanopia_machado100_then_360p_then_bottom25",
    "deuteranopia_machado100_then_360p_then_bottom25",
    "tritanopia_machado100_then_360p_then_bottom25",
]
BASELINE_VARIANTS = {
    "color_then_360p_then_bottom25": "color_360p",
    "grayscale_bt709_then_360p_then_bottom25": "grayscale_bt709_then_360p",
    "protanopia_machado100_then_360p_then_bottom25": "protanopia_machado100_then_360p",
    "deuteranopia_machado100_then_360p_then_bottom25": "deuteranopia_machado100_then_360p",
    "tritanopia_machado100_then_360p_then_bottom25": "tritanopia_machado100_then_360p",
}
MATRICES = {
    "protanopia_machado100": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]], dtype=np.float64),
    "deuteranopia_machado100": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]], dtype=np.float64),
    "tritanopia_machado100": np.array([[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]], dtype=np.float64),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=True)


def version(binary: str) -> str:
    return run([binary, "-version"]).stdout.splitlines()[0]


def detect() -> tuple[float, list[float]]:
    duration = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(CANDIDATE)]).stdout.strip())
    completed = subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "info", "-i", str(CANDIDATE),
        "-vf", "scale=160:90,format=gray,select='gt(scene,0.03)',showinfo", "-an", "-f", "null", "-",
    ], text=True, capture_output=True, check=True)
    cuts = [round(float(match.group(1)), 6) for line in completed.stderr.splitlines() if (match := re.search(r"pts_time:([0-9.]+)", line))]
    return duration, cuts


def extract(midpoint: float, target: Path) -> None:
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{midpoint:.6f}", "-i", str(CANDIDATE), "-frames:v", "1", "-vf", "scale=1920:1080:flags=lanczos", "-pix_fmt", "rgb24", "-y", str(target)])


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, 1.0)
    return np.where(clipped <= 0.0031308, 12.92 * clipped, 1.055 * clipped ** (1.0 / 2.4) - 0.055)


def represented(native: Image.Image, baseline_variant: str) -> Image.Image:
    if baseline_variant == "color_360p":
        transformed = native.convert("RGB")
    else:
        label = baseline_variant.removesuffix("_then_360p")
        linear = srgb_to_linear(np.asarray(native.convert("RGB"), dtype=np.float64) / 255.0)
        if label == "grayscale_bt709":
            luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
            transformed_linear = np.repeat(luminance[:, :, None], 3, axis=2)
        else:
            transformed_linear = np.einsum("...c,rc->...r", linear, MATRICES[label])
        transformed = Image.fromarray(np.rint(linear_to_srgb(transformed_linear) * 255.0).astype(np.uint8))
    return transformed.resize(REPRESENTED, Image.Resampling.LANCZOS)


def obstruct(image: Image.Image) -> Image.Image:
    pixels = np.asarray(image.convert("RGB"), dtype=np.uint8).copy()
    pixels[MASK_TOP_Y:, :, :] = MASK_RGB
    return Image.fromarray(pixels)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def sheet(label: str, rows: list[dict[str, object]]) -> dict[str, object]:
    tile_w, tile_h, label_h = 640, 360, 28
    canvas = Image.new("RGB", (tile_w * 4, (tile_h + label_h) * 4), (4, 8, 14))
    draw = ImageDraw.Draw(canvas)
    face = font(18)
    for index, row in enumerate(rows):
        x, y = index % 4 * tile_w, index // 4 * (tile_h + label_h)
        scene_value = row["scene"]
        if not isinstance(scene_value, int):
            raise TypeError("scene must be int")
        draw.text((x + 8, y + 3), f"S{scene_value:02d} · {label}", fill=(240, 244, 250), font=face)
        with Image.open(OUT / str(row["frame"])) as image:
            canvas.paste(image.convert("RGB"), (x, y + label_h))
    path = OUT / f"contact_sheet_{label}.png"
    canvas.save(path, format="PNG", optimize=False)
    return {"path": path.relative_to(OUT).as_posix(), "sha256": sha(path), "width": canvas.width, "height": canvas.height}


def main() -> None:
    if sha(CANDIDATE) != EXPECTED_SHA:
        raise SystemExit("candidate hash mismatch")
    pass25 = json.loads(PASS25.read_text())
    pass23 = json.loads(PASS23.read_text())
    duration, cuts = detect()
    if cuts != pass25["detected_cut_times_seconds"] or cuts != pass23["detected_cut_times_seconds"] or len(cuts) != 15:
        raise SystemExit(f"cut mismatch: {cuts}")
    if OUT.exists():
        shutil.rmtree(OUT)
    FRAMES.mkdir(parents=True)
    bounds = [0.0, *cuts, duration]
    prior25 = {int(row["scene"]): row for row in pass25["scenes"]}
    prior23 = {int(row["scene"]): row for row in pass23["scenes"]}
    clean_matches = 0
    baseline_matches = 0
    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {variant: [] for variant in VARIANTS}
    for number in range(1, 17):
        midpoint = (bounds[number - 1] + bounds[number]) / 2.0
        clean = FRAMES / f"scene_{number:02d}_clean_native.png"
        extract(midpoint, clean)
        previous_clean = ROOT / "qa/pass25_color_minimum_scale_black_lift_audit" / prior25[number]["native_clean"]
        clean_match = sha(clean) == prior25[number]["native_clean_sha256"] == sha(previous_clean)
        clean_matches += int(clean_match)
        prior_samples = {sample["variant"]: sample for sample in prior23[number]["samples"]}
        samples: list[dict[str, object]] = []
        with Image.open(clean) as opened:
            native = opened.convert("RGB")
            for variant in VARIANTS:
                baseline_variant = BASELINE_VARIANTS[variant]
                baseline = represented(native, baseline_variant)
                prior = prior_samples[baseline_variant]
                prior_path = ROOT / "qa/pass23_minimum_scale_color_vision_audit" / prior["frame"]
                with Image.open(prior_path) as prior_image:
                    baseline_match = np.array_equal(np.asarray(baseline), np.asarray(prior_image.convert("RGB")))
                baseline_matches += int(baseline_match)
                derivative = obstruct(baseline)
                base_pixels = np.asarray(baseline, dtype=np.uint8)
                derivative_pixels = np.asarray(derivative, dtype=np.uint8)
                top_exact = bool(np.array_equal(base_pixels[:MASK_TOP_Y], derivative_pixels[:MASK_TOP_Y]))
                mask_exact = bool(np.all(derivative_pixels[MASK_TOP_Y:] == MASK_RGB))
                frame = FRAMES / f"scene_{number:02d}_{variant}.png"
                derivative.save(frame, format="PNG", optimize=False)
                sample = {
                    "variant": variant,
                    "baseline_variant": baseline_variant,
                    "baseline_pass23_frame": prior["frame"],
                    "baseline_pass23_frame_sha256": prior["frame_sha256"],
                    "baseline_recomputed_pixel_exact": baseline_match,
                    "mask_fraction": MASK_FRACTION,
                    "mask_top_y": MASK_TOP_Y,
                    "mask_color_rgb": MASK_RGB.tolist(),
                    "unobstructed_pixels_exact": top_exact,
                    "masked_pixels_exact": mask_exact,
                    "frame": frame.relative_to(OUT).as_posix(),
                    "frame_sha256": sha(frame),
                    "width": 640,
                    "height": 360,
                }
                samples.append(sample)
                by_variant[variant].append({"scene": number, **sample})
        scenes.append({
            "scene": number,
            "start_seconds": round(bounds[number - 1], 6),
            "end_seconds": round(bounds[number], 6),
            "midpoint_seconds": round(midpoint, 6),
            "native_clean": clean.relative_to(OUT).as_posix(),
            "native_clean_sha256": sha(clean),
            "previous_clean_sha256": prior25[number]["native_clean_sha256"],
            "native_clean_byte_identical_to_pass25": clean_match,
            "samples": samples,
        })
    receipt = {
        "status": "QA_STATIC_PNG_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 26,
        "created_at": PACKET_CREATED_AT,
        "audit": "native_monochrome_or_color_vision_then_minimum_scale_then_bottom25_obstruction",
        "simulation_scope": "packet-specific presentation stress only; not a clinical diagnostic or named caption/player/viewing standard",
        "candidate_path": str(CANDIDATE),
        "candidate_sha256": sha(CANDIDATE),
        "candidate_modified": False,
        "duration_seconds": round(duration, 6),
        "detected_cut_count": len(cuts),
        "detected_cut_times_seconds": cuts,
        "fresh_clean_match_count": clean_matches,
        "baseline_pass23_pixel_match_count": baseline_matches,
        "scene_count": 16,
        "variant_count": 5,
        "frame_count": 80,
        "native_resolution": list(NATIVE),
        "represented_resolution": list(REPRESENTED),
        "variant_order": VARIANTS,
        "baseline_variant_map": BASELINE_VARIANTS,
        "transform_contract": {
            "order": "native RGB -> color or linear-light BT.709 grayscale/fixed Machado severity-100 matrix -> sRGB np.rint uint8 -> Pillow LANCZOS 640x360 -> opaque RGB black rows 270..359",
            "mask_fraction": MASK_FRACTION,
            "mask_top_y": MASK_TOP_Y,
            "mask_color_rgb": MASK_RGB.tolist(),
            "unobstructed_pixel_contract": "all RGB pixels in rows 0..269 byte-identical to matching lossless pass23 represented baseline",
            "matrices": {key: value.tolist() for key, value in MATRICES.items()},
        },
        "scenes": scenes,
        "contact_sheets": {variant: sheet(variant, rows) for variant, rows in by_variant.items()},
        "tools": {"python": platform.python_version(), "numpy": np.__version__, "pillow": PIL.__version__, "ffmpeg": version("ffmpeg"), "ffprobe": version("ffprobe")},
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    (OUT / "extraction_receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS candidate={EXPECTED_SHA} cuts=15 scenes=16 frames=80 clean={clean_matches}/16 baseline={baseline_matches}/80 mask=80/80")


if __name__ == "__main__":
    main()
