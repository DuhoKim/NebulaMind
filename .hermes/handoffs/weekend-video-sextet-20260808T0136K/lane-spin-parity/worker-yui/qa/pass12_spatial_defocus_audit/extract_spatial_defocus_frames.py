#!/usr/bin/env python3
"""Fresh candidate midpoints plus deterministic Gaussian spatial-defocus variants."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, __version__ as pillow_version

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
EXPECTED_CANDIDATE_SHA = (
    "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
)
EXPECTED_CUTS = [
    12.133333,
    26.366667,
    47.266667,
    60.466667,
    74.666667,
    88.066667,
    102.333333,
    116.333333,
    131.033333,
    148.033333,
    162.033333,
    179.733333,
    196.8,
    213.433333,
    233.866667,
]
VARIANTS: dict[str, float | None] = {
    "clean": None,
    "defocus_r0_75": 0.75,
    "defocus_r1_50": 1.5,
    "defocus_r2_50": 2.5,
    "defocus_r4_00": 4.0,
}
PREVIOUS_CLEAN = ROOT / "qa" / "pass11_recompression_audit" / "frames" / "clean"
FPS = 30
SMALL_WIDTH = 160
SMALL_HEIGHT = 90
MIN_CUT_SEPARATION_FRAMES = 30
CUT_COUNT = 15
WIDTH = 1920
HEIGHT = 1080
DURATION_SECONDS = 243.3


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ffmpeg_version() -> str:
    line = subprocess.check_output(["ffmpeg", "-version"], text=True).splitlines()[0]
    return line.strip()


def detect_cuts() -> list[float]:
    command = [
        "ffmpeg",
        "-v",
        "error",
        "-i",
        str(CANDIDATE),
        "-an",
        "-vf",
        f"fps={FPS},scale={SMALL_WIDTH}:{SMALL_HEIGHT}:flags=bilinear,format=gray",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "gray",
        "-",
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    assert process.stdout is not None
    frame_bytes = SMALL_WIDTH * SMALL_HEIGHT
    previous: np.ndarray | None = None
    scores: list[tuple[float, int]] = []
    frame_index = 0
    while True:
        raw = process.stdout.read(frame_bytes)
        if not raw:
            break
        if len(raw) != frame_bytes:
            raise RuntimeError("partial raw frame during cut detection")
        current = np.frombuffer(raw, dtype=np.uint8).astype(np.int16)
        if previous is not None:
            scores.append((float(np.abs(current - previous).mean()), frame_index))
        previous = current
        frame_index += 1
    return_code = process.wait()
    if return_code != 0:
        raise RuntimeError(f"ffmpeg cut detector failed: {return_code}")

    selected: list[tuple[float, int]] = []
    for score, index in sorted(scores, reverse=True):
        if all(
            abs(index - prior_index) >= MIN_CUT_SEPARATION_FRAMES
            for _, prior_index in selected
        ):
            selected.append((score, index))
        if len(selected) == CUT_COUNT:
            break
    if len(selected) != CUT_COUNT:
        raise RuntimeError(f"expected {CUT_COUNT} cuts, found {len(selected)}")
    return sorted(round(index / FPS, 6) for _, index in selected)


def midpoints(cuts: list[float]) -> list[float]:
    boundaries = [0.0, *cuts, DURATION_SECONDS]
    return [
        round((boundaries[index] + boundaries[index + 1]) / 2.0, 6)
        for index in range(16)
    ]


def extract_clean(timestamp: float, destination: Path) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-ss",
            f"{timestamp:.6f}",
            "-i",
            str(CANDIDATE),
            "-frames:v",
            "1",
            "-pix_fmt",
            "rgb24",
            "-y",
            str(destination),
        ],
        check=True,
    )
    with Image.open(destination) as image:
        if image.mode != "RGB" or image.size != (WIDTH, HEIGHT):
            raise RuntimeError(
                f"unexpected clean frame {destination.name}: {image.mode} {image.size}"
            )


def apply_defocus(source: Path, destination: Path, radius: float) -> None:
    with Image.open(source) as opened:
        image = opened.convert("RGB")
        image.filter(ImageFilter.GaussianBlur(radius=radius)).save(
            destination, format="PNG", optimize=False
        )


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_contact_sheet(
    frame_paths: list[Path], variant: str, destination: Path
) -> None:
    thumb_w, thumb_h = 480, 270
    label_h = 36
    sheet = Image.new("RGB", (thumb_w * 4, (thumb_h + label_h) * 4), (8, 12, 20))
    draw = ImageDraw.Draw(sheet)
    label_font = font(22)
    for index, frame_path in enumerate(frame_paths):
        with Image.open(frame_path) as opened:
            thumb = opened.convert("RGB").resize(
                (thumb_w, thumb_h), Image.Resampling.LANCZOS
            )
        x = (index % 4) * thumb_w
        y = (index // 4) * (thumb_h + label_h)
        sheet.paste(thumb, (x, y))
        draw.text(
            (x + 10, y + thumb_h + 5),
            f"S{index + 1:02d} · {variant}",
            fill=(235, 240, 247),
            font=label_font,
        )
    sheet.save(destination, format="PNG", optimize=False)


def main() -> None:
    candidate_sha = sha256(CANDIDATE)
    if candidate_sha != EXPECTED_CANDIDATE_SHA:
        raise SystemExit(f"candidate hash mismatch: {candidate_sha}")

    cuts = detect_cuts()
    if cuts != EXPECTED_CUTS:
        raise SystemExit(f"cut mismatch: {cuts}")
    times = midpoints(cuts)

    frames_root = OUT / "frames"
    if frames_root.exists():
        shutil.rmtree(frames_root)
    frames_root.mkdir(parents=True)

    records: list[dict[str, object]] = []
    by_variant: dict[str, list[Path]] = {variant: [] for variant in VARIANTS}
    for scene_index, timestamp in enumerate(times, start=1):
        clean_dir = frames_root / "clean"
        clean_dir.mkdir(parents=True, exist_ok=True)
        clean_path = clean_dir / f"scene_{scene_index:02d}.png"
        extract_clean(timestamp, clean_path)
        prior_clean = PREVIOUS_CLEAN / clean_path.name
        if not prior_clean.exists() or sha256(clean_path) != sha256(prior_clean):
            raise SystemExit(
                f"clean midpoint does not reproduce pass 11: scene {scene_index}"
            )

        records.append(
            {
                "scene": scene_index,
                "timestamp_seconds": timestamp,
                "variant": "clean",
                "radius_pixels": None,
                "path": clean_path.relative_to(ROOT).as_posix(),
                "png_sha256": sha256(clean_path),
                "mode": "RGB",
                "size": [WIDTH, HEIGHT],
            }
        )
        by_variant["clean"].append(clean_path)

        for variant, radius in VARIANTS.items():
            if radius is None:
                continue
            variant_dir = frames_root / variant
            variant_dir.mkdir(parents=True, exist_ok=True)
            output_path = variant_dir / clean_path.name
            apply_defocus(clean_path, output_path, radius)
            with Image.open(output_path) as image:
                if image.mode != "RGB" or image.size != (WIDTH, HEIGHT):
                    raise RuntimeError(
                        f"unexpected derivative {output_path}: {image.mode} {image.size}"
                    )
            records.append(
                {
                    "scene": scene_index,
                    "timestamp_seconds": timestamp,
                    "variant": variant,
                    "radius_pixels": radius,
                    "path": output_path.relative_to(ROOT).as_posix(),
                    "png_sha256": sha256(output_path),
                    "mode": "RGB",
                    "size": [WIDTH, HEIGHT],
                }
            )
            by_variant[variant].append(output_path)

    contact_hashes: dict[str, str] = {}
    for variant, paths in by_variant.items():
        sheet = OUT / f"contact_sheet_{variant}.png"
        make_contact_sheet(paths, variant, sheet)
        contact_hashes[variant] = sha256(sheet)

    receipt = {
        "status": "QA_STATIC_PNG_DERIVATIVES_NOT_A_CANDIDATE",
        "created_at": datetime.now(timezone.utc).astimezone().isoformat(),
        "candidate": str(CANDIDATE),
        "candidate_sha256": candidate_sha,
        "candidate_modified": False,
        "ffmpeg_version": ffmpeg_version(),
        "python_version": platform.python_version(),
        "pillow_version": pillow_version,
        "cut_detection": {
            "method": "30fps 160x90 grayscale frame-difference peaks with 30-frame nonmaximum separation",
            "cuts": cuts,
            "exact_pass11_match": True,
        },
        "scene_count": 16,
        "variant_count": len(VARIANTS),
        "frame_count": len(records),
        "variant_order": list(VARIANTS),
        "variants": {
            name: {"radius_pixels": radius} for name, radius in VARIANTS.items()
        },
        "transform_contract": {
            "implementation": "Pillow ImageFilter.GaussianBlur",
            "source_mode": "RGB",
            "radii_pixels": [0.75, 1.5, 2.5, 4.0],
            "canvas_change": False,
            "storage": "filtered RGB pixels saved as non-optimized PNG",
            "scope_limit": "deterministic spatial-defocus presentation stress only; radii are packet parameters, not claims about a named lens, projector, display, viewer, or service",
        },
        "clean_reproduction": "16/16 pass11 clean midpoint PNGs byte-identical",
        "contact_sheet_sha256": contact_hashes,
        "records": records,
        "video_or_audio_created": False,
        "tts_invoked": False,
        "git_action": False,
    }
    (OUT / "extraction_receipt.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"PASS candidate={candidate_sha} cuts={len(cuts)} scenes=16 "
        f"frames={len(records)} variants={len(VARIANTS)}"
    )


if __name__ == "__main__":
    main()
