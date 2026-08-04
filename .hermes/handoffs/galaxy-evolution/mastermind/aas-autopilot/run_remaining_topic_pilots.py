#!/usr/bin/env python3
"""Generate actual-data AAS-style pilot PDFs for remaining Galaxy Evolution topics.

The script reuses the public/read-only SDSS DR17 sample acquired by the first
AGN/sSFR pilot and writes local artifacts only.  Several proposals require data
not present in SDSS alone (radio jets, X-ray cavities, CO gas, multiphase
outflow velocities).  For those, this script produces an explicitly bounded
SDSS denominator/proxy pilot rather than claiming to solve the full proposal.
"""
from __future__ import annotations

import json
import math
import re
import shutil
import subprocess
import textwrap
from dataclasses import dataclass
from pathlib import Path
from string import Template

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

RUN_ID = "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
SOURCE_RUN = AUTOPILOT / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
SOURCE_CSV = SOURCE_RUN / "data/analysis_sample_bpt.csv"
OUT_ROOT = AUTOPILOT / "runs" / RUN_ID

C_KM_S = 299792.458
H0 = 70.0
PDF_EXPECTED_NOTE = "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."

@dataclass
class PilotSpec:
    slug: str
    method: str
    card_id: str
    title: str
    short_title: str
    question: str
    full_proposal_requires: str

SPECS = [
    PilotSpec(
        slug="m1_rp2_environment_quenching",
        method="packet-gated-paper-to-wiki-reconciliation",
        card_id="rp-2",
        title="Separating internal and environmental quenching across stellar mass, halo mass, and redshift",
        short_title="SDSS density proxy for environmental quenching",
        question="Does a nearest-neighbour density proxy add quenched-fraction information beyond stellar mass in the SDSS emission-line sample?",
        full_proposal_requires="group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions.",
    ),
    PilotSpec(
        slug="m1_rp3_maintenance_heating",
        method="packet-gated-paper-to-wiki-reconciliation",
        card_id="rp-3",
        title="Empirical duty-cycle constraints on AGN maintenance heating in massive halos",
        short_title="Optical-AGN denominator for maintenance-heating follow-up",
        question="Among massive, low-sSFR SDSS emission-line galaxies, what optical AGN fraction is available as a denominator for X-ray/radio maintenance-heating follow-up?",
        full_proposal_requires="X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.",
    ),
    PilotSpec(
        slug="m2_p1_outflow_escape_recycling",
        method="source-first-paper-adjudication",
        card_id="p1",
        title="Escape versus recycling: the fate of AGN-driven multiphase outflows",
        short_title="SDSS high-excitation AGN denominator for outflow escape tests",
        question="How large is the SDSS high-excitation optical-AGN denominator that would need resolved kinematics to test escape versus recycling?",
        full_proposal_requires="resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.",
    ),
    PilotSpec(
        slug="m2_p2_radio_jet_environment",
        method="source-first-paper-adjudication",
        card_id="p2",
        title="Environmental dependence of radio-jet coupling efficiency in galaxy gas",
        short_title="Environment proxy for optical AGN in massive SDSS hosts",
        question="Does a local-density proxy modulate the optical AGN fraction in massive SDSS hosts, motivating environment-stratified radio/X-ray jet-coupling follow-up?",
        full_proposal_requires="radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.",
    ),
    PilotSpec(
        slug="m2_p3_feedback_transition_mass",
        method="source-first-paper-adjudication",
        card_id="p3",
        title="Locating the transition from stellar-feedback to AGN-feedback regulation",
        short_title="SDSS mass transition in quenching and optical AGN incidence",
        question="At what stellar-mass scale do quenched fraction and optical AGN incidence rise in the same SDSS denominator?",
        full_proposal_requires="gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.",
    ),
    PilotSpec(
        slug="m3_p1_multiphase_census",
        method="debate-map-to-wiki-rebuild",
        card_id="p1",
        title="A multiphase, common-denominator census of AGN-driven outflows",
        short_title="Common-denominator optical tracer census in SDSS",
        question="How strongly do simple optical tracer definitions change the inferred AGN/feedback-candidate prevalence in one common SDSS denominator?",
        full_proposal_requires="ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.",
    ),
    PilotSpec(
        slug="m3_p2_gas_depletion_efficiency",
        method="debate-map-to-wiki-rebuild",
        card_id="p2",
        title="Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies",
        short_title="Optical denominator for gas-fraction versus efficiency tests",
        question="How many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction/depletion-time follow-up?",
        full_proposal_requires="CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.",
    ),
    PilotSpec(
        slug="m3_p3_simulation_validation",
        method="debate-map-to-wiki-rebuild",
        card_id="p3",
        title="Forward-modelled validation of cosmological feedback prescriptions",
        short_title="SDSS target vector for feedback-model validation",
        question="What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation?",
        full_proposal_requires="simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.",
    ),
]


def tex_escape(s: str) -> str:
    return (
        str(s)
        .replace("\\", r"\textbackslash{}")
        .replace("&", r"\&")
        .replace("%", r"\%")
        .replace("$", r"\$")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("{", r"\{")
        .replace("}", r"\}")
        .replace("~", r"\textasciitilde{}")
        .replace("^", r"\textasciicircum{}")
    )


def load_sample() -> pd.DataFrame:
    if not SOURCE_CSV.exists():
        raise SystemExit(f"Missing source sample: {SOURCE_CSV}")
    df = pd.read_csv(SOURCE_CSV)
    df = df.replace([np.inf, -np.inf], np.nan).dropna(
        subset=["ra", "dec", "z", "lgm_tot_p50", "specsfr_tot_p50", "u_minus_r", "g_minus_r", "log_nii_ha", "log_oiii_hb", "bpt_label"]
    )
    df["quenched"] = df["specsfr_tot_p50"] < -11.0
    df["red_sequence"] = df["u_minus_r"] > 2.2
    df["massive"] = df["lgm_tot_p50"] >= 10.8
    df["transition_or_quenched"] = df["specsfr_tot_p50"] < -10.7
    df["is_agn"] = df["bpt_label"] == "agn"
    df["is_sf"] = df["bpt_label"] == "star-forming"
    df["high_excitation_agn"] = (df["bpt_label"] == "agn") & (df["log_oiii_hb"] > 0.25)
    df["high_nii"] = df["log_nii_ha"] > -0.20
    df["high_oiii"] = df["log_oiii_hb"] > 0.00
    # Approximate H-alpha luminosity; SDSS line flux units are 1e-17 erg/s/cm^2.
    dl_mpc = (C_KM_S / H0) * df["z"] * (1.0 + df["z"])
    cm_per_mpc = 3.0856775814913673e24
    flux = df["h_alpha_flux"].clip(lower=1e-12) * 1e-17
    lum = 4.0 * math.pi * (dl_mpc * cm_per_mpc) ** 2 * flux
    df["log_lha"] = np.log10(lum)
    add_environment_proxy(df)
    return df


def add_environment_proxy(df: pd.DataFrame) -> None:
    ra = np.deg2rad(df["ra"].to_numpy())
    dec = np.deg2rad(df["dec"].to_numpy())
    # Low-redshift distance proxy is sufficient for ranking local density in this pilot.
    dist = (C_KM_S / H0) * df["z"].to_numpy()
    xyz = np.column_stack([
        dist * np.cos(dec) * np.cos(ra),
        dist * np.cos(dec) * np.sin(ra),
        dist * np.sin(dec),
    ])
    tree = cKDTree(xyz)
    dists, _ = tree.query(xyz, k=11)  # first neighbor is self
    kth = np.maximum(dists[:, -1], 1e-3)
    density = 10.0 / ((4.0 / 3.0) * math.pi * kth**3)
    df["local_density_proxy"] = density
    df["log_density_proxy"] = np.log10(density)
    df["density_quartile"] = pd.qcut(df["log_density_proxy"], 4, labels=["Q1 low", "Q2", "Q3", "Q4 high"], duplicates="drop").astype(str)
    df["high_density"] = df["density_quartile"] == "Q4 high"
    df["low_density"] = df["density_quartile"] == "Q1 low"


def binomial_se(p: float, n: int) -> float:
    return float(math.sqrt(max(p * (1.0 - p), 0.0) / n)) if n else float("nan")


def frac(mask: pd.Series, denom: pd.Series | np.ndarray | None = None):
    if denom is None:
        denom = np.ones(len(mask), dtype=bool)
    vals = mask[denom]
    n = int(len(vals))
    k = int(vals.sum())
    p = k / n if n else float("nan")
    return {"n": n, "k": k, "fraction": float(p), "se": binomial_se(p, n)}


def bootstrap_diff(a: np.ndarray, b: np.ndarray, n_boot: int = 2000, seed: int = 20260708):
    rng = np.random.default_rng(seed)
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    diffs = []
    for _ in range(n_boot):
        aa = a[rng.integers(0, len(a), len(a))]
        bb = b[rng.integers(0, len(b), len(b))]
        diffs.append(np.nanmean(aa) - np.nanmean(bb))
    return [float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))]


def linear_coeff(y: np.ndarray, cols: list[np.ndarray]):
    y = np.asarray(y, dtype=float)
    X = np.column_stack([np.ones(len(y))] + [np.asarray(c, dtype=float) for c in cols])
    beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ beta
    dof = max(len(y) - X.shape[1], 1)
    sigma2 = float(np.sum((y - pred) ** 2) / dof)
    cov = sigma2 * np.linalg.pinv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    return beta, se


def mass_bins(df: pd.DataFrame):
    bins = [8.0, 9.5, 10.0, 10.5, 11.0, 12.5]
    labels = ["8.0-9.5", "9.5-10.0", "10.0-10.5", "10.5-11.0", "11.0-12.5"]
    return pd.cut(df["lgm_tot_p50"], bins=bins, labels=labels, include_lowest=True)


def save_fraction_plot(path: Path, xlabels, series, ylabel, title):
    fig, ax = plt.subplots(figsize=(6.2, 4.1))
    x = np.arange(len(xlabels))
    width = 0.8 / max(len(series), 1)
    for i, (name, vals, errs) in enumerate(series):
        offset = (i - (len(series)-1)/2) * width
        ax.bar(x + offset, vals, width, label=name, yerr=errs, capsize=2)
    ax.set_xticks(x)
    ax.set_xticklabels(xlabels, rotation=25, ha="right")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_ylim(0, min(1.0, max([max(v) if len(v) else 0 for _, v, _ in series] + [0.1]) * 1.35))
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(path.with_suffix(".pdf"))
    fig.savefig(path.with_suffix(".png"), dpi=180)
    plt.close(fig)


def save_scatter_bpt(path: Path, df: pd.DataFrame, highlight: pd.Series, title: str):
    fig, ax = plt.subplots(figsize=(5.6, 4.5))
    sample = df.sample(min(len(df), 12000), random_state=42)
    ax.scatter(sample["log_nii_ha"], sample["log_oiii_hb"], s=2, alpha=0.12, color="#4c78a8", label="SDSS emission-line sample")
    hi = df[highlight]
    hi = hi.sample(min(len(hi), 3000), random_state=7) if len(hi) else hi
    ax.scatter(hi["log_nii_ha"], hi["log_oiii_hb"], s=5, alpha=0.35, color="#e45756", label="highlighted subset")
    ax.set_xlabel(r"log([N II]/H$\alpha$)")
    ax.set_ylabel(r"log([O III]/H$\beta$)")
    ax.set_title(title)
    ax.legend(fontsize=8, loc="best")
    fig.tight_layout()
    fig.savefig(path.with_suffix(".pdf"))
    fig.savefig(path.with_suffix(".png"), dpi=180)
    plt.close(fig)


def compute_topic(spec: PilotSpec, df: pd.DataFrame, fig_dir: Path):
    rows = len(df)
    common = {
        "run_id": RUN_ID,
        "sample_rows": int(rows),
        "source_sample": str(SOURCE_CSV),
        "interpretation_guard": PDF_EXPECTED_NOTE,
    }
    binned = df.copy()
    binned["mass_bin"] = mass_bins(df)
    fig = fig_dir / f"{spec.slug}_figure1"

    if spec.slug == "m1_rp2_environment_quenching":
        low = df[df["low_density"]]
        high = df[df["high_density"]]
        q_low = frac(low["quenched"])
        q_high = frac(high["quenched"])
        ci = bootstrap_diff(high["quenched"].astype(float).to_numpy(), low["quenched"].astype(float).to_numpy())
        labels=[]; low_vals=[]; high_vals=[]; low_err=[]; high_err=[]
        for mb, g in binned.groupby("mass_bin", observed=True):
            gl = g[g["low_density"]]
            gh = g[g["high_density"]]
            if len(gl) > 50 and len(gh) > 50:
                fl=frac(gl["quenched"]); fh=frac(gh["quenched"])
                labels.append(str(mb)); low_vals.append(fl["fraction"]); high_vals.append(fh["fraction"]); low_err.append(fl["se"]); high_err.append(fh["se"])
        save_fraction_plot(fig, labels, [("low density", low_vals, low_err), ("high density", high_vals, high_err)], "quenched fraction", "Quenched fraction by mass and density proxy")
        beta,se=linear_coeff(df["quenched"].astype(float), [df["lgm_tot_p50"], df["z"], df["high_density"].astype(float)])
        bullets=[
            f"The SDSS emission-line denominator contains {rows:,} galaxies with an internally computed 10th-neighbour density proxy.",
            f"The high-density quartile has quenched fraction {q_high['fraction']:.3f} ({q_high['k']:,}/{q_high['n']:,}); the low-density quartile has {q_low['fraction']:.3f} ({q_low['k']:,}/{q_low['n']:,}).",
            f"The bootstrap high-minus-low quenched-fraction interval is [{ci[0]:.3f}, {ci[1]:.3f}].",
            f"A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of {beta[3]:.3f} +/- {se[3]:.3f}.",
        ]
        stats={**common,"high_density_quenched":q_high,"low_density_quenched":q_low,"high_minus_low_ci":ci,"lpm_high_density_coeff":float(beta[3]),"lpm_high_density_se":float(se[3])}
    elif spec.slug == "m1_rp3_maintenance_heating":
        massive = df[df["massive"]]
        massive_q = massive[massive["quenched"]]
        f_all = frac(massive["is_agn"])
        f_q = frac(massive_q["is_agn"])
        labels=[]; vals=[]; errs=[]
        for mb,g in binned.groupby("mass_bin", observed=True):
            if len(g)>100:
                ff=frac(g["is_agn"]); labels.append(str(mb)); vals.append(ff["fraction"]); errs.append(ff["se"])
        save_fraction_plot(fig, labels, [("BPT AGN", vals, errs)], "optical AGN fraction", "Optical AGN denominator by stellar mass")
        bullets=[
            f"The massive subset (logM >= 10.8) contains {len(massive):,} emission-line galaxies; {len(massive_q):,} are low-sSFR by the pilot threshold.",
            f"The optical BPT AGN fraction is {f_all['fraction']:.3f} in the massive subset and {f_q['fraction']:.3f} among massive low-sSFR objects.",
            "This provides an optical duty-cycle denominator for X-ray/radio maintenance-heating follow-up, not a heating-to-cooling measurement.",
        ]
        stats={**common,"massive_rows":int(len(massive)),"massive_quenched_rows":int(len(massive_q)),"massive_agn_fraction":f_all,"massive_quenched_agn_fraction":f_q}
    elif spec.slug == "m2_p1_outflow_escape_recycling":
        f_hi = frac(df["high_excitation_agn"])
        subset = df[df["high_excitation_agn"]]
        save_scatter_bpt(fig, df, df["high_excitation_agn"], "High-excitation optical AGN candidates")
        bullets=[
            f"High-excitation optical AGN candidates number {f_hi['k']:,} of {f_hi['n']:,} emission-line galaxies ({f_hi['fraction']:.3f}).",
            f"Their median log sSFR is {subset['specsfr_tot_p50'].median():.2f}, compared with {df['specsfr_tot_p50'].median():.2f} for the full denominator.",
            "SDSS does not measure escape velocity or multiphase outflow velocities here; the pilot supplies a denominator for resolved follow-up rather than an escape/recycling result.",
        ]
        stats={**common,"high_excitation_agn":f_hi,"median_log_sSFR_high_excitation":float(subset['specsfr_tot_p50'].median()),"median_log_sSFR_all":float(df['specsfr_tot_p50'].median())}
    elif spec.slug == "m2_p2_radio_jet_environment":
        massive = df[df["massive"]]
        low = massive[massive["low_density"]]
        high = massive[massive["high_density"]]
        f_low=frac(low["is_agn"]); f_high=frac(high["is_agn"])
        ci=bootstrap_diff(high["is_agn"].astype(float).to_numpy(), low["is_agn"].astype(float).to_numpy())
        labels=["Q1 low", "Q2", "Q3", "Q4 high"]; vals=[]; errs=[]
        for q in labels:
            g=massive[massive["density_quartile"]==q]
            ff=frac(g["is_agn"]); vals.append(ff["fraction"]); errs.append(ff["se"])
        save_fraction_plot(fig, labels, [("massive BPT AGN", vals, errs)], "AGN fraction", "Massive-host optical AGN fraction by density proxy")
        bullets=[
            f"Among massive hosts, the high-density quartile has optical AGN fraction {f_high['fraction']:.3f}; the low-density quartile has {f_low['fraction']:.3f}.",
            f"The bootstrap high-minus-low interval is [{ci[0]:.3f}, {ci[1]:.3f}].",
            "This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency.",
        ]
        stats={**common,"massive_rows":int(len(massive)),"high_density_massive_agn":f_high,"low_density_massive_agn":f_low,"high_minus_low_ci":ci}
    elif spec.slug == "m2_p3_feedback_transition_mass":
        labels=[]; qvals=[]; qerr=[]; avals=[]; aerr=[]
        peak_bin=None; peak_val=-1
        transition_bin=None
        for mb,g in binned.groupby("mass_bin", observed=True):
            if len(g)>100:
                fq=frac(g["quenched"]); fa=frac(g["is_agn"])
                labels.append(str(mb)); qvals.append(fq["fraction"]); qerr.append(fq["se"]); avals.append(fa["fraction"]); aerr.append(fa["se"])
                if fa["fraction"] > peak_val:
                    peak_val=fa["fraction"]; peak_bin=str(mb)
                if transition_bin is None and fq["fraction"] >= 0.5:
                    transition_bin=str(mb)
        save_fraction_plot(fig, labels, [("quenched", qvals, qerr), ("BPT AGN", avals, aerr)], "fraction", "Mass trends in quenching and optical AGN incidence")
        bullets=[
            f"The first stellar-mass bin with quenched fraction above 0.5 is {transition_bin or 'not reached in these bins'}.",
            f"The optical AGN fraction peaks in the {peak_bin} bin at {peak_val:.3f}.",
            "The result is an optical transition diagnostic; gas fractions and baryon deficits are needed before assigning the transition to stellar or AGN feedback.",
        ]
        stats={**common,"transition_mass_bin_quenched_fraction_gt_0p5":transition_bin,"peak_agn_mass_bin":peak_bin,"peak_agn_fraction":float(peak_val),"mass_bin_labels":labels,"quenched_fraction_by_mass":qvals,"agn_fraction_by_mass":avals}
    elif spec.slug == "m3_p1_multiphase_census":
        defs={
            "BPT AGN": df["is_agn"],
            "high [NII]/Ha": df["high_nii"],
            "high [OIII]/Hb": df["high_oiii"],
            "red+emission": df["red_sequence"],
            "low-sSFR+emission": df["quenched"],
        }
        labels=list(defs.keys()); vals=[]; errs=[]; out={}
        for lab,mask in defs.items():
            ff=frac(mask); vals.append(ff["fraction"]); errs.append(ff["se"]); out[lab]=ff
        save_fraction_plot(fig, labels, [("selection prevalence", vals, errs)], "fraction of common denominator", "How optical tracer definitions change prevalence")
        minv=min(vals); maxv=max(vals); ratio=maxv/minv if minv>0 else float('inf')
        bullets=[
            f"Within the same {rows:,}-galaxy denominator, simple optical tracer definitions produce prevalence from {minv:.3f} to {maxv:.3f}.",
            f"The widest-to-narrowest prevalence ratio is {ratio:.1f}, before adding molecular, neutral, or X-ray/radio phases.",
            "This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates.",
        ]
        stats={**common,"tracer_prevalence":out,"prevalence_ratio_widest_to_narrowest":float(ratio)}
    elif spec.slug == "m3_p2_gas_depletion_efficiency":
        massive = df[df["massive"]]
        denom = massive[massive["transition_or_quenched"]]
        f_agn=frac(denom["is_agn"])
        med_lha=float(denom["log_lha"].median())
        sf_massive=massive[~massive["transition_or_quenched"]]
        diff=float(denom["log_lha"].median()-sf_massive["log_lha"].median()) if len(sf_massive) else float('nan')
        fig_obj, ax = plt.subplots(figsize=(5.8,4.2))
        ax.scatter(massive.sample(min(len(massive),8000), random_state=9)["lgm_tot_p50"], massive.sample(min(len(massive),8000), random_state=9)["specsfr_tot_p50"], s=2, alpha=0.12, color="#4c78a8")
        ax.axhline(-10.7, color="#e45756", ls="--", lw=1, label="transition/quenched cut")
        ax.set_xlabel("log stellar mass proxy")
        ax.set_ylabel("log specific SFR")
        ax.set_title("Massive SDSS denominator for gas follow-up")
        ax.legend(fontsize=8)
        fig_obj.tight_layout(); fig_obj.savefig(fig.with_suffix('.pdf')); fig_obj.savefig(fig.with_suffix('.png'), dpi=180); plt.close(fig_obj)
        bullets=[
            f"The massive transition/quenched denominator contains {len(denom):,} galaxies in the SDSS emission-line sample.",
            f"Its optical BPT AGN fraction is {f_agn['fraction']:.3f}; median log H-alpha luminosity proxy is {med_lha:.2f}.",
            f"The median H-alpha luminosity proxy is {diff:.2f} dex offset from massive star-forming emission-line galaxies.",
            "SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline.",
        ]
        stats={**common,"massive_transition_quenched_rows":int(len(denom)),"agn_fraction_in_denominator":f_agn,"median_log_lha_denominator":med_lha,"median_log_lha_offset_vs_massive_sf":diff}
    elif spec.slug == "m3_p3_simulation_validation":
        df2=df.copy()
        df2["mass_bin"] = mass_bins(df2)
        df2["z_bin"]=pd.cut(df2["z"], bins=[0.02,0.05,0.08,0.12], labels=["0.02-0.05","0.05-0.08","0.08-0.12"], include_lowest=True)
        pivot=[]
        for (mb,zb),g in df2.groupby(["mass_bin","z_bin"], observed=True):
            if len(g)>=50:
                pivot.append({"mass_bin":str(mb),"z_bin":str(zb),"n":int(len(g)),"quenched_fraction":float(g["quenched"].mean()),"agn_fraction":float(g["is_agn"].mean()),"median_u_minus_r":float(g["u_minus_r"].median())})
        labels=[]; qvals=[]; avals=[]; errs=[]
        for mb,g in df2.groupby("mass_bin", observed=True):
            if len(g)>100:
                labels.append(str(mb)); qvals.append(float(g["quenched"].mean())); avals.append(float(g["is_agn"].mean())); errs.append(binomial_se(float(g["quenched"].mean()), len(g)))
        save_fraction_plot(fig, labels, [("quenched", qvals, errs), ("BPT AGN", avals, [binomial_se(v, max(1, int(len(df2)/len(labels)))) for v in avals])], "fraction", "Observed SDSS target vector by mass")
        bullets=[
            f"The pilot writes {len(pivot)} mass-redshift cells with n >= 50 as a compact validation vector.",
            f"Across mass bins, quenched fractions span {min(qvals):.3f}-{max(qvals):.3f}; optical AGN fractions span {min(avals):.3f}-{max(avals):.3f}.",
            "The output is an observed target vector for simulation forward modelling, not a direct simulation comparison.",
        ]
        stats={**common,"target_vector_cells":pivot,"quenched_fraction_range":[float(min(qvals)),float(max(qvals))],"agn_fraction_range":[float(min(avals)),float(max(avals))]}
    else:
        raise ValueError(spec.slug)

    return stats, bullets, fig.with_suffix(".pdf")


MANUSCRIPT = Template(r"""\documentclass[twocolumn]{aastex631}
\graphicspath{{../figures/}}
\begin{document}

\title{$title}
\shorttitle{$short_title}
\author{NebulaMind Research Autopilot}
\affiliation{Local reproducible pilot run; public SDSS DR17 data only}

\begin{abstract}
We execute a bounded actual-data pilot for the Galaxy Evolution research topic ``$proposal_title''.  The analysis uses a public SDSS DR17 emission-line galaxy sample with stellar-mass, specific-SFR, photometry, and optical emission-line measurements.  The pilot question is: $question  The result is intended as a survey denominator or proxy measurement, not as a full causal test of feedback physics.
\end{abstract}

\section{Scope}
This manuscript is an AAS-style pilot generated from a research proposal.  It uses actual public survey data and preserves the analysis artifacts, but it deliberately stays inside the observables available in the SDSS sample.  The full proposal requires $requires

\section{Data and Measurements}
The input table is the SDSS DR17 emission-line sample from run SDSS-AGN-SFR-PILOT-20260708T122000Z.  It contains $sample_rows galaxies after requiring spectroscopic galaxy classification, redshift 0.02--0.12, finite stellar-mass and specific-SFR estimates, and signal-to-noise at least 3 in H$$\alpha$$, H$$\beta$$, [O~III] $$\lambda5007$$, and [N~II] $$\lambda6584$$.  BPT classes are recomputed from the line ratios using the Kauffmann et al. and Kewley et al. demarcations.  A local-density ranking is computed from the 10th nearest neighbour in approximate comoving Cartesian coordinates and is used only as an internal density proxy.

\section{Pilot Result}
\begin{itemize}
$bullets
\end{itemize}

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{$figure_name}
\caption{$caption}
\end{figure}

\section{Interpretation Guard}
This pilot should not be read as a completed proof of the full feedback proposal.  It is a reproducible SDSS measurement that defines a denominator, proxy, or validation target for the larger research design.  In particular, it does not by itself establish causal AGN feedback, gas escape, radio-jet coupling efficiency, X-ray maintenance heating, molecular-gas depletion, or simulation correctness.

\section{Reproducibility}
Run identifier: $run_id.  The run directory preserves the topic-specific JSON summary, figure files, manuscript source, compile log, and compiled PDF.  The workflow used read-only public SDSS-derived data already cached from the first pilot plus local artifact writes only.

\acknowledgments
This pilot used public SDSS DR17 data products and open-source Python tools.

\begin{thebibliography}{}
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Kauffmann et al.(2003)]{kauffmann2003} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}
""")


def write_manuscript(spec: PilotSpec, run_dir: Path, stats: dict, bullets: list[str], fig_pdf: Path):
    tex_dir = run_dir / "aastex"
    tex_dir.mkdir(parents=True, exist_ok=True)
    bullet_tex = "\n".join("\\item " + tex_escape(b) for b in bullets)
    tex = MANUSCRIPT.substitute(
        title=tex_escape(spec.short_title + ": an SDSS DR17 pilot"),
        short_title=tex_escape(spec.short_title),
        proposal_title=tex_escape(spec.title),
        question=tex_escape(spec.question),
        requires=tex_escape(spec.full_proposal_requires),
        sample_rows=f"{stats['sample_rows']:,}",
        bullets=bullet_tex,
        figure_name=tex_escape(fig_pdf.name),
        caption=tex_escape("Topic-specific SDSS DR17 pilot measurement. The figure is a proxy or denominator diagnostic, not the full multi-survey test."),
        run_id=tex_escape(RUN_ID),
    )
    tex_path = tex_dir / f"{spec.slug}_aas.tex"
    tex_path.write_text(tex)
    # Copy figure into tex directory for simple \includegraphics lookup.
    shutil.copy2(fig_pdf, tex_dir / fig_pdf.name)
    png = fig_pdf.with_suffix(".png")
    if png.exists():
        shutil.copy2(png, tex_dir / png.name)
    proc = subprocess.run(["tectonic", tex_path.name], cwd=tex_dir, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
    (tex_dir / "compile.log").write_text(proc.stdout)
    if proc.returncode != 0:
        raise SystemExit(f"Tectonic failed for {spec.slug}:\n{proc.stdout[-4000:]}")
    pdf = tex_dir / f"{spec.slug}_aas.pdf"
    if not pdf.exists() or pdf.stat().st_size <= 0:
        raise SystemExit(f"Missing compiled PDF for {spec.slug}")
    return tex_path, pdf, tex_dir / "compile.log"


def main():
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    df = load_sample()
    manifest = {"run_id": RUN_ID, "source_csv": str(SOURCE_CSV), "topics": []}
    for spec in SPECS:
        run_dir = OUT_ROOT / spec.slug
        data_dir = run_dir / "data"
        fig_dir = run_dir / "figures"
        data_dir.mkdir(parents=True, exist_ok=True)
        fig_dir.mkdir(parents=True, exist_ok=True)
        stats, bullets, fig_pdf = compute_topic(spec, df, fig_dir)
        stats.update({
            "slug": spec.slug,
            "method": spec.method,
            "card_id": spec.card_id,
            "proposal_title": spec.title,
            "short_title": spec.short_title,
            "pilot_question": spec.question,
            "full_proposal_requires": spec.full_proposal_requires,
            "result_bullets": bullets,
            "figure_pdf": str(fig_pdf),
        })
        (run_dir / "analysis_results.json").write_text(json.dumps(stats, indent=2, sort_keys=True))
        (run_dir / "METHODS_AND_SCOPE.md").write_text(
            f"# {spec.short_title}\n\n"
            f"Run: `{RUN_ID}`\n\n"
            f"Proposal: {spec.title}\n\n"
            f"Pilot question: {spec.question}\n\n"
            f"Data: cached public SDSS DR17 emission-line sample from `{SOURCE_CSV}`.\n\n"
            "Interpretation guard: this is an SDSS-only actual-data pilot. It does not claim to complete the full multi-survey feedback test.\n\n"
            f"Full proposal still requires: {spec.full_proposal_requires}\n"
        )
        tex_path, pdf, compile_log = write_manuscript(spec, run_dir, stats, bullets, fig_pdf)
        import hashlib
        pdf_sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
        item = {
            "slug": spec.slug,
            "method": spec.method,
            "card_id": spec.card_id,
            "title": spec.title,
            "short_title": spec.short_title,
            "pdf": str(pdf),
            "pdf_name": pdf.name,
            "pdf_bytes": pdf.stat().st_size,
            "pdf_sha256": pdf_sha,
            "tex": str(tex_path),
            "compile_log": str(compile_log),
            "figure_pdf": str(fig_pdf),
        }
        manifest["topics"].append(item)
        print(f"DONE {spec.slug} {pdf.stat().st_size} {pdf_sha}")
    (OUT_ROOT / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps({"run_root": str(OUT_ROOT), "topic_count": len(manifest["topics"]), "manifest": str(OUT_ROOT / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json")}, indent=2))

if __name__ == "__main__":
    main()
