#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
LANE = ROOT.parent
SPEC = LANE / "V4_Z9_CANARY_SPEC.json"
ASSETS = ROOT / "assets_receipt.json"
PRESENTER_RECEIPT = ROOT / "z9-metallicity/presenter/presenter_receipt.json"
MASK = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z/batch/presenter_mask_530x850.png")
FONT = Path("/System/Library/Fonts/SFNSMono.ttf")
OUTPUT = ROOT / "NEBULAMIND_Z9_V4_INTRO_PLOTS_CANARY.mp4"
RECEIPT = ROOT / "build_receipt.json"
W, H, FPS = 2560, 1440, 30
PRESENTER_X, PRESENTER_Y, PRESENTER_W, PRESENTER_H = 1980, 610, 430, 560


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def capture(args: list[str]) -> str:
    return subprocess.check_output(args, text=True).strip()


def probe(path: Path) -> dict[str, Any]:
    return json.loads(capture([
        "ffprobe", "-v", "error", "-count_frames",
        "-show_entries", "format=duration,size,bit_rate:stream=codec_name,codec_type,profile,width,height,pix_fmt,avg_frame_rate,nb_read_frames,sample_rate,channels,bit_rate",
        "-of", "json", str(path),
    ]))


def render_background(layouts: list[Path], durations: list[float], output: Path) -> None:
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


def make_sheet(video: Path, timeline: list[dict[str, Any]], root: Path) -> Path:
    qa = root / "qa"
    frames = qa / "encoded_frames"
    qa.mkdir(parents=True, exist_ok=True)
    frames.mkdir(parents=True, exist_ok=True)
    label_font = ImageFont.truetype(str(FONT), 18)
    rows: list[Image.Image] = []
    for row in timeline:
        slot = int(row["slot"])
        seconds = float(row["visual_start"]) + float(row["speech_duration"]) / 2
        path = frames / f"slot_{slot:02d}_{seconds:.3f}.png"
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-ss", f"{seconds:.3f}", "-i", str(video), "-frames:v", "1", str(path),
        ])
        image = Image.open(path).convert("RGB")
        full = image.resize((640, 360), Image.Resampling.LANCZOS)
        closeup = image.crop((1935, 520, 2455, 1260)).resize((253, 360), Image.Resampling.LANCZOS)
        combined = Image.new("RGB", (913, 400), (7, 16, 31))
        combined.paste(full, (0, 40))
        combined.paste(closeup, (660, 40))
        draw = ImageDraw.Draw(combined)
        draw.text((12, 8), f"SLOT {slot:02d} · {seconds:.1f}s · encoded full + presenter", font=label_font, fill=(234, 242, 255))
        rows.append(combined)
    sheet = Image.new("RGB", (913, 400 * len(rows)), (7, 16, 31))
    for index, row in enumerate(rows):
        sheet.paste(row, (0, index * 400))
    output = qa / "encoded_temporal_and_presenter_sheet.png"
    sheet.save(output)
    return output


def main() -> None:
    for required in (SPEC, ASSETS, PRESENTER_RECEIPT, MASK, FONT):
        if not required.is_file():
            raise FileNotFoundError(required)
    spec = json.loads(SPEC.read_text())
    assets = json.loads(ASSETS.read_text())
    presenter_receipt = json.loads(PRESENTER_RECEIPT.read_text())
    presenter = Path(presenter_receipt["output"])
    audio = Path(assets["narration_master"])
    if assets["spec_sha256"] != sha256(SPEC) or presenter_receipt["spec_sha256"] != sha256(SPEC):
        raise RuntimeError("spec lineage drift")
    if sha256(presenter) != presenter_receipt["output_sha256"]:
        raise RuntimeError("presenter drift")
    if sha256(audio) != assets["narration_sha256"] or presenter_receipt["audio_sha256"] != assets["narration_sha256"]:
        raise RuntimeError("narration drift")
    if tuple(spec["contract_preserved"]["presenter_box"]) != (PRESENTER_X, PRESENTER_Y, PRESENTER_W, PRESENTER_H):
        raise RuntimeError("presenter box drift")
    layouts = [Path(path) for path in assets["layouts"]]
    durations = [float(row["visual_duration"]) for row in assets["timeline"]]
    expected = sum(durations)
    if abs(expected - float(assets["expected_video_duration"])) > 0.02:
        raise RuntimeError("timeline sum drift")
    work = ROOT / "build"
    work.mkdir(parents=True, exist_ok=True)
    background = work / "silent_v4_background.mp4"
    render_background(layouts, durations, background)
    filter_complex = (
        f"[1:v]scale={PRESENTER_W}:{PRESENTER_H}:force_original_aspect_ratio=increase,"
        f"crop={PRESENTER_W}:{PRESENTER_H},fps={FPS},tpad=stop_mode=clone:stop_duration=1,"
        f"trim=duration={expected:.6f},setpts=PTS-STARTPTS,format=rgba[presenter_rgb];"
        f"[2:v]format=gray,scale={PRESENTER_W}:{PRESENTER_H}[presenter_mask];"
        "[presenter_rgb][presenter_mask]alphamerge[presenter];"
        f"[0:v][presenter]overlay={PRESENTER_X}:{PRESENTER_Y}:format=auto[v];"
        f"[3:a]apad=pad_dur={expected:.6f},atrim=duration={expected:.6f}[a]"
    )
    expected_frames = round(expected * FPS)
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(background), "-i", str(presenter), "-loop", "1", "-i", str(MASK), "-i", str(audio),
        "-filter_complex", filter_complex, "-map", "[v]", "-map", "[a]",
        "-t", f"{expected:.6f}", "-frames:v", str(expected_frames),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-profile:v", "high",
        "-pix_fmt", "yuv420p", "-r", str(FPS), "-g", str(FPS * 2),
        "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart", "-metadata", "title=z9 metallicity · V4 introduction and plots canary",
        "-metadata", "comment=Local machine-generated explainer canary; descriptive, not validated; not published",
        str(OUTPUT),
    ])
    run(["ffmpeg", "-v", "error", "-xerror", "-i", str(OUTPUT), "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"])
    media = probe(OUTPUT)
    video_stream = next(row for row in media["streams"] if row["codec_type"] == "video")
    audio_stream = next(row for row in media["streams"] if row["codec_type"] == "audio")
    observed = float(media["format"]["duration"])
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
        and abs(observed - expected) <= 0.08
    ):
        raise RuntimeError(f"final media contract failed: {media}")
    sheet = make_sheet(OUTPUT, assets["timeline"], ROOT)
    receipt = {
        "marker": "NEBULAMIND_V4_Z9_LOCAL_CANARY_MASTER_COMPLETE",
        "completed_at_utc": now(),
        "spec": str(SPEC),
        "spec_sha256": sha256(SPEC),
        "assets_receipt": str(ASSETS),
        "assets_receipt_sha256": sha256(ASSETS),
        "presenter_receipt": str(PRESENTER_RECEIPT),
        "presenter_receipt_sha256": sha256(PRESENTER_RECEIPT),
        "narration": str(audio),
        "narration_sha256": sha256(audio),
        "srt": assets["srt"],
        "srt_sha256": assets["srt_sha256"],
        "presenter_box": [PRESENTER_X, PRESENTER_Y, PRESENTER_W, PRESENTER_H],
        "timeline": assets["timeline"],
        "expected_duration": round(expected, 6),
        "observed_duration": round(observed, 6),
        "artifact": str(OUTPUT),
        "artifact_sha256": sha256(OUTPUT),
        "artifact_bytes": OUTPUT.stat().st_size,
        "probe": media,
        "encoded_sheet": str(sheet),
        "encoded_sheet_sha256": sha256(sheet),
        "publication_state": "local V4 z9 canary QA pending; not uploaded",
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "PASS",
        "artifact": str(OUTPUT),
        "sha256": receipt["artifact_sha256"],
        "bytes": receipt["artifact_bytes"],
        "duration": receipt["observed_duration"],
        "frames": int(video_stream["nb_read_frames"]),
        "sheet": str(sheet),
    }, indent=2))


if __name__ == "__main__":
    main()
