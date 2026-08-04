#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "omni/gemini_omni_gesture_michael_lipblend.mp4"
DRIVER = BASE / "lipsync/michael_gesture_excerpt_6s.wav"
STILL = BASE / "lipsync/v3_real_scene_base.png"
MASK = BASE / "lipsync/presenter_mask_430x560.png"
OUT = BASE / "lipsync/NEBULAMIND_V3_PRESENTER_C_MICHAEL_OMNI_LIPBLEND_SCENE_CANARY.mp4"
SHEET = BASE / "lipsync/V3_PRESENTER_C_MICHAEL_OMNI_LIPBLEND_TEMPORAL_QA.png"
RECEIPT = BASE / "lipsync/michael_omni_lipblend_scene_receipt.json"
FRAME_DIR = BASE / "lipsync/omni_lipblend_qa_frames"
FONT_PATH = Path("/System/Library/Fonts/SFNSMono.ttf")
W, H, FPS, DURATION = 2560, 1440, 30, 6.0


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_sheet() -> list[dict[str, object]]:
    times = [0.4, 1.4, 2.4, 3.4, 4.4, 5.4]
    font = ImageFont.truetype(str(FONT_PATH), size=18)
    frames: list[Image.Image] = []
    rows: list[dict[str, object]] = []
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
        tile = Image.new("RGB", (965, 400), (7, 16, 31))
        tile.paste(full, (0, 40))
        tile.paste(closeup, (660, 40))
        draw = ImageDraw.Draw(tile)
        draw.text(
            (12, 8),
            f"{timestamp:03.1f}s · full V3 layout + presenter closeup",
            font=font,
            fill=(234, 242, 255),
        )
        frames.append(tile)
        rows.append({"time_seconds": timestamp, "frame": str(frame_path)})
    sheet = Image.new("RGB", (965, 400 * len(frames)), (7, 16, 31))
    for index, tile in enumerate(frames):
        sheet.paste(tile, (0, index * 400))
    sheet.save(SHEET, quality=94)
    return rows


def main() -> None:
    for required in (SOURCE, DRIVER, STILL, MASK):
        if not required.is_file():
            raise FileNotFoundError(required)

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
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "17",
        "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "256k", "-ar", "48000",
        "-movflags", "+faststart", str(OUT),
    ])
    run(["ffmpeg", "-v", "error", "-xerror", "-i", str(OUT), "-f", "null", "-"])
    rows = make_sheet()
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error",
        "-show_entries",
        "format=duration,size,bit_rate:stream=codec_name,codec_type,width,height,r_frame_rate,sample_rate,channels",
        "-of", "json", str(OUT),
    ], text=True))
    receipt = {
        "marker": "NEBULAMIND_V3_PRESENTER_C_MICHAEL_OMNI_LIPBLEND_SCENE_CANARY_COMPLETE",
        "gesture_source": str(BASE / "omni/gemini_omni_gesture_raw.mp4"),
        "gesture_source_sha256": sha256(BASE / "omni/gemini_omni_gesture_raw.mp4"),
        "wav2lip_full_face_source": str(BASE / "omni/gemini_omni_gesture_michael_wav2lip.mp4"),
        "mouth_blended_source": str(SOURCE),
        "mouth_blended_source_sha256": sha256(SOURCE),
        "driver": str(DRIVER),
        "driver_sha256": sha256(DRIVER),
        "final_canary": str(OUT),
        "final_sha256": sha256(OUT),
        "temporal_sheet": str(SHEET),
        "sampled_frames": rows,
        "probe": probe,
        "presenter_overlay": {"x": 1980, "y": 610, "width": 430, "height": 560},
        "lip_sync": "Wav2Lip GAN driven by exact Michael 6.0-second WAV; soft mouth/jaw blend over Gemini gesture source",
        "gesture_generation": "Google Gemini/Veo Pro image-to-video, one successful 6.016-second canary",
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
