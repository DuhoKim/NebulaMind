#!/usr/bin/env python3
"""Render static, review-only FESC visual states from frozen model output.

This is not the shared renderer and does not produce an MP4 or candidate bundle.
It writes only worker-Yui proposal PNGs and a provenance manifest.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
SOURCE = ROOT / ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/TREND_RESULTS.json"
EXPECTED_SOURCE_SHA256 = "8df9f25b5f8acaf22825d6ece958867562c7e37a73fe69aa8e8175fe0b7aa242"
OUT = ROOT / ".hermes/handoffs/weekend-video-sextet-20260808T0136K/lane-fesc-zsweep/worker-yui/visual_proposal_v4"
STATES = OUT / "states"

BG = "#0b0f1a"
PANEL = "#111827"
FG = "#eef3fb"
DIM = "#a8b5ca"
GRID = "#2a364c"
REQ = "#ff6f61"
INF = "#68a7ff"
GREEN = "#7bd88f"
GOLD = "#f2c46d"
NO_TAIL = "#f1f5f9"
WARN = "#e3a46b"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def rounded_box(fig, x, y, w, h, color, alpha=1.0, edge=None, radius=0.02):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.008,rounding_size={radius}",
        transform=fig.transFigure,
        facecolor=color,
        edgecolor=edge or color,
        linewidth=1.5,
        alpha=alpha,
        clip_on=False,
    )
    fig.patches.append(patch)
    return patch


def add_text(fig, x, y, text, size, color=FG, weight="normal", ha="left", va="top", linespacing=1.18):
    return fig.text(
        x, y, text,
        color=color,
        fontsize=size,
        fontweight=weight,
        ha=ha,
        va=va,
        linespacing=linespacing,
        family="DejaVu Sans",
    )


def style_axis(ax):
    ax.set_facecolor(PANEL)
    for spine in ax.spines.values():
        spine.set_color("#46546c")
        spine.set_linewidth(1.2)
    ax.tick_params(colors=DIM, labelsize=14, length=5, width=1)
    ax.grid(color=GRID, alpha=0.55, linewidth=0.8)
    ax.set_axisbelow(True)


def setup_figure(title: str, step: str):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100, facecolor=BG)
    top = fig.add_axes((0.07, 0.565, 0.59, 0.31))
    bottom = fig.add_axes((0.07, 0.16, 0.59, 0.31), sharex=top)
    rail = fig.add_axes((0.70, 0.12, 0.27, 0.76))
    rail.set_facecolor(PANEL)
    rail.set_xticks([])
    rail.set_yticks([])
    for spine in rail.spines.values():
        spine.set_color("#334158")
        spine.set_linewidth(1.4)

    rounded_box(fig, 0.07, 0.915, 0.165, 0.037, "#23324a", edge="#446084", radius=0.012)
    add_text(fig, 0.083, 0.938, "MODEL OUTPUT · NO NEW MEASUREMENT", 13, color="#c6d7f3", weight="bold", va="center")
    add_text(fig, 0.07, 0.905, title, 27, weight="bold")
    add_text(fig, 0.97, 0.94, step, 15, color=DIM, weight="bold", ha="right", va="center")
    add_text(
        fig, 0.07, 0.055,
        "NebulaMind z-sweep model output (2026-08-04) · 40,000 draws per redshift · conditional on frozen low-z proxy anchors",
        12, color="#71819a", va="center",
    )
    return fig, top, bottom, rail


def draw_base(top, bottom, data, show_top=True, show_bottom=True, top_alpha=1.0, bottom_alpha=1.0):
    z = data["z"]
    if show_top:
        top.fill_between(z, data["req_lo"], data["req_hi"], color=REQ, alpha=0.17 * top_alpha, linewidth=0)
        top.fill_between(z, data["inf_lo"], data["inf_hi"], color=INF, alpha=0.15 * top_alpha, linewidth=0)
        top.plot(z, data["req_med"], "o-", color=REQ, lw=3.0, ms=7, alpha=top_alpha, label="required by budget")
        top.plot(z, data["inf_med"], "s--", color=INF, lw=2.8, ms=6, alpha=top_alpha, label="proxy-inferred; fixed in z")
    style_axis(top)
    top.set_xlim(6, 10)
    top.set_ylim(0, 1.45)
    top.set_ylabel("escape fraction  $f_{esc}$", color=FG, fontsize=17, labelpad=12)
    top.tick_params(labelbottom=False)
    if show_top:
        legend = top.legend(loc="upper left", frameon=True, fontsize=14)
        legend.get_frame().set_facecolor("#0d1422")
        legend.get_frame().set_edgecolor("#40506a")
        for text in legend.get_texts():
            text.set_color(FG)

    if show_bottom:
        bottom.fill_between(z, data["delta_lo"], data["delta_hi"], color=REQ, alpha=0.17 * bottom_alpha, linewidth=0)
        bottom.plot(z, data["delta_med"], "o-", color=REQ, lw=3.0, ms=7, alpha=bottom_alpha, label="median Δ")
        bottom.plot(z, data["delta_lo"], "-", color="#ff9a90", lw=2.2, alpha=bottom_alpha, label="16th percentile")
    bottom.axhline(0, color="#d3dae7", lw=1.7, alpha=0.85)
    style_axis(bottom)
    bottom.set_xlim(6, 10)
    bottom.set_ylim(-0.22, 1.32)
    bottom.set_xlabel("redshift  $z$", color=FG, fontsize=17, labelpad=8)
    bottom.set_ylabel("$\Delta = f_{esc}^{req} - f_{esc}^{inf}$", color=FG, fontsize=17, labelpad=12)


def rail_heading(fig, text):
    add_text(fig, 0.725, 0.84, text, 24, weight="bold")


def rail_lines(fig, lines, start=0.77, gap=0.105):
    for index, (label, body, color) in enumerate(lines):
        y = start - index * gap
        add_text(fig, 0.725, y, label, 14, color=color, weight="bold")
        add_text(fig, 0.725, y - 0.033, body, 14, color=FG, linespacing=1.2)


def save_state(fig, name):
    path = STATES / name
    fig.savefig(path, dpi=100, facecolor=BG, metadata={"Software": "worker-yui static proposal"})
    plt.close(fig)
    with Image.open(path) as image:
        if image.size != (1920, 1080):
            raise RuntimeError(f"unexpected dimensions for {path}: {image.size}")
    return path


def render_states(source):
    g = source["grid_fiducial"]
    n = source["corner_boost_none"]["grid"]
    data = {
        "z": [row["z"] for row in g],
        "req_lo": [row["f_required"][0] for row in g],
        "req_med": [row["f_required"][1] for row in g],
        "req_hi": [row["f_required"][2] for row in g],
        "inf_lo": [row["f_inferred"][0] for row in g],
        "inf_med": [row["f_inferred"][1] for row in g],
        "inf_hi": [row["f_inferred"][2] for row in g],
        "delta_lo": [row["delta"][0] for row in g],
        "delta_med": [row["delta"][1] for row in g],
        "delta_hi": [row["delta"][2] for row in g],
        "shortfall": [row["frac_shortfall"] for row in g],
        "no_tail_delta_lo": [row["delta"][0] for row in n],
    }
    zc = source["closure_crossing_fiducial"]["z_c"]
    zc_boot = source["closure_crossing_fiducial"]["bootstrap_16_50_84"]
    zm = source["median_crossing_fiducial"]["z_m"]
    zc_no = source["corner_boost_none"]["closure_crossing_z_c"]
    zc_no_boot = source["corner_boost_none"]["bootstrap_16_50_84"]
    paths = []

    fig, top, bottom, rail = setup_figure("Can galaxies leak enough ionizing light?", "01 / 08")
    draw_base(top, bottom, data, top_alpha=0.30, bottom_alpha=0.28)
    rail_heading(fig, "Escape fraction")
    rail_lines(fig, [
        ("MEANING", "share of ionizing photons\nthat get out of galaxies", GOLD),
        ("COMPARE", "required leakage\nversus proxy-based leakage", INF),
        ("STATUS", "model propagation;\nno new measurement", WARN),
    ])
    paths.append(save_state(fig, "S01_question_preview.png"))

    fig, top, bottom, rail = setup_figure("Required and proxy-inferred escape fractions", "02 / 08")
    draw_base(top, bottom, data, show_bottom=False)
    bottom.text(8.0, 0.40, "Δ panel revealed next", ha="center", va="center", color="#6c7890", fontsize=18)
    rail_heading(fig, "Read the top panel")
    rail_lines(fig, [
        ("REQUIRED", "rises with redshift\nunder the budget model", REQ),
        ("INFERRED", "fixed in redshift because\nlow-z proxies are reused", INF),
        ("BANDS", "16–84% of the stated\nmodel systematics", GOLD),
    ])
    paths.append(save_state(fig, "S02_required_vs_inferred.png"))

    fig, top, bottom, rail = setup_figure("A zero-spanning interval still allows balance", "03 / 08")
    draw_base(top, bottom, data, top_alpha=0.34)
    bottom.text(9.94, 0.025, "Δ = 0", ha="right", va="bottom", color=FG, fontsize=14)
    rail_heading(fig, "Define the criterion")
    rail_lines(fig, [
        ("Δ", "required minus inferred", REQ),
        ("LOWER EDGE", "16th percentile of Δ", GOLD),
        ("BALANCE ALLOWED", "while the 16–84%\ninterval still spans zero", GREEN),
    ])
    paths.append(save_state(fig, "S03_delta_definition.png"))

    fig, top, bottom, rail = setup_figure("The closure envelope leaves zero at z = 8.045", "04 / 08")
    draw_base(top, bottom, data, top_alpha=0.23)
    bottom.axvline(zc, color=GREEN, lw=2.6, ls="--")
    bottom.plot([zc], [0], "o", ms=11, color=GREEN, mec=BG, mew=2, zorder=5)
    bottom.annotate(
        "lower edge touches Δ = 0",
        xy=(zc, 0), xytext=(8.28, -0.15),
        color=FG, fontsize=14,
        arrowprops={"arrowstyle": "->", "color": GREEN, "lw": 1.8},
    )
    bottom.axvspan(zc_boot[0], zc_boot[2], color=GREEN, alpha=0.22)
    bottom.axvline(zm, color="#8ea0ba", lw=1.4, ls=":")
    rail_heading(fig, "Two different crossings")
    rail_lines(fig, [
        ("CLOSURE ENVELOPE", f"z_c = {zc:.3f}\nfinite-MC 16–84%: 8.030–8.059", GREEN),
        ("MEDIAN Δ", f"z_m = {zm:.3f}\nnot the headline criterion", DIM),
        ("GEOMETRY", "16th percentile reaches\nthe zero line", GOLD),
    ], gap=0.13)
    paths.append(save_state(fig, "S04_closure_crossing.png"))

    fig, top, bottom, rail = setup_figure("Conditional shortfall rises with redshift", "05 / 08")
    draw_base(top, bottom, data, top_alpha=0.20)
    for z_key, pct in [(7.0, 66), (8.0, 83), (9.0, 93)]:
        row = data["z"].index(z_key)
        y = data["delta_med"][row]
        bottom.plot([z_key], [y], "o", ms=12, color=GOLD, mec=BG, mew=2, zorder=6)
        bottom.annotate(
            f"{pct}%",
            xy=(z_key, y), xytext=(z_key, y + 0.20),
            ha="center", color=GOLD, fontsize=19, fontweight="bold",
            arrowprops={"arrowstyle": "-", "color": GOLD, "lw": 1.2},
        )
    rail_heading(fig, "Key every percentage")
    rail_lines(fig, [
        ("z = 7", "66% with Δ > 0", GOLD),
        ("z = 8", "83% with Δ > 0", GOLD),
        ("z = 9", "93% with Δ > 0", GOLD),
        ("BOUNDARY", "conditional model mass,\nnot real-world probability", WARN),
    ], start=0.77, gap=0.105)
    paths.append(save_state(fig, "S05_keyed_probabilities.png"))

    fig, top, bottom, rail = setup_figure("A separate no-tail run moves the crossing earlier", "06 / 08")
    draw_base(top, bottom, data, top_alpha=0.16, bottom_alpha=0.50)
    bottom.plot(data["z"], data["no_tail_delta_lo"], color=NO_TAIL, lw=3.0, ls=(0, (2, 2)), label="16th percentile, no SFRD tail")
    bottom.axvline(zc, color=GREEN, lw=1.8, ls="--", alpha=0.75)
    bottom.axvline(zc_no, color=NO_TAIL, lw=2.4, ls="--")
    bottom.axvspan(zc_no_boot[0], zc_no_boot[2], color=NO_TAIL, alpha=0.16)
    bottom.plot([zc_no], [0], "o", ms=10, color=NO_TAIL, mec=BG, mew=2, zorder=6)
    bottom.text(zc_no + 0.05, 1.18, "no-tail 7.615", rotation=90, color=NO_TAIL, fontsize=12, va="top")
    bottom.text(zc + 0.05, 1.18, "fiducial 8.045", rotation=90, color=GREEN, fontsize=12, va="top")
    legend = bottom.legend(loc="upper left", frameon=True, fontsize=13)
    legend.get_frame().set_facecolor("#0d1422")
    legend.get_frame().set_edgecolor("#40506a")
    for text in legend.get_texts():
        text.set_color(FG)
    rail_heading(fig, "Separate no-tail run")
    rail_lines(fig, [
        ("ONE PRIOR FAMILY", "remove the JWST-motivated\nSFRD tail; draws unpaired", NO_TAIL),
        ("NO-TAIL", f"z_c = {zc_no:.3f}; finite-MC\n16–84%: 7.602–7.631", NO_TAIL),
        ("FIDUCIAL", f"z_c = {zc:.3f}\nSFRD tail retained", GREEN),
        ("DIRECTION", "earlier crossing means\nclosure gets harder", GREEN),
    ], gap=0.105)
    paths.append(save_state(fig, "S06_no_tail_scenario.png"))

    fig, top, bottom, rail = setup_figure("A dominant omission sits outside this Monte Carlo", "07 / 08")
    draw_base(top, bottom, data, top_alpha=0.36, bottom_alpha=0.55)
    rail_heading(fig, "Boundary, not inventory")
    rail_lines(fig, [
        ("PROPAGATED EXAMPLES", "ionizing efficiency\nIGM clumping · SFRD priors", INF),
        ("DOMINANT OMISSION", "do low-z proxy calibrations\ntransport to z > 6?", WARN),
        ("NOT EXHAUSTIVE", "other structural assumptions\nalso remain unpropagated", DIM),
        ("STATUS", "no survey measurement\nin this study", GOLD),
    ], start=0.76, gap=0.13)
    paths.append(save_state(fig, "S07_model_boundary.png"))

    fig, top, bottom, rail = setup_figure("A conditional crossing, with a clear next measurement", "08 / 08")
    draw_base(top, bottom, data, top_alpha=0.42, bottom_alpha=0.65)
    bottom.axvline(zc, color=GREEN, lw=2.2, ls="--")
    bottom.plot([zc], [0], "o", ms=9, color=GREEN, mec=BG, mew=2, zorder=6)
    rail_heading(fig, "Scientific summary")
    rail_lines(fig, [
        ("FINDING", "closure envelope leaves zero\nat z_c = 8.045", GREEN),
        ("EVIDENCE", "lower Δ edge crosses zero\nfinite-MC 16–84%:\n8.030–8.059", GOLD),
        ("BOUNDARY", "frozen low-z anchors;\nno new measurement", WARN),
        ("NEXT TEST", "measure proxy transport\nat high redshift", INF),
    ], start=0.77, gap=0.115)
    paths.append(save_state(fig, "S08_summary.png"))
    return paths


def make_contact_sheet(paths):
    font_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    try:
        label_font = ImageFont.truetype(font_path, 28)
    except OSError:
        label_font = ImageFont.load_default()
    tiles = []
    for index, path in enumerate(paths, 1):
        with Image.open(path) as source:
            image = source.convert("RGB")
            image.thumbnail((640, 360), Image.Resampling.LANCZOS)
        tile = Image.new("RGB", (660, 410), (7, 11, 19))
        tile.paste(image, ((660 - image.width) // 2, 8))
        draw = ImageDraw.Draw(tile)
        draw.text((16, 375), f"S{index:02d}", font=label_font, fill=(236, 242, 251))
        tiles.append(tile)
    columns = 2
    rows = math.ceil(len(tiles) / columns)
    sheet = Image.new("RGB", (columns * 660, rows * 410), (7, 11, 19))
    for index, tile in enumerate(tiles):
        sheet.paste(tile, ((index % columns) * 660, (index // columns) * 410))
    path = OUT / "static_states_contact_sheet.jpg"
    sheet.save(path, quality=94)
    return path


def main():
    source_hash = sha256(SOURCE)
    if source_hash != EXPECTED_SOURCE_SHA256:
        raise SystemExit(f"source hash drift: {source_hash}")
    OUT.mkdir(parents=True, exist_ok=True)
    STATES.mkdir(parents=True, exist_ok=True)
    source = json.loads(SOURCE.read_text())
    paths = render_states(source)
    contact_sheet = make_contact_sheet(paths)
    manifest = {
        "packet_type": "STATIC_REVIEW_PROPOSAL__NOT_CANDIDATE",
        "source_path": str(SOURCE),
        "source_sha256": source_hash,
        "renderer_path": str(Path(__file__).resolve()),
        "state_count": len(paths),
        "states": [
            {"path": str(path), "sha256": sha256(path), "bytes": path.stat().st_size, "dimensions": [1920, 1080]}
            for path in paths
        ],
        "contact_sheet": {"path": str(contact_sheet), "sha256": sha256(contact_sheet), "bytes": contact_sheet.stat().st_size},
        "scientific_geometry": "exact deterministic redraw from frozen arrays; no generated values",
        "audio": "none; static proposal only",
        "mp4": "not produced",
        "publication": "not authorized",
    }
    manifest_path = OUT / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
