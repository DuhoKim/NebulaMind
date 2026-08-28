#!/usr/bin/env python3
"""Render static spin-parity method-only visual proposal frames.

This is a worker-Yui review artifact, not an MP4 candidate. It writes only PNG
proposal frames and a contact sheet under the official worker-yui directory.
It does not edit shared tools/storyboards, invoke TTS, or encode/mux media.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
BG = "#08101d"
PANEL = "#111c2f"
PANEL_2 = "#16243a"
FG = "#f2f6ff"
DIM = "#a8b5cc"
BLUE = "#72adff"
GREEN = "#75c79a"
ORANGE = "#f0ad67"
RED = "#ee7d79"
LINE = "#2c3c58"
ROOT = Path(__file__).resolve().parent
STORYBOARD = ROOT / "STORYBOARD_PROPOSAL.json"
OUT = ROOT / "proposal_frames" / "v8"
T1 = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/spin-parity-census-20260805T1922K/T1_FUNNEL.json")
T1C = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/spin-parity-census-20260805T1922K/T1C_COLUMN_INTEGRITY.json")
FONT_REG = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
FONT_BOLD = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if bold else FONT_REG
    return ImageFont.truetype(str(path), size)


def wrapped(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        test = f"{cur} {word}".strip()
        if not cur or draw.textlength(test, font=fnt) <= width:
            cur = test
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont,
               fill: str, width: int, gap: int = 10) -> int:
    x, y = xy
    for line in wrapped(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return int(y)


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str = PANEL,
          outline: str = LINE, radius: int = 24, width: int = 2) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def badge(draw: ImageDraw.ImageDraw, xy: tuple[int, int], label: str, fill: str, fg: str = BG,
          pad_x: int = 22, pad_y: int = 11) -> tuple[int, int, int, int]:
    fnt = font(24, True)
    x, y = xy
    box = draw.textbbox((0, 0), label, font=fnt)
    w = int(box[2] - box[0] + 2 * pad_x)
    h = int(box[3] - box[1] + 2 * pad_y)
    draw.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=fill)
    draw.text((x + pad_x, y + pad_y - 2), label, font=fnt, fill=fg)
    return x, y, x + w, y + h


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = BLUE,
          width: int = 6) -> None:
    draw.line((start, end), fill=color, width=width)
    ang = math.atan2(end[1] - start[1], end[0] - start[0])
    length = 18
    for delta in (2.55, -2.55):
        p = (int(end[0] + length * math.cos(ang + delta)), int(end[1] + length * math.sin(ang + delta)))
        draw.line((end, p), fill=color, width=width)


def base_frame(scene: dict, idx: int, total: int) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 14, H), fill=BLUE)
    draw.text((70, 50), "GALAXY SPIN  ·  METHOD-ONLY VISUAL PROPOSAL", font=font(24, True), fill=BLUE)
    badge(draw, (1605, 40), "RESULT HELD", ORANGE)
    draw.line((70, 105, 1850, 105), fill=LINE, width=2)
    draw.text((70, 990), scene["display_citation"], font=font(23), fill=DIM)
    draw.text((1630, 990), f"STATIC PROPOSAL  ·  {idx}/{total}", font=font(22, True), fill=DIM)
    return img, draw


def title(draw: ImageDraw.ImageDraw, text: str, sub: str | None = None) -> int:
    y = text_block(draw, (90, 125), text, font(58, True), FG, 1550, 8)
    if sub:
        y = text_block(draw, (92, y + 8), sub, font(30), DIM, 1540, 7)
    return y


def render_s1(scene: dict, idx: int, total: int) -> Image.Image:
    img, draw = base_frame(scene, idx, total)
    y = title(draw, scene["on_screen_copy"]["headline"], scene["on_screen_copy"]["subhead"])
    labels = [("SAMPLE", "readout"), ("STATISTIC", "one A each"),
              ("CONVENTION", "label meaning"), ("ALIGNMENT", "bounded probe"),
              ("CONTROLS", "paired design")]
    x0, top, node_w, gap = 85, y + 85, 300, 55
    for i, (a, b) in enumerate(labels):
        x = x0 + i * (node_w + gap)
        panel(draw, (x, top, x + node_w, top + 195), PANEL_2, BLUE)
        draw.text((x + 25, top + 35), f"0{i+1}", font=font(25, True), fill=BLUE)
        draw.text((x + 25, top + 82), a, font=font(29, True), fill=FG)
        draw.text((x + 25, top + 135), b, font=font(23), fill=DIM)
        if i < len(labels) - 1:
            arrow(draw, (x + node_w + 8, top + 98), (x + node_w + gap - 8, top + 98), BLUE, 5)
    lock_x = 535
    panel(draw, (lock_x, top + 250, lock_x + 850, top + 465), "#171d2b", ORANGE, 28, 3)
    draw.text((lock_x + 55, top + 282), "RESULT LOCKED", font=font(40, True), fill=ORANGE)
    draw.text((lock_x + 55, top + 345), "Unlock requires BOTH:", font=font(25, True), fill=FG)
    draw.text((lock_x + 55, top + 385), "archive frame convention  +  independent post-run review", font=font(23), fill=DIM)
    return img


def render_s2(scene: dict, idx: int, total: int) -> Image.Image:
    img, draw = base_frame(scene, idx, total)
    title(draw, scene["on_screen_copy"]["headline"], scene["on_screen_copy"]["subhead"])
    panel(draw, (90, 285, 430, 685), PANEL_2, BLUE)
    draw.text((125, 330), "FROZEN SOURCE", font=font(28, True), fill=BLUE)
    draw.text((125, 420), "667,944", font=font(74, True), fill=FG)
    draw.text((125, 515), "Galaxy Zoo rows", font=font(29), fill=DIM)
    draw.text((125, 595), "one source", font=font(25, True), fill=GREEN)
    branches = [
        ("RELEASE SPIRAL FLAG", "190,225 pass", "161,172 classified", "29,053 ties", BLUE),
        ("CONFIDENCE ≥ 0.80", "30,412 classified", "0 ties", "INSIDE 0.60", GREEN),
        ("CONFIDENCE ≥ 0.60", "51,157 classified", "0 ties", "INCLUDES 0.80", ORANGE),
    ]
    y0 = 265
    for i, (head, a, b, c, color) in enumerate(branches):
        y = y0 + i * 220
        arrow(draw, (455, 490), (585, y + 95), color)
        panel(draw, (600, y, 1770, y + 180), PANEL, color, 22, 3)
        draw.text((635, y + 25), head, font=font(30, True), fill=color)
        draw.text((635, y + 82), a, font=font(34, True), fill=FG)
        draw.text((1025, y + 82), b, font=font(30), fill=FG)
        draw.text((1430, y + 82), c, font=font(28, True), fill=color)
        if i == 0:
            draw.text((1430, y + 125), "flag overlap not quantified", font=font(21), fill=DIM)
    badge(draw, (95, 915), "ALTERNATIVE READOUTS · COUNTS OVERLAP · DO NOT SUM", ORANGE)
    return img


def render_s3(scene: dict, idx: int, total: int) -> Image.Image:
    img, draw = base_frame(scene, idx, total)
    title(draw, scene["on_screen_copy"]["headline"], "Each readout gets one A; ties stay visible but outside the denominator")
    panel(draw, (250, 300, 1670, 520), PANEL_2, BLUE, 30, 3)
    eq = scene["on_screen_copy"]["equation"]
    box = draw.textbbox((0, 0), eq, font=font(58, True))
    draw.text(((W - (box[2] - box[0])) // 2, 365), eq, font=font(58, True), fill=FG)
    items = [("N_CW", "clockwise classified", BLUE), ("N_ACW", "anticlockwise classified", GREEN),
             ("N_tie", "reported separately", ORANGE)]
    for i, (head, body, color) in enumerate(items):
        x = 205 + i * 520
        panel(draw, (x, 585, x + 430, 750), PANEL, color, 22, 3)
        draw.text((x + 35, 615), head, font=font(38, True), fill=color)
        draw.text((x + 35, 680), body, font=font(28), fill=FG)
    draw.line((1270, 765, 1590, 765), fill=ORANGE, width=5)
    draw.text((1265, 775), "outside denominator", font=font(23, True), fill=ORANGE)
    panel(draw, (250, 805, 1670, 865), PANEL_2, BLUE, 20, 2)
    sign_key = scene["on_screen_copy"]["sign_key"]
    box = draw.textbbox((0, 0), sign_key, font=font(28, True))
    draw.text(((W - (box[2] - box[0])) // 2, 820), sign_key, font=font(28, True), fill=FG)
    swap_bridge = scene["on_screen_copy"]["swap_bridge"]
    box = draw.textbbox((0, 0), swap_bridge, font=font(24, True))
    draw.text(((W - (box[2] - box[0])) // 2, 875), swap_bridge, font=font(24, True), fill=BLUE)
    text_block(draw, (300, 920), scene["on_screen_copy"]["boundary"], font(22, True), ORANGE, 1320, 4)
    return img


def spiral(draw: ImageDraw.ImageDraw, center: tuple[int, int], mirror: bool, color: str) -> None:
    cx, cy = center
    pts = []
    for i in range(180):
        t = i / 18
        r = 7 + 8.5 * t
        x = r * math.cos(t)
        y = r * math.sin(t)
        if mirror:
            x = -x
        pts.append((cx + int(x), cy + int(y)))
    draw.line(pts, fill=color, width=7)
    draw.ellipse((cx - 12, cy - 12, cx + 12, cy + 12), fill=color)


def render_s4(scene: dict, idx: int, total: int) -> Image.Image:
    img, draw = base_frame(scene, idx, total)
    title(draw, scene["on_screen_copy"]["headline"], scene["on_screen_copy"]["schematic_label"])
    panel(draw, (90, 300, 475, 650), PANEL_2, BLUE)
    spiral(draw, (282, 455), False, BLUE)
    draw.text((165, 590), "ORIGINAL DISPLAY", font=font(28, True), fill=FG)
    arrow(draw, (500, 475), (690, 475), ORANGE)
    draw.text((530, 425), "MIRROR", font=font(24, True), fill=ORANGE)
    panel(draw, (710, 300, 1095, 650), PANEL_2, ORANGE)
    spiral(draw, (902, 455), True, ORANGE)
    draw.text((790, 590), "MIRRORED DISPLAY", font=font(28, True), fill=FG)
    branch_y = (300, 505)
    for j, (label, sub, color) in enumerate([
        ("AS DISPLAYED", "label follows mirrored view", BLUE),
        ("DE-MIRRORED", "label mapped back first", GREEN),
    ]):
        y = branch_y[j]
        arrow(draw, (1120, 475), (1225, y + 70), color)
        panel(draw, (1240, y, 1780, y + 155), PANEL, color, 20, 3)
        draw.text((1270, y + 28), label, font=font(30, True), fill=color)
        draw.text((1270, y + 82), sub, font=font(25), fill=FG)
    badge(draw, (685, 690), "POSSIBILITIES SHOWN WITHOUT PROBABILITY", BLUE)
    panel(draw, (500, 750, 1420, 935), "#2b211b", ORANGE, 28, 4)
    draw.text((660, 775), "FRAME UNSTATED", font=font(52, True), fill=ORANGE)
    text_block(draw, (630, 852), scene["on_screen_copy"]["boundary_explanation"], font(24), FG, 680, 5)
    return img


def render_s5(scene: dict, idx: int, total: int) -> Image.Image:
    img, draw = base_frame(scene, idx, total)
    title(draw, scene["on_screen_copy"]["headline"], scene["on_screen_copy"]["subhead"])
    panel(draw, (90, 300, 530, 790), PANEL_2, BLUE)
    panel(draw, (920, 300, 1360, 790), PANEL_2, GREEN)
    draw.text((140, 340), "GALAXY ZOO CSV", font=font(27, True), fill=BLUE)
    draw.text((965, 340), "VIZIER GALAXIES", font=font(27, True), fill=GREEN)
    draw.text((140, 385), "P_CW / P_ACW · source CW / ACW values", font=font(18), fill=DIM)
    draw.text((965, 385), "pcS / paS · comparison CW / ACW values", font=font(18), fill=DIM)
    left = ["P_CW", "P_ACW", "P_CW", "P_ACW", "P_CW", "P_ACW"]
    right = ["pcS", "paS", "pcS", "paS", "pcS", "paS"]
    for i, (a, b) in enumerate(zip(left, right)):
        y = 440 + i * 48
        draw.text((155, y), a, font=font(25, True), fill=FG)
        draw.text((1160, y), b, font=font(25, True), fill=FG)
        arrow(draw, (320, y + 15), (1120, y + 15), GREEN, 3)
    metrics = [("36", "checked", BLUE), ("36", "same-column", GREEN), ("0", "crossed", RED), ("0", "ambiguous", ORANGE)]
    for i, (value, label, color) in enumerate(metrics):
        x = 1425 + (i % 2) * 220
        y = 315 + (i // 2) * 220
        panel(draw, (x, y, x + 190, y + 180), PANEL, color, 20, 3)
        draw.text((x + 32, y + 28), value, font=font(60, True), fill=color)
        text_block(draw, (x + 25, y + 108), label, font(21, True), FG, 145, 3)
    badge(draw, (565, 810), "SCHEMATIC · 6 EXAMPLE ROWS OF 36", BLUE)
    badge(draw, (150, 895), "THIS PROBE ONLY · NORMAL TABLE COLUMNS · MIRRORED STORAGE FRAME UNRESOLVED", ORANGE)
    return img


def render_s6(scene: dict, idx: int, total: int) -> Image.Image:
    img, draw = base_frame(scene, idx, total)
    title(draw, scene["on_screen_copy"]["headline"], "Same object, four conditions · comparison questions only · outcomes withheld")
    cards = [
        ("NORMAL", "reference labels", BLUE),
        ("MONOCHROME", "do labels stay the same?", GREEN),
        ("MIRROR 1", "do displayed labels switch? · vertical", ORANGE),
        ("MIRROR 2", "do displayed labels switch? · diagonal", ORANGE),
    ]
    for i, (head, body, color) in enumerate(cards):
        x = 110 + (i % 2) * 600
        y = 300 + (i // 2) * 220
        panel(draw, (x, y, x + 520, y + 175), PANEL_2, color, 22, 3)
        draw.text((x + 35, y + 35), head, font=font(34, True), fill=color)
        text_block(draw, (x + 35, y + 94), body, font(24), FG, 445, 4)
    panel(draw, (1335, 300, 1780, 735), PANEL, BLUE, 24, 3)
    draw.text((1380, 340), "CLASSIFICATION CONFIDENCE", font=font(21, True), fill=BLUE)
    for y, label, color in [(440, "0.80  ·  available", GREEN), (535, "0.60  ·  available", GREEN)]:
        draw.line((1390, y, 1715, y), fill=color, width=10)
        draw.text((1390, y + 24), label, font=font(27, True), fill=FG)
    draw.line((1390, 660, 1715, 660), fill=RED, width=8)
    for x in range(1390, 1716, 24):
        draw.line((x, 650, x + 12, 670), fill=BG, width=5)
    draw.text((1390, 685), "SPIRAL flag · unavailable", font=font(25, True), fill=RED)
    panel(draw, (130, 815, 1800, 940), PANEL, ORANGE, 24, 3)
    badge(draw, (170, 842), "PAIRED BY OBJECT ID", BLUE)
    draw.text((585, 850), "Compare labels within each object", font=font(27, True), fill=FG)
    badge(draw, (1350, 842), "OUTCOMES WITHHELD", ORANGE)
    return img


def render_s7(scene: dict, idx: int, total: int) -> Image.Image:
    img, draw = base_frame(scene, idx, total)
    draw.text((90, 125), scene["on_screen_copy"]["headline"], font=font(68, True), fill=ORANGE)
    cols = [
        ("KNOWN", scene["on_screen_copy"]["known"], GREEN),
        ("UNRESOLVED", scene["on_screen_copy"]["unresolved"], ORANGE),
        ("NOT CLAIMED", scene["on_screen_copy"]["not_claimed"], RED),
    ]
    for i, (head, items, color) in enumerate(cols):
        x = 90 + i * 590
        panel(draw, (x, 260, x + 530, 760), PANEL_2, color, 24, 3)
        draw.text((x + 35, 300), head, font=font(34, True), fill=color)
        y = 385
        for item in items:
            draw.ellipse((x + 38, y + 10, x + 54, y + 26), fill=color)
            y = text_block(draw, (x + 78, y), item, font(27), FG, 410, 8) + 28
    panel(draw, (220, 825, 1700, 945), "#2b211b", ORANGE, 26, 4)
    draw.text((270, 852), "SEPARATE AUTHORIZATION", font=font(26, True), fill=ORANGE)
    text_block(draw, (650, 850), scene["on_screen_copy"]["next_gate"], font(25, True), FG, 980, 6)
    return img


RENDERERS = [render_s1, render_s2, render_s3, render_s4, render_s5, render_s6, render_s7]


def validate_sources() -> None:
    sb = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    t1 = json.loads(T1.read_text(encoding="utf-8"))
    t1c = json.loads(T1C.read_text(encoding="utf-8"))
    assert sb["status"] == "PROPOSAL_ONLY_NOT_A_CANDIDATE"
    assert sb["video_reportable_now"] is False
    assert t1["files"]["zooSpec"]["rows_parsed"] == 667944
    f = t1["funnel"]["zooSpec"]
    assert f["SPIRAL_FLAG"] == {"N_CW": 75873, "N_ACW": 85299, "N_tie": 29053, "N_classified": 161172, "N_pass": 190225}
    assert f["0.80"]["N_classified"] == 30412 and f["0.80"]["N_tie"] == 0
    assert f["0.60"]["N_classified"] == 51157 and f["0.60"]["N_tie"] == 0
    assert t1c["counts"] == {"aligned": 36, "crossed": 0, "ambiguous": 0, "unmatched": 0}


def make_contact_sheet(paths: list[Path]) -> None:
    thumbs = []
    for p in paths:
        im = Image.open(p).convert("RGB").resize((640, 360), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (656, 396), BG)
        canvas.paste(im, (8, 8))
        d = ImageDraw.Draw(canvas)
        scene_number = int(p.stem.split("_")[1])
        d.text((12, 372), f"Scene {scene_number}", font=font(18, True), fill=DIM)
        thumbs.append(canvas)
    cols = 2
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 656, rows * 396), BG)
    for i, im in enumerate(thumbs):
        sheet.paste(im, ((i % cols) * 656, (i // cols) * 396))
    sheet.save(OUT / "contact_sheet.png")


def main() -> int:
    validate_sources()
    sb = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    scenes = sb["scenes"]
    assert len(scenes) == len(RENDERERS)
    OUT.mkdir(parents=True, exist_ok=True)
    paths = []
    for idx, (scene, renderer) in enumerate(zip(scenes, RENDERERS), 1):
        img = renderer(scene, idx, len(scenes))
        path = OUT / f"scene_{idx:02d}_{scene['id'].lower()}.png"
        img.save(path)
        paths.append(path)
    make_contact_sheet(paths)
    (OUT / "render_receipt.json").write_text(json.dumps({
        "status": "STATIC_PROPOSAL_ONLY_NOT_A_CANDIDATE",
        "proposal_iteration": OUT.name,
        "storyboard": str(STORYBOARD),
        "storyboard_sha256": hashlib.sha256(STORYBOARD.read_bytes()).hexdigest(),
        "lane_renderer": str(Path(__file__).resolve()),
        "lane_renderer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scenes": len(paths),
        "resolution": [W, H],
        "outputs": [str(p) for p in paths],
        "contact_sheet": str(OUT / "contact_sheet.png"),
        "shared_tools_modified": False,
        "tts_invoked": False,
        "mp4_encoded": False,
    }, indent=2), encoding="utf-8")
    print(f"rendered {len(paths)} static proposal frames to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
