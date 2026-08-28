#!/usr/bin/env python3
"""Fresh candidate midpoints plus native color-vision transforms then 360p."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass23_minimum_scale_color_vision_audit"
FRAMES = OUT / "frames"
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
PREVIOUS = ROOT / "qa/pass22_minimum_scale_dark_tone_audit/extraction_receipt.json"
EXPECTED_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
PACKET_CREATED_AT = "2026-08-08T13:28:02+09:00"
NATIVE = (1920, 1080)
REPRESENTED = (640, 360)
VARIANTS = [
    "color_360p",
    "grayscale_bt709_then_360p",
    "protanopia_machado100_then_360p",
    "deuteranopia_machado100_then_360p",
    "tritanopia_machado100_then_360p",
]
MATRICES = {
    "protanopia_machado100": np.array(
        [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
        dtype=np.float64,
    ),
    "deuteranopia_machado100": np.array(
        [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
        dtype=np.float64,
    ),
    "tritanopia_machado100": np.array(
        [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]],
        dtype=np.float64,
    ),
}
FONTS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=True)


def version(binary: str) -> str:
    return run([binary, "-version"]).stdout.splitlines()[0]


def detect() -> tuple[float, list[float]]:
    duration = float(
        run(
            [
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", str(CANDIDATE),
            ]
        ).stdout.strip()
    )
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "info", "-i", str(CANDIDATE),
        "-vf", "scale=160:90,format=gray,select='gt(scene,0.03)',showinfo",
        "-an", "-f", "null", "-",
    ]
    completed = subprocess.run(cmd, text=True, capture_output=True, check=True)
    cuts: list[float] = []
    import re

    for line in completed.stderr.splitlines():
        match = re.search(r"pts_time:([0-9.]+)", line)
        if match:
            cuts.append(round(float(match.group(1)), 6))
    return duration, cuts


def extract(midpoint: float, target: Path) -> None:
    run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{midpoint:.6f}",
            "-i", str(CANDIDATE), "-frames:v", "1", "-vf",
            "scale=1920:1080:flags=lanczos", "-pix_fmt", "rgb24", "-y", str(target),
        ]
    )


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, 1.0)
    return np.where(clipped <= 0.0031308, 12.92 * clipped, 1.055 * clipped ** (1.0 / 2.4) - 0.055)


def color_transform(image: Image.Image, base_label: str) -> Image.Image:
    rgb = np.asarray(image.convert("RGB"), dtype=np.float64) / 255.0
    linear = srgb_to_linear(rgb)
    if base_label == "grayscale_bt709":
        luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
        transformed_linear = np.repeat(luminance[:, :, None], 3, axis=2)
    else:
        transformed_linear = np.einsum("...c,rc->...r", linear, MATRICES[base_label])
    transformed = linear_to_srgb(transformed_linear)
    pixels = np.rint(np.clip(transformed, 0.0, 1.0) * 255.0).astype(np.uint8)
    return Image.fromarray(pixels)


def derive(clean: Path, variant: str, target: Path) -> None:
    with Image.open(clean) as opened:
        native = opened.convert("RGB")
        if variant == "color_360p":
            transformed = native
        else:
            transformed = color_transform(native, variant.removesuffix("_then_360p"))
        represented = transformed.resize(REPRESENTED, Image.Resampling.LANCZOS)
        represented.save(target, format="PNG", optimize=False)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONTS:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def sheet(label: str, rows: list[dict[str, object]]) -> dict[str, object]:
    tile_w, tile_h, label_h = 640, 360, 28
    canvas = Image.new("RGB", (tile_w * 4, (tile_h + label_h) * 4), (4, 8, 14))
    draw = ImageDraw.Draw(canvas)
    face = font(18)
    for index, row in enumerate(rows):
        x = index % 4 * tile_w
        y = index // 4 * (tile_h + label_h)
        scene_value = row["scene"]
        if not isinstance(scene_value, int):
            raise TypeError("scene number must be int")
        draw.text((x + 8, y + 3), f"S{scene_value:02d} · {label}", fill=(240, 244, 250), font=face)
        with Image.open(OUT / str(row["frame"])) as image:
            canvas.paste(image.convert("RGB"), (x, y + label_h))
    path = OUT / f"contact_sheet_{label}.png"
    canvas.save(path, format="PNG", optimize=False)
    return {"path": path.relative_to(OUT).as_posix(), "sha256": sha(path), "width": canvas.width, "height": canvas.height}


def main() -> None:
    if sha(CANDIDATE) != EXPECTED_SHA:
        raise SystemExit("candidate hash mismatch")
    previous = json.loads(PREVIOUS.read_text())
    duration, cuts = detect()
    expected_cuts = previous["cut_times_seconds"]
    if cuts != expected_cuts or len(cuts) != 15:
        raise SystemExit(f"cut mismatch: {cuts}")
    if OUT.exists():
        shutil.rmtree(OUT)
    FRAMES.mkdir(parents=True)
    bounds = [0.0, *cuts, duration]
    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {key: [] for key in VARIANTS}
    prior_clean = {
        scene_number: next(sample for sample in record["samples"] if sample["variant"] == "clean")
        for scene_number, record in enumerate(previous["records"], start=1)
    }
    clean_matches = 0
    for scene_number in range(1, 17):
        midpoint = (bounds[scene_number - 1] + bounds[scene_number]) / 2.0
        clean = FRAMES / f"scene_{scene_number:02d}_clean_native.png"
        extract(midpoint, clean)
        prior = prior_clean[scene_number]
        prior_path = ROOT / "qa/pass22_minimum_scale_dark_tone_audit" / prior["frame"]
        clean_match = sha(clean) == prior["sha256"] == sha(prior_path)
        clean_matches += int(clean_match)
        samples: list[dict[str, object]] = []
        for variant in VARIANTS:
            frame = FRAMES / f"scene_{scene_number:02d}_{variant}.png"
            derive(clean, variant, frame)
            with Image.open(frame) as check:
                if check.mode != "RGB" or check.size != REPRESENTED:
                    raise SystemExit(f"invalid derivative {frame}")
            sample = {
                "variant": variant,
                "frame": frame.relative_to(OUT).as_posix(),
                "frame_sha256": sha(frame),
                "width": REPRESENTED[0],
                "height": REPRESENTED[1],
            }
            samples.append(sample)
            by_variant[variant].append({"scene": scene_number, **sample})
        scenes.append(
            {
                "scene": scene_number,
                "start_seconds": round(bounds[scene_number - 1], 6),
                "end_seconds": round(bounds[scene_number], 6),
                "midpoint_seconds": round(midpoint, 6),
                "native_clean": clean.relative_to(OUT).as_posix(),
                "native_clean_sha256": sha(clean),
                "previous_clean_sha256": prior["sha256"],
                "native_clean_byte_identical_to_pass22": clean_match,
                "samples": samples,
            }
        )
    sheets = {label: sheet(label, rows) for label, rows in by_variant.items()}
    receipt = {
        "status": "QA_STATIC_PNGS_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 23,
        "created_at": PACKET_CREATED_AT,
        "audit": "native_monochrome_and_color_vision_then_minimum_scale",
        "simulation_scope": "presentation stress test only; not a clinical diagnostic or named delivery/viewing standard",
        "candidate_path": str(CANDIDATE),
        "candidate_sha256": sha(CANDIDATE),
        "candidate_modified": False,
        "duration_seconds": round(duration, 6),
        "detected_cut_count": len(cuts),
        "detected_cut_times_seconds": cuts,
        "fresh_clean_match_count": clean_matches,
        "scene_count": 16,
        "variant_count": len(VARIANTS),
        "frame_count": 16 * len(VARIANTS),
        "native_resolution": list(NATIVE),
        "represented_resolution": list(REPRESENTED),
        "variant_order": VARIANTS,
        "transform_contract": {
            "color_360p": "native RGB to Pillow LANCZOS 640x360",
            "grayscale_bt709_then_360p": "native sRGB decode to linear light; BT.709 luminance copied to RGB; sRGB encode with np.rint; Pillow LANCZOS 640x360",
            "cvd_then_360p": "native sRGB decode to linear light; fixed Machado severity-100 matrix; clip; sRGB encode with np.rint; Pillow LANCZOS 640x360",
            "matrices": {key: value.tolist() for key, value in MATRICES.items()},
        },
        "scenes": scenes,
        "contact_sheets": sheets,
        "tools": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pillow": Image.__version__,
            "ffmpeg": version("ffmpeg"),
            "ffprobe": version("ffprobe"),
        },
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    (OUT / "extraction_receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS candidate={EXPECTED_SHA} cuts=15 scenes=16 frames=80 variants=5 clean={clean_matches}/16")


if __name__ == "__main__":
    main()
