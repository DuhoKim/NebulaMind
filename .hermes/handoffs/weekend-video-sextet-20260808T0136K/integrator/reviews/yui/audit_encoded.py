#!/usr/bin/env python3
"""Read-only encoded-video audit; writes evidence only beneath this review lane."""
from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "qa"
TARGETS = {
    "candidate-spin-0149": Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4"),
    "candidate-mzr-0155": Path("/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4"),
    "public-spin": Path("/Users/duhokim/NebulaMind/NebulaMind/frontend/public/videos/spin-parity-census.mp4"),
    "public-mzr": Path("/Users/duhokim/NebulaMind/NebulaMind/frontend/public/videos/mzr-archive-census.mp4"),
    "public-fesc": Path("/Users/duhokim/NebulaMind/NebulaMind/frontend/public/videos/fesc-zsweep-photon-budget.mp4"),
    "public-c41-mzr": Path("/Users/duhokim/NebulaMind/NebulaMind/frontend/public/videos/c41-highz-mzr-calibration-anchored.mp4"),
    "public-c41-uvlf": Path("/Users/duhokim/NebulaMind/NebulaMind/frontend/public/videos/c41-brightend-uvlf-archival-gap.mp4"),
}
PTS_RE = re.compile(r"pts_time:([0-9.]+)")


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=True)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def font(size: int):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/SFNS.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size)
            except OSError:
                pass
    return ImageFont.load_default()


def probe(path: Path) -> dict:
    result = run([
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,sample_rate,channels",
        "-of", "json", str(path),
    ])
    return json.loads(result.stdout)


def scene_cuts(path: Path) -> tuple[list[float], str]:
    result = subprocess.run([
        "ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-an",
        "-vf", "scale=320:-1,select='gt(scene,0.02)',showinfo", "-f", "null", "-",
    ], text=True, capture_output=True, check=True)
    cuts = sorted({round(float(m.group(1)), 6) for m in PTS_RE.finditer(result.stderr)})
    return cuts, result.stderr


def extract(path: Path, when: float, output: Path) -> None:
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{when:.6f}",
        "-i", str(path), "-frames:v", "1", "-q:v", "2", str(output),
    ])


def contact_sheet(frames: list[tuple[float, Path]], output: Path) -> None:
    cols = 4
    thumb_w, thumb_h, label_h = 480, 270, 38
    rows = math.ceil(len(frames) / cols)
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), (5, 8, 14))
    draw = ImageDraw.Draw(sheet)
    fnt = font(24)
    for i, (when, path) in enumerate(frames):
        image = Image.open(path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = (i % cols) * thumb_w
        y = (i // cols) * (thumb_h + label_h)
        sheet.paste(image, (x, y))
        draw.text((x + 10, y + thumb_h + 5), f"state {i + 1:02d}  {when:08.3f}s", font=fnt, fill=(238, 242, 250))
    sheet.save(output, quality=92)


def audit(name: str, path: Path) -> dict:
    if not path.exists():
        return {"name": name, "path": str(path), "exists": False}
    target = OUT / name
    frames_dir = target / "state_midpoints"
    frames_dir.mkdir(parents=True, exist_ok=True)
    media = probe(path)
    duration = float(media["format"]["duration"])
    cuts, log = scene_cuts(path)
    boundaries = [0.0] + [c for c in cuts if 0.05 < c < duration - 0.05] + [duration]
    boundaries = sorted(set(boundaries))
    holds = [boundaries[i + 1] - boundaries[i] for i in range(len(boundaries) - 1)]
    midpoints = [(boundaries[i] + boundaries[i + 1]) / 2 for i in range(len(boundaries) - 1)]
    extracted: list[tuple[float, Path]] = []
    for i, midpoint in enumerate(midpoints, 1):
        output = frames_dir / f"state_{i:02d}_{midpoint:09.3f}s.jpg"
        extract(path, midpoint, output)
        extracted.append((midpoint, output))
    contact_sheet(extracted, target / "contact_sheet.jpg")
    (target / "ffprobe.json").write_text(json.dumps(media, indent=2) + "\n")
    (target / "scene_detect.log").write_text(log)
    result = {
        "name": name,
        "path": str(path),
        "exists": True,
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "duration_seconds": duration,
        "streams": media["streams"],
        "detected_cut_times_seconds": boundaries[1:-1],
        "detected_state_count": len(midpoints),
        "state_midpoints_seconds": midpoints,
        "hold_seconds": holds,
        "max_static_hold_seconds": max(holds),
        "holds_over_6_seconds": sum(1 for h in holds if h > 6.0),
        "contact_sheet": str(target / "contact_sheet.jpg"),
    }
    (target / "metrics.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    results = [audit(name, path) for name, path in TARGETS.items()]
    (OUT / "ENCODED_AUDIT.json").write_text(json.dumps({"targets": results}, indent=2) + "\n")
    for item in results:
        if item.get("exists"):
            print(
                f"{item['name']}: states={item['detected_state_count']} duration={item['duration_seconds']:.3f}s "
                f"max_hold={item['max_static_hold_seconds']:.3f}s sha256={item['sha256'][:16]}"
            )
        else:
            print(f"{item['name']}: MISSING {item['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
