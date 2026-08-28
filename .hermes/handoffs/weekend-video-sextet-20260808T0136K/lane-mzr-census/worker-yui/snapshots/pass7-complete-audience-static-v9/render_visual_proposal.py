#!/usr/bin/env python3
"""Render a static, graphics-first MZR census funnel proposal.

Worker-lane artifact only. Reads frozen evidence and writes one PNG beside this
script. It does not edit shared tools, invoke TTS, or create a video candidate.
"""
from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "frozen_sources/pass7"
OUT = HERE / "visual_proposal_v9.png"
CITATION_LEDGER = HERE / "citation_ledger.json"
AUDIENCE_FOOTER = json.loads(CITATION_LEDGER.read_text())["audience_footer"]

W, H = 1920, 1080
BG = "#08101f"
PANEL = "#111b2e"
PANEL_2 = "#17243a"
FG = "#f2f6ff"
DIM = "#aebbd2"
BLUE = "#79b2ff"
GREEN = "#71d6a5"
AMBER = "#f5bd73"
RED = "#ff8b86"
BORDER = "#314363"


def font(size: int, bold: bool = False):
    choices = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/SFNS.ttf",
    ]
    for candidate in choices:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default()


def centered(draw, box, text, fnt, fill):
    x1, y1, x2, y2 = box
    bounds = draw.textbbox((0, 0), text, font=fnt)
    tw, th = bounds[2] - bounds[0], bounds[3] - bounds[1]
    draw.text(((x1 + x2 - tw) / 2, (y1 + y2 - th) / 2 - bounds[1]), text, font=fnt, fill=fill)


def rounded(draw, box, fill=PANEL, outline=BORDER, radius=22, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw, x1, y, x2, color=DIM):
    draw.line((x1, y, x2 - 14, y), fill=color, width=4)
    draw.polygon([(x2 - 14, y - 9), (x2, y), (x2 - 14, y + 9)], fill=color)


manifest = json.loads((SOURCE / "T1_MZR_MANIFEST.json").read_text())
gas = json.loads((SOURCE / "T1E_GASPHASE_COUNT.json").read_text())
findings = (SOURCE / "T1_FINDINGS.md").read_text()

assert manifest["status"] == "DONE"
assert manifest["n_candidates_pre_filter"] == 178
assert manifest["n_candidates"] == 157
assert len(manifest["dropped_candidates"]) == 21
z_drops = sum("redshift" in row["axes_emptied_by_modifier_filter"] for row in manifest["dropped_candidates"])
ab_drops = sum("abundance" in row["axes_emptied_by_modifier_filter"] for row in manifest["dropped_candidates"])
assert (z_drops, ab_drops) == (19, 2)
assert sum(manifest["recall_members_returned"].values()) == 7
assert sum(manifest["controls_appearing"].values()) == 0
assert gas["count"] == 62 and gas["of_candidates"] == 157
for token in ("5,393", "5,568", "+175", "6,118", "6,206", "+88", "6,667", "6,687", "+20"):
    assert token in findings, token

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Header
d.text((90, 50), "Archive reach is not eligibility", font=font(56, True), fill=FG)
rounded(d, (1260, 48, 1830, 112), fill="#18243a", outline=AMBER, radius=20, width=2)
centered(d, (1260, 48, 1830, 112), "METADATA CENSUS — NOT AN MZR MEASUREMENT", font(18, True), AMBER)
d.text((90, 118), "Single-table metadata intersection · cross-table joins and crossmatches not assessed", font=font(22, True), fill=DIM)

# Retrieval channels: exact counts, intentionally equal-width cards.
axis_specs = [
    ("ABUNDANCE SEARCH", "5,393", "5,568", "+175"),
    ("MASS SEARCH", "6,118", "6,206", "+88"),
    ("REDSHIFT SEARCH", "6,667", "6,687", "+20"),
]
card_y1, card_y2 = 155, 355
card_w, gap, start_x = 500, 45, 165
for i, (label, ucd, total, gain) in enumerate(axis_specs):
    x1 = start_x + i * (card_w + gap)
    x2 = x1 + card_w
    rounded(d, (x1, card_y1, x2, card_y2), fill=PANEL)
    d.text((x1 + 28, card_y1 + 22), label, font=font(24, True), fill=BLUE)
    d.text((x1 + 28, card_y1 + 72), f"UCD  {ucd}", font=font(40, True), fill=FG)
    d.text((x1 + 28, card_y1 + 126), f"UCD + name  {total}", font=font(31, True), fill=FG)
    rounded(d, (x2 - 120, card_y1 + 20, x2 - 24, card_y1 + 66), fill="#173451", outline=BLUE, radius=16)
    centered(d, (x2 - 120, card_y1 + 20, x2 - 24, card_y1 + 66), gain, font(22, True), BLUE)
d.text((165, 370), "Two retrieval channels · zero channel failures · counts, not area encoded", font=font(25), fill=DIM)

# Main funnel.
fy1, fy2, fmid = 430, 650, 540
boxes = [
    (90, 430, 390, 650, BLUE, "178", "three-axis\nintersection"),
    (470, 430, 820, 650, RED, "−21", "axes emptied\n19 redshift-search\n2 abundance-search"),
    (900, 430, 1210, 650, BLUE, "157", "recorded\ncandidates"),
    (1430, 430, 1830, 650, GREEN, "T2", "contract frozen\napplication not completed"),
]
for x1, y1, x2, y2, color, number, label in boxes:
    rounded(d, (x1, y1, x2, y2), fill=PANEL_2, outline=color, radius=24, width=3)
    centered(d, (x1, y1 + 22, x2, y1 + 112), number, font(58, True), color)
    for line_no, line in enumerate(label.split("\n")):
        top = y1 + 116 + line_no * 30
        centered(d, (x1 + 12, top, x2 - 12, top + 32), line, font(23 if line_no == 0 else 21, line_no == 0), FG if line_no == 0 else DIM)
for left, right in zip(boxes, boxes[1:]):
    arrow(d, left[2] + 12, fmid, right[0] - 12, DIM)

# Make the drop reasons, 62 side-check topology, and T2 boundary unavoidable.
d.text((480, 660), "19 redshift-search: e_Z · e_[Z/H]", font=font(16, True), fill=RED)
d.text((480, 686), "2 abundance-search: e_Ha/Hb · e_logOI/Ha · l_logOI/Ha", font=font(15), fill=RED)
d.line((1055, 650, 1055, 675), fill=AMBER, width=3)
d.polygon([(1046, 666), (1055, 678), (1064, 666)], fill=AMBER)
rounded(d, (900, 680, 1830, 742), fill="#32281e", outline=AMBER, radius=16, width=2)
d.text((930, 691), "62 of 157 tables · frozen term-regex match in recorded descriptions", font=font(19, True), fill=AMBER)
d.text((930, 718), "SIDE CHECK ONLY · T2 STILL APPLIES TO ALL 157", font=font(16, True), fill=FG)
centered(d, (1430, 618, 1830, 646), "NO ELIGIBLE-TABLE COUNT", font(16, True), GREEN)

# Retrieval check and limitation.
rounded(d, (90, 765, 435, 930), fill=PANEL, outline=GREEN, radius=24, width=3)
d.text((120, 793), "RECALL", font=font(25, True), fill=GREEN)
d.text((120, 830), "7 / 7", font=font(62, True), fill=FG)
d.text((120, 895), "pinned members returned", font=font(22), fill=DIM)

rounded(d, (475, 765, 845, 930), fill=PANEL, outline=GREEN, radius=24, width=3)
d.text((505, 793), "CONTROLS APPEARING", font=font(25, True), fill=GREEN)
d.text((505, 830), "0 / 3", font=font(62, True), fill=FG)
d.text((505, 895), "all three stayed out", font=font(22), fill=DIM)

rounded(d, (885, 765, 1830, 950), fill="#30241d", outline=AMBER, radius=24, width=3)
d.text((920, 790), "RETRIEVAL CHECK PASSED · PRECISION NOT CERTIFIED", font=font(29, True), fill=AMBER)
d.text((920, 837), "RECORDED EXAMPLES · NOT T2 RULINGS · FROZEN CONTROLS DID NOT COVER:", font=font(18, True), fill=FG)
example_rows = [
    ("SYMBOL / MEANING COLLISION", ["Galactic height", "stellar-grid metal fraction (model Z)"]),
    ("TARGET-DOMAIN MISMATCH", ["stellar gravitational redshift", "gravitational-redshift velocity"]),
]
for row_no, (category, examples) in enumerate(example_rows):
    x = 1170
    y1 = 874 + row_no * 36
    d.text((920, y1 + 7), category, font=font(14, True), fill=AMBER)
    for example in examples:
        w = int(d.textlength(example, font=font(17))) + 32
        rounded(d, (x, y1, x + w, y1 + 31), fill="#3a2c23", outline="#8f6b45", radius=12, width=1)
        centered(d, (x, y1, x + w, y1 + 31), example, font(17), FG)
        x += w + 14

# Audience citation only: no internal paths.
d.line((90, 985, 1830, 985), fill=BORDER, width=2)
d.text((90, 1005), AUDIENCE_FOOTER, font=font(19), fill=DIM)
d.text((1515, 1038), "VISUAL PROPOSAL · NOT A CANDIDATE", font=font(18, True), fill="#687996")

img.save(OUT)
print(OUT)
