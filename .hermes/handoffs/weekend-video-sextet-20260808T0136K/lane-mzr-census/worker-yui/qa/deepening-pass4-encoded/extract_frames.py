#!/usr/bin/env python3
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont

CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4")
OUT = Path(__file__).resolve().parent
TIMES = list(range(2, 127, 4))
THUMB = (480, 270)
COLS = 4

OUT.mkdir(parents=True, exist_ok=True)
for second in TIMES:
    target = OUT / f"frame_{second:03d}s.png"
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-ss", str(second), "-i", str(CANDIDATE),
            "-frames:v", "1", "-vf", "scale=1920:1080:flags=lanczos",
            str(target),
        ],
        check=True,
    )

try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
except OSError:
    font = ImageFont.load_default()

rows = (len(TIMES) + COLS - 1) // COLS
sheet = Image.new("RGB", (COLS * THUMB[0], rows * THUMB[1]), (8, 12, 22))
for index, second in enumerate(TIMES):
    image = Image.open(OUT / f"frame_{second:03d}s.png").convert("RGB")
    image = image.resize(THUMB, Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(image)
    label = f"{second:03d}s"
    box = draw.textbbox((0, 0), label, font=font)
    draw.rectangle((0, 0, box[2] + 18, box[3] + 12), fill=(0, 0, 0))
    draw.text((9, 5), label, font=font, fill=(255, 255, 255))
    x = (index % COLS) * THUMB[0]
    y = (index // COLS) * THUMB[1]
    sheet.paste(image, (x, y))

sheet.save(OUT / "contact_sheet_32frames_offset2.jpg", quality=94, subsampling=0)
print(f"frames={len(TIMES)} contact_sheet={OUT / 'contact_sheet_32frames_offset2.jpg'}")
