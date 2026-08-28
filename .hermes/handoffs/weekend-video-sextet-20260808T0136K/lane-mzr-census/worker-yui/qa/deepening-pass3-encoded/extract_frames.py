#!/usr/bin/env python3
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont

CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4")
OUT = Path(__file__).resolve().parent
TIMESTAMPS = list(range(0, 125, 4))
THUMB = (480, 270)
COLS = 4
ROWS = 8

OUT.mkdir(parents=True, exist_ok=True)
for timestamp in TIMESTAMPS:
    target = OUT / f"frame_{timestamp:03d}s.png"
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-y",
            "-ss",
            str(timestamp),
            "-i",
            str(CANDIDATE),
            "-frames:v",
            "1",
            str(target),
        ],
        check=True,
    )

font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 18)
sheet = Image.new("RGB", (COLS * THUMB[0], ROWS * THUMB[1]), "#070b12")
for index, timestamp in enumerate(TIMESTAMPS):
    image = Image.open(OUT / f"frame_{timestamp:03d}s.png").convert("RGB")
    image = image.resize(THUMB, Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((8, 8, 90, 38), radius=7, fill=(0, 0, 0), outline=(94, 234, 212), width=2)
    draw.text((18, 13), f"{timestamp:03d}s", font=font, fill=(255, 255, 255))
    x = (index % COLS) * THUMB[0]
    y = (index // COLS) * THUMB[1]
    sheet.paste(image, (x, y))

sheet.save(OUT / "contact_sheet_32frames.jpg", quality=94, subsampling=0)
print(f"frames={len(TIMESTAMPS)} contact_sheet={OUT / 'contact_sheet_32frames.jpg'}")
