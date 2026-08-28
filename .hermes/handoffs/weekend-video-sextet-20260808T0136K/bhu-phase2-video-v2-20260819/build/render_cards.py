#!/usr/bin/env python3
"""Render deterministic 1920x1080 v2 panel states in the prior Pillow style."""
from __future__ import annotations

import functools
import hashlib
import json
import math
import random
import shutil
from collections import Counter
from pathlib import Path
from typing import Any, Callable

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
REQUIRED_GLYPHS = "ε≤⁻⁶²⁷×−“”·→"


def font_codepoints(path: Path, index: int = 0) -> set[int]:
    fonts = TTCollection(path).fonts if path.suffix.lower() == ".ttc" else [TTFont(path)]
    return set().union(*(table.cmap.keys() for table in fonts[index]["cmap"].tables))  # type: ignore[attr-defined]


def choose_font() -> tuple[Path, str, dict[str, bool]]:
    support = {glyph: ord(glyph) in font_codepoints(HELVETICA) for glyph in REQUIRED_GLYPHS}
    if all(support.values()):
        return HELVETICA, "Helvetica index 0 contains every required v2 glyph", support
    if not DEJAVU.is_file():
        raise RuntimeError("Helvetica lacks a required glyph and DejaVu Sans is unavailable")
    support = {glyph: ord(glyph) in font_codepoints(DEJAVU) for glyph in REQUIRED_GLYPHS}
    if not all(support.values()):
        raise RuntimeError(f"fallback font lacks required glyphs: {support}")
    return DEJAVU, "DejaVu Sans selected because Helvetica lacks a required v2 glyph", support


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

    def lines(self, text: str, width: int, size: int, bold: bool) -> list[str]:
        face = font(size, bold)
        output: list[str] = []
        current = ""
        for word in text.split():
            trial = (current + " " + word).strip()
            if self.draw.textlength(trial, font=face) <= width:
                current = trial
            else:
                if current:
                    output.append(current)
                current = word
        if current:
            output.append(current)
        return output

    def wrap(self, text: str, box: tuple[int, int, int, int], size: int, *, color=WHITE, bold=False, align="center", max_lines: int | None = None, min_size: int = 14) -> None:
        self._record(text)
        width = box[2] - box[0]
        actual_size = size
        lines = self.lines(text, width, actual_size, bold)
        while max_lines is not None and len(lines) > max_lines and actual_size > min_size:
            actual_size -= 1
            lines = self.lines(text, width, actual_size, bold)
        if max_lines is not None and len(lines) > max_lines:
            raise RuntimeError(f"text exceeds {max_lines} lines at minimum size: {text!r} -> {lines!r}")
        face = font(actual_size, bold)
        step = actual_size + 7
        total = len(lines) * step - 7
        y = box[1] + max(0.0, (box[3] - box[1] - total) / 2)
        for line in lines:
            length = self.draw.textlength(line, font=face)
            x = box[0] if align == "left" else box[2] - length if align == "right" else box[0] + (width - length) / 2
            self.draw.text((x, y), line, font=face, fill=color)
            y += step

    def plate(self, text: str, box: tuple[int, int, int, int], color, *, size=22, max_lines=3, fill=PANEL_2) -> None:
        rounded(self.draw, box, fill=fill, outline=color, width=3, radius=17)
        self.wrap(text, (box[0] + 14, box[1] + 7, box[2] - 14, box[3] - 7), size, color=color, bold=True, max_lines=max_lines)


def base_state(panel: dict[str, Any]) -> tuple[Image.Image, TextSurface]:
    image = Image.new("RGB", (W, H), BG)
    starfield(image)
    surface = TextSurface(image, pipeline.render_viewer_text(panel))
    surface.draw.line((82, 230, W - 82, 230), fill=GRID, width=3)
    surface.wrap(panel["assertion_heading"], (90, 38, W - 90, 210), 47, bold=True, max_lines=2)
    return image, surface


def stack(surface: TextSurface, labels: list[str], box: tuple[int, int, int, int], colors: list[tuple[int, int, int]], *, size=19, gap=10) -> None:
    height = (box[3] - box[1] - gap * (len(labels) - 1)) // len(labels)
    y = box[1]
    for index, label in enumerate(labels):
        surface.plate(label, (box[0], y, box[2], y + height), colors[index % len(colors)], size=size)
        y += height + gap


def paste_asset(image: Image.Image, asset: Path, box: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    expected = pipeline.EXPECTED_ASSETS[asset.name]
    if pipeline.sha256(asset) != expected:
        raise RuntimeError(f"refusing to embed unpinned asset: {asset}")
    source = Image.open(asset).convert("RGB")
    contained = ImageOps.contain(source, (box[2] - box[0], box[3] - box[1]), Image.Resampling.LANCZOS)
    x = box[0] + (box[2] - box[0] - contained.width) // 2
    y = box[1] + (box[3] - box[1] - contained.height) // 2
    image.paste((255, 255, 255), box)
    image.paste(contained, (x, y))
    ImageDraw.Draw(image).rectangle((x, y, x + contained.width - 1, y + contained.height - 1), outline=WHITE, width=2)
    return (x, y, x + contained.width, y + contained.height)


def map_points(source_size: tuple[int, int], actual_box: tuple[int, int, int, int], points: list[tuple[int, int]]) -> list[list[float]]:
    sx = (actual_box[2] - actual_box[0]) / source_size[0]
    sy = (actual_box[3] - actual_box[1]) / source_size[1]
    return [[actual_box[0] + x * sx, actual_box[1] + y * sy] for x, y in points]


def paper_plot(surface: TextSurface, asset_name: str, plot_box: tuple[int, int, int, int], attribution: str, chip_box: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    rounded(surface.draw, (plot_box[0] - 12, plot_box[1] - 12, plot_box[2] + 12, plot_box[3] + 12), fill=PANEL, outline=GRID, width=3)
    actual = paste_asset(surface.image, pipeline.ASSETS / asset_name, plot_box)
    surface.plate(attribution, chip_box, AMBER, size=16, max_lines=2)
    return actual


def no_plots(surface: TextSurface, text: str, box: tuple[int, int, int, int]) -> None:
    surface.plate(text, box, AMBER, size=20, max_lines=2, fill=(45, 35, 24))


def original_chip(surface: TextSurface, text: str, box: tuple[int, int, int, int]) -> None:
    surface.plate(text, box, MUTED, size=16, max_lines=1)


def panel_01(panel: dict[str, Any]) -> list[dict[str, Any]]:
    image, s = base_state(panel)
    labels = pipeline.render_viewer_text(panel)[1:]
    rounded(s.draw, (160, 270, 1760, 1015), fill=PANEL, outline=GRID)
    # Parent black hole, inheritance arrow, baby universe, and a hard ceiling.
    s.draw.ellipse((235, 420, 505, 690), fill=(1, 4, 10), outline=PURPLE, width=10)
    for r in (160, 195, 230):
        s.draw.arc((370 - r, 555 - r // 2, 370 + r, 555 + r // 2), 200, 340, fill=PURPLE, width=3)
    s.draw.ellipse((1410, 435, 1650, 675), fill=(28, 52, 87), outline=CYAN, width=8)
    arrow(s.draw, (535, 555), (870, 555), CYAN, 9)
    s.draw.rectangle((895, 365, 930, 750), fill=RED)
    s.draw.line((845, 365, 980, 365), fill=RED, width=10)
    # Text is arranged in compact rows around the deterministic silhouette.
    s.plate(labels[0], (195, 300, 855, 380), MUTED, size=21, max_lines=2)
    s.plate(labels[1], (1065, 300, 1725, 380), MUTED, size=21, max_lines=2)
    stack(s, labels[2:4], (555, 665, 895, 835), [CYAN, AMBER], size=18)
    s.plate(labels[4], (960, 695, 1690, 790), PURPLE, size=21, max_lines=2)
    s.plate(labels[5], (300, 860, 925, 960), BLUE, size=23, max_lines=2)
    s.plate(labels[6], (995, 860, 1620, 960), GREEN, size=25, max_lines=2)
    return [{"name": "main", "image": image, "surface": s, "duration_weight": 1.0, "geometry": {"parent_black_hole_to_baby_universe": True, "inheritance_arrow_stopped_at_ceiling": True}}]


def panel_02(panel: dict[str, Any]) -> list[dict[str, Any]]:
    image, s = base_state(panel)
    b = pipeline.render_viewer_text(panel)[1:]
    stack(s, b[:4], (65, 270, 795, 725), [BLUE, CYAN, PURPLE, GREEN], size=18)
    no_plots(s, b[4], (65, 750, 1210, 845))
    s.plate(b[5], (65, 870, 1210, 980), RED, size=20, max_lines=2)
    rounded(s.draw, (845, 270, 1850, 980), fill=PANEL, outline=GRID)
    # Fabric grid twists into a spring and exits through a smooth bounce.
    for offset in range(6):
        y = 360 + offset * 80
        points = []
        for x in range(910, 1791, 18):
            twist = 28 * math.sin((x - 910) / 72 + offset * 0.55) * math.exp(-((x - 1350) / 300) ** 2)
            points.append((x, y + twist))
        s.draw.line(points, fill=GRID, width=3)
    for x in range(940, 1790, 105):
        s.draw.line((x, 320, x, 820), fill=(38, 63, 93), width=2)
    spring = []
    for i in range(210):
        x = 930 + i * 3.9
        y = 600 - 220 * abs((i - 105) / 105) + 22 * math.sin(i / 4)
        spring.append((x, y))
    s.draw.line(spring, fill=CYAN, width=7, joint="curve")
    s.draw.ellipse((1312, 570, 1388, 646), outline=AMBER, width=8)
    original_chip(s, b[6], (1460, 895, 1815, 950))
    return [{"name": "main", "image": image, "surface": s, "duration_weight": 1.0, "geometry": {"no_plots_card": True, "fabric_spring_bounce": True, "original_graphic_chip": True}}]


def panel_03(panel: dict[str, Any]) -> list[dict[str, Any]]:
    image, s = base_state(panel)
    b = pipeline.render_viewer_text(panel)[1:]
    stack(s, [b[0], b[1]], (60, 270, 850, 450), [CYAN, BLUE], size=20)
    s.plate(b[2], (60, 475, 410, 560), GREEN, size=20)
    s.plate(b[3], (500, 475, 850, 560), PURPLE, size=18, max_lines=2)
    s.plate(b[4], (60, 590, 850, 690), AMBER, size=26)
    stack(s, b[5:8], (60, 720, 850, 995), [GREEN, RED, BLUE], size=18)
    rounded(s.draw, (910, 270, 1850, 995), fill=PANEL, outline=GRID)
    # Six explicit neutrino lanes split into lined-up and independent branches.
    colors = [BLUE, CYAN, GREEN, PURPLE, AMBER, RED]
    for i, color in enumerate(colors):
        y = 350 + i * 78
        s.draw.line((980, y, 1320, y), fill=color, width=7)
        arrow(s.draw, (1250, y), (1320, y), color, 7)
        s.draw.ellipse((950, y - 17, 984, y + 17), fill=color)
    arrow(s.draw, (1360, 430), (1650, 395), CYAN, 7)
    arrow(s.draw, (1360, 650), (1650, 760), PURPLE, 7)
    s.draw.rounded_rectangle((1580, 330, 1785, 470), radius=18, outline=GREEN, width=6)
    s.draw.rounded_rectangle((1580, 705, 1785, 845), radius=18, outline=PURPLE, width=6)
    # Six linear units: no log compression.
    for i in range(6):
        x = 1030 + i * 95
        s.draw.rectangle((x, 900, x + 65, 930), fill=AMBER if i == 5 else GRID)
    original_chip(s, b[8], (1480, 915, 1815, 970))
    return [{"name": "main", "image": image, "surface": s, "duration_weight": 1.0, "geometry": {"spin_lanes": 6, "linear_bracket_units": 6, "two_average_edges": True, "correction_record_separate_from_content": True}}]


def panel_04(panel: dict[str, Any]) -> list[dict[str, Any]]:
    image, s = base_state(panel)
    b = pipeline.render_viewer_text(panel)[1:]
    stack(s, b[:4], (55, 280, 755, 830), [BLUE, CYAN, GREEN, RED], size=18)
    actual = paper_plot(s, "prd_1111.4595_fig1_scale.jpg", (810, 300, 1860, 935), b[4], (835, 955, 1835, 1015))
    points = map_points((1278, 774), actual, [(110, 140), (250, 210), (410, 310), (555, 425), (635, 535), (672, 614), (710, 530), (820, 390), (975, 270), (1120, 195), (1236, 140)])
    return [{"name": "plot", "image": image, "surface": s, "duration_weight": 1.0, "cursor_points": points, "geometry": {"paper_asset": "prd_1111.4595_fig1_scale.jpg", "paper_asset_sha256": pipeline.EXPECTED_ASSETS["prd_1111.4595_fig1_scale.jpg"], "embedded_box": actual, "curve_walkthrough": "contraction_to_sharp_cusp_to_expansion", "attribution_visible": True}}]


def panel_05(panel: dict[str, Any]) -> list[dict[str, Any]]:
    b = pipeline.render_viewer_text(panel)[1:]
    plot, s1 = base_state(panel)
    stack(s1, b[:2], (55, 300, 755, 510), [BLUE, AMBER], size=20)
    actual = paper_plot(s1, "prd_1111.4595_fig2_temp.jpg", (810, 320, 1860, 955), b[2], (55, 535, 755, 610))
    points = map_points((1278, 774), actual, [(120, 632), (340, 615), (500, 580), (610, 500), (655, 360), (675, 165), (679, 87), (683, 165), (705, 360), (760, 500), (920, 585), (1100, 615), (1238, 632)])
    peak = points[6]
    # Marker is entirely above the source-image rectangle and aligned to the visible peak.
    marker_y = actual[1] - 18
    s1.draw.polygon([(peak[0], marker_y - 34), (peak[0] - 28, marker_y + 20), (peak[0] + 28, marker_y + 20)], fill=AMBER, outline=WHITE)
    s1.draw.line((peak[0], marker_y + 20, peak[0], actual[1] - 2), fill=AMBER, width=5)

    audit, s2 = base_state(panel)
    stack(s2, b[3:6], (80, 285, 855, 610), [RED, RED, MUTED], size=22)
    s2.plate(b[6], (1000, 300, 1800, 420), CYAN, size=34, max_lines=1)
    s2.plate(b[7], (1000, 455, 1800, 565), AMBER, size=25, max_lines=2)
    s2.plate(b[8], (1000, 840, 1800, 950), RED, size=22, max_lines=2)
    # 730 visible linear cells arranged in ten columns; endpoint colors carry the gap.
    for index in range(730):
        column, row = divmod(index, 73)
        x = 1015 + column * 72
        y = 805 - row * 4.7
        color = RED if index == 0 else BLUE if index == 729 else GRID
        s2.draw.rectangle((x, y, x + 48, y + 3), fill=color)
    arrow(s2.draw, (950, 810), (950, 460), AMBER, 7)
    return [
        {"name": "plot", "image": plot, "surface": s1, "duration_weight": 0.56, "cursor_points": points, "geometry": {"paper_asset": "prd_1111.4595_fig2_temp.jpg", "paper_asset_sha256": pipeline.EXPECTED_ASSETS["prd_1111.4595_fig2_temp.jpg"], "embedded_box": actual, "temperature_spike_walkthrough": True, "planck_marker_outside_paper_pixels": True, "attribution_visible": True}},
        {"name": "audit", "image": audit, "surface": s2, "duration_weight": 0.44, "geometry": {"authorized_equation": b[6], "linear_ladder_rungs": 730, "gap_factor": 730, "prescribed_velocity_jump": True, "unlabeled_log_compression": False}},
    ]


def panel_06(panel: dict[str, Any]) -> list[dict[str, Any]]:
    image, s = base_state(panel)
    b = pipeline.render_viewer_text(panel)[1:]
    stack(s, b[:5], (55, 275, 820, 670), [BLUE, CYAN, GREEN, AMBER, PURPLE], size=16)
    no_plots(s, b[5], (55, 700, 1180, 800))
    s.plate(b[6], (55, 825, 1180, 925), RED, size=20, max_lines=2)
    rounded(s.draw, (875, 275, 1850, 975), fill=PANEL, outline=GRID)
    # Seed pod and fixed-compactness gate into two starting conditions.
    s.draw.ellipse((945, 455, 1145, 655), fill=(2, 7, 14), outline=PURPLE, width=9)
    s.draw.arc((930, 430, 1160, 680), 210, 330, fill=CYAN, width=6)
    s.draw.rounded_rectangle((1225, 390, 1455, 500), radius=18, fill=PANEL_2, outline=AMBER, width=5)
    arrow(s.draw, (1155, 555), (1220, 450), CYAN, 7)
    arrow(s.draw, (1455, 445), (1635, 380), GREEN, 7)
    arrow(s.draw, (1455, 445), (1635, 620), RED, 7)
    s.draw.ellipse((1640, 325, 1770, 455), outline=GREEN, width=8)
    for r in (28, 45, 62):
        s.draw.arc((1635 - r, 620 - r, 1635 + r, 620 + r), 225, 495, fill=RED, width=5)
    original_chip(s, b[7], (1430, 885, 1810, 945))
    return [{"name": "main", "image": image, "surface": s, "duration_weight": 1.0, "geometry": {"no_plots_card": True, "parent_mass_to_initial_size_temperature": True, "fixed_compactness_gate": True}}]


def panel_07(panel: dict[str, Any]) -> list[dict[str, Any]]:
    image, s = base_state(panel)
    b = pipeline.render_viewer_text(panel)[1:]
    stack(s, b[:2], (55, 280, 820, 480), [BLUE, MUTED], size=19)
    s.plate(b[2], (55, 505, 820, 620), RED, size=20, max_lines=2)
    s.plate(b[3], (55, 645, 820, 755), PURPLE, size=20, max_lines=2)
    s.plate(b[4], (55, 780, 820, 890), AMBER, size=20, max_lines=2)
    rounded(s.draw, (875, 275, 1850, 975), fill=PANEL, outline=GRID)
    # Birth-certificate start card fades into a later track, which stops at conjecture.
    s.draw.rounded_rectangle((940, 350, 1190, 690), radius=20, fill=PANEL_2, outline=BLUE, width=5)
    for y in range(415, 635, 45):
        s.draw.line((985, y, 1145, y), fill=GRID, width=4)
    arrow(s.draw, (1205, 520), (1450, 520), MUTED, 7)
    for i in range(6):
        alpha = 165 - i * 20
        s.draw.line((1260 + i * 34, 470, 1260 + i * 34, 570), fill=(alpha, alpha, alpha), width=5)
    s.draw.line((1505, 325, 1505, 870), fill=RED, width=7)
    for y in range(325, 870, 38):
        s.draw.line((1480, y, 1530, y + 22), fill=RED, width=4)
    s.draw.arc((1560, 390, 1800, 720), 90, 270, fill=PURPLE, width=10)
    original_chip(s, b[5], (1430, 895, 1810, 950))
    return [{"name": "main", "image": image, "surface": s, "duration_weight": 1.0, "geometry": {"mass_map_fades_before_later_track": True, "dashed_conjecture_boundary": True, "silent_one_meter_input_card": True}}]


def panel_08(panel: dict[str, Any]) -> list[dict[str, Any]]:
    b = pipeline.render_viewer_text(panel)[1:]
    collapse, s1 = base_state(panel)
    stack(s1, b[:2], (55, 290, 820, 500), [BLUE, CYAN], size=20)
    no_plots(s1, b[2], (55, 535, 1150, 640))
    rounded(s1.draw, (875, 280, 1850, 980), fill=PANEL, outline=GRID)
    centers = [(1080, 560, 150), (1390, 560, 105), (1640, 560, 58)]
    for index, (x, y, r) in enumerate(centers):
        color = [AMBER, RED, CYAN][index]
        s1.draw.ellipse((x - r, y - r, x + r, y + r), fill=(55 + index * 15, 34, 27), outline=color, width=8)
        if index < len(centers) - 1:
            arrow(s1.draw, (x + r + 20, y), (centers[index + 1][0] - centers[index + 1][2] - 25, y), color, 7)
    s1.draw.arc((1560, 690, 1720, 850), 0, 180, fill=CYAN, width=10)
    original_chip(s1, b[5], (1430, 895, 1810, 950))

    quote, s2 = base_state(panel)
    rounded(s2.draw, (220, 285, 1700, 790), fill=(29, 32, 47), outline=AMBER, width=4)
    s2.wrap(b[3], (300, 350, 1620, 695), 38, color=WHITE, bold=False, max_lines=5, min_size=29)
    s2.plate(b[4], (320, 835, 1600, 955), RED, size=22, max_lines=2)
    return [
        {"name": "collapse", "image": collapse, "surface": s1, "duration_weight": 0.44, "geometry": {"no_plots_card": True, "shrinking_star_sequence": 3, "proposed_bounce": True}},
        {"name": "quote", "image": quote, "surface": s2, "duration_weight": 0.56, "geometry": {"exact_source_sentence_card": True, "equation_on_quote_card": False, "rotating_model_on_quote_card": False}},
    ]


def panel_09(panel: dict[str, Any]) -> list[dict[str, Any]]:
    b = pipeline.render_viewer_text(panel)[1:]
    ceiling, s1 = base_state(panel)
    stack(s1, b[:4], (50, 275, 850, 720), [BLUE, PURPLE, CYAN, RED], size=18)
    s1.plate(b[4], (965, 285, 1795, 410), AMBER, size=38, max_lines=1)
    s1.plate(b[5], (965, 435, 1795, 535), MUTED, size=22, max_lines=2)
    s1.plate(b[6], (965, 560, 1795, 660), PURPLE, size=22, max_lines=2)
    # Causality ladder with 27 explicit order steps.
    x, y0, y1 = 430, 765, 985
    s1.draw.line((x, y0, x, y1), fill=RED, width=7)
    for i in range(28):
        yy = y1 - i * (y1 - y0) / 27
        length = 120 if i in (0, 27) else 48
        s1.draw.line((x - length, yy, x + length, yy), fill=RED if i == 27 else CYAN if i == 0 else GRID, width=4)
    # A labeled treatment BAND with both branch edges visibly marked.
    band = (1080, 735, 1690, 855)
    s1.draw.rounded_rectangle(band, radius=18, fill=(70, 49, 104), outline=PURPLE, width=4)
    s1.draw.line((band[0], band[1], band[2], band[1]), fill=WHITE, width=7)
    s1.draw.line((band[0], band[3], band[2], band[3]), fill=WHITE, width=7)
    s1.draw.ellipse((band[0] - 10, band[1] - 10, band[0] + 10, band[1] + 10), fill=AMBER)
    s1.draw.ellipse((band[2] - 10, band[3] - 10, band[2] + 10, band[3] + 10), fill=AMBER)
    original_chip(s1, b[11], (1390, 915, 1795, 975))

    ratio, s2 = base_state(panel)
    s2.plate(b[7], (220, 285, 900, 420), CYAN, size=39, max_lines=1)
    s2.plate(b[8], (1020, 285, 1740, 420), BLUE, size=25, max_lines=2)
    rounded(s2.draw, (220, 470, 1740, 740), fill=PANEL, outline=GRID)
    s2.draw.line((350, 605, 820, 605), fill=CYAN, width=12)
    s2.draw.line((1140, 605, 1610, 605), fill=PURPLE, width=12)
    s2.draw.polygon([(960, 510), (900, 700), (1020, 700)], fill=GRID, outline=WHITE)
    s2.draw.line((570, 540, 570, 670), fill=CYAN, width=6)
    s2.draw.line((1390, 540, 1390, 670), fill=PURPLE, width=6)
    s2.plate(b[9], (320, 780, 1600, 880), GREEN, size=23, max_lines=2)
    s2.plate(b[10], (320, 905, 1600, 995), RED, size=21, max_lines=2)
    return [
        {"name": "ceiling", "image": ceiling, "surface": s1, "duration_weight": 0.58, "geometry": {"causality_order_steps": 27, "causality_overshoot": "6.6e26", "authorized_ceiling_equation": b[4], "treatment_band_edges": 2, "treatment_band_label": b[6], "ceiling_not_measurement": True, "unlabeled_log_compression": False}},
        {"name": "ratio", "image": ratio, "surface": s2, "duration_weight": 0.42, "geometry": {"authorized_equal_scaling_equation": b[7], "balanced_ratio": True, "reading_1_less_to_see": True, "amplitude_claim": False}},
    ]


def panel_10(panel: dict[str, Any]) -> list[dict[str, Any]]:
    b = pipeline.render_viewer_text(panel)[1:]
    fig1, s1 = base_state(panel)
    stack(s1, b[:3], (40, 290, 790, 620), [BLUE, CYAN, GREEN], size=18)
    actual1 = paper_plot(s1, "ds_1006.4166_comparison.png", (835, 275, 1855, 1010), b[3], (40, 650, 790, 730))
    centers = map_points((883, 638), actual1, [(500, 65), (500, 65), (500, 285), (500, 285), (500, 500), (500, 500)])

    fig2, s2 = base_state(panel)
    s2.plate(b[5], (45, 305, 790, 430), CYAN, size=21, max_lines=3)
    s2.plate(b[6], (45, 465, 790, 585), AMBER, size=23, max_lines=2)
    actual2 = paper_plot(s2, "ds_1006.4166_prefac_Yp.png", (835, 275, 1855, 1010), b[4], (45, 620, 790, 700))
    curve = map_points((883, 695), actual2, [(155, 612), (240, 540), (330, 465), (420, 390), (510, 315), (600, 245), (690, 175), (780, 100), (870, 32)])

    summary, s3 = base_state(panel)
    stack(s3, b[7:10], (70, 300, 930, 690), [RED, PURPLE, GREEN], size=21)
    rounded(s3.draw, (1010, 285, 1810, 970), fill=PANEL, outline=GRID)
    x, top, bottom = 1400, 355, 895
    s3.draw.line((x, top, x, bottom), fill=AMBER, width=8)
    for i in range(46):
        y = bottom - i * (bottom - top) / 45
        length = 120 if i in (0, 45) else 45
        s3.draw.line((x - length, y, x + length, y), fill=AMBER if i in (0, 45) else GRID, width=4)
    arrow(s3.draw, (1180, bottom), (1180, top), PURPLE, 8)
    return [
        {"name": "figure1", "image": fig1, "surface": s1, "duration_weight": 0.34, "cursor_points": centers, "geometry": {"paper_asset": "ds_1006.4166_comparison.png", "paper_asset_sha256": pipeline.EXPECTED_ASSETS["ds_1006.4166_comparison.png"], "embedded_box": actual1, "walkthrough_panels": ["helium", "deuterium", "lithium"], "attribution_visible": True}},
        {"name": "figure2", "image": fig2, "surface": s2, "duration_weight": 0.34, "cursor_points": curve, "geometry": {"paper_asset": "ds_1006.4166_prefac_Yp.png", "paper_asset_sha256": pipeline.EXPECTED_ASSETS["ds_1006.4166_prefac_Yp.png"], "embedded_box": actual2, "helium_change_curve_trace": True, "attribution_visible": True}},
        {"name": "reality", "image": summary, "surface": s3, "duration_weight": 0.32, "geometry": {"bound_multiple": 30, "labeled_order_steps": 45, "sign_caveat_visible": True, "unlabeled_log_compression": False}},
    ]


def panel_11(panel: dict[str, Any]) -> list[dict[str, Any]]:
    image, s = base_state(panel)
    b = pipeline.render_viewer_text(panel)[1:]
    stack(s, b[:2], (45, 280, 760, 490), [CYAN, GREEN], size=21)
    s.plate(b[2], (45, 520, 760, 650), PURPLE, size=21, max_lines=3)
    stack(s, b[3:6], (45, 680, 760, 980), [BLUE, AMBER, MUTED], size=18)
    rounded(s.draw, (825, 275, 1850, 995), fill=PANEL, outline=GRID)
    # Every generosity knob points toward survival.
    for i, color in enumerate([CYAN, GREEN, AMBER, PURPLE]):
        cy = 365 + i * 120
        s.draw.arc((900, cy - 45, 990, cy + 45), 200, 520, fill=color, width=8)
        arrow(s.draw, (945, cy), (980, cy - 28), color, 5)
    # Floor ladder and a treatment RANGE band with two explicit edges.
    x, top, bottom = 1470, 340, 850
    s.draw.line((x, top, x, bottom), fill=CYAN, width=8)
    for i in range(7):
        y = bottom - i * (bottom - top) / 6
        s.draw.line((x - (130 if i in (0, 6) else 55), y, x + (130 if i in (0, 6) else 55), y), fill=CYAN if i in (0, 6) else GRID, width=5)
    band_top, band_bottom = 725, 815
    s.draw.rounded_rectangle((1280, band_top, 1660, band_bottom), radius=15, fill=(65, 48, 98), outline=PURPLE, width=4)
    s.draw.line((1280, band_top, 1660, band_top), fill=WHITE, width=7)
    s.draw.line((1280, band_bottom, 1660, band_bottom), fill=WHITE, width=7)
    s.draw.ellipse((1268, band_top - 12, 1292, band_top + 12), fill=AMBER)
    s.draw.ellipse((1648, band_bottom - 12, 1672, band_bottom + 12), fill=AMBER)
    s.plate(b[6], (900, 875, 1340, 965), AMBER, size=17, max_lines=2)
    s.plate(b[7], (1370, 875, 1810, 965), RED, size=17, max_lines=2)
    original_chip(s, b[8], (900, 780, 1215, 835))
    return [{"name": "main", "image": image, "surface": s, "duration_weight": 1.0, "geometry": {"generosity_knobs": 4, "signal_floor_ladder_steps": 6, "signal_range_band_edges": 2, "signal_range_label": b[2], "all_galaxies_floor": "2 trillion theoretical best", "planck_regime_chip": True, "external_review_chip": True, "unlabeled_log_compression": False}}]


def panel_12(panel: dict[str, Any]) -> list[dict[str, Any]]:
    image, s = base_state(panel)
    b = pipeline.render_viewer_text(panel)[1:]
    rounded(s.draw, (200, 270, 1720, 1010), fill=PANEL, outline=GRID)
    stack(s, b[:4], (260, 310, 1660, 665), [BLUE, RED, PURPLE, AMBER], size=21)
    s.plate(b[4], (300, 700, 1620, 785), MUTED, size=23, max_lines=2)
    s.plate(b[5], (300, 810, 1620, 895), PURPLE, size=23, max_lines=2)
    s.plate(b[6], (300, 915, 920, 980), BLUE, size=19, max_lines=2)
    s.plate(b[7], (1000, 915, 1620, 980), GREEN, size=21, max_lines=2)
    return [{"name": "main", "image": image, "surface": s, "duration_weight": 1.0, "geometry": {"four_paper_stack": True, "ends_on_verdict": b[-1] == "THE CEILING SAYS THE ROUTE STAYS CLOSED", "post_verdict_caveat": False}}]


DRAWERS: dict[str, Callable[[dict[str, Any]], list[dict[str, Any]]]] = {
    "01": panel_01, "02": panel_02, "03": panel_03, "04": panel_04,
    "05": panel_05, "06": panel_06, "07": panel_07, "08": panel_08,
    "09": panel_09, "10": panel_10, "11": panel_11, "12": panel_12,
}


def render_cursor(path: Path) -> None:
    image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((5, 5, 59, 59), fill=(246, 184, 91, 45), outline=(246, 184, 91, 255), width=7)
    draw.ellipse((25, 25, 39, 39), fill=(255, 255, 255, 255), outline=(7, 13, 25, 255), width=3)
    image.save(path, format="PNG", optimize=False, compress_level=9)


def render_all_cards(output_root: Path) -> dict[str, Any]:
    frozen = pipeline.load_frozen_inputs()
    cards_dir, qa_dir = output_root / "cards", output_root / "qa"
    cards_dir.mkdir(parents=True, exist_ok=True)
    qa_dir.mkdir(parents=True, exist_ok=True)
    cursor_path = cards_dir / "walkthrough-cursor.png"
    render_cursor(cursor_path)

    panel_records: list[dict[str, Any]] = []
    all_state_images: list[Image.Image] = []
    quantitative_geometry: dict[str, Any] = {}
    for panel in frozen["panels"]:
        states = DRAWERS[panel["id"]](panel)
        if abs(sum(float(state["duration_weight"]) for state in states) - 1.0) > 1e-9:
            raise RuntimeError(f"panel {panel['id']} state weights do not sum to 1")
        state_records = []
        all_emitted: list[str] = []
        panel_geometry: dict[str, Any] = {}
        for state in states:
            surface: TextSurface = state.pop("surface")
            image: Image.Image = state.pop("image")
            state_name = state["name"]
            path = cards_dir / f"card-{panel['id']}-{state_name}.png"
            image.save(path, format="PNG", optimize=False, compress_level=9)
            all_state_images.append(image.copy())
            all_emitted.extend(surface.emitted)
            panel_geometry[state_name] = state.get("geometry", {})
            state_records.append({
                "name": state_name,
                "path": str(path.relative_to(output_root)),
                "sha256": sha256(path),
                "duration_weight": state["duration_weight"],
                "cursor_points": state.get("cursor_points", []),
                "heading": panel["assertion_heading"],
                "emitted_text": surface.emitted,
                "geometry": state.get("geometry", {}),
            })
        counts = Counter(all_emitted)
        permitted = pipeline.render_viewer_text(panel)
        missing = [text for text in permitted if counts[text] == 0]
        extra = [text for text in counts if text not in permitted]
        if missing or extra:
            raise RuntimeError(f"panel {panel['id']} closed-world text projection failed: missing={missing}, extra={extra}")
        if any(record["emitted_text"][0] != panel["assertion_heading"] for record in state_records):
            raise RuntimeError(f"assertion heading is not first on every state for panel {panel['id']}")
        panel_records.append({
            "id": panel["id"],
            "heading": panel["assertion_heading"],
            "permitted_text": permitted,
            "emission_counts": dict(counts),
            "text_contract_status": "PASS_EXACT_CLOSED_WORLD_ACROSS_PANEL_STATES",
            "states": state_records,
        })
        quantitative_geometry[f"panel_{panel['id']}"] = panel_geometry

    columns = 4
    rows = math.ceil(len(all_state_images) / columns)
    sheet = Image.new("RGB", (1920, rows * 270), BG)
    for index, image in enumerate(all_state_images):
        sheet.paste(ImageOps.fit(image, (480, 270), Image.Resampling.LANCZOS), ((index % columns) * 480, (index // columns) * 270))
    contact = qa_dir / "source-state-contact-sheet.png"
    sheet.save(contact, format="PNG", optimize=False, compress_level=9)

    equations = []
    for record in panel_records:
        for text in record["permitted_text"]:
            if " = " in text or " ≤ " in text:
                equations.append(text)
    if equations != pipeline.EXPECTED_EQUATIONS:
        raise RuntimeError(f"equation projection mismatch: {equations!r}")

    asset_receipt = {
        "status": "PASS_ONE_SHASUM_PER_PIN_BEFORE_EMBEDDING",
        "manifest": str(pipeline.PINS.relative_to(pipeline.ROOT)),
        "manifest_sha256": pipeline.sha256(pipeline.PINS),
        "records": frozen["asset_pins"],
    }
    (qa_dir / "asset-pins.json").write_text(json.dumps(asset_receipt, indent=2) + "\n", encoding="utf-8")
    receipt = {
        "status": "PASS_SOURCE_STATE_RENDER",
        "resolution": [W, H],
        "font_path": str(FONT_PATH),
        "font_sha256": sha256(FONT_PATH),
        "font_choice_reason": FONT_REASON,
        "required_glyph_support": GLYPH_SUPPORT,
        "equations_projected_exactly": equations,
        "other_equations_projected": False,
        "no_plots_panels": pipeline.EXPECTED_NO_PLOTS_PANELS,
        "paper_assets_verified_before_embedding": True,
        "asset_pin_receipt": str((qa_dir / "asset-pins.json").relative_to(output_root)),
        "cursor_asset": str(cursor_path.relative_to(output_root)),
        "cursor_asset_sha256": sha256(cursor_path),
        "panels": panel_records,
        "quantitative_geometry": quantitative_geometry,
        "source_contact_sheet": str(contact.relative_to(output_root)),
        "source_contact_sheet_sha256": sha256(contact),
    }
    (qa_dir / "card-text-and-geometry-audit.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return receipt


def main() -> int:
    receipt = render_all_cards(pipeline.BUILD)
    states = sum(len(panel["states"]) for panel in receipt["panels"])
    print(json.dumps({"status": receipt["status"], "panels": len(receipt["panels"]), "states": states, "font": receipt["font_path"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
