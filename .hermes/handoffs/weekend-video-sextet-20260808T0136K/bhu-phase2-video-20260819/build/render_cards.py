#!/usr/bin/env python3
"""Render ten deterministic 1920x1080 Phase-2 cards in the Phase-1 Pillow style."""
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
REQUIRED_GLYPHS = "ε≤⁻⁶²⁷×−“”·ł"


def font_codepoints(path: Path, index: int = 0) -> set[int]:
    fonts = TTCollection(path).fonts if path.suffix.lower() == ".ttc" else [TTFont(path)]
    cmap = fonts[index]["cmap"]
    return set().union(*(table.cmap.keys() for table in cmap.tables))  # type: ignore[attr-defined]


def choose_font() -> tuple[Path, str, dict[str, bool]]:
    support = {glyph: ord(glyph) in font_codepoints(HELVETICA) for glyph in REQUIRED_GLYPHS}
    if all(support.values()):
        return HELVETICA, "Helvetica index 0 contains every Phase-2 required glyph", support
    if not DEJAVU.is_file():
        raise RuntimeError("Helvetica lacks a required glyph and DejaVu Sans is unavailable")
    support = {glyph: ord(glyph) in font_codepoints(DEJAVU) for glyph in REQUIRED_GLYPHS}
    if not all(support.values()):
        raise RuntimeError(f"fallback font lacks required glyphs: {support}")
    return DEJAVU, "DejaVu Sans selected because Helvetica lacks a required Phase-2 glyph", support


FONT_PATH, FONT_REASON, GLYPH_SUPPORT = choose_font()


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
        step = size + 8
        total = len(lines) * step - 8
        y = box[1] + max(0.0, (box[3] - box[1] - total) / 2)
        for line in lines:
            length = self.draw.textlength(line, font=face)
            x = box[0] if align == "left" else box[2] - length if align == "right" else box[0] + (width - length) / 2
            self.draw.text((x, y), line, font=face, fill=color)
            y += step

    def plate(self, text: str, box: tuple[int, int, int, int], color, *, size=22, max_lines=3) -> None:
        rounded(self.draw, box, fill=PANEL_2, outline=color, width=3, radius=17)
        self.wrap(text, (box[0] + 14, box[1] + 7, box[2] - 14, box[3] - 7), size, color=color, bold=True, max_lines=max_lines)


def base_card(panel: dict) -> tuple[Image.Image, TextSurface, list[str]]:
    image = Image.new("RGB", (W, H), BG)
    starfield(image)
    surface = TextSurface(image, panel["viewer_text_closed_world"])
    surface.draw.line((82, 246, W - 82, 246), fill=GRID, width=3)
    surface.wrap(panel["viewer_text_closed_world"][0], (90, 48, W - 90, 224), 47, bold=True, max_lines=2)
    return image, surface, panel["viewer_text_closed_world"][1:]


def stacked(surface: TextSurface, labels: list[str], box: tuple[int, int, int, int], colors: list[tuple[int, int, int]], *, size=21) -> None:
    gap = 11
    height = (box[3] - box[1] - gap * (len(labels) - 1)) // len(labels)
    y = box[1]
    for index, label in enumerate(labels):
        surface.plate(label, (box[0], y, box[2], y + height), colors[index % len(colors)], size=size)
        y += height + gap


def draw_panel_01(surface: TextSurface, labels: list[str]) -> dict:
    rounded(surface.draw, (260, 278, 1660, 1000), fill=PANEL, outline=GRID)
    stacked(surface, labels, (315, 315, 1605, 965), [MUTED, MUTED, CYAN, AMBER, PURPLE, BLUE, GREEN], size=25)
    return {"opening_scope_visible_from_frame_zero": True, "opening_verdict_visible": True}


def draw_panel_02(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (75, 275, 950, 1010), [BLUE, CYAN, BLUE, PURPLE, GREEN, AMBER, RED, RED, MUTED], size=16)
    draw = surface.draw
    rounded(draw, (1010, 280, 1840, 1005))
    paper_y = [350, 480, 610, 740]
    for index, y in enumerate(paper_y):
        color = [BLUE, PURPLE, GREEN, AMBER][index]
        draw.rounded_rectangle((1090, y, 1760, y + 92), radius=14, fill=PANEL_2, outline=color, width=5)
        for row in range(4):
            draw.line((1130, y + 23 + row * 15, 1700, y + 23 + row * 15), fill=GRID, width=3)
    draw.rectangle((1110, 783, 1740, 809), fill=RED)
    arrow(draw, (1460, 744), (1460, 815), RED, width=7)
    return {"paper_cards": 4, "audit_rows": 77, "later_paper_quote_attributed": True}


def draw_panel_03(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (70, 275, 950, 1010), [CYAN, BLUE, RED, AMBER, AMBER, GREEN], size=19)
    draw = surface.draw
    rounded(draw, (1000, 275, 1845, 1010))
    # Smooth U-shaped turning point and lower prescribed cusp remain visibly distinct.
    smooth = [(1045 + index * 4, 590 - int(0.0042 * (index * 4 - 165) ** 2)) for index in range(83)]
    draw.line(smooth, fill=BLUE, width=8, joint="curve")
    draw.line([(1045, 690), (1210, 830), (1375, 690)], fill=RED, width=9, joint="curve")
    draw.line((1210, 785, 1210, 875), fill=WHITE, width=5)
    # A Planck-caveat marker sits beside each drawn bounce state; the approved text label is on the left.
    for x, y in ((1270, 590), (1270, 830)):
        draw.polygon([(x, y - 34), (x - 31, y + 25), (x + 31, y + 25)], fill=AMBER, outline=WHITE)
        draw.line((x, y - 12, x, y + 8), fill=BG, width=5)
        draw.ellipse((x - 3, y + 14, x + 3, y + 20), fill=BG)
    # All 730 linear units are visible as a ten-column magnitude ladder: no log compression.
    start_x, start_y = 1500, 335
    for index in range(730):
        column, row = divmod(index, 73)
        x = start_x + column * 27
        y = 915 - row * 8
        color = RED if index == 0 else BLUE if index == 729 else GRID
        draw.rectangle((x, y, x + 17, y + 5), fill=color)
    draw.line((1465, 915, 1465, 335), fill=CYAN, width=6)
    arrow(draw, (1465, 915), (1465, 335), CYAN, width=6)
    return {"smooth_turning_point_drawn": True, "prescribed_cusp_drawn": True, "planck_caveat_markers": 2, "linear_ladder_rungs": 730, "gap_factor": 730, "unlabeled_log_compression": False}


def draw_panel_04(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (75, 280, 950, 1005), [BLUE, RED, GREEN, PURPLE, AMBER, CYAN], size=18)
    draw = surface.draw
    rounded(draw, (1010, 280, 1840, 1005))
    y = 650
    draw.line((1110, y, 1740, y), fill=WHITE, width=8)
    for index in range(7):
        x = 1110 + index * 105
        draw.line((x, y - 45, x, y + 45), fill=GRID if index not in (0, 6) else CYAN, width=5)
    draw.ellipse((1084, y - 26, 1136, y + 26), fill=PURPLE, outline=WHITE, width=2)
    draw.ellipse((1714, y - 35, 1784, y + 35), fill=AMBER, outline=WHITE, width=2)
    arrow(draw, (1150, 755), (1695, 755), CYAN)
    draw.rounded_rectangle((1330, 810, 1520, 900), radius=18, outline=GREEN, width=5)
    arrow(draw, (1425, 755), (1425, 810), GREEN)
    return {"linear_intervals": 6, "swing_factor": 6, "bracket_attached_downstream": True, "unlabeled_log_compression": False}


def draw_panel_05(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (75, 285, 950, 1000), [GREEN, RED, AMBER, CYAN, PURPLE], size=19)
    draw = surface.draw
    rounded(draw, (1010, 285, 1840, 1000))
    draw.rounded_rectangle((1070, 350, 1325, 865), radius=20, fill=PANEL_2, outline=GREEN, width=6)
    for y in (420, 520, 620):
        draw.rounded_rectangle((1110, y, 1285, y + 58), radius=10, fill=PANEL, outline=RED, width=4)
        draw.line((1140, y + 29, 1255, y + 29), fill=RED, width=5)
    draw.rectangle((1390, 315, 1465, 930), fill=GRID, outline=WHITE, width=4)
    for y in (420, 520, 620):
        arrow(draw, (1485, y + 29), (1685, y + 29), CYAN)
        draw.ellipse((1690, y, 1748, y + 58), fill=GREEN, outline=WHITE, width=3)
    draw.arc((1375, 520, 1480, 690), 180, 360, fill=RED, width=10)
    draw.rectangle((1405, 600, 1450, 690), fill=RED)
    return {"erratum_record_separate_from_content": True, "paywall_drawn": True, "quarantined_numbers": 3, "recomputations": 3}


def draw_panel_06(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (65, 275, 950, 1010), [BLUE, GREEN, RED, CYAN, AMBER, PURPLE, GREEN], size=17)
    draw = surface.draw
    rounded(draw, (1000, 275, 1845, 1010))
    for index in range(4):
        x = 1055 + index * 180
        draw.rounded_rectangle((x, 345, x + 140, 535), radius=15, fill=PANEL_2, outline=[BLUE, PURPLE, GREEN, AMBER][index], width=5)
        for row in range(6):
            color = RED if index == 3 and row == 3 else GRID
            width = 7 if index == 3 and row == 3 else 3
            draw.line((x + 20, 385 + row * 22, x + 120, 385 + row * 22), fill=color, width=width)
    draw.ellipse((1080, 700, 1180, 800), outline=GREEN, width=8)
    arrow(draw, (1190, 750), (1480, 750), GREEN)
    draw.ellipse((1510, 700, 1610, 800), outline=BLUE, width=8)
    draw.line((1640, 750, 1770, 750), fill=RED, width=7)
    draw.line((1690, 715, 1720, 785), fill=RED, width=8)
    draw.line((1720, 715, 1690, 785), fill=RED, width=8)
    return {"paper_cards": 4, "parent_spin_sentences": 1, "parent_spin_equations": 0, "mass_channel_connected": True, "spin_bridge_missing": True}


def draw_panel_07(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (65, 270, 950, 1015), [BLUE, AMBER, RED, RED, CYAN, PURPLE, MUTED], size=17)
    draw = surface.draw
    rounded(draw, (1000, 275, 1845, 1010))
    # 27 order-of-magnitude steps with both endpoints carried by the approved labels.
    x0, y0, y1 = 1320, 345, 915
    draw.line((x0, y0, x0, y1), fill=RED, width=7)
    for index in range(28):
        y = y1 - index * (y1 - y0) / 27
        length = 135 if index in (0, 27) else 68
        draw.line((x0 - length, y, x0 + length, y), fill=RED if index == 27 else CYAN if index == 0 else GRID, width=5)
    draw.arc((1085, 430, 1275, 620), 90, 450, fill=AMBER, width=12)
    arrow(draw, (1180, 535), (1180, 410), AMBER, width=8)
    draw.line((1515, 485, 1755, 485), fill=MUTED, width=6)
    draw.line((1615, 440, 1655, 530), fill=RED, width=9)
    draw.line((1655, 440, 1615, 530), fill=RED, width=9)
    return {"order_steps": 27, "causality_overshoot": "6.6e26", "reading_1_branch": "ceiling", "reading_2_branch": "underived", "ceiling_not_measurement": True}


def draw_panel_08(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (65, 270, 950, 1015), [CYAN, BLUE, PURPLE, AMBER, GREEN, MUTED, RED], size=17)
    draw = surface.draw
    rounded(draw, (1000, 275, 1845, 1010))
    center_x, beam_y = 1425, 600
    draw.line((1110, beam_y, 1740, beam_y), fill=WHITE, width=10)
    draw.polygon([(center_x, beam_y), (1365, 795), (1485, 795)], fill=GRID, outline=WHITE)
    draw.ellipse((1080, 555, 1170, 645), outline=BLUE, width=9)
    draw.ellipse((1680, 555, 1770, 645), outline=PURPLE, width=9)
    for radius in (250, 185, 120):
        draw.arc((center_x - radius, beam_y - radius, center_x + radius, beam_y + radius), 205, 335, fill=CYAN, width=5)
    arrow(draw, (1210, 870), (1355, 870), MUTED)
    arrow(draw, (1640, 870), (1495, 870), MUTED)
    return {"balanced_scale_level": True, "equal_dilution_rates": True, "ratio_frozen": True, "axis_memory_survival": "undetermined", "axis_memory_erasure": "undetermined"}


def draw_panel_09(surface: TextSurface, labels: list[str]) -> dict:
    stacked(surface, labels, (60, 265, 950, 1020), [AMBER, GREEN, BLUE, PURPLE, CYAN, MUTED, RED], size=16)
    draw = surface.draw
    rounded(draw, (995, 270, 1850, 1020))
    # 45 explicit order steps for the BBN margin.
    x = 1150
    draw.line((x, 330, x, 725), fill=AMBER, width=7)
    for index in range(46):
        y = 725 - index * (395 / 45)
        length = 82 if index in (0, 45) else 34
        draw.line((x - length, y, x + length, y), fill=AMBER if index in (0, 45) else GRID, width=3)
    # Separate six-step 10^-5-class signal-to-floor scale, anchored by exact ppm labels.
    sx = 1420
    draw.line((sx, 350, sx, 705), fill=CYAN, width=7)
    for index in range(7):
        y = 705 - index * (355 / 6)
        draw.line((sx - (90 if index in (0, 6) else 42), y, sx + (90 if index in (0, 6) else 42), y), fill=CYAN if index in (0, 6) else GRID, width=4)
    # All-galaxies theoretical floor tiling; representational, not a claim that classification exists.
    for row in range(10):
        for col in range(20):
            xx, yy = 1550 + col * 12, 510 + row * 12
            draw.rectangle((xx, yy, xx + 8, yy + 8), fill=BLUE if row == 0 and col == 0 else GRID)
    return {"bbn_order_steps": 45, "signal_floor_order_steps": 6, "treatment_ppm": [8.5, 76], "all_galaxies_floor": "2 trillion theoretical best", "unlabeled_log_compression": False}


def draw_panel_10(surface: TextSurface, labels: list[str]) -> dict:
    rounded(surface.draw, (260, 278, 1660, 1000), fill=PANEL, outline=GRID)
    stacked(surface, labels, (315, 315, 1605, 965), [MUTED, BLUE, CYAN, PURPLE, MUTED, AMBER, GREEN], size=24)
    return {"ends_on_verdict": labels[-1] == "THE CEILING SAYS THE ROUTE STAYS CLOSED", "post_verdict_caveat": False}


DRAWERS: dict[str, Callable[[TextSurface, list[str]], dict]] = {
    "01": draw_panel_01, "02": draw_panel_02, "03": draw_panel_03, "04": draw_panel_04, "05": draw_panel_05,
    "06": draw_panel_06, "07": draw_panel_07, "08": draw_panel_08, "09": draw_panel_09, "10": draw_panel_10,
}


def render_all_cards(output_root: Path) -> dict:
    frozen = pipeline.load_frozen_inputs()
    cards_dir, qa_dir = output_root / "cards", output_root / "qa"
    cards_dir.mkdir(parents=True, exist_ok=True)
    qa_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    geometry: dict[str, dict] = {}
    for panel in frozen["panels"]:
        image, surface, labels = base_card(panel)
        geometry[f"panel_{panel['id']}"] = DRAWERS[panel["id"]](surface, labels)
        if surface.emitted != panel["viewer_text_closed_world"]:
            raise RuntimeError(f"panel {panel['id']} exact text projection mismatch")
        path = cards_dir / f"card-{panel['id']}.png"
        image.save(path, format="PNG", optimize=False, compress_level=9)
        records.append({
            "id": panel["id"], "path": str(path.relative_to(output_root)), "sha256": sha256(path),
            "heading": panel["assertion_heading"], "permitted_text": panel["viewer_text_closed_world"],
            "emitted_text": surface.emitted, "text_contract_status": "PASS_EXACT_CLOSED_WORLD",
        })
    sheet = Image.new("RGB", (1920, 810), BG)
    for index, record in enumerate(records):
        card = Image.open(output_root / record["path"]).convert("RGB")
        sheet.paste(ImageOps.fit(card, (480, 270), Image.Resampling.LANCZOS), ((index % 4) * 480, (index // 4) * 270))
    contact = qa_dir / "source-contact-sheet.png"
    sheet.save(contact, format="PNG", optimize=False, compress_level=9)
    equations = [text for record in records for text in record["emitted_text"] if " = " in text or " ≤ " in text]
    if equations != pipeline.EXPECTED_EQUATIONS:
        raise RuntimeError(f"equation projection mismatch: {equations!r}")
    receipt = {
        "status": "PASS_SOURCE_CARD_RENDER",
        "resolution": [W, H],
        "font_path": str(FONT_PATH),
        "font_sha256": sha256(FONT_PATH),
        "font_choice_reason": FONT_REASON,
        "required_glyph_support": GLYPH_SUPPORT,
        "equations_projected_exactly": equations,
        "other_equations_projected": False,
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
