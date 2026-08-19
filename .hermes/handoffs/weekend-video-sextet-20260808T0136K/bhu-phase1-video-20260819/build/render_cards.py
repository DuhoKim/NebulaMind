#!/usr/bin/env python3
"""Render ten deterministic 1920x1080 Phase 1 explainer cards."""
from __future__ import annotations

import functools
import hashlib
import json
import math
import random
from pathlib import Path
from typing import Callable

from fontTools.ttLib import TTCollection, TTFont
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
HELVETICA = Path("/System/Library/Fonts/Helvetica.ttc")
DEJAVU = Path("/Users/duhokim/Library/Python/3.9/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf")
REQUIRED_GLYPHS = "Ω²⁹⁻"


def font_codepoints(path: Path, index: int = 0) -> set[int]:
    fonts = TTCollection(path).fonts if path.suffix.lower() == ".ttc" else [TTFont(path)]
    font_obj = fonts[index]
    cmap_table = font_obj["cmap"]  # pyright: ignore[reportAssignmentType]
    return set().union(*(table.cmap.keys() for table in cmap_table.tables))  # type: ignore[attr-defined]


def choose_font() -> tuple[Path, str, dict[str, bool]]:
    helvetica_support = font_codepoints(HELVETICA)
    support = {glyph: ord(glyph) in helvetica_support for glyph in REQUIRED_GLYPHS}
    if all(support.values()):
        return HELVETICA, "Helvetica index 0 contains every required Ω/²/⁹/⁻ glyph", support
    if not DEJAVU.is_file():
        raise RuntimeError("Helvetica lacks required glyphs and DejaVu Sans fallback is unavailable")
    dejavu_support = font_codepoints(DEJAVU)
    fallback = {glyph: ord(glyph) in dejavu_support for glyph in REQUIRED_GLYPHS}
    if not all(fallback.values()):
        raise RuntimeError(f"DejaVu Sans fallback lacks required glyphs: {fallback}")
    return DEJAVU, "Helvetica lacked a required glyph; selected DejaVu Sans fallback", fallback


FONT_PATH, FONT_CHOICE_REASON, GLYPH_SUPPORT = choose_font()


@functools.lru_cache(maxsize=None)
def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    index = 1 if bold and FONT_PATH == HELVETICA else 0
    return ImageFont.truetype(str(FONT_PATH), size, index=index)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, fill=PANEL, outline=GRID, width=3, radius=24) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color=CYAN, width: int = 6) -> None:
    draw.line((*start, *end), fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    for offset in (2.55, -2.55):
        draw.line((end[0], end[1], end[0] + 18 * math.cos(angle + offset), end[1] + 18 * math.sin(angle + offset)), fill=color, width=width)


def starfield(image: Image.Image) -> None:
    draw = ImageDraw.Draw(image)
    rng = random.Random(20260819)
    for _ in range(180):
        x, y = rng.randrange(W), rng.randrange(H)
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

    def wrap(self, text: str, box: tuple[int, int, int, int], size: int, *, color=WHITE, bold=False, align="center", max_lines: int | None = None) -> None:
        self._record(text)
        face = font(size, bold)
        words = text.split()
        width = box[2] - box[0]
        lines: list[str] = []
        current = ""
        for word in words:
            trial = (current + " " + word).strip()
            if self.draw.textlength(trial, font=face) <= width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        if max_lines is not None and len(lines) > max_lines:
            raise RuntimeError(f"text exceeds {max_lines} lines: {text!r} -> {lines!r}")
        step = size + 9
        total = len(lines) * step - 9
        y = box[1] + max(0.0, (box[3] - box[1] - total) / 2)
        for line in lines:
            line_width = self.draw.textlength(line, font=face)
            x = box[0] if align == "left" else box[2] - line_width if align == "right" else box[0] + (width - line_width) / 2
            self.draw.text((x, y), line, font=face, fill=color)
            y += step

    def plate(self, text: str, box: tuple[int, int, int, int], color, *, size=24, max_lines=2) -> None:
        rounded(self.draw, box, fill=PANEL_2, outline=color, width=3, radius=17)
        self.wrap(text, (box[0] + 18, box[1] + 8, box[2] - 18, box[3] - 8), size, color=color, bold=True, max_lines=max_lines)


def base_card(panel: dict) -> tuple[Image.Image, TextSurface, list[str]]:
    image = Image.new("RGB", (W, H), BG)
    starfield(image)
    surface = TextSurface(image, panel["viewer_text_closed_world"])
    surface.draw.line((82, 246, W - 82, 246), fill=GRID, width=3)
    surface.wrap(panel["viewer_text_closed_world"][0], (110, 56, W - 110, 224), 48, bold=True, max_lines=2)
    return image, surface, panel["viewer_text_closed_world"][1:]


def stacked(surface: TextSurface, labels: list[str], box: tuple[int, int, int, int], colors: list[tuple[int, int, int]], size=24) -> None:
    gap = 14
    height = (box[3] - box[1] - gap * (len(labels) - 1)) // len(labels)
    y = box[1]
    for index, label in enumerate(labels):
        surface.plate(label, (box[0], y, box[2], y + height), colors[index % len(colors)], size=size, max_lines=3)
        y += height + gap


def draw_panel_01(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (300, 285, 1620, 980), [MUTED, MUTED, CYAN, AMBER, GREEN], size=29)
    return {"opening_scope_visible": True, "verdict_visible": True}


def draw_panel_02(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (100, 285, 920, 980), [BLUE, PURPLE, GREEN, AMBER, CYAN, MUTED], size=22)
    draw = surface.draw
    rounded(draw, (1010, 285, 1820, 980))
    counts = [(8, GREEN), (4, RED), (6, AMBER), (3, PURPLE), (1, MUTED), (1, BLUE)]
    palette = [color for count, color in counts for _ in range(count)]
    for index, color in enumerate(palette):
        col, row = index % 6, index // 6
        x, y = 1095 + col * 106, 390 + row * 125
        draw.rounded_rectangle((x, y, x + 74, y + 74), radius=12, fill=color, outline=WHITE, width=2)
    return {"verdict_block_count": len(palette), "verdict_counts": [count for count, _ in counts]}


def draw_panel_03(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels[:8], (80, 280, 930, 1000), [BLUE, AMBER, CYAN, PURPLE, RED, AMBER, MUTED, GREEN], size=20)
    draw = surface.draw
    rounded(draw, (1010, 280, 1840, 1000))
    surface.plate(labels[8], (1060, 305, 1790, 405), RED, size=25)
    surface.plate(labels[9], (1060, 875, 1790, 975), BLUE, size=24)
    # Two separate readouts: 9 tenfold steps for horn 1 and 18 for horn 2.
    for index in range(10):
        y = 445 + index * 20
        draw.line((1190, y, 1420, y), fill=RED if index in (0, 9) else GRID, width=5)
    for index in range(19):
        y = 660 + index * 10
        draw.line((1435, y, 1665, y), fill=BLUE if index in (0, 18) else GRID, width=4)
    draw.line((1305, 445, 1305, 625), fill=RED, width=5)
    draw.line((1550, 660, 1550, 840), fill=BLUE, width=5)
    return {"horn_1_tenfold_steps": 9, "horn_2_tenfold_steps": 18, "separate_quantity_readouts": True, "horn_2_label": labels[9], "unlabeled_log_spacing_used": False}


def draw_panel_04(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (90, 285, 930, 990), [BLUE, CYAN, AMBER, RED, PURPLE, MUTED], size=22)
    draw = surface.draw
    rounded(draw, (1020, 285, 1825, 990))
    y = 640
    draw.line((1110, y, 1735, y), fill=WHITE, width=8)
    draw.polygon([(1422, y), (1380, 790), (1465, 790)], fill=GRID, outline=WHITE)
    draw.ellipse((1100, y - 28, 1156, y + 28), fill=PURPLE)
    draw.ellipse((1675, y - 35, 1745, y + 35), fill=AMBER)
    draw.line((1128, y, 1710, y), fill=CYAN, width=4)
    for index in range(47):
        x = 1128 + index * (582 / 46)
        draw.line((x, y - 14, x, y + 14), fill=GRID, width=2)
    return {"sigma_interval_count": 46, "continuous_linear_scale": True}


def draw_panel_05(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (300, 275, 1620, 1000), [BLUE, MUTED, CYAN, PURPLE, GREEN, AMBER, RED], size=25)
    return {"strict_model_constraints_listed": 7}


def draw_panel_06(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (90, 285, 900, 980), [BLUE, GREEN, AMBER, CYAN, MUTED], size=23)
    draw = surface.draw
    rounded(draw, (990, 285, 1830, 980))
    xs = [1100, 1400, 1710]
    radii = [120, 80, 42]
    colors = [AMBER, GREEN, MUTED]
    for x, radius, color in zip(xs, radii, colors):
        draw.ellipse((x - radius, 590 - radius, x + radius, 590 + radius), outline=color, width=9)
        draw.arc((x - radius - 20, 570 - radius, x + radius + 20, 610 + radius), 210, 510, fill=color, width=7)
    arrow(draw, (1225, 590), (1305, 590), CYAN)
    arrow(draw, (1485, 590), (1605, 590), CYAN)
    draw.rounded_rectangle((1645, 430, 1785, 750), radius=18, outline=RED, width=5)
    return {"era_count": 3, "radiation_fade_radius": 120, "matter_fade_radius": 80, "inflation_quarantined": True}


def draw_panel_07(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (70, 270, 940, 1015), [BLUE, CYAN, GREEN, PURPLE, AMBER, AMBER, GREEN, MUTED, RED], size=19)
    draw = surface.draw
    rounded(draw, (1010, 285, 1840, 1000))
    center = (1425, 650)
    for index, angle in enumerate((210, 270, 330, 30)):
        rad = math.radians(angle)
        node = (center[0] + 270 * math.cos(rad), center[1] + 260 * math.sin(rad))
        draw.ellipse((node[0] - 38, node[1] - 38, node[0] + 38, node[1] + 38), fill=PANEL_2, outline=[BLUE, GREEN, PURPLE, AMBER][index], width=7)
        arrow(draw, node, center, [BLUE, GREEN, PURPLE, AMBER][index], width=5)
    draw.arc((1190, 410, 1660, 880), 200, 340, fill=CYAN, width=16)
    for fraction, color in ((0.0, MUTED), ((7.2 - 1.4) / (12.8 - 1.4), AMBER), (1.0, MUTED)):
        angle = math.radians(200 + 140 * fraction)
        x = center[0] + 230 * math.cos(angle)
        y = center[1] + 230 * math.sin(angle)
        draw.ellipse((x - 14, y - 14, x + 14, y + 14), fill=color)
    return {"coefficient": 7.2, "bracket": [1.4, 12.8], "ingredient_nodes": 4}


def draw_panel_08(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (70, 275, 950, 1010), [RED, MUTED, BLUE, AMBER, CYAN, PURPLE, GREEN], size=20)
    draw = surface.draw
    rounded(draw, (1010, 280, 1840, 1005))
    tile = 5
    gap = 1
    cols, rows = 120, 100
    start_x, start_y = 1065, 335
    for index in range(cols * rows):
        col, row = index % cols, index // cols
        x, y = start_x + col * (tile + gap), start_y + row * (tile + gap)
        color = CYAN if index == 0 else GRID
        draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=color)
    return {"required_universe_tiles": cols * rows, "highlighted_existing_tiles": 1, "ghosted_required_tiles": cols * rows - 1}


def draw_panel_09(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels[:7], (65, 270, 955, 1015), [GREEN, AMBER, CYAN, BLUE, PURPLE, MUTED, RED], size=20)
    draw = surface.draw
    rounded(draw, (1010, 285, 1840, 1000))
    surface.plate(labels[7], (1065, 315, 1790, 405), BLUE, size=24)
    surface.plate(labels[8], (1065, 875, 1790, 965), PURPLE, size=24)
    for x, steps, color in ((1260, 22, BLUE), (1590, 30, PURPLE)):
        draw.line((x, 455, x, 825), fill=color, width=7)
        for index in range(steps + 1):
            y = 825 - index * (370 / steps)
            length = 85 if index in (0, steps) else 42
            draw.line((x - length, y, x + length, y), fill=color if index in (0, steps) else GRID, width=4)
    return {"supermassive_threshold_power": 22, "stellar_threshold_power": 30, "floors_exceeded": True}


def draw_panel_10(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (280, 275, 1640, 1005), [MUTED, MUTED, BLUE, CYAN, PURPLE, AMBER, GREEN], size=25)
    return {"ends_on_verdict": labels[-1] == "THE NUMBER SAYS THE ROUTE STAYS CLOSED"}


DRAWERS: dict[str, Callable[[TextSurface, list[str]], dict]] = {
    "01": draw_panel_01, "02": draw_panel_02, "03": draw_panel_03, "04": draw_panel_04, "05": draw_panel_05,
    "06": draw_panel_06, "07": draw_panel_07, "08": draw_panel_08, "09": draw_panel_09, "10": draw_panel_10,
}


def render_all_cards(output_root: Path) -> dict:
    frozen = pipeline.load_frozen_inputs()
    cards_dir, qa_dir = output_root / "cards", output_root / "qa"
    cards_dir.mkdir(parents=True, exist_ok=True)
    qa_dir.mkdir(parents=True, exist_ok=True)
    records, geometry = [], {}
    for panel in frozen["panels"]:
        image, surface, labels = base_card(panel)
        geometry[f"panel_{panel['id']}"] = DRAWERS[panel["id"]](surface, labels)
        if surface.emitted != panel["viewer_text_closed_world"]:
            raise RuntimeError(f"panel {panel['id']} text projection mismatch: {surface.emitted!r} != {panel['viewer_text_closed_world']!r}")
        path = cards_dir / f"card-{panel['id']}.png"
        image.save(path, format="PNG", optimize=False, compress_level=9)
        records.append({"id": panel["id"], "path": str(path.relative_to(output_root)), "sha256": sha256(path), "heading": panel["assertion_heading"], "permitted_text": panel["viewer_text_closed_world"], "emitted_text": surface.emitted, "text_contract_status": "PASS_EXACT_CLOSED_WORLD"})
    sheet = Image.new("RGB", (1920, 810), BG)
    for index, record in enumerate(records):
        card = Image.open(output_root / record["path"]).convert("RGB")
        sheet.paste(ImageOps.fit(card, (480, 270), Image.Resampling.LANCZOS), ((index % 4) * 480, (index // 4) * 270))
    contact = qa_dir / "source-contact-sheet.png"
    sheet.save(contact, format="PNG", optimize=False, compress_level=9)
    equation_projection = {
        "Λ = 3Ω²/c²": "Λ = 3Ω²/c²" in records[2]["emitted_text"],
        "w = +1/3": "w = +1/3" in records[3]["emitted_text"],
    }
    if not all(equation_projection.values()):
        raise RuntimeError(f"required equation projection failed: {equation_projection}")
    receipt = {
        "status": "PASS_SOURCE_CARD_RENDER",
        "resolution": [W, H],
        "font_path": str(FONT_PATH),
        "font_sha256": sha256(FONT_PATH),
        "font_choice_reason": FONT_CHOICE_REASON,
        "required_glyph_support": GLYPH_SUPPORT,
        "required_equations_projected_exactly": equation_projection,
        "cards": records,
        "quantitative_geometry": geometry,
        "source_contact_sheet": str(contact.relative_to(output_root)),
        "source_contact_sheet_sha256": sha256(contact),
    }
    (qa_dir / "card-text-and-geometry-audit.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return receipt


def main() -> int:
    receipt = render_all_cards(pipeline.BUILD)
    print(json.dumps({"status": receipt["status"], "cards": len(receipt["cards"]), "font": receipt["font_path"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
