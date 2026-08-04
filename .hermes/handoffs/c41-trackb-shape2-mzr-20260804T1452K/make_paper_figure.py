#!/usr/bin/env python3
"""make_paper_figure.py — anchor-gap paper figure (Lana, from receipted artifacts only).

Reads T3_REAL_SAMPLE.jsonl (the 5 anchors) and T3_REAL_RESULTS.json (bins,
below-floor count, frozen forecasts v1/v2, anchor-frame form) — no number is
typed here that does not come from those files. The AM13 curve is drawn from
the anchor_frame.form recorded in the results (AM13 eq. 5 parameters as frozen
in the reviewed t3_real.py). Outputs ANCHOR_GAP_FIGURE.png + .pdf. No network.

Palette: reference categorical slots 1-3 (#2a78d6 blue = actual/measured,
#eb6834 orange = forecast v1, #1baf7a aqua = forecast v2), validated
colorblind-safe all-pairs; forecasts additionally carry hatch textures and all
bars carry direct value labels (contrast relief for the aqua slot).
"""
import json, math, os

LANE = os.path.dirname(os.path.abspath(__file__))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED = "#1a1a19", "#6b6a63"

res = json.load(open(os.path.join(LANE, "T3_REAL_RESULTS.json")))
rows = [json.loads(l) for l in open(os.path.join(LANE, "T3_REAL_SAMPLE.jsonl"))]
anchors = [r for r in rows if r.get("exclusion") is None and r.get("oh_direct")]
assert len(anchors) == res["forecast_vs_actual"]["actual_usable_anchors_total"] == 5

# AM13 eq.5 asymptotic form exactly as frozen in results["anchor_frame"]["form"]
AM13_ASYM, AM13_LOGMTO, AM13_GAMMA = 8.798, 8.901, 0.640
assert res["anchor_frame"]["form"] == (
    "AM13 eq.5 asymptotic: 8.798 - log10(1+(10^(8.901-logM))^0.640)")

def anchor_oh(logm):
    return AM13_ASYM - math.log10(1.0 + (10 ** (AM13_LOGMTO - logm)) ** AM13_GAMMA)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.2))
for ax in (ax1, ax2):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color(MUTED)
    ax.tick_params(colors=MUTED, labelcolor=INK)

# ---------------- panel (a): the MZR plane ----------------
BIN_EDGES = [8.0, 9.0, 10.0]
ax1.axvspan(7.35, 8.0, color="#e9e8e2", zorder=0)
for e in BIN_EDGES:
    ax1.axvline(e, color="#d8d7cf", lw=1, zorder=0)
am_x = [x / 100 for x in range(800, 1051, 5)]
ax1.plot(am_x, [anchor_oh(x) for x in am_x], ls="--", lw=2, color=INK,
         label="AM13 T$_e$ anchor frame (z<3)", zorder=2)
xs = [r["logmass"] for r in anchors]
ys = [r["oh_direct"] for r in anchors]
ax1.scatter(xs, ys, s=64, color=BLUE, edgecolors="white", linewidths=2,
            label=f"A$'$ direct-T$_e$ anchors, z>3 (N={len(anchors)})", zorder=3)
for r in anchors:
    ax1.annotate(r["id"].strip(), (r["logmass"], r["oh_direct"]),
                 textcoords="offset points", xytext=(7, -3), fontsize=7.5, color=MUTED)
ax1.text(7.67, 8.62, "below frozen\nbin floor (logM<8)", fontsize=8, color=MUTED,
         ha="center")
ax1.set_xlim(7.35, 10.6)
ax1.set_ylim(6.95, 8.9)
ax1.set_xlabel(r"$\log\,M_*/M_\odot$", color=INK)
ax1.set_ylabel(r"$12+\log(\mathrm{O/H})$ (direct T$_e$)", color=INK)
ax1.legend(loc="lower right", frameon=False, fontsize=8.5)
ax1.set_title("(a) The five contract-grade public anchors", fontsize=10, color=INK, loc="left")

# ---------------- panel (b): forecast vs actual per bin ----------------
fva = res["forecast_vs_actual"]
v1 = fva["frozen_forecast_v1"]["expected_N_anchors_z_gt_3"]
v2 = fva["frozen_forecast_v2"]["expected_N_anchors_z_gt_3"]
act = fva["actual_per_bin"]
bins = ["M_star_bin_8_9", "M_star_bin_9_10", "M_star_bin_gt_10"]
labels = [r"$8 \leq \log M_* < 9$", r"$9 \leq \log M_* < 10$", r"$\log M_* \geq 10$"]
x = range(len(bins))
w = 0.27
def bars(offs, vals, color, label, hatch=None):
    b = ax2.bar([i + offs for i in x], vals, width=w, color=color, label=label,
                hatch=hatch, edgecolor="white", linewidth=2, zorder=2)
    for rect, v in zip(b, vals):
        ax2.annotate(str(v), (rect.get_x() + rect.get_width() / 2, rect.get_height()),
                     ha="center", va="bottom", fontsize=9, color=INK,
                     xytext=(0, 2), textcoords="offset points")
bars(-w, [v1[b] for b in bins], ORANGE, "forecast v1 (frozen pre-fetch)", hatch="//")
bars(0.0, [v2[b] for b in bins], AQUA, "forecast v2 (re-frozen, Ruling 3)", hatch="\\\\")
bars(+w, [act[b] for b in bins], BLUE, "actual contract-grade anchors")
ax2.axhline(3, color=MUTED, lw=1, ls=":", zorder=1)
ax2.text(2.45, 3.6, "3-anchor\nbin minimum", fontsize=8, color=MUTED, ha="right", va="bottom")
below = res["per_class_counts"]["below_bin_floor"]
ax2.text(0.0, 0.99,
         f"+{below} verified anchors below the frozen\nlowest bin edge (logM<8): binned nowhere",
         transform=ax2.transAxes, fontsize=8, color=MUTED, va="top")
ax2.set_xticks(list(x))
ax2.set_xticklabels(labels, fontsize=9)
ax2.set_ylabel("N (T$_e$ anchors, z>3)", color=INK)
ax2.set_ylim(0, 49)
ax2.legend(loc="upper right", bbox_to_anchor=(1.0, 0.90), frameon=False, fontsize=8.5)
ax2.set_title("(b) The anchor gap: frozen forecasts vs the public archive", fontsize=10,
              color=INK, loc="left")

fig.tight_layout()
for ext in ("png", "pdf"):
    fig.savefig(os.path.join(LANE, f"ANCHOR_GAP_FIGURE.{ext}"),
                dpi=200 if ext == "png" else None)
print("anchors plotted:", [(r["id"].strip(), r["logmass"], r["oh_direct"]) for r in anchors])
print("bins v1", v1, "v2", v2, "actual", act, "below_floor", below)
print("wrote ANCHOR_GAP_FIGURE.png/.pdf")
