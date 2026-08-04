#!/usr/bin/env python3
"""Goru mechanical robustness tick for the NebulaMind overnight 9-paper swarm.

Read-only inputs: cached SDSS-derived CSV/JSON/PDF artifacts under aas-autopilot.
Writes: lane-local Goru artifacts only. The overnight ledger is appended separately
by Hermes after this script succeeds.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

TS = "20260708T141459Z"
REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
OVERNIGHT = AUTOPILOT / "overnight-9-papers-20260708"
LANE = OVERNIGHT / "lanes/goru"
SOURCE_RUN = AUTOPILOT / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
SOURCE_CSV = SOURCE_RUN / "data/analysis_sample_bpt.csv"
SOURCE_RESULTS = SOURCE_RUN / "analysis_results.json"
BATCH_RUN = AUTOPILOT / "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
BATCH_MANIFEST = BATCH_RUN / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json"

TABLE_DIR = LANE / "tables"
ARTIFACT_DIR = LANE / "artifacts"
TICK_DIR = LANE / "ticks"
for directory in (TABLE_DIR, ARTIFACT_DIR, TICK_DIR, LANE / "scripts"):
    directory.mkdir(parents=True, exist_ok=True)

SAMPLE_COUNTS_CSV = TABLE_DIR / f"sample_counts_by_cut_{TS}.csv"
BPT_SENSITIVITY_CSV = TABLE_DIR / f"bpt_sensitivity_{TS}.csv"
SN_Z_MASS_CSV = TABLE_DIR / f"sn_redshift_mass_bins_{TS}.csv"
MATCHED_CSV = TABLE_DIR / f"matched_sfr_offset_robustness_{TS}.csv"
TOPIC_METRICS_CSV = TABLE_DIR / f"topic_metric_robustness_{TS}.csv"
TARGET_VECTOR_CSV = TABLE_DIR / f"simulation_target_vector_cells_{TS}.csv"
INVENTORY_CSV = TABLE_DIR / f"figure_table_inventory_{TS}.csv"
SUMMARY_JSON = ARTIFACT_DIR / f"goru_actual_data_robustness_{TS}.json"
REPORT_MD = TICK_DIR / f"GORU_TICK_{TS}.md"

C_KM_S = 299792.458
H0 = 70.0
MASS_BINS = [8.0, 9.5, 10.0, 10.5, 11.0, 12.5]
MASS_LABELS = ["8.0-9.5", "9.5-10.0", "10.0-10.5", "10.5-11.0", "11.0-12.5"]
Z_BINS = [0.02, 0.05, 0.08, 0.12]
Z_LABELS = ["0.02-0.05", "0.05-0.08", "0.08-0.12"]
SN_THRESHOLDS = [3.0, 5.0, 10.0]

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


def assert_lane_write(path: Path) -> None:
    """Protect the single-writer rule for this cron lane."""
    resolved = path.resolve()
    lane_resolved = LANE.resolve()
    if lane_resolved not in [resolved, *resolved.parents]:
        raise RuntimeError(f"Refusing non-Goru-lane write: {resolved}")


for output_path in [
    SAMPLE_COUNTS_CSV,
    BPT_SENSITIVITY_CSV,
    SN_Z_MASS_CSV,
    MATCHED_CSV,
    TOPIC_METRICS_CSV,
    TARGET_VECTOR_CSV,
    INVENTORY_CSV,
    SUMMARY_JSON,
    REPORT_MD,
]:
    assert_lane_write(output_path)


def safe_float(value: Any) -> float | None:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(out):
        return None
    return out


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: Iterable[str] | None = None) -> None:
    assert_lane_write(path)
    if fieldnames is None:
        keys: list[str] = []
        seen = set()
        for row in rows:
            for key in row:
                if key not in seen:
                    seen.add(key)
                    keys.append(key)
        fieldnames = keys
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def load_json(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        return json.load(handle)


def bpt_demarcations(x: pd.Series | np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    arr = np.asarray(x, dtype=float)
    kauffmann = 0.61 / (arr - 0.05) + 1.30
    kewley = 0.61 / (arr - 0.47) + 1.19
    return kauffmann, kewley


def add_density_proxy(df: pd.DataFrame, k: int) -> None:
    ra = np.deg2rad(df["ra"].to_numpy(dtype=float))
    dec = np.deg2rad(df["dec"].to_numpy(dtype=float))
    dist = (C_KM_S / H0) * df["z"].to_numpy(dtype=float)
    xyz = np.column_stack(
        [
            dist * np.cos(dec) * np.cos(ra),
            dist * np.cos(dec) * np.sin(ra),
            dist * np.sin(dec),
        ]
    )
    tree = cKDTree(xyz)
    dists, _ = tree.query(xyz, k=k + 1)  # first neighbor is self
    kth = np.maximum(dists[:, -1], 1e-6)
    density = k / ((4.0 / 3.0) * math.pi * kth**3)
    log_density = np.log10(density)
    df[f"log_density_k{k}"] = log_density
    df[f"density_q_k{k}"] = pd.qcut(
        log_density, 4, labels=["Q1 low", "Q2", "Q3", "Q4 high"], duplicates="drop"
    ).astype(str)
    df[f"low_density_k{k}"] = df[f"density_q_k{k}"] == "Q1 low"
    df[f"high_density_k{k}"] = df[f"density_q_k{k}"] == "Q4 high"


def load_and_prepare() -> pd.DataFrame:
    if not SOURCE_CSV.exists():
        raise SystemExit(f"Missing source CSV: {SOURCE_CSV}")
    required = {
        "specObjID",
        "ra",
        "dec",
        "z",
        "lgm_tot_p50",
        "specsfr_tot_p50",
        "modelMag_u",
        "modelMag_r",
        "h_alpha_flux",
        "h_alpha_flux_err",
        "h_beta_flux",
        "h_beta_flux_err",
        "oiii_5007_flux",
        "oiii_5007_flux_err",
        "nii_6584_flux",
        "nii_6584_flux_err",
        "bpt_label",
        "log_nii_ha",
        "log_oiii_hb",
        "u_minus_r",
    }
    df = pd.read_csv(SOURCE_CSV)
    missing = sorted(required - set(df.columns))
    if missing:
        raise SystemExit(f"Source CSV missing columns: {missing}")

    for col in required - {"specObjID", "bpt_label"}:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=sorted(required - {"specObjID", "bpt_label"}))

    df["sn_ha_recalc"] = df["h_alpha_flux"] / df["h_alpha_flux_err"]
    df["sn_hb_recalc"] = df["h_beta_flux"] / df["h_beta_flux_err"]
    df["sn_oiii_recalc"] = df["oiii_5007_flux"] / df["oiii_5007_flux_err"]
    df["sn_nii_recalc"] = df["nii_6584_flux"] / df["nii_6584_flux_err"]
    df["sn_min_bpt"] = df[["sn_ha_recalc", "sn_hb_recalc", "sn_oiii_recalc", "sn_nii_recalc"]].min(axis=1)
    df["log_nii_ha_recalc"] = np.log10(df["nii_6584_flux"] / df["h_alpha_flux"])
    df["log_oiii_hb_recalc"] = np.log10(df["oiii_5007_flux"] / df["h_beta_flux"])
    kauffmann, kewley = bpt_demarcations(df["log_nii_ha_recalc"])
    finite_ratio = np.isfinite(df["log_nii_ha_recalc"]) & np.isfinite(df["log_oiii_hb_recalc"])
    safe_x = df["log_nii_ha_recalc"] <= 0.35
    y = df["log_oiii_hb_recalc"].to_numpy(dtype=float)
    df["bpt_sf_recalc"] = finite_ratio & safe_x & (y < kauffmann)
    df["bpt_agn_recalc"] = finite_ratio & safe_x & (y > kewley)
    df["bpt_intermediate_recalc"] = finite_ratio & safe_x & (y >= kauffmann) & (y <= kewley)
    df["bpt_inclusive_non_sf"] = df["bpt_intermediate_recalc"] | df["bpt_agn_recalc"]
    df["bpt_sf_base"] = df["bpt_label"] == "star-forming"
    df["bpt_agn_base"] = df["bpt_label"] == "agn"
    df["bpt_intermediate_base"] = df["bpt_label"] == "intermediate"
    df["bpt_inclusive_non_sf_base"] = df["bpt_label"].isin(["intermediate", "agn"])
    df["high_excitation_agn"] = df["bpt_agn_recalc"] & (df["log_oiii_hb_recalc"] > 0.25)
    df["high_nii"] = df["log_nii_ha_recalc"] > -0.20
    df["high_oiii"] = df["log_oiii_hb_recalc"] > 0.00
    df["quenched"] = df["specsfr_tot_p50"] < -11.0
    df["transition_or_quenched"] = df["specsfr_tot_p50"] < -10.7
    df["massive_10p8"] = df["lgm_tot_p50"] >= 10.8
    df["red_sequence"] = df["u_minus_r"] > 2.2
    df["mass_bin"] = pd.cut(df["lgm_tot_p50"], MASS_BINS, labels=MASS_LABELS, include_lowest=True).astype(str)
    df["z_bin"] = pd.cut(df["z"], Z_BINS, labels=Z_LABELS, include_lowest=True).astype(str)
    dl_mpc = (C_KM_S / H0) * df["z"] * (1.0 + df["z"])
    cm_per_mpc = 3.0856775814913673e24
    flux = df["h_alpha_flux"].clip(lower=1e-12) * 1e-17
    lum = 4.0 * math.pi * (dl_mpc * cm_per_mpc) ** 2 * flux
    df["log_lha_proxy"] = np.log10(lum)
    for k in (5, 10, 20):
        add_density_proxy(df, k)
    return df


def binomial_se(p: float, n: int) -> float | None:
    if n <= 0 or not math.isfinite(p):
        return None
    return math.sqrt(max(p * (1.0 - p), 0.0) / n)


def fraction(mask: pd.Series | np.ndarray) -> dict[str, Any]:
    vals = pd.Series(mask).dropna().astype(bool)
    n = int(len(vals))
    k = int(vals.sum())
    p = k / n if n else float("nan")
    return {"n": n, "k": k, "fraction": safe_float(p), "se": safe_float(binomial_se(p, n) if n else None)}


def bootstrap_ci(values: np.ndarray, func=np.nanmedian, n_boot: int = 1000, seed: int = 20260708) -> list[float | None]:
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if len(values) == 0:
        return [None, None]
    rng = np.random.default_rng(seed)
    draws = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        sample = values[rng.integers(0, len(values), len(values))]
        draws[i] = func(sample)
    return [safe_float(np.percentile(draws, 2.5)), safe_float(np.percentile(draws, 97.5))]


def bootstrap_fraction_diff_ci(a: np.ndarray, b: np.ndarray, n_boot: int = 1000, seed: int = 20260708) -> list[float | None]:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    a = a[np.isfinite(a)]
    b = b[np.isfinite(b)]
    if len(a) == 0 or len(b) == 0:
        return [None, None]
    rng = np.random.default_rng(seed)
    draws = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        aa = a[rng.integers(0, len(a), len(a))]
        bb = b[rng.integers(0, len(b), len(b))]
        draws[i] = np.nanmean(aa) - np.nanmean(bb)
    return [safe_float(np.percentile(draws, 2.5)), safe_float(np.percentile(draws, 97.5))]


def sample_counts_rows(df: pd.DataFrame) -> list[dict[str, Any]]:
    rows = []
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min_bpt"] >= sn]
        counts = sub["bpt_label"].value_counts().to_dict()
        rec = {
            "sn_min_cut": sn,
            "n": int(len(sub)),
            "n_star_forming": int(counts.get("star-forming", 0)),
            "n_intermediate": int(counts.get("intermediate", 0)),
            "n_agn": int(counts.get("agn", 0)),
            "n_unclassified": int(counts.get("unclassified", 0)),
            "quenched_fraction": safe_float(sub["quenched"].mean()),
            "transition_or_quenched_fraction": safe_float(sub["transition_or_quenched"].mean()),
            "agn_fraction": safe_float(sub["bpt_agn_base"].mean()),
            "high_excitation_agn_fraction": safe_float(sub["high_excitation_agn"].mean()),
            "median_z": safe_float(sub["z"].median()),
            "median_logM": safe_float(sub["lgm_tot_p50"].median()),
            "median_log_sSFR": safe_float(sub["specsfr_tot_p50"].median()),
            "median_sn_min_bpt": safe_float(sub["sn_min_bpt"].median()),
        }
        rows.append(rec)
    return rows


def bpt_sensitivity_rows(df: pd.DataFrame) -> list[dict[str, Any]]:
    definitions = [
        ("baseline_star_forming", "BPT below Kauffmann+03 curve", df["bpt_label"] == "star-forming"),
        ("recomputed_star_forming", "Recomputed BPT below Kauffmann+03 curve", df["bpt_sf_recalc"]),
        ("baseline_intermediate", "Between Kauffmann+03 and Kewley+01", df["bpt_label"] == "intermediate"),
        ("baseline_agn", "BPT above Kewley+01 curve", df["bpt_label"] == "agn"),
        ("recomputed_agn", "Recomputed BPT above Kewley+01 curve", df["bpt_agn_recalc"]),
        ("inclusive_intermediate_plus_agn", "Composite/intermediate plus AGN; not a pure AGN class", df["bpt_inclusive_non_sf"]),
        ("high_excitation_agn", "Recomputed AGN with log([OIII]/Hb)>0.25", df["high_excitation_agn"]),
        ("high_nii", "log([NII]/Halpha)>-0.20 optical tracer proxy", df["high_nii"]),
        ("high_oiii", "log([OIII]/Hbeta)>0.00 optical tracer proxy", df["high_oiii"]),
        ("red_sequence", "u-r>2.2 optical colour proxy", df["red_sequence"]),
        ("low_sSFR_quenched", "specsfr_tot_p50<-11.0", df["quenched"]),
    ]
    rows: list[dict[str, Any]] = []
    for sn in SN_THRESHOLDS:
        sn_mask = df["sn_min_bpt"] >= sn
        denom = int(sn_mask.sum())
        for name, note, mask in definitions:
            vals = mask[sn_mask]
            k = int(vals.sum())
            p = k / denom if denom else float("nan")
            rows.append(
                {
                    "sn_min_cut": sn,
                    "definition": name,
                    "denominator_n": denom,
                    "selected_k": k,
                    "fraction": safe_float(p),
                    "binomial_se": safe_float(binomial_se(p, denom) if denom else None),
                    "note": note,
                }
            )
    return rows


def sn_z_mass_rows(df: pd.DataFrame) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min_bpt"] >= sn].copy()
        grouped = sub.groupby(["z_bin", "mass_bin"], observed=True)
        for (zbin, mbin), g in grouped:
            if str(zbin) == "nan" or str(mbin) == "nan":
                continue
            n = int(len(g))
            rows.append(
                {
                    "sn_min_cut": sn,
                    "z_bin": str(zbin),
                    "mass_bin": str(mbin),
                    "n": n,
                    "n_star_forming": int((g["bpt_label"] == "star-forming").sum()),
                    "n_intermediate": int((g["bpt_label"] == "intermediate").sum()),
                    "n_agn": int((g["bpt_label"] == "agn").sum()),
                    "quenched_fraction": safe_float(g["quenched"].mean()),
                    "agn_fraction": safe_float(g["bpt_agn_base"].mean()),
                    "high_excitation_agn_fraction": safe_float(g["high_excitation_agn"].mean()),
                    "median_log_sSFR": safe_float(g["specsfr_tot_p50"].median()),
                    "median_u_minus_r": safe_float(g["u_minus_r"].median()),
                    "proxy_limit": "SDSS emission-line selected denominator; no gas/radio/X-ray causal feedback measurement.",
                }
            )
    return rows


def matched_offset(
    df: pd.DataFrame,
    target_mask: pd.Series,
    control_mask: pd.Series,
    variant: str,
    min_n: int = 30,
) -> dict[str, Any]:
    target = df[target_mask].copy()
    control = df[control_mask].copy()
    row: dict[str, Any] = {
        "topic": "m1_rp1_agn_sfr",
        "variant": variant,
        "target_n": int(len(target)),
        "control_n": int(len(control)),
        "median_delta_log_sSFR": None,
        "median_ci95_low": None,
        "median_ci95_high": None,
        "mean_delta_log_sSFR": None,
        "mean_ci95_low": None,
        "mean_ci95_high": None,
        "match_abs_delta_logM_median": None,
        "match_abs_delta_z_median": None,
        "match_distance_scaled_median": None,
        "proxy_limit": "Association of optical BPT class with sSFR; not causal AGN feedback proof.",
    }
    if len(target) < min_n or len(control) < min_n:
        row["proxy_limit"] += f" Insufficient target/control rows for robust matching at min_n={min_n}."
        return row
    features = ["lgm_tot_p50", "z"]
    scale = control[features].std().replace(0, 1.0)
    center = control[features].mean()
    control_scaled = (control[features] - center) / scale
    target_scaled = (target[features] - center) / scale
    tree = cKDTree(control_scaled.to_numpy(dtype=float))
    dist, idx = tree.query(target_scaled.to_numpy(dtype=float), k=1)
    matched_control = control.iloc[idx].reset_index(drop=True)
    target2 = target.reset_index(drop=True)
    delta = target2["specsfr_tot_p50"].to_numpy(dtype=float) - matched_control["specsfr_tot_p50"].to_numpy(dtype=float)
    med_ci = bootstrap_ci(delta, np.nanmedian)
    mean_ci = bootstrap_ci(delta, np.nanmean)
    row.update(
        {
            "median_delta_log_sSFR": safe_float(np.nanmedian(delta)),
            "median_ci95_low": med_ci[0],
            "median_ci95_high": med_ci[1],
            "mean_delta_log_sSFR": safe_float(np.nanmean(delta)),
            "mean_ci95_low": mean_ci[0],
            "mean_ci95_high": mean_ci[1],
            "match_abs_delta_logM_median": safe_float(np.nanmedian(np.abs(target2["lgm_tot_p50"] - matched_control["lgm_tot_p50"]))),
            "match_abs_delta_z_median": safe_float(np.nanmedian(np.abs(target2["z"] - matched_control["z"]))),
            "match_distance_scaled_median": safe_float(np.nanmedian(dist)),
        }
    )
    return row


def matched_rows(df: pd.DataFrame) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min_bpt"] >= sn]
        rows.append(matched_offset(sub, sub["bpt_agn_base"], sub["bpt_sf_base"], f"sn_ge_{sn:g}_baseline_agn_vs_sf"))
    base = df[df["sn_min_bpt"] >= 3.0]
    rows.append(
        matched_offset(
            base,
            base["high_excitation_agn"],
            base["bpt_sf_base"],
            "sn_ge_3_high_excitation_agn_vs_sf",
        )
    )
    rows.append(
        matched_offset(
            base,
            base["bpt_inclusive_non_sf_base"],
            base["bpt_sf_base"],
            "sn_ge_3_inclusive_intermediate_plus_agn_vs_sf_proxy",
        )
    )
    for label in Z_LABELS:
        sub = base[base["z_bin"] == label]
        rows.append(matched_offset(sub, sub["bpt_agn_base"], sub["bpt_sf_base"], f"z_bin_{label}_baseline_agn_vs_sf"))
    for label in MASS_LABELS:
        sub = base[base["mass_bin"] == label]
        rows.append(matched_offset(sub, sub["bpt_agn_base"], sub["bpt_sf_base"], f"mass_bin_{label}_baseline_agn_vs_sf"))
    return rows


def add_metric_row(
    rows: list[dict[str, Any]],
    topic: str,
    variant: str,
    metric: str,
    denominator_n: int | None,
    numerator_k: int | None,
    value: Any,
    se: Any = None,
    ci: list[Any] | None = None,
    note: str = "",
) -> None:
    ci = ci or [None, None]
    rows.append(
        {
            "topic": topic,
            "topic_label": TOPIC_LABELS.get(topic, topic),
            "variant": variant,
            "metric": metric,
            "denominator_n": denominator_n,
            "numerator_k": numerator_k,
            "value": value,
            "se": se,
            "ci95_low": ci[0],
            "ci95_high": ci[1],
            "proxy_limit": note,
        }
    )


def topic_metric_rows(df: pd.DataFrame, matched: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    # M1 RP-1: harvest matched-control robustness rows into the shared topic table.
    for rec in matched:
        add_metric_row(
            rows,
            "m1_rp1_agn_sfr",
            rec["variant"],
            "median_matched_delta_log_sSFR_agn_minus_control",
            rec["target_n"],
            rec["target_n"],
            rec["median_delta_log_sSFR"],
            None,
            [rec["median_ci95_low"], rec["median_ci95_high"]],
            rec["proxy_limit"],
        )

    base = df[df["sn_min_bpt"] >= 3.0]

    # M1 RP-2: density proxy / quenching robustness.
    for k in (5, 10, 20):
        low = base[base[f"low_density_k{k}"]]
        high = base[base[f"high_density_k{k}"]]
        low_f = fraction(low["quenched"])
        high_f = fraction(high["quenched"])
        ci = bootstrap_fraction_diff_ci(high["quenched"].astype(float).to_numpy(), low["quenched"].astype(float).to_numpy())
        add_metric_row(
            rows,
            "m1_rp2_environment_quenching",
            f"knn_density_k{k}_sn_ge_3",
            "high_minus_low_quenched_fraction",
            int(len(high) + len(low)),
            None,
            safe_float(float(high_f["fraction"]) - float(low_f["fraction"])),
            None,
            ci,
            f"High-minus-low quartile quenched-fraction difference using k={k} density proxy; group/halo labels absent.",
        )
        add_metric_row(rows, "m1_rp2_environment_quenching", f"knn_density_k{k}_sn_ge_3_high", "high_density_quenched_fraction", high_f["n"], high_f["k"], high_f["fraction"], high_f["se"], None, "Density proxy only; not halo mass or central/satellite classification.")
        add_metric_row(rows, "m1_rp2_environment_quenching", f"knn_density_k{k}_sn_ge_3_low", "low_density_quenched_fraction", low_f["n"], low_f["k"], low_f["fraction"], low_f["se"], None, "Density proxy only; not halo mass or central/satellite classification.")
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min_bpt"] >= sn]
        low = sub[sub["low_density_k10"]]
        high = sub[sub["high_density_k10"]]
        ci = bootstrap_fraction_diff_ci(high["quenched"].astype(float).to_numpy(), low["quenched"].astype(float).to_numpy())
        add_metric_row(rows, "m1_rp2_environment_quenching", f"knn_density_k10_sn_ge_{sn:g}", "high_minus_low_quenched_fraction", int(len(high) + len(low)), None, safe_float(high["quenched"].mean() - low["quenched"].mean()), None, ci, "S/N robustness for density proxy only; no group catalogue.")

    # M1 RP-3: massive low-sSFR optical AGN denominator.
    for mass_cut in (10.6, 10.8, 11.0):
        massive = base[base["lgm_tot_p50"] >= mass_cut]
        massive_q = massive[massive["quenched"]]
        f_massive = fraction(massive["bpt_agn_base"])
        f_massive_q = fraction(massive_q["bpt_agn_base"])
        add_metric_row(rows, "m1_rp3_maintenance_heating", f"mass_ge_{mass_cut}", "optical_agn_fraction_massive", f_massive["n"], f_massive["k"], f_massive["fraction"], f_massive["se"], None, "Optical AGN denominator only; no X-ray cavity/radio heating measurement.")
        add_metric_row(rows, "m1_rp3_maintenance_heating", f"mass_ge_{mass_cut}", "optical_agn_fraction_massive_quenched", f_massive_q["n"], f_massive_q["k"], f_massive_q["fraction"], f_massive_q["se"], None, "Optical AGN denominator only; no X-ray cavity/radio heating measurement.")

    # M2 P1: high-excitation optical AGN denominator by S/N and redshift.
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min_bpt"] >= sn]
        f = fraction(sub["high_excitation_agn"])
        add_metric_row(rows, "m2_p1_outflow_escape_recycling", f"sn_ge_{sn:g}", "high_excitation_agn_fraction", f["n"], f["k"], f["fraction"], f["se"], None, "Denominator for resolved outflow follow-up; no velocity/escape/recycling measurement.")
    for zbin in Z_LABELS:
        sub = base[base["z_bin"] == zbin]
        f = fraction(sub["high_excitation_agn"])
        add_metric_row(rows, "m2_p1_outflow_escape_recycling", f"z_bin_{zbin}", "high_excitation_agn_fraction", f["n"], f["k"], f["fraction"], f["se"], None, "Redshift-bin denominator only; no multiphase kinematics.")

    # M2 P2: massive-host optical AGN fraction by density proxy.
    for k in (5, 10, 20):
        massive = base[base["massive_10p8"]]
        low = massive[massive[f"low_density_k{k}"]]
        high = massive[massive[f"high_density_k{k}"]]
        low_f = fraction(low["bpt_agn_base"])
        high_f = fraction(high["bpt_agn_base"])
        ci = bootstrap_fraction_diff_ci(high["bpt_agn_base"].astype(float).to_numpy(), low["bpt_agn_base"].astype(float).to_numpy())
        add_metric_row(rows, "m2_p2_radio_jet_environment", f"mass_ge_10.8_knn_k{k}", "high_minus_low_density_optical_agn_fraction", int(len(high) + len(low)), None, safe_float(high["bpt_agn_base"].mean() - low["bpt_agn_base"].mean()), None, ci, "Optical AGN/environment proxy only; no radio jet power/coupling measurement.")
        add_metric_row(rows, "m2_p2_radio_jet_environment", f"mass_ge_10.8_knn_k{k}_high", "high_density_massive_optical_agn_fraction", high_f["n"], high_f["k"], high_f["fraction"], high_f["se"], None, "Optical AGN/environment proxy only.")
        add_metric_row(rows, "m2_p2_radio_jet_environment", f"mass_ge_10.8_knn_k{k}_low", "low_density_massive_optical_agn_fraction", low_f["n"], low_f["k"], low_f["fraction"], low_f["se"], None, "Optical AGN/environment proxy only.")

    # M2 P3: mass trend / transition bins.
    for mb in MASS_LABELS:
        g = base[base["mass_bin"] == mb]
        if len(g) == 0:
            continue
        fq = fraction(g["quenched"])
        fa = fraction(g["bpt_agn_base"])
        add_metric_row(rows, "m2_p3_feedback_transition_mass", f"mass_bin_{mb}", "quenched_fraction", fq["n"], fq["k"], fq["fraction"], fq["se"], None, "Mass-transition optical diagnostic; no gas fractions/baryon deficits.")
        add_metric_row(rows, "m2_p3_feedback_transition_mass", f"mass_bin_{mb}", "optical_agn_fraction", fa["n"], fa["k"], fa["fraction"], fa["se"], None, "Mass-transition optical diagnostic; no gas fractions/baryon deficits.")

    # M3 P1: common-denominator optical tracer prevalence.
    tracer_defs = {
        "bpt_agn": base["bpt_agn_base"],
        "high_nii": base["high_nii"],
        "high_oiii": base["high_oiii"],
        "red_sequence": base["red_sequence"],
        "low_sSFR_quenched": base["quenched"],
    }
    for name, mask in tracer_defs.items():
        f = fraction(mask)
        add_metric_row(rows, "m3_p1_multiphase_census", f"sn_ge_3_{name}", "optical_tracer_prevalence", f["n"], f["k"], f["fraction"], f["se"], None, "Common SDSS optical denominator only; no molecular/neutral/X-ray/radio phases.")
    for sn in (5.0, 10.0):
        sub = df[df["sn_min_bpt"] >= sn]
        for name, mask in {
            "bpt_agn": sub["bpt_agn_base"],
            "high_nii": sub["high_nii"],
            "high_oiii": sub["high_oiii"],
            "red_sequence": sub["red_sequence"],
            "low_sSFR_quenched": sub["quenched"],
        }.items():
            f = fraction(mask)
            add_metric_row(rows, "m3_p1_multiphase_census", f"sn_ge_{sn:g}_{name}", "optical_tracer_prevalence", f["n"], f["k"], f["fraction"], f["se"], None, "S/N robustness in optical denominator only.")

    # M3 P2: gas-depletion follow-up denominator and optical H-alpha proxy.
    for mass_cut in (10.6, 10.8, 11.0):
        for ssfr_cut in (-10.7, -11.0):
            denom = base[(base["lgm_tot_p50"] >= mass_cut) & (base["specsfr_tot_p50"] < ssfr_cut)]
            f = fraction(denom["bpt_agn_base"])
            add_metric_row(rows, "m3_p2_gas_depletion_efficiency", f"mass_ge_{mass_cut}_ssfr_lt_{ssfr_cut}", "massive_transition_quenched_denominator_rows", int(len(base)), int(len(denom)), int(len(denom)), None, None, "CO/dust gas follow-up denominator; no molecular gas depletion or SFE measurement.")
            add_metric_row(rows, "m3_p2_gas_depletion_efficiency", f"mass_ge_{mass_cut}_ssfr_lt_{ssfr_cut}", "optical_agn_fraction_in_denominator", f["n"], f["k"], f["fraction"], f["se"], None, "CO/dust gas follow-up denominator; no molecular gas depletion or SFE measurement.")
            add_metric_row(rows, "m3_p2_gas_depletion_efficiency", f"mass_ge_{mass_cut}_ssfr_lt_{ssfr_cut}", "median_log_lha_proxy", int(len(denom)), None, safe_float(denom["log_lha_proxy"].median()), None, None, "H-alpha luminosity is an optical proxy, not a molecular gas mass.")

    return rows


def target_vector_rows(df: pd.DataFrame) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    base = df[df["sn_min_bpt"] >= 3.0]
    grouped = base.groupby(["mass_bin", "z_bin"], observed=True)
    for (mb, zb), g in grouped:
        if str(mb) == "nan" or str(zb) == "nan" or len(g) < 50:
            continue
        rows.append(
            {
                "topic": "m3_p3_simulation_validation",
                "mass_bin": str(mb),
                "z_bin": str(zb),
                "n": int(len(g)),
                "quenched_fraction": safe_float(g["quenched"].mean()),
                "optical_agn_fraction": safe_float(g["bpt_agn_base"].mean()),
                "high_excitation_agn_fraction": safe_float(g["high_excitation_agn"].mean()),
                "median_u_minus_r": safe_float(g["u_minus_r"].median()),
                "median_log_sSFR": safe_float(g["specsfr_tot_p50"].median()),
                "median_logM": safe_float(g["lgm_tot_p50"].median()),
                "median_log_density_k10": safe_float(g["log_density_k10"].median()),
                "proxy_limit": "Observed SDSS target vector only; no forward-modelled simulation comparison in this tick.",
            }
        )
    return rows


def inventory_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    first_topics = [
        {
            "slug": "m1_rp1_agn_sfr",
            "run_dir": SOURCE_RUN,
            "title": TOPIC_LABELS["m1_rp1_agn_sfr"],
        }
    ]
    topics = first_topics
    if BATCH_MANIFEST.exists():
        manifest = load_json(BATCH_MANIFEST)
        for item in manifest.get("topics", []):
            topics.append(
                {
                    "slug": item["slug"],
                    "run_dir": Path(item["pdf"]).parents[1],
                    "title": item.get("title", item["slug"]),
                }
            )
    for topic in topics:
        slug = topic["slug"]
        run_dir = Path(topic["run_dir"])
        for path in sorted(run_dir.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(run_dir)
            suffix = path.suffix.lower()
            if suffix in {".pdf", ".png", ".json", ".csv", ".tex", ".log", ".md", ".sql"}:
                kind = "other"
                if "figures" in rel.parts and suffix in {".pdf", ".png"}:
                    kind = "figure"
                elif "aastex" in rel.parts and suffix == ".pdf":
                    kind = "compiled_pdf"
                elif suffix == ".csv":
                    kind = "data_or_table_csv"
                elif path.name == "analysis_results.json":
                    kind = "analysis_json"
                elif path.name == "compile.log":
                    kind = "compile_log"
                elif suffix == ".tex":
                    kind = "aastex_source"
                rows.append(
                    {
                        "paper_slug": slug,
                        "paper_title": topic["title"],
                        "kind": kind,
                        "suffix": suffix,
                        "path": str(path),
                        "relative_path": str(rel),
                        "bytes": path.stat().st_size,
                        "sha256": sha256(path) if suffix in {".pdf", ".json", ".csv", ".tex", ".md", ".sql"} else None,
                    }
                )
    return rows


def write_report(summary: dict[str, Any]) -> None:
    assert_lane_write(REPORT_MD)
    lines = [
        f"# Goru actual-data robustness tick — {TS}",
        "",
        f"Marker: `GORU_ACTUAL_DATA_ROBUSTNESS_TICK_{TS}`",
        "",
        "## Work completed",
        "",
        "- Read cached SDSS DR17-derived analysis CSV only; no network or product writes.",
        "- Generated lane-local mechanical tables for sample counts, BPT sensitivity, S/N-redshift-mass bins, matched-control robustness, topic metrics, simulation target cells, and figure/table inventory.",
        "- All metrics are optical SDSS proxy/denominator quantities unless explicitly noted; no causal AGN feedback, gas depletion, escape/recycling, radio-jet, X-ray, or simulation-validation claim is made.",
        "",
        "## Key mechanical results",
        "",
    ]
    base_counts = summary["base_counts"]
    lines.extend(
        [
            f"- Source analysis rows: {base_counts['analysis_rows']:,}; BPT counts: star-forming {base_counts['bpt_counts'].get('star-forming', 0):,}, intermediate {base_counts['bpt_counts'].get('intermediate', 0):,}, AGN {base_counts['bpt_counts'].get('agn', 0):,}, unclassified {base_counts['bpt_counts'].get('unclassified', 0):,}.",
            f"- Baseline matched AGN-minus-SF median log-sSFR offset: {summary['matched_baseline']['median_delta_log_sSFR']:.3f} dex with bootstrap CI [{summary['matched_baseline']['median_ci95_low']:.3f}, {summary['matched_baseline']['median_ci95_high']:.3f}] across {summary['matched_baseline']['target_n']:,} optical AGN targets.",
            f"- S/N>=5 matched offset: {summary['matched_sn5']['median_delta_log_sSFR']:.3f} dex; S/N>=10 matched offset: {summary['matched_sn10']['median_delta_log_sSFR']:.3f} dex. These remain association/proxy checks, not causal feedback evidence.",
            f"- k=10 density-proxy high-minus-low quenched-fraction difference at S/N>=3: {summary['density_k10_diff']['value']:.3f} with bootstrap CI [{summary['density_k10_diff']['ci95_low']:.3f}, {summary['density_k10_diff']['ci95_high']:.3f}].",
            f"- Figure/table inventory rows: {summary['inventory_rows']:,}; compiled PDF entries found: {summary['compiled_pdf_entries']:,}; figure entries found: {summary['figure_entries']:,}; CSV/table entries found: {summary['csv_entries']:,}.",
            "",
            "## Output artifacts",
            "",
        ]
    )
    for label, path in summary["outputs"].items():
        lines.append(f"- {label}: `{path}`")
    lines.extend(
        [
            "",
            "## Safety",
            "",
            "No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission changes. Lane-local writes only, with the separate required concise append to `OVERNIGHT_LEDGER.md` performed by Hermes after verification.",
        ]
    )
    REPORT_MD.write_text("\n".join(lines) + "\n")


def main() -> None:
    df = load_and_prepare()
    source_results = load_json(SOURCE_RESULTS) if SOURCE_RESULTS.exists() else {}

    sample_rows = sample_counts_rows(df)
    bpt_rows = bpt_sensitivity_rows(df)
    sn_rows = sn_z_mass_rows(df)
    matched = matched_rows(df)
    topic_rows = topic_metric_rows(df, matched)
    target_rows = target_vector_rows(df)
    inv_rows = inventory_rows()

    write_csv(SAMPLE_COUNTS_CSV, sample_rows)
    write_csv(BPT_SENSITIVITY_CSV, bpt_rows)
    write_csv(SN_Z_MASS_CSV, sn_rows)
    write_csv(MATCHED_CSV, matched)
    write_csv(TOPIC_METRICS_CSV, topic_rows)
    write_csv(TARGET_VECTOR_CSV, target_rows)
    write_csv(INVENTORY_CSV, inv_rows)

    base_counts = {
        "analysis_rows": int(len(df)),
        "bpt_counts": {str(k): int(v) for k, v in df["bpt_label"].value_counts().to_dict().items()},
        "source_results_analysis_rows": source_results.get("analysis_rows"),
        "source_results_bpt_counts": source_results.get("bpt_counts"),
    }
    by_variant = {row["variant"]: row for row in matched}
    topic_lookup = {(row["topic"], row["variant"], row["metric"]): row for row in topic_rows}
    density_key = ("m1_rp2_environment_quenching", "knn_density_k10_sn_ge_3", "high_minus_low_quenched_fraction")
    summary = {
        "timestamp_utc": TS,
        "marker": f"GORU_ACTUAL_DATA_ROBUSTNESS_TICK_{TS}",
        "source_csv": str(SOURCE_CSV),
        "base_counts": base_counts,
        "sample_count_rows": len(sample_rows),
        "bpt_sensitivity_rows": len(bpt_rows),
        "sn_redshift_mass_rows": len(sn_rows),
        "matched_rows": len(matched),
        "topic_metric_rows": len(topic_rows),
        "target_vector_rows": len(target_rows),
        "inventory_rows": len(inv_rows),
        "compiled_pdf_entries": sum(1 for r in inv_rows if r["kind"] == "compiled_pdf"),
        "figure_entries": sum(1 for r in inv_rows if r["kind"] == "figure"),
        "csv_entries": sum(1 for r in inv_rows if r["kind"] == "data_or_table_csv"),
        "matched_baseline": by_variant["sn_ge_3_baseline_agn_vs_sf"],
        "matched_sn5": by_variant["sn_ge_5_baseline_agn_vs_sf"],
        "matched_sn10": by_variant["sn_ge_10_baseline_agn_vs_sf"],
        "density_k10_diff": topic_lookup[density_key],
        "outputs": {
            "sample_counts_csv": str(SAMPLE_COUNTS_CSV),
            "bpt_sensitivity_csv": str(BPT_SENSITIVITY_CSV),
            "sn_redshift_mass_bins_csv": str(SN_Z_MASS_CSV),
            "matched_sfr_offset_robustness_csv": str(MATCHED_CSV),
            "topic_metric_robustness_csv": str(TOPIC_METRICS_CSV),
            "simulation_target_vector_cells_csv": str(TARGET_VECTOR_CSV),
            "figure_table_inventory_csv": str(INVENTORY_CSV),
            "summary_json": str(SUMMARY_JSON),
            "tick_report_md": str(REPORT_MD),
        },
        "safety": "Read cached SDSS/local artifacts only; wrote lane-local Goru artifacts only; no DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission.",
        "proxy_limits": "All science quantities are SDSS optical emission-line/color/sSFR proxy or denominator checks; they do not establish causal feedback, gas depletion, escape/recycling, radio-jet coupling, X-ray maintenance heating, or simulation correctness.",
    }
    assert_lane_write(SUMMARY_JSON)
    SUMMARY_JSON.write_text(json.dumps(summary, indent=2, sort_keys=True))
    write_report(summary)
    print(json.dumps({"ok": True, "report": str(REPORT_MD), "summary": str(SUMMARY_JSON), "outputs": summary["outputs"]}, indent=2))


if __name__ == "__main__":
    main()
