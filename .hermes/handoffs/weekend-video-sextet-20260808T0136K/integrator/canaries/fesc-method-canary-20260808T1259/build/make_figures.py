#!/usr/bin/env python3
"""Deterministic method-only figure for the fesc z-sweep canary (v1).

A DEFINITIONS diagram — labeled quantity boxes, no curves, no axis values —
because this deck carries no result geometry. The two-panel evidence surface is
described, not drawn: drawing schematic curves could imply the actual trend,
which is result-layer and unauthorized. Labels come from the lane's OWN
storyboard proposal (S02/S03 definitions) and TREND_DATA.json's frozen grid
description. Deterministic; metadata={} pinned.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
CAN = os.path.dirname(HERE)
OUT = os.path.join(CAN, "figures")

BG = "#0b0f1a"
FG = "#e9eef7"
DIM = "#96a3ba"
ACCENT = "#7ab2ff"
GRID = "#2a3346"
AMBER = "#d69a66"

plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "text.color": FG, "font.family": "Arial",
    "svg.hashsalt": "fesc-method-canary-v1",
})

with open(os.path.join(CAN, "sources", "TREND_DATA.json")) as f:
    trend = json.load(f)
grid_desc = trend["source"]              # "trend-grid 9 runs z=6.0..10.0"
n_runs = len(trend["rows"])              # 9

fig, ax = plt.subplots(figsize=(15.0, 8.0), dpi=100)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")


def box(x, y, w, h, edge):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012",
                                linewidth=2.0, edgecolor=edge, facecolor="#101828"))


def arrow(x1, y1, x2, y2, color=ACCENT):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=20, linewidth=2.0, color=color))


box(0.03, 0.62, 0.42, 0.26, GRID)
ax.text(0.05, 0.815, "REQUIRED escape fraction", fontsize=16, color=ACCENT, fontweight="bold")
ax.text(0.05, 0.745, "what the reionization budget demands at each", fontsize=13.5, color=FG)
ax.text(0.05, 0.695, "redshift step — median with a 16–84% model band", fontsize=13.5, color=FG)
ax.text(0.05, 0.640, "rises as the budget tightens", fontsize=12.5, color=DIM)

box(0.03, 0.24, 0.42, 0.26, GRID)
ax.text(0.05, 0.435, "INFERRED escape fraction", fontsize=16, color=ACCENT, fontweight="bold")
ax.text(0.05, 0.365, "the same frozen low-redshift proxy anchors,", fontsize=13.5, color=FG)
ax.text(0.05, 0.315, "transported unchanged — median with a 16–84% band", fontsize=13.5, color=FG)
ax.text(0.05, 0.260, "fixed by construction, not re-measured", fontsize=12.5, color=DIM)

arrow(0.455, 0.75, 0.545, 0.60)
arrow(0.455, 0.37, 0.545, 0.50)

box(0.555, 0.40, 0.42, 0.30, ACCENT)
ax.text(0.765, 0.635, "Δ = required − inferred", fontsize=19, color=FG,
        ha="center", fontweight="bold")
ax.text(0.765, 0.565, "band: 16–84% model interval", fontsize=14, color=FG, ha="center")
ax.text(0.765, 0.505, "the budget can still balance while", fontsize=13, color=DIM, ha="center")
ax.text(0.765, 0.455, "the interval spans zero", fontsize=13, color=DIM, ha="center")

box(0.555, 0.13, 0.42, 0.185, AMBER)
ax.text(0.765, 0.265, "how a crossing is read", fontsize=14.5, color=AMBER,
        ha="center", fontweight="bold")
ax.text(0.765, 0.205, "from the 16th-percentile EDGE reaching zero —", fontsize=12.5,
        color=FG, ha="center")
ax.text(0.765, 0.155, "never from the median; the two are different quantities",
        fontsize=12.5, color=FG, ha="center")

ax.text(0.5, 0.975,
        "The comparison, defined — quantities and reading rule, no data drawn",
        fontsize=20, color=FG, ha="center", va="top")
fig.text(0.5, 0.075, "CONCEPTUAL — definitions, not data. No curve, axis value, or crossing"
         " is shown in this cut.", fontsize=14, color=AMBER, ha="center", fontweight="bold")
fig.text(0.5, 0.038,
         f"Frozen model grid: {grid_desc} ({n_runs} runs) · "
         "NebulaMind z-sweep model output · 2026-08-04",
         fontsize=12.5, color=DIM, ha="center")
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.11)
fig.savefig(os.path.join(OUT, "comparison_definitions.png"), metadata={})
plt.close(fig)

print("figure written:", sorted(os.listdir(OUT)))
