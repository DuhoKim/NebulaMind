#!/usr/bin/env python3
"""Deterministic method-only figure for the MZR archive-census canary (v1).

Every count drawn here is read from the pinned copies of the lane's OWN frozen
artifacts (T1_MZR_MANIFEST.json, T1_FINDINGS.md) — the spin lane's content is
NOT reused; only the method-only pattern is. Nothing is computed from the
counts: no eligibility verdicts, no relation, no measurement.

Deterministic: fixed sizes, fixed dpi, no timestamps, no randomness,
metadata={} pinned.
"""
import json
import os
import re

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
    "text.color": FG, "axes.edgecolor": GRID, "axes.labelcolor": DIM,
    "xtick.color": DIM, "ytick.color": DIM,
    "font.family": "Arial", "svg.hashsalt": "mzr-census-method-canary-v1",
})

with open(os.path.join(CAN, "sources", "T1_MZR_MANIFEST.json")) as f:
    man = json.load(f)
n_pre = man["n_candidates_pre_filter"]          # 178
n_cand = man["n_candidates"]                    # 157
dropped = man["dropped_candidates"]
n_drop = len(dropped)                            # 21
axis_counts = {}
for d in dropped:
    for ax in d["axes_emptied_by_modifier_filter"]:
        axis_counts[ax] = axis_counts.get(ax, 0) + 1
drop_z = axis_counts.get("redshift", 0)          # 19
drop_ab = axis_counts.get("abundance", 0)        # 2
assert n_pre - n_drop == n_cand

# per-axis UCD / UCD+name reach from the frozen findings table
findings = open(os.path.join(CAN, "sources", "T1_FINDINGS.md")).read()
reach = {}
for axis in ("abundance", "mass", "redshift"):
    m = re.search(rf"\|\s*{axis}\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|", findings)
    reach[axis] = (m.group(1), m.group(2))

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


ylist = [0.72, 0.44, 0.16]
for (axis, (ucd, both)), y in zip(reach.items(), ylist):
    box(0.02, y, 0.30, 0.20, GRID)
    ax.text(0.04, y + 0.145, f"{axis.upper()} search axis", fontsize=15.5,
            color=ACCENT, fontweight="bold")
    ax.text(0.04, y + 0.082, f"UCD reach {ucd}", fontsize=14, color=FG)
    ax.text(0.04, y + 0.028, f"UCD + name reach {both}", fontsize=14, color=DIM)
    arrow(0.325, y + 0.10, 0.42, 0.52)

box(0.43, 0.40, 0.16, 0.24, ACCENT)
ax.text(0.51, 0.575, "SINGLE-TABLE", fontsize=13, color=ACCENT, ha="center", fontweight="bold")
ax.text(0.51, 0.51, f"{n_pre}", fontsize=30, color=FG, ha="center", fontweight="bold")
ax.text(0.51, 0.435, "three-axis candidates", fontsize=12, color=DIM, ha="center")
arrow(0.595, 0.52, 0.665, 0.52)

box(0.675, 0.40, 0.14, 0.24, AMBER)
ax.text(0.745, 0.575, "MODIFIER FILTER", fontsize=12, color=AMBER, ha="center", fontweight="bold")
ax.text(0.745, 0.51, f"−{n_drop}", fontsize=28, color=FG, ha="center", fontweight="bold")
ax.text(0.745, 0.435, f"{drop_z} redshift · {drop_ab} abundance", fontsize=12,
        color=DIM, ha="center")
arrow(0.82, 0.52, 0.875, 0.52)

box(0.885, 0.38, 0.105, 0.28, ACCENT)
ax.text(0.9375, 0.60, "RECORDED", fontsize=12.5, color=ACCENT, ha="center", fontweight="bold")
ax.text(0.9375, 0.515, f"{n_cand}", fontsize=34, color=FG, ha="center", fontweight="bold")
ax.text(0.9375, 0.425, "candidates", fontsize=12.5, color=DIM, ha="center")

ax.text(0.5, 0.975,
        "Three search axes, one intersection — counts as recorded in the frozen T1 manifest",
        fontsize=20, color=FG, ha="center", va="top")
fig.text(0.5, 0.10,
         "SINGLE-TABLE METADATA INTERSECTION — CROSS-TABLE JOINS AND CROSSMATCHES NOT ASSESSED.",
         fontsize=14.5, color=AMBER, ha="center", fontweight="bold")
fig.text(0.5, 0.055,
         "Metadata reachability only: nothing here claims a table's values are adjudicated"
         " measurements, and no eligibility has been ruled.",
         fontsize=12.5, color=DIM, ha="center")
fig.text(0.5, 0.02,
         "NebulaMind MZR archive census · frozen T1 run · 2026-08-05",
         fontsize=12.5, color=DIM, ha="center")
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.14)
fig.savefig(os.path.join(OUT, "census_spine.png"), metadata={})
plt.close(fig)

print("figure written:", sorted(os.listdir(OUT)))
