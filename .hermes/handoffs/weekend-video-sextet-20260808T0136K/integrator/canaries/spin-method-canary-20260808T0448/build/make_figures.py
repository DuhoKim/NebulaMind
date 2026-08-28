#!/usr/bin/env python3
"""Deterministic method-only figures for the galaxy-spin visual canary, v3.

v3 correction (integration pass 6): the spin lane's completed independent audit
(INDEPENDENT_QA.md, v3 adversarial blocker upheld through the v5 PASS) requires zero
visible forbidden audience terms; the schematic boundary line no longer names the
forbidden contexts and states the boundary neutrally. Counts, geometry, and every
other pixel-generating statement are unchanged from v2.

v2 correction (evidence-backed, integration pass 4): T1_FUNNEL.json records the
SPIRAL-flag readout and the two dominance readouts as SIBLING entries under
funnel.zooSpec — three predeclared readouts of one frozen source, each with its
own pass/classified/tie accounting. The v1 figure drew them as a descending
sequential funnel ("each rung only narrows it"), asserting a nesting the cited
artifact does not state. The spin worker lane's independently validated
claim-traceability (lane-spin-parity/worker-yui, static proposal v2) renders
the same counts as parallel branches; this figure adopts that structure.

Everything else is unchanged from v1: counts are read from the pinned copy of
T1_FUNNEL.json (sha-verified against the lane freeze); nothing is computed from
the counts — no asymmetry, no ratio, no significance; quarantined result
figures are untouched. Deterministic: fixed sizes, fixed dpi, no timestamps,
no randomness, metadata={} pinned.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
CAN = os.path.dirname(HERE)
SRC = os.path.join(CAN, "sources", "T1_FUNNEL.json")
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
    "font.family": "Arial", "svg.hashsalt": "spin-method-canary-v8",
})

with open(SRC) as f:
    t1 = json.load(f)

fun = t1["funnel"]["zooSpec"]
rows_parsed = t1["files"]["zooSpec"]["rows_parsed"]

# ------------------------------------------------- parallel readouts figure --
fig, ax = plt.subplots(figsize=(15.0, 8.0), dpi=100)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")


def box(x, y, w, h, edge):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012",
                       linewidth=2.0, edgecolor=edge, facecolor="#101828")
    ax.add_patch(p)


# source box
box(0.02, 0.36, 0.22, 0.30, ACCENT)
ax.text(0.13, 0.60, "FROZEN SOURCE", fontsize=15, color=ACCENT,
        ha="center", fontweight="bold")
ax.text(0.13, 0.505, f"{rows_parsed:,}", fontsize=30, color=FG,
        ha="center", fontweight="bold")
ax.text(0.13, 0.425, "rows parsed (zooSpec)", fontsize=13, color=DIM, ha="center")

readouts = [
    (0.70, "RELEASE SPIRAL FLAG readout",
     f"{fun['SPIRAL_FLAG']['N_pass']:,} pass · "
     f"{fun['SPIRAL_FLAG']['N_classified']:,} decisively labelled",
     f"{fun['SPIRAL_FLAG']['N_tie']:,} ties excluded"),
    (0.39, "DOMINANCE ≥ 0.60 readout",
     f"{fun['0.60']['N_classified']:,} decisively labelled",
     "ties structurally impossible"),
    (0.08, "DOMINANCE ≥ 0.80 readout",
     f"{fun['0.80']['N_classified']:,} decisively labelled",
     "ties structurally impossible"),
]
for y, title, line1, line2 in readouts:
    box(0.36, y, 0.60, 0.22, GRID)
    ax.text(0.385, y + 0.155, title, fontsize=15.5, color=ACCENT, fontweight="bold")
    ax.text(0.385, y + 0.085, line1, fontsize=16, color=FG)
    ax.text(0.385, y + 0.028, line2, fontsize=13, color=DIM)
    ax.add_patch(FancyArrowPatch((0.245, 0.51), (0.352, y + 0.11),
                                 arrowstyle="-|>", mutation_scale=22,
                                 linewidth=2.0, color=ACCENT))

ax.text(0.5, 0.965,
        "Three predeclared readouts of one frozen source — counts as recorded in T1_FUNNEL.json",
        fontsize=20, color=FG, ha="center", va="top")
ax.text(0.5, 0.005,
        "PARALLEL READOUTS — NOT A SEQUENTIAL FUNNEL: each readout starts from the same frozen source.",
        fontsize=14.5, color=AMBER, ha="center", va="bottom", fontweight="bold")

acct = (
    "Frozen per-readout accounting (sample definition, not a result):   "
    f"SPIRAL flag  CW {fun['SPIRAL_FLAG']['N_CW']:,} · ACW {fun['SPIRAL_FLAG']['N_ACW']:,}     "
    f"0.60  CW {fun['0.60']['N_CW']:,} · ACW {fun['0.60']['N_ACW']:,}     "
    f"0.80  CW {fun['0.80']['N_CW']:,} · ACW {fun['0.80']['N_ACW']:,}"
)
fig.text(0.015, 0.118,
         "dominance threshold: the larger of the archive's spin-vote fractions (P_CW / P_ACW)"
         " must reach 0.60 or 0.80 — above one half, a tie is impossible.",
         fontsize=12.5, color=DIM)
fig.text(0.015, 0.078, acct, fontsize=12.5, color=DIM)
fig.text(0.015, 0.040,
         "The asymmetry A is NOT computed or shown in this method-only cut.  "
         "Galaxy Zoo 1 DR · frozen NebulaMind T1 run · 2026-08-05",
         fontsize=12.5, color=DIM)
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.17)
fig.savefig(os.path.join(OUT, "readouts_method.png"), metadata={})
plt.close(fig)

# ------------------------------------------------------------- schematic ----
# unchanged from v1 apart from the hashsalt above
import numpy as np


def spiral_arm(handed, phase):
    th = np.linspace(0.0, 3.6 * np.pi / 2, 300)
    r = 0.12 * np.exp(0.28 * th)
    x = r * np.cos(handed * th + phase)
    y = r * np.sin(handed * th + phase)
    return x, y


fig, axes = plt.subplots(1, 2, figsize=(15.0, 7.2), dpi=100)
for ax2, handed, title, sub in (
    (axes[0], -1, "appears clockwise (CW)", "archive column P_CW"),
    (axes[1], +1, "appears anticlockwise (ACW)", "archive column P_ACW"),
):
    for phase in (0.0, np.pi):
        x, y = spiral_arm(handed, phase)
        ax2.plot(x, y, color=ACCENT, lw=3.2, solid_capstyle="round")
    ax2.scatter([0], [0], s=420, color=FG, zorder=3)
    ax2.set_xlim(-0.85, 0.85)
    ax2.set_ylim(-0.85, 0.85)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title(title, fontsize=20, color=FG, pad=10)
    ax2.text(0, -0.80, sub, fontsize=15, color=DIM, ha="center")

fig.text(0.5, 0.50, "mirror\n<-->", fontsize=22, color=FG, ha="center", va="center")
fig.text(0.5, 0.985,
         "One galaxy, two records: a horizontal mirror reverses apparent handedness",
         fontsize=21, color=FG, ha="center", va="top")
fig.text(0.5, 0.045,
         "Predeclared control logic: a signal in the sky must flip sign under mirroring;"
         " one in the classifiers need not.",
         fontsize=14.5, color=DIM, ha="center")
fig.text(0.5, 0.012,
         "Whether stored directions are as-seen or corrected-back is UNRESOLVED —"
         " until the convention is stated, the measurement's meaning is not recoverable.",
         fontsize=14.5, color=DIM, ha="center")
fig.subplots_adjust(left=0.03, right=0.97, top=0.82, bottom=0.13, wspace=0.25)
fig.savefig(os.path.join(OUT, "handedness_schematic.png"), metadata={})
plt.close(fig)

print("figures written:", sorted(os.listdir(OUT)))
