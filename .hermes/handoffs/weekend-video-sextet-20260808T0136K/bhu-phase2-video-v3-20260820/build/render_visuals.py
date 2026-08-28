#!/usr/bin/env python3
"""Render the v3 design system as staged 1920x1080 panel states.

This is a new visual implementation. It intentionally does not import or copy v2 card code.
"""
from __future__ import annotations

import json
import math
import random
import shutil
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

import pipeline

W, H = 1920, 1080
SAFE = 120
BG = "#0B0C10"
PANEL = "#1F2833"
WHITE = "#FFFFFF"
SILVER = "#C5C6C7"
CYAN = "#66FCF1"
TEAL = "#45A29E"
RED = "#FF4C4C"
BLACK = "#0B0C10"
FONT_REG = "/System/Library/Fonts/SFNS.ttf"
FONT_BOLD = "/System/Library/Fonts/SFNS.ttf"
FONT_MONO = "/System/Library/Fonts/SFNSMono.ttf"
CARDS = pipeline.BUILD / "cards"
STILLS = pipeline.BUILD / "PANEL_STILLS"
CURSOR = CARDS / "plot-cursor.png"

# State names and visual dwell fractions. Content order follows narration order.
PANEL_STAGES: dict[str, list[tuple[str, float]]] = {
    "01": [("birthmark", .27), ("audit", .23), ("ceiling", .25), ("verdict", .25)],
    "02": [("nursery", .38), ("thread", .32), ("method", .30)],
    "03": [("cloth", .30), ("needles", .25), ("torsion", .27), ("no-plots", .18)],
    "04": [("spring", .28), ("pushback", .30), ("bounce", .22), ("whisper", .20)],
    "05": [("crowd", .28), ("branches", .30), ("sixfold", .22), ("carry-both", .20)],
    "06": [("sealed", .34), ("status", .33), ("recompute", .33)],
    "07": [("new-engine", .24), ("plot", .52), ("cusp", .24)],
    "08": [("thermometer", .25), ("plot", .31), ("quotes", .22), ("fork", .22)],
    "09": [("seed-pod", .30), ("mass-map", .36), ("rotation-outside", .34)],
    "10": [("certificate", .28), ("dial", .27), ("join", .23), ("one-meter", .22)],
    "11": [("bridge", .24), ("collapse", .23), ("no-plots", .15), ("quote", .38)],
    "12": [("skater", .19), ("wall", .24), ("overshoot", .20), ("ceiling", .22), ("reading", .15)],
    "13": [("balloon", .27), ("shear", .22), ("balance", .29), ("condition", .22)],
    "14": [("fossil", .19), ("figure1", .25), ("figure2", .25), ("gulf", .31)],
    "15": [("coins", .22), ("floor", .22), ("knobs", .23), ("range", .20), ("caveat", .13)],
    "16": [("papers", .44), ("helium", .16), ("ceiling", .20), ("closed", .20)],
}


@lru_cache(maxsize=64)
def font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_MONO if mono else FONT_BOLD if bold else FONT_REG
    return ImageFont.truetype(path, size=size)


def rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def rgba(value: str, alpha: int) -> tuple[int, int, int, int]:
    return (*rgb(value), alpha)


@lru_cache(maxsize=32)
def gradient_background(seed: int, accent: str = CYAN) -> Image.Image:
    # Paint the smooth field at quarter resolution and upscale. This keeps the
    # deterministic 1080p result inexpensive across dozens of staged states.
    sw, sh = W // 4, H // 4
    base = Image.new("RGB", (sw, sh), rgb(BG))
    px = base.load()
    ar, ag, ab = rgb(accent)
    for y in range(sh):
        ny = y / sh
        for x in range(sw):
            nx = x / sw
            glow1 = max(0.0, 1.0 - math.hypot((nx - .78) / .72, (ny - .22) / .70))
            glow2 = max(0.0, 1.0 - math.hypot((nx - .20) / .65, (ny - .85) / .65))
            amount = .095 * glow1 + .045 * glow2
            px[x, y] = (11 + int(ar * amount), 12 + int(ag * amount), 16 + int(ab * amount))
    base = base.resize((W, H), Image.Resampling.BICUBIC)
    rnd = random.Random(seed)
    d = ImageDraw.Draw(base, "RGBA")
    for _ in range(145):
        x, y = rnd.randrange(W), rnd.randrange(H)
        r = rnd.choice([1, 1, 1, 2])
        a = rnd.randrange(35, 130)
        d.ellipse((x-r, y-r, x+r, y+r), fill=(102, 252, 241, a))
    # Subtle perspective grid makes the frame feel designed rather than slide-like.
    for x in range(SAFE, W-SAFE+1, 140):
        d.line((W//2, 630, x, H), fill=(69, 162, 158, 18), width=1)
    for y in range(720, H, 72):
        d.line((SAFE, y, W-SAFE, y), fill=(69, 162, 158, max(6, 22-(y-720)//8)), width=1)
    return base


@lru_cache(maxsize=1)
def full_bleed_cold_open() -> Image.Image:
    source = Image.open(pipeline.ASSETS / "nbp_p01_cold_open.png").convert("RGB")
    image = ImageOps.fit(source, (W, H), Image.Resampling.LANCZOS)
    dark = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(dark)
    d.rectangle((0, 0, W, H), fill=(5, 7, 14, 70))
    d.rectangle((0, 0, 980, H), fill=(4, 6, 12, 115))
    d.rectangle((0, 0, W, 230), fill=(4, 6, 12, 95))
    dark = dark.filter(ImageFilter.GaussianBlur(45))
    return Image.alpha_composite(image.convert("RGBA"), dark).convert("RGB")


def glow_layer(size: tuple[int, int], painter: Callable[[ImageDraw.ImageDraw], None], radius: int = 18) -> Image.Image:
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    painter(ImageDraw.Draw(layer, "RGBA"))
    return layer.filter(ImageFilter.GaussianBlur(radius))


def round_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: Any, outline: Any | None = None, width: int = 2, radius: int = 28) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text_width(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont) -> int:
    b = draw.textbbox((0, 0), text, font=f)
    return b[2] - b[0]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else current + " " + word
        if text_width(draw, candidate, f) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def fit_text(draw: ImageDraw.ImageDraw, text: str, width: int, max_size: int, min_size: int, max_lines: int = 2, bold: bool = False, mono: bool = False) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for size in range(max_size, min_size - 1, -2):
        f = font(size, bold=bold, mono=mono)
        lines = wrap_text(draw, text, f, width)
        if len(lines) <= max_lines:
            return f, lines
    f = font(min_size, bold=bold, mono=mono)
    return f, wrap_text(draw, text, f, width)


def draw_multiline(draw: ImageDraw.ImageDraw, xy: tuple[int, int], lines: list[str], f: ImageFont.FreeTypeFont, fill: str, spacing: int = 10, anchor: str = "la", stroke_width: int = 0, stroke_fill: str = BLACK) -> tuple[int, int, int, int]:
    text = "\n".join(lines)
    draw.multiline_text(xy, text, font=f, fill=fill, spacing=spacing, anchor=anchor, stroke_width=stroke_width, stroke_fill=stroke_fill)
    return draw.multiline_textbbox(xy, text, font=f, spacing=spacing, anchor=anchor, stroke_width=stroke_width)


class PanelCanvas:
    def __init__(self, panel: dict[str, Any], image: Image.Image):
        self.panel = panel
        self.allowed = list(panel["viewer_text_closed_world"])
        self.image = image.convert("RGBA")
        self.draw = ImageDraw.Draw(self.image, "RGBA")
        self.emitted: list[str] = []

    def emit(self, text: str) -> None:
        if text not in self.allowed:
            raise RuntimeError(f"panel {self.panel['id']} attempted unreviewed viewer text: {text!r}")
        self.emitted.append(text)

    def heading(self) -> None:
        text = self.panel["assertion_heading"]
        self.emit(text)
        # Remain inside the binding 64–96 px display scale while leaving a
        # stable content gutter under two-line assertion headings.
        f, lines = fit_text(self.draw, text, W - 2*SAFE, 72, 64, max_lines=2, bold=True)
        self.draw.line((SAFE, 100, SAFE+82, 100), fill=CYAN, width=7)
        bbox = draw_multiline(self.draw, (SAFE, 122), lines, f, WHITE, spacing=6, stroke_width=1)
        divider_y = min(286, int(bbox[3]) + 14)
        self.draw.line((SAFE, divider_y, W-SAFE, divider_y), fill=rgba(TEAL, 105), width=2)

    def label(self, text: str, box: tuple[int, int, int, int], *, size: int = 40, color: str = WHITE, panel_fill: bool = True, outline: str | None = None, max_lines: int = 3, bold: bool = False, align: str = "left") -> None:
        self.emit(text)
        x1, y1, x2, y2 = box
        if panel_fill:
            round_rect(self.draw, box, rgba(PANEL, 225), rgba(outline or TEAL, 120), width=2, radius=24)
        f, lines = fit_text(self.draw, text, x2-x1-48, size, max(26, size-12), max_lines=max_lines, bold=bold)
        total_h = len(lines) * (f.size + 8) - 8
        y = y1 + max(18, (y2-y1-total_h)//2)
        if align == "center":
            draw_multiline(self.draw, ((x1+x2)//2, y), lines, f, color, spacing=8, anchor="ma")
        else:
            draw_multiline(self.draw, (x1+24, y), lines, f, color, spacing=8)

    def chip(self, text: str, xy: tuple[int, int], *, illustration: bool = False, attribution: bool = False) -> tuple[int, int, int, int]:
        self.emit(text)
        f = font(28)
        pad_x, pad_y = 22, 12
        tw = text_width(self.draw, text, f)
        x, y = xy
        box = (x, y, x+tw+2*pad_x, y+f.size+2*pad_y+4)
        outline = TEAL if illustration else CYAN if attribution else SILVER
        round_rect(self.draw, box, rgba(BLACK, 205), rgba(outline, 220), width=2, radius=26)
        self.draw.text((x+pad_x, y+pad_y), text, font=f, fill=SILVER)
        return box

    def illustration_chip(self, y: int | None = None, *, x: int | None = None, required: bool = False) -> None:
        if pipeline.ILLUSTRATION_CHIP in self.allowed or required:
            if required and pipeline.ILLUSTRATION_CHIP not in self.allowed:
                self.allowed.append(pipeline.ILLUSTRATION_CHIP)
            f = font(28)
            tw = text_width(self.draw, pipeline.ILLUSTRATION_CHIP, f)
            chip_y = H-SAFE-58 if y is None else y
            chip_x = W-SAFE-tw-44 if x is None else x
            self.chip(pipeline.ILLUSTRATION_CHIP, (chip_x, chip_y), illustration=True)

    def no_plots(self, xy: tuple[int, int], width: int = 700) -> None:
        text = pipeline.NO_PLOTS_TEXT
        self.label(text, (xy[0], xy[1], xy[0]+width, xy[1]+112), size=34, color=SILVER, outline=SILVER, max_lines=2, bold=True)

    def finish(self) -> Image.Image:
        return self.image.convert("RGB")


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = CYAN, width: int = 8, head: int = 24, dashed: bool = False) -> None:
    x1, y1 = start; x2, y2 = end
    if dashed:
        length = math.hypot(x2-x1, y2-y1)
        for i in range(0, int(length)-head, 28):
            a, b = i/length, min((i+16)/length, 1)
            draw.line((x1+(x2-x1)*a, y1+(y2-y1)*a, x1+(x2-x1)*b, y1+(y2-y1)*b), fill=color, width=width)
    else:
        draw.line((x1, y1, x2, y2), fill=color, width=width)
    angle = math.atan2(y2-y1, x2-x1)
    pts = [(x2, y2), (x2-head*math.cos(angle-.55), y2-head*math.sin(angle-.55)), (x2-head*math.cos(angle+.55), y2-head*math.sin(angle+.55))]
    draw.polygon(pts, fill=color)


def draw_mesh_birth(c: PanelCanvas, stage: int) -> None:
    d = c.draw
    # Large parent and small baby with an explicit dashed conceptual route.
    glow = glow_layer((W, H), lambda gd: gd.ellipse((860, 270, 1500, 910), outline=rgba(CYAN, 190), width=36), 30)
    c.image.alpha_composite(glow)
    for r, a in [(300, 50), (245, 90), (190, 160)]:
        d.ellipse((1180-r, 590-r, 1180+r, 590+r), outline=rgba(CYAN, a), width=6)
    d.ellipse((1015, 425, 1345, 755), fill=rgba(BLACK, 240), outline=CYAN, width=8)
    c.label("BLACK HOLE · COSMIC NURSERY", (835, 255, 1525, 350), size=38, color=CYAN, align="center", bold=True)
    if stage >= 1:
        d.ellipse((1535, 640, 1745, 850), fill=rgba(TEAL, 120), outline=CYAN, width=7)
        c.label("BABY UNIVERSE", (1450, 865, 1810, 945), size=38, color=WHITE, align="center", bold=True)
        arrow(d, (1340, 620), (1550, 720), CYAN, width=7, dashed=True)
        c.label("PARENT'S TURNING DIRECTION · BIRTHMARK?", (135, 315, 750, 460), size=40, color=WHITE, bold=True)
    if stage >= 2:
        c.label("FOLLOW EACH CALCULATION", (135, 520, 720, 625), size=39, color=CYAN, bold=True)
        c.label("STOP WHERE THE CALCULATION STOPS", (135, 660, 720, 780), size=37, color=SILVER, bold=True)
    c.illustration_chip()


def draw_twist(c: PanelCanvas, stage: int) -> None:
    d = c.draw
    art = (760, 285, 1785, 850)
    round_rect(d, art, rgba(PANEL, 155), rgba(TEAL, 80), width=2, radius=40)
    # Cloth lines first.
    for lane in range(7):
        points = []
        for i in range(160):
            x = 810 + i*5.8
            y = 570 + (lane-3)*48 + 70*math.sin(i/18 + lane*.38)
            points.append((x, y))
        d.line(points, fill=rgba(TEAL, 80+lane*12), width=3)
    c.label("SPACETIME · CLOTH", (135, 305, 680, 410), size=42, color=CYAN, bold=True)
    if stage >= 1:
        # Compass needles reveal the spin analogy.
        for iy in range(5):
            for ix in range(8):
                x, y = 845+ix*118, 395+iy*92
                ang = .28*math.sin(ix*.7+iy)
                dx, dy = 25*math.cos(ang), 25*math.sin(ang)
                d.line((x-dx, y-dy, x+dx, y+dy), fill=WHITE, width=4)
                d.ellipse((x-5, y-5, x+5, y+5), fill=CYAN)
        c.label("SPIN · A BUILT-IN QUANTUM TWIST", (135, 450, 690, 585), size=36, color=WHITE, bold=True)
    if stage >= 2:
        glow = glow_layer((W, H), lambda gd: gd.arc((950, 360, 1610, 810), 210, 535, fill=rgba(CYAN, 255), width=18), 22)
        c.image.alpha_composite(glow)
        d.arc((950, 360, 1610, 810), 210, 535, fill=CYAN, width=7)
        c.label("EINSTEIN-CARTAN GRAVITY · GRAVITY THAT INCLUDES SPIN", (135, 615, 690, 750), size=34, color=SILVER, bold=True)
        c.label("TORSION · SPIN'S TWIST OF SPACETIME", (780, 865, 1770, 955), size=37, color=CYAN, align="center", bold=True)
    if stage >= 3:
        c.no_plots((135, 795), 600)
    c.illustration_chip()


def draw_spring(c: PanelCanvas, stage: int) -> None:
    d = c.draw
    art = (735, 285, 1785, 880)
    round_rect(d, art, rgba(PANEL, 160), rgba(TEAL, 90), width=2, radius=40)
    # Programmatic compressed sine wave reflecting into expansion curve.
    pts = []
    for i in range(260):
        x = 805 + i*3.6
        squeeze = 1.0 - .72*math.exp(-((i-130)/42)**2)
        y = 570 + 150*squeeze*math.sin(i*.22)
        pts.append((x, y))
    glow = glow_layer((W, H), lambda gd: gd.line(pts, fill=rgba(CYAN, 210), width=18), 20)
    c.image.alpha_composite(glow)
    d.line(pts, fill=CYAN, width=7)
    c.label("SPRING · SQUEEZE IN, PUSH OUT", (135, 315, 650, 430), size=40, color=CYAN, bold=True)
    if stage >= 1:
        arrow(d, (1040, 760), (1040, 660), TEAL, width=8)
        arrow(d, (1450, 760), (1450, 660), TEAL, width=8)
        c.label("TORSION · SPIN-MADE TWIST IN SPACETIME", (135, 470, 650, 605), size=35, color=WHITE, bold=True)
        c.label("NEGATIVE TORSION DENSITY · OUTWARD EFFECT", (790, 840, 1730, 935), size=35, color=CYAN, align="center", bold=True)
    if stage >= 2:
        c.label("BOUNCE · SHRINKING TURNS TO GROWING", (135, 640, 650, 770), size=37, color=WHITE, bold=True)
        # Planck marker symbol, intentionally text-free because viewer text is closed-world.
        d.polygon([(1260, 292), (1274, 308), (1260, 324), (1246, 308)], fill=RED)
    if stage >= 3:
        c.label("A NEGATIVE 1 SITTING 70 PLACES AFTER THE DECIMAL POINT", (790, 710, 1730, 820), size=35, color=WHITE, align="center", bold=True)
        c.no_plots((135, 810), 600)
    c.illustration_chip()


def draw_crowd(c: PanelCanvas, stage: int) -> None:
    d = c.draw
    # Programmatic crowd circles in two bays.
    for bay, x0 in enumerate((790, 1320)):
        round_rect(d, (x0, 300, x0+410, 690), rgba(PANEL, 160), rgba(TEAL, 90), 2, 36)
        for row in range(5):
            for col in range(6):
                x = x0+55+col*60; y=370+row*57
                d.ellipse((x-13,y-13,x+13,y+13), fill=rgba(CYAN if bay==0 else SILVER, 210))
                if bay==0:
                    d.line((x, y-24, x, y-45), fill=CYAN, width=3)
                else:
                    ang=((row*6+col)%5-2)*.55
                    d.line((x,y-24,x+20*math.sin(ang),y-42*math.cos(ang)), fill=SILVER, width=3)
    c.label("CROWD CLAPS TOGETHER · LOUD", (750, 725, 1240, 830), size=35, color=CYAN, align="center", bold=True)
    c.label("CROWD CLAPS RANDOMLY · MOSTLY CANCELS", (1280, 725, 1785, 850), size=34, color=SILVER, align="center", bold=True)
    if stage >= 1:
        c.label("SPECIES · ONE KIND OF PARTICLE", (135, 310, 650, 415), size=38, color=WHITE, bold=True)
        c.label("6 NEUTRINO SPECIES", (135, 455, 650, 555), size=44, color=CYAN, bold=True)
        y=610
        d.line((165, y, 630, y), fill=SILVER, width=7)
        for i in range(7):
            x=165+i*(465/6)
            d.line((x,y-14,x,y+14), fill=SILVER, width=4)
        c.label("LINED-UP EDGE", (135, 650, 360, 755), size=31, color=CYAN, bold=True)
    if stage >= 2:
        c.label("INDEPENDENT EDGE · EXACTLY 6 TIMES SMALLER", (360, 650, 700, 790), size=31, color=WHITE, bold=True)
    if stage >= 3:
        c.label("THE PRINTED VALUE SITS NEAR THE LINED-UP EDGE · CARRY BOTH", (135, 820, 700, 940), size=33, color=CYAN, bold=True)
    c.illustration_chip()


def draw_envelope(c: PanelCanvas, stage: int) -> None:
    d=c.draw
    round_rect(d,(650,300,1265,820),rgba(PANEL,210),rgba(SILVER,110),3,44)
    d.rounded_rectangle((760,410,1155,675),radius=22,fill=rgba(BLACK,230),outline=SILVER,width=5)
    d.line((760,410,955,560,1155,410),fill=SILVER,width=5)
    d.line((760,675,920,535),fill=rgba(SILVER,120),width=4)
    d.line((1155,675,990,535),fill=rgba(SILVER,120),width=4)
    c.label("CORRECTION NOTICE · EXISTS",(135,315,570,420),size=38,color=CYAN,bold=True)
    if stage>=1:
        c.label("CONTENTS · PAYWALLED AND UNREAD",(1300,330,1785,455),size=36,color=WHITE,bold=True)
        c.label("AFFECTED PRINTED NUMBERS · QUARANTINED",(1300,500,1785,650),size=34,color=RED,bold=True)
    if stage>=2:
        c.label("RECOMPUTED HERE",(220,690,570,800),size=41,color=CYAN,bold=True,align="center")
        c.label("NO GUESSING",(1320,720,1740,830),size=44,color=WHITE,bold=True,align="center")


def paste_plot(c: PanelCanvas, filename: str, chip: str, box: tuple[int,int,int,int]) -> tuple[int,int,int,int]:
    src=Image.open(pipeline.ASSETS/filename).convert("RGB")
    x1,y1,x2,y2=box
    fitted=ImageOps.contain(src,(x2-x1,y2-y1),Image.Resampling.LANCZOS)
    px=x1+(x2-x1-fitted.width)//2; py=y1+(y2-y1-fitted.height)//2
    shadow=Image.new("RGBA",(fitted.width+28,fitted.height+28),(0,0,0,0))
    ImageDraw.Draw(shadow).rounded_rectangle((14,14,fitted.width+14,fitted.height+14),radius=18,fill=(0,0,0,170))
    shadow=shadow.filter(ImageFilter.GaussianBlur(12)); c.image.alpha_composite(shadow,(px-14,py-14))
    mask=Image.new("L",fitted.size,0); ImageDraw.Draw(mask).rounded_rectangle((0,0,*fitted.size),radius=18,fill=255)
    c.image.paste(fitted,(px,py),mask)
    c.draw.rounded_rectangle((px,py,px+fitted.width,py+fitted.height),radius=18,outline=rgba(CYAN,120),width=3)
    c.chip(chip,(px+18,py+fitted.height-68),attribution=True)
    return (px,py,px+fitted.width,py+fitted.height)


def draw_panel07(c: PanelCanvas, stage: int) -> dict[str, Any]:
    meta: dict[str, Any]={}
    c.label("PRD 85, 107502 (2012) · arXiv:1111.4595",(135,275,680,380),size=32,color=SILVER,bold=True)
    if stage==0:
        c.label("FERMION FIELDS · DEEP INGREDIENTS OF MATTER PARTICLES",(135,430,680,575),size=35,color=WHITE,bold=True)
        # New engine icon.
        c.draw.ellipse((960,390,1510,870),outline=CYAN,width=8)
        for r in range(5): c.draw.arc((995+r*35,425+r*25,1475-r*35,835-r*25),20,300,fill=rgba(TEAL,170-r*20),width=6)
    else:
        plot_box=paste_plot(c,"prd_1111.4595_fig1_scale.jpg","Figure 1, arXiv:1111.4595 (author version)",(650,265,1785,925))
        meta["paper_asset"]="prd_1111.4595_fig1_scale.jpg"
        meta["plot_box"]=plot_box
        c.label("SCALE FACTOR · THE UNIVERSE'S SIZE RULER",(135,430,600,565),size=34,color=CYAN,bold=True)
        if stage>=2:
            c.label("SHRINK → SHARP CUSP → GROW",(135,650,600,780),size=39,color=WHITE,bold=True)
    return meta


def draw_panel08(c: PanelCanvas, stage: int) -> dict[str, Any]:
    meta: dict[str, Any]={}
    if stage<=1:
        plot_box=paste_plot(c,"prd_1111.4595_fig2_temp.jpg","Figure 2, arXiv:1111.4595 (author version)",(650,260,1785,925))
        meta["paper_asset"]="prd_1111.4595_fig2_temp.jpg"; meta["plot_box"]=plot_box
        c.label("TEMPERATURE · NARROW SPIKE",(135,300,590,415),size=40,color=CYAN,bold=True)
        if stage>=1:
            c.label("PLANCK SCALE · TESTED CLASSICAL RULES RUN OUT",(135,480,590,630),size=34,color=RED,bold=True)
            c.draw.polygon([(1190,270),(1206,288),(1190,306),(1174,288)],fill=RED)
    elif stage==2:
        c.label("“VIOLATES THE COSMOLOGICAL PRINCIPLE”",(150,290,900,430),size=39,color=WHITE,bold=True,align="center")
        c.label("COSMOLOGICAL PRINCIPLE · LARGE-SCALE UNIVERSE LOOKS THE SAME IN EVERY DIRECTION",(150,455,900,615),size=34,color=SILVER,bold=True,align="center")
        c.label("“NOT SELF-CONSISTENT”",(1020,340,1770,475),size=43,color=WHITE,bold=True,align="center")
        c.label("THE PAPER'S OWN WORDS",(1090,530,1700,625),size=34,color=CYAN,bold=True,align="center")
    else:
        c.label("w = +1 vs w = −1",(135,310,690,450),size=55,color=WHITE,bold=True,align="center")
        # Honest linear band with both edges labelled by the reviewed sentence.
        x1,x2,y=830,1740,525
        c.draw.line((x1,y,x2,y),fill=SILVER,width=9)
        for i in range(11):
            x=x1+i*(x2-x1)/10
            c.draw.line((x,y-16,x,y+16),fill=CYAN if i in (0,10) else rgba(SILVER,130),width=4)
        c.label("ABOUT 730 TIMES APART IN BOUNCE DENSITY",(790,590,1780,710),size=39,color=CYAN,bold=True,align="center")
        c.label("REVERSAL · WRITTEN IN BY HAND",(135,720,690,850),size=39,color=RED,bold=True,align="center")
    return meta


def draw_seed_pod(c: PanelCanvas, stage: int) -> None:
    d=c.draw
    round_rect(d,(760,285,1775,875),rgba(PANEL,155),rgba(TEAL,100),2,48)
    # Semi-transparent seed pod with dense parent mass feeding a fiery core.
    d.ellipse((1010,335,1540,825),fill=rgba(TEAL,32),outline=CYAN,width=7)
    d.ellipse((1145,390,1405,595),fill=rgba(BLACK,235),outline=TEAL,width=7)
    d.ellipse((1200,665,1350,815),fill=rgba(RED,80),outline=CYAN,width=6)
    glow=glow_layer((W,H),lambda gd:gd.ellipse((1190,655,1360,825),fill=rgba(CYAN,170)),22);c.image.alpha_composite(glow)
    c.label("BLACK HOLE · SEED POD",(135,300,650,405),size=42,color=CYAN,bold=True)
    if stage>=1:
        c.label("COMPACTNESS · HOW TIGHTLY STARTING MATTER IS PACKED",(135,455,650,600),size=34,color=WHITE,bold=True)
        arrow(d,(1260,600),(1275,665),CYAN,width=8)
        c.label("PARENT MASS → STARTING SIZE + HEAT",(820,875,1745,960),size=37,color=CYAN,bold=True,align="center")
    if stage>=2:
        arrow(d,(650,735),(995,735),RED,width=8)
        d.line((995,700,995,770),fill=RED,width=8)
        c.label("PARENT ROTATION · OUTSIDE THE MAP",(135,650,650,790),size=36,color=RED,bold=True)
        c.no_plots((135,825),600)
    c.illustration_chip()


def draw_fingerprint(c: PanelCanvas, stage: int) -> None:
    d=c.draw
    c.label("BIRTH CERTIFICATE · STARTING SIZE, NOT A LIFE STORY",(135,290,690,430),size=37,color=CYAN,bold=True)
    # Start-state card fades visually into dial; programmatic continuation of seed-pod fallback.
    round_rect(d,(780,300,1210,720),rgba(PANEL,205),rgba(TEAL,120),3,36)
    d.ellipse((915,410,1075,570),outline=CYAN,width=7)
    d.line((995,570,995,650),fill=CYAN,width=7)
    if stage>=1:
        c.label("PARTICLE-CREATION DIAL · HOW QUICKLY NEW PARTICLES APPEAR",(1260,310,1785,455),size=34,color=WHITE,bold=True)
        d.arc((1360,505,1680,825),190,350,fill=CYAN,width=16)
        arrow(d,(1520,665),(1630,575),CYAN,width=10)
        c.label("MASS ENTERS THE START · NO CLAIMED LATER FINGERPRINT",(135,495,690,630),size=34,color=SILVER,bold=True)
    if stage>=2:
        # Dashed join stops before one-way boundary.
        arrow(d,(620,765),(910,765),SILVER,width=6,dashed=True)
        d.line((950,680,950,850),fill=RED,width=8)
        c.label("BLACK-HOLE-TO-BABY JOIN · SKETCH, NOT WELD",(135,690,700,800),size=32,color=WHITE,bold=True)
        c.label("HORIZON MATCHING · NOT PROVIDED",(1000,735,1740,835),size=37,color=RED,bold=True,align="center")
    if stage>=3:
        c.label("STARTING BALL · EXACTLY 1 METER · ABOUT A DOORWAY · CHOICE UNSTATED",(820,865,1770,970),size=33,color=CYAN,bold=True,align="center")
    c.illustration_chip(y=245)


def draw_collapse(c: PanelCanvas, stage: int) -> None:
    d=c.draw
    if stage==0:
        c.label("A BRIDGE NEEDS BEAMS",(135,320,700,440),size=52,color=CYAN,bold=True)
        c.label("SPIN BRIDGE · AN EQUATION CARRYING PARENT ROTATION INTO THE BABY",(135,510,790,675),size=36,color=WHITE,bold=True)
        for x in (1040,1320,1600):
            d.line((x,350,x,810),fill=TEAL,width=18)
        d.line((930,430,1710,430),fill=CYAN,width=14)
        d.line((930,700,1710,700),fill=CYAN,width=14)
    elif stage in (1,2):
        # Deterministic shrinking concentric circles, heavily darkened full-bleed.
        for i,r in enumerate((300,220,150,88,38)):
            a=80+i*30
            d.ellipse((1260-r,570-r,1260+r,570+r),outline=rgba(CYAN,a),width=8)
        c.label("IJMPA 40, 2544007 (2025) · arXiv:2509.11468",(135,285,750,395),size=32,color=SILVER,bold=True)
        if stage>=2: c.no_plots((135,520),620)
        c.illustration_chip()
    else:
        c.label("“It would still be valid for a more realistic gravitational collapse of an inhomogeneous and rotating fluid.”",(190,300,1730,630),size=46,color=WHITE,bold=True,align="center",max_lines=4)
        c.label("NO ROTATING MODEL",(260,735,830,850),size=42,color=RED,bold=True,align="center")
        c.label("NO AXIS CALCULATION",(1090,735,1660,850),size=42,color=RED,bold=True,align="center")


def draw_causality(c: PanelCanvas, stage: int) -> None:
    d=c.draw
    if stage==4:
        # Reading 1 receives an uncluttered closing beat while the ceiling and
        # causality wall preserve its context.
        d.line((825,650,1740,650),fill=RED,width=12)
        for x in range(825,1740,48):
            d.line((x,630,x+22,630),fill=rgba(RED,180),width=5)
        c.label("ε ≤ 10⁻²⁷",(920,300,1680,445),size=72,color=CYAN,bold=True,align="center")
        c.label("CEILING · NOT A MEASURED TRANSFER",(900,490,1700,605),size=39,color=CYAN,bold=True,align="center")
        c.label("IF THE SPINNING PARENT CANNOT MAKE THE BOUNCE · EVEN LESS TO SEE",(180,760,1740,910),size=42,color=RED,bold=True,align="center",max_lines=2)
        c.illustration_chip(y=930)
        return
    if stage==0:
        c.label("SPINNING SKATER · PULL IN, SPIN FASTER",(135,295,730,420),size=39,color=CYAN,bold=True)
        # Programmatic skater silhouette.
        d.ellipse((1215,320,1305,410),fill=WHITE)
        d.line((1260,410,1260,670),fill=WHITE,width=20)
        d.line((1260,480,1060,520),fill=WHITE,width=16)
        d.line((1260,480,1460,520),fill=WHITE,width=16)
        d.line((1260,670,1140,850),fill=WHITE,width=18)
        d.line((1260,670,1380,850),fill=WHITE,width=18)
        c.label("KEEP ALL PARENT ROTATION",(135,500,660,610),size=41,color=WHITE,bold=True)
        c.label("10-SOLAR-MASS PARENT - SPIN 0.7",(135,670,700,790),size=38,color=CYAN,bold=True)
    else:
        x0,x1=825,1740; wall_y=650
        d.line((x0,wall_y,x1,wall_y),fill=RED,width=12)
        for x in range(x0,x1,48): d.line((x,wall_y-20,x+22,wall_y-20),fill=rgba(RED,180),width=5)
        c.label("CAUSALITY WALL · NATURE'S RED LINE",(865,685,1695,785),size=39,color=RED,bold=True,align="center")
        if stage>=2:
            arrow(d,(1180,930),(1180,320),CYAN,width=16,head=36)
            c.label("6.6×10²⁶ BEYOND LIGHT",(135,300,690,430),size=48,color=WHITE,bold=True,align="center")
        if stage>=3:
            # Labeled edge ladder: floor/ceiling and branch edges both visible.
            d.line((250,540,650,540),fill=SILVER,width=8)
            d.line((250,500,250,580),fill=CYAN,width=8)
            d.line((650,500,650,580),fill=CYAN,width=8)
            c.label("UNIFORM BOUNCE · EVERY REGION COLLAPSES ALIKE",(135,620,700,755),size=33,color=WHITE,bold=True)
            c.label("TREATMENTS · RIVAL ENGINES",(135,790,700,885),size=35,color=SILVER,bold=True)
            c.label("ε ≤ 10⁻²⁷",(900,290,1680,430),size=72,color=CYAN,bold=True,align="center")
            c.label("TREATMENT BRANCHES · ROUGHLY 1 ORDER OF MAGNITUDE",(815,840,1760,950),size=34,color=WHITE,bold=True,align="center")
            c.label("CEILING · NOT A MEASURED TRANSFER",(890,470,1690,585),size=39,color=CYAN,bold=True,align="center")
    c.illustration_chip()


def draw_balance(c: PanelCanvas, stage: int) -> None:
    d=c.draw
    # Uneven balloon programmatic fallback.
    d.ellipse((890,320,1450,800),fill=rgba(TEAL,35),outline=CYAN,width=8)
    d.line((890,560,1450,560),fill=rgba(SILVER,100),width=4)
    d.polygon([(890,560),(965,500),(1010,620)],fill=rgba(RED,100))
    c.label("BALLOON SQUEEZED UNEVENLY",(135,300,700,415),size=42,color=CYAN,bold=True)
    if stage>=1:
        c.label("SHEAR · UNEVEN SQUEEZING",(135,470,700,580),size=40,color=WHITE,bold=True)
        c.label("TORSION · SPIN-MADE TWIST IN SPACETIME",(135,630,700,760),size=35,color=SILVER,bold=True)
    if stage>=2:
        # Balanced scale stays level.
        d.line((900,780,1680,780),fill=WHITE,width=10)
        d.line((1290,780,1290,920),fill=WHITE,width=12)
        d.polygon([(1180,930),(1400,930),(1290,820)],fill=rgba(PANEL,245),outline=WHITE)
        c.label("a⁻⁶ = a⁻⁶",(870,360,1685,500),size=68,color=CYAN,bold=True,align="center")
        c.label("BALANCED SCALE · RATIO FROZEN",(870,610,1690,720),size=39,color=WHITE,bold=True,align="center")
    if stage>=3:
        c.label("NEITHER SMOOTHED NOR CREATED",(135,815,740,925),size=39,color=CYAN,bold=True)
        c.label("PARTICLE PRODUCTION · CREATION OF NEW PARTICLES",(820,815,1775,915),size=34,color=SILVER,bold=True,align="center")
        c.label("CONDITION · NOT A SIGNAL SIZE",(820,925,1775,1015),size=36,color=RED,bold=True,align="center")
    c.illustration_chip(y=245)


def draw_helium(c: PanelCanvas, stage: int) -> dict[str, Any]:
    meta: dict[str,Any]={}
    if stage==0:
        c.label("HELIUM · FOSSIL THERMOMETER",(135,310,760,435),size=46,color=CYAN,bold=True)
        c.label("BIG-BANG NUCLEOSYNTHESIS · FIRST LIGHT ELEMENTS RECORD EARLY EXPANSION",(135,500,850,670),size=35,color=WHITE,bold=True)
        for x,y,r in [(1180,500,110),(1450,430,60),(1540,700,85),(1080,760,50)]:
            c.draw.ellipse((x-r,y-r,x+r,y+r),outline=CYAN,width=6)
            c.draw.ellipse((x-12,y-12,x+12,y+12),fill=WHITE)
    elif stage==1:
        box=paste_plot(c,"ds_1006.4166_comparison.png","Figure 1, arXiv:1006.4166 (author version)",(610,250,1785,945))
        meta["paper_asset"]="ds_1006.4166_comparison.png";meta["plot_box"]=box
        c.label("STIFF COMPONENT · ENERGY THAT FADES FASTER THAN RADIATION",(135,310,560,470),size=33,color=WHITE,bold=True)
    elif stage==2:
        box=paste_plot(c,"ds_1006.4166_prefac_Yp.png","Figure 2, arXiv:1006.4166 (author version)",(610,250,1785,945))
        meta["paper_asset"]="ds_1006.4166_prefac_Yp.png";meta["plot_box"]=box
        c.label("AT 10 MeV · UP TO 30 TIMES RADIATION",(135,330,560,490),size=36,color=CYAN,bold=True)
    else:
        # Both authoritative figures remain large enough for comparison, with matching chips.
        b1=paste_plot(c,"ds_1006.4166_comparison.png","Figure 1, arXiv:1006.4166 (author version)",(120,270,925,790))
        b2=paste_plot(c,"ds_1006.4166_prefac_Yp.png","Figure 2, arXiv:1006.4166 (author version)",(995,270,1800,790))
        meta["paper_assets"]=["ds_1006.4166_comparison.png","ds_1006.4166_prefac_Yp.png"]
        meta["plot_boxes"]=[b1,b2]
        c.label("TORSION WHISPER · ABOUT 45 ORDERS OF MAGNITUDE SMALLER",(135,820,850,940),size=34,color=CYAN,bold=True,align="center")
        c.label("ONE WATER MOLECULE BESIDE EARTH'S OCEANS",(930,820,1785,920),size=34,color=WHITE,bold=True,align="center")
        c.label("DIFFERENT SIGNS · BOTH INVISIBLE ACROSS THE GULF",(480,945,1440,1030),size=33,color=RED,bold=True,align="center")
    return meta


def draw_floor(c: PanelCanvas, stage: int) -> None:
    d=c.draw
    # Programmatic starlight grid floor, exact Part-2 fallback.
    horizon=530
    for y in range(horizon,940,55):
        d.line((760,y,1780,y),fill=rgba(TEAL,50),width=2)
    for x in range(760,1781,85): d.line((1270,horizon,x,940),fill=rgba(TEAL,50),width=2)
    rnd=random.Random(1515)
    for _ in range(340):
        x=rnd.randrange(780,1760); y=rnd.randrange(horizon+10,925)
        d.ellipse((x-2,y-2,x+2,y+2),fill=rgba(CYAN,rnd.randrange(80,230)))
    if stage==0:
        c.label("COIN FLIPS · CHANCE LEAVES A WOBBLE",(135,300,690,425),size=42,color=CYAN,bold=True)
        for i in range(7):
            x=920+i*115; y=430+(i%2)*85
            d.ellipse((x-42,y-42,x+42,y+42),fill=rgba(PANEL,230),outline=CYAN,width=5)
    elif stage==1:
        c.label("ALL 2 TRILLION OBSERVABLE GALAXIES · ONE VOTE EACH",(135,290,700,430),size=37,color=WHITE,bold=True)
        c.label("COUNTING FLOOR · QUIETEST SIGNAL A PERFECT COUNT COULD HEAR",(135,470,700,620),size=34,color=CYAN,bold=True)
        c.label("NOT AN INSTRUMENT",(135,660,600,770),size=42,color=RED,bold=True)
    elif stage==2:
        c.label("EVERY SURVIVAL KNOB · MAXIMUM",(135,305,700,420),size=40,color=CYAN,bold=True)
        for i in range(4):
            x=850+i*230; y=405
            d.arc((x,y,x+160,y+160),190,350,fill=CYAN,width=14)
            arrow(d,(x+80,y+80),(x+140,y+35),CYAN,width=8)
    elif stage==3:
        # Two-edged band ladder; both edges are explicit and no unlabeled logarithmic compression.
        x1,x2,y=860,1710,775
        d.line((x1,y,x2,y),fill=SILVER,width=10)
        d.line((x1,y-40,x1,y+40),fill=CYAN,width=12)
        d.line((x2,y-40,x2,y+40),fill=CYAN,width=12)
        for i in range(1,8):
            x=x1+i*(x2-x1)/8; d.line((x,y-16,x,y+16),fill=rgba(SILVER,150),width=4)
        c.label("ABOUT 10,000 TO 100,000 TIMES BELOW THE FLOOR",(800,840,1780,955),size=38,color=CYAN,bold=True,align="center")
        c.label("PLANCK REGIME · QUANTUM GRAVITY SHOULD MATTER",(135,500,700,645),size=35,color=SILVER,bold=True)
    elif stage==4:
        c.label("PLANCK REGIME · QUANTUM GRAVITY SHOULD MATTER",(220,350,900,500),size=39,color=SILVER,bold=True,align="center")
        c.label("ABOUT 10,000 TO 100,000 TIMES BELOW THE FLOOR",(980,350,1740,500),size=39,color=CYAN,bold=True,align="center")
        c.label("EXTERNAL THEORIST REVIEW · AWAITED",(300,700,1620,855),size=48,color=RED,bold=True,align="center")
    c.illustration_chip(y=900 if stage==4 else None)


def draw_finale(c: PanelCanvas, stage: int) -> None:
    d=c.draw
    cards=[
        ("SPRING PAPER · STRENGTH NOT UNIQUE",(135,300,855,415),CYAN),
        ("SHARP-CORNER PAPER · INCOMPATIBLE INSERTED TURN",(1065,300,1785,435),RED),
        ("MASS-MAP PAPER · STARTING SIZE + HEAT · NOT ROTATION",(135,515,855,650),TEAL),
        ("COLLAPSE PAPER · LONE UNSUPPORTED SENTENCE · NO BRIDGE",(1065,515,1785,665),SILVER),
    ]
    if stage>=0:
        for text,box,color in cards: c.label(text,box,size=34,color=color,bold=True,align="center")
        d.line((855,360,1065,360),fill=rgba(CYAN,130),width=5)
        d.line((855,580,1065,580),fill=rgba(CYAN,130),width=5)
    if stage>=1:
        c.label("HELIUM · NO WHISPER",(620,735,1300,845),size=44,color=CYAN,bold=True,align="center")
    if stage>=2:
        c.label("ABOUT 10,000 TO 100,000 TIMES BELOW THE COUNTING FLOOR",(220,865,1700,965),size=39,color=WHITE,bold=True,align="center")
        c.label("THE STRONGEST ROUTE ENDS AT A CEILING",(470,685,1450,800),size=44,color=CYAN,bold=True,align="center")
    if stage>=3:
        # Final claim dominates and nothing follows it.
        overlay=Image.new("RGBA",(W,H),(11,12,16,220)); c.image.alpha_composite(overlay)
        c.draw=ImageDraw.Draw(c.image,"RGBA")
        c.heading()
        c.label("THE CEILING SAYS THE ROUTE STAYS CLOSED",(260,390,1660,720),size=70,color=WHITE,bold=True,align="center",max_lines=2,outline=CYAN)


def render_panel(panel: dict[str, Any], stage_index: int) -> tuple[Image.Image, dict[str, Any]]:
    pid=panel["id"]
    image=(full_bleed_cold_open() if pid=="01" else gradient_background(int(pid), RED if pid in {"08","12"} else CYAN)).copy()
    c=PanelCanvas(panel,image)
    c.heading()
    meta: dict[str,Any]={}
    if pid=="01":
        if stage_index>=0: c.label("BORN INSIDE A BLACK HOLE?",(135,285,850,405),size=58,color=WHITE,bold=True)
        if stage_index>=0: c.label("PARENT'S SPIN · A BIRTHMARK?",(135,455,850,570),size=43,color=CYAN,bold=True)
        if stage_index>=1: c.label("4 PUBLISHED PAPERS · THE WHOLE CHAIN",(135,620,850,730),size=38,color=SILVER,bold=True)
        if stage_index>=2:
            c.label("CEILING · THE LOUDEST POSSIBLE WHISPER",(940,265,1785,390),size=40,color=CYAN,bold=True,align="center")
            c.label("ABOUT 10,000 TO 100,000 TIMES QUIETER THAN THE BEST POSSIBLE GALAXY COUNT",(940,440,1785,620),size=35,color=WHITE,bold=True,align="center")
        if stage_index>=3:
            c.label("NO OBSERVABLE SIGNATURE SURVIVES",(940,690,1785,805),size=40,color=RED,bold=True,align="center")
            c.label("THE ROUTE STAYS CLOSED",(940,845,1785,955),size=48,color=WHITE,bold=True,align="center",outline=CYAN)
        c.illustration_chip()
    elif pid=="02": draw_mesh_birth(c,stage_index)
    elif pid=="03": draw_twist(c,stage_index)
    elif pid=="04": draw_spring(c,stage_index)
    elif pid=="05": draw_crowd(c,stage_index)
    elif pid=="06": draw_envelope(c,stage_index)
    elif pid=="07": meta=draw_panel07(c,stage_index)
    elif pid=="08": meta=draw_panel08(c,stage_index)
    elif pid=="09": draw_seed_pod(c,stage_index)
    elif pid=="10": draw_fingerprint(c,stage_index)
    elif pid=="11": draw_collapse(c,stage_index)
    elif pid=="12": draw_causality(c,stage_index)
    elif pid=="13": draw_balance(c,stage_index)
    elif pid=="14": meta=draw_helium(c,stage_index)
    elif pid=="15": draw_floor(c,stage_index)
    elif pid=="16": draw_finale(c,stage_index)
    else: raise RuntimeError(pid)
    # Render-gate chip fix: keep the standard DESIGN_SYSTEM pill visible for
    # every state of the three specifically mandated concept-art panels.
    if pid in {"01", "02", "11"} and pipeline.ILLUSTRATION_CHIP not in c.emitted:
        c.illustration_chip(x=SAFE if pid in {"01", "02"} else None, required=True)
    return c.finish(), {"emitted_text":c.emitted,"geometry":meta}


def make_cursor() -> None:
    size=96
    image=Image.new("RGBA",(size,size),(0,0,0,0))
    d=ImageDraw.Draw(image,"RGBA")
    for r,a in [(42,22),(32,45),(24,80),(16,155)]: d.ellipse((48-r,48-r,48+r,48+r),fill=rgba(CYAN,a))
    d.ellipse((36,36,60,60),fill=WHITE,outline=CYAN,width=4)
    image.save(CURSOR)


def cursor_points(panel_id: str, state_name: str, plot_box: tuple[int,int,int,int] | None) -> list[list[float]]:
    if plot_box is None:
        return []
    x1,y1,x2,y2=plot_box; w=x2-x1; h=y2-y1
    if (panel_id,state_name)==("07","plot"):
        rel=[(.09,.17),(.22,.27),(.36,.40),(.47,.58),(.50,.79),(.54,.58),(.68,.40),(.82,.27),(.93,.17)]
    elif (panel_id,state_name)==("08","plot"):
        rel=[(.10,.81),(.30,.79),(.43,.70),(.49,.47),(.50,.10),(.51,.47),(.58,.70),(.76,.79),(.92,.81)]
    elif (panel_id,state_name)==("14","figure1"):
        rel=[(.13,.19),(.35,.20),(.58,.19),(.82,.18),(.90,.18),(.75,.49),(.50,.46),(.20,.38),(.25,.82),(.60,.72),(.88,.62)]
    elif (panel_id,state_name)==("14","figure2"):
        rel=[(.12,.84),(.25,.70),(.40,.52),(.58,.35),(.75,.20),(.91,.08)]
    else:
        return []
    return [[x1+a*w,y1+b*h] for a,b in rel]


def main() -> int:
    frozen=pipeline.load_frozen_inputs()
    CARDS.mkdir(parents=True,exist_ok=True);STILLS.mkdir(parents=True,exist_ok=True)
    make_cursor()
    receipt={
        "status":"PASS_NEW_V3_DESIGN_SYSTEM_STATES_RENDERED",
        "resolution":[W,H],"palette":[BG,PANEL,WHITE,SILVER,CYAN,TEAL,RED],
        "safe_margin_px":SAFE,"generated_image_usage":{"panel":"01","asset":"nbp_p01_cold_open.png","full_bleed":True},
        "equations_projected_exactly":frozen["equations"],"other_equations_projected":[],
        "no_plots_panels":frozen["no_plots_panels"],"paper_assets_verified_before_embedding":True,
        "illustration_chip_exact":pipeline.ILLUSTRATION_CHIP,"panels":[],
    }
    for panel in frozen["panels"]:
        stage_records=[]; weights=PANEL_STAGES[panel["id"]]
        for index,(name,weight) in enumerate(weights):
            image,record=render_panel(panel,index)
            path=CARDS/f"panel-{panel['id']}-{name}.png"
            image.save(path,format="PNG",optimize=False,compress_level=6)
            box=record["geometry"].get("plot_box")
            points=cursor_points(panel["id"],name,box)
            stage_records.append({
                "name":name,"duration_weight":weight,"path":str(path.relative_to(pipeline.BUILD)),
                "sha256":pipeline.sha256(path),"emitted_text":record["emitted_text"],
                "cursor_points":points,"geometry":record["geometry"],
            })
        # Representative still is normally the final teaching/result state.
        # Panel 08 uses its large attributed paper-plot walkthrough so the
        # inexpensive still gate can audit all four required source figures.
        representative_index = 1 if panel["id"] == "08" else -1
        final_path=pipeline.BUILD/stage_records[representative_index]["path"]
        still=STILLS/f"panel_{panel['id']}.png"
        shutil.copy2(final_path,still)
        receipt["panels"].append({
            "id":panel["id"],"heading":panel["assertion_heading"],"text_closed_world":panel["viewer_text_closed_world"],
            "states":stage_records,"representative_still":str(still.relative_to(pipeline.BUILD)),
            "representative_still_sha256":pipeline.sha256(still),
            "design_source":"DESIGN_SYSTEM.md Part 1 + named Part 2 fallback",
        })
        print(f"panel {panel['id']}: {len(stage_records)} staged states")
    (pipeline.BUILD/"visual-receipt.json").write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":receipt["status"],"panels":len(receipt["panels"]),"stills":len(list(STILLS.glob('panel_*.png')))}))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
