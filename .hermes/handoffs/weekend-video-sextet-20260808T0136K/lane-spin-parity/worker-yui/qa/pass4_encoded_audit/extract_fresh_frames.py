#!/usr/bin/env python3
"""Extract fresh, hash-bound pass-4 early/mid/late frames from the held candidate."""

from __future__ import annotations

import hashlib
import json
import platform
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import PIL
from PIL import Image, ImageDraw, ImageFont

MP4 = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
EXPECTED_MP4_SHA256 = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
OUT = Path(__file__).resolve().parent
FRAMES = OUT / "frames"
SCENE_THRESHOLD = 0.04
EDGE_OFFSET_SECONDS = 1.0


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=True)


def extract_frame(time_seconds: float, path: Path) -> None:
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-i",
            str(MP4),
            "-ss",
            f"{time_seconds:.6f}",
            "-frames:v",
            "1",
            "-vf",
            "format=rgb24",
            str(path),
        ]
    )


def build_contact_sheet(label: str, rows: list[dict[str, Any]]) -> dict[str, str]:
    sheet = Image.new("RGB", (1920, 1200), "#07101d")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for zero_index, row in enumerate(rows):
        with Image.open(OUT / str(row["frame"])) as source:
            thumb = source.copy()
            thumb.thumbnail((468, 263), Image.Resampling.LANCZOS)
        column = zero_index % 4
        line = zero_index // 4
        x = column * 480 + 6
        y = line * 300 + 6
        sheet.paste(thumb, (x, y))
        draw.text(
            (x, y + 267),
            f"S{int(row['scene']):02d} · {float(row['time_seconds']):.3f}s · {label}",
            fill="#dbeafe",
            font=font,
        )
    path = OUT / f"contact_sheet_{label}.png"
    sheet.save(path)
    return {"path": path.name, "sha256": sha256(path)}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)

    candidate_sha = sha256(MP4)
    if candidate_sha != EXPECTED_MP4_SHA256:
        raise SystemExit(f"candidate hash mismatch: {candidate_sha}")

    probe = json.loads(
        run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration,size:stream=index,codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels",
                "-of",
                "json",
                str(MP4),
            ]
        ).stdout
    )
    duration = float(probe["format"]["duration"])
    scene_probe = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            str(MP4),
            "-vf",
            f"select='gt(scene,{SCENE_THRESHOLD})',showinfo",
            "-an",
            "-f",
            "null",
            "-",
        ],
        check=True,
        text=True,
        capture_output=True,
    )
    detected = [float(value) for value in re.findall(r"pts_time:([0-9.]+)", scene_probe.stderr)]
    cut_times: list[float] = []
    for value in detected:
        if value <= 0.0 or value >= duration:
            continue
        if not cut_times or value - cut_times[-1] > 0.25:
            cut_times.append(value)
    boundaries = [0.0, *cut_times, duration]
    if len(boundaries) != 17:
        raise SystemExit(f"expected 16 scenes, detected {len(boundaries) - 1}: {cut_times}")

    samples: dict[str, list[dict[str, Any]]] = {
        "early": [],
        "mid": [],
        "late": [],
    }
    scenes = []
    for scene, (start, end) in enumerate(zip(boundaries, boundaries[1:]), start=1):
        midpoint = (start + end) / 2.0
        edge_offset = min(EDGE_OFFSET_SECONDS, (end - start) / 4.0)
        times = {
            "early": start + edge_offset,
            "mid": midpoint,
            "late": end - edge_offset,
        }
        scene_rows = []
        for label, time_seconds in times.items():
            frame = FRAMES / f"scene_{scene:02d}_{label}_{time_seconds:09.3f}s.png"
            extract_frame(time_seconds, frame)
            with Image.open(frame) as image:
                size = list(image.size)
                mode = image.mode
            row = {
                "scene": scene,
                "sample": label,
                "time_seconds": round(time_seconds, 6),
                "frame": str(frame.relative_to(OUT)),
                "frame_sha256": sha256(frame),
                "size": size,
                "mode": mode,
            }
            samples[label].append(row)
            scene_rows.append(row)
        scenes.append(
            {
                "scene": scene,
                "start_seconds": round(start, 6),
                "end_seconds": round(end, 6),
                "samples": scene_rows,
                "early_mid_late_byte_identical": len(
                    {row["frame_sha256"] for row in scene_rows}
                )
                == 1,
            }
        )

    contact_sheets = {
        label: build_contact_sheet(label, rows) for label, rows in samples.items()
    }
    ffmpeg_version = run(["ffmpeg", "-version"]).stdout.splitlines()[0]
    receipt = {
        "status": "READ_ONLY_ENCODED_FRAME_AUDIT_EVIDENCE",
        "deepening_pass": 4,
        "sampling": "early/mid/late per detected scene",
        "edge_offset_seconds": EDGE_OFFSET_SECONDS,
        "candidate": str(MP4),
        "candidate_sha256": candidate_sha,
        "expected_candidate_sha256": EXPECTED_MP4_SHA256,
        "candidate_hash_match": True,
        "candidate_mtime_utc": datetime.fromtimestamp(
            MP4.stat().st_mtime, timezone.utc
        ).isoformat(),
        "scene_threshold": SCENE_THRESHOLD,
        "detected_cut_times_seconds": cut_times,
        "scene_count": len(scenes),
        "sample_count": sum(len(rows) for rows in samples.values()),
        "probe": probe,
        "scenes": scenes,
        "contact_sheets": contact_sheets,
        "runtime": {
            "python": platform.python_version(),
            "pillow": PIL.__version__,
            "ffmpeg": ffmpeg_version,
        },
        "extracted_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate_modified": False,
        "tts_invoked": False,
        "encoded_output_created": False,
    }
    (OUT / "extraction_receipt.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    static_scenes = sum(row["early_mid_late_byte_identical"] for row in scenes)
    print(
        f"PASS candidate={candidate_sha} cuts={len(cut_times)} scenes={len(scenes)} "
        f"samples={receipt['sample_count']} byte_static_scenes={static_scenes}"
    )


if __name__ == "__main__":
    main()
