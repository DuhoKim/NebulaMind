#!/usr/bin/env python3
"""Reproduce pass-14 candidate cuts, midpoints, and shadow-floor PNG evidence."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass14_shadow_floor_audit"
FRAMES = OUT / "frames"
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
PASS13_FRAMES = ROOT / "qa/pass13_directional_smear_audit/frames/clean"
EXPECTED_CANDIDATE_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
VARIANTS: dict[str, int | None] = {
    "clean": None,
    "shadow_floor_08": 8,
    "shadow_floor_16": 16,
    "shadow_floor_32": 32,
    "shadow_floor_48": 48,
}


def run(command: list[str]) -> str:
    return subprocess.run(command, check=True, capture_output=True, text=True).stdout


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def detect_cuts() -> tuple[list[int], list[float], dict[str, float]]:
    payload = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(CANDIDATE), "-an", "-vf", "fps=30,scale=160:90:flags=area,format=gray", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
        check=True,
        capture_output=True,
    ).stdout
    frame_size = 160 * 90
    if len(payload) % frame_size:
        raise ValueError("detector payload is not frame aligned")
    frames = np.frombuffer(payload, dtype=np.uint8).reshape((-1, 90, 160))
    scores = np.mean(np.abs(frames[1:].astype(np.int16) - frames[:-1].astype(np.int16)), axis=(1, 2))
    selected: list[int] = []
    for candidate_index in np.argsort(scores)[::-1]:
        incoming = int(candidate_index) + 1
        if all(abs(incoming - previous) >= 30 for previous in selected):
            selected.append(incoming)
            if len(selected) == 15:
                break
    selected.sort()
    cuts = [round(frame / 30.0, 6) for frame in selected]
    outside = [float(score) for index, score in enumerate(scores) if all(abs((index + 1) - frame) >= 30 for frame in selected)]
    minimum_selected = min(float(scores[frame - 1]) for frame in selected)
    maximum_outside = max(outside)
    return selected, cuts, {
        "minimum_selected_score": round(minimum_selected, 9),
        "maximum_nonselected_score_outside_exclusion": round(maximum_outside, 9),
        "minimum_selected_to_nonselected_ratio": round(minimum_selected / maximum_outside, 9),
    }


def midpoint_timestamps(cuts: list[float], duration: float) -> list[float]:
    bounds = [0.0, *cuts, duration]
    return [round((left + right) / 2.0, 6) for left, right in zip(bounds, bounds[1:])]


def decode(timestamp: float, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", f"{timestamp:.6f}", "-i", str(CANDIDATE), "-frames:v", "1", "-pix_fmt", "rgb24", "-f", "image2", str(output)],
        check=True,
    )


def luma(values: np.ndarray) -> np.ndarray:
    data = values.astype(np.uint32)
    return ((54 * data[:, :, 0] + 183 * data[:, :, 1] + 19 * data[:, :, 2] + 128) // 256).astype(np.uint16)


def shadow_floor(image: Image.Image, floor: int) -> Image.Image:
    values = np.asarray(image.convert("RGB"), dtype=np.uint8)
    lum = luma(values).astype(np.uint32)
    numerator = np.maximum(lum.astype(np.int32) - floor, 0).astype(np.uint32) * 255
    remapped = (numerator + (255 - floor) // 2) // (255 - floor)
    output = np.zeros_like(values, dtype=np.uint8)
    nonzero = lum > 0
    for channel in range(3):
        scaled = np.zeros_like(lum, dtype=np.uint32)
        scaled[nonzero] = (values[:, :, channel].astype(np.uint32)[nonzero] * remapped[nonzero] + lum[nonzero] // 2) // lum[nonzero]
        output[:, :, channel] = np.clip(scaled, 0, 255).astype(np.uint8)
    return Image.fromarray(output)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def contact_sheet(paths: list[Path], labels: list[str], output: Path) -> None:
    cell_w, cell_h, label_h, columns = 480, 270, 36, 4
    rows = (len(paths) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_w, rows * (cell_h + label_h)), (4, 8, 14))
    draw = ImageDraw.Draw(sheet)
    label_font = font(19)
    for index, (path, label) in enumerate(zip(paths, labels)):
        with Image.open(path).convert("RGB") as image:
            thumb = image.resize((cell_w, cell_h), Image.Resampling.LANCZOS)
        x = (index % columns) * cell_w
        y = (index // columns) * (cell_h + label_h)
        sheet.paste(thumb, (x, y + label_h))
        draw.text((x + 8, y + 7), label, fill=(240, 244, 250), font=label_font)
    sheet.save(output, format="PNG", optimize=False)


def main() -> None:
    if FRAMES.exists():
        shutil.rmtree(FRAMES)
    for old_sheet in OUT.glob("contact_sheet_*.png"):
        old_sheet.unlink()
    OUT.mkdir(parents=True, exist_ok=True)
    candidate_sha = sha256(CANDIDATE)
    if candidate_sha != EXPECTED_CANDIDATE_SHA:
        raise ValueError("candidate hash differs from worker freeze")
    probe = json.loads(run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(CANDIDATE)]))
    duration = float(probe["format"]["duration"])
    selected, cuts, score_contract = detect_cuts()
    if cuts != EXPECTED_CUTS:
        raise ValueError(f"cut reproduction failed: {cuts}")
    timestamps = midpoint_timestamps(cuts, duration)
    records: list[dict[str, Any]] = []
    sheet_paths: dict[str, list[Path]] = {variant: [] for variant in VARIANTS}
    fresh_match = 0
    for scene, timestamp in enumerate(timestamps, start=1):
        clean = FRAMES / "clean" / f"scene_{scene:02d}.png"
        decode(timestamp, clean)
        with Image.open(clean).convert("RGB") as opened:
            image = opened.copy()
        if image.size != (1920, 1080):
            raise ValueError(f"scene {scene} decoded at {image.size}")
        pass13 = PASS13_FRAMES / f"scene_{scene:02d}.png"
        if sha256(clean) != sha256(pass13):
            raise ValueError(f"clean scene {scene} differs from pass 13")
        fresh_match += 1
        for variant, floor in VARIANTS.items():
            output = FRAMES / variant / f"scene_{scene:02d}.png"
            output.parent.mkdir(parents=True, exist_ok=True)
            if floor is not None:
                shadow_floor(image, floor).save(output, format="PNG", optimize=False)
            records.append({
                "scene": scene,
                "timestamp_seconds": timestamp,
                "variant": variant,
                "luma_floor_code_value": floor,
                "path": output.relative_to(ROOT).as_posix(),
                "png_sha256": sha256(output),
                "pass13_clean_sha256": sha256(pass13) if floor is None else None,
            })
            sheet_paths[variant].append(output)
    sheet_hashes: dict[str, str] = {}
    for variant, paths in sheet_paths.items():
        sheet = OUT / f"contact_sheet_{variant}.png"
        contact_sheet(paths, [f"S{scene} · {variant}" for scene in range(1, 17)], sheet)
        sheet_hashes[variant] = sha256(sheet)
    receipt = {
        "status": "QA_STATIC_PNG_DERIVATIVES_NOT_A_CANDIDATE",
        "deepening_pass": 14,
        "created_at": datetime.now().astimezone().isoformat(),
        "candidate_path": str(CANDIDATE),
        "candidate_sha256": candidate_sha,
        "ffprobe": probe,
        "decoder": {"ffmpeg": run(["ffmpeg", "-version"]).splitlines()[0], "python": platform.python_version(), "pillow": Image.__version__, "numpy": np.__version__},
        "cut_detection": {"implementation": "30fps 160x90 grayscale mean-absolute frame difference", "nonmaximum_separation_frames": 30, "selected_incoming_frame_indices": selected, "cuts": cuts, "exact_pass13_match": True, **score_contract},
        "fresh_clean_match": f"{fresh_match}/16_PASS13_BYTE_IDENTICAL",
        "scene_count": 16,
        "variant_count": 5,
        "variant_order": list(VARIANTS),
        "frame_count": len(records),
        "records": records,
        "contact_sheet_sha256": sheet_hashes,
        "transform_contract": {"implementation": "integer-luma-preserving dark-tone floor and full-range remap", "luma_weights_integer_over_256": [54, 183, 19], "luma_rounding": "add 128 then floor divide by 256", "floors_srgb_code_value": [8, 16, 32, 48], "remap": "Y2=max(Y-floor,0)*255/(255-floor), integer round-half-up; RGB2=RGB*Y2/Y, integer round-half-up", "source_mode": "RGB", "canvas_change": False},
        "raw_ocr_text_stored": False,
        "scientific_adjudication_performed": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    (OUT / "extraction_receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS candidate={candidate_sha} cuts=15 scenes=16 frames={len(records)} variants=5")


if __name__ == "__main__":
    main()
