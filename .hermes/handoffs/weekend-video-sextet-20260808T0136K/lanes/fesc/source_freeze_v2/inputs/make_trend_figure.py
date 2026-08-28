#!/usr/bin/env python3
"""Lane script — fesc-zsweep-merged-paper-20260804T1040K (Lana).

Computes the merged-paper trend quantities from the pipeline's own model and
verifies every number against the 9 trend-grid run JSONs (z=6.0..10.0, dz=0.5):

  * shortfall fraction vs z and Delta(required-inferred) vs z with 16-84% band
  * the closure-crossing z_c where the 16-84% interval of Delta stops spanning
    zero (i.e. the 16th percentile of Delta crosses 0), root-found on a fine
    z-grid with the pipeline's exact seed/constants, + bootstrap uncertainty
  * the median-crossing z_m (where Delta's median crosses 0)
  * the boost_mode="none" systematic corner (Kun F1c): same sweep without the
    JWST-SFRD tail, incl. whether the z=9 shortfall survives
  * per-z O32-only / beta-only medians (non-circularity test, matching runs)

Writes TREND_RESULTS.json and the central figure (PNG + PDF) into the lane dir.
No network, no writes outside the lane. The tool module is imported read-only.
"""
import json
import os
import sys

import numpy as np

LANE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/duhokim/NebulaMind/NebulaMind"
sys.path.insert(0, os.path.join(REPO, "tools"))
import nm_ionizing_budget as nb  # noqa: E402  (read-only import of the pipeline model)

SEED = 20260723
N = 40000
XI_C, XI_SIG = 25.5, 0.15
C_LO, C_HI = 2.0, 5.0
GRID_Z = [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]


def draw_streams(boost_mode="jwst"):
    """Reproduce run_ionizing_budget()'s rng stream order exactly."""
    rng = np.random.default_rng(SEED)
    log_xi = rng.normal(XI_C, XI_SIG, N)
    C = rng.uniform(C_LO, C_HI, N)
    if boost_mode == "none":
        boost = 10 ** rng.normal(0.0, 0.2, N)
    else:  # "jwst" fiducial: lognormal x (1 + U(0,1.5) on half the draws)
        boost = 10 ** rng.normal(0.0, 0.2, N) * (
            1.0 + rng.uniform(0.0, 1.5, N) * (rng.random(N) < 0.5)
        )
    use_o32 = rng.random(N) < 0.5
    inf_o32 = nb._sample_proxy(rng, "O32", N)
    inf_beta = nb._sample_proxy(rng, "beta", N)
    f_inf = np.where(use_o32, inf_o32, inf_beta)
    # the tool draws FRESH proxy samples for the non-circularity medians
    nc_o32 = nb._sample_proxy(rng, "O32", N)
    nc_beta = nb._sample_proxy(rng, "beta", N)
    return log_xi, C, boost, f_inf, nc_o32, nc_beta


def a_of_z(z):
    """f_required(z) = K_draw * A(z) with A(z) = (1+z)^3 / SFRD(z)."""
    return (1.0 + z) ** 3 / nb.sfrd_md14(z)


def make_K(log_xi, C, boost):
    """Per-draw z-independent factor, anchored at z=8 (pre-clip)."""
    z_ref = 8.0
    return nb.fesc_required(z_ref, log_xi, C, boost) / a_of_z(z_ref)


def stats_at_z(z, K, f_inf):
    f_req = np.clip(K * a_of_z(z), 1e-4, 5.0)
    delta = f_req - f_inf
    q = lambda a, p: float(np.percentile(a, p))
    return {
        "f_required": [q(f_req, 16), q(f_req, 50), q(f_req, 84)],
        "f_inferred": [q(f_inf, 16), q(f_inf, 50), q(f_inf, 84)],
        "delta": [q(delta, 16), q(delta, 50), q(delta, 84)],
        "frac_shortfall": float(np.mean(delta > 0)),
    }


def bisect(fn, lo, hi, tol=1e-4):
    flo, fhi = fn(lo), fn(hi)
    if flo * fhi > 0:
        return None
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if flo * fn(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def crossing(K, f_inf, pctl, zlo=5.0, zhi=10.5):
    fn = lambda z: np.percentile(np.clip(K * a_of_z(z), 1e-4, 5.0) - f_inf, pctl)
    return bisect(fn, zlo, zhi)


def bootstrap_crossing(K, f_inf, pctl, nboot=200):
    rng = np.random.default_rng(SEED + 1)  # lane-local resampling stream
    zs = []
    for _ in range(nboot):
        idx = rng.integers(0, N, N)
        zc = crossing(K[idx], f_inf[idx], pctl)
        if zc is not None:
            zs.append(zc)
    zs = np.array(zs)
    return [float(np.percentile(zs, p)) for p in (16, 50, 84)]


def main():
    # ---------- fiducial (jwst boost, "both" proxy) — the pipeline's corner ----------
    log_xi, C, boost, f_inf, nc_o32, nc_beta = draw_streams("jwst")
    K = make_K(log_xi, C, boost)

    # sanity: K*A(z) reproduces the tool's direct evaluation
    for z in (6.0, 8.0, 10.0):
        direct = np.clip(nb.fesc_required(z, log_xi, C, boost), 1e-4, 5.0)
        assert np.allclose(np.clip(K * a_of_z(z), 1e-4, 5.0), direct), z

    # verify against the 9 trend-grid run JSONs
    trend = json.load(open(os.path.join(LANE, "TREND_DATA.json")))
    rows, max_dev = [], 0.0
    for row in trend["rows"]:
        z = float(row["z0"])
        mine = stats_at_z(z, K, f_inf)
        f_req_z = np.clip(K * a_of_z(z), 1e-4, 5.0)
        d_o32 = float(np.median(f_req_z - nc_o32))
        d_beta = float(np.median(f_req_z - nc_beta))
        theirs = row["fesc"]
        dev = max(
            np.max(np.abs(np.array(mine["f_required"]) - theirs["f_required"])),
            np.max(np.abs(np.array(mine["f_inferred"]) - theirs["f_inferred"])),
            np.max(np.abs(np.array(mine["delta"]) - theirs["delta"])),
            abs(mine["frac_shortfall"] - theirs["frac_shortfall"]),
            abs(d_o32 - theirs["delta_O32"]),
            abs(d_beta - theirs["delta_beta"]),
        )
        max_dev = max(max_dev, dev)
        robust = (np.sign(d_o32) == np.sign(d_beta)) and (
            np.sign(mine["delta"][1]) == np.sign(d_o32)
        )
        rows.append({
            "z": z, "run": row["run"], **mine,
            "delta_O32": d_o32, "delta_beta": d_beta,
            "noncircular_robust": bool(robust),
            "matches_run_json": bool(dev < 1e-9),
        })
    print(f"verification vs 9 run JSONs: max abs deviation = {max_dev:.3e}")
    assert max_dev < 1e-6, "lane MC does not reproduce the run JSONs"

    # closure crossing (16th pctl of Delta = 0) + median crossing, fiducial
    zc16 = crossing(K, f_inf, 16)
    zc16_boot = bootstrap_crossing(K, f_inf, 16)
    zm50 = crossing(K, f_inf, 50)
    zm50_boot = bootstrap_crossing(K, f_inf, 50)
    at_zc = stats_at_z(zc16, K, f_inf)

    # ---------- boost_mode="none" corner (Kun F1c) ----------
    log_xi_n, C_n, boost_n, f_inf_n, nc_o32_n, nc_beta_n = draw_streams("none")
    K_n = make_K(log_xi_n, C_n, boost_n)
    none_rows = []
    for z in GRID_Z:
        s = stats_at_z(z, K_n, f_inf_n)
        f_req_z = np.clip(K_n * a_of_z(z), 1e-4, 5.0)
        s["delta_O32"] = float(np.median(f_req_z - nc_o32_n))
        s["delta_beta"] = float(np.median(f_req_z - nc_beta_n))
        none_rows.append({"z": z, **s})
    zc16_none = crossing(K_n, f_inf_n, 16)
    zc16_none_boot = bootstrap_crossing(K_n, f_inf_n, 16)
    z9_none = stats_at_z(9.0, K_n, f_inf_n)
    # median required-f_esc ratio none/fiducial (the boost prior's pull)
    boost_ratio = float(np.median(K_n * a_of_z(9.0)) / np.median(K * a_of_z(9.0)))

    results = {
        "lane": "fesc-zsweep-merged-paper-20260804T1040K",
        "script": "make_trend_figure.py",
        "model": "tools/nm_ionizing_budget.py (imported read-only), seed 20260723, N=40000",
        "verification": {"n_runs_checked": len(rows), "max_abs_deviation": max_dev,
                          "all_match": bool(max_dev < 1e-9)},
        "grid_fiducial": rows,
        "closure_crossing_fiducial": {
            "definition": "z_c where the 16th percentile of Delta(required-inferred) "
                          "crosses 0, i.e. the 16-84% interval stops spanning zero",
            "z_c": zc16, "bootstrap_16_50_84": zc16_boot,
            "stats_at_z_c": at_zc,
        },
        "median_crossing_fiducial": {
            "definition": "z_m where the median of Delta crosses 0",
            "z_m": zm50, "bootstrap_16_50_84": zm50_boot,
        },
        "corner_boost_none": {
            "definition": "sfrd_boost_mode='none' (no JWST-SFRD tail), Kun F1c",
            "grid": none_rows,
            "z9": z9_none,
            "z9_shortfall_survives": bool(z9_none["delta"][0] > 0),
            "closure_crossing_z_c": zc16_none,
            "bootstrap_16_50_84": zc16_none_boot,
            "median_f_required_ratio_none_over_fiducial_z9": boost_ratio,
        },
        "constants": {
            "log_xi_ion": [XI_C, XI_SIG], "clumping_C_uniform": [C_LO, C_HI],
            "proxy_anchors_median_sigmadex": dict(nb._PROXY),
            "sfrd": "Madau & Dickinson (2014) analytic fit",
            "boost_fiducial": "10**N(0,0.2dex) * (1 + U(0,1.5) on half the draws)",
            "boost_none": "10**N(0,0.2dex)",
            "kappa_UV": nb._KAPPA_UV, "alpha_B": nb._ALPHA_B,
        },
    }
    with open(os.path.join(LANE, "TREND_RESULTS.json"), "w") as f:
        json.dump(results, f, indent=1)
    print("wrote TREND_RESULTS.json")
    print(f"  closure crossing z_c = {zc16:.3f}  (boot 16-84: {zc16_boot[0]:.3f}-{zc16_boot[2]:.3f})")
    print(f"  median crossing  z_m = {zm50:.3f}  (boot 16-84: {zm50_boot[0]:.3f}-{zm50_boot[2]:.3f})")
    print(f"  boost=none: z_c = {zc16_none}  z=9 delta16 = {z9_none['delta'][0]:+.3f}  "
          f"shortfall survives: {z9_none['delta'][0] > 0}")

    # ---------- central figure ----------
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    RED, BLUE, INK, MUT = "#b3392e", "#2f6fa8", "#26241f", "#6f6b61"
    plt.rcParams.update({
        "font.size": 8, "axes.edgecolor": MUT, "axes.labelcolor": INK,
        "xtick.color": MUT, "ytick.color": MUT, "axes.linewidth": 0.8,
        "font.family": "serif", "mathtext.fontset": "dejavuserif",
    })
    zz = np.linspace(6.0, 10.0, 401)
    req = np.array([np.percentile(np.clip(K * a_of_z(z), 1e-4, 5.0), (16, 50, 84)) for z in zz])
    dl = np.array([np.percentile(np.clip(K * a_of_z(z), 1e-4, 5.0) - f_inf, (16, 50, 84)) for z in zz])
    dl_none16 = np.array([np.percentile(np.clip(K_n * a_of_z(z), 1e-4, 5.0) - f_inf_n, 16) for z in zz])
    inf16, inf50, inf84 = np.percentile(f_inf, (16, 50, 84))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.5, 5.0), sharex=True,
                                   gridspec_kw={"hspace": 0.08})
    # (a) required vs inferred
    ax1.fill_between(zz, req[:, 0], req[:, 2], color=RED, alpha=0.18, lw=0)
    ax1.plot(zz, req[:, 1], color=RED, lw=1.8)
    gz = np.array(GRID_Z)
    ax1.plot(gz, [r["f_required"][1] for r in rows], "o", color=RED, ms=3.5,
             mec="white", mew=0.6)
    ax1.axhspan(inf16, inf84, color=BLUE, alpha=0.15, lw=0)
    ax1.axhline(inf50, color=BLUE, lw=1.6, ls="--")
    ax1.text(6.1, 0.52, "required $f_{\\rm esc}$\n($\\xi_{\\rm ion}\\times C\\times$SFRD syst.)",
             color=RED, fontsize=7.5)
    ax1.text(6.1, 0.21, "proxy-inferred (LzLCS O32/$\\beta$,\n$z$-independent by construction)",
             color=BLUE, fontsize=7.5)
    ax1.set_ylabel("LyC escape fraction $f_{\\rm esc}$")
    ax1.set_ylim(0, 1.45)
    ax1.set_yticks([0, 0.25, 0.5, 0.75, 1.0, 1.25])
    ax1.grid(axis="y", color=MUT, alpha=0.15, lw=0.6)
    # (b) delta with band, crossing, boost-none corner
    ax2.fill_between(zz, dl[:, 0], dl[:, 2], color=RED, alpha=0.18, lw=0)
    ax2.plot(zz, dl[:, 1], color=RED, lw=1.8, label="$\\Delta$ median (fiducial)")
    ax2.plot(zz, dl[:, 0], color=RED, lw=0.9, alpha=0.7)
    ax2.plot(zz, dl_none16, color=INK, lw=1.1, ls=":",
             label="16th pctl, no JWST-SFRD tail")
    ax2.axhline(0, color=MUT, lw=0.9)
    ax2.axvline(zc16, color=INK, lw=0.9, ls="--")
    ax2.annotate(f"$z_c={zc16:.2f}$\n(16–84% interval\nleaves zero)",
                 xy=(zc16, 0.0), xytext=(zc16 - 1.55, 0.42), fontsize=7.5, color=INK,
                 arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    for zi, r in zip(gz, rows):
        if zi in (7.0, 8.0, 9.0):
            ax2.annotate(f"{r['frac_shortfall']*100:.0f}%", ha="right",
                         xy=(zi, r["delta"][1]), xytext=(zi - 0.08, r["delta"][1] + 0.09),
                         fontsize=7, color=MUT)
    ax2.plot(gz, [r["delta"][1] for r in rows], "o", color=RED, ms=3.5,
             mec="white", mew=0.6)
    ax2.set_xlabel("redshift $z$")
    # thin space before the superscripts: the italic f otherwise abuts "req"
    # and reads as the word "freq" at print size (Kun R4)
    ax2.set_ylabel("$\\Delta = f_{\\rm esc}^{\\,\\rm req} - f_{\\rm esc}^{\\,\\rm inf}$")
    ax2.set_xlim(6.0, 10.0)
    ax2.set_ylim(-0.25, 1.35)
    ax2.grid(axis="y", color=MUT, alpha=0.15, lw=0.6)
    ax2.legend(fontsize=6.8, loc="upper left", frameon=False)
    fig.align_ylabels()
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(LANE, f"fesc_zsweep_trend.{ext}"),
                    dpi=300, bbox_inches="tight")
    print("wrote fesc_zsweep_trend.png / .pdf")


if __name__ == "__main__":
    main()
