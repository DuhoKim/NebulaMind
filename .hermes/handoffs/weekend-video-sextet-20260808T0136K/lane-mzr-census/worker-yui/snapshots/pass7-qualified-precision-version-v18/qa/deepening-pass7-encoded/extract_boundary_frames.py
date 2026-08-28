#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont

CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4")
EXPECTED_SHA256 = "0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d"
DURATION = 128.4
CUTS = [2.666667, 13.766667, 25.566667, 28.066667, 41.833333, 52.466667, 61.433333, 68.666667, 71.166667, 85.766667, 99.533333, 102.0, 118.133333, 120.633333]
OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha(CANDIDATE) == EXPECTED_SHA256

boundary = []
for index, cut in enumerate(CUTS, 1):
    for side, sample in (("before", cut - 0.25), ("after", cut + 0.25)):
        token = f"{sample:07.3f}".replace(".", "p")
        name = f"cut_{index:02d}_{side}_{token}s.png"
        path = OUT / name
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{sample:.6f}",
            "-i", str(CANDIDATE), "-frames:v", "1", str(path)
        ], check=True)
        boundary.append({"cut_index": index, "cut_seconds": cut, "side": side, "sample_seconds": round(sample, 6), "file": name, "sha256": sha(path)})

starts = [0.0] + CUTS
ends = CUTS + [DURATION]
midpoints = []
for index, (start, end) in enumerate(zip(starts, ends), 1):
    sample = (start + end) / 2
    token = f"{sample:07.3f}".replace(".", "p")
    name = f"hold_{index:02d}_mid_{token}s.png"
    path = OUT / name
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{sample:.6f}",
        "-i", str(CANDIDATE), "-frames:v", "1", str(path)
    ], check=True)
    midpoints.append({"hold_index": index, "start_seconds": round(start, 6), "end_seconds": round(end, 6), "sample_seconds": round(sample, 6), "file": name, "sha256": sha(path)})


def make_sheet(rows, filename, columns, thumb=(480, 270)):
    label_h = 30
    count = len(rows)
    sheet = Image.new("RGB", (columns * thumb[0], ((count + columns - 1) // columns) * (thumb[1] + label_h)), (8, 16, 31))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for i, row in enumerate(rows):
        image = Image.open(OUT / row["file"]).convert("RGB")
        image.thumbnail(thumb)
        x = (i % columns) * thumb[0]
        y = (i // columns) * (thumb[1] + label_h)
        sheet.paste(image, (x, y))
        if "cut_index" in row:
            label = f"cut {row['cut_index']:02d} {row['side']} · {row['sample_seconds']:.3f}s"
        else:
            label = f"hold {row['hold_index']:02d} midpoint · {row['sample_seconds']:.3f}s"
        draw.text((x + 8, y + thumb[1] + 8), label, fill="white", font=font)
    path = OUT / filename
    sheet.save(path, quality=92)
    return {"file": filename, "sha256": sha(path), "count": count}

boundary_sheet = make_sheet(boundary, "contact_sheet_cut_boundaries_28frames.jpg", 4)
midpoint_sheet = make_sheet(midpoints, "contact_sheet_hold_midpoints_15frames.jpg", 3)
manifest = {
    "candidate_sha256": EXPECTED_SHA256,
    "method": "14 detected hard cuts sampled at ±0.25 seconds plus midpoint of all 15 resulting holds",
    "boundary_offset_seconds": 0.25,
    "boundary_frames": boundary,
    "hold_midpoint_frames": midpoints,
    "contact_sheets": {"boundaries": boundary_sheet, "midpoints": midpoint_sheet},
}
(OUT / "FRAME_HASHES.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"boundary_frames": len(boundary), "midpoint_frames": len(midpoints), "boundary_sheet": boundary_sheet, "midpoint_sheet": midpoint_sheet, "frame_manifest_sha256": sha(OUT / "FRAME_HASHES.json")}, indent=2))
