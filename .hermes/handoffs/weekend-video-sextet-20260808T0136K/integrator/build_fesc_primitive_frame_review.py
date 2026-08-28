#!/usr/bin/env python3
"""Build exhaustive actual-frame review sheets for one FESC primitive correction."""
from __future__ import annotations

import hashlib
import json
import math
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "integrator/canaries/fesc-method-overhaul-canary-20260809T1420K"
VIDEO = CANDIDATE / "fesc-method-overhaul-canary-20260809T1420K.mp4"
OUT = CANDIDATE / "frame-review-2fps"
EXACT_TIMES = [5.052, 15.013, 24.243, 31.816, 42.050, 51.592, 222.410, 231.051]
FONT = "/System/Library/Fonts/Menlo.ttc"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def contact_sheet(items: list[tuple[str, Path]], output: Path, cols: int, tile: tuple[int, int]) -> None:
    tw, th = tile
    label_h = 38
    rows = math.ceil(len(items) / cols)
    sheet = Image.new("RGB", (cols * tw, rows * (th + label_h)), (3, 6, 12))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(FONT, 23)
    for index, (label, path) in enumerate(items):
        x = index % cols * tw
        y = index // cols * (th + label_h)
        image = ImageOps.fit(Image.open(path).convert("RGB"), (tw, th), Image.Resampling.LANCZOS)
        sheet.paste(image, (x, y))
        box = draw.textbbox((0, 0), label, font=font)
        draw.text((x + (tw - (box[2] - box[0])) / 2, y + th + 4), label, font=font, fill=(239, 244, 251))
    sheet.save(output, quality=95, subsampling=0)


def main() -> int:
    if OUT.exists():
        raise RuntimeError(f"refusing to overwrite existing review tree: {OUT}")
    frames = OUT / "frames"
    exact = OUT / "exact-reported-times"
    sheets = OUT / "sheets"
    frames.mkdir(parents=True)
    exact.mkdir()
    sheets.mkdir()

    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(VIDEO),
        "-vf", "fps=2,scale=960:540:flags=lanczos", "-q:v", "2",
        str(frames / "frame-%04d.jpg"),
    ])
    frame_paths = sorted(frames.glob("frame-*.jpg"))
    full_items = [(f"{index / 2:07.3f}s", path) for index, path in enumerate(frame_paths)]
    page_size = 48
    full_sheets = []
    for start in range(0, len(full_items), page_size):
        page = start // page_size + 1
        output = sheets / f"full-2fps-{page:02d}.jpg"
        contact_sheet(full_items[start:start + page_size], output, cols=8, tile=(480, 270))
        full_sheets.append(output)

    exact_items = []
    for index, timestamp in enumerate(EXACT_TIMES, 1):
        target = exact / f"reported-{index:02d}-{timestamp:07.3f}s.jpg"
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{timestamp:.6f}",
            "-i", str(VIDEO), "-frames:v", "1", "-q:v", "1", str(target),
        ])
        exact_items.append((f"reported {timestamp:07.3f}s", target))
    exact_sheet = sheets / "exact-reported-times.jpg"
    contact_sheet(exact_items, exact_sheet, cols=4, tile=(960, 540))

    index = {
        "created_at": datetime.now(timezone.utc).astimezone().isoformat(),
        "candidate": CANDIDATE.name,
        "video": VIDEO.name,
        "video_sha256": sha256(VIDEO),
        "sampling_fps": 2,
        "frame_count": len(frame_paths),
        "full_sheet_count": len(full_sheets),
        "full_sheets": [{"path": str(path.relative_to(CANDIDATE)), "sha256": sha256(path)} for path in full_sheets],
        "reported_times_seconds": EXACT_TIMES,
        "exact_sheet": {"path": str(exact_sheet.relative_to(CANDIDATE)), "sha256": sha256(exact_sheet)},
        "exact_frames": [{"label": label, "path": str(path.relative_to(CANDIDATE)), "sha256": sha256(path)} for label, path in exact_items],
    }
    (OUT / "FRAME_INDEX.json").write_text(json.dumps(index, indent=2) + "\n")
    print(json.dumps({"frame_count": len(frame_paths), "full_sheet_count": len(full_sheets), "video_sha256": index["video_sha256"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
