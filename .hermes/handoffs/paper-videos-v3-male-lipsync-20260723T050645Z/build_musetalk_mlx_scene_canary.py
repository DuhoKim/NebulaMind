#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "omni/gemini_omni_gesture_michael_musetalk_mlx.mp4"
SOURCE_RECEIPT = BASE / "omni/musetalk_mlx_canary_receipt.json"
DRIVER = BASE / "lipsync/michael_gesture_excerpt_6s.wav"
STILL = BASE / "lipsync/v3_real_scene_base.png"
MASK = BASE / "lipsync/presenter_mask_430x560.png"
OUT = BASE / "lipsync/NEBULAMIND_V3_PRESENTER_C_MICHAEL_MUSETALK_MLX_SCENE_CANARY.mp4"
SHEET = BASE / "lipsync/V3_PRESENTER_C_MICHAEL_MUSETALK_MLX_TEMPORAL_QA.png"
RECEIPT = BASE / "lipsync/michael_musetalk_mlx_scene_receipt.json"
FRAME_DIR = BASE / "lipsync/musetalk_mlx_scene_qa_frames"
FONT_PATH = Path("/System/Library/Fonts/SFNSMono.ttf")
FPS, DURATION = 30, 6.0


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def make_sheet() -> list[dict[str, object]]:
    times = [0.0, 0.4, 1.4, 2.4, 3.4, 4.4, 5.4, 5.9]
    font = ImageFont.truetype(str(FONT_PATH), size=18)
    rows: list[Image.Image] = []
    metadata: list[dict[str, object]] = []
    FRAME_DIR.mkdir(parents=True, exist_ok=True)
    for index, timestamp in enumerate(times):
        frame_path = FRAME_DIR / f"frame_{index:02d}_{timestamp:03.1f}.png"
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-ss", str(timestamp), "-i", str(OUT), "-frames:v", "1",
            str(frame_path),
        ])
        image = Image.open(frame_path).convert("RGB")
        full = image.resize((640, 360), Image.Resampling.LANCZOS)
        closeup = image.crop((1700, 250, 2485, 1245)).resize(
            (305, 360), Image.Resampling.LANCZOS
        )
        row = Image.new("RGB", (965, 400), (7, 16, 31))
        row.paste(full, (0, 40))
        row.paste(closeup, (660, 40))
        draw = ImageDraw.Draw(row)
        draw.text(
            (12, 8),
            f"{timestamp:03.1f}s · MuseTalk MLX V3 scene + presenter closeup",
            font=font,
            fill=(234, 242, 255),
        )
        rows.append(row)
        metadata.append({"time_seconds": timestamp, "frame": str(frame_path)})
    sheet = Image.new("RGB", (965, 400 * len(rows)), (7, 16, 31))
    for index, row in enumerate(rows):
        sheet.paste(row, (0, index * 400))
    sheet.save(SHEET, quality=94)
    return metadata


def main() -> None:
    for required in (SOURCE, SOURCE_RECEIPT, DRIVER, STILL, MASK):
        if not required.is_file():
            raise FileNotFoundError(required)

    source_receipt = json.loads(SOURCE_RECEIPT.read_text())
    filter_complex = (
        "[0:v]format=rgba[bg];"
        "[1:v]scale=430:560:force_original_aspect_ratio=increase,"
        "crop=430:560,fps=30,trim=duration=6,setpts=PTS-STARTPTS,format=rgba[presenter_rgb];"
        "[2:v]format=gray,scale=430:560[presenter_mask];"
        "[presenter_rgb][presenter_mask]alphamerge[presenter];"
        "[bg][presenter]overlay=1980:610:format=auto[v];"
        "[3:a]atrim=duration=6,asetpts=PTS-STARTPTS,"
        "loudnorm=I=-16:TP=-2:LRA=7[a]"
    )
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-loop", "1", "-i", str(STILL),
        "-i", str(SOURCE),
        "-loop", "1", "-i", str(MASK),
        "-i", str(DRIVER),
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "[a]",
        "-t", str(DURATION), "-frames:v", str(round(DURATION * FPS)),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
        "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "256k", "-ar", "48000",
        "-movflags", "+faststart", str(OUT),
    ])
    run(["ffmpeg", "-v", "error", "-xerror", "-i", str(OUT), "-f", "null", "-"])
    rows = make_sheet()
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-count_frames",
        "-show_entries",
        "format=duration,size,bit_rate:stream=codec_name,codec_type,width,height,r_frame_rate,nb_read_frames,sample_rate,channels",
        "-of", "json", str(OUT),
    ], text=True))
    receipt = {
        "marker": "NEBULAMIND_V3_PRESENTER_C_MICHAEL_MUSETALK_MLX_SCENE_CANARY_COMPLETE",
        "source": str(SOURCE),
        "source_sha256": sha256(SOURCE),
        "source_receipt": str(SOURCE_RECEIPT),
        "source_sharpness": source_receipt["sharpness"],
        "driver": str(DRIVER),
        "driver_sha256": sha256(DRIVER),
        "final_canary": str(OUT),
        "final_sha256": sha256(OUT),
        "temporal_sheet": str(SHEET),
        "sampled_frames": rows,
        "probe": probe,
        "presenter_overlay": {"x": 1980, "y": 610, "width": 430, "height": 560},
        "lip_sync": "MuseTalk 1.5 q4 on Apple MLX; exact Michael WAV; dynamic S3FD tracking; tight mouth-only paste-back",
        "replaces_rejected_method": "standard Wav2Lip 96x96 mouth blend rejected for blur",
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
