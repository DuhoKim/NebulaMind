#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "canary-g3"
SLIDES = OUT / "slides"
SCENES = OUT / "scenes"
SPEC_PATH = ROOT / "V5_G3_MOTION_GRAPHICS_SPEC.json"
STORYBOARD_PATH = ROOT / "V5_G2_Z9_STORYBOARD.json"
SIGNOFF_PATH = ROOT / "V5_G3_SEMANTIC_SIGNOFF.md"
AUDIO_RECEIPT_PATH = OUT / "V5_G3_AUDIO_RECEIPT.json"
FIG1 = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v4-intro-plots-20260723T120045Z/sources-v4/figures/z9-metallicity-figure-1-vector-crop.png")
FFMPEG = "/opt/homebrew/bin/ffmpeg"
FFPROBE = "/opt/homebrew/bin/ffprobe"
VIDEO = OUT / "NEBULAMIND_Z9_V5_G3_MOTION_CANARY.mp4"
VIDEO_ONLY = OUT / "V5_G3_VIDEO_ONLY.mp4"
RECEIPT = OUT / "V5_G3_BUILD_RECEIPT.json"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
W, H, FPS = 2560, 1440, 30
EXPECTED_FIG_SHA = "8d1575a7e2cc173504290face69385aec4e7ac6e48df19ddb002cc78ef39b14e"
EXPECTED_STORYBOARD_SHA = "4ff525782afeeee7d8462c18f45ba16cf6fdabe1fe739dea2a5d84246165c33e"
BG = "#07111f"
PANEL = "#101e31"
PANEL_2 = "#152840"
WHITE = "#f7fbff"
MUTED = "#a9bdd1"
CYAN = "#46d8d2"
BLUE = "#4ca3e6"
AMBER = "#ffb648"
RED = "#e65b4f"
GRID = "#2a425d"

VIEW_ROIS = {
    "VS1_axes": (0.0, 0.0, 1.0, 1.0),
    "VS2_curves": (0.12, 0.065, 1.0, 0.61),
    "VS3_points": (0.432, 0.36, 0.786, 0.705),
    "VS4_gap": (0.432, 0.20, 0.786, 0.705),
    "VS5_anchor_swap": (0.12, 0.065, 1.0, 0.61),
    "VS6_stack": (0.29, 0.39, 0.54, 0.71),
}
RED_POINT_CENTERS_NORM = [(0.505, 0.591), (0.560, 0.558), (0.560, 0.463), (0.605, 0.518), (0.706, 0.573)]
RED_POINT_REGION_NORM = (0.495, 0.405, 0.716, 0.675)
BLUE_POINT_CENTER_NORM = (0.409, 0.550)
BLUE_POINT_REGION_NORM = (0.398, 0.502, 0.421, 0.598)


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


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill: str, outline: str | None = None, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        trial = word if not current else f"{current} {word}"
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def text_block(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str, max_width: int, line_gap: int = 10, anchor: str = "la") -> tuple[int, int, int, int]:
    lines = wrap(draw, text, fnt, max_width)
    x, y = xy
    heights = []
    widths = []
    for line in lines:
        box = draw.textbbox((0, 0), line, font=fnt)
        widths.append(box[2] - box[0])
        heights.append(box[3] - box[1])
    line_height = max(heights or [0]) + line_gap
    for index, line in enumerate(lines):
        draw.text((x, y + index * line_height), line, font=fnt, fill=fill, anchor=anchor)
    total_height = max(0, len(lines) * line_height - line_gap)
    return (x, y, x + max(widths or [0]), y + total_height)


def base_canvas(section: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, W, 86), fill="#0b1727")
    draw.text((70, 46), "NEBULAMIND · V5 GRAPHICS CANARY", font=font(30, True), fill=CYAN, anchor="lm")
    draw.text((W - 70, 46), section, font=font(26, True), fill=MUTED, anchor="rm")
    return image, draw


def add_caption(image: Image.Image, sentence: str, row_number: int) -> None:
    draw = ImageDraw.Draw(image)
    rounded(draw, (70, 1235, W - 70, H - 45), 28, "#0c192a", outline="#29445f", width=2)
    draw.text((105, 1270), f"{row_number:02d}", font=font(30, True), fill=CYAN, anchor="la")
    caption_font = font(43, True)
    lines = wrap(draw, sentence, caption_font, 2200)
    line_height = 52
    y = 1260 if len(lines) > 1 else 1305
    for index, line in enumerate(lines[:2]):
        draw.text((180, y + index * line_height), line, font=caption_font, fill=WHITE, anchor="la")


def fit_crop(source: Image.Image, roi: tuple[float, float, float, float], box: tuple[int, int, int, int]) -> tuple[Image.Image, tuple[int, int, int, int]]:
    sw, sh = source.size
    crop_box = (int(roi[0] * sw), int(roi[1] * sh), int(roi[2] * sw), int(roi[3] * sh))
    crop = source.crop(crop_box)
    x1, y1, x2, y2 = box
    target_w, target_h = x2 - x1, y2 - y1
    scale = min(target_w / crop.width, target_h / crop.height)
    resized = crop.resize((max(1, int(crop.width * scale)), max(1, int(crop.height * scale))), Image.Resampling.LANCZOS)
    px = x1 + (target_w - resized.width) // 2
    py = y1 + (target_h - resized.height) // 2
    return resized, (px, py, px + resized.width, py + resized.height)


def side_panel(draw: ImageDraw.ImageDraw, title: str, lines: list[tuple[str, str]], accent: str = CYAN) -> None:
    rounded(draw, (1920, 125, 2500, 1200), 30, PANEL, outline="#31516f", width=3)
    draw.rectangle((1920, 125, 1940, 1200), fill=accent)
    draw.text((1985, 190), title, font=font(40, True), fill=accent, anchor="la")
    y = 280
    for text, kind in lines:
        if kind == "big":
            fnt, color, gap = font(66, True), WHITE, 100
        elif kind == "value":
            fnt, color, gap = font(55, True), AMBER, 86
        elif kind == "small":
            fnt, color, gap = font(31), MUTED, 62
        else:
            fnt, color, gap = font(38, True), WHITE, 72
        boxes = text_block(draw, (1985, y), text, fnt, color, 450, line_gap=9)
        y = max(y + gap, boxes[3] + 28)
    draw.text((2210, 1140), "Source pixels SHA-locked", font=font(25), fill=MUTED, anchor="ma")


def figure_slide(row: dict[str, Any], source: Image.Image) -> Image.Image:
    number = int(row["n"])
    state = str(row["view_state"])
    image, draw = base_canvas("REAL FIGURE · PROGRESSIVE READ")
    rounded(draw, (55, 115, 1885, 1215), 28, "#f7f8fa", outline="#29445f", width=3)
    roi = VIEW_ROIS[state]
    crop, placed = fit_crop(source, roi, (75, 135, 1865, 1195))
    image.paste(crop, (placed[0], placed[1]))
    draw.rectangle((placed[0], placed[1], placed[2], placed[3]), outline="#d6e1eb", width=3)
    if number == 12:
        side_panel(draw, "REAL PAPER FIGURE", [("Mass versus gas oxygen", "big"), ("The source figure enters unchanged.", "small")])
    elif number == 13:
        side_panel(draw, "READ THE AXES", [("Across →", "value"), ("stellar mass", "normal"), ("Up →", "value"), ("gas oxygen abundance", "normal")])
    elif number == 14:
        side_panel(draw, "NEARBY BENCHMARKS", [("Solid", "value"), ("extrapolated relation", "small"), ("Dashed", "value"), ("measured relation", "small")])
    elif number == 15:
        side_panel(draw, "THE FIVE GALAXIES", [("Red circles", "big"), ("All five stay fully in frame.", "small")], RED)
    elif number == 16:
        side_panel(draw, "MAIN PATTERN", [("All five are below", "big"), ("≈ one fifth", "value"), ("of the nearby oxygen level", "normal")], RED)
    elif number == 17:
        side_panel(draw, "AVERAGE SHORTFALL", [("−0.69 ± 0.03 dex", "value"), ("The value is shown beside—not over—the data.", "small")], RED)
    elif number == 18:
        side_panel(draw, "ROBUSTNESS CHECK", [("Swap the benchmark", "big"), ("Extrapolated → measured at these masses", "small")], AMBER)
    elif number == 19:
        side_panel(draw, "RESULT HOLDS", [("≈ −0.65 dex", "value"), ("The shortfall barely changes.", "normal")], AMBER)
    elif number == 22:
        side_panel(draw, "INDEPENDENT STACK", [("Blue square", "big"), ("≈ 1,500 galaxies", "value"), ("−0.5 to −0.6 dex", "value")], BLUE)
    else:
        raise RuntimeError(f"unexpected figure row {number}")
    add_caption(image, str(row["sentence"]), number)
    return image


def conceptual_header(draw: ImageDraw.ImageDraw, title: str) -> None:
    draw.text((90, 150), title, font=font(55, True), fill=WHITE, anchor="la")
    rounded(draw, (1700, 118, 2480, 190), 20, "#122a3e", outline=CYAN, width=2)
    label = "CONCEPTUAL — illustration, not data"
    label_font = font(32, True)
    draw.text((2090, 154), label, font=label_font, fill=CYAN, anchor="mm")
    glyph_height = draw.textbbox((0, 0), label, font=label_font)[3]
    if glyph_height < 22:
        raise RuntimeError("conceptual label glyph height below 22 px")


def stack_slide(row: dict[str, Any]) -> Image.Image:
    number = int(row["n"])
    image, draw = base_canvas("CONCEPTUAL CROSS-CHECK")
    conceptual_header(draw, "From many faint spectra to one stacked measurement")
    rounded(draw, (90, 250, 2460, 1170), 36, PANEL, outline="#31516f", width=3)
    if number == 20:
        draw.text((450, 315), "Many faint spectra", font=font(40, True), fill=MUTED, anchor="ma")
        for index in range(8):
            y = 410 + index * 75
            points = []
            for x in range(170, 930, 14):
                yy = y + int(18 * math.sin((x / 52.0) + index * 0.7) + 5 * math.sin(x / 17.0))
                points.append((x, yy))
            draw.line(points, fill=(70 + index * 10, 150 + index * 6, 190 + index * 4), width=4)
        draw.line((1050, 700, 1480, 700), fill=CYAN, width=12)
        draw.polygon([(1480, 700), (1435, 675), (1435, 725)], fill=CYAN)
        rounded(draw, (1600, 460, 2290, 920), 34, PANEL_2, outline=BLUE, width=4)
        draw.text((1945, 610), "Independent", font=font(50, True), fill=WHITE, anchor="mm")
        draw.text((1945, 690), "cross-check", font=font(50, True), fill=WHITE, anchor="mm")
        draw.text((1945, 800), "revealed", font=font(36), fill=BLUE, anchor="mm")
    elif number == 21:
        draw.text((520, 315), "≈ 1,500 galaxies", font=font(54, True), fill=AMBER, anchor="ma")
        for index in range(7):
            y = 440 + index * 75
            draw.line((220, y, 950, 700), fill="#497a9d", width=5)
        draw.line((1040, 700, 1500, 700), fill=CYAN, width=14)
        draw.polygon([(1500, 700), (1450, 670), (1450, 730)], fill=CYAN)
        rounded(draw, (1700, 500, 2230, 900), 34, PANEL_2, outline=BLUE, width=4)
        draw.rectangle((1900, 625, 2030, 755), fill="#69b8eb", outline="#1f78b4", width=12)
        draw.text((1965, 835), "one stacked measurement", font=font(34, True), fill=WHITE, anchor="mm")
    else:
        raise RuntimeError(f"unexpected stack row {number}")
    add_caption(image, str(row["sentence"]), number)
    return image


def uncertainty_slide(row: dict[str, Any]) -> Image.Image:
    number = int(row["n"])
    image, draw = base_canvas("CONCEPTUAL UNCERTAINTY BUDGET")
    conceptual_header(draw, "What could still bend the result?")
    rounded(draw, (85, 245, 1240, 1165), 34, PANEL, outline="#31516f", width=3)
    rounded(draw, (1320, 245, 2475, 1165), 34, PANEL, outline="#31516f", width=3)
    draw.line((1280, 270, 1280, 1140), fill=AMBER, width=5)
    draw.text((660, 320), "Calibration systematic", font=font(43, True), fill=CYAN, anchor="mm")
    draw.text((1895, 320), "Sample size", font=font(43, True), fill=CYAN, anchor="mm")
    if number == 24:
        draw.text((660, 690), "Scale uncertainty", font=font(48, True), fill=MUTED, anchor="mm")
        draw.text((1895, 690), "Five-galaxy limit", font=font(48, True), fill=MUTED, anchor="mm")
    if number in (25, 26, 27):
        draw.text((250, 475), "0", font=font(30), fill=MUTED, anchor="mm")
        draw.text((1100, 475), "0.8 dex", font=font(30), fill=MUTED, anchor="mm")
        draw.line((250, 520, 1100, 520), fill=GRID, width=6)
        scale_w = int(850 * (0.2 / 0.8))
        draw.rectangle((250, 600, 250 + scale_w, 710), fill=CYAN)
        draw.text((250 + scale_w + 25, 655), "0.1–0.2 dex", font=font(38, True), fill=CYAN, anchor="lm")
        draw.text((250, 765), "absolute temperature-based scale", font=font(31), fill=MUTED, anchor="la")
    if number in (26, 27):
        deficit_w = int(850 * (0.69 / 0.8))
        draw.rectangle((250, 865, 250 + deficit_w, 975), fill=AMBER)
        draw.text((250 + deficit_w - 20, 920), "0.69 dex shortfall", font=font(38, True), fill=BG, anchor="rm")
        draw.text((660, 1045), "systematic < measured shortfall", font=font(35, True), fill=WHITE, anchor="mm")
    if number == 27:
        for index in range(5):
            x = 1570 + (index % 3) * 320
            y = 580 + (index // 3) * 300
            draw.ellipse((x - 52, y - 52, x + 52, y + 52), fill=RED, outline="#ff9d92", width=7)
        draw.text((1895, 1020), "five galaxies", font=font(50, True), fill=WHITE, anchor="mm")
        draw.text((1895, 1080), "sample limitation", font=font(34), fill=MUTED, anchor="mm")
    else:
        draw.text((1895, 760), "separate limitation", font=font(38), fill=MUTED, anchor="mm")
    add_caption(image, str(row["sentence"]), number)
    return image


def boundary_slide(row: dict[str, Any]) -> Image.Image:
    number = int(row["n"])
    image, draw = base_canvas("INTERPRETATION BOUNDARY")
    rounded(draw, (150, 180, 2410, 1175), 48, "#221a13", outline=AMBER, width=7)
    draw.text((1280, 300), "INTERPRETATION BOUNDARY", font=font(62, True), fill=AMBER, anchor="mm")
    if number == 28:
        body_font = font(54, True)
        lines = wrap(draw, str(row["sentence"]), body_font, 1950)
        y = 470
        for line in lines:
            draw.text((1280, y), line, font=body_font, fill=WHITE, anchor="ma")
            y += 82
        draw.text((1280, 980), "Automated review ≠ journal or human peer review", font=font(42), fill=MUTED, anchor="mm")
    elif number == 29:
        text = str(row["sentence"])
        draw.text((1280, 650), text, font=font(76, True), fill=WHITE, anchor="mm")
        width = int(draw.textlength(text, font=font(76, True)))
        draw.line((1280 - width // 2, 720, 1280 + width // 2, 720), fill=RED, width=12)
        draw.text((1280, 900), "No sigma or significance value is invented.", font=font(42), fill=MUTED, anchor="mm")
    else:
        raise RuntimeError(f"unexpected boundary row {number}")
    add_caption(image, str(row["sentence"]), number)
    return image


def render_slide(row: dict[str, Any], source: Image.Image) -> Image.Image:
    asset = str(row["asset"])
    if asset == "FIG1":
        return figure_slide(row, source)
    if asset == "CG_D_stacked_crosscheck":
        return stack_slide(row)
    if asset == "CG_E_systematic_budget":
        return uncertainty_slide(row)
    if asset == "TXT_boundary":
        return boundary_slide(row)
    raise RuntimeError(f"unapproved G3 asset {asset}")


def probe(path: Path) -> dict[str, Any]:
    return json.loads(subprocess.check_output([
        FFPROBE, "-v", "error", "-show_entries", "format=duration,size:stream=codec_name,codec_type,width,height,r_frame_rate,pix_fmt,sample_rate,channels", "-of", "json", str(path)
    ], text=True))


def main() -> None:
    for path in (SPEC_PATH, STORYBOARD_PATH, SIGNOFF_PATH, AUDIO_RECEIPT_PATH, FIG1, Path(FONT_REGULAR), Path(FONT_BOLD)):
        if not path.is_file():
            raise FileNotFoundError(path)
    if sha256(FIG1) != EXPECTED_FIG_SHA:
        raise RuntimeError("Figure 1 hash drift")
    if sha256(STORYBOARD_PATH) != EXPECTED_STORYBOARD_SHA:
        raise RuntimeError("storyboard hash drift")
    spec = json.loads(SPEC_PATH.read_text())
    storyboard = json.loads(STORYBOARD_PATH.read_text())
    audio_receipt = json.loads(AUDIO_RECEIPT_PATH.read_text())
    if spec.get("marker") != "NEBULAMIND_V5_G3_MOTION_GRAPHICS_SPEC_V1":
        raise RuntimeError("unexpected G3 spec marker")
    if audio_receipt.get("marker") != "NEBULAMIND_V5_G3_AUDIO_PASS":
        raise RuntimeError("audio receipt does not pass")
    if "HWAO_V5_G3_MOTION_SPEC_SIGNED_COMPLETE" not in SIGNOFF_PATH.read_text():
        raise RuntimeError("semantic sign-off missing")
    selected = [int(value) for value in spec["canary_selection"]["included_storyboard_rows_in_cut_order"]]
    if selected != [int(value) for value in audio_receipt["selected_rows"]]:
        raise RuntimeError("audio row selection drift")
    rows_by_number = {int(row["n"]): row for row in storyboard["rows"]}
    rows = [rows_by_number[number] for number in selected]
    audio_rows = {int(row["storyboard_row"]): row for row in audio_receipt["sentences"]}
    source = Image.open(FIG1).convert("RGB")
    OUT.mkdir(parents=True, exist_ok=True)
    SLIDES.mkdir(parents=True, exist_ok=True)
    SCENES.mkdir(parents=True, exist_ok=True)

    slides: list[dict[str, Any]] = []
    for index, row in enumerate(rows, 1):
        image = render_slide(row, source)
        path = SLIDES / f"scene_{index:02d}_row_{int(row['n']):02d}.png"
        image.save(path, optimize=True)
        slides.append({"cut_index": index, "storyboard_row": int(row["n"]), "path": str(path), "sha256": sha256(path), "size": list(image.size)})
        print(f"slide {index}/{len(rows)} row {row['n']}")

    total_audio = float(audio_receipt["duration_seconds"])
    video_rows: list[dict[str, Any]] = []
    scene_paths: list[Path] = []
    previous_end_frame = 0
    for index, row in enumerate(rows):
        number = int(row["n"])
        start_seconds = float(audio_rows[number]["actual_start_seconds"])
        next_start = float(audio_rows[int(rows[index + 1]["n"])]["actual_start_seconds"]) if index + 1 < len(rows) else total_audio
        start_frame = round(start_seconds * FPS)
        end_frame = round(next_start * FPS) if index + 1 < len(rows) else math.ceil(total_audio * FPS)
        if start_frame != previous_end_frame:
            raise RuntimeError(f"frame timeline gap at row {number}: {start_frame} != {previous_end_frame}")
        frame_count = end_frame - start_frame
        if frame_count <= 0:
            raise RuntimeError(f"invalid frame count row {number}")
        slide = Path(slides[index]["path"])
        scene = SCENES / f"scene_{index + 1:02d}_row_{number:02d}.mp4"
        zoom_increment = 0.00011 if index % 2 == 0 else 0.00009
        vf = (
            f"zoompan=z='min(max(zoom,pzoom)+{zoom_increment},1.022)':"
            "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:"
            f"s={W}x{H}:fps={FPS},format=yuv420p"
        )
        run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-loop", "1", "-i", str(slide),
             "-vf", vf, "-frames:v", str(frame_count), "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
             "-pix_fmt", "yuv420p", "-r", str(FPS), str(scene)])
        scene_paths.append(scene)
        video_start = start_frame / FPS
        onset_error = abs(video_start - start_seconds)
        if onset_error > 0.3:
            raise RuntimeError(f"sync onset failed row {number}: {onset_error}")
        video_rows.append({
            "cut_index": index + 1,
            "storyboard_row": number,
            "audio_start_seconds": start_seconds,
            "video_start_frame": start_frame,
            "video_start_seconds": round(video_start, 6),
            "onset_error_seconds": round(onset_error, 6),
            "frame_count": frame_count,
            "action": row["action"],
            "asset": row["asset"],
            "view_state": row["view_state"],
            "slide": str(slide),
            "scene_video": str(scene),
            "scene_video_sha256": sha256(scene),
        })
        previous_end_frame = end_frame
        print(f"video scene {index + 1}/{len(rows)} row {number} frames={frame_count}")

    concat = OUT / "video_concat.txt"
    concat.write_text("\n".join(f"file '{path.as_posix()}'" for path in scene_paths) + "\n")
    run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(VIDEO_ONLY)])
    master_audio = Path(audio_receipt["master"])
    if sha256(master_audio) != audio_receipt["master_sha256"]:
        raise RuntimeError("audio master hash drift")
    run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", str(VIDEO_ONLY), "-i", str(master_audio),
         "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart", str(VIDEO)])
    run([FFMPEG, "-v", "error", "-xerror", "-i", str(VIDEO), "-f", "null", "-"])
    media = probe(VIDEO)
    video_stream = next(stream for stream in media["streams"] if stream["codec_type"] == "video")
    audio_stream = next(stream for stream in media["streams"] if stream["codec_type"] == "audio")
    if video_stream["codec_name"] != "h264" or video_stream["width"] != W or video_stream["height"] != H or video_stream["r_frame_rate"] != "30/1":
        raise RuntimeError(f"video format failed: {video_stream}")
    if audio_stream["codec_name"] != "aac" or audio_stream["sample_rate"] != "48000" or audio_stream["channels"] != 1:
        raise RuntimeError(f"audio format failed: {audio_stream}")
    video_duration = float(media["format"]["duration"])
    if video_duration > float(spec["plan_totals"]["contract"]["max_seconds"]):
        raise RuntimeError(f"video exceeds duration contract: {video_duration}")

    receipt = {
        "marker": "NEBULAMIND_V5_G3_BUILD_PASS",
        "completed_at_utc": now(),
        "host": "Duhoui-MacStudio.local",
        "spec": str(SPEC_PATH),
        "spec_sha256": sha256(SPEC_PATH),
        "storyboard": str(STORYBOARD_PATH),
        "storyboard_sha256": sha256(STORYBOARD_PATH),
        "semantic_signoff": str(SIGNOFF_PATH),
        "semantic_signoff_sha256": sha256(SIGNOFF_PATH),
        "figure1": str(FIG1),
        "figure1_sha256": sha256(FIG1),
        "figure1_dimensions": list(source.size),
        "view_rois_normalized": VIEW_ROIS,
        "red_point_centers_normalized": RED_POINT_CENTERS_NORM,
        "red_point_region_normalized": RED_POINT_REGION_NORM,
        "blue_point_center_normalized": BLUE_POINT_CENTER_NORM,
        "blue_point_region_normalized": BLUE_POINT_REGION_NORM,
        "plot_overlay_policy": "No generated labels or brackets are placed over source pixels. All generated explanatory annotations live in the external right sidebar; the source plot crop is not redrawn.",
        "font_pixel_contract": {"minimum": 22, "conceptual_label_font_size": 32, "caption_font_size": 43, "sidebar_min_font_size": 25},
        "asset_manifest": {
            "source_assets": [str(FIG1)],
            "generated_asset_classes": ["PIL vector-style conceptual diagrams", "PIL text cards", "source-plot view-state slides"],
            "presenter": False,
            "face": False,
            "office": False,
            "opencv": False,
        },
        "selected_rows": selected,
        "slides": slides,
        "video_rows": video_rows,
        "audio_receipt": str(AUDIO_RECEIPT_PATH),
        "audio_receipt_sha256": sha256(AUDIO_RECEIPT_PATH),
        "audio_duration_seconds": total_audio,
        "delivered_wpm": audio_receipt["delivered_wpm"],
        "video": str(VIDEO),
        "video_sha256": sha256(VIDEO),
        "video_duration_seconds": round(video_duration, 6),
        "media_probe": media,
        "max_action_onset_error_seconds": max(row["onset_error_seconds"] for row in video_rows),
        "external_mutations": {"youtube": False, "visibility": False, "website": False, "database": False, "git": False, "runtime": False, "cockpit": False},
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "video": str(VIDEO), "sha256": receipt["video_sha256"], "duration": video_duration, "wpm": receipt["delivered_wpm"], "max_onset_error": receipt["max_action_onset_error_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
