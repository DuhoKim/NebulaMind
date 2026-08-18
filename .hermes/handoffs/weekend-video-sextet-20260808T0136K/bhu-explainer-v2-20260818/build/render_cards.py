#!/usr/bin/env python3
"""Render ten deterministic 1920x1080 PIL infographic cards."""
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
    surface.plate(labels[0], (340, 300, 1580, 405), MUTED, size=30)
    surface.plate(labels[1], (340, 430, 1580, 535), MUTED, size=28)
    surface.plate(labels[2], (300, 585, 1620, 690), CYAN, size=30)
    arrow(draw, (960, 535), (960, 580), CYAN)
    surface.plate(labels[3], (180, 770, 910, 910), AMBER, size=31)
    surface.plate(labels[4], (1010, 770, 1740, 910), RED, size=31)


def draw_panel_02(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (100, 340, 720, 480), BLUE, size=27, max_lines=3)
    surface.plate(labels[1], (100, 535, 720, 690), MUTED, size=23, max_lines=4)
    draw.ellipse((770, 455, 850, 535), fill=CYAN)
    for index in range(5):
        y = 350 + index * 105
        arrow(draw, (850, 495), (1130, y), (BLUE, CYAN, MUTED, PURPLE, AMBER)[index], width=4)
    surface.plate(labels[2], (1130, 315, 1780, 475), CYAN, size=34, max_lines=3)
    surface.plate(labels[3], (1130, 650, 1780, 800), MUTED, size=32, max_lines=3)


def draw_panel_03(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    nodes = [(960, 355), (1390, 650), (530, 650)]
    boxes = [(600, 290, 1320, 420), (1110, 585, 1720, 715), (200, 585, 810, 715)]
    colors = [CYAN, PURPLE, BLUE]
    for index, (box, color) in enumerate(zip(boxes, colors)):
        surface.plate(labels[index], box, color, size=25, max_lines=3)
    arrow(draw, (1250, 430), (1375, 565), CYAN)
    arrow(draw, (1110, 710), (830, 710), CYAN)
    arrow(draw, (545, 565), (780, 425), CYAN)
    draw.ellipse((885, 470, 1035, 620), outline=CYAN, width=6)
    surface.plate(labels[3], (370, 815, 1550, 935), WHITE, size=28, max_lines=3)


def draw_panel_04(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (350, 290, 1570, 395), BLUE, size=29)
    draw.polygon(((420, 455), (1500, 455), (1270, 680), (650, 680)), fill=PANEL_2, outline=CYAN)
    surface.plate(labels[1], (470, 485, 1450, 625), PURPLE, size=25, max_lines=3)
    arrow(draw, (960, 680), (960, 745), WHITE)
    surface.plate(labels[2], (390, 760, 1530, 865), AMBER, size=28)
    draw.ellipse((1640, 700, 1760, 820), outline=WHITE, width=5)
    for angle in range(0, 360, 45):
        radians = math.radians(angle)
        draw.line((1700 + 62 * math.cos(radians), 760 + 62 * math.sin(radians), 1700 + 92 * math.cos(radians), 760 + 92 * math.sin(radians)), fill=WHITE, width=3)
    surface.plate(labels[3], (450, 900, 1470, 990), CYAN, size=27)


def draw_panel_05(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (120, 410, 820, 610), BLUE, size=28, max_lines=4)
    surface.plate(labels[1], (875, 455, 1045, 565), WHITE, size=42)
    surface.plate(labels[2], (1100, 410, 1800, 610), BLUE, size=27, max_lines=4)
    draw.line((960, 330, 960, 440), fill=WHITE, width=5)
    draw.line((820, 510, 875, 510), fill=WHITE, width=5)
    draw.line((1045, 510, 1100, 510), fill=WHITE, width=5)
    surface.plate(labels[3], (350, 765, 1570, 890), CYAN, size=34)


def draw_panel_06(surface: TextSurface, labels: list[str]) -> dict[str, float | bool]:
    draw = surface.draw
    x_axis, y_bottom, y_top, low, high = 470, 905, 300, 1.4, 2.22
    def y_of(value: float) -> float:
        return y_bottom - (value - low) / (high - low) * (y_bottom - y_top)
    draw.line((x_axis, y_top, x_axis, y_bottom), fill=WHITE, width=5)
    y_15, y_20 = y_of(1.5), y_of(2.0)
    draw.line((x_axis, y_15, 900, y_15), fill=RED, width=6)
    for x in range(x_axis, 900, 24):
        draw.line((x, y_20, min(x + 12, 900), y_20), fill=AMBER, width=5)
    for value, x in ((1.66, 610), (1.75, 700), (1.84, 790)):
        y = y_of(value)
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill=RED, outline=WHITE, width=2)
    center, one_sigma_low, one_sigma_high, strict_visual_low = 2.08, 2.01, 2.15, 1.94
    y_center, y_low_1, y_high_1, y_strict_low = map(y_of, (center, one_sigma_low, one_sigma_high, strict_visual_low))
    for index in range(14):
        fraction = index / 13
        y = y_center + fraction * (y_strict_low - y_center)
        alpha = 130 * (1 - fraction)
        color = tuple(round(BG[i] * (1 - alpha / 255) + PURPLE[i] * alpha / 255) for i in range(3))
        draw.ellipse((676, y - 7, 764, y + 7), fill=color)
    draw.line((720, y_high_1, 720, y_low_1), fill=WHITE, width=10)
    draw.line((698, y_high_1, 742, y_high_1), fill=WHITE, width=6)
    draw.line((698, y_low_1, 742, y_low_1), fill=WHITE, width=6)
    draw.ellipse((705, y_center - 15, 735, y_center + 15), fill=WHITE)
    surface.plate(labels[0], (940, 285, 1810, 395), CYAN, size=25)
    surface.plate(labels[1], (940, 420, 1810, 510), WHITE, size=24)
    surface.plate(labels[2], (940, 530, 1810, 620), PURPLE, size=24)
    surface.plate(labels[3], (940, 650, 1810, 755), RED, size=24)
    surface.plate(labels[4], (940, 790, 1810, 900), RED, size=26)
    return {"threshold": 2.0, "center": center, "one_sigma_low": one_sigma_low, "one_sigma_high": one_sigma_high, "strict_95_4_visual_crosses_threshold": strict_visual_low < 2.0, "strict_95_4_hard_lower_endpoint_drawn": False}


def draw_panel_07(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (120, 285, 550, 385), CYAN, size=28)
    surface.plate(labels[1], (600, 285, 1800, 385), MUTED, size=25)
    x0, x1, axis_y = 220, 1690, 755
    draw.line((x0, axis_y, x1, axis_y), fill=WHITE, width=5)
    x4, x193, x186, x200 = [x0 + value / 22 * (x1 - x0) for value in (4, 19.3, 18.6, 20.0)]
    draw.line((x4, 485, x4, 800), fill=WHITE, width=6)
    draw.rounded_rectangle((x0, 610, x193, 680), radius=18, fill=RED)
    draw.line((x186, 645, x200, 645), fill=WHITE, width=8)
    draw.line((x186, 625, x186, 665), fill=WHITE, width=5)
    draw.line((x200, 625, x200, 665), fill=WHITE, width=5)
    surface.plate(labels[2], (180, 430, 630, 525), WHITE, size=25)
    surface.plate(labels[3], (760, 455, 1740, 555), RED, size=28)
    surface.plate(labels[4], (780, 790, 1740, 885), RED, size=27)
    surface.plate(labels[5], (450, 925, 1470, 1000), MUTED, size=23)


def draw_panel_08(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    boxes = [(130, 300, 900, 410), (130, 475, 900, 585), (130, 650, 900, 760)]
    for index, box in enumerate(boxes):
        surface.plate(labels[index], box, (CYAN, BLUE, MUTED)[index], size=27)
        if index < 2:
            arrow(draw, (515, box[3] + 8), (515, boxes[index + 1][1] - 8), CYAN, width=4)
    draw.arc((165, 245, 295, 355), start=180, end=360, fill=WHITE, width=10)
    draw.rectangle((170, 295, 290, 375), outline=WHITE, width=8)
    surface.plate(labels[3], (1050, 385, 1800, 535), AMBER, size=27, max_lines=3)
    surface.plate(labels[4], (980, 675, 1810, 785), WHITE, size=27)
    surface.plate(labels[5], (500, 880, 1420, 980), RED, size=32)


def draw_panel_09(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (490, 290, 1430, 390), RED, size=24)
    surface.plate(labels[1], (100, 500, 800, 625), AMBER, size=24, max_lines=3)
    surface.plate(labels[2], (1120, 500, 1820, 625), RED, size=24, max_lines=3)
    surface.plate(labels[3], (1120, 700, 1820, 805), MUTED, size=26)
    surface.plate(labels[4], (300, 875, 1620, 980), MUTED, size=28)
    draw.line((960, 390, 960, 450), fill=GRID, width=5)
    draw.line((450, 450, 1470, 450), fill=GRID, width=5)
    draw.line((450, 450, 450, 500), fill=GRID, width=5)
    draw.line((1470, 450, 1470, 500), fill=GRID, width=5)
    draw.line((1470, 625, 1470, 700), fill=GRID, width=5)
    draw.line((960, 805, 960, 875), fill=GRID, width=5)
    draw.line((500, 338, 1420, 338), fill=RED, width=8)


def draw_panel_10(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (390, 285, 1530, 380), MUTED, size=28)
    surface.plate(labels[1], (390, 415, 1530, 510), CYAN, size=28)
    surface.plate(labels[2], (160, 620, 900, 750), AMBER, size=30)
    surface.plate(labels[3], (1020, 620, 1760, 750), RED, size=29, max_lines=3)
    surface.plate(labels[4], (230, 865, 1690, 990), RED, size=33, max_lines=2)
    draw.line((960, 510, 960, 585), fill=GRID, width=5)
    draw.line((530, 585, 1390, 585), fill=GRID, width=5)
    draw.line((530, 585, 530, 620), fill=GRID, width=5)
    draw.line((1390, 585, 1390, 620), fill=GRID, width=5)


DRAWERS: dict[str, Callable[[TextSurface, list[str]], dict[str, float | bool] | None]] = {
    "01": draw_panel_01,
    "02": draw_panel_02,
    "03": draw_panel_03,
    "04": draw_panel_04,
    "05": draw_panel_05,
    "06": draw_panel_06,
    "07": draw_panel_07,
    "08": draw_panel_08,
    "09": draw_panel_09,
    "10": draw_panel_10,
}


def render_all_cards(output_root: Path) -> dict:
    frozen = pipeline.load_frozen_inputs()
    cards_dir = output_root / "cards"
    qa_dir = output_root / "qa"
    cards_dir.mkdir(parents=True, exist_ok=True)
    qa_dir.mkdir(parents=True, exist_ok=True)
    records = []
    panel_06_geometry: dict | None = None
    for panel in frozen["panels"]:
        image, surface, support = base_card(panel)
        result = DRAWERS[panel["id"]](surface, support)
        if surface.emitted != panel["viewer_text_closed_world"]:
            raise RuntimeError(
                f"panel {panel['id']} text projection mismatch: "
                f"{surface.emitted!r} != {panel['viewer_text_closed_world']!r}"
            )
        if panel["id"] == "06":
            if not isinstance(result, dict):
                raise RuntimeError("panel 06 renderer returned no geometry receipt")
            panel_06_geometry = result
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
    if panel_06_geometry is None:
        raise RuntimeError("panel 06 geometry receipt missing")

    thumb_w, thumb_h = 480, 270
    sheet = Image.new("RGB", (thumb_w * 4, thumb_h * 3), BG)
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
        "panel_06_geometry": panel_06_geometry,
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
