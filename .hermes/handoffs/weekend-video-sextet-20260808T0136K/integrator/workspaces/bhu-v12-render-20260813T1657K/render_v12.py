#!/usr/bin/env python3
"""Render V12 from Lana's picture-first, closed-world visual contract."""
from __future__ import annotations

import functools
import hashlib
import json
import math
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import PIL
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
ROOT = Path(__file__).resolve().parent
STORY_PATH = SOURCE / "STORYBOARD_DRAFT_V12.json"
NARRATION_PATH = SOURCE / "NARRATION_DRAFT_V12.md"
TEXT_CONTRACT_PATH = SOURCE / "V12_VISUAL_TEXT_CONTRACT.json"
SPEC_PATH = SOURCE / "LANA_VISUAL_REDESIGN_SPEC.md"
TIMELINE_PATH = ROOT / "audio" / "timeline.json"
AUDIO_PATH = ROOT / "audio" / "narration_master.wav"
SRT_PATH = ROOT / "captions_v12.srt"
VTT_PATH = ROOT / "captions_v12.vtt"
GEN_LEDGER_PATH = ROOT / "V12_GENERATION_SPEND_LEDGER.json"
ASSET_DIR = ROOT / "assets" / "generated_prepared"
OUTPUT_DIR = Path("/Users/duhokim/HermesOps/cockpit/videos")
OUTPUT = OUTPUT_DIR / "bhu-closing-record-v12-local-20260813T1657K.mp4"
OUTPUT_SRT = OUTPUT_DIR / "bhu-closing-record-v12-captions-20260813T1657K.srt"
OUTPUT_VTT = OUTPUT_DIR / "bhu-closing-record-v12-captions-20260813T1657K.vtt"
FRAME_DIR = ROOT / "render_states"
CONCAT_PATH = ROOT / "render_states.ffconcat"
MANIFEST_PATH = ROOT / "render_manifest.json"
PREVIEW_DIR = ROOT / "preview"
EXPECTED = {
    "STORYBOARD_DRAFT_V12.json": "9d55257fe62c7a82d2fe32f424e896ce079393219c08aed6663b6c90c3539399",
    "NARRATION_DRAFT_V12.md": "178ffe4ada125668c8ff84bc156adee7820954591f9781adb7101aac562d80da",
    "V12_VISUAL_TEXT_CONTRACT.json": "c91662e15de095161e84d128683dd69150c8a73b4cbb6f303dda8f79c943999c",
    "LANA_VISUAL_REDESIGN_SPEC.md": "cf9cefe8a0c07f8cc960388004a20d4518a7cf7fbcea5ff688825ffdc47bfd22",
    "audio/timeline.json": "c30c93419f7f09402524444d4107a74f9be59e1299dec2c99f3b2d3e3950f6fe",
    "audio/narration_master.wav": "b65dd6bedfb4dd460ae386b1d4b0caecbcf8531be6501ea2496465efab56be0a",
    "captions_v12.srt": "8966f66a3d74c9b0e0c80c7d1aff9651bf6a5ee7267d72347f75f86d3ad7d8d5",
    "captions_v12.vtt": "e893244f46e9bd377defc81d4afeb37a32a211adafee776103baa32790874f13",
    "V12_GENERATION_SPEND_LEDGER.json": "65b465fcb225c8d0bdb3e7214324aaa08e800a9133abac2095670fdb24ec4489",
}
W, H, FPS, DURATION = 1920, 1080, 30, 402
BG = (8, 14, 28)
BG2 = (14, 25, 47)
WHITE = (241, 245, 250)
MUTED = (153, 170, 194)
BLUE = (96, 190, 255)
CYAN = (76, 220, 218)
AMBER = (246, 185, 96)
CORAL = (242, 116, 106)
GREEN = (113, 210, 155)
PURPLE = (176, 133, 238)
GRID = (50, 74, 108)
FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"
SERIF_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
MONO_PATH = "/System/Library/Fonts/Menlo.ttc"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, capture_output=True, text=True)


@functools.lru_cache(maxsize=None)
def font(size: int, bold: bool = False, serif: bool = False, mono: bool = False):
    path = SERIF_PATH if serif else MONO_PATH if mono else FONT_PATH
    index = 1 if bold and path == FONT_PATH else 0
    return ImageFont.truetype(path, size, index=index)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def smooth(value: float) -> float:
    value = clamp(value)
    return value * value * (3 - 2 * value)


def center(draw: ImageDraw.ImageDraw, value: str, xy: tuple[float, float], size: int, color=WHITE, bold=False, serif=False, mono=False):
    face = font(size, bold, serif, mono)
    box = draw.textbbox((0, 0), value, font=face)
    draw.text((xy[0] - (box[2] - box[0]) / 2, xy[1] - (box[3] - box[1]) / 2), value, font=face, fill=color)


def wrap(draw: ImageDraw.ImageDraw, value: str, box: tuple[int, int, int, int], size: int, color=WHITE, bold=False, max_lines=3, align="center", serif=False):
    face = font(size, bold, serif)
    words = value.split()
    lines = []
    current = ""
    width = box[2] - box[0]
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=face) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > max_lines:
        raise RuntimeError(f"text overflows {max_lines} lines: {value}")
    line_height = size + 8
    total = len(lines) * line_height - 8
    y = box[1] + (box[3] - box[1] - total) / 2
    for line in lines:
        length = draw.textlength(line, font=face)
        x = box[0] if align == "left" else box[2] - length if align == "right" else box[0] + (width - length) / 2
        draw.text((x, y), line, font=face, fill=color)
        y += line_height


def rounded(draw, box, radius=24, fill=BG2, outline=GRID, width=3):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def line_arrow(draw, start, end, color=CYAN, width=6, head=18):
    draw.line((*start, *end), fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    for offset in (2.55, -2.55):
        draw.line((end[0], end[1], end[0] + head * math.cos(angle + offset), end[1] + head * math.sin(angle + offset)), fill=color, width=width)


def background() -> Image.Image:
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    for radius, alpha in ((750, 35), (520, 28), (300, 24)):
        color = tuple(round(BG[i] * (1 - alpha / 255) + BLUE[i] * alpha / 255) for i in range(3))
        draw.ellipse((960 - radius * 1.55, 515 - radius, 960 + radius * 1.55, 515 + radius), fill=color)
    return image


@functools.lru_cache(maxsize=None)
def asset(name: str) -> Image.Image:
    path = ASSET_DIR / name
    if not path.exists():
        raise RuntimeError(f"prepared generated asset missing: {path}")
    return Image.open(path).convert("RGB")


def fit_image(source: Image.Image, box: tuple[int, int, int, int], cover=False) -> Image.Image:
    bw, bh = box[2] - box[0], box[3] - box[1]
    ratio = max(bw / source.width, bh / source.height) if cover else min(bw / source.width, bh / source.height)
    size = (max(1, round(source.width * ratio)), max(1, round(source.height * ratio)))
    resized = source.resize(size, Image.Resampling.LANCZOS)
    if cover:
        left = max(0, (resized.width - bw) // 2)
        top = max(0, (resized.height - bh) // 2)
        resized = resized.crop((left, top, left + bw, top + bh))
    return resized


def paste_asset(image: Image.Image, name: str, box: tuple[int, int, int, int], opacity=1.0, cover=False):
    prepared = fit_image(asset(name), box, cover)
    x = box[0] + ((box[2] - box[0]) - prepared.width) // 2
    y = box[1] + ((box[3] - box[1]) - prepared.height) // 2
    if opacity >= 0.999:
        image.paste(prepared, (x, y))
    else:
        image.paste(prepared, (x, y), Image.new("L", prepared.size, round(255 * opacity)))


def glow_circle(draw, xy, radius, color, width=0):
    x, y = xy
    for ring in range(4, 0, -1):
        rr = radius + ring * 8
        blend = tuple(round(BG[i] * (1 - 0.10 * ring) + color[i] * 0.10 * ring) for i in range(3))
        draw.ellipse((x - rr, y - rr, x + rr, y + rr), fill=blend)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=WHITE if width else None, width=width)


def sun(draw, xy, radius, fraction=1.0, color=AMBER):
    x, y = xy
    if fraction >= 0.999:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=WHITE, width=3)
    else:
        draw.pieslice((x - radius, y - radius, x + radius, y + radius), 90, 270, fill=color, outline=WHITE, width=3)
    for angle in range(0, 360, 45):
        a = math.radians(angle)
        start = (x + math.cos(a) * (radius + 6), y + math.sin(a) * (radius + 6))
        end = (x + math.cos(a) * (radius + 16), y + math.sin(a) * (radius + 16))
        draw.line((*start, *end), fill=color, width=3)


def spiral(draw, xy, radius, color=BLUE, flip=1, phase=0.0, width=5):
    points = []
    x, y = xy
    for index in range(90):
        angle = phase + index * 0.19
        r = radius * index / 90
        points.append((x + flip * math.cos(angle) * r, y + math.sin(angle) * r * 0.52))
    if len(points) > 1:
        draw.line(points, fill=color, width=width, joint="curve")
    draw.ellipse((x - 6, y - 6, x + 6, y + 6), fill=WHITE)


def gate(draw, x, y, scale=1.0, closure=1.0, locked=False):
    width, height = 420 * scale, 230 * scale
    top = y - height * closure
    post_w = 26 * scale
    draw.rounded_rectangle((x - width / 2 - post_w, y - height - 20 * scale, x - width / 2 + post_w, y + 28 * scale), radius=8, fill=(126, 84, 50), outline=AMBER, width=max(2, round(3 * scale)))
    draw.rounded_rectangle((x + width / 2 - post_w, y - height - 20 * scale, x + width / 2 + post_w, y + 28 * scale), radius=8, fill=(126, 84, 50), outline=AMBER, width=max(2, round(3 * scale)))
    for fraction in (0.17, 0.50, 0.83):
        yy = top + height * fraction
        draw.rounded_rectangle((x - width / 2, yy - 10 * scale, x + width / 2, yy + 10 * scale), radius=5, fill=(168, 112, 64), outline=AMBER, width=max(1, round(2 * scale)))
    draw.line((x - width / 2 + 25 * scale, top + height * 0.12, x + width / 2 - 25 * scale, top + height * 0.88), fill=(168, 112, 64), width=max(4, round(18 * scale)))
    if locked:
        lock(draw, x, y - height * 0.42, scale * 0.75, "plain")


def lock(draw, x, y, scale=1.0, kind="plain"):
    body = (x - 58 * scale, y - 10 * scale, x + 58 * scale, y + 92 * scale)
    draw.arc((x - 43 * scale, y - 60 * scale, x + 43 * scale, y + 22 * scale), 180, 360, fill=WHITE, width=max(4, round(12 * scale)))
    draw.rounded_rectangle(body, radius=15 * scale, fill=(198, 139, 67), outline=WHITE, width=max(2, round(3 * scale)))
    if kind == "ruler":
        draw.rectangle((x - 33 * scale, y + 28 * scale, x + 33 * scale, y + 42 * scale), fill=BLUE)
    elif kind == "footprint":
        footprint(draw, (x, y + 41 * scale), scale * 0.28, BG2)
    else:
        draw.ellipse((x - 8 * scale, y + 30 * scale, x + 8 * scale, y + 46 * scale), fill=BG)


def footprint(draw, xy, scale=1.0, color=AMBER):
    x, y = xy
    draw.ellipse((x - 44 * scale, y - 4 * scale, x + 44 * scale, y + 58 * scale), fill=color)
    for dx, dy, radius in ((-55, -35, 15), (-22, -55, 16), (17, -57, 16), (52, -37, 15)):
        draw.ellipse((x + (dx - radius) * scale, y + (dy - radius) * scale, x + (dx + radius) * scale, y + (dy + radius) * scale), fill=color)


def dartboard(draw, xy, radius=175):
    x, y = xy
    for fraction, color in ((1.0, (225, 222, 198)), (0.78, CORAL), (0.56, (225, 222, 198)), (0.34, BLUE), (0.12, AMBER)):
        r = radius * fraction
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color, outline=WHITE, width=3)


def dart(draw, start, end, color=WHITE, progress=1.0):
    px = start[0] + (end[0] - start[0]) * progress
    py = start[1] + (end[1] - start[1]) * progress
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    length = 88
    tail = (px - math.cos(angle) * length, py - math.sin(angle) * length)
    draw.line((*tail, px, py), fill=color, width=6)
    normal = angle + math.pi / 2
    for side in (-1, 1):
        wing = (tail[0] + math.cos(normal) * 18 * side, tail[1] + math.sin(normal) * 18 * side)
        draw.polygon([tail, wing, (tail[0] - math.cos(angle) * 22, tail[1] - math.sin(angle) * 22)], fill=CORAL)


def key(draw, x, y, kind="range", scale=1.0):
    color = GREEN if kind == "range" else CYAN
    draw.ellipse((x - 62 * scale, y - 62 * scale, x + 62 * scale, y + 62 * scale), outline=color, width=max(5, round(14 * scale)))
    draw.line((x + 60 * scale, y, x + 260 * scale, y), fill=color, width=max(7, round(22 * scale)))
    draw.line((x + 205 * scale, y, x + 205 * scale, y + 52 * scale), fill=color, width=max(5, round(18 * scale)))
    draw.line((x + 250 * scale, y, x + 250 * scale, y + 36 * scale), fill=color, width=max(5, round(18 * scale)))
    if kind == "range":
        draw.rounded_rectangle((x - 38 * scale, y - 20 * scale, x + 38 * scale, y + 20 * scale), radius=8, fill=AMBER)
        draw.line((x - 26 * scale, y - 30 * scale, x - 26 * scale, y + 30 * scale), fill=WHITE, width=max(2, round(5 * scale)))
        draw.line((x + 26 * scale, y - 30 * scale, x + 26 * scale, y + 30 * scale), fill=WHITE, width=max(2, round(5 * scale)))
    else:
        spiral(draw, (x, y), 40 * scale, color=AMBER, width=max(2, round(5 * scale)))


def text_plate(draw, value, box, color=WHITE, size=32, max_lines=2):
    rounded(draw, box, 22, (10, 18, 34), color, 3)
    wrap(draw, value, (box[0] + 24, box[1] + 10, box[2] - 24, box[3] - 10), size, color, True, max_lines=max_lines)


def reveal_map(card: dict) -> dict[str, float]:
    return {item["name"]: float(item["card_seconds"]) for item in card["reveals"]}


def shown(times: dict[str, float], name: str, t: float) -> bool:
    return t + 1e-9 >= times[name]


def draw_card01(image, draw, t, times, hide_text=False):
    # Local open book: the same source visibly produces two distinct routes.
    draw.polygon([(560, 875), (920, 760), (950, 955), (570, 1000)], fill=(225, 214, 183), outline=AMBER)
    draw.polygon([(960, 760), (1360, 875), (1350, 1000), (970, 955)], fill=(232, 220, 190), outline=AMBER)
    draw.line((960, 762, 960, 957), fill=(125, 83, 55), width=9)
    for offset in (22, 48, 74):
        draw.arc((590, 845 + offset, 945, 1010 + offset), 190, 345, fill=(150, 126, 93), width=3)
        draw.arc((975, 845 + offset, 1330, 1010 + offset), 195, 350, fill=(150, 126, 93), width=3)
    origin = (960, 765)
    if shown(times, "number_we_can_check", t):
        left_path = [(origin[0]-18, origin[1]), (810, 650), (650, 520), (505, 360)]
        draw.line(left_path, fill=(238, 229, 191), width=62, joint="curve")
        draw.line(left_path, fill=AMBER, width=5, joint="curve")
        star_x, star_y = 470, 305
        points = []
        for index in range(10):
            angle = -math.pi/2 + index*math.pi/5
            radius = 72 if index % 2 == 0 else 30
            points.append((star_x + math.cos(angle)*radius, star_y + math.sin(angle)*radius))
        draw.polygon(points, fill=AMBER, outline=WHITE)
    if shown(times, "galaxy_spin_limits", t):
        right_path = [(origin[0]+18, origin[1]), (1115, 650), (1290, 535), (1445, 390)]
        draw.line(right_path, fill=(129, 112, 180), width=62, joint="curve")
        draw.line(right_path, fill=PURPLE, width=5, joint="curve")
        for x, y, rx, ry, color in (
            (1370, 300, 225, 150, (44, 36, 91)),
            (1530, 345, 250, 170, (51, 39, 106)),
            (1260, 410, 210, 130, (40, 34, 82)),
        ):
            draw.ellipse((x-rx, y-ry, x+rx, y+ry), fill=color)
        for x, y, radius, flip in ((1325, 265, 70, 1), (1515, 330, 82, -1), (1425, 425, 54, 1)):
            spiral(draw, (x, y), radius, PURPLE, flip, width=6)
    if shown(times, "route_verdict", t):
        progress = smooth((t - times["route_verdict"]) / 2.0)
        gate(draw, 1435, 545, 0.78, progress)
    if not hide_text:
        text_plate(draw, "A PERSONAL SIDE-QUESTION · NOT PART OF THE LAB'S RESEARCH PROGRAMME", (42, 42, 720, 116), BLUE, 22, 2)
        if shown(times, "route_verdict", t):
            text_plate(draw, "ROUTE CLOSED", (675, 890, 1245, 970), CORAL, 38, 1)


def draw_card02(image, draw, t, times, hide_text=False):
    positions = [
        ("proposal_1", "card02_nested.png", (150, 160, 530, 500), "CLOSED UNIVERSE", BLUE),
        ("proposal_2", "card02_bounce.png", (605, 140, 970, 500), "COLLAPSE BOUNCE", AMBER),
        ("proposal_3", "card02_parent_top.png", (1070, 130, 1410, 500), "INHERITED SPIN", PURPLE),
        ("proposal_4", "card02_family.png", (410, 520, 820, 870), "REPRODUCING UNIVERSES", GREEN),
        ("proposal_5", "card02_fingerprints.png", (1090, 530, 1610, 870), "DISTINCT FINGERPRINTS", CYAN),
    ]
    root = (960, 510)
    for index, (name, filename, box, label, color) in enumerate(positions):
        if shown(times, name, t):
            target = ((box[0] + box[2]) // 2, (box[1] + box[3]) // 2)
            endpoint = (target[0] + (-85, -35, 45, -55, 90)[index], target[1] + (-25, -60, -10, 50, 70)[index])
            line_arrow(draw, root, endpoint, color, 4, 14)
            paste_asset(image, filename, box, 0.95)
            draw = ImageDraw.Draw(image)
            if name == "proposal_3":
                paste_asset(image, "card02_child_top.png", (1330, 265, 1580, 500), 0.95)
                draw = ImageDraw.Draw(image)
            if not hide_text:
                center(draw, label, ((box[0] + box[2]) / 2, box[3] + 28), 22, color, True)
    glow_circle(draw, root, 55, BLUE)
    if not hide_text and shown(times, "bhu", t):
        text_plate(draw, "BLACK-HOLE UNIVERSE (BHU)", (640, 425, 1280, 505), BLUE, 30, 1)
    if not hide_text and shown(times, "no_shared_forecast", t):
        text_plate(draw, "FIVE IDEAS — NO SHARED PREDICTION", (500, 910, 1420, 985), CORAL, 32, 1)


def draw_card03(image, draw, t, times, hide_text=False):
    first = times["target"]
    second = times["identify"]
    dwell = max(second + 4.0, 35.5)
    if t < first:
        glow_circle(draw, (300, 550), 72, BLUE)
        dartboard(draw, (1450, 540), 190)
        dart(draw, (380, 550), (1240, 360), WHITE, clamp(t / max(1, first)))
    elif t < second:
        glow_circle(draw, (300, 550), 72, BLUE)
        board_alpha = 1.0 - clamp((t - first) / 2.0)
        if board_alpha > 0:
            board_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(board_layer)
            dartboard(bd, (1450, 540), 190)
            board_layer.putalpha(round(255 * board_alpha))
            image.paste(board_layer.convert("RGB"), (0, 0), board_layer.getchannel("A"))
            draw = ImageDraw.Draw(image)
        dart(draw, (380, 550), (1780, 430), WHITE, clamp((t - first) / 3.0))
    else:
        glow_circle(draw, (260, 360), 66, BLUE)
        glow_circle(draw, (260, 720), 66, AMBER)
        dartboard(draw, (1450, 540), 190)
        p = smooth(clamp((t - second) / 3.0))
        dart(draw, (340, 360), (1450, 520), BLUE, p)
        dart(draw, (340, 720), (1450, 560), AMBER, p)
        if t >= dwell:
            draw.ellipse((1432, 522, 1468, 558), outline=WHITE, width=5)


def draw_card04(image, draw, t, times, hide_text=False):
    # Quantitative card: no generated asset is loaded or pasted here.
    draw.rounded_rectangle((300, 140, 1620, 900), radius=60, fill=(12, 23, 42), outline=GRID, width=4)
    column_x = 965
    floor_y, lid_y, top_y = 790, 500, 230
    draw.line((column_x, floor_y, column_x, top_y), fill=GRID, width=8)
    # Deterministic sun units: one-and-a-half below the lid, two above it.
    sun(draw, (790, lid_y), 48, 1.0)
    sun(draw, (895, lid_y), 48, 0.5)
    draw.line((650, lid_y - 5, 1280, lid_y - 5), fill=CORAL, width=20)
    sun(draw, (790, top_y + 35), 48, 1.0)
    sun(draw, (895, top_y + 35), 48, 1.0)
    progress = smooth(clamp((t - times["mass_1_5"]) / max(1.0, (47 - times["mass_1_5"] - 1.0)))) if shown(times, "mass_1_5", t) else 0.0
    star_y = floor_y - progress * (floor_y - lid_y - 75)
    radius = 48 + progress * 52
    sun(draw, (column_x, star_y), radius, 1.0, AMBER)
    if shown(times, "family_tree", t):
        for x, y, r in ((360, 260, 42), (430, 340, 30), (290, 355, 28), (500, 420, 22)):
            draw.ellipse((x-r, y-r, x+r, y+r), outline=BLUE, width=5)
        line_arrow(draw, (390, 280), (445, 327), CYAN, 4, 12)
        line_arrow(draw, (385, 290), (310, 335), CYAN, 4, 12)
        line_arrow(draw, (440, 365), (490, 405), CYAN, 4, 12)
    if not hide_text and shown(times, "source_quote", t):
        text_plate(draw, "“SERIOUS DOUBT OR SIMPLY FALSIFY” — BROWN, LEE & RHO", (330, 925, 1590, 1002), CORAL, 30, 1)


def mass_position(value: float) -> float:
    return 230 + (value - 1.4) / 0.8 * (1690 - 230)


def gradient_no_terminus(image: Image.Image, y0: int, y1: int, peak: int, intensity: float):
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    pixels = overlay.load()
    if pixels is None:
        raise RuntimeError("gradient pixel buffer unavailable")
    left, right = round(mass_position(1.4)), round(mass_position(2.2))
    for x in range(left, right):
        if x <= peak:
            u = (x - left) / max(1, peak - left)
        else:
            u = (right - 1 - x) / max(1, right - 1 - peak)
        alpha = round(150 * intensity * max(0.0, u) ** 2)
        for y in range(y0, y1):
            pixels[x, y] = (*GREEN, alpha)
    image.paste(overlay.convert("RGB"), (0, 0), overlay.getchannel("A"))


def draw_card05(image, draw, t, times, hide_text=False):
    # Quantitative card: no generated asset is loaded or pasted here.
    axis_y = 700
    draw.line((230, axis_y, 1690, axis_y), fill=WHITE, width=5)
    sun(draw, (mass_position(1.5), 790), 34, 1.0)
    sun(draw, (mass_position(1.5) + 75, 790), 34, 0.5)
    sun(draw, (mass_position(2.0) - 40, 790), 34, 1.0)
    sun(draw, (mass_position(2.0) + 40, 790), 34, 1.0)
    if shown(times, "demorest_uncertainty", t):
        y = 430
        x0, x1, xc = mass_position(1.93), mass_position(2.01), mass_position(1.97)
        draw.line((x0, y, x1, y), fill=BLUE, width=15)
        draw.line((x0, y-20, x0, y+20), fill=BLUE, width=5); draw.line((x1, y-20, x1, y+20), fill=BLUE, width=5)
        sun(draw, (xc, y), 18, 1.0, WHITE)
        if not hide_text:
            center(draw, "1.97 ± 0.04 M☉", ((x0+x1)/2, y-70), 28, BLUE, True, serif=True)
    if shown(times, "fonseca_uncertainty", t):
        y = 570
        x0, x1, xc = mass_position(2.01), mass_position(2.15), mass_position(2.08)
        if shown(times, "percent_95_4", t):
            progress = smooth(clamp((t - times["percent_95_4"]) / 8.0))
            gradient_no_terminus(image, y-24, y+25, round(xc), progress)
            draw = ImageDraw.Draw(image)
        else:
            draw.line((x0, y, x1, y), fill=GREEN, width=15)
            draw.line((x0, y-20, x0, y+20), fill=GREEN, width=5); draw.line((x1, y-20, x1, y+20), fill=GREEN, width=5)
        sun(draw, (xc, y), 18, 1.0, WHITE)
        if not hide_text:
            center(draw, "2.08 ± 0.07 M☉", ((x0+x1)/2, y-75), 28, GREEN, True, serif=True)
            if shown(times, "percent_68_3", t) and not shown(times, "percent_95_4", t):
                center(draw, "68.3%", ((x0+x1)/2, y+58), 26, GREEN, True)
    if not hide_text and shown(times, "percent_95_4", t):
        text_plate(draw, "AT 95.4% CREDIBILITY, THE CLOSING RECORD STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00", (215, 900, 1705, 1005), CORAL, 27, 2)


def draw_card06(image, draw, t, times, hide_text=False):
    paste_asset(image, "card06_fork_background.png", (0, 0, W, H), 0.43, True)
    draw = ImageDraw.Draw(image)
    # Cover the generated rectangular sign; replace with a local two-arm signpost.
    draw.rounded_rectangle((650, 180, 1270, 390), radius=35, fill=(12, 23, 42))
    draw.line((960, 350, 960, 740), fill=(144, 94, 55), width=30)
    left = [(960, 310), (670, 240), (520, 330), (920, 410)]
    right = [(960, 310), (1250, 240), (1400, 330), (1000, 410)]
    draw.polygon(left, fill=(55, 42, 42), outline=AMBER)
    draw.polygon(right, fill=(55, 35, 42), outline=CORAL)
    if not hide_text and shown(times, "source_disjunction", t):
        wrap(draw, "SERIOUS DOUBT", (555, 260, 915, 365), 30, AMBER, True, 2)
        wrap(draw, "SIMPLY FALSIFY", (1005, 260, 1365, 365), 30, CORAL, True, 2)
        center(draw, "OR", (960, 210), 32, WHITE, True)
    start = (960, 970); stop = (960, 675)
    progress = smooth(clamp((t - times["not_adjudicated"]) / 3.0)) if shown(times, "not_adjudicated", t) else 0.0
    marker = (start[0], start[1] + (stop[1] - start[1]) * progress)
    glow_circle(draw, marker, 32, BLUE)


def draw_card07(image, draw, t, times, hide_text=False):
    if shown(times, "cw_ccw", t):
        # The generated galaxy crop supplies icon texture only; all stack geometry is local.
        galaxy_sheet = asset("card07_galaxies.png")
        cells = [(0, 0, 260, 190), (260, 0, 520, 190), (0, 190, 260, 380), (260, 190, 520, 380), (0, 380, 260, 576), (260, 380, 520, 576)]
        left_centers = [(590, 760), (590, 610), (590, 460), (590, 310)]
        right_centers = [(1330, 760), (1330, 610), (1330, 460)]
        for index, (x, y) in enumerate(left_centers + right_centers):
            crop = galaxy_sheet.crop(cells[index % len(cells)])
            prepared = fit_image(crop, (x-150, y-90, x+150, y+90))
            image.paste(prepared, (x-prepared.width//2, y-prepared.height//2))
            draw = ImageDraw.Draw(image)
            spiral(draw, (x, y), 62, BLUE if index < len(left_centers) else PURPLE, 1 if index < len(left_centers) else -1, phase=(t % 2) * 0.6, width=4)
        draw.line((875, 275, 1045, 275), fill=MUTED, width=5)
        draw.line((875, 460, 1045, 460), fill=MUTED, width=5)
        draw.line((960, 275, 960, 460), fill=MUTED, width=3)
    else:
        spiral(draw, (650, 540), 155, BLUE, 1, width=8)
        spiral(draw, (1270, 540), 155, PURPLE, -1, width=8)
    if not hide_text and shown(times, "no_amplitude", t):
        center(draw, "?", (960, 360), 95, AMBER, True)


def blank_prop(draw, kind, box, color):
    x0, y0, x1, y1 = box
    rounded(draw, box, 24, (12, 24, 43), color, 4)
    cx, cy = (x0+x1)/2, (y0+y1)/2
    if kind == "ruler":
        draw.rounded_rectangle((cx-85, cy-18, cx+85, cy+18), radius=8, fill=color)
    elif kind == "map":
        draw.polygon([(cx-95, cy-55), (cx-30, cy-75), (cx+30, cy-55), (cx+95, cy-75), (cx+95, cy+65), (cx+30, cy+45), (cx-30, cy+65), (cx-95, cy+45)], outline=color, fill=(20, 35, 56))
    elif kind == "compass":
        draw.ellipse((cx-70, cy-70, cx+70, cy+70), outline=color, width=8)
        draw.ellipse((cx-7, cy-7, cx+7, cy+7), fill=MUTED)
    else:
        draw.arc((cx-85, cy-70, cx+85, cy+95), 180, 360, fill=color, width=8)
        draw.ellipse((cx-7, cy-7, cx+7, cy+7), fill=MUTED)


def draw_card08(image, draw, t, times, hide_text=False):
    draw.line((180, 430, 1740, 430), fill=GRID, width=8)
    if shown(times, "timeline", t):
        paste_asset(image, "card08_photos.png", (180, 105, 700, 400), 0.9)
        draw = ImageDraw.Draw(image)
        draw.ellipse((540, 408, 584, 452), fill=BLUE)
        draw.rounded_rectangle((1080, 140, 1360, 380), radius=18, fill=(238, 228, 196), outline=AMBER, width=5)
        paste_asset(image, "card08_bubble.png", (1270, 85, 1740, 390), 0.88)
        draw = ImageDraw.Draw(image)
        draw.ellipse((1240, 408, 1284, 452), fill=AMBER)
        if not hide_text:
            center(draw, "2025", (1262, 485), 28, AMBER, True, mono=True)
    if shown(times, "forecast_blanks", t):
        elapsed = t - times["forecast_blanks"]
        kinds = ["ruler", "map", "compass", "meter"]
        colors = [BLUE, PURPLE, CYAN, CORAL]
        for index, (kind, color) in enumerate(zip(kinds, colors)):
            if elapsed >= index:
                box = (130 + index*430, 600, 520 + index*430, 870)
                blank_prop(draw, kind, box, color)
                if not hide_text:
                    center(draw, "?", ((box[0]+box[2])/2, 910), 48, color, True)


def draw_card09(image, draw, t, times, hide_text=False):
    paste_asset(image, "card09_final.png", (0, 0, W, H), 0.82, True)
    draw = ImageDraw.Draw(image)
    if shown(times, "other_causes", t):
        origin = (960, 690)
        for end in ((430, 350), (960, 285), (1490, 350)):
            line_arrow(draw, origin, end, MUTED, 6, 17)
    if not hide_text and shown(times, "measurement_not_identification", t):
        text_plate(draw, "MEASUREMENT ≠ IDENTIFICATION", (570, 920, 1350, 1000), CORAL, 34, 1)


def draw_card10(image, draw, t, times, hide_text=False):
    draw.polygon([(420, 1010), (720, 540), (1200, 540), (1500, 1010)], fill=(20, 38, 62), outline=GRID)
    gate(draw, 960, 665, 1.35, 1.0)
    if shown(times, "no_range", t):
        lock(draw, 790, 555, 0.85, "ruler")
    if shown(times, "no_signature", t):
        lock(draw, 1130, 555, 0.85, "footprint")
    if shown(times, "trustworthy_measurement", t):
        glow_circle(draw, (960, 880), 35, BLUE)


def unequal_stack_token(draw, x, y, scale=1.0):
    for column, count, color in ((-1, 4, BLUE), (1, 3, PURPLE)):
        for index in range(count):
            yy = y - index * 38 * scale
            draw.ellipse((x + column*55*scale - 34*scale, yy-16*scale, x + column*55*scale + 34*scale, yy+16*scale), fill=color, outline=WHITE, width=max(1, round(2*scale)))


def draw_card11(image, draw, t, times, hide_text=False):
    draw.polygon([(360, 1020), (680, 610), (1240, 610), (1560, 1020)], fill=(20, 38, 62), outline=GRID)
    gate(draw, 960, 725, 1.45, 1.0, locked=True)
    keyhole_y = 555
    draw.ellipse((720, keyhole_y-44, 808, keyhole_y+44), fill=(5, 9, 18), outline=GREEN, width=6)
    draw.ellipse((1112, keyhole_y-44, 1200, keyhole_y+44), fill=(5, 9, 18), outline=CYAN, width=6)
    if shown(times, "target_gate", t):
        key(draw, 330, 300, "range", 0.75)
    if shown(times, "signature_gate", t):
        key(draw, 1330, 300, "fingerprint", 0.75)
    if shown(times, "asymmetry_alone", t):
        elapsed = t - times["asymmetry_alone"]
        if elapsed < 2.0:
            x = 960 - 180 * smooth(elapsed/2.0)
        elif elapsed < 4.0:
            x = 780 + 360 * smooth((elapsed-2.0)/2.0)
        else:
            x = 960
        unequal_stack_token(draw, x, 915, 0.72)
        if elapsed >= 4.0:
            draw.line((910, 860, 1010, 960), fill=CORAL, width=10)
            draw.line((1010, 860, 910, 960), fill=CORAL, width=10)
    if not hide_text and shown(times, "reopen", t):
        text_plate(draw, "REOPENS ONLY WITH A NUMBER — OR A FINGERPRINT", (430, 935, 1490, 1015), GREEN, 32, 1)


DRAWERS: dict[str, Callable] = {
    "01": draw_card01, "02": draw_card02, "03": draw_card03, "04": draw_card04, "05": draw_card05,
    "06": draw_card06, "07": draw_card07, "08": draw_card08, "09": draw_card09, "10": draw_card10, "11": draw_card11,
}


class Renderer:
    def __init__(self):
        paths = {
            "STORYBOARD_DRAFT_V12.json": STORY_PATH, "NARRATION_DRAFT_V12.md": NARRATION_PATH,
            "V12_VISUAL_TEXT_CONTRACT.json": TEXT_CONTRACT_PATH, "LANA_VISUAL_REDESIGN_SPEC.md": SPEC_PATH,
            "audio/timeline.json": TIMELINE_PATH, "audio/narration_master.wav": AUDIO_PATH,
            "captions_v12.srt": SRT_PATH, "captions_v12.vtt": VTT_PATH,
            "V12_GENERATION_SPEND_LEDGER.json": GEN_LEDGER_PATH,
        }
        for name, path in paths.items():
            actual = sha(path)
            if actual != EXPECTED[name]:
                raise RuntimeError(f"frozen input drift {name}: {actual}")
        self.story = json.loads(STORY_PATH.read_text())
        self.timeline = json.loads(TIMELINE_PATH.read_text())
        self.text_contract = json.loads(TEXT_CONTRACT_PATH.read_text())
        self.ledger = json.loads(GEN_LEDGER_PATH.read_text())
        if self.story["estimated_duration_seconds"] != DURATION or float(self.timeline["master_duration_seconds"]) != DURATION:
            raise RuntimeError("V12 duration contract drift")
        if any(abs(float(card["delivered_wpm"]) - 142.0) > 0.02 for card in self.timeline["cards"]):
            raise RuntimeError("V12 audio not at 142 WPM")
        if not self.story["render_contract"]["embedded_subtitle_stream_required"]:
            raise RuntimeError("subtitle stream gate missing from story")
        if self.ledger["boundary"]["cards_04_05_generated_pixels"]:
            raise RuntimeError("generation ledger permits pixels in quantitative cards")
        self.cards = self.timeline["cards"]
        self.story_cards = {card["id"]: card for card in self.story["cards"]}
        if {card["card_id"] for card in self.cards} != set(self.story_cards):
            raise RuntimeError("timeline/story card set mismatch")
        for card in self.cards:
            spec = self.story_cards[card["card_id"]]
            if card["narration"] != spec["narration"] or float(card["planned_seconds"]) != float(spec["planned_seconds"]):
                raise RuntimeError(f"timeline/story drift Card {card['card_id']}")
        self.generated_asset_usage = {"01": [], "02": ["card02_nested.png", "card02_family.png", "card02_fingerprints.png", "card02_bounce.png", "card02_parent_top.png", "card02_child_top.png"], "03": [], "04": [], "05": [], "06": ["card06_fork_background.png"], "07": ["card07_galaxies.png"], "08": ["card08_photos.png", "card08_bubble.png"], "09": ["card09_final.png"], "10": [], "11": []}
        if self.generated_asset_usage["04"] or self.generated_asset_usage["05"]:
            raise RuntimeError("generated asset assigned to quantitative card")

    def active_card(self, master_t: float) -> tuple[dict, float]:
        for card in self.cards:
            if master_t < float(card["master_end_seconds"]) - 1e-9:
                return card, master_t - float(card["master_start_seconds"])
        return self.cards[-1], float(self.cards[-1]["planned_seconds"]) - 1 / FPS

    def frame(self, master_t: float, hide_text=False) -> Image.Image:
        card, card_t = self.active_card(master_t)
        image = background()
        draw = ImageDraw.Draw(image)
        DRAWERS[card["card_id"]](image, draw, card_t, reveal_map(card), hide_text)
        return image.convert("RGB")

    def interval_boundaries(self) -> list[int]:
        boundaries = {0, DURATION * FPS}
        for card in self.cards:
            start = float(card["master_start_seconds"])
            end = float(card["master_end_seconds"])
            boundaries |= {round(start*FPS), round(end*FPS)}
            for reveal in card["reveals"]:
                at = float(reveal["master_seconds"])
                boundaries.add(math.ceil(at*FPS))
            cid = card["card_id"]
            times = reveal_map(card)
            def add_steps(card_seconds_start: float, span: float, steps: int):
                for index in range(steps+1):
                    value = start + card_seconds_start + span * index / steps
                    if start <= value <= end:
                        boundaries.add(math.ceil(value*FPS))
            if cid == "01": add_steps(times["route_verdict"], 2.0, 6)
            elif cid == "03":
                add_steps(0.0, max(1.0, times["target"]), 6); add_steps(times["target"], 3.0, 6); add_steps(times["identify"], 3.0, 6)
            elif cid == "04": add_steps(times["mass_1_5"], max(1.0, float(card["planned_seconds"])-times["mass_1_5"]-0.5), 12)
            elif cid == "05": add_steps(times["percent_95_4"], min(8.0, float(card["planned_seconds"])-times["percent_95_4"]), 12)
            elif cid == "06": add_steps(times["not_adjudicated"], min(3.0, float(card["planned_seconds"])-times["not_adjudicated"]), 8)
            elif cid == "07":
                for sec in range(math.ceil(start + times["cw_ccw"]), math.floor(end)):
                    boundaries.add(sec*FPS)
            elif cid == "08": add_steps(times["forecast_blanks"], min(4.0, float(card["planned_seconds"])-times["forecast_blanks"]), 4)
            elif cid == "11": add_steps(times["asymmetry_alone"], min(5.0, float(card["planned_seconds"])-times["asymmetry_alone"]), 10)
        result = sorted(value for value in boundaries if 0 <= value <= DURATION*FPS)
        if result[0] != 0 or result[-1] != DURATION*FPS:
            raise RuntimeError("render boundaries do not cover V12")
        return result

    def build_states(self) -> tuple[list[int], list[dict]]:
        if FRAME_DIR.exists():
            shutil.rmtree(FRAME_DIR)
        FRAME_DIR.mkdir(parents=True)
        boundaries = self.interval_boundaries()
        entries = []
        for index, (start_frame, end_frame) in enumerate(zip(boundaries, boundaries[1:])):
            if end_frame <= start_frame:
                continue
            timestamp = start_frame / FPS
            output = FRAME_DIR / f"state-{index:04d}-{start_frame:05d}.png"
            self.frame(timestamp).save(output, optimize=True)
            entries.append({"index": index, "start_frame": start_frame, "end_frame": end_frame, "frames": end_frame-start_frame, "start_seconds": timestamp, "duration_seconds": (end_frame-start_frame)/FPS, "file": str(output.relative_to(ROOT)), "sha256": sha(output)})
        lines = ["ffconcat version 1.0"]
        for item in entries:
            lines += [f"file '{(ROOT/item['file']).as_posix()}'", f"duration {item['duration_seconds']:.9f}"]
        lines.append(f"file '{(ROOT/entries[-1]['file']).as_posix()}'")
        CONCAT_PATH.write_text("\n".join(lines) + "\n")
        return boundaries, entries

    def preview(self):
        PREVIEW_DIR.mkdir(exist_ok=True)
        outputs = []
        for card in self.cards:
            start = float(card["master_start_seconds"]); planned = float(card["planned_seconds"])
            for label, fraction in (("early", 0.08), ("mid", 0.55), ("late", 0.93)):
                path = PREVIEW_DIR / f"card-{card['card_id']}-{label}.png"
                self.frame(start + planned*fraction).save(path)
                outputs.append(path)
            hidden = PREVIEW_DIR / f"card-{card['card_id']}-late-text-hidden.png"
            self.frame(start + planned*0.93, hide_text=True).save(hidden)
            outputs.append(hidden)
        print("\n".join(str(path) for path in outputs))

    def render(self):
        boundaries, entries = self.build_states()
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SRT_PATH, OUTPUT_SRT)
        shutil.copyfile(VTT_PATH, OUTPUT_VTT)
        command = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "concat", "-safe", "0", "-i", str(CONCAT_PATH),
            "-i", str(AUDIO_PATH), "-i", str(SRT_PATH),
            "-map", "0:v:0", "-map", "1:a:0", "-map", "2:s:0",
            "-vf", f"fps={FPS}", "-r", str(FPS), "-t", f"{DURATION:.6f}",
            "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-c:s", "mov_text", "-metadata:s:s:0", "language=eng",
            "-metadata:s:s:0", "title=English", "-disposition:s:0", "default",
            "-movflags", "+faststart", str(OUTPUT),
        ]
        subprocess.run(command, check=True)
        probe = json.loads(run("ffprobe", "-v", "error", "-show_entries", "format=duration,size:stream=index,codec_name,codec_type,width,height,r_frame_rate,nb_frames,sample_rate,channels:stream_tags=language,title:stream_disposition=default", "-of", "json", str(OUTPUT)).stdout)
        streams = probe["streams"]
        video = next(x for x in streams if x["codec_type"] == "video")
        subtitles = [x for x in streams if x["codec_type"] == "subtitle"]
        if (int(video["width"]), int(video["height"]), video["r_frame_rate"], int(video.get("nb_frames", 0))) != (W, H, "30/1", DURATION*FPS):
            raise RuntimeError(f"encoded geometry drift: {video}")
        if len(subtitles) != 1 or subtitles[0]["codec_name"] != "mov_text":
            raise RuntimeError(f"subtitle stream presence assertion failed: {subtitles}")
        if abs(float(probe["format"]["duration"])-DURATION) > 0.05:
            raise RuntimeError("encoded duration drift")
        manifest = {
            "status": "ENCODED_V12_CANDIDATE_WITH_EMBEDDED_SUBTITLE_STREAM_AWAITING_ENCODED_QA",
            "created_at_utc": datetime.now(timezone.utc).isoformat(), "source_hashes": EXPECTED,
            "renderer": str(Path(__file__)), "renderer_sha256": sha(Path(__file__)),
            "pillow_version": PIL.__version__, "generated_asset_usage": self.generated_asset_usage,
            "quantitative_cards_with_generated_assets": [cid for cid in ("04", "05") if self.generated_asset_usage[cid]],
            "generation_spend_ledger": str(GEN_LEDGER_PATH), "generation_spend_ledger_sha256": sha(GEN_LEDGER_PATH),
            "interval_boundary_count": len(boundaries), "render_state_count": len(entries), "raw_frames_encoded": DURATION*FPS,
            "audio_timeline": str(TIMELINE_PATH), "audio_timeline_sha256": sha(TIMELINE_PATH),
            "output": str(OUTPUT), "output_sha256": sha(OUTPUT), "output_srt": str(OUTPUT_SRT), "output_srt_sha256": sha(OUTPUT_SRT), "output_vtt": str(OUTPUT_VTT), "output_vtt_sha256": sha(OUTPUT_VTT),
            "subtitle_stream_presence_asserted": True, "subtitle_stream_codec": subtitles[0]["codec_name"], "probe": probe,
            "upload_authorized": False, "publication_authorized": False,
        }
        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
        print(json.dumps(manifest, indent=2, ensure_ascii=False))


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(); parser.add_argument("--preview", action="store_true"); parser.add_argument("--render", action="store_true")
    args = parser.parse_args(); renderer = Renderer()
    if args.preview: renderer.preview()
    if args.render: renderer.render()
    if not args.preview and not args.render: raise SystemExit("choose --preview or --render")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
