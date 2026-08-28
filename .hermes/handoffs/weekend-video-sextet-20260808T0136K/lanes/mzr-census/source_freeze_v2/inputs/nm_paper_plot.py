#!/usr/bin/env python3
"""nm_paper_plot.py — plot a paper's OWN recorded numbers for its video.

Duho, 2026-08-06, asked for literature plots in the video intros. Plots get the opposite
treatment from the backdrop footage: a backdrop may be generated because it carries no
information, but **a chart carries data, and a generated chart is fabricated data** — the single
thing this pipeline exists to refuse. So every plot here is drawn with matplotlib from a JSON
artifact already on disk, and the figure caption names the file it was read from.

Same rule as the cards: if the number is not in a recorded artifact, it does not appear. A plot
that cannot be sourced is not drawn.

Styling matches the video cards (dark, restrained) so a figure can sit in the same cut without
looking imported.

Usage:  nm_paper_plot.py <lane-slug>        # draw whatever that lane supports
        nm_paper_plot.py --list             # what is plottable today
"""
import argparse, json, os, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/Users/duhokim/NebulaMind/NebulaMind"
LANES = os.path.join(ROOT, ".hermes", "handoffs")
OUT = "/Users/duhokim/HermesOps/cockpit/videos/plots"

BG, FG, DIM, ACCENT = "#0b0f1a", "#e9eef7", "#8b98ae", "#7ab2ff"
WARN = "#d69a66"


def style(ax, fig, title, source):
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    for sp in ax.spines.values():
        sp.set_color("#2a3346")
    ax.tick_params(colors=DIM, labelsize=9)
    ax.xaxis.label.set_color(DIM)
    ax.yaxis.label.set_color(DIM)
    ax.set_title(title, color=FG, fontsize=13, pad=12, loc="left")
    # the caption is not decoration: it is the plot's provenance, same as a card's `source`
    fig.text(0.01, 0.015, f"drawn from {source}", color="#5d6a80", fontsize=7)


def save(fig, name, tight=True):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    # tight cropping fights an explicit subplots_adjust; plots that place their own captions
    # opt out so the layout they asked for is the layout that ships
    fig.savefig(p, dpi=160, facecolor=BG, **({"bbox_inches": "tight"} if tight else {}))
    plt.close(fig)
    print(f"  wrote {p}")
    return p


def plot_spin_funnel():
    """The measured funnel, by rung. Counts only — no asymmetry is computed or shown, because
    the lane's frozen contract forbids it and a plot is not an exemption."""
    src = "spin-parity-census-20260805T1922K/T1_FUNNEL.json"
    d = json.load(open(os.path.join(LANES, src)))
    f = (d.get("funnel") or {}).get("zooSpec") or {}
    rungs = [r for r in ("SPIRAL_FLAG", "0.80", "0.60") if r in f]
    if not rungs:
        return None
    passed = [f[r]["N_pass"] for r in rungs]
    classified = [f[r]["N_classified"] for r in rungs]
    ties = [f[r]["N_tie"] for r in rungs]

    fig, ax = plt.subplots(figsize=(7.5, 4))
    x = range(len(rungs))
    ax.bar([i - 0.22 for i in x], passed, width=0.2, color=ACCENT, label="passed the rung")
    ax.bar([i for i in x], classified, width=0.2, color="#7fb27f", label="classified (ties excluded)")
    ax.bar([i + 0.22 for i in x], ties, width=0.2, color=WARN, label="ties")
    ax.set_xticks(list(x)); ax.set_xticklabels(rungs)
    ax.set_ylabel("galaxies")
    ax.legend(facecolor=BG, edgecolor="#2a3346", labelcolor=DIM, fontsize=8)
    style(ax, fig, "Where the sample goes at each rung", src)
    return save(fig, "spin-parity-census_funnel.png")


def plot_mzr_census():
    """157 candidates, and how few carry gas-phase evidence."""
    src = "mzr-archive-census-20260805T1857K/T1E_GASPHASE_COUNT.json"
    d = json.load(open(os.path.join(LANES, src)))
    n, total = d.get("count"), d.get("of_candidates")
    if not (n and total):
        return None
    fig, ax = plt.subplots(figsize=(7.5, 2.6))
    ax.barh([0], [total], color="#2a3346", label=f"{total} candidates carrying all three axes")
    ax.barh([0], [n], color=ACCENT, label=f"{n} with explicit gas-phase evidence")
    ax.set_yticks([]); ax.set_xlabel("archive tables")
    ax.legend(facecolor=BG, edgecolor="#2a3346", labelcolor=DIM, fontsize=8, loc="lower right")
    style(ax, fig, "Reach is not eligibility", src)
    return save(fig, "mzr-archive-census_evidence.png")


def plot_anchor_gap():
    """The z>3 anchor null: how many objects survive each stage."""
    src = "c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_RESULTS.json"
    d = json.load(open(os.path.join(LANES, src)))
    bins = d.get("bins") or {}
    labels, counts = [], []
    for k, v in bins.items():
        labels.append(k.replace("M_star_bin_", "logM ").replace("_", "–"))
        counts.append(v.get("N", 0))
    if not labels:
        return None
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    cols = [WARN if c < 3 else ACCENT for c in counts]
    ax.bar(labels, counts, color=cols)
    for i, c in enumerate(counts):
        ax.text(i, c + 0.05, str(c), ha="center", color=FG, fontsize=10)
    ax.set_ylabel("contract-grade anchors")
    ax.set_ylim(0, max(counts + [1]) * 1.4)
    style(ax, fig, "Every mass bin returned no-verdict-possible", src)
    return save(fig, "c41-highz-mzr-calibration-anchored_bins.png")


def plot_spin_conditions():
    """The four conditions side by side. THE plot this study is about: normal and monochrome sit
    together, both mirrored sets sit apart. Counts only — the asymmetry statistic has its own
    figure, and mixing them would let a reader take the bar chart for the result."""
    src = "spin-parity-census-20260805T1922K/T2_MIRROR_BIAS.json"
    d = json.load(open(os.path.join(LANES, src)))
    conds = ["normal", "monochrome", "mirrored_1", "mirrored_2"]
    rungs = ["0.80", "0.60"]
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    w = 0.36
    for j, r in enumerate(rungs):
        vals = []
        for c in conds:
            cell = d["conditions"][c]["rungs"][r]
            vals.append(cell["N_CW"] / cell["N_classified"])
        ax.bar([i + (j - 0.5) * w for i in range(len(conds))], vals, width=w,
               color=(ACCENT if j == 0 else "#7fb27f"), label=f"rung {r}")
    ax.axhline(0.5, color=WARN, lw=1, ls="--")
    ax.text(3.45, 0.502, "parity", color=WARN, fontsize=8, ha="right")
    ax.set_xticks(range(len(conds)))
    ax.set_xticklabels(["normal", "monochrome", "mirrored 1", "mirrored 2"])
    ax.set_ylabel("clockwise fraction")
    ax.set_ylim(0.44, 0.56)
    ax.legend(facecolor=BG, edgecolor="#2a3346", labelcolor=DIM, fontsize=8)
    fig.subplots_adjust(bottom=0.24, left=0.11, right=0.98, top=0.90)
    style(ax, fig, "The mirrored conditions sit on the other side of parity", src)
    fig.text(0.01, 0.055, "normal and monochrome agree; both mirrored sets differ from them and "
                          "from each other only slightly", color="#7c89a0", fontsize=7)
    return save(fig, "spin-parity-census_conditions.png", tight=False)


def plot_spin_asymmetry():
    """A with its error bar, per condition per rung, from the reading artifact. The error bars are
    the point: the separation is many sigma, and a reader should see that rather than be told."""
    src = "spin-parity-census-20260805T1922K/T3_READING.json"
    d = json.load(open(os.path.join(LANES, src)))
    rows = []
    for rung, row in d["per_rung"].items():
        rows.append((f"normal\n{rung}", row["A_normal"], row["sigma_normal"], ACCENT))
        for ms, v in row["sets"].items():
            rows.append((f"{ms.replace('mirrored_', 'mirrored ')}\n{rung}", v["A"], v["sigma"], WARN))
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    xs = range(len(rows))
    ax.errorbar(list(xs), [r[1] for r in rows], yerr=[r[2] for r in rows],
                fmt="o", ms=6, lw=1.4, capsize=4, color=DIM, zorder=1)
    for i, r in enumerate(rows):
        ax.plot([i], [r[1]], "o", ms=7, color=r[3], zorder=2)
    ax.axhline(0.0, color="#5d6a80", lw=1)
    ax.set_xticks(list(xs)); ax.set_xticklabels([r[0] for r in rows], fontsize=8)
    ax.set_ylabel("asymmetry  A = (CW − ACW)/(CW + ACW)")
    fig.subplots_adjust(bottom=0.26, left=0.13, right=0.98, top=0.90)
    style(ax, fig, "The asymmetry, with its error bar, per condition", src)
    fig.text(0.01, 0.055, "error bars are 1σ_A = 2·sqrt(p(1−p)/N). No reading is shown here — the "
                          "branch is a separate, gated step", color="#7c89a0", fontsize=7)
    return save(fig, "spin-parity-census_asymmetry.png", tight=False)


# --- fences welded onto the figure itself -------------------------------------------------
# KUN_VIDEO_CONSULT §5c: once a figure shows four error bars cleanly split across zero, the
# VISUAL claim is stronger than any sentence in the script. If the conditionality lives only in
# prose, the video over-claims by image what it disclaims in text. So the fences are drawn INTO
# the figure, where they cannot be separated from the result they qualify.
SPIN_FENCES = ("classifier mirror-bias on the bias-study sample — NOT a cosmological asymmetry, "
               "dipole or parity result   ·   monochrome = control, reported never read   ·   "
               "two-rung ladder: the SPIRAL-flag rung is unavailable for these conditions")


def _fence(fig, extra=None):
    fig.text(0.01, 0.105, SPIN_FENCES, color="#8b6a4a", fontsize=6.5, wrap=True)
    if extra:
        fig.text(0.01, 0.055, extra, color="#7c89a0", fontsize=7)


def plot_spin_verdict():
    """F1 — THE figure. A with sigma_A per condition, both rungs, zero line drawn.

    normal and the monochrome CONTROL sit one side of zero; both mirror sets sit the other, at
    both rungs. That is the entire finding in one glance. Monochrome comes from Lana's recorded
    table because T3 deliberately carries no monochrome cell — it is a control, never read.
    """
    t3s = "spin-parity-census-20260805T1922K/T3_READING.json"
    d = json.load(open(os.path.join(LANES, t3s)))
    MONO = {"0.80": (-0.066298, 0.012044), "0.60": (-0.058315, 0.011096)}   # LANA §2 table
    order, vals, errs, cols = [], [], [], []
    for rung in ("0.80", "0.60"):
        row = d["per_rung"][rung]
        order.append(f"normal\n{rung}");      vals.append(row["A_normal"]); errs.append(row["sigma_normal"]); cols.append(ACCENT)
        order.append(f"monochrome\n{rung}");  vals.append(MONO[rung][0]);   errs.append(MONO[rung][1]);       cols.append("#7fb27f")
        for ms in ("mirrored_1", "mirrored_2"):
            v = row["sets"][ms]
            order.append(f"{ms.replace('mirrored_','mirrored ')}\n{rung}")
            vals.append(v["A"]); errs.append(v["sigma"]); cols.append(WARN)
    fig, ax = plt.subplots(figsize=(7.8, 4.3))
    ax.errorbar(range(len(vals)), vals, yerr=errs, fmt="none", ecolor=DIM, lw=1.4, capsize=4, zorder=1)
    for i, (v, c) in enumerate(zip(vals, cols)):
        ax.plot([i], [v], "o", ms=7, color=c, zorder=2)
    ax.axhline(0.0, color="#5d6a80", lw=1)
    ax.set_xticks(range(len(order))); ax.set_xticklabels(order, fontsize=7.5)
    ax.set_ylabel("A = (CW − ACW)/(CW + ACW)")
    fig.subplots_adjust(bottom=0.36, left=0.12, right=0.98, top=0.90)
    style(ax, fig, "Both mirrored sets sit on the far side of zero", t3s)
    _fence(fig, "error bars 1σ_A = 2·sqrt(p(1−p)/N)   ·   monochrome from LANA_T3_REDERIVATION.md §2")
    return save(fig, "spin-parity-census_verdict.png", tight=False)


def plot_spin_significance():
    """F2 — |ΔA|/σ_diff for the four primary cells against the drawn, pre-registered 3σ bar.

    Card 13 said "more than a factor of two". Four points above 6σ against a frozen line says it
    exactly, and a viewer can check the claim instead of accepting it.
    """
    src = "spin-parity-census-20260805T1922K/T3_READING.json"
    d = json.load(open(os.path.join(LANES, src)))
    labs, zs = [], []
    for rung in ("0.80", "0.60"):
        for ms, v in d["per_rung"][rung]["sets"].items():
            labs.append(f"{ms.replace('mirrored_','mirrored ')}\n{rung}")
            zs.append(v["abs_diff"] / v["sigma_diff"])
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.bar(range(len(zs)), zs, width=0.5, color=ACCENT)
    for i, z in enumerate(zs):
        ax.text(i, z + 0.15, f"{z:.2f}σ", ha="center", color=FG, fontsize=10)
    ax.axhline(3.0, color=WARN, lw=1.4, ls="--")
    ax.text(len(zs) - 0.4, 3.15, "pre-registered REVERSES bar: 3σ", color=WARN, fontsize=8, ha="right")
    ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylabel("|ΔA| / σ_diff"); ax.set_ylim(0, max(zs) * 1.25)
    fig.subplots_adjust(bottom=0.32, left=0.11, right=0.98, top=0.90)
    style(ax, fig, "Every cell clears the frozen bar by more than twice", src)
    _fence(fig, "σ_diff is independent quadrature on a PAIRED design — conservative, so this "
                "understates the separation   ·   re-derived digit-for-digit: LANA_T3_REDERIVATION.md")
    return save(fig, "spin-parity-census_significance.png", tight=False)


def plot_spin_decomposition():
    """F4 — the honest nuance no card shows: the flip is real, but the mirrored magnitude is
    smaller than a pure mirror predicts. Recorded algebra from LANA §4.1 on published aggregates."""
    src = "spin-parity-census-20260805T1922K/LANA_T3_REDERIVATION.md"
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    names = ["flipping component\n(A_n − A_m)/2", "non-flipping component\n(A_n + A_m)/2"]
    vals, errs = [-0.0559, -0.0120], [0.0083, 0.0083]
    ax.barh(range(2), vals, xerr=errs, height=0.45, color=[ACCENT, WARN],
            error_kw={"ecolor": DIM, "lw": 1.4, "capsize": 4})
    ax.axvline(0.0, color="#5d6a80", lw=1)
    ax.set_yticks(range(2)); ax.set_yticklabels(names, fontsize=9)
    ax.set_xlabel("component of the asymmetry")
    ax.invert_yaxis()
    fig.subplots_adjust(bottom=0.30, left=0.28, right=0.97, top=0.88)
    style(ax, fig, "A clean mirror would leave nothing behind", src)
    _fence(fig, "mirrored_1 at the 0.80 rung. The non-flipping part is under 2σ from zero at every "
                "cell — a coherent hint, not an established fact")
    return save(fig, "spin-parity-census_decomposition.png", tight=False)


def plot_spin_paired():
    """T4's McNemar table as a 2x2. Zero on both diagonals is the whole picture: of the objects
    clearly classified in both conditions, not one kept its label. The blank diagonal says more
    than any sentence, so the figure is the claim and the caption is the fence."""
    src = "spin-parity-census-20260805T1922K/T4_PAIRED_FLIP.json"
    d = json.load(open(os.path.join(LANES, src)))
    cell = d["cells"]["mirrored_1|normal|0.80"]
    m = cell["mcnemar"]
    grid = [[m["CW->CW"], m["CW->ACW"]], [m["ACW->CW"], m["ACW->ACW"]]]
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    for i in range(2):
        for j in range(2):
            v = grid[i][j]
            on_diag = (i == j)
            ax.add_patch(plt.Rectangle((j, 1 - i), 1, 1,
                                       facecolor=("#141a28" if on_diag else "#1d2740"),
                                       edgecolor="#2a3346", lw=1.5))
            ax.text(j + 0.5, 1 - i + 0.5, f"{v:,}", ha="center", va="center",
                    color=(DIM if on_diag else ACCENT), fontsize=26,
                    fontweight=("normal" if on_diag else "bold"))
    ax.set_xlim(0, 2); ax.set_ylim(0, 2)
    ax.set_xticks([0.5, 1.5]); ax.set_xticklabels(["mirrored: CW", "mirrored: ACW"])
    ax.set_yticks([0.5, 1.5]); ax.set_yticklabels(["normal: ACW", "normal: CW"])
    ax.set_xlabel(""); ax.tick_params(length=0)
    fig.subplots_adjust(bottom=0.34, left=0.20, right=0.97, top=0.88)
    style(ax, fig, "Not one object kept its label", src)
    _fence(fig, f"mirrored 1 x normal, 0.80 rung, {cell['n_pair']:,} paired objects   ·   "
                f"pre-registered reading: MIXED")
    return save(fig, "spin-parity-census_paired.png", tight=False)


FESC_FENCE = ("photon-budget closure on one fiducial model grid — NOT a measurement of f_esc, "
              "and not evidence that reionization did or did not close")
MZR_FENCE  = ("archive census of what catalogues HOLD — reach is not eligibility, and no "
              "metallicity relation is fitted or evaluated here")


def plot_fesc_trend():
    """f_required vs f_inferred across the redshift grid, with the crossing the study reports.
    The whole point is the TREND, not one redshift, so the figure shows every grid point."""
    src = "fesc-zsweep-merged-paper-20260804T1040K/TREND_RESULTS.json"
    d = json.load(open(os.path.join(LANES, src)))
    g = d["grid_fiducial"]
    z = [p["z"] for p in g]
    req = [p["f_required"][1] for p in g]          # median of the 16/50/84 triple
    inf = [p["f_inferred"][1] for p in g]
    req_lo = [p["f_required"][0] for p in g]; req_hi = [p["f_required"][2] for p in g]
    inf_lo = [p["f_inferred"][0] for p in g]; inf_hi = [p["f_inferred"][2] for p in g]
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.fill_between(z, req_lo, req_hi, color=ACCENT, alpha=0.18)
    ax.fill_between(z, inf_lo, inf_hi, color=WARN, alpha=0.18)
    ax.plot(z, req, "o-", color=ACCENT, ms=5, label="required to close the budget")
    ax.plot(z, inf, "s-", color=WARN, ms=5, label="inferred from observations")
    zc = (d.get("closure_crossing_fiducial") or {}).get("z_c")
    if zc:
        ax.axvline(zc, color="#7fb27f", lw=1.4, ls="--")
        ax.text(zc + 0.05, max(req_hi) * 0.92, f"crossing z = {zc:.3f}", color="#7fb27f", fontsize=8)
    ax.set_xlabel("redshift"); ax.set_ylabel("escape fraction")
    ax.legend(facecolor=BG, edgecolor="#2a3346", labelcolor=DIM, fontsize=8)
    fig.subplots_adjust(bottom=0.30, left=0.12, right=0.98, top=0.90)
    style(ax, fig, "Where the two curves cross is the result", src)
    fig.text(0.01, 0.105, FESC_FENCE, color="#8b6a4a", fontsize=6.5, wrap=True)
    fig.text(0.01, 0.055, "bands are the 16-84% interval; the crossing is where the interval "
                          "stops spanning zero", color="#7c89a0", fontsize=7)
    return save(fig, "fesc-zsweep-photon-budget_trend.png", tight=False)


def plot_mzr_recall():
    """The instrument test: seven recall members had to come back, three controls had to stay out.
    A census is only worth reading if the search that produced it was tested first."""
    src = "mzr-archive-census-20260805T1857K/T1_MZR_MANIFEST.json"
    d = json.load(open(os.path.join(LANES, src)))
    rec = d.get("recall_members_returned") or {}
    con = d.get("controls_appearing") or {}
    labels = list(rec) + list(con)
    vals = [1 if rec[k] else 0 for k in rec] + [1 if con[k] else 0 for k in con]
    kinds = ["recall"] * len(rec) + ["control"] * len(con)
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    for i, (v, k) in enumerate(zip(vals, kinds)):
        want = 1 if k == "recall" else 0
        ok = (v == want)
        ax.bar([i], [1], color=(ACCENT if k == "recall" else "#7fb27f") if ok else WARN,
               alpha=1.0 if ok else 0.9)
        ax.text(i, 0.5, "returned" if v else "absent", ha="center", va="center",
                color="#0b0f1a", fontsize=8, rotation=90)
    ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels, fontsize=9)
    ax.set_yticks([]); ax.set_ylim(0, 1.25)
    ax.text(len(rec) - 0.5, 1.12, "recall set — must come back", color=ACCENT, fontsize=8, ha="center")
    ax.text(len(rec) + len(con) / 2 - 0.5, 1.12, "controls — must stay out", color="#7fb27f",
            fontsize=8, ha="center")
    fig.subplots_adjust(bottom=0.30, left=0.05, right=0.98, top=0.88)
    style(ax, fig, "The search was tested before it was trusted", src)
    fig.text(0.01, 0.105, MZR_FENCE, color="#8b6a4a", fontsize=6.5, wrap=True)
    fig.text(0.01, 0.055, "the recall set was sha-pinned before the run and read from the pinned "
                          "file, never retyped", color="#7c89a0", fontsize=7)
    return save(fig, "mzr-archive-census_recall.png", tight=False)


DISPERSION = os.path.join(
    ROOT, ".hermes", "handoffs", "galaxy-evolution",
    "corpus-ga-co-2009-2026-20260718", "dispersion_v2.json")


def plot_literature(quantity, title, ylabel, out, note=None, color_by_method=False):
    """An INTRODUCTION plot: what the published literature actually reports, before this lane
    says anything.

    The values are real measurements extracted from papers — each carries a bibcode — so this is
    drawn, never generated, exactly like the results plots. What it shows is the SPREAD: the
    motivation for most of these lanes is that published values for the same quantity disagree by
    more than the effect being chased.

    Measurements with no stated redshift are excluded from the scatter and their count is printed,
    because silently dropping half a sample is how a plot lies without stating a false number.
    """
    src = "galaxy-evolution/corpus-ga-co-2009-2026-20260718/dispersion_v2.json"
    d = json.load(open(DISPERSION))
    ms = [m for m in d["measurements"] if m["quantity"] == quantity]
    wz = [m for m in ms if m.get("redshift") is not None]
    if len(wz) < 8:
        return None
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    if color_by_method:
        # Method matters here: O/H calibrations sit on different scales, so the visible spread is
        # partly systematic, not disagreement about the sky. Colouring says which is which.
        groups = {}
        for m in wz:
            groups.setdefault((m.get("method_raw") or "unstated")[:18], []).append(m)
        top = sorted(groups.items(), key=lambda kv: -len(kv[1]))[:4]
        palette = [ACCENT, "#7fb27f", WARN, "#b48ead"]
        for (name, pts), col in zip(top, palette):
            ax.errorbar([m["redshift"] for m in pts], [m["value"] for m in pts],
                        yerr=[m.get("sigma") or 0 for m in pts], fmt="o", ms=4, lw=0.8,
                        color=col, alpha=0.85, capsize=0, label=f"{name} ({len(pts)})")
        rest = sum(len(v) for k, v in groups.items() if k not in dict(top))
        if rest:
            ax.scatter([], [], c=DIM, label=f"other methods ({rest})")
        ax.legend(facecolor=BG, edgecolor="#2a3346", labelcolor=DIM, fontsize=7, loc="best")
    else:
        ax.errorbar([m["redshift"] for m in wz], [m["value"] for m in wz],
                    yerr=[m.get("sigma") or 0 for m in wz], fmt="o", ms=4, lw=0.8,
                    color=ACCENT, alpha=0.85, capsize=0)
    ax.set_xlabel("redshift")
    ax.set_ylabel(ylabel)
    # the two caption lines live below the axes; without this the coverage note lands on top of
    # the x-label, which is how a provenance line ends up unreadable
    fig.subplots_adjust(bottom=0.30, left=0.10, right=0.98, top=0.90)
    style(ax, fig, title, src)
    tail = f"{len(wz)} of {len(ms)} published values carry a redshift; the rest are not plotted"
    if note:
        tail += f". {note}"
    fig.text(0.01, 0.055, tail, color="#7c89a0", fontsize=7)
    return save(fig, out, tight=False)


def lit_metallicity():
    return plot_literature(
        "metallicity", "What the literature reports for gas-phase metallicity",
        "12 + log(O/H)", "lit_metallicity.png", color_by_method=True,
        note="Spread here is partly calibration, not disagreement about galaxies")


def lit_fesc():
    return plot_literature("fesc", "What the literature reports for escape fraction",
                           "f_esc", "lit_fesc.png")


def lit_uvlf():
    return plot_literature("uvlf_alpha", "What the literature reports for the UV faint-end slope",
                           "alpha", "lit_uvlf_alpha.png")


PLOTS = {
    "spin-parity-census": plot_spin_funnel,
    "spin-conditions": plot_spin_conditions,
    "spin-verdict": plot_spin_verdict,
    "spin-significance": plot_spin_significance,
    "spin-decomposition": plot_spin_decomposition,
    "spin-paired": plot_spin_paired,
    "fesc-trend": plot_fesc_trend,
    "mzr-recall": plot_mzr_recall,
    "spin-asymmetry": plot_spin_asymmetry,
    "mzr-archive-census": plot_mzr_census,
    "c41-highz-mzr-calibration-anchored": plot_anchor_gap,
    # introduction plots: the field's published values, drawn from extracted measurements
    "lit-metallicity": lit_metallicity,
    "lit-fesc": lit_fesc,
    "lit-uvlf": lit_uvlf,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list or not a.slug:
        print("plottable from recorded artifacts today:")
        for k in PLOTS:
            print(f"  {k}")
        return 0
    fn = PLOTS.get(a.slug)
    if not fn:
        print(f"no recorded-data plot defined for {a.slug} — not inventing one")
        return 2
    return 0 if fn() else 3


if __name__ == "__main__":
    raise SystemExit(main())
