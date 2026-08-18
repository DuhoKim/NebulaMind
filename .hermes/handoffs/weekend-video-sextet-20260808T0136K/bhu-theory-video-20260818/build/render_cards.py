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
    surface.plate(labels[0], (360, 290, 1560, 405), MUTED, size=30)
    surface.plate(labels[1], (360, 435, 1560, 550), MUTED, size=28)
    surface.plate(labels[2], (300, 610, 1620, 730), CYAN, size=31)
    surface.plate(labels[3], (300, 790, 1620, 925), AMBER, size=33)


def draw_panel_02(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    rounded(draw, (100, 280, 860, 920))
    draw.ellipse((230, 345, 730, 845), outline=PURPLE, width=14)
    draw.arc((190, 305, 770, 885), 205, 510, fill=AMBER, width=10)
    arrow(draw, (690, 410), (720, 465), AMBER, width=8)
    draw.ellipse((350, 465, 610, 725), fill=PANEL_2, outline=CYAN, width=10)
    draw.line((480, 375, 480, 810), fill=MUTED, width=5)
    for y, direction in ((535, 1), (605, -1), (675, 1)):
        draw.arc((410, y - 30, 550, y + 30), 190 if direction > 0 else 10, 350 if direction > 0 else 170, fill=BLUE, width=6)
    surface.plate(labels[0], (1070, 285, 1810, 385), BLUE, size=25)
    surface.plate(labels[1], (1070, 420, 1810, 525), PURPLE, size=27)
    surface.plate(labels[2], (1070, 555, 1810, 670), CYAN, size=24, max_lines=2)
    surface.plate(labels[3], (1070, 700, 1810, 810), AMBER, size=23, max_lines=2)
    surface.plate(labels[4], (1070, 840, 1810, 930), MUTED, size=23, max_lines=2)


def draw_panel_03(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (250, 285, 845, 375), BLUE, size=25)
    surface.plate(labels[1], (1075, 285, 1670, 375), PURPLE, size=25)
    for left, color, twist in ((330, BLUE, 1), (1155, PURPLE, -1)):
        draw.line((left, 450, left, 720), fill=color, width=7)
        draw.line((left + 430, 450, left + 430, 720), fill=color, width=7)
        draw.line((left, 720, left + 430, 720), fill=color, width=7)
        for index in range(8):
            x = left + 65 + (index % 4) * 100
            y = 520 + (index // 4) * 105
            draw.arc((x - 28, y - 28, x + 28, y + 28), 25 if twist > 0 else 205, 300 if twist > 0 else 480, fill=WHITE, width=5)
    surface.plate(labels[2], (650, 765, 1270, 850), CYAN, size=27)
    surface.plate(labels[3], (180, 875, 1010, 970), AMBER, size=23, max_lines=2)
    surface.plate(labels[4], (1060, 875, 1740, 970), RED, size=23, max_lines=2)
    surface.plate(labels[5], (610, 400, 1310, 475), GREEN, size=26)


def draw_panel_04(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    rounded(draw, (100, 280, 1820, 610))
    draw.ellipse((260, 335, 1660, 560), fill=PANEL_2, outline=BLUE, width=6)
    rng = random.Random(404)
    for _ in range(180):
        angle = rng.random() * math.tau
        radius = math.sqrt(rng.random())
        x = 960 + math.cos(angle) * 650 * radius
        y = 447 + math.sin(angle) * 95 * radius
        value = rng.randrange(70, 180)
        draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill=(value, 80, 210 - value // 2))
    draw.arc((760, 345, 1160, 550), 205, 500, fill=CYAN, width=8)
    surface.plate(labels[0], (680, 295, 1240, 365), BLUE, size=22)
    surface.plate(labels[1], (240, 660, 1680, 755), GREEN, size=27)
    surface.plate(labels[2], (240, 785, 1680, 895), AMBER, size=26, max_lines=2)
    surface.plate(labels[3], (480, 925, 1440, 1000), MUTED, size=24)


def draw_panel_05(surface: TextSurface, labels: list[str]) -> None:
    surface.plate(labels[0], (360, 290, 1560, 390), BLUE, size=27)
    surface.plate(labels[1], (360, 420, 1560, 520), MUTED, size=29)
    surface.plate(labels[2], (360, 550, 1560, 650), MUTED, size=29)
    surface.plate(labels[3], (300, 705, 1620, 830), CYAN, size=34)
    surface.plate(labels[4], (300, 865, 1620, 975), AMBER, size=28)


def draw_panel_06(surface: TextSurface, labels: list[str]) -> dict[str, object]:
    draw = surface.draw
    surface.plate(labels[0], (100, 285, 860, 385), BLUE, size=25)
    surface.plate(labels[1], (100, 420, 860, 520), GREEN, size=27)
    surface.plate(labels[2], (100, 555, 860, 655), AMBER, size=27)
    surface.plate(labels[3], (100, 700, 860, 810), RED, size=27, max_lines=2)
    surface.plate(labels[4], (100, 850, 860, 950), MUTED, size=25)
    x0, x1 = 1160, 1540
    y_ticks = [310, 425, 540, 655, 770, 885]
    draw.line((x0, y_ticks[0], x0, y_ticks[-1]), fill=WHITE, width=6)
    for y in y_ticks:
        draw.line((x0 - 24, y, x0 + 24, y), fill=WHITE, width=5)
    for index in range(4):
        top = y_ticks[index] + 22
        bottom = y_ticks[index + 1] - 22
        draw.rounded_rectangle((x0 + 70, top, x1, bottom), radius=15, fill=PANEL_2, outline=CYAN, width=4)
        draw.line((x0 + 115, (top + bottom) // 2, x1 - 45, (top + bottom) // 2), fill=CYAN, width=6)
        arrow(draw, (x1 - 80, (top + bottom) // 2), (x1 - 45, (top + bottom) // 2), CYAN, width=6)
    surface.plate(labels[5], (1240, 265, 1810, 365), GREEN, size=25)
    allowed_y = int(y_ticks[4] + 0.301 * (y_ticks[5] - y_ticks[4]))
    draw.line((x0 - 20, allowed_y, 1230, allowed_y), fill=AMBER, width=7)
    surface.plate(labels[6], (1240, allowed_y - 50, 1810, allowed_y + 50), AMBER, size=25)
    return {
        "tenfold_tick_count": len(y_ticks),
        "explicit_tenfold_step_blocks": 4,
        "needed_tick_power": -2,
        "allowed_value": 5e-7,
        "allowed_between_tick_powers": [-6, -7],
        "unlabeled_log_spacing_used": False,
    }


def draw_panel_07(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (200, 280, 920, 375), RED, size=25)
    surface.plate(labels[1], (1000, 280, 1720, 375), BLUE, size=25)
    for index in range(18):
        col, row = index % 6, index // 6
        x, y = 210 + col * 250, 440 + row * 135
        color = BLUE if index == 0 else GRID
        draw.rounded_rectangle((x, y, x + 190, y + 95), radius=15, fill=PANEL_2, outline=color, width=6)
        draw.ellipse((x + 72, y + 24, x + 118, y + 70), outline=color, width=4)
    surface.plate(labels[2], (300, 865, 1620, 950), AMBER, size=28)
    surface.plate(labels[3], (180, 970, 970, 1045), RED, size=22)
    surface.plate(labels[4], (1010, 970, 1740, 1045), MUTED, size=23)


def draw_panel_08(surface: TextSurface, labels: list[str]) -> None:
    surface.plate(labels[0], (300, 285, 1620, 400), RED, size=31)
    surface.plate(labels[1], (300, 440, 1620, 545), MUTED, size=29)
    surface.plate(labels[2], (300, 580, 1620, 685), BLUE, size=29)
    surface.plate(labels[3], (300, 720, 1620, 825), AMBER, size=28)
    surface.plate(labels[4], (260, 870, 1660, 985), CYAN, size=29)


def draw_panel_09(surface: TextSurface, labels: list[str]) -> None:
    draw = surface.draw
    surface.plate(labels[0], (100, 290, 900, 405), GREEN, size=25)
    surface.plate(labels[1], (100, 450, 900, 565), AMBER, size=24)
    surface.plate(labels[2], (100, 610, 900, 725), CYAN, size=24)
    surface.plate(labels[3], (100, 770, 900, 900), BLUE, size=23, max_lines=3)
    rounded(draw, (1000, 290, 1820, 900))
    draw.arc((1320, 330, 1500, 500), 180, 360, fill=WHITE, width=12)
    draw.line((1410, 415, 1410, 715), fill=WHITE, width=10)
    draw.ellipse((1355, 625, 1465, 735), outline=AMBER, width=10)
    draw.line((1410, 680, 1515, 785), fill=AMBER, width=12)
    draw.line((1515, 785, 1585, 715), fill=AMBER, width=12)
    surface.plate(labels[4], (1090, 790, 1730, 875), MUTED, size=25)


def draw_panel_10(surface: TextSurface, labels: list[str]) -> None:
    surface.plate(labels[0], (360, 290, 1560, 390), MUTED, size=29)
    surface.plate(labels[1], (360, 420, 1560, 520), MUTED, size=29)
    surface.plate(labels[2], (360, 550, 1560, 650), BLUE, size=29)
    surface.plate(labels[3], (300, 705, 1620, 830), RED, size=33)
    surface.plate(labels[4], (260, 870, 1660, 995), AMBER, size=34)


DRAWERS: dict[str, Callable[[TextSurface, list[str]], dict[str, object] | None]] = {
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
