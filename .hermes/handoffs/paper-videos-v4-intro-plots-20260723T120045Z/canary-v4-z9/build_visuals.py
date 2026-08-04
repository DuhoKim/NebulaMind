#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
LANE = ROOT.parent
SPEC_PATH = LANE / "V4_Z9_CANARY_SPEC.json"
SELECTION_PATH = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z/selection_v3.json")
IDENTITY_PATH = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z/identity/candidate_c_young_black_male.png")
LAYOUT_DIR = ROOT / "layouts"
RECEIPT_PATH = ROOT / "visuals_receipt.json"
SHEET_PATH = ROOT / "qa/layout_contact_sheet.png"
FONT_PATH = Path("/System/Library/Fonts/SFNSMono.ttf")
ITALIC_PATH = Path("/System/Library/Fonts/SFNSMonoItalic.ttf")
W, H = 2560, 1440
PRESENTER_BOX = (1980, 610, 430, 560)
BG = "#07101F"
PANEL = "#101E39"
OUTLINE = "#29466E"
BODY = "#EAF2FF"
MUTED = "#91A4C4"
CYAN = "#35D9F2"
MAGENTA = "#E879F9"
GREEN = "#57E389"
AMBER = "#F6C453"
RED = "#FF6B6B"
TONE = {"cyan": CYAN, "magenta": MAGENTA, "green": GREEN, "amber": AMBER, "red": RED}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def font(size: int, italic: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(ITALIC_PATH if italic else FONT_PATH), size=size)


def wrap(text: str, width: int) -> str:
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False))


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, fill: str = PANEL, outline: str = OUTLINE, radius: int = 28, width: int = 3) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def base_frame(scene: dict[str, Any]) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    draw.text((55, 40), "NebulaMind", font=font(38), fill=BODY)
    draw.text((350, 47), "PAPER EXPLAINER · INTRODUCTION + EVIDENCE", font=font(24), fill=CYAN)
    draw.text((2235, 47), f"{int(scene['slot']):02d} / 09", font=font(24), fill=MUTED)
    draw.line((55, 112, 2495, 112), fill=OUTLINE, width=2)
    rounded(draw, (1935, 145, 2495, 1285), outline=CYAN)
    draw.text((1972, 188), "PRESENTER C · MICHAEL", font=font(27), fill=BODY)
    draw.text((1972, 235), "Exact-audio lip-sync", font=font(20), fill=CYAN)
    draw.text((1972, 275), "Fictional presenter · science remains primary", font=font(15), fill=MUTED)
    draw.rounded_rectangle((1962, 570, 2448, 1215), radius=42, fill="#050B16", outline=OUTLINE, width=2)
    x, y, width, height = PRESENTER_BOX
    draw.rectangle((x, y, x + width, y + height), outline="#355984", width=2)
    draw.line((55, 1310, 2495, 1310), fill=OUTLINE, width=2)
    draw.text((55, 1342), "FLAGSHIP · CURRENT-SOURCE V4 LOCAL CANARY", font=font(20), fill=MUTED)
    draw.text((1828, 1342), "Manual captions · not published", font=font(19), fill=MUTED)
    return image, draw


def draw_header(draw: ImageDraw.ImageDraw, scene: dict[str, Any], *, warning: bool = False) -> None:
    color = AMBER if warning else CYAN
    draw.text((70, 154), str(scene.get("kicker", "")).upper(), font=font(23), fill=color)
    title = str(scene.get("title", ""))
    size = 50 if len(title) < 52 else 43
    draw.text((70, 194), wrap(title, 54), font=font(size), fill=BODY, spacing=9)


def card_scene(scene: dict[str, Any]) -> Image.Image:
    image, draw = base_frame(scene)
    warning = bool(scene.get("warning_style"))
    draw_header(draw, scene, warning=warning)
    cards = list(scene.get("cards", []))
    count = max(1, len(cards))
    left, right = 70, 1885
    gap = 28
    card_width = (right - left - gap * (count - 1)) // count
    top, bottom = 570, 1125
    for index, card in enumerate(cards):
        x0 = left + index * (card_width + gap)
        x1 = x0 + card_width
        tone = TONE.get(str(card.get("tone", "cyan")), CYAN)
        rounded(draw, (x0, top, x1, bottom), outline=tone, radius=30, width=4)
        value = str(card.get("value", ""))
        value_size = 39 if len(value) <= 18 else 31
        draw.text((x0 + 30, top + 72), wrap(value, 19), font=font(value_size), fill=tone, spacing=7)
        draw.line((x0 + 30, top + 235, x1 - 30, top + 235), fill=OUTLINE, width=2)
        draw.text((x0 + 30, top + 272), wrap(str(card.get("label", "")), 27), font=font(25), fill=BODY, spacing=8)
    return image


def hook_scene(scene: dict[str, Any]) -> Image.Image:
    image, draw = base_frame(scene)
    draw.text((75, 170), str(scene.get("kicker", "NEBULAMIND PAPER")), font=font(25), fill=CYAN)
    draw.text((75, 255), wrap(str(scene["title"]), 30), font=font(66), fill=BODY, spacing=15)
    rounded(draw, (75, 655, 1875, 1165), outline=CYAN, radius=36, width=4)
    draw.text((135, 725), "STARS", font=font(42), fill=BODY)
    draw.text((530, 725), "→", font=font(58), fill=CYAN)
    draw.text((700, 725), "OXYGEN", font=font(42), fill=MAGENTA)
    draw.text((1180, 725), "→", font=font(58), fill=CYAN)
    draw.text((1350, 725), "YOUNG GALAXIES", font=font(38), fill=GREEN)
    draw.text((135, 880), "Question first", font=font(28), fill=MUTED)
    draw.text((700, 880), "Evidence next", font=font(28), fill=MUTED)
    draw.text((1350, 880), "Limits stated", font=font(28), fill=MUTED)
    draw.text((135, 1040), "No manuscript cover page", font=font(24), fill=AMBER)
    return image


def plot_scene(scene: dict[str, Any], plot: Image.Image) -> tuple[Image.Image, float]:
    image, draw = base_frame(scene)
    draw_header(draw, scene)
    target = (75, 330, 1435, 1320)
    available = (target[2] - target[0], target[3] - target[1])
    contained = ImageOps.contain(plot.convert("RGB"), available, Image.Resampling.LANCZOS)
    scale = contained.width / plot.width
    px = target[0] + (available[0] - contained.width) // 2
    py = target[1] + (available[1] - contained.height) // 2
    draw.rounded_rectangle((px - 12, py - 12, px + contained.width + 12, py + contained.height + 12), radius=20, fill="white", outline=CYAN, width=3)
    image.paste(contained, (px, py))
    rounded(draw, (1465, 330, 1905, 1278), outline=MAGENTA, radius=28, width=3)
    draw.text((1500, 370), "HOW TO READ IT", font=font(22), fill=CYAN)
    draw.text((1500, 418), wrap(str(scene["axis_caption"]), 26), font=font(23), fill=BODY, spacing=8)
    draw.line((1500, 655, 1870, 655), fill=OUTLINE, width=2)
    draw.text((1500, 700), "ONE CLAIM", font=font(22), fill=MAGENTA)
    draw.text((1500, 748), wrap(str(scene["claim"]), 25), font=font(25), fill=BODY, spacing=8)
    draw.rounded_rectangle((1500, 1175, 1870, 1232), radius=16, fill="#152A4C")
    draw.text((1520, 1190), str(scene.get("overlay_emphasis", "evidence")), font=font(18), fill=GREEN)
    return image, scale


def outro_scene(scene: dict[str, Any], boundary: str) -> Image.Image:
    image, draw = base_frame(scene)
    draw.text((75, 185), "READ THE PAPER", font=font(25), fill=CYAN)
    draw.text((75, 285), "Full manuscript and current figures", font=font(53), fill=BODY)
    rounded(draw, (75, 470, 1880, 760), outline=CYAN, radius=32, width=4)
    draw.text((125, 545), wrap("nebulamind.net/studies/z9-10-unlensed-metallicity-deficit.pdf", 57), font=font(31), fill=CYAN, spacing=8)
    rounded(draw, (75, 835, 1880, 1215), outline=AMBER, radius=32, width=3)
    draw.text((125, 895), wrap(boundary, 76), font=font(27), fill=BODY, spacing=9)
    return image


def make_sheet(paths: list[Path]) -> None:
    SHEET_PATH.parent.mkdir(parents=True, exist_ok=True)
    thumb = (640, 360)
    row_height = 400
    sheet = Image.new("RGB", (1280, row_height * 5), BG)
    label_font = font(18)
    for index, path in enumerate(paths):
        image = Image.open(path).convert("RGB").resize(thumb, Image.Resampling.LANCZOS)
        x = (index % 2) * 640
        y = (index // 2) * row_height
        sheet.paste(image, (x, y + 40))
        draw = ImageDraw.Draw(sheet)
        draw.text((x + 12, y + 8), f"SLOT {index:02d}", font=label_font, fill=BODY)
    sheet.save(SHEET_PATH)


def main() -> None:
    for required in (SPEC_PATH, SELECTION_PATH, IDENTITY_PATH, FONT_PATH, ITALIC_PATH):
        if not required.is_file():
            raise FileNotFoundError(required)
    spec = json.loads(SPEC_PATH.read_text())
    selection = json.loads(SELECTION_PATH.read_text())
    if spec.get("marker") != "NEBULAMIND_V4_Z9_CANARY_SPEC_V1" or len(spec.get("scenes", [])) != 10:
        raise RuntimeError("unexpected signed spec")
    if selection["identity"]["sha256"] != sha256(IDENTITY_PATH):
        raise RuntimeError("identity drift")
    if tuple(spec["contract_preserved"]["presenter_box"]) != PRESENTER_BOX:
        raise RuntimeError("presenter box drift")
    figure = spec["figure_assets"][0]
    plot_path = LANE / figure["path"]
    if sha256(plot_path) != figure["sha256"]:
        raise RuntimeError("figure crop drift")
    plot = Image.open(plot_path).convert("RGB")
    LAYOUT_DIR.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    plot_scales: dict[str, float] = {}
    for scene in spec["scenes"]:
        slot = int(scene["slot"])
        if slot == 0:
            image = hook_scene(scene)
        elif scene.get("figure"):
            image, scale = plot_scene(scene, plot)
            plot_scales[str(slot)] = round(scale, 6)
        elif slot == 9:
            image = outro_scene(scene, spec["contract_preserved"]["boundary_text"])
        else:
            image = card_scene(scene)
        path = LAYOUT_DIR / f"slot_{slot:02d}.png"
        image.save(path)
        paths.append(path)
    make_sheet(paths)
    source_names = [str(SPEC_PATH), str(SELECTION_PATH), str(IDENTITY_PATH), str(plot_path)]
    if any(re.search(r"page.?1|cover", name, re.IGNORECASE) for name in source_names):
        raise RuntimeError("forbidden source entered layout lineage")
    receipt = {
        "marker": "NEBULAMIND_V4_Z9_VISUALS_COMPLETE",
        "completed_at_utc": now(),
        "spec": str(SPEC_PATH),
        "spec_sha256": sha256(SPEC_PATH),
        "identity": str(IDENTITY_PATH),
        "identity_sha256": sha256(IDENTITY_PATH),
        "figure": str(plot_path),
        "figure_sha256": sha256(plot_path),
        "figure_source_pixels": list(plot.size),
        "figure_pdf_render_pixels_per_point": 6,
        "plot_display_scales": plot_scales,
        "presenter_box": list(PRESENTER_BOX),
        "layout_count": len(paths),
        "layouts": [{"slot": index, "path": str(path), "sha256": sha256(path), "pixels": list(Image.open(path).size)} for index, path in enumerate(paths)],
        "layout_contact_sheet": str(SHEET_PATH),
        "layout_contact_sheet_sha256": sha256(SHEET_PATH),
        "source_lineage": source_names,
        "forbidden_source_scan": "PASS",
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "layouts": len(paths), "plot_scales": plot_scales, "sheet": str(SHEET_PATH)}, indent=2))


if __name__ == "__main__":
    main()
