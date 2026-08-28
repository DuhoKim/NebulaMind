#!/usr/bin/env python3
"""Extract deterministic encoded-video QA evidence without mutating the source video."""

import argparse
import json
import math
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def run(command):
    return subprocess.run(command, check=True, capture_output=True, text=True)


def font(size):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/SFNS.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("outdir")
    parser.add_argument("--scene-threshold", type=float, default=0.02)
    args = parser.parse_args()

    video = Path(args.video).resolve()
    outdir = Path(args.outdir).resolve()
    frames_dir = outdir / "representative_frames"
    full_dir = outdir / "full_resolution_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    full_dir.mkdir(parents=True, exist_ok=True)

    probe = run([
        "ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(video)
    ])
    probe_data = json.loads(probe.stdout)
    (outdir / "ffprobe.json").write_text(json.dumps(probe_data, indent=2) + "\n")
    duration = float(probe_data["format"]["duration"])

    cuts = subprocess.run([
        "ffmpeg", "-hide_banner", "-i", str(video),
        "-vf", f"select='gt(scene,{args.scene_threshold})',showinfo",
        "-an", "-f", "null", "-",
    ], capture_output=True, text=True)
    (outdir / "scene_detect.log").write_text(cuts.stderr)
    cut_times = [float(value) for value in re.findall(r"pts_time:([0-9.]+)", cuts.stderr)]
    boundaries = [0.0]
    for value in cut_times:
        if value > boundaries[-1] + 0.05 and value < duration - 0.05:
            boundaries.append(value)
    boundaries.append(duration)

    midpoint_times = []
    for index, (start, end) in enumerate(zip(boundaries[:-1], boundaries[1:])):
        midpoint = (start + end) / 2.0
        midpoint_times.append(midpoint)
        output = frames_dir / f"scene_{index:02d}_{midpoint:07.3f}s.png"
        run([
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-ss", f"{midpoint:.6f}", "-i", str(video), "-frames:v", "1", str(output),
        ])

    critical_times = sorted(set(
        [max(0.0, min(duration - 0.05, t)) for t in midpoint_times]
        + [max(0.0, min(duration - 0.05, b + 0.05)) for b in boundaries[:-1]]
        + [duration - 0.10]
    ))
    for index, timestamp in enumerate(critical_times):
        output = full_dir / f"frame_{index:03d}_{timestamp:07.3f}s.png"
        run([
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-ss", f"{timestamp:.6f}", "-i", str(video), "-frames:v", "1", str(output),
        ])

    thumbs = []
    label_font = font(28)
    for path, timestamp in zip(sorted(frames_dir.glob("*.png")), midpoint_times):
        image = Image.open(path).convert("RGB")
        image.thumbnail((480, 270), Image.Resampling.LANCZOS)
        tile = Image.new("RGB", (500, 320), (8, 12, 22))
        tile.paste(image, ((500 - image.width) // 2, 8))
        draw = ImageDraw.Draw(tile)
        draw.text((14, 282), f"{timestamp:06.2f} s", font=label_font, fill=(232, 238, 247))
        thumbs.append(tile)
    columns = min(3, max(1, len(thumbs)))
    rows = int(math.ceil(len(thumbs) / columns))
    sheet = Image.new("RGB", (columns * 500, rows * 320), (8, 12, 22))
    for index, tile in enumerate(thumbs):
        sheet.paste(tile, ((index % columns) * 500, (index // columns) * 320))
    sheet.save(outdir / "contact_sheet.jpg", quality=94)

    inventory = {
        "source_video": str(video),
        "duration_seconds": duration,
        "scene_threshold": args.scene_threshold,
        "cut_times_seconds": boundaries[:-1],
        "scene_count": len(midpoint_times),
        "midpoint_times_seconds": midpoint_times,
        "representative_frames": [str(path) for path in sorted(frames_dir.glob("*.png"))],
        "full_resolution_frames": [str(path) for path in sorted(full_dir.glob("*.png"))],
        "contact_sheet": str(outdir / "contact_sheet.jpg"),
    }
    (outdir / "frame_inventory.json").write_text(json.dumps(inventory, indent=2) + "\n")
    print(json.dumps(inventory, indent=2))


if __name__ == "__main__":
    main()
