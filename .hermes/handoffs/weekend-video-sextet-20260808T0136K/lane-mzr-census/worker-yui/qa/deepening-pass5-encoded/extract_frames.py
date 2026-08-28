#!/usr/bin/env python3
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont

CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4")
OUT = Path(__file__).resolve().parent
FRAME_DIR = OUT
TIMES = list(range(1, 126, 4))

OUT.mkdir(parents=True, exist_ok=True)
for second in TIMES:
    target = FRAME_DIR / f"frame_{second:03d}s.png"
    subprocess.run(
        [
            "ffmpeg", "-v", "error", "-ss", str(second), "-i", str(CANDIDATE),
            "-frames:v", "1", "-y", str(target),
        ],
        check=True,
    )

thumbs = []
for second in TIMES:
    image = Image.open(FRAME_DIR / f"frame_{second:03d}s.png").convert("RGB")
    image.thumbnail((480, 270), Image.Resampling.LANCZOS)
    cell = Image.new("RGB", (480, 300), "#050914")
    cell.paste(image, (0, 0))
    draw = ImageDraw.Draw(cell)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", 21)
    except OSError:
        font = ImageFont.load_default()
    draw.rounded_rectangle((10, 272, 115, 297), radius=7, fill="#111b2e")
    draw.text((20, 274), f"{second:03d} s", font=font, fill="#f2f6ff")
    thumbs.append(cell)

columns = 4
rows = (len(thumbs) + columns - 1) // columns
sheet = Image.new("RGB", (columns * 480, rows * 300), "#050914")
for index, thumb in enumerate(thumbs):
    sheet.paste(thumb, ((index % columns) * 480, (index // columns) * 300))
sheet.save(OUT / "contact_sheet_32frames_offset1.jpg", quality=94, subsampling=0)
print(f"extracted={len(TIMES)} contact_sheet={OUT / 'contact_sheet_32frames_offset1.jpg'}")
