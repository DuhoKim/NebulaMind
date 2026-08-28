#!/usr/bin/env python3
"""Fresh midpoint extraction plus deterministic monochrome/CVD QA variants."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
FRAMES = OUT / "frames"
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
EXPECTED_CANDIDATE_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
WIDTH, HEIGHT = 1920, 1080
VARIANTS = [
    "color",
    "grayscale_bt709",
    "protanopia_machado100",
    "deuteranopia_machado100",
    "tritanopia_machado100",
]
MATRICES = {
    "protanopia_machado100": np.array(
        [
            [0.152286, 1.052583, -0.204868],
            [0.114503, 0.786281, 0.099216],
            [-0.003882, -0.048116, 1.051998],
        ],
        dtype=np.float64,
    ),
    "deuteranopia_machado100": np.array(
        [
            [0.367322, 0.860646, -0.227968],
            [0.280085, 0.672501, 0.047413],
            [-0.011820, 0.042940, 0.968881],
        ],
        dtype=np.float64,
    ),
    "tritanopia_machado100": np.array(
        [
            [1.255528, -0.076749, -0.178779],
            [-0.078411, 0.930809, 0.147602],
            [0.004733, 0.691367, 0.303900],
        ],
        dtype=np.float64,
    ),
}
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=True)


def version_line(binary: str) -> str:
    return run([binary, "-version"]).stdout.splitlines()[0]


def duration_seconds() -> float:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(CANDIDATE),
        ]
    )
    return float(result.stdout.strip())


def scene_cuts() -> list[float]:
    detector_width, detector_height, detector_fps = 160, 90, 30
    process = subprocess.Popen(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(CANDIDATE),
            "-vf",
            f"fps={detector_fps},scale={detector_width}:{detector_height},format=gray",
            "-an",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "gray",
            "-",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if process.stdout is None:
        raise RuntimeError("ffmpeg detector stdout unavailable")
    frame_bytes = detector_width * detector_height
    previous: np.ndarray | None = None
    frame_index = 0
    scores: list[tuple[float, float]] = []
    while True:
        raw = process.stdout.read(frame_bytes)
        if len(raw) != frame_bytes:
            break
        current = np.frombuffer(raw, dtype=np.uint8)
        if previous is not None:
            score = float(np.abs(current.astype(np.int16) - previous.astype(np.int16)).mean())
            scores.append((frame_index / detector_fps, score))
        previous = current.copy()
        frame_index += 1
    process.stdout.close()
    if process.wait() != 0:
        raise RuntimeError("ffmpeg detector failed")
    selected: list[tuple[float, float]] = []
    for timestamp, score in sorted(scores, key=lambda item: item[1], reverse=True):
        if all(abs(timestamp - kept_time) >= 1.0 for kept_time, _ in selected):
            selected.append((timestamp, score))
            if len(selected) == 15:
                break
    if len(selected) != 15:
        raise RuntimeError(f"detector found only {len(selected)} separated peaks")
    return sorted(timestamp for timestamp, _ in selected)


def midpoint_ranges(cuts: list[float], duration: float) -> list[tuple[float, float, float]]:
    bounds = [0.0, *cuts, duration]
    return [
        (bounds[index], bounds[index + 1], (bounds[index] + bounds[index + 1]) / 2.0)
        for index in range(len(bounds) - 1)
    ]


def extract_color(midpoint: float, destination: Path) -> None:
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{midpoint:.6f}",
            "-i",
            str(CANDIDATE),
            "-frames:v",
            "1",
            "-vf",
            "scale=1920:1080:flags=lanczos",
            "-pix_fmt",
            "rgb24",
            "-y",
            str(destination),
        ]
    )


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, 1.0)
    return np.where(clipped <= 0.0031308, 12.92 * clipped, 1.055 * clipped ** (1.0 / 2.4) - 0.055)


def transform(source: Path, label: str, destination: Path) -> None:
    with Image.open(source).convert("RGB") as image:
        rgb = np.asarray(image, dtype=np.float64) / 255.0
    if label == "grayscale_bt709":
        linear = srgb_to_linear(rgb)
        luminance = (
            0.2126 * linear[:, :, 0]
            + 0.7152 * linear[:, :, 1]
            + 0.0722 * linear[:, :, 2]
        )
        transformed = linear_to_srgb(np.repeat(luminance[:, :, None], 3, axis=2))
    elif label in MATRICES:
        linear = srgb_to_linear(rgb)
        transformed_linear = np.einsum("...c,rc->...r", linear, MATRICES[label])
        transformed = linear_to_srgb(transformed_linear)
    else:
        raise ValueError(f"unknown transform: {label}")
    pixels = np.rint(np.clip(transformed, 0.0, 1.0) * 255.0).astype(np.uint8)
    Image.fromarray(pixels).save(destination, format="PNG", optimize=False)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_sheet(label: str, rows: list[dict[str, object]]) -> dict[str, object]:
    tile_w, image_h, label_h = 480, 270, 30
    tile_h = image_h + label_h
    sheet = Image.new("RGB", (tile_w * 4, tile_h * 4), (4, 8, 14))
    draw = ImageDraw.Draw(sheet)
    label_font = font(19)
    for index, row in enumerate(rows):
        frame = OUT / str(row["frame"])
        scene_number = row["scene"]
        if not isinstance(scene_number, int):
            raise TypeError("scene number must be integer")
        x = (index % 4) * tile_w
        y = (index // 4) * tile_h
        draw.rectangle((x, y, x + tile_w, y + label_h), fill=(4, 8, 14))
        draw.text((x + 8, y + 4), f"S{scene_number:02d} · {label}", fill=(242, 246, 252), font=label_font)
        with Image.open(frame).convert("RGB") as image:
            image.thumbnail((tile_w, image_h), Image.Resampling.LANCZOS)
            sheet.paste(image, (x, y + label_h))
    destination = OUT / f"contact_sheet_{label}.png"
    sheet.save(destination, format="PNG", optimize=False)
    return {
        "path": destination.relative_to(OUT).as_posix(),
        "sha256": sha256(destination),
        "width": sheet.width,
        "height": sheet.height,
    }


def main() -> None:
    for path in OUT.glob("contact_sheet_*.png"):
        path.unlink()
    receipt_path = OUT / "extraction_receipt.json"
    if receipt_path.exists():
        receipt_path.unlink()
    if FRAMES.exists():
        shutil.rmtree(FRAMES)
    FRAMES.mkdir(parents=True, exist_ok=True)

    candidate_sha = sha256(CANDIDATE)
    if candidate_sha != EXPECTED_CANDIDATE_SHA:
        raise SystemExit(f"candidate hash mismatch: {candidate_sha}")
    duration = duration_seconds()
    cuts = scene_cuts()
    ranges = midpoint_ranges(cuts, duration)
    if len(cuts) != 15 or len(ranges) != 16:
        raise SystemExit(f"unexpected scene structure: cuts={len(cuts)} scenes={len(ranges)}")

    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {key: [] for key in VARIANTS}
    for scene_number, (start, end, midpoint) in enumerate(ranges, start=1):
        color_rel = Path("frames") / f"scene_{scene_number:02d}_color.png"
        color_path = OUT / color_rel
        extract_color(midpoint, color_path)
        samples: list[dict[str, object]] = []
        for label in VARIANTS:
            if label == "color":
                frame_rel = color_rel
            else:
                frame_rel = Path("frames") / f"scene_{scene_number:02d}_{label}.png"
                transform(color_path, label, OUT / frame_rel)
            frame_path = OUT / frame_rel
            with Image.open(frame_path) as image:
                if image.mode != "RGB" or image.size != (WIDTH, HEIGHT):
                    raise SystemExit(f"invalid frame {frame_rel}: {image.mode} {image.size}")
            sample = {
                "variant": label,
                "frame": frame_rel.as_posix(),
                "frame_sha256": sha256(frame_path),
                "width": WIDTH,
                "height": HEIGHT,
            }
            samples.append(sample)
            by_variant[label].append({"scene": scene_number, **sample})
        scenes.append(
            {
                "scene": scene_number,
                "start_seconds": round(start, 6),
                "end_seconds": round(end, 6),
                "midpoint_seconds": round(midpoint, 6),
                "samples": samples,
            }
        )

    sheets = {label: make_sheet(label, rows) for label, rows in by_variant.items()}
    receipt = {
        "status": "QA_STATIC_PNGS_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 8,
        "audit": "monochrome_and_color_vision_redundancy",
        "simulation_scope": "presentation stress test only; not a clinical diagnostic",
        "extracted_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate_path": str(CANDIDATE),
        "candidate_sha256": candidate_sha,
        "candidate_expected_sha256": EXPECTED_CANDIDATE_SHA,
        "candidate_hash_match": True,
        "candidate_modified": False,
        "duration_seconds": round(duration, 6),
        "detected_cut_count": len(cuts),
        "detected_cut_times_seconds": [round(cut, 6) for cut in cuts],
        "scene_count": len(scenes),
        "variant_count": len(VARIANTS),
        "frame_count": len(scenes) * len(VARIANTS),
        "resolution": [WIDTH, HEIGHT],
        "variants": VARIANTS,
        "transform_contract": {
            "grayscale_bt709": "linear-light BT.709 luminance copied to RGB",
            "cvd_simulations": "Machado severity-100 matrices in linear RGB, clipped then converted to sRGB",
            "matrices": {key: value.tolist() for key, value in MATRICES.items()},
        },
        "scenes": scenes,
        "contact_sheets": sheets,
        "tools": {
            "python": platform.python_version(),
            "ffmpeg": version_line("ffmpeg"),
            "ffprobe": version_line("ffprobe"),
            "numpy": np.__version__,
            "pillow": Image.__version__,
        },
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
    }
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"PASS candidate={candidate_sha} cuts={len(cuts)} scenes={len(scenes)} "
        f"frames={receipt['frame_count']} variants={len(VARIANTS)}"
    )


if __name__ == "__main__":
    main()
