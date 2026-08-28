#!/usr/bin/env python3
"""Deterministic method-only figures for the spin-parity visual canary.

Every count drawn here is read from the pinned copy of T1_FUNNEL.json in this
canary's sources/ directory — sha-verified against the lane freeze before use.
Nothing is computed from the counts: no asymmetry, no ratio, no significance.
The quarantined result figures are not read, not reused, not approximated.

Deterministic by construction: fixed figure sizes, fixed dpi, no timestamps,
no randomness. Re-running this script byte-identically reproduces the PNGs
apart from matplotlib's own metadata, which is pinned via metadata={} below.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CAN = os.path.dirname(HERE)
SRC = os.path.join(CAN, "sources", "T1_FUNNEL.json")
OUT = os.path.join(CAN, "figures")

# House style, matched to the shared renderer's locked palette.
BG = "#0b0f1a"
FG = "#e9eef7"
DIM = "#96a3ba"
ACCENT = "#7ab2ff"
GRID = "#2a3346"

plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "text.color": FG, "axes.edgecolor": GRID, "axes.labelcolor": DIM,
    "xtick.color": DIM, "ytick.color": DIM,
    "font.family": "Arial", "svg.hashsalt": "spin-method-canary",
})

with open(SRC) as f:
    t1 = json.load(f)

fun = t1["funnel"]["zooSpec"]
rows_parsed = t1["files"]["zooSpec"]["rows_parsed"]

# ---------------------------------------------------------------- funnel ----
stages = [
    ("Source catalogue rows parsed", rows_parsed, ""),
    ("SPIRAL flag rung — pass", fun["SPIRAL_FLAG"]["N_pass"], ""),
    ("SPIRAL flag rung — decisively labelled", fun["SPIRAL_FLAG"]["N_classified"],
     f"{fun['SPIRAL_FLAG']['N_tie']:,} ties excluded"),
    ("Dominance rung 0.60 — decisively labelled", fun["0.60"]["N_classified"],
     "ties structurally impossible"),
    ("Dominance rung 0.80 — decisively labelled", fun["0.80"]["N_classified"],
     "ties structurally impossible"),
]

fig, ax = plt.subplots(figsize=(15.0, 8.0), dpi=100)
ys = np.arange(len(stages))[::-1]
vals = [s[1] for s in stages]
ax.barh(ys, vals, height=0.52, color=ACCENT, zorder=3)
ax.set_xlim(0, max(vals) * 1.30)
ax.set_ylim(-0.7, len(stages) - 0.3)
ax.set_yticks([])
ax.set_xticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
for y, (label, val, note) in zip(ys, stages):
    ax.text(0, y + 0.40, label, fontsize=17, color=FG, va="bottom")
    ax.text(val + max(vals) * 0.012, y, f"{val:,}", fontsize=18, color=FG,
            va="center", fontweight="bold")
    if note:
        num_w = len(f"{val:,}") * max(vals) * 0.0115
        ax.text(val + max(vals) * 0.030 + num_w, y, f"({note})", fontsize=13,
                color=DIM, va="center")
ax.set_title("Frozen sample funnel — counts as recorded in T1_FUNNEL.json",
             fontsize=20, color=FG, loc="left", pad=18)

# Sample accounting per rung, as text — no bars compare CW with ACW, and no
# asymmetry is computed anywhere in this canary.
acct = (
    "Frozen per-rung accounting (sample definition, not a result):   "
    f"SPIRAL flag  CW {fun['SPIRAL_FLAG']['N_CW']:,} · ACW {fun['SPIRAL_FLAG']['N_ACW']:,}     "
    f"0.60  CW {fun['0.60']['N_CW']:,} · ACW {fun['0.60']['N_ACW']:,}     "
    f"0.80  CW {fun['0.80']['N_CW']:,} · ACW {fun['0.80']['N_ACW']:,}"
)
fig.text(0.015, 0.055, acct, fontsize=12.5, color=DIM)
fig.text(0.015, 0.015,
         "The asymmetry A is NOT computed or shown in this method-only cut.  "
         "source: T1_FUNNEL.json (sha256 ed97758a…)",
         fontsize=12.5, color=DIM)
fig.subplots_adjust(left=0.015, right=0.985, top=0.90, bottom=0.13)
fig.savefig(os.path.join(OUT, "funnel_method.png"), metadata={})
plt.close(fig)

# ------------------------------------------------------------- schematic ----
def spiral_arm(handed, phase):
    """Logarithmic spiral arm; handed=+1 winds one way, -1 its mirror."""
    th = np.linspace(0.0, 3.6 * np.pi / 2, 300)
    r = 0.12 * np.exp(0.28 * th)
    x = r * np.cos(handed * th + phase)
    y = r * np.sin(handed * th + phase)
    return x, y

fig, axes = plt.subplots(1, 2, figsize=(15.0, 7.2), dpi=100)
for ax, handed, title, sub in (
    (axes[0], -1, "appears clockwise (CW)", "archive column P_CW"),
    (axes[1], +1, "appears anticlockwise (ACW)", "archive column P_ACW"),
):
    for phase in (0.0, np.pi):
        x, y = spiral_arm(handed, phase)
        ax.plot(x, y, color=ACCENT, lw=3.2, solid_capstyle="round")
    ax.scatter([0], [0], s=420, color=FG, zorder=3)
    ax.set_xlim(-0.85, 0.85)
    ax.set_ylim(-0.85, 0.85)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=20, color=FG, pad=10)
    ax.text(0, -0.80, sub, fontsize=15, color=DIM, ha="center")

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
         " no sky, dipole, or parity meaning may be attached.",
         fontsize=14.5, color=DIM, ha="center")
fig.subplots_adjust(left=0.03, right=0.97, top=0.82, bottom=0.13, wspace=0.25)
fig.savefig(os.path.join(OUT, "handedness_schematic.png"), metadata={})
plt.close(fig)

print("figures written:", sorted(os.listdir(OUT)))
