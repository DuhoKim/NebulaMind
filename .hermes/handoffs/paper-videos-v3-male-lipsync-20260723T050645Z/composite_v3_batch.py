#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z")
BATCH = BASE / "batch"
ASSETS = BATCH / "assets_batch_receipt.json"
MASK = BATCH / "presenter_mask_530x850.png"
FONT_PATH = Path("/System/Library/Fonts/SFNSMono.ttf")
W, H, FPS = 2560, 1440, 30
INTRO_SECONDS = 2.5
OUTRO_SECONDS = 2.8


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def capture(args: list[str]) -> str:
    return subprocess.check_output(args, text=True).strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def probe(path: Path) -> dict[str, Any]:
    return json.loads(capture([
        "ffprobe", "-v", "error", "-count_frames",
        "-show_entries", "format=duration,size,bit_rate:stream=codec_name,codec_type,profile,width,height,pix_fmt,avg_frame_rate,nb_read_frames,sample_rate,channels,bit_rate",
        "-of", "json", str(path),
    ]))


def render_background(layouts: list[Path], durations: list[float], output: Path) -> None:
    if len(layouts) != len(durations):
        raise RuntimeError("layout/duration mismatch")
    args: list[str] = []
    filters: list[str] = []
    labels: list[str] = []
    for index, (layout, duration) in enumerate(zip(layouts, durations)):
        args.extend(["-loop", "1", "-framerate", str(FPS), "-i", str(layout)])
        filters.append(
            f"[{index}:v]trim=duration={duration:.6f},setpts=PTS-STARTPTS,"
            f"scale={W}:{H}:flags=lanczos,fps={FPS},setsar=1,format=yuv420p[v{index}]"
        )
        labels.append(f"[v{index}]")
    filters.append("".join(labels) + f"concat=n={len(layouts)}:v=1:a=0[vout]")
    expected = sum(durations)
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args,
        "-filter_complex", ";".join(filters), "-map", "[vout]",
        "-t", f"{expected:.6f}", "-an", "-r", str(FPS),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
        "-profile:v", "high", "-pix_fmt", "yuv420p", "-g", str(FPS * 2),
        "-movflags", "+faststart", str(output),
    ])


def make_sheet(video: Path, timeline: list[dict[str, Any]], duration: float, root: Path, key: str) -> Path:
    qa_dir = root / "qa"
    frame_dir = qa_dir / "frames"
    qa_dir.mkdir(parents=True, exist_ok=True)
    frame_dir.mkdir(parents=True, exist_ok=True)
    times = [1.2]
    times.extend(float(row["visual_start"]) + float(row["speech_duration"]) / 2 for row in timeline)
    times.append(duration - 1.2)
    labels = ["INTRO"] + [f"SCENE {index}" for index in range(1, 9)] + ["OUTRO"]
    font = ImageFont.truetype(str(FONT_PATH), 18)
    rows: list[Image.Image] = []
    for index, (seconds, label) in enumerate(zip(times, labels)):
        path = frame_dir / f"{index:02d}_{seconds:.3f}.png"
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-ss", f"{seconds:.3f}", "-i", str(video), "-frames:v", "1", str(path),
        ])
        image = Image.open(path).convert("RGB")
        full = image.resize((640, 360), Image.Resampling.LANCZOS)
        closeup = image.crop((1870, 105, 2520, 1325)).resize((305, 360), Image.Resampling.LANCZOS)
        row = Image.new("RGB", (965, 400), (7, 16, 31))
        row.paste(full, (0, 40))
        row.paste(closeup, (660, 40))
        draw = ImageDraw.Draw(row)
        draw.text((12, 8), f"{label} · {seconds:.1f}s · {key}", font=font, fill=(234, 242, 255))
        rows.append(row)
    sheet = Image.new("RGB", (965, 400 * len(rows)), (7, 16, 31))
    for index, row in enumerate(rows):
        sheet.paste(row, (0, index * 400))
    output = qa_dir / f"{key}_ENCODED_TEMPORAL_AND_CLOSEUPS.png"
    sheet.save(output, quality=94)
    return output


def composite_one(asset: dict[str, Any]) -> dict[str, Any]:
    key = asset["key"]
    root = BATCH / key
    presenter_receipt_path = root / "presenter/presenter_receipt.json"
    if not presenter_receipt_path.is_file():
        raise FileNotFoundError(presenter_receipt_path)
    presenter_receipt = json.loads(presenter_receipt_path.read_text())
    presenter = Path(presenter_receipt["output"])
    audio = Path(asset["narration_master"])
    if sha256(presenter) != presenter_receipt["output_sha256"]:
        raise RuntimeError(f"{key}: presenter drift")
    if sha256(audio) != asset["narration_sha256"]:
        raise RuntimeError(f"{key}: narration drift")
    layouts = [Path(path) for path in asset["layouts"]]
    durations = [INTRO_SECONDS]
    durations.extend(float(row["visual_duration"]) for row in asset["timeline"])
    durations.append(OUTRO_SECONDS)
    expected = sum(durations)
    if abs(expected - float(asset["expected_video_duration"])) > 0.02:
        raise RuntimeError(f"{key}: timeline sum drift")
    work = root / "build"
    work.mkdir(parents=True, exist_ok=True)
    background = work / "silent_v3_background.mp4"
    output = root / f"NEBULAMIND_PAPER_{key.upper().replace('-', '_')}_V3.mp4"
    render_background(layouts, durations, background)
    narration_end = INTRO_SECONDS + float(asset["narration_duration"])
    filter_complex = (
        "[1:v]scale=530:850:force_original_aspect_ratio=increase,"
        "crop=530:850,fps=30,tpad=stop_mode=clone:stop_duration=1,"
        f"trim=duration={float(asset['narration_duration']):.6f},"
        f"setpts=PTS-STARTPTS+{INTRO_SECONDS}/TB,format=rgba[presenter_rgb];"
        "[2:v]format=gray,scale=530:850[presenter_mask];"
        "[presenter_rgb][presenter_mask]alphamerge[presenter];"
        f"[0:v][presenter]overlay=1930:340:format=auto:enable='between(t,{INTRO_SECONDS:.3f},{narration_end:.6f})'[v];"
        f"[3:a]adelay={round(INTRO_SECONDS * 1000)}:all=1,"
        f"apad=pad_dur={expected:.6f},atrim=duration={expected:.6f}[a]"
    )
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(background), "-i", str(presenter), "-loop", "1", "-i", str(MASK), "-i", str(audio),
        "-filter_complex", filter_complex, "-map", "[v]", "-map", "[a]",
        "-t", f"{expected:.6f}", "-frames:v", str(round(expected * FPS)),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-profile:v", "high",
        "-pix_fmt", "yuv420p", "-r", str(FPS), "-g", str(FPS * 2),
        "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart", "-metadata", f"title={key} · Male Presenter V3",
        "-metadata", "comment=Plain-language machine-generated explainer; descriptive, not validated",
        str(output),
    ])
    run(["ffmpeg", "-v", "error", "-xerror", "-i", str(output), "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"])
    media = probe(output)
    video_stream = next(row for row in media["streams"] if row["codec_type"] == "video")
    audio_stream = next(row for row in media["streams"] if row["codec_type"] == "audio")
    observed_duration = float(media["format"]["duration"])
    expected_frames = round(expected * FPS)
    if not (
        video_stream["codec_name"] == "h264"
        and video_stream["profile"] == "High"
        and video_stream["width"] == W
        and video_stream["height"] == H
        and video_stream["pix_fmt"] == "yuv420p"
        and video_stream["avg_frame_rate"] == "30/1"
        and int(video_stream["nb_read_frames"]) == expected_frames
        and audio_stream["codec_name"] == "aac"
        and audio_stream["sample_rate"] == "48000"
        and audio_stream["channels"] == 2
        and abs(observed_duration - expected) <= 0.08
    ):
        raise RuntimeError(f"{key}: final media contract failed {media}")
    sheet = make_sheet(output, asset["timeline"], observed_duration, root, key)
    receipt = {
        "marker": "NEBULAMIND_PAPER_V3_LOCAL_MASTER_COMPLETE",
        "completed_at_utc": now(),
        "key": key,
        "source_v2_spec_sha256": asset["source_v2_spec_sha256"],
        "voice": "am_michael",
        "voice_speed": 1.0,
        "presenter_receipt": str(presenter_receipt_path),
        "presenter_sha256": sha256(presenter),
        "narration": str(audio),
        "narration_sha256": sha256(audio),
        "srt": asset["srt"],
        "srt_sha256": asset["srt_sha256"],
        "timeline": asset["timeline"],
        "expected_duration": round(expected, 6),
        "observed_duration": round(observed_duration, 6),
        "artifact": str(output),
        "artifact_sha256": sha256(output),
        "artifact_bytes": output.stat().st_size,
        "probe": media,
        "encoded_sheet": str(sheet),
        "encoded_sheet_sha256": sha256(sheet),
        "publication_state": "local V3 QA pending; not uploaded",
    }
    (root / "build_receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keys", nargs="*", help="composite selected keys; default all available presenter tracks")
    args = parser.parse_args()
    if not ASSETS.is_file() or not MASK.is_file():
        raise FileNotFoundError("assets receipt or presenter mask missing")
    assets = json.loads(ASSETS.read_text())
    papers = {row["key"]: row for row in assets["papers"]}
    selected = args.keys or [key for key in papers if (BATCH / key / "presenter/presenter_receipt.json").is_file()]
    unknown = set(selected) - set(papers)
    if unknown:
        raise RuntimeError(f"unknown keys: {sorted(unknown)}")
    receipts = []
    for index, key in enumerate(selected, 1):
        print(f"COMPOSITE {index}/{len(selected)} {key}", flush=True)
        receipts.append(composite_one(papers[key]))
    progress = {
        "marker": "NEBULAMIND_FIVE_PAPER_V3_LOCAL_MASTER_BATCH_PROGRESS",
        "completed_at_utc": now(),
        "selected": selected,
        "completed": [{"key": row["key"], "artifact": row["artifact"], "sha256": row["artifact_sha256"]} for row in receipts],
        "publication_state": "local V3 QA only; not uploaded",
    }
    (BATCH / "master_batch_progress.json").write_text(json.dumps(progress, indent=2) + "\n")
    print(json.dumps(progress, indent=2))


if __name__ == "__main__":
    main()
