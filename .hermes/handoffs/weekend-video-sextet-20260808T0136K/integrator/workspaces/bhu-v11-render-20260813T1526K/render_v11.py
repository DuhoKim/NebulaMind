#!/usr/bin/env python3
"""Render one exact-source V11 BHU candidate with measured reveal timing."""
from __future__ import annotations

import functools
import hashlib
import json
import math
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import PIL
from PIL import Image, ImageDraw, ImageFont

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
ROOT = Path(__file__).resolve().parent
STORY_PATH = SOURCE / "STORYBOARD_DRAFT_V11.json"
NARRATION_PATH = SOURCE / "NARRATION_DRAFT_V11.md"
TIMELINE_PATH = ROOT / "audio" / "timeline.json"
AUDIO_PATH = ROOT / "audio" / "narration_master.wav"
OUTPUT = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v11-local-20260813T1526K.mp4")
EXPECTED = {
    "STORYBOARD_DRAFT_V11.json": "b0ec6a53061ccea4196df3036bd0ad59e34ef50814b92dd3ec16cf0e4794f7c4",
    "NARRATION_DRAFT_V11.md": "027a6e17fcb3c7d3708177b8fa30078735c11cc4157f6b44edfacceef7bb8535",
}
W, H, FPS = 1920, 1080, 30
BG = (9, 14, 24)
PANEL = (18, 29, 47)
PANEL2 = (25, 40, 62)
GRID = (54, 73, 99)
WHITE = (237, 242, 248)
MUTED = (154, 168, 188)
BLUE = (118, 182, 255)
AMBER = (240, 179, 107)
RED = (217, 123, 123)
GREEN = (121, 198, 163)
CYAN = (89, 213, 220)
PURPLE = (171, 135, 231)
FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"
SERIF_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
MONO_PATH = "/System/Library/Fonts/Menlo.ttc"
FRAME_DIR = ROOT / "render_states"
CONCAT_PATH = ROOT / "render_states.ffconcat"
MANIFEST_PATH = ROOT / "render_manifest.json"
CREW_TERMS = ("duho", "lana", "goru", "kun", "hwao", "yui", "tori", "fable")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@functools.lru_cache(maxsize=None)
def font(size: int, bold: bool = False, serif: bool = False, mono: bool = False):
    path = SERIF_PATH if serif else MONO_PATH if mono else FONT_PATH
    index = 1 if bold and path == FONT_PATH else 0
    return ImageFont.truetype(path, size, index=index)


def rounded(draw, box, radius=18, fill=PANEL, outline=GRID, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def wrap(draw, text, box, size, color=WHITE, bold=False, align="center", max_lines=None, serif=False, mono=False):
    face = font(size, bold, serif, mono)
    paragraphs = text.split("\n")
    lines: list[str] = []
    width = box[2] - box[0]
    for paragraph in paragraphs:
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = ""
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
    if max_lines is not None and len(lines) > max_lines:
        raise RuntimeError(f"text exceeds {max_lines} lines at {size}px: {text}")
    step = size + 8
    total = max(0, len(lines) * step - 8)
    y = box[1] + max(0, (box[3] - box[1] - total) / 2)
    for line in lines:
        line_width = draw.textlength(line, font=face)
        if align == "left":
            x = box[0]
        elif align == "right":
            x = box[2] - line_width
        else:
            x = box[0] + (width - line_width) / 2
        draw.text((x, y), line, font=face, fill=color)
        y += step
    return len(lines)


def center(draw, text, xy, size, color=WHITE, bold=False, serif=False, mono=False):
    face = font(size, bold, serif, mono)
    box = draw.textbbox((0, 0), text, font=face)
    draw.text((xy[0] - (box[2] - box[0]) / 2, xy[1] - (box[3] - box[1]) / 2), text, font=face, fill=color)


def arrow(draw, start, end, color=CYAN, width=4, head=True):
    draw.line((*start, *end), fill=color, width=width)
    if head:
        angle = math.atan2(end[1] - start[1], end[0] - start[0])
        length = 16
        for offset in (2.55, -2.55):
            draw.line((end[0], end[1], end[0] + length * math.cos(angle + offset), end[1] + length * math.sin(angle + offset)), fill=color, width=width)


def badge(draw, box, text, color, size=24, max_lines=2):
    fill = tuple(round(BG[i] * 0.84 + color[i] * 0.16) for i in range(3))
    rounded(draw, box, 15, fill, color, 2)
    wrap(draw, text, (box[0] + 18, box[1] + 8, box[2] - 18, box[3] - 8), size, color, True, max_lines=max_lines)


def galaxy(draw, x, y, color, flip=1, scale=1.0):
    for index in range(180):
        theta = index * 0.31
        radius = index * 0.48 * scale
        xx = x + flip * radius * math.cos(theta)
        yy = y + 0.48 * radius * math.sin(theta)
        draw.ellipse((xx - 2, yy - 2, xx + 2, yy + 2), fill=color)
    draw.ellipse((x - 8, y - 8, x + 8, y + 8), fill=WHITE)


def mass_axis(draw, y=650, show_unit=True):
    x0, x1 = 260, 1660
    low, high = 1.4, 2.2
    draw.line((x0, y, x1, y), fill=WHITE, width=4)
    def position(value: float) -> float:
        return x0 + (value - low) / (high - low) * (x1 - x0)
    for value in (1.4, 1.6, 1.8, 2.0, 2.2):
        x = position(value)
        draw.line((x, y - 12, x, y + 12), fill=MUTED, width=3)
        center(draw, f"{value:.1f}", (x, y + 46), 24, MUTED, mono=True)
    label = "NEUTRON-STAR MASS (M☉)" if show_unit else "NEUTRON-STAR MASS"
    center(draw, label, ((x0 + x1) / 2, y + 88), 25, MUTED, True, serif=show_unit)
    return position


def reveal_times(card: dict) -> dict[str, float]:
    return {item["name"]: float(item["card_seconds"]) for item in card["reveals"]}


def visible(times: dict[str, float], name: str, card_t: float) -> bool:
    return card_t + 1e-9 >= times[name]


def card01(draw, card_t, times):
    galaxy(draw, 280, 520, BLUE, 1, 0.52)
    badge(draw, (80, 275, 630, 395), "A PERSONAL SIDE-QUESTION · NOT PART OF THE LAB'S RESEARCH PROGRAMME", BLUE, 23, 3)
    if visible(times, "primary_sources", card_t):
        rounded(draw, (700, 315, 1140, 520), 24, PANEL2, CYAN, 4)
        badge(draw, (750, 345, 1090, 425), "PRIMARY SOURCES", CYAN, 26)
        wrap(draw, "WE READ THE PRIMARY SOURCES", (750, 435, 1090, 495), 23, WHITE, True, max_lines=2)
    if visible(times, "number_we_can_check", card_t):
        arrow(draw, (1145, 380), (1310, 315), BLUE)
        rounded(draw, (1300, 255, 1815, 445), 22, PANEL, BLUE, 4)
        wrap(draw, "A NUMBER WE CAN CHECK", (1350, 300, 1765, 400), 31, BLUE, True, max_lines=2)
    if visible(times, "galaxy_spin_limits", card_t):
        arrow(draw, (1145, 470), (1290, 620), AMBER)
        rounded(draw, (1230, 500, 1840, 800), 22, PANEL, AMBER, 4)
        wrap(draw, "GALAXY SPIN", (1300, 525, 1770, 580), 28, AMBER, True, max_lines=1)
        wrap(draw, "THE SOURCES GIVE NO EXPECTED SIZE FOR THE EFFECT", (1280, 590, 1790, 680), 23, WHITE, True, max_lines=3)
        badge(draw, (1310, 700, 1760, 770), "NOT IDENTIFYING BY ITSELF", RED, 22)
    if visible(times, "route_verdict", card_t):
        text = "ROUTE CLOSED"
        if visible(times, "true_false_boundary", card_t):
            text = "ROUTE CLOSED · IDEA NOT DECLARED TRUE OR FALSE"
        badge(draw, (500, 790, 1420, 850), text, RED, 23)


def card02(draw, card_t, times):
    badge(draw, (90, 290, 420, 365), "ONE LABEL", BLUE, 27)
    rounded(draw, (90, 390, 420, 500), 20, PANEL2, BLUE, 3)
    wrap(draw, "BLACK-HOLE UNIVERSE", (120, 415, 390, 475), 25, BLUE, True, max_lines=2)
    if visible(times, "bhu", card_t):
        badge(draw, (145, 515, 365, 580), "BHU", CYAN, 29)
    specs = [
        ("proposal_1", (540, 245, 910, 395), "CLOSED UNIVERSE\nINSIDE A BLACK HOLE", BLUE),
        ("proposal_2", (1010, 245, 1380, 395), "COLLAPSE\nBOUNCES", AMBER),
        ("proposal_3", (1450, 245, 1820, 395), "INHERITS\nPARENT'S SPIN", PURPLE),
        ("proposal_4", (760, 520, 1160, 690), "UNIVERSES REPRODUCE\nAND TUNE PHYSICS", GREEN),
        ("proposal_5", (1270, 520, 1670, 690), "BABY UNIVERSES WITH\nDIFFERENT FINGERPRINTS", CYAN),
    ]
    for name, box, label, color in specs:
        if visible(times, name, card_t):
            arrow(draw, (430, 445), (box[0] - 14, (box[1] + box[3]) / 2), color, 3)
            rounded(draw, box, 20, PANEL2, color, 3)
            wrap(draw, label, (box[0] + 25, box[1] + 20, box[2] - 25, box[3] - 20), 23, color, True, max_lines=3)
    if visible(times, "no_shared_forecast", card_t):
        badge(draw, (500, 735, 1420, 800), "AT LEAST FIVE PROPOSALS IN THIS SURVEY · NO SINGLE SHARED FORECAST", RED, 22)
    if visible(times, "closing_record", card_t):
        badge(draw, (585, 805, 1335, 850), "CLOSING RECORD · THE DOCUMENT THIS VIDEO REPORTS FROM", MUTED, 20)


def card03(draw, card_t, times):
    nodes = [(150, 375, 500, 545, "MODEL", BLUE), (715, 350, 1205, 575, "TARGET", GREEN), (1420, 375, 1770, 545, "MEASUREMENT", AMBER)]
    for x0, y0, x1, y1, label, color in nodes:
        rounded(draw, (x0, y0, x1, y1), 24, PANEL2, color, 4)
        center(draw, label, ((x0 + x1) / 2, (y0 + y1) / 2), 30, color, True)
    arrow(draw, (505, 460), (705, 460), CYAN)
    arrow(draw, (1215, 460), (1410, 460), CYAN)
    if visible(times, "target", card_t):
        draw.ellipse((1305, 428, 1333, 456), fill=RED)
        arrow(draw, (1319, 442), (1195, 375), RED)
        badge(draw, (325, 695, 880, 765), "1 · CAN BE WRONG", GREEN, 25)
    if visible(times, "identify", card_t):
        arrow(draw, (1590, 555), (1360, 690), AMBER)
        arrow(draw, (1590, 555), (1735, 690), AMBER)
        badge(draw, (1050, 695, 1620, 765), "2 · CAN IDENTIFY THE IDEA", BLUE, 25)
    if visible(times, "neutron_stars", card_t):
        badge(draw, (270, 785, 1050, 840), "NEUTRON STARS: ULTRA-DENSE COLLAPSED CORES", MUTED, 21)
    if visible(times, "pulsars", card_t):
        badge(draw, (1080, 785, 1750, 840), "SPINNING, TIMED NEUTRON STARS ARE PULSARS", MUTED, 20)


def card04(draw, card_t, times):
    if visible(times, "family_tree", card_t):
        center(draw, "UNIVERSE", (260, 335), 27, BLUE, True)
        arrow(draw, (380, 335), (570, 335), CYAN)
        center(draw, "BLACK HOLES", (735, 335), 27, CYAN, True)
        arrow(draw, (900, 335), (1080, 335), CYAN)
        center(draw, "CHILD UNIVERSES", (1325, 335), 27, GREEN, True)
        for index in range(3):
            draw.ellipse((1510 + index * 95, 300 + index * 28, 1560 + index * 95, 350 + index * 28), outline=GREEN, width=3)
    if visible(times, "mass_1_5", card_t):
        position = mass_axis(draw, 665, show_unit=True)
        x = position(1.5)
        draw.line((x, 530, x, 685), fill=BLUE, width=5)
        center(draw, "BROWN–BETHE MAXIMUM ~1.5 M☉", (x, 500), 23, BLUE, True, serif=True)
        if visible(times, "mass_2", card_t):
            x = position(2.0)
            draw.rectangle((x, 570, position(2.2), 650), fill=(80, 54, 44))
            draw.line((x, 540, x, 685), fill=AMBER, width=5)
            center(draw, "M ≳ 2 M☉", (x, 510), 26, AMBER, True, serif=True)
        if visible(times, "source_quote", card_t):
            badge(draw, (500, 775, 1420, 845), "“SERIOUS DOUBT OR SIMPLY FALSIFY” — BROWN, LEE & RHO", RED, 22)


def draw_gradient_no_terminus(image: Image.Image, y0: int, y1: int, x0: int, peak_x: int, x1: int):
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    pixels = overlay.load()
    if pixels is None:
        raise RuntimeError("gradient pixel buffer unavailable")
    for x in range(x0, x1):
        if x <= peak_x:
            u = (x - x0) / max(1, peak_x - x0)
        else:
            u = (x1 - 1 - x) / max(1, x1 - 1 - peak_x)
        alpha = round(115 * max(0.0, u) ** 2)
        for y in range(y0, y1):
            pixels[x, y] = (*GREEN, alpha)
    image.alpha_composite(overlay)


def card05(image, draw, card_t, times):
    position = mass_axis(draw, 655, show_unit=True)
    center(draw, "EVERY DISTANT-STAR MASS HAS AN UNCERTAINTY RANGE", (960, 285), 27, AMBER, True)
    draw.rectangle((position(2.0), 390, position(2.2), 640), fill=(49, 38, 37))
    draw.line((position(1.5), 400, position(1.5), 675), fill=BLUE, width=3)
    center(draw, "BROWN–BETHE MAXIMUM ~1.5 M☉", (position(1.5), 375), 18, BLUE, True, serif=True)
    center(draw, "M ≳ 2 M☉", ((position(2.0) + position(2.2)) / 2, 425), 20, AMBER, True, serif=True)
    draw.line((position(2.0), 400, position(2.0), 680), fill=AMBER, width=3)
    center(draw, "2.00", (position(2.0), 378), 22, AMBER, True, mono=True)
    # At 95.4%, the only scaled uncertainty representation is a continuous
    # alpha gradient. It fades at both image-space ends and remains visibly
    # continuous through 2.00; no endpoint or lower-bound position is drawn.
    if visible(times, "percent_95_4", card_t):
        draw_gradient_no_terminus(
            image, 536, 575,
            round(position(1.40)), round(position(2.08)), round(position(2.20)),
        )
        draw = ImageDraw.Draw(image)
    if visible(times, "demorest_uncertainty", card_t):
        y = 475
        center(draw, "DEMOREST: 1.97 ± 0.04 M☉", (455, y), 22, BLUE, True, serif=True)
        draw.line((position(1.93), y, position(2.01), y), fill=BLUE, width=8)
        draw.line((position(1.93), y - 12, position(1.93), y + 12), fill=BLUE, width=4)
        draw.line((position(2.01), y - 12, position(2.01), y + 12), fill=BLUE, width=4)
        draw.ellipse((position(1.97) - 8, y - 8, position(1.97) + 8, y + 8), fill=WHITE)
    if visible(times, "fonseca_uncertainty", card_t):
        y = 555
        label = "FONSECA: 2.08 ± 0.07 M☉"
        if visible(times, "percent_68_3", card_t):
            label += " · 68.3%"
        center(draw, label, (485, y), 21, GREEN, True, serif=True)
        if not visible(times, "percent_95_4", card_t):
            draw.line((position(2.01), y, position(2.15), y), fill=GREEN, width=8)
            draw.line((position(2.01), y - 12, position(2.01), y + 12), fill=GREEN, width=4)
            draw.line((position(2.15), y - 12, position(2.15), y + 12), fill=GREEN, width=4)
            draw.ellipse((position(2.08) - 8, y - 8, position(2.08) + 8, y + 8), fill=WHITE)
    if visible(times, "percent_95_4", card_t):
        rounded(draw, (220, 720, 1700, 835), 22, PANEL2, RED, 3)
        wrap(draw, "AT 95.4% CREDIBILITY, THE CLOSING RECORD STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00", (270, 735, 1650, 780), 21, WHITE, True, max_lines=2)
        wrap(draw, "NO 95.4% LOWER-BOUND VALUE IS QUOTED OR PLOTTED HERE", (320, 790, 1600, 825), 20, RED, True, max_lines=1)


def card06(draw, card_t, times):
    draw.line((260, 315, 1660, 315), fill=GRID, width=3)
    for x in (435, 785, 1135, 1485):
        draw.line((x, 307, x, 323), fill=GRID, width=2)
    if visible(times, "source_disjunction", card_t):
        rounded(draw, (210, 360, 750, 610), 24, PANEL2, AMBER, 4)
        wrap(draw, "SERIOUS DOUBT", (260, 420, 700, 550), 34, AMBER, True, max_lines=2)
        center(draw, "OR", (960, 485), 46, WHITE, True)
        rounded(draw, (1170, 360, 1710, 610), 24, PANEL2, RED, 4)
        wrap(draw, "SIMPLY FALSIFY", (1220, 420, 1660, 550), 34, RED, True, max_lines=2)
    if visible(times, "not_adjudicated", card_t):
        arrow(draw, (960, 720), (960, 615), MUTED)
        badge(draw, (590, 690, 1330, 755), "NOT ADJUDICATED HERE", BLUE, 26)
    if visible(times, "named_regime", card_t):
        badge(draw, (500, 780, 1420, 850), "OBSERVATIONS ENTER THE SOURCE-NAMED REGIME", GREEN, 24)


def card07(draw, card_t, times):
    draw.ellipse((120, 320, 610, 800), outline=BLUE, width=6)
    center(draw, "PARENT ROTATION AXIS", (365, 290), 24, BLUE, True)
    draw.line((365, 315, 1170, 710), fill=CYAN, width=5)
    arrow(draw, (610, 500), (965, 625), CYAN)
    draw.ellipse((835, 320, 1455, 820), outline=PURPLE, width=5)
    center(draw, "CHILD UNIVERSE", (1145, 290), 24, PURPLE, True)
    for index in range(10):
        galaxy(draw, 995 + (index % 5) * 90, 410 + (index // 5) * 180, BLUE if index % 2 == 0 else PURPLE, -1 if index % 2 else 1, 0.15)
    if visible(times, "inherited_axis", card_t):
        badge(draw, (775, 735, 1515, 790), "INHERITED PREFERRED AXIS", PURPLE, 22)
    if visible(times, "cw_ccw", card_t):
        badge(draw, (1500, 375, 1810, 460), "CW COUNTS", BLUE, 23)
        center(draw, "≠", (1655, 545), 48, AMBER, True)
        badge(draw, (1500, 630, 1810, 715), "CCW COUNTS", PURPLE, 23)
    if visible(times, "no_amplitude", card_t):
        badge(draw, (610, 800, 1310, 850), "EXPLICIT QUALITATIVE CLAIM · NO AMPLITUDE SHOWN", MUTED, 20)


def card08(draw, card_t, times):
    draw.line((170, 390, 1750, 390), fill=GRID, width=5)
    if visible(times, "timeline", card_t):
        draw.ellipse((385, 373, 419, 407), fill=BLUE)
        draw.ellipse((1200, 373, 1234, 407), fill=AMBER)
        center(draw, "OBSERVATIONS CITED FIRST", (402, 335), 23, BLUE, True)
        center(draw, "HANDEDNESS CLAIM ADDED IN 2025", (1217, 335), 23, AMBER, True)
    rounded(draw, (180, 500, 1740, 790), 26, PANEL, GRID, 3)
    center(draw, "EQUATIONS PRESENT", (960, 545), 27, GREEN, True)
    if visible(times, "forecast_blanks", card_t):
        labels = ["SIZE?", "WHERE / WHEN?", "DIRECTION?", "PASS-OR-FAIL RANGE?"]
        for index, label in enumerate(labels):
            x = 250 + index * 380
            rounded(draw, (x, 610, x + 330, 715), 16, PANEL2, RED, 3)
            center(draw, label, (x + 165, 662), 20, RED, True)
    if visible(times, "post_data", card_t):
        badge(draw, (500, 800, 1420, 850), "NOT A PREDICTION MADE BEFORE THE DATA", RED, 24)


def card09(draw, card_t, times):
    if visible(times, "observed_difference", card_t):
        rounded(draw, (650, 365, 1270, 545), 26, PANEL2, AMBER, 4)
        wrap(draw, "OBSERVED CW/CCW DIFFERENCE", (720, 410, 1200, 500), 29, AMBER, True, max_lines=2)
    if visible(times, "not_identify", card_t):
        arrow(draw, (850, 550), (560, 710), MUTED)
        badge(draw, (340, 690, 710, 780), "BHU?", BLUE, 32)
    if visible(times, "other_causes", card_t):
        arrow(draw, (1070, 550), (1390, 710), MUTED)
        badge(draw, (1210, 690, 1680, 780), "OTHER POSSIBLE CAUSES", PURPLE, 25)
        badge(draw, (650, 585, 1270, 635), "NOT BHU-SPECIFIC BY ITSELF", MUTED, 21)
    if visible(times, "measurement_not_identification", card_t):
        badge(draw, (540, 805, 1380, 855), "MEASUREMENT ≠ IDENTIFICATION", RED, 27)


def card10(draw, card_t, times):
    rounded(draw, (100, 300, 900, 760), 28, PANEL, BLUE, 4)
    rounded(draw, (1020, 300, 1820, 760), 28, PANEL, PURPLE, 4)
    if visible(times, "no_range", card_t):
        wrap(draw, "1 · NO SOURCE-DEFINED PASS-OR-FAIL RANGE", (160, 330, 840, 405), 23, BLUE, True, max_lines=2)
        center(draw, "FINITE-PRECISION RESULT", (500, 475), 25, WHITE, True)
        draw.line((245, 550, 755, 550), fill=MUTED, width=5)
        badge(draw, (250, 625, 750, 690), "NO PREDICTED SIZE", RED, 24)
    if visible(times, "no_signature", card_t):
        center(draw, "2 · NO UNIQUE SIGNATURE", (1420, 365), 27, PURPLE, True)
        badge(draw, (1260, 440, 1580, 520), "POSITIVE RESULT", AMBER, 23)
        arrow(draw, (1340, 525), (1180, 640), MUTED)
        arrow(draw, (1500, 525), (1650, 640), MUTED)
        wrap(draw, "A POSITIVE RESULT DOES NOT IDENTIFY BHU", (1080, 630, 1760, 710), 23, WHITE, True, max_lines=2)
    if visible(times, "trustworthy_measurement", card_t):
        center(draw, "MEASUREMENT MAY STILL BE TRUSTWORTHY", (960, 785), 20, MUTED, True)
    if visible(times, "closing_line", card_t):
        badge(draw, (420, 820, 1500, 865), "THE HUNT HAD A SOURCE · IT DID NOT HAVE A TARGET", RED, 21)


def card11(draw, card_t, times):
    badge(draw, (510, 285, 740, 345), "MODEL", BLUE, 22)
    arrow(draw, (750, 315), (825, 315), CYAN, 3)
    badge(draw, (835, 285, 1085, 345), "TARGET", GREEN, 22)
    arrow(draw, (1095, 315), (1170, 315), CYAN, 3)
    badge(draw, (1180, 285, 1470, 345), "MEASUREMENT", AMBER, 22)
    if visible(times, "target_gate", card_t):
        rounded(draw, (145, 400, 665, 650), 28, PANEL2, BLUE, 4)
        wrap(draw, "REOPEN CONDITION 1 · CALIBRATED TARGET", (205, 455, 605, 590), 29, BLUE, True, max_lines=3)
    if visible(times, "signature_gate", card_t):
        rounded(draw, (1255, 400, 1775, 650), 28, PANEL2, GREEN, 4)
        wrap(draw, "REOPEN CONDITION 2 · UNIQUE SIGNATURE", (1315, 455, 1715, 590), 29, GREEN, True, max_lines=3)
    if visible(times, "asymmetry_alone", card_t):
        rounded(draw, (720, 430, 1200, 590), 23, PANEL, AMBER, 3)
        wrap(draw, "SPIN ASYMMETRY ALONE IS NOT A BHU TEST", (770, 465, 1150, 555), 23, AMBER, True, max_lines=3)
        arrow(draw, (720, 510), (675, 510), MUTED)
        arrow(draw, (1200, 510), (1245, 510), MUTED)
    if visible(times, "reopen", card_t):
        badge(draw, (370, 785, 1550, 850), "REOPEN ONLY FOR A CALIBRATED TARGET OR A UNIQUE SIGNATURE", GREEN, 26)


DRAWERS: dict[str, Callable] = {
    "01": card01, "02": card02, "03": card03, "04": card04,
    "06": card06, "07": card07, "08": card08, "09": card09,
    "10": card10, "11": card11,
}


class Renderer:
    def __init__(self):
        for name, expected in EXPECTED.items():
            actual = sha(SOURCE / name)
            if actual != expected:
                raise RuntimeError(f"frozen source hash mismatch {name}: {actual}")
        self.story = json.loads(STORY_PATH.read_text())
        self.timeline = json.loads(TIMELINE_PATH.read_text())
        self.cards = self.timeline["cards"]
        if self.timeline["source_hashes"] != EXPECTED:
            raise RuntimeError("audio timeline source tuple mismatch")
        if abs(float(self.timeline["master_duration_seconds"]) - 415.0) > 0.002:
            raise RuntimeError("audio duration is not 415 seconds")
        if any(not 120 <= float(card["delivered_wpm"]) <= 135 for card in self.cards):
            raise RuntimeError("encoded input audio WPM outside contract")
        story_cards = {card["id"]: card for card in self.story["cards"]}
        for card in self.cards:
            spec = story_cards[card["card_id"]]
            if card["heading"] != spec["heading"] or card["narration"] != spec["narration"]:
                raise RuntimeError(f"timeline/storyboard drift Card {card['card_id']}")
            if " ".join(cue["text"] for cue in card["captions"]) != card["narration"]:
                raise RuntimeError(f"captions not word-for-word Card {card['card_id']}")
        public_surface = [self.story["title"]]
        for card in self.story["cards"]:
            public_surface += [card["heading"], card["narration"], card["diagram"], *card["on_screen_support"]]
        public_blob = " ".join(public_surface).lower()
        for name in CREW_TERMS:
            if re.search(rf"\b{re.escape(name)}\b", public_blob):
                raise RuntimeError(f"viewer-facing crew name in V11 source: {name}")
        if "cns" in public_blob.lower():
            raise RuntimeError("retired CNS form in V11 public projection")
        self.story_cards = story_cards
        self.card04_heading_reveal = self.phrase_end(self.cards[3], "cosmological natural selection")

    @staticmethod
    def phrase_end(card: dict, phrase: str) -> float:
        needle = re.findall(r"[a-z0-9]+", phrase.lower())
        tokens = card["tokens"]
        haystack = [item["token"] for item in tokens]
        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index:index + len(needle)] == needle:
                return float(tokens[index + len(needle) - 1]["card_end_seconds"])
        raise RuntimeError(f"phrase not found in Card {card['card_id']}: {phrase}")

    def active_card(self, master_t: float) -> tuple[dict, float]:
        for card in self.cards:
            if master_t < float(card["master_end_seconds"]) - 1e-9:
                return card, master_t - float(card["master_start_seconds"])
        return self.cards[-1], float(self.cards[-1]["planned_seconds"]) - 1 / FPS

    @staticmethod
    def active_caption(card: dict, card_t: float) -> str | None:
        for cue in card["captions"]:
            if float(cue["card_start_seconds"]) <= card_t <= float(cue["card_end_seconds"]):
                return cue["text"]
        return None

    def frame(self, master_t: float) -> Image.Image:
        card, card_t = self.active_card(master_t)
        card_id = card["card_id"]
        spec = self.story_cards[card_id]
        image = Image.new("RGBA", (W, H), (*BG, 255))
        draw = ImageDraw.Draw(image)
        for x in range(0, W + 1, 96):
            draw.line((x, 0, x, H), fill=(19, 31, 48), width=1)
        for y in range(0, H + 1, 96):
            draw.line((0, y, W, y), fill=(19, 31, 48), width=1)
        draw.text((72, 36), "NEBULAMIND · CLOSING RECORD", font=font(21, True), fill=MUTED)
        right = f"{int(card_id)} / 11"
        face = font(21, True)
        draw.text((W - 72 - draw.textlength(right, font=face), 36), right, font=face, fill=MUTED)
        draw.line((72, 82, W - 72, 82), fill=GRID, width=2)
        heading_visible = card_id != "04" or card_t >= self.card04_heading_reveal
        if heading_visible:
            wrap(draw, spec["heading"], (125, 105, 1795, 235), 46, WHITE, True, max_lines=2)
        elif card_id == "04":
            center(draw, "LISTENING FOR THE PROPOSAL'S FULL NAME…", (960, 170), 24, MUTED, True)
        times = reveal_times(card)
        if card_id == "05":
            card05(image, draw, card_t, times)
            draw = ImageDraw.Draw(image)
        else:
            DRAWERS[card_id](draw, card_t, times)
        caption = self.active_caption(card, card_t)
        if caption:
            rounded(draw, (125, 875, 1795, 1000), 18, (7, 12, 21), GRID, 2)
            wrap(draw, caption, (175, 890, 1745, 982), 27, WHITE, True, max_lines=3)
        return image.convert("RGB")

    def interval_boundaries(self) -> list[int]:
        boundaries = {0, 415 * FPS}
        for card in self.cards:
            card_start = float(card["master_start_seconds"])
            card_end = float(card["master_end_seconds"])
            boundaries.add(round(card_start * FPS))
            boundaries.add(round(card_end * FPS))
            for cue in card["captions"]:
                boundaries.add(max(round((card_start + float(cue["card_start_seconds"])) * FPS), round(card_start * FPS)))
                boundaries.add(min(math.ceil((card_start + float(cue["card_end_seconds"])) * FPS), round(card_end * FPS)))
            for reveal in card["reveals"]:
                boundaries.add(math.ceil((card_start + float(reveal["card_seconds"])) * FPS))
        card04_start = float(self.cards[3]["master_start_seconds"])
        boundaries.add(math.ceil((card04_start + self.card04_heading_reveal) * FPS))
        result = sorted(frame for frame in boundaries if 0 <= frame <= 415 * FPS)
        if result[0] != 0 or result[-1] != 415 * FPS:
            raise RuntimeError("render interval boundaries do not cover 415 seconds")
        return result

    def build_states(self):
        FRAME_DIR.mkdir(parents=True, exist_ok=True)
        boundaries = self.interval_boundaries()
        entries = []
        for index, (start_frame, end_frame) in enumerate(zip(boundaries, boundaries[1:])):
            if end_frame <= start_frame:
                continue
            timestamp = start_frame / FPS
            output = FRAME_DIR / f"state-{index:04d}-{start_frame:05d}.png"
            self.frame(timestamp).save(output, optimize=True)
            entries.append({
                "index": index,
                "start_frame": start_frame,
                "end_frame": end_frame,
                "frames": end_frame - start_frame,
                "start_seconds": timestamp,
                "duration_seconds": (end_frame - start_frame) / FPS,
                "file": str(output.relative_to(ROOT)),
                "sha256": sha(output),
            })
        lines = ["ffconcat version 1.0"]
        for entry in entries:
            lines.append(f"file '{(ROOT / entry['file']).as_posix()}'")
            lines.append(f"duration {entry['duration_seconds']:.9f}")
        lines.append(f"file '{(ROOT / entries[-1]['file']).as_posix()}'")
        CONCAT_PATH.write_text("\n".join(lines) + "\n")
        return boundaries, entries

    def preview(self):
        preview_dir = ROOT / "preview"
        preview_dir.mkdir(exist_ok=True)
        samples = []
        for card in self.cards:
            start = float(card["master_start_seconds"])
            for label, fraction in (("early", 0.05), ("mid", 0.55), ("late", 0.92)):
                timestamp = start + float(card["planned_seconds"]) * fraction
                output = preview_dir / f"card-{card['card_id']}-{label}.png"
                self.frame(timestamp).save(output)
                samples.append(output)
        print("\n".join(str(path) for path in samples))

    def render(self):
        boundaries, entries = self.build_states()
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        command = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "concat", "-safe", "0", "-i", str(CONCAT_PATH),
            "-i", str(AUDIO_PATH),
            "-map", "0:v:0", "-map", "1:a:0",
            "-vf", f"fps={FPS}", "-r", str(FPS), "-t", "415.000000",
            "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(OUTPUT),
        ]
        subprocess.run(command, check=True)
        probe = json.loads(subprocess.run([
            "ffprobe", "-v", "error", "-show_entries",
            "format=duration,size:stream=codec_name,codec_type,width,height,r_frame_rate,nb_frames,sample_rate,channels",
            "-of", "json", str(OUTPUT),
        ], check=True, capture_output=True, text=True).stdout)
        video_stream = next(stream for stream in probe["streams"] if stream["codec_type"] == "video")
        audio_stream = next(stream for stream in probe["streams"] if stream["codec_type"] == "audio")
        if (int(video_stream["width"]), int(video_stream["height"]), video_stream["r_frame_rate"]) != (W, H, "30/1"):
            raise RuntimeError(f"encoded video geometry drift: {video_stream}")
        if int(video_stream.get("nb_frames", 0)) != 415 * FPS:
            raise RuntimeError(f"encoded frame count drift: {video_stream.get('nb_frames')}")
        if abs(float(probe["format"]["duration"]) - 415) > 0.05:
            raise RuntimeError(f"encoded duration drift: {probe['format']['duration']}")
        manifest = {
            "status": "ENCODED_V11_CANDIDATE_AWAITING_ENCODED_QA",
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "source_hashes": EXPECTED,
            "audio_timeline": str(TIMELINE_PATH.relative_to(ROOT)),
            "audio_timeline_sha256": sha(TIMELINE_PATH),
            "renderer": str(Path(__file__).relative_to(ROOT)),
            "renderer_sha256": sha(Path(__file__)),
            "pillow_version": PIL.__version__,
            "interval_boundary_count": len(boundaries),
            "render_state_count": len(entries),
            "raw_frames_encoded": 415 * FPS,
            "output": str(OUTPUT),
            "output_sha256": sha(OUTPUT),
            "probe": probe,
            "card04_heading_reveal_card_seconds": self.card04_heading_reveal,
            "upload_authorized": False,
            "publication_authorized": False,
        }
        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
        print(json.dumps(manifest, indent=2, ensure_ascii=False))


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args()
    renderer = Renderer()
    if args.preview:
        renderer.preview()
    if args.render:
        renderer.render()
    if not args.preview and not args.render:
        raise SystemExit("choose --preview or --render")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
