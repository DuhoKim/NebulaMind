#!/usr/bin/env python3
"""Extract fresh scene midpoints at four playback resolutions for pass 6."""

from __future__ import annotations

import hashlib
import json
import platform
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT_ROOT = Path(__file__).resolve().parent
FRAMES = OUT_ROOT / "frames"
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
EXPECTED_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
THRESHOLD = 0.04
RESOLUTIONS = {
    "1080p": (1920, 1080),
    "720p": (1280, 720),
    "540p": (960, 540),
    "360p": (640, 360),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(command: list[str]) -> str:
    result = subprocess.run(command, check=True, text=True, capture_output=True)
    return result.stdout


def version_line(tool: str) -> str:
    result = subprocess.run([tool, "-version"], check=True, text=True, capture_output=True)
    return result.stdout.splitlines()[0]


def probe() -> dict[str, Any]:
    payload = json.loads(
        run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration,size:stream=index,codec_name,width,height,r_frame_rate,sample_rate,channels",
                "-of",
                "json",
                str(CANDIDATE),
            ]
        )
    )
    video = next(stream for stream in payload["streams"] if stream["codec_name"] == "h264")
    audio = next(stream for stream in payload["streams"] if stream["codec_name"] == "aac")
    return {
        "duration_seconds": float(payload["format"]["duration"]),
        "bytes": int(payload["format"]["size"]),
        "video": {
            "codec": video["codec_name"],
            "width": video["width"],
            "height": video["height"],
            "rate": video["r_frame_rate"],
        },
        "audio": {
            "codec": audio["codec_name"],
            "sample_rate": audio["sample_rate"],
            "channels": audio["channels"],
        },
    }


def detect_cuts(duration: float) -> list[float]:
    result = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            str(CANDIDATE),
            "-filter:v",
            f"select='gt(scene,{THRESHOLD})',showinfo",
            "-an",
            "-f",
            "null",
            "-",
        ],
        check=True,
        text=True,
        capture_output=True,
    )
    cuts = sorted(
        {
            round(float(value), 6)
            for value in re.findall(r"pts_time:([0-9.]+)", result.stderr)
            if 0.5 < float(value) < duration - 0.5
        }
    )
    return cuts


def extract_frame(time_seconds: float, width: int, height: int, output: Path) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{time_seconds:.6f}",
            "-i",
            str(CANDIDATE),
            "-frames:v",
            "1",
            "-vf",
            f"scale={width}:{height}:flags=lanczos",
            "-pix_fmt",
            "rgb24",
            "-y",
            str(output),
        ],
        check=True,
    )


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/SFNS.ttf",
    ):
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_contact_sheet(label: str, rows: list[dict[str, Any]], output: Path) -> None:
    tile_w, tile_h, label_h, gap = 480, 270, 34, 12
    cols, grid_rows = 4, 4
    sheet = Image.new(
        "RGB",
        (
            gap + cols * (tile_w + gap),
            gap + grid_rows * (tile_h + label_h + gap),
        ),
        "#07111f",
    )
    draw = ImageDraw.Draw(sheet)
    label_font = font(18)
    for index, row in enumerate(rows):
        col, grid_row = index % cols, index // cols
        x = gap + col * (tile_w + gap)
        y = gap + grid_row * (tile_h + label_h + gap)
        with Image.open(OUT_ROOT / row["frame"]).convert("RGB") as image:
            tile = image.resize((tile_w, tile_h), Image.Resampling.LANCZOS)
            sheet.paste(tile, (x, y))
        draw.text(
            (x, y + tile_h + 6),
            f"S{row['scene']:02d} · {row['midpoint_seconds']:.3f}s · {label}",
            fill="#c8d7ef",
            font=label_font,
        )
    sheet.save(output)


def main() -> None:
    for tool in ("ffmpeg", "ffprobe"):
        if shutil.which(tool) is None:
            raise SystemExit(f"missing dependency: {tool}")
    actual_sha = sha256(CANDIDATE)
    if actual_sha != EXPECTED_SHA:
        raise SystemExit(f"candidate hash mismatch: {actual_sha}")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    for old in FRAMES.glob("*.png"):
        old.unlink()

    media = probe()
    cuts = detect_cuts(media["duration_seconds"])
    if len(cuts) != 15:
        raise SystemExit(f"expected 15 cuts, found {len(cuts)}")
    boundaries = [0.0, *cuts, media["duration_seconds"]]
    scenes: list[dict[str, Any]] = []
    by_resolution: dict[str, list[dict[str, Any]]] = {label: [] for label in RESOLUTIONS}
    for scene_index, (start, end) in enumerate(zip(boundaries, boundaries[1:]), start=1):
        midpoint = (start + end) / 2.0
        samples = []
        for label, (width, height) in RESOLUTIONS.items():
            relative = f"frames/scene_{scene_index:02d}_{label}_{midpoint:09.3f}s.png"
            output = OUT_ROOT / relative
            extract_frame(midpoint, width, height, output)
            with Image.open(output) as image:
                if image.mode != "RGB" or image.size != (width, height):
                    raise SystemExit(f"unexpected frame format: {relative}")
            row = {
                "resolution": label,
                "width": width,
                "height": height,
                "frame": relative,
                "frame_sha256": sha256(output),
                "scene": scene_index,
                "midpoint_seconds": round(midpoint, 6),
            }
            samples.append(row)
            by_resolution[label].append(row)
        scenes.append(
            {
                "scene": scene_index,
                "start_seconds": round(start, 6),
                "end_seconds": round(end, 6),
                "midpoint_seconds": round(midpoint, 6),
                "samples": samples,
            }
        )

    contact_sheets = {}
    for label, rows in by_resolution.items():
        relative = f"contact_sheet_{label}.png"
        output = OUT_ROOT / relative
        make_contact_sheet(label, rows, output)
        contact_sheets[label] = {"path": relative, "sha256": sha256(output)}

    receipt = {
        "status": "FRESH_HASH_BOUND_MULTI_RESOLUTION_EXTRACTION",
        "deepening_pass": 6,
        "candidate": str(CANDIDATE),
        "candidate_sha256": actual_sha,
        "expected_candidate_sha256": EXPECTED_SHA,
        "candidate_hash_match": True,
        "candidate_modified": False,
        "extracted_at_utc": datetime.now(timezone.utc).isoformat(),
        "tool_versions": {
            "python": platform.python_version(),
            "ffmpeg": version_line("ffmpeg"),
            "ffprobe": version_line("ffprobe"),
            "pillow": Image.__version__,
        },
        "media": media,
        "scene_detection_threshold": THRESHOLD,
        "detected_cut_times_seconds": cuts,
        "scene_count": len(scenes),
        "resolution_count": len(RESOLUTIONS),
        "frame_count": sum(len(scene["samples"]) for scene in scenes),
        "resolutions": [
            {"label": label, "width": size[0], "height": size[1]}
            for label, size in RESOLUTIONS.items()
        ],
        "scenes": scenes,
        "contact_sheets": contact_sheets,
        "tts_invoked": False,
        "audio_generated": False,
        "encoded_output_created": False,
        "shared_or_public_assets_modified": False,
    }
    receipt_path = OUT_ROOT / "extraction_receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(
        f"PASS candidate={actual_sha} cuts={len(cuts)} scenes={len(scenes)} "
        f"frames={receipt['frame_count']} resolutions={len(RESOLUTIONS)}"
    )


if __name__ == "__main__":
    main()
