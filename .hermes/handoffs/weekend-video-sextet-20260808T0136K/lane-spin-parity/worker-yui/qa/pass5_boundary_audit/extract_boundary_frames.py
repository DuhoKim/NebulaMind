#!/usr/bin/env python3
"""Extract hash-bound frames around all held-candidate cut boundaries for pass 5."""

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
FPS = 30
FRAME_OFFSETS = (-2, -1, 0, 1, 2)
OFFSET_LABELS = {
    -2: "minus_2f",
    -1: "minus_1f",
    0: "cut",
    1: "plus_1f",
    2: "plus_2f",
}


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
            f"C{int(row['transition']):02d} · {float(row['time_seconds']):.3f}s · {label}",
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
    if len(cut_times) != 15:
        raise SystemExit(f"expected 15 cuts, detected {len(cut_times)}: {cut_times}")

    rows_by_offset: dict[int, list[dict[str, Any]]] = {
        offset: [] for offset in FRAME_OFFSETS
    }
    transitions = []
    for transition, cut_time in enumerate(cut_times, start=1):
        rows = []
        for offset_frames in FRAME_OFFSETS:
            label = OFFSET_LABELS[offset_frames]
            sample_time = cut_time + offset_frames / FPS
            frame = FRAMES / (
                f"cut_{transition:02d}_{label}_{sample_time:09.3f}s.png"
            )
            extract_frame(sample_time, frame)
            with Image.open(frame) as image:
                size = list(image.size)
                mode = image.mode
            row = {
                "transition": transition,
                "from_scene": transition,
                "to_scene": transition + 1,
                "cut_time_seconds": round(cut_time, 6),
                "offset_frames": offset_frames,
                "offset_seconds": round(offset_frames / FPS, 6),
                "sample": label,
                "time_seconds": round(sample_time, 6),
                "frame": str(frame.relative_to(OUT)),
                "frame_sha256": sha256(frame),
                "size": size,
                "mode": mode,
            }
            rows.append(row)
            rows_by_offset[offset_frames].append(row)
        transitions.append(
            {
                "transition": transition,
                "from_scene": transition,
                "to_scene": transition + 1,
                "cut_time_seconds": round(cut_time, 6),
                "samples": rows,
                "unique_sample_hashes": len({row["frame_sha256"] for row in rows}),
            }
        )

    contact_sheets = {
        OFFSET_LABELS[offset]: build_contact_sheet(
            OFFSET_LABELS[offset], rows_by_offset[offset]
        )
        for offset in FRAME_OFFSETS
    }
    ffmpeg_version = run(["ffmpeg", "-version"]).stdout.splitlines()[0]
    receipt = {
        "status": "READ_ONLY_ENCODED_CUT_BOUNDARY_AUDIT_EVIDENCE",
        "deepening_pass": 5,
        "candidate": str(MP4),
        "candidate_sha256": candidate_sha,
        "expected_candidate_sha256": EXPECTED_MP4_SHA256,
        "candidate_hash_match": True,
        "candidate_mtime_utc": datetime.fromtimestamp(
            MP4.stat().st_mtime, timezone.utc
        ).isoformat(),
        "scene_threshold": SCENE_THRESHOLD,
        "fps": FPS,
        "frame_offsets": list(FRAME_OFFSETS),
        "detected_cut_times_seconds": cut_times,
        "transition_count": len(transitions),
        "sample_count": sum(len(row["samples"]) for row in transitions),
        "probe": probe,
        "transitions": transitions,
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
    print(
        f"PASS candidate={candidate_sha} cuts={len(transitions)} "
        f"samples={receipt['sample_count']} sheets={len(contact_sheets)}"
    )


if __name__ == "__main__":
    main()
