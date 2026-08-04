#!/usr/bin/env python3
"""
SDSS DR17 AGN/star-formation pilot analysis for NebulaMind RT autopilot.

This is a bounded, reproducible pilot study mapped to the research proposal
"Observational constraints on the suppression of star formation by AGN feedback".
It uses public SDSS DR17 spectroscopy/photometry and MPA/JHU-style derived
quantities exposed through SkyServer/astroquery.

Safety: read-only public SDSS query + local artifact writes only.
"""
from __future__ import annotations

import json
import math
import textwrap
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

try:
    from astroquery.sdss import SDSS
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"astroquery.sdss is required: {exc}")

RUN_ID = "SDSS_AGN_SFR_PILOT_20260708T122000Z"
REVISION_MARKER = "AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z"

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs") / RUN_ID
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
TEX_DIR = ROOT / "aastex"
for d in (DATA_DIR, FIG_DIR, TEX_DIR):
    d.mkdir(parents=True, exist_ok=True)

RAW_CSV = DATA_DIR / "sdss_dr17_emission_line_sample.csv"
ANALYSIS_CSV = DATA_DIR / "analysis_sample_bpt.csv"
MATCHED_CSV = DATA_DIR / "matched_agn_sf_pairs.csv"
RESULTS_JSON = ROOT / "analysis_results.json"
METHODS_MD = ROOT / "METHODS_AND_SCOPE.md"

SQL = r"""
SELECT TOP 60000
 s.specObjID,
 s.z,
 i.ra,
 i.dec,
 x.bptclass,
 x.lgm_tot_p50,
 x.sfr_tot_p50,
 x.specsfr_tot_p50,
 p.modelMag_u,
 p.modelMag_g,
 p.modelMag_r,
 l.h_alpha_flux,
 l.h_alpha_flux_err,
 l.h_beta_flux,
 l.h_beta_flux_err,
 l.oiii_5007_flux,
 l.oiii_5007_flux_err,
 l.nii_6584_flux,
 l.nii_6584_flux_err
FROM SpecObj AS s
JOIN galSpecInfo AS i ON s.specObjID=i.specObjID
JOIN PhotoObj AS p ON s.bestObjID=p.objID
JOIN galSpecLine AS l ON s.specObjID=l.specObjID
JOIN galSpecExtra AS x ON s.specObjID=x.specObjID
WHERE s.class='GALAXY'
AND s.z BETWEEN 0.02 AND 0.12
AND l.h_alpha_flux > 0 AND l.h_beta_flux > 0 AND l.oiii_5007_flux > 0 AND l.nii_6584_flux > 0
AND l.h_alpha_flux_err > 0 AND l.h_beta_flux_err > 0 AND l.oiii_5007_flux_err > 0 AND l.nii_6584_flux_err > 0
AND l.h_alpha_flux / l.h_alpha_flux_err >= 3
AND l.h_beta_flux / l.h_beta_flux_err >= 3
AND l.oiii_5007_flux / l.oiii_5007_flux_err >= 3
AND l.nii_6584_flux / l.nii_6584_flux_err >= 3
AND x.lgm_tot_p50 BETWEEN 8.0 AND 12.5
AND x.specsfr_tot_p50 BETWEEN -14.0 AND -7.0
ORDER BY s.specObjID
"""


def table_to_frame(tbl) -> pd.DataFrame:
    df = tbl.to_pandas()
    # Astroquery can return object dtypes; force numeric except IDs if possible.
    for c in df.columns:
        if c != "specObjID":
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def fetch_or_load() -> pd.DataFrame:
    if RAW_CSV.exists():
        return pd.read_csv(RAW_CSV)
    tbl = SDSS.query_sql(SQL, data_release=17, timeout=240)
    if tbl is None or len(tbl) == 0:
        raise SystemExit("SDSS query returned no rows")
    df = table_to_frame(tbl)
    df.to_csv(RAW_CSV, index=False)
    (DATA_DIR / "query.sql").write_text(SQL.strip() + "\n")
    return df


def bpt_classify(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["sn_ha"] = out.h_alpha_flux / out.h_alpha_flux_err
    out["sn_hb"] = out.h_beta_flux / out.h_beta_flux_err
    out["sn_oiii"] = out.oiii_5007_flux / out.oiii_5007_flux_err
    out["sn_nii"] = out.nii_6584_flux / out.nii_6584_flux_err
    out["log_nii_ha"] = np.log10(out.nii_6584_flux / out.h_alpha_flux)
    out["log_oiii_hb"] = np.log10(out.oiii_5007_flux / out.h_beta_flux)
    out["u_minus_r"] = out.modelMag_u - out.modelMag_r
    out["g_minus_r"] = out.modelMag_g - out.modelMag_r

    # Standard optical BPT demarcations.
    x = out["log_nii_ha"].to_numpy()
    y = out["log_oiii_hb"].to_numpy()
    kauffmann = 0.61 / (x - 0.05) + 1.30
    kewley = 0.61 / (x - 0.47) + 1.19
    label = np.full(len(out), "intermediate", dtype=object)
    label[y < kauffmann] = "star-forming"
    label[y > kewley] = "agn"
    # Remove pathological ratio range where the demarcation curves diverge.
    label[(x > 0.35) | ~np.isfinite(x) | ~np.isfinite(y)] = "unclassified"
    out["bpt_label"] = label
    keep = out.replace([np.inf, -np.inf], np.nan).dropna(
        subset=["z", "lgm_tot_p50", "specsfr_tot_p50", "log_nii_ha", "log_oiii_hb", "u_minus_r"]
    )
    keep.to_csv(ANALYSIS_CSV, index=False)
    return keep


def bootstrap_ci(values: np.ndarray, func=np.median, n_boot: int = 5000, rng_seed: int = 42):
    rng = np.random.default_rng(rng_seed)
    values = np.asarray(values)
    if len(values) == 0:
        return [None, None]
    draws = np.empty(n_boot)
    for i in range(n_boot):
        sample = values[rng.integers(0, len(values), len(values))]
        draws[i] = func(sample)
    return [float(np.percentile(draws, 2.5)), float(np.percentile(draws, 97.5))]


def match_agn_to_controls(df: pd.DataFrame):
    agn = df[df.bpt_label == "agn"].copy()
    sf = df[df.bpt_label == "star-forming"].copy()
    if len(agn) < 10 or len(sf) < 10:
        raise SystemExit(f"Insufficient classes after BPT cuts: agn={len(agn)} sf={len(sf)}")
    features = ["lgm_tot_p50", "z"]
    scale = sf[features].std().replace(0, 1)
    sf_scaled = (sf[features] - sf[features].mean()) / scale
    agn_scaled = (agn[features] - sf[features].mean()) / scale
    tree = cKDTree(sf_scaled.to_numpy())
    dist, idx = tree.query(agn_scaled.to_numpy(), k=1)
    ctrl = sf.iloc[idx].reset_index(drop=True)
    agn2 = agn.reset_index(drop=True)
    pairs = pd.DataFrame(
        {
            "agn_specObjID": agn2.specObjID.astype(str),
            "control_specObjID": ctrl.specObjID.astype(str),
            "agn_z": agn2.z,
            "control_z": ctrl.z,
            "agn_logM": agn2.lgm_tot_p50,
            "control_logM": ctrl.lgm_tot_p50,
            "agn_log_sSFR": agn2.specsfr_tot_p50,
            "control_log_sSFR": ctrl.specsfr_tot_p50,
            "delta_log_sSFR_agn_minus_control": agn2.specsfr_tot_p50.to_numpy() - ctrl.specsfr_tot_p50.to_numpy(),
            "match_distance_scaled": dist,
        }
    )
    pairs.to_csv(MATCHED_CSV, index=False)
    return agn, sf, pairs


def ols_coefficient(df: pd.DataFrame):
    two = df[df.bpt_label.isin(["agn", "star-forming"])].copy()
    two["is_agn"] = (two.bpt_label == "agn").astype(float)
    y = two.specsfr_tot_p50.to_numpy(dtype=float)
    X = np.column_stack([
        np.ones(len(two)),
        two.is_agn.to_numpy(dtype=float),
        two.lgm_tot_p50.to_numpy(dtype=float),
        two.z.to_numpy(dtype=float),
    ])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = len(y) - X.shape[1]
    sigma2 = float((resid @ resid) / dof)
    cov = sigma2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    return {
        "n_regression": int(len(two)),
        "coef_is_agn_log_sSFR_dex": float(beta[1]),
        "coef_is_agn_se": float(se[1]),
        "coef_is_agn_ci95": [float(beta[1] - 1.96 * se[1]), float(beta[1] + 1.96 * se[1])],
        "coef_logM": float(beta[2]),
        "coef_z": float(beta[3]),
    }


def make_figures(df: pd.DataFrame, pairs: pd.DataFrame):
    # Figure 1: BPT diagram.
    fig, ax = plt.subplots(figsize=(6.2, 5.1))
    colors = {"star-forming": "#2878b5", "intermediate": "#8c8c8c", "agn": "#c82423"}
    for lab in ["star-forming", "intermediate", "agn"]:
        sub = df[df.bpt_label == lab]
        if len(sub) == 0:
            continue
        plot_sub = sub.sample(min(len(sub), 7000), random_state=3) if len(sub) > 7000 else sub
        ax.scatter(plot_sub.log_nii_ha, plot_sub.log_oiii_hb, s=3, alpha=0.18, label=f"{lab} (n={len(sub)})", color=colors[lab], rasterized=True)
    xs1 = np.linspace(-1.5, 0.03, 300)
    xs2 = np.linspace(-1.5, 0.35, 300)
    ax.plot(xs1, 0.61 / (xs1 - 0.05) + 1.30, color="black", lw=1.2, ls="--", label="Kauffmann+03")
    ax.plot(xs2, 0.61 / (xs2 - 0.47) + 1.19, color="black", lw=1.2, ls=":", label="Kewley+01")
    ax.set_xlim(-1.45, 0.45)
    ax.set_ylim(-1.25, 1.55)
    ax.set_xlabel(r"$\log([\mathrm{N\,II}]\lambda6584/\mathrm{H}\alpha)$")
    ax.set_ylabel(r"$\log([\mathrm{O\,III}]\lambda5007/\mathrm{H}\beta)$")
    ax.legend(fontsize=7, loc="lower left", frameon=False)
    ax.set_title("SDSS DR17 pilot BPT classification")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "figure1_bpt.pdf")
    fig.savefig(FIG_DIR / "figure1_bpt.png", dpi=220)
    plt.close(fig)

    # Figure 2: matched pair offsets and sSFR-mass plane.
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.4))
    ax = axes[0]
    bins = np.linspace(-4, 2, 45)
    ax.hist(pairs.delta_log_sSFR_agn_minus_control, bins=bins, color="#6c5ce7", alpha=0.78)
    med = np.median(pairs.delta_log_sSFR_agn_minus_control)
    ax.axvline(med, color="black", lw=1.5, label=f"median={med:.2f} dex")
    ax.axvline(0, color="0.4", lw=1, ls="--")
    ax.set_xlabel(r"$\Delta \log\,\mathrm{sSFR}$ (AGN $-$ matched SF control)")
    ax.set_ylabel("Matched AGN hosts")
    ax.legend(frameon=False, fontsize=8)

    ax = axes[1]
    for lab, color in [("star-forming", "#2878b5"), ("agn", "#c82423")]:
        sub = df[df.bpt_label == lab]
        plot_sub = sub.sample(min(len(sub), 5000), random_state=9) if len(sub) > 5000 else sub
        ax.scatter(plot_sub.lgm_tot_p50, plot_sub.specsfr_tot_p50, s=4, alpha=0.18, color=color, label=f"{lab} (n={len(sub)})", rasterized=True)
    ax.set_xlabel(r"$\log(M_\star/M_\odot)$")
    ax.set_ylabel(r"$\log(\mathrm{sSFR}/\mathrm{yr}^{-1})$")
    ax.set_ylim(-13.8, -7.3)
    ax.legend(frameon=False, fontsize=8)
    ax.set_title("Specific SFR versus stellar mass proxy")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "figure2_matched_offsets.pdf")
    fig.savefig(FIG_DIR / "figure2_matched_offsets.png", dpi=220)
    plt.close(fig)


def summarize(df: pd.DataFrame, pairs: pd.DataFrame):
    counts = df.bpt_label.value_counts().to_dict()
    groups = {}
    for lab in ["star-forming", "intermediate", "agn", "unclassified"]:
        sub = df[df.bpt_label == lab]
        if len(sub):
            groups[lab] = {
                "n": int(len(sub)),
                "median_z": float(sub.z.median()),
                "median_logM": float(sub.lgm_tot_p50.median()),
                "median_log_sSFR": float(sub.specsfr_tot_p50.median()),
                "median_u_minus_r": float(sub.u_minus_r.median()),
            }
    delta = pairs.delta_log_sSFR_agn_minus_control.to_numpy()
    results = {
        "run_id": RUN_ID,
        "revision_marker": REVISION_MARKER,
        "data_release": "SDSS DR17 SkyServer via astroquery.sdss",
        "query_top_n": 60000,
        "raw_rows": int(len(pd.read_csv(RAW_CSV))),
        "analysis_rows": int(len(df)),
        "bpt_counts": {str(k): int(v) for k, v in counts.items()},
        "group_medians": groups,
        "matched_pairs": int(len(pairs)),
        "matched_delta_log_sSFR_median_dex": float(np.median(delta)),
        "matched_delta_log_sSFR_mean_dex": float(np.mean(delta)),
        "matched_delta_log_sSFR_median_ci95_bootstrap": bootstrap_ci(delta, np.median),
        "matched_delta_log_sSFR_mean_ci95_bootstrap": bootstrap_ci(delta, np.mean),
        "match_distance_scaled_median": float(np.median(pairs.match_distance_scaled)),
        "match_abs_delta_logM_median": float(np.median(np.abs(pairs.agn_logM - pairs.control_logM))),
        "match_abs_delta_z_median": float(np.median(np.abs(pairs.agn_z - pairs.control_z))),
        "ols_adjusted_for_logM_z": ols_coefficient(df),
        "files": {
            "raw_csv": str(RAW_CSV),
            "analysis_csv": str(ANALYSIS_CSV),
            "matched_pairs_csv": str(MATCHED_CSV),
            "figure1_pdf": str(FIG_DIR / "figure1_bpt.pdf"),
            "figure2_pdf": str(FIG_DIR / "figure2_matched_offsets.pdf"),
        },
        "safety": "read-only public SDSS query; local artifact writes only; no DB/API/page_versions/live wiki publish/deploy/git/cron",
    }
    RESULTS_JSON.write_text(json.dumps(results, indent=2))
    return results


def write_methods(results):
    METHODS_MD.write_text(textwrap.dedent(f"""
    # SDSS AGN/sSFR pilot methods and scope

    Marker: `{RUN_ID}`

    This run is a bounded pilot execution of the AGN-feedback research proposal. It uses public SDSS DR17 spectroscopy and derived quantities to test whether optically selected BPT AGN hosts show a specific-SFR offset relative to nearest star-forming controls matched in stellar mass proxy and redshift.

    Data source: SDSS DR17 SkyServer queried through `astroquery.sdss`.

    Main cuts:
    - spectroscopic class `GALAXY`
    - redshift 0.02--0.12
    - positive Halpha, Hbeta, [O III] 5007, [N II] 6584 line fluxes
    - S/N >= 3 in all four BPT lines
    - `lgm_tot_p50` between 8.0 and 12.5
    - `specsfr_tot_p50` between -14 and -7

    Classification: BPT line-ratio cuts using Kauffmann et al. (2003) and Kewley et al. (2001) demarcations. AGN includes the high-excitation optical AGN/LINER side as a single pilot class.

    Matched-control test: every BPT AGN host is paired to the nearest BPT star-forming galaxy in standardized `(logM, z)` space, with replacement. The primary statistic is the median difference `log sSFR_AGN - log sSFR_control`.

    Key result from this run:
    - analysis rows: {results['analysis_rows']}
    - BPT AGN rows: {results['bpt_counts'].get('agn', 0)}
    - BPT star-forming rows: {results['bpt_counts'].get('star-forming', 0)}
    - matched pairs: {results['matched_pairs']}
    - median matched delta log sSFR: {results['matched_delta_log_sSFR_median_dex']:.3f} dex
    - 95% bootstrap CI for median delta: {results['matched_delta_log_sSFR_median_ci95_bootstrap'][0]:.3f}, {results['matched_delta_log_sSFR_median_ci95_bootstrap'][1]:.3f} dex

    Scope guard: this pilot measures an optical-classification-associated sSFR offset. It does not establish causal AGN feedback, duty-cycle timing, molecular-gas depletion, or halo-scale energy coupling.

    {RUN_ID}
    """).strip() + "\n")


def main():
    raw = fetch_or_load()
    df = bpt_classify(raw)
    agn, sf, pairs = match_agn_to_controls(df)
    make_figures(df, pairs)
    results = summarize(df, pairs)
    write_methods(results)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
