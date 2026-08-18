#!/usr/bin/env python3
"""Render eight deterministic 1920x1080 PIL infographic cards."""
from __future__ import annotations

import functools
import hashlib
import json
import math
import random
from pathlib import Path
from typing import Callable

from PIL import Image, ImageDraw, ImageFont, ImageOps

import pipeline

W, H = 1920, 1080
BG = (7, 13, 25)
PANEL = (16, 27, 46)
PANEL_2 = (23, 39, 63)
GRID = (55, 78, 111)
WHITE = (239, 244, 250)
MUTED = (157, 174, 197)
BLUE = (103, 181, 255)
CYAN = (84, 221, 226)
AMBER = (246, 184, 91)
RED = (242, 111, 113)
GREEN = (111, 211, 166)
PURPLE = (176, 142, 244)
FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"
MONO_PATH = "/System/Library/Fonts/Menlo.ttc"


@functools.lru_cache(maxsize=None)
def font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    path = MONO_PATH if mono else FONT_PATH
    index = 1 if bold and not mono else 0
    return ImageFont.truetype(path, size, index=index)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rounded(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    *,
    fill: tuple[int, int, int] = PANEL,
    outline: tuple[int, int, int] = GRID,
    width: int = 3,
    radius: int = 24,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    color: tuple[int, int, int] = CYAN,
    width: int = 6,
) -> None:
    draw.line((*start, *end), fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    length = 18
    for offset in (2.55, -2.55):
        draw.line(
            (
                end[0],
                end[1],
                end[0] + length * math.cos(angle + offset),
                end[1] + length * math.sin(angle + offset),
            ),
            fill=color,
            width=width,
        )


def starfield(image: Image.Image) -> None:
    draw = ImageDraw.Draw(image)
    rng = random.Random(20260818)
    for _ in range(180):
        x = rng.randrange(0, W)
        y = rng.randrange(0, H)
        radius = rng.choice((1, 1, 1, 2))
        value = rng.randrange(25, 65)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(value, value + 5, value + 16))
    for y in range(0, H + 1, 90):
        draw.line((0, y, W, y), fill=(14, 27, 46), width=1)
    for x in range(0, W + 1, 96):
        draw.line((x, 0, x, H), fill=(14, 27, 46), width=1)


class TextSurface:
    def __init__(self, image: Image.Image, permitted: list[str]):
        self.image = image
        self.draw = ImageDraw.Draw(image)
        self.permitted = permitted
        self.emitted: list[str] = []

    def _record(self, text: str) -> None:
        if text not in self.permitted:
            raise RuntimeError(f"unpermitted viewer text: {text!r}")
        self.emitted.append(text)

    def wrap(
        self,
        text: str,
        box: tuple[int, int, int, int],
        size: int,
        *,
        color: tuple[int, int, int] = WHITE,
        bold: bool = False,
        align: str = "center",
        max_lines: int | None = None,
        mono: bool = False,
    ) -> None:
        self._record(text)
        f = font(size, bold, mono)
        words = text.split()
        lines: list[str] = []
        current = ""
        width = box[2] - box[0]
        for word in words:
            trial = (current + " " + word).strip()
            if self.draw.textlength(trial, font=f) <= width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        if max_lines is not None and len(lines) > max_lines:
            raise RuntimeError(f"text exceeds {max_lines} lines: {text!r} -> {lines!r}")
        step = size + 10
        total = len(lines) * step - 10
        y = box[1] + max(0.0, (box[3] - box[1] - total) / 2)
        for line in lines:
            line_width = self.draw.textlength(line, font=f)
            if align == "left":
                x = box[0]
            elif align == "right":
                x = box[2] - line_width
            else:
                x = box[0] + (width - line_width) / 2
            self.draw.text((x, y), line, font=f, fill=color)
            y += step

    def plate(
        self,
        text: str,
        box: tuple[int, int, int, int],
        color: tuple[int, int, int],
        *,
        size: int = 25,
        max_lines: int = 2,
    ) -> None:
        rounded(self.draw, box, fill=PANEL_2, outline=color, width=3, radius=18)
        self.wrap(text, (box[0] + 24, box[1] + 10, box[2] - 24, box[3] - 10), size, color=color, bold=True, max_lines=max_lines)


def base_card(panel: dict) -> tuple[Image.Image, TextSurface, list[str]]:
    image = Image.new("RGB", (W, H), BG)
    starfield(image)
    permitted = panel["viewer_text_closed_world"]
    surface = TextSurface(image, permitted)
    surface.draw.line((82, 246, W - 82, 246), fill=GRID, width=3)
    surface.wrap(permitted[0], (110, 56, W - 110, 224), 48, bold=True, max_lines=2)
    return image, surface, permitted[1:]


def draw_panel_01(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (150, 340, 830, 455), BLUE, size=30)
    surface.plate(labels[1], (150, 500, 830, 615), MUTED, size=27)
    rounded(draw, (900, 325, 1770, 640), fill=PANEL, outline=CYAN, width=4)
    draw.rectangle((990, 395, 1220, 565), outline=CYAN, width=5)
    draw.line((1030, 435, 1180, 435), fill=CYAN, width=4)
    draw.line((1030, 480, 1160, 480), fill=CYAN, width=4)
    draw.line((1030, 525, 1130, 525), fill=CYAN, width=4)
    surface.plate(labels[2], (1260, 405, 1690, 555), CYAN, size=27)
    arrow(draw, (800, 477), (900, 477), CYAN)
    surface.plate(labels[3], (390, 755, 1530, 885), RED, size=34)
    draw.line((960, 640, 960, 750), fill=RED, width=6)


def draw_panel_02(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    draw.ellipse((825, 300, 1095, 570), fill=PANEL_2, outline=CYAN, width=5)
    for offset in (-55, 0, 55):
        draw.ellipse((930 + offset - 12, 423 - 12, 930 + offset + 12, 423 + 12), fill=WHITE)
        if offset < 55:
            draw.line((942 + offset, 423, 973 + offset, 423), fill=WHITE, width=5)
    arrow(draw, (870, 555), (590, 690), BLUE)
    arrow(draw, (1050, 555), (1330, 690), AMBER)
    surface.plate(labels[0], (120, 670, 790, 820), BLUE, size=29, max_lines=3)
    surface.plate(labels[1], (835, 610, 1085, 730), WHITE, size=44)
    surface.plate(labels[2], (1130, 670, 1800, 820), AMBER, size=28, max_lines=3)
    draw.rectangle((280, 860, 360, 940), outline=BLUE, width=6)
    draw.rectangle((1560, 860, 1640, 940), outline=AMBER, width=6)
    arrow(draw, (790, 744), (850, 744), MUTED, width=4)
    arrow(draw, (1130, 744), (1070, 744), MUTED, width=4)


def draw_panel_03(surface: TextSurface, labels: list[str]) -> dict[str, float | bool]:
    draw = surface.draw
    x_axis = 570
    y_bottom = 900
    y_top = 305
    low = 1.4
    high = 2.22

    def y_of(value: float) -> float:
        return y_bottom - (value - low) / (high - low) * (y_bottom - y_top)

    draw.line((x_axis, y_top, x_axis, y_bottom), fill=WHITE, width=5)
    for value in (1.4, 1.6, 1.8, 2.0, 2.2):
        y = y_of(value)
        draw.line((x_axis - 13, y, x_axis + 13, y), fill=MUTED, width=3)
    y_15 = y_of(1.5)
    y_20 = y_of(2.0)
    draw.line((x_axis - 10, y_15, 960, y_15), fill=BLUE, width=5)
    for x in range(x_axis - 10, 960, 24):
        draw.line((x, y_20, min(x + 12, 960), y_20), fill=AMBER, width=5)
    for value, x in ((1.66, 690), (1.75, 760), (1.84, 830)):
        y = y_of(value)
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill=BLUE, outline=WHITE, width=2)

    center = 2.08
    one_sigma_low = center - 0.07
    one_sigma_high = center + 0.07
    y_center = y_of(center)
    y_low_1 = y_of(one_sigma_low)
    y_high_1 = y_of(one_sigma_high)

    # The stricter state is a soft uncertainty halo that visibly crosses 2.00.
    # It carries no hard lower endpoint or invented numeric lower-bound label.
    strict_visual_low = 1.94
    y_strict_low = y_of(strict_visual_low)
    steps = 14
    for index in range(steps):
        fraction = index / (steps - 1)
        y = y_center + fraction * (y_strict_low - y_center)
        alpha = 130 * (1.0 - fraction)
        color = tuple(round(BG[i] * (1 - alpha / 255) + PURPLE[i] * (alpha / 255)) for i in range(3))
        draw.ellipse((716, y - 7, 804, y + 7), fill=color)

    # Draw the quoted one-sigma interval above the softer strict-credibility halo.
    # Its lower cap is visibly above the dashed 2.00 line.
    draw.line((760, y_high_1, 760, y_low_1), fill=GREEN, width=10)
    draw.line((738, y_high_1, 782, y_high_1), fill=GREEN, width=6)
    draw.line((738, y_low_1, 782, y_low_1), fill=GREEN, width=6)
    draw.ellipse((745, y_center - 15, 775, y_center + 15), fill=WHITE, outline=GREEN, width=4)

    surface.plate(labels[0], (1010, 290, 1800, 385), BLUE, size=23)
    surface.plate(labels[1], (1010, 400, 1800, 500), AMBER, size=23)
    surface.plate(labels[2], (1010, 515, 1800, 630), GREEN, size=22)
    surface.plate(labels[3], (1010, 645, 1390, 745), GREEN, size=22)
    surface.plate(labels[4], (1420, 645, 1800, 745), PURPLE, size=21)
    surface.plate(labels[5], (1080, 805, 1730, 900), AMBER, size=27)
    return {
        "threshold": 2.0,
        "center": center,
        "one_sigma_low": one_sigma_low,
        "one_sigma_high": one_sigma_high,
        "strict_95_4_visual_crosses_threshold": strict_visual_low < 2.0,
        "strict_95_4_hard_lower_endpoint_drawn": False,
    }


def draw_panel_04(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (520, 300, 1400, 405), BLUE, size=29)
    draw.ellipse((360, 500, 650, 790), fill=(27, 60, 93), outline=BLUE, width=6)
    draw.ellipse((1270, 500, 1560, 790), fill=(81, 55, 31), outline=AMBER, width=6)
    draw.line((560, 850, 1360, 850), fill=WHITE, width=6)
    draw.polygon(((960, 760), (900, 900), (1020, 900)), fill=MUTED)
    surface.plate(labels[1], (700, 455, 1220, 595), AMBER, size=30, max_lines=3)
    surface.plate(labels[2], (520, 905, 1400, 995), GREEN, size=27)


def draw_panel_05(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (130, 290, 850, 395), BLUE, size=25)
    surface.plate(labels[1], (1070, 290, 1790, 395), BLUE, size=25)
    x0, x1 = 245, 1690
    y_threshold, y_observed = 555, 730
    draw.line((x0, 880, x1, 880), fill=WHITE, width=5)
    for value in (0, 4, 8, 12, 16, 20):
        x = x0 + value / 22 * (x1 - x0)
        draw.line((x, 870, x, 895), fill=MUTED, width=3)
    x4 = x0 + 4 / 22 * (x1 - x0)
    x193 = x0 + 19.3 / 22 * (x1 - x0)
    x186 = x0 + 18.6 / 22 * (x1 - x0)
    x200 = x0 + 20.0 / 22 * (x1 - x0)
    draw.rounded_rectangle((x0, y_threshold - 28, x4, y_threshold + 28), radius=14, fill=AMBER)
    draw.rounded_rectangle((x0, y_observed - 36, x193, y_observed + 36), radius=16, fill=RED)
    draw.line((x186, y_observed, x200, y_observed), fill=WHITE, width=8)
    draw.line((x186, y_observed - 16, x186, y_observed + 16), fill=WHITE, width=5)
    draw.line((x200, y_observed - 16, x200, y_observed + 16), fill=WHITE, width=5)
    surface.plate(labels[2], (160, 450, 720, 525), AMBER, size=24)
    surface.plate(labels[3], (780, 620, 1710, 695), RED, size=25)
    surface.plate(labels[4], (1210, 770, 1740, 845), WHITE, size=23)
    surface.plate(labels[5], (490, 925, 1430, 995), MUTED, size=22)


def draw_panel_06(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    boxes = [(120, 320, 560, 455), (740, 320, 1180, 455), (1360, 320, 1800, 455)]
    colors = [BLUE, AMBER, GREEN]
    for index, (box, color) in enumerate(zip(boxes, colors)):
        surface.plate(labels[index], box, color, size=24, max_lines=2)
        if index < 2:
            arrow(draw, (box[2] + 20, 387), (boxes[index + 1][0] - 20, 387), CYAN, width=5)
    draw.rounded_rectangle((805, 530, 1115, 820), radius=38, fill=PANEL_2, outline=CYAN, width=6)
    draw.arc((830, 440, 1090, 660), start=180, end=360, fill=CYAN, width=18)
    draw.ellipse((930, 625, 990, 685), fill=WHITE)
    draw.rectangle((953, 675, 967, 745), fill=WHITE)
    surface.plate(labels[3], (100, 540, 650, 635), BLUE, size=26)
    surface.plate(labels[4], (1260, 540, 1820, 655), BLUE, size=24, max_lines=3)
    surface.plate(labels[5], (200, 860, 1720, 965), RED, size=31)


def draw_panel_07(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (420, 300, 1500, 400), RED, size=29)
    surface.plate(labels[1], (420, 455, 1500, 575), AMBER, size=26, max_lines=3)
    surface.plate(labels[2], (420, 630, 1500, 730), RED, size=26)
    surface.plate(labels[3], (250, 820, 900, 925), MUTED, size=27)
    surface.plate(labels[4], (1020, 820, 1670, 925), MUTED, size=27)
    draw.line((960, 400, 960, 455), fill=GRID, width=6)
    draw.line((960, 575, 960, 630), fill=GRID, width=6)
    draw.line((960, 730, 960, 785), fill=GRID, width=6)
    draw.line((575, 785, 1345, 785), fill=GRID, width=6)
    draw.line((575, 785, 575, 820), fill=GRID, width=6)
    draw.line((1345, 785, 1345, 820), fill=GRID, width=6)
    draw.line((1530, 310, 1595, 375), fill=RED, width=10)
    draw.line((1595, 310, 1530, 375), fill=RED, width=10)


def draw_panel_08(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (175, 300, 740, 405), MUTED, size=25)
    surface.plate(labels[1], (1180, 300, 1745, 405), BLUE, size=25)
    draw.ellipse((810, 325, 1110, 625), fill=PANEL_2, outline=CYAN, width=6)
    arrow(draw, (860, 590), (610, 700), AMBER)
    arrow(draw, (1060, 590), (1310, 700), RED)
    surface.plate(labels[2], (150, 680, 780, 790), AMBER, size=29)
    surface.plate(labels[3], (1140, 680, 1770, 810), RED, size=27, max_lines=3)
    draw.ellipse((390, 825, 510, 945), outline=AMBER, width=12)
    draw.line((430, 880, 470, 920), fill=AMBER, width=10)
    draw.line((470, 880, 430, 920), fill=AMBER, width=10)
    draw.line((1410, 845, 1510, 945), fill=RED, width=14)
    draw.line((1510, 845, 1410, 945), fill=RED, width=14)
    surface.plate(labels[4], (450, 945, 1470, 1020), WHITE, size=27)


DRAWERS: dict[str, Callable[[TextSurface, list[str]], dict[str, float | bool] | None]] = {
    "01": draw_panel_01,
    "02": draw_panel_02,
    "03": draw_panel_03,
    "04": draw_panel_04,
    "05": draw_panel_05,
    "06": draw_panel_06,
    "07": draw_panel_07,
    "08": draw_panel_08,
}


def render_all_cards(output_root: Path) -> dict:
    frozen = pipeline.load_frozen_inputs()
    cards_dir = output_root / "cards"
    qa_dir = output_root / "qa"
    cards_dir.mkdir(parents=True, exist_ok=True)
    qa_dir.mkdir(parents=True, exist_ok=True)
    records = []
    panel_03_geometry: dict | None = None
    for panel in frozen["panels"]:
        image, surface, support = base_card(panel)
        result = DRAWERS[panel["id"]](surface, support)
        if surface.emitted != panel["viewer_text_closed_world"]:
            raise RuntimeError(
                f"panel {panel['id']} text projection mismatch: "
                f"{surface.emitted!r} != {panel['viewer_text_closed_world']!r}"
            )
        if panel["id"] == "03":
            if not isinstance(result, dict):
                raise RuntimeError("panel 03 renderer returned no geometry receipt")
            panel_03_geometry = result
        path = cards_dir / f"card-{panel['id']}.png"
        image.save(path, format="PNG", optimize=False, compress_level=9)
        records.append(
            {
                "id": panel["id"],
                "path": str(path.relative_to(output_root)),
                "sha256": sha256(path),
                "heading": panel["assertion_heading"],
                "permitted_text": panel["viewer_text_closed_world"],
                "emitted_text": surface.emitted,
                "text_contract_status": "PASS_EXACT_CLOSED_WORLD",
            }
        )
    if panel_03_geometry is None:
        raise RuntimeError("panel 03 geometry receipt missing")

    thumb_w, thumb_h = 480, 270
    sheet = Image.new("RGB", (thumb_w * 4, thumb_h * 2), BG)
    for index, record in enumerate(records):
        card = Image.open(output_root / record["path"]).convert("RGB")
        thumb = ImageOps.fit(card, (thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(thumb, ((index % 4) * thumb_w, (index // 4) * thumb_h))
    contact = qa_dir / "source-contact-sheet.png"
    sheet.save(contact, format="PNG", optimize=False, compress_level=9)

    receipt = {
        "status": "PASS_SOURCE_CARD_RENDER",
        "resolution": [W, H],
        "font_path": FONT_PATH,
        "font_sha256": sha256(Path(FONT_PATH)),
        "cards": records,
        "panel_03_geometry": panel_03_geometry,
        "source_contact_sheet": str(contact.relative_to(output_root)),
        "source_contact_sheet_sha256": sha256(contact),
    }
    audit_path = qa_dir / "card-text-and-geometry-audit.json"
    audit_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return receipt


def main() -> int:
    receipt = render_all_cards(pipeline.BUILD)
    print(json.dumps({"status": receipt["status"], "cards": len(receipt["cards"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
