#!/usr/bin/env python3
"""Render the audio-timed spin-method conference-science overhaul.

The renderer is isolated inside the versioned canary. It reads only the v2 PCM-derived timeline and
frozen source facts, creates genuine per-frame scientific animation, and never imports repo tools.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import random
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
TIMELINE_PATH = ROOT / "audio_v2" / "timeline.json"
AUDIO_PATH = ROOT / "audio_v2" / "narration_master.wav"
OUTPUT_PATH = ROOT / "spin-method-overhaul-canary-20260808T1312K.mp4"
RECEIPT_PATH = ROOT / "build_receipt.json"
PREVIEW_PATH = ROOT / "preview-contact-sheet-v2.jpg"
QA_FRAME_DIR = ROOT / "qa_frames" / "sentence-mid-v2"

W, H, FPS = 1920, 1080, 30
BG = (8, 14, 27)
BG2 = (15, 24, 42)
PANEL = (20, 32, 52)
PANEL2 = (25, 41, 64)
WHITE = (239, 245, 250)
MUTED = (155, 176, 196)
GRID = (31, 49, 70)
CYAN = (69, 211, 230)
BLUE = (94, 146, 255)
TEAL = (72, 206, 168)
AMBER = (244, 183, 74)
CORAL = (246, 118, 108)
GREEN = (101, 211, 142)
PURPLE = (166, 126, 237)
RED = (230, 91, 94)
FONT_PATH = "/System/Library/Fonts/Avenir Next.ttc"
MONO_PATH = "/System/Library/Fonts/Menlo.ttc"

TIMELINE = json.loads(TIMELINE_PATH.read_text())
RECORDS = TIMELINE["records"]
DURATION = float(TIMELINE["master_duration_seconds"])


@lru_cache(maxsize=None)
def font(size: int, mono: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(MONO_PATH if mono else FONT_PATH, size=size)


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def ease(x: float) -> float:
    x = clamp(x)
    return x * x * (3.0 - 2.0 * x)


def seg(p: float, a: float, b: float) -> float:
    return ease((p - a) / max(1e-9, b - a))


def mix(a: tuple[int, int, int], b: tuple[int, int, int], p: float) -> tuple[int, int, int]:
    p = clamp(p)
    return (
        round(a[0] + (b[0] - a[0]) * p),
        round(a[1] + (b[1] - a[1]) * p),
        round(a[2] + (b[2] - a[2]) * p),
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_size(draw: ImageDraw.ImageDraw, value: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), value, font=fnt)
    return int(box[2] - box[0]), int(box[3] - box[1])


def center_text(
    draw: ImageDraw.ImageDraw,
    value: str,
    xy: tuple[float, float],
    size: int,
    fill: tuple[int, int, int] = WHITE,
    mono: bool = False,
    anchor: str = "mm",
    stroke: int = 0,
) -> None:
    draw.text(xy, value, font=font(size, mono), fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=BG)


def wrap_lines(draw: ImageDraw.ImageDraw, value: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = value.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else current + " " + word
        if text_size(draw, candidate, fnt)[0] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def wrapped_text(
    draw: ImageDraw.ImageDraw,
    value: str,
    box: tuple[int, int, int, int],
    size: int,
    fill: tuple[int, int, int] = WHITE,
    align: str = "center",
    mono: bool = False,
    line_gap: int = 8,
) -> None:
    fnt = font(size, mono)
    x0, y0, x1, y1 = box
    lines = wrap_lines(draw, value, fnt, x1 - x0)
    line_h = size + line_gap
    total_h = len(lines) * line_h - line_gap
    y = y0 + max(0, (y1 - y0 - total_h) // 2)
    for line in lines:
        width, _ = text_size(draw, line, fnt)
        x = x0 if align == "left" else x0 + (x1 - x0 - width) // 2
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_h


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill, outline=None, width=2) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    color: tuple[int, int, int],
    progress: float = 1.0,
    width: int = 5,
) -> None:
    progress = clamp(progress)
    sx, sy = start
    ex, ey = end
    px, py = sx + (ex - sx) * progress, sy + (ey - sy) * progress
    draw.line((sx, sy, px, py), fill=color, width=width)
    if progress > 0.92:
        angle = math.atan2(ey - sy, ex - sx)
        head = 15
        for offset in (2.55, -2.55):
            hx = px + head * math.cos(angle + offset)
            hy = py + head * math.sin(angle + offset)
            draw.line((px, py, hx, hy), fill=color, width=width)


def flow_dots(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    t: float,
    color: tuple[int, int, int],
    count: int = 5,
) -> None:
    for i in range(count):
        q = (t * 0.22 + i / count) % 1.0
        x = start[0] + (end[0] - start[0]) * q
        y = start[1] + (end[1] - start[1]) * q
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=color)


def badge(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], label: str, color=CYAN, size=28) -> None:
    rounded(draw, box, 18, mix(BG, color, 0.16), color, 2)
    center_text(draw, label, ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2 + 1), size, color)


def make_background() -> Image.Image:
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    for y in range(H):
        draw.line((0, y, W, y), fill=mix(BG, BG2, y / H))
    for x in range(0, W, 96):
        draw.line((x, 0, x, H), fill=GRID, width=1)
    for y in range(0, H, 96):
        draw.line((0, y, W, y), fill=GRID, width=1)
    rng = random.Random(31173)
    for _ in range(150):
        x, y = rng.randrange(W), rng.randrange(880)
        c = rng.choice((GRID, (43, 64, 89), (53, 77, 99)))
        r = rng.choice((1, 1, 2))
        draw.ellipse((x - r, y - r, x + r, y + r), fill=c)
    return image


BACKGROUND = make_background()


def global_chrome(draw: ImageDraw.ImageDraw, t: float, section: str) -> None:
    # Moving scan-lines keep even long scientific states alive without decorative zoom.
    for k in range(3):
        x = ((t * (32 + 7 * k) + 430 * k) % (W + 500)) - 250
        draw.line((x, 82, x + 220, 82), fill=mix(GRID, CYAN, 0.25 + 0.1 * k), width=2)
    center_text(draw, "NEBULAMIND · SPIN METHOD", (72, 45), 25, MUTED, anchor="lm")
    center_text(draw, "METHOD DESIGN · NO MEASURED VALUE", (W - 72, 45), 23, AMBER, anchor="rm")
    draw.line((70, 80, W - 70, 80), fill=GRID, width=2)

    stages = [
        ("QUESTION", {"question", "two-worlds"}),
        ("MIRROR TEST", {"mirror-climax"}),
        ("FROZEN DESIGN", {"discipline", "funnel"}),
        ("ESTIMATOR", {"equation"}),
        ("CONTROLS", {"controls"}),
        ("SCIENTIFIC GATE", {"discipline-gates", "boundary", "payoff"}),
    ]
    y = 884
    x0, x1 = 110, W - 110
    draw.line((x0, y, x1, y), fill=GRID, width=3)
    for i, (name, memberships) in enumerate(stages):
        x = x0 + (x1 - x0) * i / (len(stages) - 1)
        active = section in memberships
        color = CYAN if active else MUTED
        r = 10 if active else 6
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)
        center_text(draw, name, (x, y + 33), 19, color)


def caption(draw: ImageDraw.ImageDraw, t: float, record: dict) -> None:
    if not (record["audio_start_seconds"] <= t <= record["audio_end_seconds"]):
        return
    fade = min(seg(t - record["audio_start_seconds"], 0, 0.18), seg(record["audio_end_seconds"] - t, 0, 0.18))
    fill = mix(BG2, WHITE, fade)
    rounded(draw, (170, 940, W - 170, 1055), 24, (10, 18, 31), GRID, 2)
    wrapped_text(draw, record["text"], (205, 950, W - 205, 1045), 31, fill)


def spiral_points(cx: float, cy: float, radius: float, scale_x: float, phase: float = 0.0) -> list[tuple[float, float]]:
    points = []
    steps = 150
    for i in range(steps):
        theta = 0.18 + i / (steps - 1) * math.pi * 4.6
        r = radius * (0.08 + 0.92 * i / (steps - 1))
        x = cx + scale_x * r * math.cos(theta + phase)
        y = cy + 0.68 * r * math.sin(theta + phase)
        points.append((x, y))
    return points


def draw_spiral(draw: ImageDraw.ImageDraw, cx: float, cy: float, radius: float, scale_x: float, color=CYAN, width=8) -> None:
    draw.ellipse((cx - radius * 0.12, cy - radius * 0.12, cx + radius * 0.12, cy + radius * 0.12), fill=mix(BG, color, 0.55))
    for phase in (0.0, math.pi):
        draw.line(spiral_points(cx, cy, radius, scale_x, phase), fill=color, width=width, joint="curve")
    draw.ellipse((cx - radius, cy - radius * 0.72, cx + radius, cy + radius * 0.72), outline=mix(BG, color, 0.45), width=2)


def explanation_node(draw: ImageDraw.ImageDraw, box, title: str, subtitle: str, color, active=1.0, icon="spiral") -> None:
    edge = mix(GRID, color, active)
    rounded(draw, box, 30, PANEL, edge, 4 if active > 0.6 else 2)
    cx = (box[0] + box[2]) / 2
    if icon == "spiral":
        draw_spiral(draw, cx, box[1] + 135, 72, 1.0, edge, 5)
    else:
        rounded(draw, (int(cx - 95), box[1] + 78, int(cx + 95), box[1] + 172), 16, mix(BG, color, 0.12), edge, 3)
        badge(draw, (int(cx - 74), box[1] + 96, int(cx - 4), box[1] + 151), "CW", edge, 22)
        badge(draw, (int(cx + 8), box[1] + 96, int(cx + 78), box[1] + 151), "ACW", edge, 22)
    center_text(draw, title, (cx, box[1] + 235), 35, edge)
    wrapped_text(draw, subtitle, (box[0] + 35, box[1] + 270, box[2] - 35, box[3] - 25), 25, MUTED)


def draw_question(draw: ImageDraw.ImageDraw, sid: str, p: float, t: float) -> None:
    if sid == "s01":
        q = seg(p, 0.05, 0.9)
        draw_spiral(draw, W / 2, 420, 210, 1.0, mix(BG, CYAN, q), 10)
        center_text(draw, "GALAXY SPIN HANDEDNESS", (W / 2, 182 + 25 * (1 - q)), 70, mix(BG, WHITE, q))
        center_text(draw, "A MIRROR TEST BEFORE THE RESULT", (W / 2, 270), 38, mix(BG, AMBER, q))
        arrow(draw, (W / 2 - 330, 680), (W / 2 - 80, 680), BLUE, q, 5)
        arrow(draw, (W / 2 + 330, 680), (W / 2 + 80, 680), PURPLE, q, 5)
        center_text(draw, "TWO EXPLANATIONS", (W / 2, 730), 29, MUTED)
        center_text(draw, "ONE DISCRIMINATING INTERVENTION", (W / 2, 775), 29, CYAN)
    else:
        explanation_node(draw, (130, 180, 730, 680), "IMAGE-LINKED", "a pattern carried by the pixels", BLUE, 0.55, "spiral")
        explanation_node(draw, (1190, 180, 1790, 680), "LABELING PROCESS", "an effect introduced while labels are assigned", PURPLE, 0.55, "labels")
        arrow(draw, (730, 430), (850, 430), BLUE, seg(p, 0.15, 0.55))
        arrow(draw, (1190, 430), (1070, 430), PURPLE, seg(p, 0.15, 0.55))
        rounded(draw, (820, 325, 1100, 540), 30, PANEL2, AMBER, 3)
        center_text(draw, "APPARENT", (960, 380), 29, MUTED)
        center_text(draw, "COUNT", (960, 430), 45, WHITE)
        center_text(draw, "?", (960, 495), 68, AMBER)
        wrapped_text(
            draw,
            "Can the image-linked and labeling-process explanations be separated?",
            (340, 710, 1580, 830),
            41,
            WHITE,
        )


def draw_two_worlds(draw: ImageDraw.ImageDraw, sid: str, p: float, t: float) -> None:
    left_active = 0.35 if sid == "s05" else 1.0
    right_active = 0.35 if sid == "s04" else 1.0
    explanation_node(draw, (120, 175, 730, 685), "IMAGE-LINKED", "pattern belongs to the images", BLUE, left_active, "spiral")
    explanation_node(draw, (1190, 175, 1800, 685), "LABELING PROCESS", "effect enters during labeling", PURPLE, right_active, "labels")
    rounded(draw, (820, 325, 1100, 535), 26, PANEL2, AMBER, 3)
    center_text(draw, "SAME", (960, 375), 27, MUTED)
    center_text(draw, "APPARENT", (960, 420), 30, WHITE)
    center_text(draw, "IMBALANCE", (960, 468), 32, AMBER)
    center_text(draw, "?", (960, 515), 46, AMBER)
    arrow(draw, (730, 430), (820, 430), BLUE, seg(p, 0.05, 0.6))
    arrow(draw, (1190, 430), (1100, 430), PURPLE, seg(p, 0.05, 0.6))
    flow_dots(draw, (710, 430), (820, 430), t, BLUE, 3)
    flow_dots(draw, (1210, 430), (1100, 430), t, PURPLE, 3)
    label = "TWO EXPLANATIONS · ONE OBSERVABLE" if sid == "s03" else ("WORLD 1" if sid == "s04" else "WORLD 2")
    badge(draw, (650, 745, 1270, 815), label, CYAN if sid == "s03" else (BLUE if sid == "s04" else PURPLE), 28)


def mirror_flip_progress(sid: str, p: float) -> float:
    if sid == "s06":
        return 0.42 * ease(p)
    if sid == "s07":
        return 0.42 + 0.58 * ease(p)
    return 1.0


def draw_mirror(draw: ImageDraw.ImageDraw, sid: str, p: float, t: float) -> None:
    center_text(draw, "ONE INTERVENTION · TWO PREDICTIONS", (W / 2, 135), 37, WHITE)
    center_text(draw, "CONCEPTUAL — illustration, not data", (W / 2, 180), 24, AMBER)
    flip = mirror_flip_progress(sid, p)
    sx = math.cos(math.pi * flip)
    plane_glow = 0.5 + 0.5 * math.sin(t * 5.0)
    draw.line((960, 215, 960, 670), fill=mix(GRID, CYAN, plane_glow), width=5)
    for yy in range(235, 660, 42):
        draw.line((945, yy, 975, yy + 16), fill=mix(GRID, CYAN, 0.65), width=3)
    draw_spiral(draw, 960, 420, 225, sx, CYAN, 10)
    before = clamp(1.0 - seg(flip, 0.35, 0.6))
    after = seg(flip, 0.45, 0.75)
    center_text(draw, "appears CLOCKWISE · CW", (960, 700), 35, mix(BG, BLUE, before))
    center_text(draw, "appears ANTICLOCKWISE · ACW", (960, 700), 35, mix(BG, PURPLE, after))

    # The peak is built progressively, not shown all at once.
    left_reveal = 1.0 if sid in {"s08", "s09", "s10"} else 0.0
    right_reveal = 1.0 if sid in {"s09", "s10"} else 0.0
    if sid == "s08":
        left_reveal = seg(p, 0.05, 0.7)
    if sid == "s09":
        right_reveal = seg(p, 0.05, 0.7)
    if sid == "s10":
        left_reveal = right_reveal = 1.0
    if left_reveal:
        rounded(draw, (110, 270, 565, 575), 28, PANEL, mix(GRID, BLUE, left_reveal), 4)
        center_text(draw, "IMAGE-LINKED", (338, 325), 31, BLUE)
        center_text(draw, "pixels flip", (338, 390), 28, MUTED)
        arrow(draw, (338, 425), (338, 485), BLUE, left_reveal, 5)
        center_text(draw, "MUST INVERT", (338, 525), 39, mix(BG, BLUE, left_reveal))
        arrow(draw, (565, 430), (735, 430), BLUE, left_reveal, 4)
    if right_reveal:
        rounded(draw, (1355, 270, 1810, 575), 28, PANEL, mix(GRID, PURPLE, right_reveal), 4)
        center_text(draw, "LABELING PROCESS", (1582, 325), 30, PURPLE)
        center_text(draw, "labels assigned", (1582, 390), 28, MUTED)
        arrow(draw, (1582, 425), (1582, 485), PURPLE, right_reveal, 5)
        center_text(draw, "NEED NOT INVERT", (1582, 525), 35, mix(BG, PURPLE, right_reveal))
        arrow(draw, (1355, 430), (1185, 430), PURPLE, right_reveal, 4)
    if sid == "s10":
        q = 0.82 + 0.18 * math.sin(t * 4.0)
        badge(draw, (615, 760, 1305, 835), "MIRROR DISCRIMINANT", mix(CYAN, WHITE, q), 37)
        arrow(draw, (338, 575), (720, 775), BLUE, seg(p, 0.0, 0.6), 4)
        arrow(draw, (1582, 575), (1200, 775), PURPLE, seg(p, 0.0, 0.6), 4)


def draw_discipline_freeze(draw: ImageDraw.ImageDraw, p: float, t: float) -> None:
    center_text(draw, "RULES FIXED BEFORE ANY NUMBER", (W / 2, 150), 48, WHITE)
    items = [("MIRROR LOGIC", BLUE), ("EVERY CUT", CYAN), ("0.60 / 0.80", TEAL), ("SAME-OBJECT PAIRS", PURPLE)]
    centers = [280, 730, 1190, 1640]
    for i, ((label, color), x) in enumerate(zip(items, centers)):
        q = seg(p, i * 0.15, i * 0.15 + 0.35)
        y = 420 - 45 * (1 - q)
        rounded(draw, (x - 175, int(y - 115), x + 175, int(y + 115)), 28, PANEL, mix(GRID, color, q), 4)
        center_text(draw, label, (x, y), 31, mix(BG, color, q))
        if q > 0.72:
            draw.arc((x - 32, y + 35, x + 32, y + 100), 180, 360, fill=color, width=7)
            rounded(draw, (x - 43, int(y + 65), x + 43, int(y + 132)), 10, mix(BG, color, 0.25), color, 4)
    bracket = seg(p, 0.6, 1.0)
    draw.line((130, 700, 130 + (1660 * bracket), 700), fill=AMBER, width=6)
    draw.line((130, 700, 130, 650), fill=AMBER, width=6)
    if bracket > 0.95:
        draw.line((1790, 700, 1790, 650), fill=AMBER, width=6)
    center_text(draw, "SELF-IMPOSED BEFORE CALCULATION", (W / 2, 765), 31, mix(BG, AMBER, bracket))


def funnel_branch(draw: ImageDraw.ImageDraw, y: int, title: str, count: str, detail: str, color, reveal: float, t: float) -> None:
    arrow(draw, (620, 430), (800, y), color, reveal, 5)
    if reveal > 0.25:
        rounded(draw, (800, y - 72, 1740, y + 72), 24, PANEL, mix(GRID, color, reveal), 3)
        center_text(draw, title, (850, y - 24), 29, color, anchor="lm")
        center_text(draw, count, (1370, y - 14), 41, WHITE)
        center_text(draw, detail, (850, y + 30), 23, MUTED, anchor="lm")
        flow_dots(draw, (640, 430), (790, y), t, color, 4)


def draw_funnel(draw: ImageDraw.ImageDraw, sid: str, p: float, t: float) -> None:
    center_text(draw, "ONE FROZEN SOURCE · THREE PARALLEL READOUTS", (W / 2, 145), 43, WHITE)
    rounded(draw, (140, 275, 620, 590), 34, PANEL2, CYAN, 4)
    center_text(draw, "GALAXY ZOO 1", (380, 340), 37, CYAN)
    center_text(draw, "DATA RELEASE", (380, 390), 29, MUTED)
    center_text(draw, "667,944", (380, 480), 65, WHITE)
    center_text(draw, "source rows", (380, 535), 27, MUTED)
    for i in range(14):
        q = (t * 0.18 + i / 14) % 1
        x = 160 + 430 * q
        y = 250 + 18 * math.sin(i * 1.9 + t)
        draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=CYAN)
    if sid == "s12":
        badge(draw, (815, 350, 1660, 505), "FROZEN SAMPLE ACCOUNTING", CYAN, 40)
        center_text(draw, "sample size attached to its source stage", (1238, 560), 29, MUTED)
    else:
        funnel_branch(draw, 285, "SPIRAL FLAG", "190,225 rows", "161,172 decisive · 29,053 ties", BLUE, seg(p, 0.00, 0.45), t)
        funnel_branch(draw, 465, "DOMINANCE ≥ 0.60", "51,157 rows", "decisively labelled", TEAL, seg(p, 0.20, 0.68), t)
        funnel_branch(draw, 645, "DOMINANCE ≥ 0.80", "30,412 rows", "decisively labelled", PURPLE, seg(p, 0.42, 0.90), t)
        badge(draw, (840, 748, 1700, 818), "PARALLEL — NOT SEQUENTIAL", AMBER, 28)
    center_text(draw, "Galaxy Zoo 1 data release · Table 2", (W - 95, 844), 22, MUTED, anchor="rm")


def draw_equation(draw: ImageDraw.ImageDraw, sid: str, p: float, t: float) -> None:
    center_text(draw, "PREDECLARED ASYMMETRY ESTIMATOR", (W / 2, 145), 43, WHITE)
    rounded(draw, (210, 245, 1710, 690), 35, PANEL, GRID, 3)
    if sid == "s14":
        q1 = seg(p, 0.05, 0.6)
        q2 = seg(p, 0.30, 0.88)
        badge(draw, (355, 380, 775, 535), "N_CW", BLUE, 63)
        badge(draw, (1145, 380, 1565, 535), "N_ACW", PURPLE, 63)
        center_text(draw, "clockwise labels", (565, 590), 27, mix(BG, MUTED, q1))
        center_text(draw, "anticlockwise labels", (1355, 590), 27, mix(BG, MUTED, q2))
        arrow(draw, (780, 457), (915, 457), BLUE, q1, 5)
        arrow(draw, (1140, 457), (1005, 457), PURPLE, q2, 5)
        center_text(draw, "ONE READOUT", (960, 457), 30, WHITE)
    else:
        numerator = seg(p, 0.02, 0.40) if sid == "s15" else 1.0
        denominator = seg(p, 0.20, 0.62) if sid == "s15" else 1.0
        a_reveal = seg(p, 0.55, 0.92) if sid == "s15" else 1.0
        center_text(draw, "A", (500, 465), 84, mix(BG, WHITE, a_reveal), mono=True)
        center_text(draw, "=", (620, 465), 70, mix(BG, WHITE, a_reveal), mono=True)
        center_text(draw, "N_CW − N_ACW", (1100, 370), 58, mix(BG, CYAN, numerator), mono=True)
        draw.line((815, 455, 1385, 455), fill=mix(BG, WHITE, denominator), width=6)
        center_text(draw, "N_CW + N_ACW", (1100, 535), 58, mix(BG, TEAL, denominator), mono=True)
        center_text(draw, "numerator: difference", (1100, 300), 25, mix(BG, MUTED, numerator))
        center_text(draw, "denominator: total", (1100, 605), 25, mix(BG, MUTED, denominator))
    if sid == "s16":
        labels = [("A < 0 · more ACW", BLUE), ("A = 0 · equal", MUTED), ("A > 0 · more CW", PURPLE)]
        for i, (label, color) in enumerate(labels):
            x0 = 245 + i * 485
            rounded(draw, (x0, 735, x0 + 440, 810), 16, PANEL2, GRID, 2)
            center_text(draw, label, (x0 + 220, 773), 27, mix(MUTED, color, 0.35), mono=True)
        lock = 0.75 + 0.25 * math.sin(t * 5)
        badge(draw, (690, 610, 1230, 690), "VALUE WITHHELD", mix(AMBER, WHITE, lock), 34)
        center_text(draw, "no sign selected", (W / 2, 842), 24, MUTED)


def draw_controls(draw: ImageDraw.ImageDraw, sid: str, p: float, t: float) -> None:
    center_text(draw, "PREDECLARED BIAS-CONTROL MATRIX", (W / 2, 140), 44, WHITE)
    x0, x1, x2 = 130, 700, 1770
    y0 = 245
    rounded(draw, (x0, y0, x2, 790), 28, PANEL, GRID, 3)
    draw.rectangle((x0, y0, x2, y0 + 82), fill=PANEL2)
    center_text(draw, "CONTROL", (x0 + 35, y0 + 41), 27, CYAN, anchor="lm")
    center_text(draw, "FAILURE MODE TESTED", (x1 + 35, y0 + 41), 27, AMBER, anchor="lm")
    rows = [
        ("HORIZONTAL MIRROR", "label response does not follow image inversion", BLUE),
        ("0.60 / 0.80 THRESHOLDS", "classification depends on one decisiveness cut", TEAL),
        ("PAIRED SAME OBJECT", "aggregate change comes from sample composition", PURPLE),
    ]
    for i, (control, test, color) in enumerate(rows):
        ry0 = y0 + 82 + i * 148
        q = seg(p, i * 0.09, i * 0.09 + 0.28) if sid == "s17" else 1.0
        draw.line((x0, ry0, x2, ry0), fill=GRID, width=2)
        center_text(draw, control, (x0 + 35, ry0 + 74), 30, mix(BG, color, q), anchor="lm")
        arrow(draw, (x1 - 80, ry0 + 74), (x1 + 15, ry0 + 74), color, q, 4)
        center_text(draw, test, (x1 + 55, ry0 + 74), 28, mix(BG, WHITE, q), anchor="lm")
        if sid == "s18":
            pulse_x = x1 + 20 + ((t * 110 + i * 220) % (x2 - x1 - 80))
            draw.ellipse((pulse_x - 5, ry0 + 69, pulse_x + 5, ry0 + 79), fill=color)
    if sid == "s18":
        q = seg(p, 0.35, 0.85)
        badge(draw, (610, 815, 1310, 875), "DESIGN ONLY · NO OUTCOMES", mix(AMBER, WHITE, 0.2 * q), 29)


def draw_discipline_gates(draw: ImageDraw.ImageDraw, sid: str, p: float, t: float) -> None:
    if sid == "s19":
        center_text(draw, "WE TIED OUR OWN HANDS", (W / 2, 150), 52, WHITE)
        center_text(draw, "so later choices cannot shape the answer", (W / 2, 205), 31, MUTED)
        cx, cy = W / 2, 505
        radius = 240
        for i, (label, color) in enumerate((("MIRROR", BLUE), ("CUTS", CYAN), ("THRESHOLDS", TEAL), ("PAIRS", PURPLE))):
            angle = -math.pi / 2 + i * math.pi / 2
            x, y = cx + radius * math.cos(angle), cy + radius * math.sin(angle)
            q = seg(p, i * 0.12, i * 0.12 + 0.35)
            rounded(draw, (int(x - 115), int(y - 48), int(x + 115), int(y + 48)), 18, PANEL, mix(GRID, color, q), 3)
            center_text(draw, label, (x, y), 27, mix(BG, color, q))
            arrow(draw, (x, y), (cx + 10 * math.cos(angle), cy + 10 * math.sin(angle)), color, q, 4)
        lock_q = seg(p, 0.55, 1.0)
        draw.arc((cx - 70, cy - 135, cx + 70, cy + 5), 180, 360, fill=mix(BG, AMBER, lock_q), width=12)
        rounded(draw, (int(cx - 95), int(cy - 45), int(cx + 95), int(cy + 125)), 22, mix(BG, AMBER, 0.12 * lock_q), mix(BG, AMBER, lock_q), 7)
        center_text(draw, "FIXED", (cx, cy + 35), 35, mix(BG, AMBER, lock_q))
        for x in (240, 1680):
            center_text(draw, "LATER CHOICE", (x, 360), 24, CORAL)
            arrow(draw, (x, 395), (cx - 120 if x < cx else cx + 120, cy), CORAL, 1.0, 4)
            bx = 640 if x < cx else 1280
            draw.line((bx - 25, 455, bx + 25, 505), fill=RED, width=8)
            draw.line((bx + 25, 455, bx - 25, 505), fill=RED, width=8)
    else:
        center_text(draw, "THE SAME STANDARD SETS THE SCIENTIFIC GATES", (W / 2, 135), 42, WHITE)
        center_text(draw, "requirements we imposed before calculation", (W / 2, 185), 28, MUTED)
        nodes = [
            ("FROZEN\nMETHOD", GREEN),
            ("NEXT GATE\nINDEPENDENT VERDICT", AMBER),
            ("EVIDENCE", MUTED),
            ("RECEIPT", MUTED),
            ("REFEREE", MUTED),
            ("ANSWER", CYAN),
        ]
        xs = [165, 490, 835, 1125, 1405, 1710]
        y = 470
        for i, ((label, color), x) in enumerate(zip(nodes, xs)):
            q = (0.70 + 0.30 * seg(p, i * 0.08, i * 0.08 + 0.35)) if i < 5 else 0.16 * seg(p, 0.55, 0.95)
            if i:
                arrow(draw, (xs[i - 1] + 115, y), (x - 115, y), color, q, 4)
                flow_dots(draw, (xs[i - 1] + 120, y), (x - 120, y), t, color, 2)
            rounded(draw, (x - 120, y - 90, x + 120, y + 90), 24, PANEL, mix(GRID, color, q), 4)
            wrapped_text(draw, label, (x - 105, y - 70, x + 105, y + 70), 27, mix(BG, color, q))
        # The pulse cannot enter the answer field yet.
        lock_x = 1580
        draw.line((lock_x, 345, lock_x, 595), fill=AMBER, width=7)
        center_text(draw, "STANDARD HOLDS HERE", (lock_x, 625), 22, AMBER)
        badge(draw, (410, 720, 1510, 790), "STORED-DIRECTION FRAME ALSO UNRESOLVED", AMBER, 28)
        center_text(draw, "consequences of a standard set in advance", (W / 2, 840), 25, MUTED)


def draw_boundary(draw: ImageDraw.ImageDraw, p: float, t: float) -> None:
    center_text(draw, "SCIENTIFIC BOUNDARY", (W / 2, 135), 47, WHITE)
    cols = [
        (150, 590, "KNOWN NOW", GREEN, ["667,944-row source", "symbolic estimator", "mirror discriminant", "control design"]),
        (655, 1265, "NOT REPORTABLE", CORAL, ["measured value", "result direction", "interpretation"]),
        (1330, 1770, "NEXT SCIENTIFIC GATE", AMBER, ["independent verdict", "stored-direction frame", "then evidence checks"]),
    ]
    for i, (x0, x1, title, color, items) in enumerate(cols):
        q = seg(p, i * 0.2, i * 0.2 + 0.55)
        rounded(draw, (x0, 235, x1, 800), 28, PANEL, mix(GRID, color, q), 3)
        center_text(draw, title, ((x0 + x1) / 2, 295), 29, mix(BG, color, q))
        for j, item in enumerate(items):
            yy = 390 + j * 95
            draw.ellipse((x0 + 45, yy - 8, x0 + 61, yy + 8), fill=mix(BG, color, q))
            center_text(draw, item, (x0 + 85, yy), 27, mix(BG, WHITE, q), anchor="lm")
    q = 0.6 + 0.4 * math.sin(t * 4)
    center_text(draw, "VALUE · DIRECTION · INTERPRETATION", (960, 842), 25, mix(MUTED, CORAL, q))


def draw_payoff(draw: ImageDraw.ImageDraw, sid: str, p: float, t: float) -> None:
    question_q = seg(p, 0.0, 0.5) if sid == "s22" else 1.0
    center_text(draw, "IMAGES OR LABELING PROCESS?", (W / 2, 145), 53, mix(BG, WHITE, question_q))
    left_color = BLUE
    right_color = PURPLE
    explanation_node(draw, (130, 245, 650, 670), "IMAGES", "image-linked pattern", left_color, 0.85, "spiral")
    explanation_node(draw, (1270, 245, 1790, 670), "LABELING PROCESS", "effect introduced with labels", right_color, 0.85, "labels")
    flip = 1.0 if sid != "s22" else ease(p)
    sx = math.cos(math.pi * flip)
    draw.line((960, 265, 960, 650), fill=CYAN, width=4)
    draw_spiral(draw, 960, 430, 170, sx, CYAN, 8)
    arrow(draw, (650, 455), (775, 455), left_color, seg(p, 0.15, 0.7) if sid == "s23" else 1.0, 4)
    arrow(draw, (1270, 455), (1145, 455), right_color, seg(p, 0.15, 0.7) if sid == "s23" else 1.0, 4)
    if sid in {"s23", "s24"}:
        badge(draw, (660, 710, 1260, 785), "MIRROR DISCRIMINANT", CYAN, 35)
        center_text(draw, "different mirror predictions", (960, 825), 28, MUTED)
    if sid == "s24":
        q = seg(p, 0.1, 0.75)
        rounded(draw, (450, 90, 1470, 210), 24, mix(BG, CYAN, 0.08), mix(GRID, CYAN, q), 4)
        center_text(draw, "THE MIRROR TELLS THE EXPLANATIONS APART", (960, 150), 35, mix(BG, CYAN, q))
        center_text(draw, "gate-cleared answer not yet reportable", (960, 860), 22, AMBER)


def active_record(t: float) -> tuple[dict, float]:
    record = RECORDS[0]
    index = 0
    for i, item in enumerate(RECORDS):
        if t >= item["audio_start_seconds"]:
            record = item
            index = i
        else:
            break
    start = record["audio_start_seconds"]
    next_start = RECORDS[index + 1]["audio_start_seconds"] if index + 1 < len(RECORDS) else DURATION
    return record, clamp((t - start) / max(0.001, next_start - start))


def draw_frame(t: float) -> Image.Image:
    image = BACKGROUND.copy()
    draw = ImageDraw.Draw(image)
    record, p = active_record(t)
    sid, section = record["id"], record["section"]
    global_chrome(draw, t, section)
    if section == "question":
        draw_question(draw, sid, p, t)
    elif section == "two-worlds":
        draw_two_worlds(draw, sid, p, t)
    elif section == "mirror-climax":
        draw_mirror(draw, sid, p, t)
    elif section == "discipline":
        draw_discipline_freeze(draw, p, t)
    elif section == "funnel":
        draw_funnel(draw, sid, p, t)
    elif section == "equation":
        draw_equation(draw, sid, p, t)
    elif section == "controls":
        draw_controls(draw, sid, p, t)
    elif section == "discipline-gates":
        draw_discipline_gates(draw, sid, p, t)
    elif section == "boundary":
        draw_boundary(draw, p, t)
    elif section == "payoff":
        draw_payoff(draw, sid, p, t)
    caption(draw, t, record)
    return image


def midpoint_times() -> list[tuple[str, float]]:
    return [(r["id"], (r["audio_start_seconds"] + r["audio_end_seconds"]) / 2) for r in RECORDS]


def validate_caption_layout() -> None:
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    caption_font = font(31)
    offenders = []
    for record in RECORDS:
        lines = wrap_lines(draw, record["text"], caption_font, W - 410)
        if len(lines) > 2:
            offenders.append({"id": record["id"], "lines": len(lines), "text": record["text"]})
    if offenders:
        raise RuntimeError(f"caption layout exceeds two lines: {offenders}")


def make_contact_sheet(images: list[tuple[str, float, Image.Image]], output: Path) -> None:
    cols = 4
    thumb_w, thumb_h = 480, 270
    label_h = 38
    rows = math.ceil(len(images) / cols)
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), (5, 8, 14))
    draw = ImageDraw.Draw(sheet)
    for i, (label, t, image) in enumerate(images):
        x = (i % cols) * thumb_w
        y = (i // cols) * (thumb_h + label_h)
        thumb = ImageOps.fit(image, (thumb_w, thumb_h), method=Image.Resampling.LANCZOS)
        sheet.paste(thumb, (x, y))
        center_text(draw, f"{label} · {t:06.2f}s", (x + thumb_w / 2, y + thumb_h + label_h / 2), 20, WHITE)
    sheet.save(output, quality=92, subsampling=0)


def preview() -> None:
    QA_FRAME_DIR.mkdir(parents=True, exist_ok=True)
    frames = []
    for sid, t in midpoint_times():
        image = draw_frame(t)
        image.save(QA_FRAME_DIR / f"{sid}-{t:07.3f}.png")
        frames.append((sid, t, image))
    # Add a five-position real flip sequence to the preview evidence.
    mirror = next(r for r in RECORDS if r["id"] == "s07")
    for i, q in enumerate((0.05, 0.25, 0.50, 0.75, 0.95)):
        t = mirror["audio_start_seconds"] + (mirror["audio_end_seconds"] - mirror["audio_start_seconds"]) * q
        image = draw_frame(t)
        label = f"mirror-{i+1}"
        image.save(QA_FRAME_DIR / f"{label}-{t:07.3f}.png")
        frames.append((label, t, image))
    make_contact_sheet(frames, PREVIEW_PATH)
    print(PREVIEW_PATH)


def render() -> None:
    frame_count = math.ceil(DURATION * FPS)
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        f"{W}x{H}",
        "-r",
        str(FPS),
        "-i",
        "pipe:0",
        "-i",
        str(AUDIO_PATH),
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "18",
        "-pix_fmt",
        "yuv420p",
        "-r",
        str(FPS),
        "-g",
        "60",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-ar",
        "48000",
        "-movflags",
        "+faststart",
        "-shortest",
        str(OUTPUT_PATH),
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert process.stdin is not None
    try:
        for frame_index in range(frame_count):
            image = draw_frame(frame_index / FPS)
            process.stdin.write(image.tobytes())
            if frame_index % 300 == 0:
                print(f"frame {frame_index}/{frame_count}", flush=True)
        process.stdin.close()
        return_code = process.wait()
    except Exception:
        process.kill()
        raise
    if return_code != 0:
        raise RuntimeError(f"ffmpeg exited {return_code}")

    probe = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size:stream=index,codec_name,codec_type,width,height,r_frame_rate,sample_rate,channels",
            "-of",
            "json",
            str(OUTPUT_PATH),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    receipt = {
        "candidate": ROOT.name,
        "revision": "v2-hwao-narrative-correction",
        "renderer": str(Path(__file__).name),
        "renderer_sha256": sha256(Path(__file__)),
        "narration_script": "narration_script_v2.json",
        "narration_script_sha256": sha256(ROOT / "narration_script_v2.json"),
        "timeline": str(TIMELINE_PATH.relative_to(ROOT)),
        "timeline_sha256": sha256(TIMELINE_PATH),
        "audio_master": str(AUDIO_PATH.relative_to(ROOT)),
        "audio_master_sha256": sha256(AUDIO_PATH),
        "output": str(OUTPUT_PATH.relative_to(ROOT)),
        "output_sha256": sha256(OUTPUT_PATH),
        "frame_count": frame_count,
        "fps": FPS,
        "resolution": [W, H],
        "duration_from_audio_seconds": DURATION,
        "word_count": TIMELINE["word_count"],
        "delivered_wpm": TIMELINE["delivered_wpm"],
        "audio_visual_start_max_delta_seconds": TIMELINE["max_abs_audio_visual_start_delta_seconds"],
        "music": False,
        "python": sys.version,
        "platform": platform.platform(),
        "pillow": Image.__version__,
        "ffprobe": json.loads(probe.stdout),
        "status": "PENDING_SEXTET_POST_ENCODED_REVIEW",
    }
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2) + "\n")
    print(OUTPUT_PATH)
    print(receipt["output_sha256"])


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preview", action="store_true")
    group.add_argument("--render", action="store_true")
    args = parser.parse_args()
    validate_caption_layout()
    if args.preview:
        preview()
    else:
        render()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
