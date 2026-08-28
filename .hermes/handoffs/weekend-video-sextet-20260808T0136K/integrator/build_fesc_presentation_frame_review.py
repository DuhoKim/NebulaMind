#!/usr/bin/env python3
"""Build durable off-candidate encoded-frame evidence for the FESC presentation fix."""
from __future__ import annotations

import hashlib
import json
import math
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "integrator/canaries/fesc-method-overhaul-canary-20260809T1501K"
WORKSPACE = ROOT / "integrator/workspaces/fesc-presentation-fix-20260809T1501K"
REVIEW = WORKSPACE / "encoded-frame-review"
VIDEO = CANDIDATE / "fesc-method-overhaul-canary-20260809T1501K.mp4"
EXACT_TIMES = [5.052, 118.0, 222.410]
CYAN = np.array([44.0, 212.0, 230.0])
RAIL_XS = [110, 450, 790, 1130, 1470, 1810]
STAGE_SECTIONS = [
    {"motivation", "difficulty"},
    {"peak"},
    {"sample"},
    {"estimator"},
    {"controls", "discipline"},
    {"boundary", "payoff"},
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def contact_sheet(items: list[tuple[str, float, Path]], target: Path, cols: int, tile: tuple[int, int]) -> None:
    tw, th = tile
    label_h = 30
    rows = math.ceil(len(items) / cols)
    sheet = Image.new("RGB", (cols * tw, rows * (th + label_h)), (4, 7, 13))
    draw = ImageDraw.Draw(sheet)
    label_font = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 18, index=7)
    for index, (label, timestamp, path) in enumerate(items):
        x = (index % cols) * tw
        y = (index // cols) * (th + label_h)
        image = ImageOps.fit(Image.open(path).convert("RGB"), (tw, th), Image.Resampling.LANCZOS)
        sheet.paste(image, (x, y))
        caption = f"{label} · {timestamp:07.3f}s"
        bbox = draw.textbbox((0, 0), caption, font=label_font)
        draw.text((x + (tw - (bbox[2] - bbox[0])) / 2, y + th + 3), caption, font=label_font, fill=(239, 244, 251))
    target.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(target, quality=94, subsampling=0)


def section_at(records: list[dict], duration: float, timestamp: float) -> str:
    for index, record in enumerate(records):
        end = records[index + 1]["audio_start_seconds"] if index + 1 < len(records) else duration
        if timestamp < end:
            return record["section"]
    return records[-1]["section"]


def audit_rail(timeline: dict) -> dict:
    crop_x, crop_y, width, height, rate = 94, 884, 1732, 8, 2
    process = subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(VIDEO),
            "-vf", f"fps={rate},crop={width}:{height}:{crop_x}:{crop_y},format=rgb24",
            "-f", "rawvideo", "-pix_fmt", "rgb24", "-",
        ],
        check=True,
        capture_output=True,
    )
    chunk = width * height * 3
    frame_count = len(process.stdout) // chunk
    mismatches: list[dict] = []
    off_dot_cyan_frames: list[dict] = []
    local_xs = [x - crop_x for x in RAIL_XS]
    off_dot_mask = np.ones(width, dtype=bool)
    for x in local_xs:
        off_dot_mask[max(0, x - 18):min(width, x + 19)] = False
    for index in range(frame_count):
        timestamp = index / rate
        frame = np.frombuffer(process.stdout[index * chunk:(index + 1) * chunk], dtype=np.uint8).reshape(height, width, 3).astype(np.float32)
        distances = []
        for x in local_xs:
            patch = frame[2:7, x - 2:x + 3, :]
            distances.append(float(np.linalg.norm(patch.mean(axis=(0, 1)) - CYAN)))
        observed = int(np.argmin(distances))
        section = section_at(timeline["records"], float(timeline["master_duration_seconds"]), timestamp)
        expected = next(i for i, sections in enumerate(STAGE_SECTIONS) if section in sections)
        if observed != expected or distances[observed] >= 80:
            mismatches.append({"time": timestamp, "section": section, "expected_stage": expected, "observed_stage": observed, "cyan_distances": distances})
        off_dot = frame[:, off_dot_mask, :]
        cyan_like = int((np.linalg.norm(off_dot - CYAN, axis=2) < 55).sum())
        if cyan_like:
            off_dot_cyan_frames.append({"time": timestamp, "cyan_like_pixels": cyan_like})
    return {
        "sampling_fps": rate,
        "sampled_frames": frame_count,
        "stage_dot_mismatch_count": len(mismatches),
        "stage_dot_mismatches": mismatches[:20],
        "off_dot_cyan_fill_frame_count": len(off_dot_cyan_frames),
        "off_dot_cyan_fill_frames": off_dot_cyan_frames[:20],
        "status": "PASS" if not mismatches and not off_dot_cyan_frames else "HOLD",
    }


def main() -> int:
    if REVIEW.exists():
        shutil.rmtree(REVIEW)
    frames_dir = REVIEW / "frames-2fps"
    exact_dir = REVIEW / "exact-reported-times"
    sheets_dir = REVIEW / "sheets"
    frames_dir.mkdir(parents=True)
    exact_dir.mkdir(parents=True)
    sheets_dir.mkdir(parents=True)

    timeline = json.loads((CANDIDATE / "audio/timeline.json").read_text())
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(VIDEO),
        "-vf", "fps=2,scale=960:540:flags=lanczos", "-q:v", "2", str(frames_dir / "frame-%04d.jpg"),
    ])
    frames = sorted(frames_dir.glob("frame-*.jpg"))
    full_sheets = []
    for page, start in enumerate(range(0, len(frames), 48), 1):
        page_frames = frames[start:start + 48]
        items = [(path.stem, (start + offset) / 2, path) for offset, path in enumerate(page_frames)]
        target = sheets_dir / f"full-2fps-{page:02d}.jpg"
        contact_sheet(items, target, 8, (480, 270))
        full_sheets.append({"path": str(target.relative_to(WORKSPACE)), "sha256": sha256(target)})

    exact_items = []
    exact_rows = []
    for index, timestamp in enumerate(EXACT_TIMES, 1):
        target = exact_dir / f"reported-{index:02d}-{timestamp:07.3f}s.jpg"
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{timestamp:.6f}",
            "-i", str(VIDEO), "-frames:v", "1", "-q:v", "2", str(target),
        ])
        exact_items.append((f"reported-{index:02d}", timestamp, target))
        exact_rows.append({"time": timestamp, "path": str(target.relative_to(WORKSPACE)), "sha256": sha256(target)})
    exact_sheet = sheets_dir / "exact-reported-times.jpg"
    contact_sheet(exact_items, exact_sheet, 3, (960, 540))

    rail = audit_rail(timeline)
    report = {
        "created_at": datetime.now(timezone.utc).astimezone().isoformat(),
        "candidate": CANDIDATE.name,
        "video": VIDEO.name,
        "video_sha256": sha256(VIDEO),
        "workspace": str(WORKSPACE.relative_to(ROOT)),
        "scratch_inside_candidate": False,
        "system_tmp_used": False,
        "sampling_fps": 2,
        "frame_count": len(frames),
        "full_sheet_count": len(full_sheets),
        "full_sheets": full_sheets,
        "exact_reported_times": exact_rows,
        "exact_sheet": {"path": str(exact_sheet.relative_to(WORKSPACE)), "sha256": sha256(exact_sheet)},
        "rail_audit": rail,
        "status": "PASS" if rail["status"] == "PASS" else "HOLD",
    }
    index_path = REVIEW / "FRAME_INDEX.json"
    index_path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "video_sha256": report["video_sha256"], "frame_count": len(frames), "sheet_count": len(full_sheets), "rail": rail}, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
