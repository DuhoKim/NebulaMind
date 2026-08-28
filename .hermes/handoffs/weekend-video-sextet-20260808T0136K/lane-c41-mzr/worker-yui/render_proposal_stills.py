#!/usr/bin/env python3
"""Render proposal-only scientific stills; never creates video or audio."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

LANE = Path(__file__).resolve().parent
OUT = LANE / "proposals/stills-v2"
EVIDENCE = json.loads((LANE / "EVIDENCE_FREEZE.json").read_text())

W, H = 1920, 1080
BG = (10, 15, 26)
PANEL = (19, 28, 45)
FG = (235, 241, 250)
DIM = (162, 176, 199)
GRID = (52, 67, 91)
TABLE = (238, 170, 96)
ROW = (91, 203, 218)
ANCHOR = (113, 171, 255)
WARN = (232, 112, 112)
GOOD = (116, 199, 145)
PURPLE = (187, 144, 255)

FONT_REGULAR = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/SFNS.ttf",
]
FONT_BOLD = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/SFNS.ttf",
]


def font(size: int, bold: bool = False) -> Any:
    for candidate in (FONT_BOLD if bold else FONT_REGULAR):
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def wrapped(draw: ImageDraw.ImageDraw, text: str, fnt: Any, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def text_block(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: Any,
    fill: tuple[int, int, int],
    width: int,
    spacing: int = 8,
) -> int:
    x, y = xy
    for line in wrapped(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        bbox = draw.textbbox((x, y), line, font=fnt)
        y = int(y + bbox[3] - bbox[1] + spacing)
    return y


def base(title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 16, H), fill=ANCHOR)
    draw.text((80, 60), title, font=font(48, True), fill=FG)
    draw.text((82, 130), subtitle, font=font(28), fill=DIM)
    draw.rounded_rectangle((1480, 54, 1840, 112), radius=18, fill=(36, 50, 72))
    draw.text((1503, 70), "PROPOSAL STILL — NOT A CANDIDATE", font=font(19, True), fill=(190, 205, 228))
    return image, draw


def footer(draw: ImageDraw.ImageDraw) -> None:
    citation = (
        "Display citation: NebulaMind Autonomous Research Crew (2026), "
        "The Public-Archive Direct-Te Anchor Gap at z>3, §§3–4"
    )
    draw.line((80, 1000, 1840, 1000), fill=GRID, width=2)
    draw.text((80, 1020), citation, font=font(22), fill=(115, 132, 159))


def render_pipeline() -> Path:
    image, draw = base(
        "The archive funnel — with the unit attached to every count",
        "Equal-width cards are deliberate: this is a sequence of changing units, not a proportional funnel.",
    )
    stages = EVIDENCE["funnel"]["stages"]
    colors = [TABLE, TABLE, TABLE, ROW, ANCHOR]
    extra = [
        "λ4363-class column",
        "redshift in-table or sibling join",
        "8 catalogs; 12 candidate tables unreachable",
        "tabulated λ4363 flux",
        "direct-Te abundance + linked stellar mass",
    ]
    left, y, card_w, card_h, gap = 80, 250, 320, 560, 45
    for index, stage in enumerate(stages):
        x = left + index * (card_w + gap)
        color = colors[index]
        draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=26, fill=PANEL, outline=color, width=4)
        draw.text((x + 28, y + 34), str(stage["count"]), font=font(96, True), fill=color)
        unit = stage["unit"].upper()
        text_block(draw, (x + 28, y + 152), unit, font(30, True), FG, card_w - 56, 6)
        draw.rounded_rectangle((x + 26, y + 235, x + card_w - 26, y + 291), radius=14, fill=(31, 43, 63))
        draw.text((x + 43, y + 251), f"STAGE {index + 1}", font=font(20, True), fill=color)
        text_block(draw, (x + 28, y + 325), extra[index], font(25), DIM, card_w - 56, 10)
        if index < len(stages) - 1:
            x1 = x + card_w + 8
            x2 = x + card_w + gap - 8
            mid = y + card_h // 2
            draw.line((x1, mid, x2, mid), fill=(106, 124, 151), width=5)
            draw.polygon(((x2, mid), (x2 - 14, mid - 10), (x2 - 14, mid + 10)), fill=(106, 124, 151))
    draw.rounded_rectangle((80, 842, 1840, 952), radius=22, fill=(21, 31, 49), outline=GRID, width=2)
    draw.text((118, 865), "UNIT PATH", font=font(22, True), fill=DIM)
    draw.text((330, 853), "TABLES  →  TABLES  →  TABLES  →  ROWS  →  ANCHORS", font=font(38, True), fill=FG)
    footer(draw)
    path = OUT / "01_unit_pipeline.png"
    image.save(path)
    return path


def render_row_accounting() -> Path:
    image, draw = base(
        "All ninety-five rows close exactly",
        "Proportional geometry is valid here because every segment has the same unit: rows.",
    )
    counts = EVIDENCE["exclusion_accounting"]
    categories = [
        ("sn4363_below_floor", "below S/N floor", TABLE),
        ("no_hbeta", "no Hβ", PURPLE),
        ("missing_flux", "missing flux", WARN),
        ("te_failure", "Te failure", (218, 132, 104)),
        ("contract_grade_anchor", "contract-grade anchor", ANCHOR),
    ]
    cells: list[tuple[str, tuple[int, int, int]]] = []
    for key, label, color in categories:
        cells.extend([(label, color)] * counts[key])
    if len(cells) != 95:
        raise ValueError(f"row accounting changed: {len(cells)}")

    cols, cell, gap = 19, 54, 7
    start_x, start_y = 95, 280
    for index, (_, color) in enumerate(cells):
        row, col = divmod(index, cols)
        x = start_x + col * (cell + gap)
        y = start_y + row * (cell + gap)
        draw.rounded_rectangle((x, y, x + cell, y + cell), radius=9, fill=color)
    draw.text((95, 620), "95 ROWS", font=font(46, True), fill=FG)
    draw.text((95, 680), "90 exclusions + 5 survivors", font=font(34), fill=DIM)

    legend_x, legend_y = 1310, 280
    for index, (key, label, color) in enumerate(categories):
        y = legend_y + index * 105
        draw.rounded_rectangle((legend_x, y, legend_x + 48, y + 48), radius=8, fill=color)
        draw.text((legend_x + 70, y - 4), str(counts[key]), font=font(40, True), fill=FG)
        draw.text((legend_x + 140, y + 6), label, font=font(27), fill=DIM)
    draw.rounded_rectangle((1310, 825, 1815, 935), radius=22, fill=(21, 31, 49), outline=ANCHOR, width=3)
    draw.text((1340, 850), "UNIT REMAINS: ROWS", font=font(30, True), fill=ANCHOR)
    draw.text((1340, 892), "No table/anchor conflation", font=font(22), fill=DIM)
    footer(draw)
    path = OUT / "02_row_accounting.png"
    image.save(path)
    return path


def render_mass_bins() -> Path:
    image, draw = base(
        "The mass-bin result is a decision-threshold null",
        "Actual anchor counts share one pre-committed minimum. The separate below-floor pool is not a fourth bin.",
    )
    mass = EVIDENCE["mass_bin_null"]
    counts = list(mass["actual_anchor_counts"].values())
    threshold = mass["shared_minimum_per_bin"]
    below = mass["below_frozen_logM_8_floor"]

    chart = (180, 250, 1390, 850)
    x0, y0, x1, y1 = chart
    draw.rectangle(chart, fill=(14, 21, 35), outline=GRID, width=2)
    scale = (y1 - y0) / 4
    for tick in range(5):
        y = int(y1 - tick * scale)
        draw.line((x0, y, x1, y), fill=(35, 48, 68), width=2)
        draw.text((x0 - 55, y - 18), str(tick), font=font(24), fill=DIM)
    label = Image.new("RGBA", (430, 52), (0, 0, 0, 0))
    label_draw = ImageDraw.Draw(label)
    label_draw.text((0, 6), "contract-grade anchors, N", font=font(26, True), fill=DIM)
    label = label.rotate(90, expand=True)
    image.paste(label, (62, 330), label)

    threshold_y = int(y1 - threshold * scale)
    draw.line((x0, threshold_y, x1, threshold_y), fill=WARN, width=5)
    draw.rounded_rectangle((905, threshold_y - 58, 1365, threshold_y - 10), radius=12, fill=(64, 35, 42))
    draw.text((928, threshold_y - 48), "SHARED MINIMUM  N = 3", font=font(24, True), fill=(255, 181, 181))

    labels = ["8 <= log10 M* < 9", "9 <= log10 M* < 10", "log10 M* >= 10"]
    centers = [400, 770, 1140]
    for value, label, center in zip(counts, labels, centers):
        bar_w = 190
        top = int(y1 - value * scale)
        if value > 0:
            draw.rounded_rectangle((center - bar_w // 2, top, center + bar_w // 2, y1), radius=18, fill=ANCHOR)
        else:
            draw.line((center - bar_w // 2, y1 - 3, center + bar_w // 2, y1 - 3), fill=ANCHOR, width=7)
        draw.text((center - 18, top - 58), str(value), font=font(46, True), fill=FG)
        bbox = draw.textbbox((0, 0), label, font=font(24, True))
        draw.text((center - (bbox[2] - bbox[0]) // 2, y1 + 30), label, font=font(24, True), fill=DIM)

    draw.text((540, 930), "stellar-mass bin, log10(M*/M_sun)", font=font(28, True), fill=DIM)

    draw.rounded_rectangle((1460, 270, 1815, 745), radius=24, fill=PANEL, outline=TABLE, width=4)
    draw.text((1500, 315), str(below), font=font(92, True), fill=TABLE)
    draw.text((1500, 425), "ANCHORS", font=font(30, True), fill=FG)
    draw.text((1500, 468), "log10(M*/M_sun) < 8", font=font(25, True), fill=TABLE)
    text_block(draw, (1500, 535), "below frozen bin floor — binned nowhere", font(25), DIM, 270, 9)
    draw.rounded_rectangle((1460, 780, 1815, 940), radius=24, fill=(39, 27, 36), outline=WARN, width=3)
    draw.text((1500, 813), "NO DEFICIT", font=font(30, True), fill=(255, 181, 181))
    draw.text((1500, 856), "VERDICT POSSIBLE", font=font(30, True), fill=(255, 181, 181))
    draw.text((1500, 902), "all bins below N = 3", font=font(22), fill=DIM)
    footer(draw)
    path = OUT / "03_mass_bin_threshold.png"
    image.save(path)
    return path


def render_boundary() -> Path:
    image, draw = base(
        "What the result says — and what it does not say",
        "The boundary must remain visually dominant through the final held frame.",
    )
    draw.rounded_rectangle((90, 250, 910, 875), radius=28, fill=(18, 34, 38), outline=GOOD, width=4)
    draw.text((140, 305), "REPORTABLE", font=font(34, True), fill=GOOD)
    left_lines = [
        "5 contract-grade public anchors",
        "2 / 1 / 0 inside frozen mass bins",
        "+2 below the logM = 8 bin floor",
        "every bin below N = 3",
        "no deficit verdict possible",
    ]
    y = 390
    for line in left_lines:
        draw.ellipse((145, y + 7, 165, y + 27), fill=GOOD)
        y = text_block(draw, (190, y), line, font(30), FG, 650, 8) + 30

    draw.rounded_rectangle((1010, 250, 1830, 875), radius=28, fill=(42, 25, 31), outline=WARN, width=4)
    draw.text((1060, 305), "NOT ESTABLISHED", font=font(34, True), fill=(255, 171, 171))
    right_lines = [
        "a calibrated high-z relation",
        "a deficit of any size or direction",
        "local diagnostics validated or invalidated",
        "anchors absent from the sky",
        "an FMR result",
    ]
    y = 390
    for line in right_lines:
        draw.line((1060, y + 17, 1080, y + 17), fill=WARN, width=5)
        y = text_block(draw, (1105, y), line, font(30), FG, 650, 8) + 30

    draw.rounded_rectangle((270, 900, 1650, 970), radius=20, fill=(27, 38, 58), outline=ANCHOR, width=3)
    draw.text((330, 918), "ARCHIVE CENSUS — NOT A GALAXY RELATION", font=font(36, True), fill=ANCHOR)
    footer(draw)
    path = OUT / "04_scientific_boundary.png"
    image.save(path)
    return path


def contact_sheet(paths: list[Path]) -> Path:
    thumb_w, thumb_h = 800, 450
    sheet = Image.new("RGB", (thumb_w * 2 + 60, thumb_h * 2 + 60), BG)
    for index, path in enumerate(paths):
        image = Image.open(path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = 20 + (index % 2) * (thumb_w + 20)
        y = 20 + (index // 2) * (thumb_h + 20)
        sheet.paste(image, (x, y))
    output = OUT / "contact_sheet.png"
    sheet.save(output)
    return output


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    paths = [render_pipeline(), render_row_accounting(), render_mass_bins(), render_boundary()]
    sheet = contact_sheet(paths)
    print(sheet)


if __name__ == "__main__":
    main()
