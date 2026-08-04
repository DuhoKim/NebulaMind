#!/usr/bin/env python3
"""Goru lane: regression/bin sensitivity robustness tick for overnight active-9 papers.

Reads cached SDSS-derived local CSVs only and writes lane-local Goru artifacts.
Adds mechanical regression/LPM sensitivity, alternate mass/redshift bins, bootstrap
paper-table candidates, and an inventory of this tick's outputs. All quantities
are SDSS optical proxy/denominator measurements, not causal feedback claims.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
WORK_ROOT = AUTOPILOT / "overnight-9-papers-20260708"
GORU_ROOT = WORK_ROOT / "lanes/goru"
os.environ.setdefault("MPLCONFIGDIR", str(GORU_ROOT / "matplotlib-cache"))

try:
    import matplotlib.pyplot as plt
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"matplotlib is required for lane-local figure output: {exc}")

RUN1 = AUTOPILOT / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
SOURCE_CSV = RUN1 / "data/analysis_sample_bpt.csv"
SOURCE_RESULTS = RUN1 / "analysis_results.json"

MARKER_BASE = "GORU_REGRESSION_BIN_SENSITIVITY_TICK"
PROXY_GUARD = (
    "SDSS optical emission-line/color/sSFR proxy or denominator only; no causal AGN feedback, "
    "gas-depletion, radio-jet coupling, escape/recycling, X-ray maintenance-heating, or simulation-validation proof."
)
SN_THRESHOLDS = [3, 5, 10]
DENSITY_K = [5, 10, 20]
RNG_SEED = 20260708
C_KM_S = 299792.458
H0 = 70.0

TOPIC_LABELS = {
    "m1_rp1_agn_sfr": "M1 RP-1 — SDSS AGN/sSFR matched-control pilot",
    "m1_rp2_environment_quenching": "M1 RP-2 — SDSS density proxy for environmental quenching",
    "m1_rp3_maintenance_heating": "M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up",
    "m2_p1_outflow_escape_recycling": "M2 P1 — high-excitation optical AGN denominator for outflow escape/recycling tests",
    "m2_p2_radio_jet_environment": "M2 P2 — environment proxy for optical AGN in massive hosts",
    "m2_p3_feedback_transition_mass": "M2 P3 — mass transition in quenching and optical AGN incidence",
    "m3_p1_multiphase_census": "M3 P1 — common-denominator optical tracer census",
    "m3_p2_gas_depletion_efficiency": "M3 P2 — optical denominator for gas-fraction versus efficiency tests",
    "m3_p3_simulation_validation": "M3 P3 — SDSS target vector for feedback-model validation",
}


def utc_ts() -> str:
    return os.environ.get("GORU_TICK_TS") or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def assert_goru_write(path: Path) -> None:
    resolved = path.resolve()
    goru = GORU_ROOT.resolve()
    if goru not in [resolved, *resolved.parents]:
        raise RuntimeError(f"Refusing non-Goru-lane write: {resolved}")


def safe_float(v: Any) -> float | None:
    try:
        x = float(v)
    except Exception:
        return None
    return x if math.isfinite(x) else None


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    assert_goru_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        rows = [{"status": "NO_ROWS"}]
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def fraction(mask: Iterable[Any]) -> dict[str, Any]:
    vals = np.asarray(list(mask), dtype=bool)
    n = int(len(vals))
    k = int(vals.sum())
    p = k / n if n else float("nan")
    se = math.sqrt(max(p * (1.0 - p), 0.0) / n) if n else float("nan")
    return {"n": n, "k": k, "fraction": safe_float(p), "se": safe_float(se)}


def bootstrap_ci(values: Iterable[float], func: Callable[[np.ndarray], float] = np.nanmean, n_boot: int = 1200, seed: int = RNG_SEED) -> tuple[float | None, float | None]:
    arr = np.asarray([float(v) for v in values if math.isfinite(float(v))], dtype=float)
    if len(arr) == 0:
        return None, None
    rng = np.random.default_rng(seed + len(arr))
    draws = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        sample = arr[rng.integers(0, len(arr), len(arr))]
        draws[i] = float(func(sample))
    return safe_float(np.percentile(draws, 2.5)), safe_float(np.percentile(draws, 97.5))


def bootstrap_fraction_ci(mask: Iterable[Any], n_boot: int = 1200, seed: int = RNG_SEED) -> tuple[float | None, float | None]:
    vals = np.asarray(list(mask), dtype=float)
    if len(vals) == 0:
        return None, None
    rng = np.random.default_rng(seed + len(vals) + int(vals.sum()))
    draws = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        sample = vals[rng.integers(0, len(vals), len(vals))]
        draws[i] = float(np.mean(sample))
    return safe_float(np.percentile(draws, 2.5)), safe_float(np.percentile(draws, 97.5))


def bootstrap_diff_ci(a: Iterable[Any], b: Iterable[Any], func: Callable[[np.ndarray], float] = np.nanmean, n_boot: int = 1200, seed: int = RNG_SEED) -> tuple[float | None, float | None]:
    aa = np.asarray([float(v) for v in a if math.isfinite(float(v))], dtype=float)
    bb = np.asarray([float(v) for v in b if math.isfinite(float(v))], dtype=float)
    if len(aa) == 0 or len(bb) == 0:
        return None, None
    rng = np.random.default_rng(seed + len(aa) * 3 + len(bb))
    draws = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        da = aa[rng.integers(0, len(aa), len(aa))]
        db = bb[rng.integers(0, len(bb), len(bb))]
        draws[i] = float(func(da) - func(db))
    return safe_float(np.percentile(draws, 2.5)), safe_float(np.percentile(draws, 97.5))


def add_density_proxy(df: pd.DataFrame, k: int) -> None:
    ra = np.deg2rad(df["ra"].to_numpy(dtype=float))
    dec = np.deg2rad(df["dec"].to_numpy(dtype=float))
    dist = (C_KM_S / H0) * df["z"].to_numpy(dtype=float)
    xyz = np.column_stack([
        dist * np.cos(dec) * np.cos(ra),
        dist * np.cos(dec) * np.sin(ra),
        dist * np.sin(dec),
    ])
    tree = cKDTree(xyz)
    dists, _ = tree.query(xyz, k=k + 1)
    kth = np.maximum(dists[:, -1], 1e-6)
    density = k / ((4.0 / 3.0) * math.pi * kth**3)
    logd = np.log10(density)
    df[f"log_density_k{k}"] = logd
    q = pd.qcut(logd, 4, labels=["Q1 low", "Q2", "Q3", "Q4 high"], duplicates="drop").astype(str)
    df[f"density_q_k{k}"] = q
    df[f"low_density_k{k}"] = q == "Q1 low"
    df[f"high_density_k{k}"] = q == "Q4 high"


def load_sample() -> pd.DataFrame:
    if not SOURCE_CSV.exists():
        raise SystemExit(f"Missing cached source CSV: {SOURCE_CSV}")
    df = pd.read_csv(SOURCE_CSV)
    required = [
        "specObjID", "ra", "dec", "z", "lgm_tot_p50", "specsfr_tot_p50",
        "modelMag_u", "modelMag_r", "u_minus_r", "g_minus_r",
        "h_alpha_flux", "h_alpha_flux_err", "h_beta_flux", "h_beta_flux_err",
        "oiii_5007_flux", "oiii_5007_flux_err", "nii_6584_flux", "nii_6584_flux_err",
        "log_nii_ha", "log_oiii_hb", "bpt_label",
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise SystemExit(f"Cached source CSV missing required columns: {missing}")
    for col in [c for c in required if c not in {"specObjID", "bpt_label"}]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=[c for c in required if c not in {"specObjID", "bpt_label"}]).copy()
    df["specObjID"] = df["specObjID"].astype(str)
    df["sn_ha_calc"] = df["h_alpha_flux"] / df["h_alpha_flux_err"]
    df["sn_hb_calc"] = df["h_beta_flux"] / df["h_beta_flux_err"]
    df["sn_oiii_calc"] = df["oiii_5007_flux"] / df["oiii_5007_flux_err"]
    df["sn_nii_calc"] = df["nii_6584_flux"] / df["nii_6584_flux_err"]
    df["sn_min"] = df[["sn_ha_calc", "sn_hb_calc", "sn_oiii_calc", "sn_nii_calc"]].min(axis=1)
    x = df["log_nii_ha"].to_numpy(dtype=float)
    y = df["log_oiii_hb"].to_numpy(dtype=float)
    kauffmann = 0.61 / (x - 0.05) + 1.30
    kewley = 0.61 / (x - 0.47) + 1.19
    seyfert_line = 1.01 * x + 0.48
    valid = np.isfinite(x) & np.isfinite(y) & (x <= 0.35)
    # Preserve the mutually exclusive class labels used by the original cached
    # run.  The analytic demarcation curves are still computed above for
    # Seyfert/LINER-style proxy margins, but direct y< Kauffmann and y> Kewley
    # masks can overlap near the divergent curve segment; using `bpt_label`
    # avoids double-counting controls in matched tests.
    df["bpt_sf"] = df["bpt_label"].eq("star-forming")
    df["bpt_intermediate"] = df["bpt_label"].eq("intermediate")
    df["bpt_agn"] = df["bpt_label"].eq("agn")
    df["inclusive_non_sf"] = df["bpt_intermediate"] | df["bpt_agn"]
    df["high_excitation_agn_ygt0p25"] = df["bpt_agn"] & (df["log_oiii_hb"] > 0.25)
    df["high_excitation_agn_ygt0p50"] = df["bpt_agn"] & (df["log_oiii_hb"] > 0.50)
    df["nii_seyfert_like_proxy"] = df["bpt_agn"] & ((y - seyfert_line) >= 0)
    df["nii_liner_like_proxy"] = df["bpt_agn"] & ((y - seyfert_line) < 0)
    df["quenched_ssfr_lt_m11"] = df["specsfr_tot_p50"] < -11.0
    df["transition_or_quenched_ssfr_lt_m10p7"] = df["specsfr_tot_p50"] < -10.7
    df["very_quenched_ssfr_lt_m11p5"] = df["specsfr_tot_p50"] < -11.5
    df["massive_ge_10p8"] = df["lgm_tot_p50"] >= 10.8
    df["red_sequence_u_minus_r_gt_2p2"] = df["u_minus_r"] > 2.2
    dl_mpc = (C_KM_S / H0) * df["z"] * (1.0 + df["z"])
    flux = df["h_alpha_flux"].clip(lower=1e-12) * 1e-17
    lum = 4.0 * math.pi * (dl_mpc * 3.0856775814913673e24) ** 2 * flux
    df["log_lha_proxy"] = np.log10(lum)
    for k in DENSITY_K:
        add_density_proxy(df, k)
    return df


def ols_hc1(y: Iterable[Any], x_interest: Iterable[Any], controls: list[Iterable[Any]], interest_name: str) -> dict[str, Any]:
    y_arr = np.asarray(list(y), dtype=float)
    xi = np.asarray(list(x_interest), dtype=float)
    cols = [np.ones(len(y_arr), dtype=float), xi]
    for c in controls:
        cols.append(np.asarray(list(c), dtype=float))
    X = np.column_stack(cols)
    finite = np.isfinite(y_arr) & np.all(np.isfinite(X), axis=1)
    y2 = y_arr[finite]
    X2 = X[finite]
    xi2 = xi[finite]
    n = int(len(y2))
    p = int(X2.shape[1]) if n else 0
    out = {
        "n_regression": n,
        "n_interest_positive": int(np.sum(xi2 > 0.5)) if n else 0,
        "interest_name": interest_name,
        "coef_interest": None,
        "robust_se_interest": None,
        "ci95_low": None,
        "ci95_high": None,
        "r2": None,
        "skip_reason": "",
    }
    if n <= p + 2 or int(np.sum(xi2 > 0.5)) < 10 or int(np.sum(xi2 <= 0.5)) < 10:
        out["skip_reason"] = "insufficient_rows_or_interest_balance"
        return out
    beta = np.linalg.pinv(X2.T @ X2) @ X2.T @ y2
    resid = y2 - X2 @ beta
    xtx_inv = np.linalg.pinv(X2.T @ X2)
    meat = X2.T @ ((resid[:, None] ** 2) * X2)
    cov = (n / max(n - p, 1)) * xtx_inv @ meat @ xtx_inv
    se = np.sqrt(np.maximum(np.diag(cov), 0.0))
    tss = float(np.sum((y2 - y2.mean()) ** 2))
    rss = float(np.sum(resid**2))
    b = float(beta[1])
    s = float(se[1])
    out.update({
        "coef_interest": safe_float(b),
        "robust_se_interest": safe_float(s),
        "ci95_low": safe_float(b - 1.96 * s),
        "ci95_high": safe_float(b + 1.96 * s),
        "r2": safe_float(1.0 - rss / tss) if tss > 0 else None,
    })
    return out


def regression_rows(df: pd.DataFrame) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    target_defs = [
        ("bpt_agn_vs_sf", "bpt_agn", "BPT AGN vs star-forming controls", "m1_rp1_agn_sfr"),
        ("inclusive_non_sf_vs_sf", "inclusive_non_sf", "BPT intermediate+AGN vs star-forming controls", "m1_rp1_agn_sfr"),
        ("high_excitation_ygt0p25_vs_sf", "high_excitation_agn_ygt0p25", "AGN with log([OIII]/Hb)>0.25 vs star-forming controls", "m2_p1_outflow_escape_recycling"),
        ("nii_seyfert_like_proxy_vs_sf", "nii_seyfert_like_proxy", "NII-BPT Seyfert-like proxy vs star-forming controls", "m2_p1_outflow_escape_recycling"),
    ]
    for sn in SN_THRESHOLDS:
        sn_sub = df[df["sn_min"] >= sn].copy()
        for variant, col, desc, topic in target_defs:
            use = sn_sub[sn_sub[col] | sn_sub["bpt_sf"]].copy()
            fit = ols_hc1(
                y=use["specsfr_tot_p50"],
                x_interest=use[col].astype(float),
                controls=[use["lgm_tot_p50"], use["z"]],
                interest_name=variant,
            )
            rows.append({
                "topic": topic,
                "topic_label": TOPIC_LABELS[topic],
                "model_family": "OLS_HC1",
                "outcome": "log_sSFR",
                "variant": variant,
                "sn_min_ge": sn,
                "sample_scope": "target_definition_or_BPT_star_forming_only",
                "coefficient_interpretation": "target minus star-forming conditional on logM and z; association only",
                "definition_note": desc,
                **fit,
                "proxy_guard": PROXY_GUARD,
            })
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min"] >= sn].copy()
        for k in DENSITY_K:
            fit = ols_hc1(
                y=sub["quenched_ssfr_lt_m11"].astype(float),
                x_interest=sub[f"high_density_k{k}"].astype(float),
                controls=[sub["lgm_tot_p50"], sub["z"]],
                interest_name=f"high_density_k{k}",
            )
            rows.append({
                "topic": "m1_rp2_environment_quenching",
                "topic_label": TOPIC_LABELS["m1_rp2_environment_quenching"],
                "model_family": "LPM_OLS_HC1",
                "outcome": "quenched_ssfr_lt_-11",
                "variant": f"high_density_k{k}_sn_ge_{sn}",
                "sn_min_ge": sn,
                "sample_scope": "all_cached_rows_at_sn_cut",
                "coefficient_interpretation": "high-density quartile minus other quartiles conditional on logM and z; density proxy only",
                **fit,
                "proxy_guard": PROXY_GUARD,
            })
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min"] >= sn].copy()
        # Mass-transition coefficients per dex, used only as a mechanical trend check.
        for outcome, ycol in [("quenched_ssfr_lt_-11", "quenched_ssfr_lt_m11"), ("bpt_agn_fraction", "bpt_agn")]:
            fit = ols_hc1(
                y=sub[ycol].astype(float),
                x_interest=sub["lgm_tot_p50"],
                controls=[sub["z"]],
                interest_name="logM_per_dex",
            )
            rows.append({
                "topic": "m2_p3_feedback_transition_mass",
                "topic_label": TOPIC_LABELS["m2_p3_feedback_transition_mass"],
                "model_family": "LPM_OLS_HC1",
                "outcome": outcome,
                "variant": f"logM_trend_sn_ge_{sn}",
                "sn_min_ge": sn,
                "sample_scope": "all_cached_rows_at_sn_cut",
                "coefficient_interpretation": "change in probability per dex logM conditional on z; optical trend only",
                **fit,
                "proxy_guard": PROXY_GUARD,
            })
        for mass_cut in [10.6, 10.8, 11.0]:
            massive = sub[sub["lgm_tot_p50"] >= mass_cut].copy()
            for k in DENSITY_K:
                fit = ols_hc1(
                    y=massive["bpt_agn"].astype(float),
                    x_interest=massive[f"high_density_k{k}"].astype(float),
                    controls=[massive["lgm_tot_p50"], massive["z"]],
                    interest_name=f"high_density_k{k}",
                )
                rows.append({
                    "topic": "m2_p2_radio_jet_environment",
                    "topic_label": TOPIC_LABELS["m2_p2_radio_jet_environment"],
                    "model_family": "LPM_OLS_HC1",
                    "outcome": "bpt_agn_fraction",
                    "variant": f"mass_ge_{mass_cut}_high_density_k{k}_sn_ge_{sn}",
                    "sn_min_ge": sn,
                    "sample_scope": f"mass_ge_{mass_cut}",
                    "coefficient_interpretation": "high-density quartile optical-AGN probability coefficient conditional on logM and z; no radio jet data",
                    **fit,
                    "proxy_guard": PROXY_GUARD,
                })
            fit_halpha = ols_hc1(
                y=massive["log_lha_proxy"],
                x_interest=massive["transition_or_quenched_ssfr_lt_m10p7"].astype(float),
                controls=[massive["lgm_tot_p50"], massive["z"]],
                interest_name="transition_or_quenched_ssfr_lt_-10.7",
            )
            rows.append({
                "topic": "m3_p2_gas_depletion_efficiency",
                "topic_label": TOPIC_LABELS["m3_p2_gas_depletion_efficiency"],
                "model_family": "OLS_HC1",
                "outcome": "log_Halpha_luminosity_proxy",
                "variant": f"mass_ge_{mass_cut}_transition_quenched_sn_ge_{sn}",
                "sn_min_ge": sn,
                "sample_scope": f"mass_ge_{mass_cut}",
                "coefficient_interpretation": "transition/quenched minus star-forming-like massive hosts conditional on logM and z; H-alpha is not molecular gas",
                **fit_halpha,
                "proxy_guard": PROXY_GUARD,
            })
    return rows


def alternate_bin_rows(df: pd.DataFrame) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    grids = [
        ("broad_mass_z3", [8.0, 9.5, 10.0, 10.5, 11.0, 12.5], [0.02, 0.05, 0.08, 0.12]),
        ("transition_fine_mass_z4", [8.0, 9.0, 9.5, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 12.5], [0.02, 0.04, 0.06, 0.09, 0.12]),
        ("aperture_proxy_low_mid_high_z", [8.0, 10.0, 10.5, 10.8, 11.0, 12.5], [0.02, 0.06, 0.10, 0.12]),
    ]
    for grid_name, mass_edges, z_edges in grids:
        mass_labels = [f"{mass_edges[i]:.2f}-{mass_edges[i+1]:.2f}" for i in range(len(mass_edges) - 1)]
        z_labels = [f"{z_edges[i]:.3f}-{z_edges[i+1]:.3f}" for i in range(len(z_edges) - 1)]
        tmp = df.copy()
        tmp["alt_mass_bin"] = pd.cut(tmp["lgm_tot_p50"], mass_edges, labels=mass_labels, include_lowest=True).astype(str)
        tmp["alt_z_bin"] = pd.cut(tmp["z"], z_edges, labels=z_labels, include_lowest=True).astype(str)
        for sn in SN_THRESHOLDS:
            sub = tmp[tmp["sn_min"] >= sn]
            for (mb, zb), g in sub.groupby(["alt_mass_bin", "alt_z_bin"], observed=True):
                if str(mb) == "nan" or str(zb) == "nan" or len(g) == 0:
                    continue
                n = int(len(g))
                rows.append({
                    "grid_name": grid_name,
                    "sn_min_ge": sn,
                    "mass_bin_logM": str(mb),
                    "z_bin": str(zb),
                    "n": n,
                    "low_n_flag": "LOW_N_LT_50" if n < 50 else "OK",
                    "bpt_agn_n": int(g["bpt_agn"].sum()),
                    "bpt_agn_fraction": safe_float(g["bpt_agn"].mean()),
                    "inclusive_non_sf_fraction": safe_float(g["inclusive_non_sf"].mean()),
                    "high_excitation_ygt0p25_fraction": safe_float(g["high_excitation_agn_ygt0p25"].mean()),
                    "nii_seyfert_like_proxy_fraction": safe_float(g["nii_seyfert_like_proxy"].mean()),
                    "quenched_ssfr_lt_m11_fraction": safe_float(g["quenched_ssfr_lt_m11"].mean()),
                    "transition_or_quenched_ssfr_lt_m10p7_fraction": safe_float(g["transition_or_quenched_ssfr_lt_m10p7"].mean()),
                    "red_sequence_fraction": safe_float(g["red_sequence_u_minus_r_gt_2p2"].mean()),
                    "median_log_sSFR": safe_float(g["specsfr_tot_p50"].median()),
                    "median_logM": safe_float(g["lgm_tot_p50"].median()),
                    "median_z": safe_float(g["z"].median()),
                    "median_log_lha_proxy": safe_float(g["log_lha_proxy"].median()),
                    "median_log_density_k10": safe_float(g["log_density_k10"].median()),
                    "proxy_guard": PROXY_GUARD,
                })
    return rows


def match_delta(df: pd.DataFrame, target_mask: pd.Series, control_mask: pd.Series) -> dict[str, Any]:
    targets = df[target_mask].copy()
    controls = df[control_mask].copy()
    base = {
        "target_n": int(len(targets)),
        "control_n": int(len(controls)),
        "matched_pairs": 0,
        "median_delta": None,
        "median_ci95_low": None,
        "median_ci95_high": None,
        "mean_delta": None,
        "mean_ci95_low": None,
        "mean_ci95_high": None,
        "match_abs_delta_logM_median": None,
        "match_abs_delta_z_median": None,
        "skip_reason": "",
    }
    if len(targets) < 30 or len(controls) < 30:
        base["skip_reason"] = "target_n_or_control_n_lt_30"
        return base
    features = ["lgm_tot_p50", "z"]
    scale = controls[features].std().replace(0, 1.0)
    center = controls[features].mean()
    tree = cKDTree(((controls[features] - center) / scale).to_numpy(dtype=float))
    dist, idx = tree.query(((targets[features] - center) / scale).to_numpy(dtype=float), k=1)
    ctrl = controls.iloc[idx].reset_index(drop=True)
    targ = targets.reset_index(drop=True)
    delta = targ["specsfr_tot_p50"].to_numpy(dtype=float) - ctrl["specsfr_tot_p50"].to_numpy(dtype=float)
    med_lo, med_hi = bootstrap_ci(delta, np.nanmedian)
    mean_lo, mean_hi = bootstrap_ci(delta, np.nanmean)
    base.update({
        "matched_pairs": int(len(delta)),
        "median_delta": safe_float(np.nanmedian(delta)),
        "median_ci95_low": med_lo,
        "median_ci95_high": med_hi,
        "mean_delta": safe_float(np.nanmean(delta)),
        "mean_ci95_low": mean_lo,
        "mean_ci95_high": mean_hi,
        "match_abs_delta_logM_median": safe_float(np.nanmedian(np.abs(targ["lgm_tot_p50"] - ctrl["lgm_tot_p50"]))),
        "match_abs_delta_z_median": safe_float(np.nanmedian(np.abs(targ["z"] - ctrl["z"]))),
    })
    return base


def add_topic_row(rows: list[dict[str, Any]], topic: str, metric: str, variant: str, value: Any, n: Any = None, k: Any = None, ci: tuple[Any, Any] | None = None, note: str = "") -> None:
    ci = ci or (None, None)
    rows.append({
        "topic": topic,
        "topic_label": TOPIC_LABELS[topic],
        "metric": metric,
        "variant": variant,
        "n": n,
        "k": k,
        "value": value,
        "ci95_low": ci[0],
        "ci95_high": ci[1],
        "note": note,
        "proxy_guard": PROXY_GUARD,
    })


def topic_bootstrap_rows(df: pd.DataFrame) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min"] >= sn].copy()
        for name, mask_col, topic in [
            ("bpt_agn_vs_sf", "bpt_agn", "m1_rp1_agn_sfr"),
            ("high_excitation_ygt0p25_vs_sf", "high_excitation_agn_ygt0p25", "m2_p1_outflow_escape_recycling"),
            ("nii_seyfert_like_proxy_vs_sf", "nii_seyfert_like_proxy", "m2_p1_outflow_escape_recycling"),
        ]:
            md = match_delta(sub, sub[mask_col], sub["bpt_sf"])
            add_topic_row(rows, topic, "matched_median_delta_log_sSFR_target_minus_sf", f"{name}_sn_ge_{sn}", md["median_delta"], md["matched_pairs"], md["target_n"], (md["median_ci95_low"], md["median_ci95_high"]), "Nearest-neighbour matched in logM,z; association only.")
        for k in DENSITY_K:
            low = sub[sub[f"low_density_k{k}"]]
            high = sub[sub[f"high_density_k{k}"]]
            ci = bootstrap_diff_ci(high["quenched_ssfr_lt_m11"].astype(float), low["quenched_ssfr_lt_m11"].astype(float), np.nanmean)
            val = safe_float(high["quenched_ssfr_lt_m11"].mean() - low["quenched_ssfr_lt_m11"].mean())
            add_topic_row(rows, "m1_rp2_environment_quenching", "high_minus_low_density_quenched_fraction", f"k{k}_sn_ge_{sn}", val, int(len(high) + len(low)), None, ci, "Nearest-neighbour density quartiles only; no halo/group catalogue.")
            massive = sub[sub["massive_ge_10p8"]]
            lowm = massive[massive[f"low_density_k{k}"]]
            highm = massive[massive[f"high_density_k{k}"]]
            ci2 = bootstrap_diff_ci(highm["bpt_agn"].astype(float), lowm["bpt_agn"].astype(float), np.nanmean)
            val2 = safe_float(highm["bpt_agn"].mean() - lowm["bpt_agn"].mean())
            add_topic_row(rows, "m2_p2_radio_jet_environment", "massive_high_minus_low_density_bpt_agn_fraction", f"mass_ge_10.8_k{k}_sn_ge_{sn}", val2, int(len(highm) + len(lowm)), None, ci2, "Optical AGN/density denominator only; no radio jet measurement.")
        for mass_cut in [10.6, 10.8, 11.0]:
            massive = sub[sub["lgm_tot_p50"] >= mass_cut]
            for ssfr_name, ssfr_col in [("transition_ssfr_lt_m10p7", "transition_or_quenched_ssfr_lt_m10p7"), ("quenched_ssfr_lt_m11", "quenched_ssfr_lt_m11")]:
                denom = massive[massive[ssfr_col]]
                fr = fraction(denom["bpt_agn"])
                ci = bootstrap_fraction_ci(denom["bpt_agn"].astype(bool))
                add_topic_row(rows, "m1_rp3_maintenance_heating", "optical_agn_fraction_massive_low_sSFR", f"mass_ge_{mass_cut}_{ssfr_name}_sn_ge_{sn}", fr["fraction"], fr["n"], fr["k"], ci, "Optical duty-cycle denominator only; no X-ray/radio heating data.")
                add_topic_row(rows, "m3_p2_gas_depletion_efficiency", "massive_low_sSFR_denominator_count", f"mass_ge_{mass_cut}_{ssfr_name}_sn_ge_{sn}", int(len(denom)), int(len(massive)), int(len(denom)), None, "CO/dust follow-up denominator only; not gas depletion/SFE.")
        for definition, col in [
            ("bpt_agn", "bpt_agn"),
            ("inclusive_non_sf", "inclusive_non_sf"),
            ("high_excitation_ygt0p25", "high_excitation_agn_ygt0p25"),
            ("high_excitation_ygt0p50", "high_excitation_agn_ygt0p50"),
            ("red_sequence", "red_sequence_u_minus_r_gt_2p2"),
            ("low_sSFR_quenched", "quenched_ssfr_lt_m11"),
        ]:
            fr = fraction(sub[col])
            ci = bootstrap_fraction_ci(sub[col].astype(bool))
            add_topic_row(rows, "m3_p1_multiphase_census", "common_denominator_optical_tracer_prevalence", f"{definition}_sn_ge_{sn}", fr["fraction"], fr["n"], fr["k"], ci, "Optical tracer only; no molecular/neutral/X-ray/radio phases.")
    # M2 P3 and M3 P3 compact summaries from alternate target-vector cells.
    base = df[df["sn_min"] >= 3].copy()
    mass_edges = [8.0, 9.5, 10.0, 10.5, 11.0, 12.5]
    mass_labels = [f"{mass_edges[i]:.1f}-{mass_edges[i+1]:.1f}" for i in range(len(mass_edges) - 1)]
    base["mass_bin"] = pd.cut(base["lgm_tot_p50"], mass_edges, labels=mass_labels, include_lowest=True).astype(str)
    qvals = []
    avals = []
    for mb, g in base.groupby("mass_bin", observed=True):
        if str(mb) == "nan" or len(g) < 50:
            continue
        q = safe_float(g["quenched_ssfr_lt_m11"].mean())
        a = safe_float(g["bpt_agn"].mean())
        qvals.append((str(mb), q, len(g)))
        avals.append((str(mb), a, len(g)))
    transition_bin = next((mb for mb, q, _ in qvals if q is not None and q >= 0.5), "not_reached")
    peak_agn_bin, peak_agn_val, peak_n = max(avals, key=lambda t: t[1] if t[1] is not None else -1)
    add_topic_row(rows, "m2_p3_feedback_transition_mass", "first_mass_bin_quenched_fraction_ge_0.5", "broad_mass_bins_sn_ge_3", transition_bin, None, None, None, "Mass-bin diagnostic only; no baryon deficit/gas fraction evidence.")
    add_topic_row(rows, "m2_p3_feedback_transition_mass", "peak_optical_agn_mass_bin", "broad_mass_bins_sn_ge_3", peak_agn_val, peak_n, None, None, f"Peak broad bin {peak_agn_bin}; optical diagnostic only.")
    base["z_bin"] = pd.cut(base["z"], [0.02, 0.05, 0.08, 0.12], labels=["0.02-0.05", "0.05-0.08", "0.08-0.12"], include_lowest=True).astype(str)
    cell_count = 0
    low_n_count = 0
    for (_mb, _zb), g in base.groupby(["mass_bin", "z_bin"], observed=True):
        if len(g) >= 50:
            cell_count += 1
        else:
            low_n_count += 1
    add_topic_row(rows, "m3_p3_simulation_validation", "usable_mass_redshift_target_vector_cells", "broad_mass_z3_sn_ge_3_n_ge_50", cell_count, cell_count + low_n_count, cell_count, None, "Observed SDSS target-vector cells only; no simulation comparison.")
    return rows


def paper_table_candidates(topic_rows: list[dict[str, Any]], reg_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for topic in TOPIC_LABELS:
        candidates = [r for r in topic_rows if r.get("topic") == topic]
        # Keep deterministic, concise table candidates: S/N>=3 rows first, then all others.
        selected = []
        for r in candidates:
            variant = str(r.get("variant", ""))
            if "sn_ge_3" in variant or topic in {"m2_p3_feedback_transition_mass", "m3_p3_simulation_validation"}:
                selected.append(r)
        selected = selected[:8]
        for rank, r in enumerate(selected, start=1):
            rows.append({
                "paper_topic": topic,
                "paper_title": TOPIC_LABELS[topic],
                "candidate_rank": rank,
                "metric": r.get("metric"),
                "variant": r.get("variant"),
                "n": r.get("n"),
                "k": r.get("k"),
                "value": r.get("value"),
                "ci95_low": r.get("ci95_low"),
                "ci95_high": r.get("ci95_high"),
                "table_note": r.get("note"),
                "proxy_guard": PROXY_GUARD,
            })
    # Add one regression candidate per topic where available.
    for topic in TOPIC_LABELS:
        regs = [r for r in reg_rows if r.get("topic") == topic and r.get("coef_interest") is not None and int(r.get("sn_min_ge", 99)) == 3]
        if regs:
            r = regs[0]
            rows.append({
                "paper_topic": topic,
                "paper_title": TOPIC_LABELS[topic],
                "candidate_rank": "regression_sensitivity",
                "metric": f"{r.get('model_family')} coefficient: {r.get('outcome')}",
                "variant": r.get("variant"),
                "n": r.get("n_regression"),
                "k": r.get("n_interest_positive"),
                "value": r.get("coef_interest"),
                "ci95_low": r.get("ci95_low"),
                "ci95_high": r.get("ci95_high"),
                "table_note": r.get("coefficient_interpretation"),
                "proxy_guard": PROXY_GUARD,
            })
    return rows


def make_coefficient_figure(reg_rows: list[dict[str, Any]], out_dir: Path, ts: str) -> dict[str, str]:
    assert_goru_write(out_dir / "dummy")
    out_dir.mkdir(parents=True, exist_ok=True)
    selected_variants = [
        ("m1_rp1_agn_sfr", "bpt_agn_vs_sf", "RP1: AGN sSFR coef"),
        ("m1_rp2_environment_quenching", "high_density_k10", "RP2: high density quench coef"),
        ("m2_p2_radio_jet_environment", "mass_ge_10.8_high_density_k10", "M2P2: massive high-density AGN coef"),
        ("m2_p3_feedback_transition_mass", "logM_trend", "M2P3: logM quench coef"),
        ("m3_p2_gas_depletion_efficiency", "mass_ge_10.8_transition_quenched", "M3P2: Halpha proxy coef"),
    ]
    fig, axes = plt.subplots(len(selected_variants), 1, figsize=(7.2, 9.2), sharex=True)
    if len(selected_variants) == 1:
        axes = [axes]
    for ax, (topic, needle, title) in zip(axes, selected_variants):
        plot_rows = [r for r in reg_rows if r.get("topic") == topic and needle in str(r.get("variant")) and r.get("coef_interest") is not None]
        plot_rows = sorted(plot_rows, key=lambda r: int(r.get("sn_min_ge", 0)))
        if not plot_rows:
            ax.text(0.5, 0.5, "no valid fit", transform=ax.transAxes, ha="center")
            ax.set_title(title, fontsize=9)
            continue
        xs = [int(r["sn_min_ge"]) for r in plot_rows]
        ys = [float(r["coef_interest"]) for r in plot_rows]
        lo = [float(r["coef_interest"]) - float(r["ci95_low"]) for r in plot_rows]
        hi = [float(r["ci95_high"]) - float(r["coef_interest"]) for r in plot_rows]
        ax.errorbar(xs, ys, yerr=[lo, hi], fmt="o-", capsize=3, lw=1.2)
        ax.axhline(0, color="0.45", lw=0.8, ls="--")
        ax.set_title(title, fontsize=9)
        ax.set_ylabel("coef")
        ax.grid(alpha=0.2)
    axes[-1].set_xlabel("minimum S/N in all four BPT lines")
    fig.suptitle("Regression/LPM sensitivity across S/N cuts (proxy quantities)", y=0.995, fontsize=11)
    fig.tight_layout()
    png = out_dir / f"regression_coefficient_sensitivity_{ts}.png"
    pdf = out_dir / f"regression_coefficient_sensitivity_{ts}.pdf"
    fig.savefig(png, dpi=220)
    fig.savefig(pdf)
    plt.close(fig)
    return {"regression_coefficient_sensitivity_png": str(png), "regression_coefficient_sensitivity_pdf": str(pdf)}


def output_inventory(paths: dict[str, Path], fig_paths: dict[str, str], ts: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    merged: dict[str, str] = {k: str(v) for k, v in paths.items()}
    merged.update(fig_paths)
    for label, path_str in sorted(merged.items()):
        path = Path(path_str)
        rows.append({
            "timestamp_utc": ts,
            "label": label,
            "path": str(path),
            "exists": path.exists(),
            "bytes": int(path.stat().st_size) if path.exists() else None,
            "sha256": sha256_path(path) if path.exists() and path.is_file() else None,
            "guard": "Goru lane-local artifact inventory for this tick.",
        })
    return rows


def main() -> int:
    ts = utc_ts()
    marker = f"{MARKER_BASE}_{ts}"
    tables_dir = GORU_ROOT / "tables"
    artifacts_dir = GORU_ROOT / "artifacts"
    ticks_dir = GORU_ROOT / "ticks"
    figures_dir = GORU_ROOT / "figures"
    for d in (tables_dir, artifacts_dir, ticks_dir, figures_dir):
        assert_goru_write(d / "dummy")
        d.mkdir(parents=True, exist_ok=True)

    df = load_sample()
    source_results = {}
    if SOURCE_RESULTS.exists():
        with SOURCE_RESULTS.open("r", encoding="utf-8") as f:
            source_results = json.load(f)

    reg = regression_rows(df)
    alt_bins = alternate_bin_rows(df)
    topic_rows = topic_bootstrap_rows(df)
    candidates = paper_table_candidates(topic_rows, reg)

    paths = {
        "regression_sensitivity_csv": tables_dir / f"regression_lpm_sensitivity_{ts}.csv",
        "alternate_bin_target_vector_csv": tables_dir / f"alternate_mass_redshift_sn_target_vector_{ts}.csv",
        "topic_bootstrap_summary_csv": tables_dir / f"topic_bootstrap_summary_{ts}.csv",
        "paper_table_candidates_csv": tables_dir / f"paper_table_candidate_rows_{ts}.csv",
        "inventory_csv": tables_dir / f"goru_tick_output_inventory_{ts}.csv",
        "summary_json": artifacts_dir / f"goru_regression_bin_sensitivity_{ts}.json",
        "tick_report_md": ticks_dir / f"GORU_TICK_{ts}.md",
    }
    for p in paths.values():
        assert_goru_write(p)

    write_csv(paths["regression_sensitivity_csv"], reg)
    write_csv(paths["alternate_bin_target_vector_csv"], alt_bins)
    write_csv(paths["topic_bootstrap_summary_csv"], topic_rows)
    write_csv(paths["paper_table_candidates_csv"], candidates)
    fig_paths = make_coefficient_figure(reg, figures_dir, ts)
    inventory = output_inventory({k: v for k, v in paths.items() if k != "inventory_csv"}, fig_paths, ts)
    write_csv(paths["inventory_csv"], inventory)

    key_lookup = {(r.get("topic"), r.get("variant"), r.get("metric")): r for r in topic_rows}
    rp1 = key_lookup[("m1_rp1_agn_sfr", "bpt_agn_vs_sf_sn_ge_3", "matched_median_delta_log_sSFR_target_minus_sf")]
    rp2 = key_lookup[("m1_rp2_environment_quenching", "k10_sn_ge_3", "high_minus_low_density_quenched_fraction")]
    m2p2 = key_lookup[("m2_p2_radio_jet_environment", "mass_ge_10.8_k10_sn_ge_3", "massive_high_minus_low_density_bpt_agn_fraction")]
    m3p3 = next(r for r in topic_rows if r.get("topic") == "m3_p3_simulation_validation")
    sn_counts = {f"sn_ge_{sn}": int((df["sn_min"] >= sn).sum()) for sn in SN_THRESHOLDS}

    outputs = {k: str(v) for k, v in paths.items()}
    outputs.update(fig_paths)
    summary = {
        "marker": marker,
        "timestamp_utc": ts,
        "source_csv": str(SOURCE_CSV),
        "source_rows": int(len(df)),
        "source_results_analysis_rows": source_results.get("analysis_rows"),
        "source_results_bpt_counts": source_results.get("bpt_counts"),
        "sn_threshold_counts": sn_counts,
        "row_counts": {
            "regression_sensitivity": len(reg),
            "alternate_bin_target_vector": len(alt_bins),
            "topic_bootstrap_summary": len(topic_rows),
            "paper_table_candidates": len(candidates),
            "inventory": len(inventory),
        },
        "key_results": {
            "rp1_sn3_matched_delta_log_sSFR": rp1,
            "rp2_k10_sn3_high_minus_low_quenched_fraction": rp2,
            "m2p2_k10_massive_sn3_high_minus_low_bpt_agn_fraction": m2p2,
            "m3p3_usable_target_vector_cells": m3p3,
        },
        "outputs": outputs,
        "proxy_limits": PROXY_GUARD,
        "safety": "Read cached SDSS/local artifacts only; wrote under lanes/goru only. No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission.",
    }
    paths["summary_json"].write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    report = f"""# Goru regression/bin sensitivity tick — {ts}

Marker: `{marker}`

## Work completed

- Read cached SDSS DR17-derived sample only (`analysis_sample_bpt.csv`, {len(df):,} rows) plus local source summary metadata; no network, DB, API, deploy, git, cron, billing, OAuth, or external submission action.
- Generated lane-local regression/LPM robustness coefficients with HC1 standard errors for optical-class sSFR offsets, density/quenching proxies, massive-host optical-AGN density sensitivity, transition-mass trends, and H-alpha proxy checks.
- Generated alternate mass/redshift/S/N target-vector grids, bootstrap topic summaries, 9-paper table-candidate rows, a coefficient-sensitivity figure, and a per-output inventory with hashes.

## Key mechanical results

- Cached sample S/N counts: S/N>=3 = {sn_counts['sn_ge_3']:,}; S/N>=5 = {sn_counts['sn_ge_5']:,}; S/N>=10 = {sn_counts['sn_ge_10']:,}.
- RP-1 matched BPT-AGN minus star-forming median log-sSFR offset at S/N>=3: {float(rp1['value']):.3f} dex (CI {float(rp1['ci95_low']):.3f}, {float(rp1['ci95_high']):.3f}; matched pairs {int(rp1['n']):,}).
- RP-2 k=10 density proxy high-minus-low quenched-fraction difference at S/N>=3: {float(rp2['value']):.3f} (CI {float(rp2['ci95_low']):.3f}, {float(rp2['ci95_high']):.3f}).
- M2 P2 massive-host k=10 high-minus-low optical-AGN fraction at S/N>=3: {float(m2p2['value']):.3f} (CI {float(m2p2['ci95_low']):.3f}, {float(m2p2['ci95_high']):.3f}).
- M3 P3 usable broad mass-redshift target-vector cells at S/N>=3 and n>=50: {int(m3p3['value'])}.

## Output artifacts

- summary_json: `{paths['summary_json']}`
- tick_report_md: `{paths['tick_report_md']}`
- regression_sensitivity_csv: `{paths['regression_sensitivity_csv']}`
- alternate_bin_target_vector_csv: `{paths['alternate_bin_target_vector_csv']}`
- topic_bootstrap_summary_csv: `{paths['topic_bootstrap_summary_csv']}`
- paper_table_candidates_csv: `{paths['paper_table_candidates_csv']}`
- inventory_csv: `{paths['inventory_csv']}`
- coefficient_figure: `{fig_paths.get('regression_coefficient_sensitivity_png')}`

## Safety / interpretation guard

{PROXY_GUARD}

No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission changes. Lane-local writes only, with the separate required concise append to `OVERNIGHT_LEDGER.md` to be performed after verification.
"""
    paths["tick_report_md"].write_text(report, encoding="utf-8")
    print(json.dumps({
        "marker": marker,
        "summary_json": str(paths["summary_json"]),
        "tick_report_md": str(paths["tick_report_md"]),
        "row_counts": summary["row_counts"],
        "key_values": {
            "rp1_sn3_delta": rp1["value"],
            "rp2_k10_diff": rp2["value"],
            "m2p2_k10_diff": m2p2["value"],
            "m3p3_cells": m3p3["value"],
        },
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
