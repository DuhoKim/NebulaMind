#!/usr/bin/env python3
"""Fresh candidate midpoints plus deterministic horizontal box-smear variants."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
FRAMES = OUT / "frames"
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
EXPECTED_CANDIDATE_SHA = (
    "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
)
PASS12_RECEIPT = ROOT / "qa/pass12_spatial_defocus_audit/extraction_receipt.json"
PASS12_CLEAN = ROOT / "qa/pass12_spatial_defocus_audit/frames/clean"
WIDTHS: dict[str, int | None] = {
    "clean": None,
    "smear_w03": 3,
    "smear_w07": 7,
    "smear_w13": 13,
    "smear_w21": 21,
}
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


def run(command: list[str]) -> bytes:
    return subprocess.run(command, check=True, capture_output=True).stdout


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ffprobe() -> dict[str, object]:
    return json.loads(
        run(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=width,height,r_frame_rate,pix_fmt:format=duration",
                "-of",
                "json",
                str(CANDIDATE),
            ]
        )
    )


def decode_gray_lowres() -> np.ndarray:
    raw = run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-i",
            str(CANDIDATE),
            "-map",
            "0:v:0",
            "-vf",
            "fps=30,scale=160:90:flags=area,format=gray",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "gray",
            "pipe:1",
        ]
    )
    frame_size = 160 * 90
    if len(raw) % frame_size:
        raise ValueError("low-resolution decode has a partial frame")
    return np.frombuffer(raw, dtype=np.uint8).reshape((-1, 90, 160))


def detect_cuts(frames: np.ndarray) -> tuple[list[int], list[float], dict[str, object]]:
    diffs = np.mean(
        np.abs(frames[1:].astype(np.int16) - frames[:-1].astype(np.int16)),
        axis=(1, 2),
    )
    ranked = np.argsort(diffs)[::-1]
    selected: list[int] = []
    for diff_index in ranked:
        incoming_frame = int(diff_index) + 1
        if all(abs(incoming_frame - previous) >= 30 for previous in selected):
            selected.append(incoming_frame)
            if len(selected) == 15:
                break
    selected.sort()
    cuts = [round(frame / 30.0, 6) for frame in selected]
    if cuts != EXPECTED_CUTS:
        raise ValueError(f"cut mismatch: {cuts}")
    ordered = sorted((float(diffs[frame - 1]), frame) for frame in selected)
    minimum_selected_score = ordered[0][0]
    excluded_maximum = max(
        float(score)
        for index, score in enumerate(diffs, start=1)
        if all(abs(index - frame) >= 30 for frame in selected)
    )
    detector = {
        "implementation": "30fps 160x90 grayscale mean-absolute frame difference",
        "nonmaximum_separation_frames": 30,
        "selected_incoming_frame_indices": selected,
        "cuts": cuts,
        "exact_pass12_match": True,
        "minimum_selected_score": round(minimum_selected_score, 9),
        "maximum_nonselected_score_outside_exclusion": round(excluded_maximum, 9),
        "minimum_selected_to_nonselected_ratio": round(
            minimum_selected_score / excluded_maximum, 9
        ),
    }
    return selected, cuts, detector


def scene_midpoints(cuts: list[float], duration_seconds: float) -> list[float]:
    boundaries = [0.0, *cuts, duration_seconds]
    return [
        round((boundaries[index] + boundaries[index + 1]) / 2.0, 6)
        for index in range(16)
    ]


def decode_frame(timestamp: float, destination: Path) -> Image.Image:
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
        return image.convert("RGB")


def horizontal_smear(image: Image.Image, width: int) -> Image.Image:
    if width <= 0 or width % 2 != 1:
        raise ValueError("smear width must be a positive odd integer")
    values = np.asarray(image.convert("RGB"), dtype=np.uint8)
    radius = width // 2
    padded = np.pad(values, ((0, 0), (radius, radius), (0, 0)), mode="edge")
    cumulative = np.cumsum(padded, axis=1, dtype=np.uint64)
    cumulative = np.concatenate(
        [np.zeros((values.shape[0], 1, 3), dtype=np.uint64), cumulative], axis=1
    )
    sums = cumulative[:, width:, :] - cumulative[:, :-width, :]
    smeared = ((sums + width // 2) // width).astype(np.uint8)
    if smeared.shape != values.shape:
        raise ValueError(f"smear shape mismatch: {smeared.shape}")
    return Image.fromarray(smeared)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def contact_sheet(paths: list[Path], labels: list[str], output: Path) -> None:
    thumb_size = (480, 270)
    columns = 4
    rows = (len(paths) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * 480, rows * 306), (5, 9, 15))
    draw = ImageDraw.Draw(sheet)
    label_font = font(18)
    for index, (path, label) in enumerate(zip(paths, labels)):
        with Image.open(path).convert("RGB") as image:
            thumb = image.resize(thumb_size, Image.Resampling.LANCZOS)
        x = (index % columns) * 480
        y = (index // columns) * 306
        sheet.paste(thumb, (x, y + 36))
        draw.text((x + 8, y + 8), label, font=label_font, fill=(240, 244, 250))
    sheet.save(output, format="PNG", optimize=False)


def main() -> None:
    if sha256(CANDIDATE) != EXPECTED_CANDIDATE_SHA:
        raise ValueError("candidate hash mismatch")
    if FRAMES.exists():
        shutil.rmtree(FRAMES)
    for variant in WIDTHS:
        (FRAMES / variant).mkdir(parents=True, exist_ok=True)

    probe = ffprobe()
    format_row = probe.get("format")
    if not isinstance(format_row, dict) or "duration" not in format_row:
        raise ValueError("ffprobe duration missing")
    duration_seconds = float(format_row["duration"])
    lowres = decode_gray_lowres()
    _cut_frames, cuts, detector = detect_cuts(lowres)
    midpoints = scene_midpoints(cuts, duration_seconds)
    pass12 = json.loads(PASS12_RECEIPT.read_text(encoding="utf-8"))
    if pass12["cut_detection"]["cuts"] != cuts:
        raise ValueError("pass12 receipt cut mismatch")

    records: list[dict[str, object]] = []
    sheets: dict[str, list[Path]] = {variant: [] for variant in WIDTHS}
    for scene, timestamp in enumerate(midpoints, start=1):
        clean_path = FRAMES / "clean" / f"scene_{scene:02d}.png"
        clean = decode_frame(timestamp, clean_path)
        if clean.size != (1920, 1080):
            raise ValueError(f"scene {scene} unexpected size {clean.size}")
        prior_clean = PASS12_CLEAN / f"scene_{scene:02d}.png"
        for variant, width in WIDTHS.items():
            output = FRAMES / variant / f"scene_{scene:02d}.png"
            if width is None:
                derived = clean
            else:
                derived = horizontal_smear(clean, width)
                derived.save(output, format="PNG", optimize=False)
            prior_sha = sha256(prior_clean) if width is None else None
            if width is None and sha256(output) != prior_sha:
                raise ValueError(f"scene {scene} clean frame differs from pass12")
            records.append(
                {
                    "scene": scene,
                    "timestamp_seconds": timestamp,
                    "variant": variant,
                    "kernel_width_pixels": width,
                    "path": output.relative_to(ROOT).as_posix(),
                    "png_sha256": sha256(output),
                    "pass12_clean_sha256": prior_sha,
                }
            )
            sheets[variant].append(output)

    sheet_hashes: dict[str, str] = {}
    for variant, paths in sheets.items():
        output = OUT / f"contact_sheet_{variant}.png"
        contact_sheet(paths, [f"S{scene} · {variant}" for scene in range(1, 17)], output)
        sheet_hashes[variant] = sha256(output)

    receipt = {
        "status": "QA_STATIC_PNGS_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION",
        "deepening_pass": 13,
        "created_at": datetime.now(ZoneInfo("Asia/Seoul")).isoformat(),
        "candidate_path": str(CANDIDATE),
        "candidate_sha256": EXPECTED_CANDIDATE_SHA,
        "ffprobe": probe,
        "decoder": {
            "ffmpeg_version": run(["ffmpeg", "-version"])
            .decode("utf-8")
            .splitlines()[0],
            "python_version": sys.version.split()[0],
            "numpy_version": np.__version__,
            "pillow_version": Image.__version__,
            "platform": platform.platform(),
        },
        "cut_detection": detector,
        "scene_count": 16,
        "variant_count": 5,
        "frame_count": 80,
        "variant_order": list(WIDTHS),
        "transform_contract": {
            "implementation": "centered horizontal box smear with edge replication, uint64 summed, round-half-up integer division",
            "kernel_widths_pixels": [3, 7, 13, 21],
            "axis": "horizontal",
            "source_mode": "RGB",
            "canvas_change": False,
        },
        "records": records,
        "contact_sheet_sha256": sheet_hashes,
        "fresh_clean_match": "16/16_PASS12_BYTE_IDENTICAL",
        "raw_ocr_text_stored": False,
        "scientific_adjudication_performed": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    (OUT / "extraction_receipt.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"PASS candidate={EXPECTED_CANDIDATE_SHA} cuts={len(cuts)} "
        f"scenes={len(midpoints)} frames={len(records)} variants={len(WIDTHS)}"
    )


if __name__ == "__main__":
    main()
