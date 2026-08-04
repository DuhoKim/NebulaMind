#!/usr/bin/env python3
"""Goru lane: stratified SDSS/BPT mechanical robustness tick.

Reads only cached SDSS-derived CSVs and existing local manifests. Writes only
under lanes/goru. This tick extends the earlier global robustness pass with
class-boundary sensitivity, S/N/mass/redshift stratification, matched-control
bootstrap summaries, selection-caution overlays, and artifact inventories.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Tuple

import numpy as np
import pandas as pd

try:
    from scipy.spatial import cKDTree
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"scipy is required for deterministic nearest-neighbour matching: {exc}")

try:
    import matplotlib.pyplot as plt
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"matplotlib is required for lane-local figures: {exc}")

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
WORK_ROOT = AUTOPILOT / "overnight-9-papers-20260708"
GORU_ROOT = WORK_ROOT / "lanes/goru"
RUN1 = AUTOPILOT / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
RUN8 = AUTOPILOT / "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
SOURCE_CSV = RUN1 / "data/analysis_sample_bpt.csv"
SOURCE_RESULTS = RUN1 / "analysis_results.json"
MATCHED_CSV = RUN1 / "data/matched_agn_sf_pairs.csv"
BATCH_MANIFEST = RUN8 / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json"
TORI_ATTRITION_ROOT = WORK_ROOT / "lanes/tori/selection-function-attrition"

MARKER_BASE = "GORU_STRATIFIED_BPT_ROBUSTNESS_TICK"
PROXY_GUARD = (
    "SDSS optical emission-line/color/sSFR proxy or denominator only; no causal AGN feedback, "
    "gas-depletion, radio-jet coupling, escape/recycling, X-ray maintenance-heating, or simulation-validation proof."
)

MASS_BINS = [8.0, 9.5, 10.0, 10.5, 11.0, 12.5]
MASS_LABELS = ["8.0-9.5", "9.5-10.0", "10.0-10.5", "10.5-11.0", "11.0-12.5"]
Z_BINS = [0.02, 0.05, 0.08, 0.12]
Z_LABELS = ["0.02-0.05", "0.05-0.08", "0.08-0.12"]
SN_THRESHOLDS = [3, 5, 10]
RNG_SEED = 20260708


def utc_ts() -> str:
    return os.environ.get("GORU_TICK_TS") or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_float(v: Any) -> float | None:
    try:
        x = float(v)
        if math.isfinite(x):
            return x
    except Exception:
        pass
    return None


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        rows = [{"empty": "no rows"}]
    # Preserve first-seen column order across heterogeneous rows.
    fields: List[str] = []
    for row in rows:
        for key in row.keys():
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            w.writerow(row)


def binomial_se(p: float, n: int) -> float | None:
    if n <= 0 or not math.isfinite(p):
        return None
    return float(math.sqrt(max(p * (1.0 - p), 0.0) / n))


def bootstrap_ci(values: Iterable[float], func: Callable[[np.ndarray], float], n_boot: int = 1000, seed: int = RNG_SEED) -> Tuple[float | None, float | None]:
    arr = np.asarray([v for v in values if math.isfinite(float(v))], dtype=float)
    if len(arr) == 0:
        return None, None
    rng = np.random.default_rng(seed + len(arr))
    out = np.empty(n_boot)
    for i in range(n_boot):
        draw = arr[rng.integers(0, len(arr), len(arr))]
        out[i] = float(func(draw))
    return float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))


def bootstrap_fraction(mask: Iterable[bool], n_boot: int = 1000, seed: int = RNG_SEED) -> Tuple[float | None, float | None]:
    arr = np.asarray(list(mask), dtype=float)
    if len(arr) == 0:
        return None, None
    rng = np.random.default_rng(seed + len(arr) + int(arr.sum()))
    out = np.empty(n_boot)
    for i in range(n_boot):
        draw = arr[rng.integers(0, len(arr), len(arr))]
        out[i] = float(np.mean(draw))
    return float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))


def frac_row(mask: pd.Series | np.ndarray) -> Dict[str, Any]:
    vals = np.asarray(mask, dtype=bool)
    n = int(len(vals))
    k = int(vals.sum())
    p = float(k / n) if n else float("nan")
    lo, hi = bootstrap_fraction(vals) if n else (None, None)
    return {"n": n, "k": k, "fraction": p, "se": binomial_se(p, n), "ci95_low": lo, "ci95_high": hi}


def load_sample() -> pd.DataFrame:
    if not SOURCE_CSV.exists():
        raise SystemExit(f"Missing source CSV: {SOURCE_CSV}")
    df = pd.read_csv(SOURCE_CSV)
    needed = [
        "specObjID", "z", "ra", "dec", "bptclass", "lgm_tot_p50", "specsfr_tot_p50",
        "u_minus_r", "g_minus_r", "sn_ha", "sn_hb", "sn_oiii", "sn_nii",
        "log_nii_ha", "log_oiii_hb", "bpt_label",
    ]
    missing = [c for c in needed if c not in df.columns]
    if missing:
        raise SystemExit(f"Source CSV missing required columns: {missing}")
    for c in [c for c in needed if c not in {"specObjID", "bpt_label"}]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=[
        "z", "lgm_tot_p50", "specsfr_tot_p50", "u_minus_r", "g_minus_r",
        "sn_ha", "sn_hb", "sn_oiii", "sn_nii", "log_nii_ha", "log_oiii_hb", "bpt_label",
    ]).copy()
    df["specObjID"] = df["specObjID"].astype(str)
    df["sn_min"] = df[["sn_ha", "sn_hb", "sn_oiii", "sn_nii"]].min(axis=1)
    df["mass_bin"] = pd.cut(df["lgm_tot_p50"], MASS_BINS, labels=MASS_LABELS, include_lowest=True)
    df["z_bin"] = pd.cut(df["z"], Z_BINS, labels=Z_LABELS, include_lowest=True)
    df["quenched_ssfr_lt_m11"] = df["specsfr_tot_p50"] < -11.0
    df["transition_or_quenched_ssfr_lt_m10p7"] = df["specsfr_tot_p50"] < -10.7
    add_alt_bpt(df)
    return df


def add_alt_bpt(df: pd.DataFrame) -> None:
    x = df["log_nii_ha"].to_numpy(dtype=float)
    y = df["log_oiii_hb"].to_numpy(dtype=float)
    kauff = 0.61 / (x - 0.05) + 1.30
    kewley = 0.61 / (x - 0.47) + 1.19
    seyfert_line = 1.01 * x + 0.48
    valid = np.isfinite(x) & np.isfinite(y) & (x <= 0.35)
    alt = np.full(len(df), "unclassified_or_right_grid", dtype=object)
    alt[valid & (y < kauff)] = "star_forming_kauffmann03"
    alt[valid & (y >= kauff) & (y <= kewley)] = "composite_between_lines"
    alt[valid & (y > kewley)] = "agn_kewley01"
    df["alt_bpt_class"] = alt
    df["kauffmann_margin_y_minus_curve"] = y - kauff
    df["kewley_margin_y_minus_curve"] = y - kewley
    df["seyfert_liner_margin_y_minus_line"] = y - seyfert_line
    df["near_kauffmann_boundary_abs_y_lt_0p05"] = np.abs(df["kauffmann_margin_y_minus_curve"]) < 0.05
    df["near_kewley_boundary_abs_y_lt_0p05"] = np.abs(df["kewley_margin_y_minus_curve"]) < 0.05
    df["is_bpt_agn"] = df["bpt_label"] == "agn"
    df["is_bpt_sf"] = df["bpt_label"] == "star-forming"
    df["is_bpt_intermediate"] = df["bpt_label"] == "intermediate"
    df["is_alt_agn"] = df["alt_bpt_class"] == "agn_kewley01"
    df["is_alt_sf"] = df["alt_bpt_class"] == "star_forming_kauffmann03"
    df["is_alt_composite"] = df["alt_bpt_class"] == "composite_between_lines"
    df["is_high_excitation_y_gt_0p25"] = df["is_alt_agn"] & (df["log_oiii_hb"] > 0.25)
    df["is_high_excitation_y_gt_0p50"] = df["is_alt_agn"] & (df["log_oiii_hb"] > 0.50)
    df["is_seyfert_like_nii_proxy"] = df["is_alt_agn"] & (df["seyfert_liner_margin_y_minus_line"] >= 0)
    df["is_liner_like_nii_proxy"] = df["is_alt_agn"] & (df["seyfert_liner_margin_y_minus_line"] < 0)


def load_latest_tori_attrition() -> Dict[str, Any] | None:
    if not TORI_ATTRITION_ROOT.exists():
        return None
    candidates = sorted(TORI_ATTRITION_ROOT.glob("*/selection_function_attrition_summary_*.json"))
    if not candidates:
        return None
    with candidates[-1].open("r", encoding="utf-8") as f:
        data = json.load(f)
    data["_source_json"] = str(candidates[-1])
    return data


def build_crosswalk_tables(df: pd.DataFrame) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    crosswalk: List[Dict[str, Any]] = []
    boundary_rows: List[Dict[str, Any]] = []
    bptclass_rows: List[Dict[str, Any]] = []
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min"] >= sn]
        denom = len(sub)
        for label, alt_counts in sub.groupby("bpt_label")["alt_bpt_class"].value_counts().items():
            # Pandas returns MultiIndex tuple from value_counts on groupby.
            pass
        for (current, alt), g in sub.groupby(["bpt_label", "alt_bpt_class"], dropna=False):
            crosswalk.append({
                "sn_min_ge": sn,
                "current_bpt_label": current,
                "recomputed_alt_bpt_class": alt,
                "n": int(len(g)),
                "fraction_of_sn_threshold_sample": float(len(g) / denom) if denom else None,
                "proxy_guard": PROXY_GUARD,
            })
        for (bptclass, current), g in sub.groupby(["bptclass", "bpt_label"], dropna=False):
            bptclass_rows.append({
                "sn_min_ge": sn,
                "sdss_galSpecExtra_bptclass_numeric": int(bptclass) if math.isfinite(float(bptclass)) else bptclass,
                "current_bpt_label": current,
                "n": int(len(g)),
                "fraction_of_sn_threshold_sample": float(len(g) / denom) if denom else None,
                "note": "Numeric SDSS bptclass is recorded for cross-check only; manuscript pilots use recomputed Kauffmann/Kewley labels.",
            })
        boundary_rows.append({
            "sn_min_ge": sn,
            "n_threshold": int(denom),
            "near_kauffmann_abs_y_margin_lt_0p05_n": int(sub["near_kauffmann_boundary_abs_y_lt_0p05"].sum()),
            "near_kauffmann_abs_y_margin_lt_0p05_fraction": float(sub["near_kauffmann_boundary_abs_y_lt_0p05"].mean()) if denom else None,
            "near_kewley_abs_y_margin_lt_0p05_n": int(sub["near_kewley_boundary_abs_y_lt_0p05"].sum()),
            "near_kewley_abs_y_margin_lt_0p05_fraction": float(sub["near_kewley_boundary_abs_y_lt_0p05"].mean()) if denom else None,
            "bpt_agn_near_kewley_boundary_n": int((sub["is_bpt_agn"] & sub["near_kewley_boundary_abs_y_lt_0p05"]).sum()),
            "intermediate_near_kewley_boundary_n": int((sub["is_bpt_intermediate"] & sub["near_kewley_boundary_abs_y_lt_0p05"]).sum()),
            "guard": "Boundary-near counts flag classification sensitivity; they are not new physical classes.",
        })
    return crosswalk, boundary_rows, bptclass_rows


def build_stratified_counts(df: pd.DataFrame) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for sn in SN_THRESHOLDS:
        sub_sn = df[df["sn_min"] >= sn].copy()
        for (mass_bin, z_bin), g in sub_sn.groupby(["mass_bin", "z_bin"], observed=True):
            n = int(len(g))
            if n == 0:
                continue
            agn = int(g["is_bpt_agn"].sum())
            sf = int(g["is_bpt_sf"].sum())
            inter = int(g["is_bpt_intermediate"].sum())
            high025 = int(g["is_high_excitation_y_gt_0p25"].sum())
            seyfert = int(g["is_seyfert_like_nii_proxy"].sum())
            liner = int(g["is_liner_like_nii_proxy"].sum())
            quenched = int(g["quenched_ssfr_lt_m11"].sum())
            rows.append({
                "sn_min_ge": sn,
                "mass_bin_logM": str(mass_bin),
                "z_bin": str(z_bin),
                "n": n,
                "bpt_star_forming_n": sf,
                "bpt_star_forming_fraction": sf / n,
                "bpt_intermediate_n": inter,
                "bpt_intermediate_fraction": inter / n,
                "bpt_agn_n": agn,
                "bpt_agn_fraction": agn / n,
                "high_excitation_proxy_y_gt_0p25_n": high025,
                "high_excitation_proxy_y_gt_0p25_fraction": high025 / n,
                "nii_seyfert_like_proxy_n": seyfert,
                "nii_seyfert_like_proxy_fraction": seyfert / n,
                "nii_liner_like_proxy_n": liner,
                "nii_liner_like_proxy_fraction": liner / n,
                "quenched_ssfr_lt_m11_n": quenched,
                "quenched_ssfr_lt_m11_fraction": quenched / n,
                "median_log_sSFR": float(g["specsfr_tot_p50"].median()),
                "median_logM": float(g["lgm_tot_p50"].median()),
                "median_z": float(g["z"].median()),
                "median_u_minus_r": float(g["u_minus_r"].median()),
                "min_cell_flag": "LOW_N_LT_50" if n < 50 else "OK",
                "proxy_guard": PROXY_GUARD,
            })
    return rows


def match_targets_to_controls(g: pd.DataFrame, target_mask: pd.Series, control_mask: pd.Series) -> Dict[str, Any] | None:
    targets = g[target_mask].copy()
    controls = g[control_mask].copy()
    if len(targets) < 30 or len(controls) < 30:
        return None
    features = ["lgm_tot_p50", "z"]
    scale = controls[features].std().replace(0, 1)
    ctrl_scaled = (controls[features] - controls[features].mean()) / scale
    targ_scaled = (targets[features] - controls[features].mean()) / scale
    tree = cKDTree(ctrl_scaled.to_numpy())
    dist, idx = tree.query(targ_scaled.to_numpy(), k=1)
    ctrl = controls.iloc[idx].reset_index(drop=True)
    targ = targets.reset_index(drop=True)
    delta = targ["specsfr_tot_p50"].to_numpy(dtype=float) - ctrl["specsfr_tot_p50"].to_numpy(dtype=float)
    med_lo, med_hi = bootstrap_ci(delta, np.median, n_boot=1000)
    mean_lo, mean_hi = bootstrap_ci(delta, np.mean, n_boot=1000)
    return {
        "target_n": int(len(targets)),
        "control_n": int(len(controls)),
        "matched_pairs": int(len(delta)),
        "median_delta_log_sSFR_target_minus_control": float(np.median(delta)),
        "median_delta_ci95_low": med_lo,
        "median_delta_ci95_high": med_hi,
        "mean_delta_log_sSFR_target_minus_control": float(np.mean(delta)),
        "mean_delta_ci95_low": mean_lo,
        "mean_delta_ci95_high": mean_hi,
        "match_abs_delta_logM_median": float(np.median(np.abs(targ["lgm_tot_p50"].to_numpy(dtype=float) - ctrl["lgm_tot_p50"].to_numpy(dtype=float)))),
        "match_abs_delta_z_median": float(np.median(np.abs(targ["z"].to_numpy(dtype=float) - ctrl["z"].to_numpy(dtype=float)))),
        "match_distance_scaled_median": float(np.median(dist)),
    }


def build_matched_tables(df: pd.DataFrame) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    matched_rows: List[Dict[str, Any]] = []
    sensitivity_rows: List[Dict[str, Any]] = []
    target_defs: Dict[str, Callable[[pd.DataFrame], pd.Series]] = {
        "bpt_agn_vs_bpt_sf": lambda g: g["is_bpt_agn"],
        "high_excitation_y_gt_0p25_vs_bpt_sf": lambda g: g["is_high_excitation_y_gt_0p25"],
        "nii_seyfert_like_proxy_vs_bpt_sf": lambda g: g["is_seyfert_like_nii_proxy"],
        "nii_liner_like_proxy_vs_bpt_sf": lambda g: g["is_liner_like_nii_proxy"],
        "composite_plus_agn_vs_bpt_sf": lambda g: g["is_bpt_agn"] | g["is_bpt_intermediate"],
    }
    for sn in SN_THRESHOLDS:
        sub_sn = df[df["sn_min"] >= sn].copy()
        for name, target_func in target_defs.items():
            stats = match_targets_to_controls(sub_sn, target_func(sub_sn), sub_sn["is_bpt_sf"])
            row_base = {"sn_min_ge": sn, "target_definition": name, "stratum_type": "all", "stratum": "all"}
            if stats:
                sensitivity_rows.append({**row_base, **stats, "proxy_guard": PROXY_GUARD})
            else:
                sensitivity_rows.append({**row_base, "target_n": int(target_func(sub_sn).sum()), "control_n": int(sub_sn["is_bpt_sf"].sum()), "matched_pairs": 0, "skip_reason": "target_n_or_control_n_lt_30", "proxy_guard": PROXY_GUARD})
        # Stratified only for the primary two definitions to keep output readable.
        strat_defs = {
            "bpt_agn_vs_bpt_sf": lambda g: g["is_bpt_agn"],
            "high_excitation_y_gt_0p25_vs_bpt_sf": lambda g: g["is_high_excitation_y_gt_0p25"],
        }
        groups: List[Tuple[str, str, pd.DataFrame]] = [("all", "all", sub_sn)]
        for mass_bin, g in sub_sn.groupby("mass_bin", observed=True):
            groups.append(("mass_bin", str(mass_bin), g.copy()))
        for z_bin, g in sub_sn.groupby("z_bin", observed=True):
            groups.append(("z_bin", str(z_bin), g.copy()))
        for (mass_bin, z_bin), g in sub_sn.groupby(["mass_bin", "z_bin"], observed=True):
            groups.append(("mass_z_bin", f"{mass_bin}|{z_bin}", g.copy()))
        for stratum_type, stratum, g in groups:
            for name, target_func in strat_defs.items():
                stats = match_targets_to_controls(g, target_func(g), g["is_bpt_sf"])
                base = {"sn_min_ge": sn, "target_definition": name, "stratum_type": stratum_type, "stratum": stratum}
                if stats:
                    matched_rows.append({**base, **stats, "proxy_guard": PROXY_GUARD})
                else:
                    matched_rows.append({
                        **base,
                        "target_n": int(target_func(g).sum()),
                        "control_n": int(g["is_bpt_sf"].sum()),
                        "matched_pairs": 0,
                        "skip_reason": "target_n_or_control_n_lt_30",
                        "proxy_guard": PROXY_GUARD,
                    })
    return matched_rows, sensitivity_rows


def build_bootstrap_summary(df: pd.DataFrame) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    metric_defs: Dict[str, Callable[[pd.DataFrame], pd.Series]] = {
        "bpt_agn_fraction": lambda g: g["is_bpt_agn"],
        "high_excitation_y_gt_0p25_fraction": lambda g: g["is_high_excitation_y_gt_0p25"],
        "nii_seyfert_like_proxy_fraction": lambda g: g["is_seyfert_like_nii_proxy"],
        "quenched_ssfr_lt_m11_fraction": lambda g: g["quenched_ssfr_lt_m11"],
    }
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min"] >= sn].copy()
        for metric, func in metric_defs.items():
            fr = frac_row(func(sub))
            rows.append({
                "sn_min_ge": sn,
                "metric": metric,
                "n": fr["n"],
                "k": fr["k"],
                "value": fr["fraction"],
                "se": fr["se"],
                "ci95_low": fr["ci95_low"],
                "ci95_high": fr["ci95_high"],
                "proxy_guard": PROXY_GUARD,
            })
        for label in ["star-forming", "intermediate", "agn"]:
            g = sub[sub["bpt_label"] == label]
            if len(g) == 0:
                continue
            lo, hi = bootstrap_ci(g["specsfr_tot_p50"].to_numpy(dtype=float), np.median, n_boot=1000)
            rows.append({
                "sn_min_ge": sn,
                "metric": f"median_log_sSFR_{label}",
                "n": int(len(g)),
                "k": "",
                "value": float(g["specsfr_tot_p50"].median()),
                "se": "",
                "ci95_low": lo,
                "ci95_high": hi,
                "proxy_guard": PROXY_GUARD,
            })
        sf = sub[sub["is_bpt_sf"]]["specsfr_tot_p50"].to_numpy(dtype=float)
        agn = sub[sub["is_bpt_agn"]]["specsfr_tot_p50"].to_numpy(dtype=float)
        if len(sf) and len(agn):
            raw_diff = float(np.median(agn) - np.median(sf))
            rng = np.random.default_rng(RNG_SEED + sn)
            boot = []
            for _ in range(1000):
                a = agn[rng.integers(0, len(agn), len(agn))]
                s = sf[rng.integers(0, len(sf), len(sf))]
                boot.append(float(np.median(a) - np.median(s)))
            rows.append({
                "sn_min_ge": sn,
                "metric": "unmatched_median_log_sSFR_difference_bpt_agn_minus_sf",
                "n": int(len(agn) + len(sf)),
                "k": int(len(agn)),
                "value": raw_diff,
                "se": "",
                "ci95_low": float(np.percentile(boot, 2.5)),
                "ci95_high": float(np.percentile(boot, 97.5)),
                "proxy_guard": PROXY_GUARD,
            })
    return rows


def build_high_excitation_denominators(df: pd.DataFrame) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    defs = [
        ("bpt_agn_all", lambda g: g["is_bpt_agn"]),
        ("logOIII_Hb_gt_0p00_within_agn", lambda g: g["is_alt_agn"] & (g["log_oiii_hb"] > 0.00)),
        ("logOIII_Hb_gt_0p25_within_agn", lambda g: g["is_high_excitation_y_gt_0p25"]),
        ("logOIII_Hb_gt_0p50_within_agn", lambda g: g["is_high_excitation_y_gt_0p50"]),
        ("nii_seyfert_like_proxy_within_agn", lambda g: g["is_seyfert_like_nii_proxy"]),
    ]
    for sn in SN_THRESHOLDS:
        sub = df[df["sn_min"] >= sn]
        groups: List[Tuple[str, str, pd.DataFrame]] = [("all", "all", sub)]
        for mass_bin, g in sub.groupby("mass_bin", observed=True):
            groups.append(("mass_bin", str(mass_bin), g))
        for z_bin, g in sub.groupby("z_bin", observed=True):
            groups.append(("z_bin", str(z_bin), g))
        for stratum_type, stratum, g in groups:
            denom = len(g)
            for name, func in defs:
                k = int(func(g).sum())
                rows.append({
                    "sn_min_ge": sn,
                    "definition": name,
                    "stratum_type": stratum_type,
                    "stratum": stratum,
                    "denominator_n": int(denom),
                    "candidate_n": k,
                    "candidate_fraction": float(k / denom) if denom else None,
                    "guard": "High-excitation/Seyfert-like labels are NII-BPT optical proxies only; no outflow, radio, or X-ray measurement is implied.",
                })
    return rows


def build_selection_overlay(tori: Dict[str, Any] | None, df: pd.DataFrame) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if not tori:
        return [{"status": "NO_TORI_SELECTION_ATTRITION_JSON_FOUND", "guard": PROXY_GUARD}]
    for row in tori.get("stage_counts", []):
        rows.append({
            "source": "tori_selection_attrition_stage_counts",
            "source_json": tori.get("_source_json", ""),
            "stage_key": row.get("stage_key"),
            "stage_label": row.get("stage_label"),
            "sdss_dr17_count": row.get("sdss_dr17_count"),
            "retention_vs_previous_stage": row.get("retention_vs_previous_stage"),
            "cached_sample_count_at_matching_stage": row.get("cached_sample_count_at_matching_stage"),
            "cached_coverage_of_sdss_stage": row.get("cached_coverage_of_sdss_stage"),
            "guard": "Read-only public SDSS count inherited from Tori attrition packet; Goru overlay did not query network.",
        })
    for key in ["ssfr_low_bin_reference", "ssfr_star_forming_bin_reference", "m3_p2_default_denominator", "m3_p2_strict_denominator"]:
        item = tori.get(key, {}) or {}
        rows.append({
            "source": "tori_selection_attrition_named_reference",
            "source_json": tori.get("_source_json", ""),
            "reference_key": key,
            "sdss_parent_count": item.get("sdss_parent_count") or item.get("sdss_parent_mass_ssfr_count"),
            "sdss_sn_ge_3_count": item.get("sdss_sn_ge_3_count"),
            "cached_sn_ge_3_count": item.get("cached_sn_ge_3_count"),
            "sn_ge_3_retention_vs_parent": item.get("sn_ge_3_retention_vs_parent"),
            "cached_coverage_of_sdss_sn_ge_3": item.get("cached_coverage_of_sdss_sn_ge_3"),
            "guard": item.get("guard", PROXY_GUARD),
        })
    local_counts = df.groupby(["bpt_label"], dropna=False).size().to_dict()
    for label, n in local_counts.items():
        rows.append({
            "source": "cached_sample_class_composition",
            "source_json": str(SOURCE_CSV),
            "class": label,
            "cached_class_count": int(n),
            "cached_fraction_of_60000": float(n / len(df)) if len(df) else None,
            "guard": "Composition is for the capped cached 60,000-row sample, not the full SDSS eligible population.",
        })
    return rows


def build_inventory(ts: str) -> List[Dict[str, Any]]:
    roots = [
        ("run1_primary", RUN1),
        ("run8_batch", RUN8),
        ("overnight_lanes", WORK_ROOT / "lanes"),
    ]
    suffixes = {".pdf", ".png", ".csv", ".json", ".jsonl", ".tex", ".log", ".md", ".py"}
    rows: List[Dict[str, Any]] = []
    for bucket, root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in suffixes:
                continue
            try:
                rel = path.relative_to(root)
            except ValueError:
                rel = path
            digest = ""
            if path.suffix.lower() in {".pdf", ".csv", ".json", ".tex"}:
                try:
                    digest = sha256_path(path)
                except Exception:
                    digest = "HASH_FAILED"
            rows.append({
                "inventory_timestamp_utc": ts,
                "bucket": bucket,
                "relative_path": str(rel),
                "suffix": path.suffix.lower(),
                "bytes": int(path.stat().st_size),
                "sha256_if_hashed": digest,
                "guard": "Local artifact inventory only; no writes outside Goru except required ledger append.",
            })
    return rows


def write_latex_fragment(path: Path, sensitivity_rows: List[Dict[str, Any]]) -> None:
    selected = [r for r in sensitivity_rows if r.get("stratum_type") == "all" and r.get("matched_pairs", 0)]
    selected = sorted(selected, key=lambda r: (int(r.get("sn_min_ge", 0)), str(r.get("target_definition", ""))))
    lines = [
        "% GORU_STRATIFIED_BPT_ROBUSTNESS_TICK table fragment; lane-local only, not merged.",
        "\\begin{deluxetable*}{llrrrr}",
        "\\tablecaption{BPT/SN sensitivity of matched optical-class sSFR offsets}",
        "\\tablehead{\\colhead{S/N cut} & \\colhead{Target definition} & \\colhead{$N_{target}$} & \\colhead{$N_{ctrl}$} & \\colhead{Median $\\Delta\\log\\mathrm{sSFR}$} & \\colhead{95\\% CI}}",
        "\\startdata",
    ]
    for r in selected:
        ci = f"[{float(r['median_delta_ci95_low']):.2f}, {float(r['median_delta_ci95_high']):.2f}]" if r.get("median_delta_ci95_low") not in (None, "") else "--"
        target = str(r["target_definition"]).replace("_", "\\_")
        lines.append(
            f"$\\geq${int(r['sn_min_ge'])} & {target} & {int(r['target_n']):,} & {int(r['control_n']):,} & {float(r['median_delta_log_sSFR_target_minus_control']):.2f} & {ci} \\\\"
        )
    lines += [
        "\\enddata",
        "\\tablecomments{All rows are optical SDSS BPT proxy definitions matched to star-forming controls in stellar-mass/redshift space. They are association checks, not causal feedback evidence.}",
        "\\end{deluxetable*}",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def make_figures(df: pd.DataFrame, sensitivity_rows: List[Dict[str, Any]], out_dir: Path, ts: str) -> Dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs: Dict[str, str] = {}
    # BPT boundary sensitivity figure.
    fig, ax = plt.subplots(figsize=(6.2, 5.1))
    sample = df.sample(min(len(df), 18000), random_state=RNG_SEED)
    color_map = {"star-forming": "#2878b5", "intermediate": "#8c8c8c", "agn": "#c82423", "unclassified": "#111111"}
    for lab, g in sample.groupby("bpt_label"):
        ax.scatter(g["log_nii_ha"], g["log_oiii_hb"], s=3, alpha=0.16, label=f"{lab} cached", color=color_map.get(str(lab), "#555555"), rasterized=True)
    xs1 = np.linspace(-1.5, 0.03, 300)
    xs2 = np.linspace(-1.5, 0.35, 300)
    ax.plot(xs1, 0.61 / (xs1 - 0.05) + 1.30, color="black", lw=1.2, ls="--", label="Kauffmann+03")
    ax.plot(xs2, 0.61 / (xs2 - 0.47) + 1.19, color="black", lw=1.2, ls=":", label="Kewley+01")
    ax.plot(xs2, 1.01 * xs2 + 0.48, color="#7b3294", lw=1.0, ls="-.", label="NII Seyfert/LINER proxy")
    near = df[df["near_kewley_boundary_abs_y_lt_0p05"]]
    near = near.sample(min(len(near), 2500), random_state=RNG_SEED + 1) if len(near) else near
    if len(near):
        ax.scatter(near["log_nii_ha"], near["log_oiii_hb"], s=5, alpha=0.35, color="#ffbf00", label="near Kewley boundary", rasterized=True)
    ax.set_xlim(-1.45, 0.45)
    ax.set_ylim(-1.25, 1.55)
    ax.set_xlabel(r"$\log([\mathrm{N\,II}]/\mathrm{H}\alpha)$")
    ax.set_ylabel(r"$\log([\mathrm{O\,III}]/\mathrm{H}\beta)$")
    ax.set_title("Cached SDSS BPT boundary-sensitivity overlay")
    ax.legend(fontsize=7, loc="lower left", frameon=False)
    fig.tight_layout()
    png = out_dir / f"bpt_boundary_sensitivity_{ts}.png"
    pdf = out_dir / f"bpt_boundary_sensitivity_{ts}.pdf"
    fig.savefig(png, dpi=220)
    fig.savefig(pdf)
    plt.close(fig)
    outputs["bpt_boundary_sensitivity_png"] = str(png)
    outputs["bpt_boundary_sensitivity_pdf"] = str(pdf)

    # Matched offset sensitivity figure.
    plot_rows = [r for r in sensitivity_rows if r.get("stratum_type") == "all" and r.get("matched_pairs", 0)]
    labels = [f"S/N≥{r['sn_min_ge']}\n{str(r['target_definition']).replace('_vs_bpt_sf','').replace('_',' ')}" for r in plot_rows]
    vals = [float(r["median_delta_log_sSFR_target_minus_control"]) for r in plot_rows]
    lows = [float(r["median_delta_log_sSFR_target_minus_control"]) - float(r["median_delta_ci95_low"]) for r in plot_rows]
    highs = [float(r["median_delta_ci95_high"]) - float(r["median_delta_log_sSFR_target_minus_control"]) for r in plot_rows]
    if plot_rows:
        fig, ax = plt.subplots(figsize=(max(7.0, 0.42 * len(plot_rows)), 4.8))
        x = np.arange(len(plot_rows))
        ax.errorbar(x, vals, yerr=[lows, highs], fmt="o", color="#6c5ce7", ecolor="#6c5ce7", capsize=2)
        ax.axhline(0, color="0.4", ls="--", lw=1)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=55, ha="right", fontsize=7)
        ax.set_ylabel(r"median $\Delta\log$ sSFR (target - matched SF)")
        ax.set_title("Matched-control offset sensitivity to S/N and optical class proxy")
        fig.tight_layout()
        png2 = out_dir / f"matched_offset_sensitivity_{ts}.png"
        pdf2 = out_dir / f"matched_offset_sensitivity_{ts}.pdf"
        fig.savefig(png2, dpi=220)
        fig.savefig(pdf2)
        plt.close(fig)
        outputs["matched_offset_sensitivity_png"] = str(png2)
        outputs["matched_offset_sensitivity_pdf"] = str(pdf2)
    return outputs


def main() -> int:
    ts = utc_ts()
    marker = f"{MARKER_BASE}_{ts}"
    tables_dir = GORU_ROOT / "tables"
    artifacts_dir = GORU_ROOT / "artifacts"
    ticks_dir = GORU_ROOT / "ticks"
    figures_dir = GORU_ROOT / "figures"
    for d in (tables_dir, artifacts_dir, ticks_dir, figures_dir):
        d.mkdir(parents=True, exist_ok=True)

    df = load_sample()
    with SOURCE_RESULTS.open("r", encoding="utf-8") as f:
        source_results = json.load(f)
    tori_attrition = load_latest_tori_attrition()

    crosswalk, boundary_rows, bptclass_rows = build_crosswalk_tables(df)
    stratified_counts = build_stratified_counts(df)
    matched_rows, sensitivity_rows = build_matched_tables(df)
    bootstrap_rows = build_bootstrap_summary(df)
    high_excitation_rows = build_high_excitation_denominators(df)
    selection_overlay_rows = build_selection_overlay(tori_attrition, df)
    inventory_rows: List[Dict[str, Any]] = []

    paths = {
        "crosswalk_csv": tables_dir / f"bpt_demarcation_crosswalk_{ts}.csv",
        "boundary_margin_csv": tables_dir / f"bpt_boundary_margin_counts_{ts}.csv",
        "sdss_bptclass_crosscheck_csv": tables_dir / f"sdss_bptclass_numeric_crosscheck_{ts}.csv",
        "stratified_counts_csv": tables_dir / f"stratified_agn_fraction_by_mass_z_sn_{ts}.csv",
        "matched_strata_csv": tables_dir / f"matched_control_by_strata_{ts}.csv",
        "bpt_sensitivity_matched_csv": tables_dir / f"bpt_class_sensitivity_matched_offsets_{ts}.csv",
        "bootstrap_summary_csv": tables_dir / f"bootstrap_summary_key_metrics_{ts}.csv",
        "high_excitation_denominators_csv": tables_dir / f"high_excitation_denominators_{ts}.csv",
        "selection_overlay_csv": tables_dir / f"selection_caution_overlay_{ts}.csv",
        "inventory_csv": tables_dir / f"figure_table_inventory_deep_{ts}.csv",
        "latex_fragment": artifacts_dir / f"bpt_sensitivity_table_fragment_{ts}.tex",
        "summary_json": artifacts_dir / f"goru_stratified_bpt_robustness_{ts}.json",
        "tick_report_md": ticks_dir / f"GORU_TICK_{ts}.md",
    }

    write_csv(paths["crosswalk_csv"], crosswalk)
    write_csv(paths["boundary_margin_csv"], boundary_rows)
    write_csv(paths["sdss_bptclass_crosscheck_csv"], bptclass_rows)
    write_csv(paths["stratified_counts_csv"], stratified_counts)
    write_csv(paths["matched_strata_csv"], matched_rows)
    write_csv(paths["bpt_sensitivity_matched_csv"], sensitivity_rows)
    write_csv(paths["bootstrap_summary_csv"], bootstrap_rows)
    write_csv(paths["high_excitation_denominators_csv"], high_excitation_rows)
    write_csv(paths["selection_overlay_csv"], selection_overlay_rows)
    write_latex_fragment(paths["latex_fragment"], sensitivity_rows)
    figure_paths = make_figures(df, sensitivity_rows, figures_dir, ts)
    inventory_rows = build_inventory(ts)
    write_csv(paths["inventory_csv"], inventory_rows)

    # Key values for fast reporting.
    baseline = next(r for r in sensitivity_rows if r.get("sn_min_ge") == 3 and r.get("target_definition") == "bpt_agn_vs_bpt_sf" and r.get("stratum_type") == "all")
    sn10 = next(r for r in sensitivity_rows if r.get("sn_min_ge") == 10 and r.get("target_definition") == "bpt_agn_vs_bpt_sf" and r.get("stratum_type") == "all")
    high025 = next(r for r in sensitivity_rows if r.get("sn_min_ge") == 3 and r.get("target_definition") == "high_excitation_y_gt_0p25_vs_bpt_sf" and r.get("stratum_type") == "all")
    seyfert = next(r for r in sensitivity_rows if r.get("sn_min_ge") == 3 and r.get("target_definition") == "nii_seyfert_like_proxy_vs_bpt_sf" and r.get("stratum_type") == "all")
    all_sn3 = df[df["sn_min"] >= 3]
    near_kewley = int(all_sn3["near_kewley_boundary_abs_y_lt_0p05"].sum())
    near_kauffmann = int(all_sn3["near_kauffmann_boundary_abs_y_lt_0p05"].sum())
    selection_strict_total = None
    cached_coverage = None
    if tori_attrition:
        selection_strict_total = tori_attrition.get("strict_sdss_sn_ge_3_total")
        cached_coverage = tori_attrition.get("cached_coverage_of_strict_sdss_sn_ge_3")

    outputs = {k: str(v) for k, v in paths.items()}
    outputs.update(figure_paths)
    summary = {
        "marker": marker,
        "timestamp_utc": ts,
        "source_csv": str(SOURCE_CSV),
        "source_rows": int(len(df)),
        "source_results_analysis_rows": source_results.get("analysis_rows"),
        "source_results_bpt_counts": source_results.get("bpt_counts"),
        "sn_threshold_counts": {f"sn_ge_{sn}": int((df["sn_min"] >= sn).sum()) for sn in SN_THRESHOLDS},
        "boundary_near_counts_sn3": {
            "near_kauffmann_abs_y_lt_0p05": near_kauffmann,
            "near_kewley_abs_y_lt_0p05": near_kewley,
        },
        "matched_bpt_agn_baseline_sn3": baseline,
        "matched_bpt_agn_sn10": sn10,
        "matched_high_excitation_y_gt_0p25_sn3": high025,
        "matched_nii_seyfert_like_proxy_sn3": seyfert,
        "selection_overlay": {
            "tori_attrition_source_json": None if not tori_attrition else tori_attrition.get("_source_json"),
            "strict_sdss_sn_ge_3_total": selection_strict_total,
            "cached_coverage_of_strict_sdss_sn_ge_3": cached_coverage,
        },
        "row_counts": {
            "crosswalk": len(crosswalk),
            "boundary_margin": len(boundary_rows),
            "sdss_bptclass_crosscheck": len(bptclass_rows),
            "stratified_counts": len(stratified_counts),
            "matched_strata": len(matched_rows),
            "bpt_sensitivity_matched": len(sensitivity_rows),
            "bootstrap_summary": len(bootstrap_rows),
            "high_excitation_denominators": len(high_excitation_rows),
            "selection_overlay": len(selection_overlay_rows),
            "inventory": len(inventory_rows),
        },
        "outputs": outputs,
        "proxy_limits": PROXY_GUARD,
        "safety": "Read cached SDSS/local artifacts only; wrote under lanes/goru only. No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission.",
    }
    paths["summary_json"].write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    report = f"""# Goru stratified BPT/SN robustness tick — {ts}

Marker: `{marker}`

## Work completed

- Read cached SDSS DR17-derived sample only (`analysis_sample_bpt.csv`, {len(df):,} rows) plus existing local manifests/selection-count summaries; no network, DB, API, deploy, git, cron, billing, OAuth, or external submission action.
- Generated lane-local mechanical tables for BPT demarcation crosswalks, boundary-margin sensitivity, SDSS numeric `bptclass` cross-check, S/N×mass×redshift class fractions, matched-control offsets by strata, high-excitation denominators, bootstrap metric summaries, selection-caution overlay, and deeper figure/table inventory.
- Generated two lane-local figures: BPT boundary sensitivity and matched-offset sensitivity. All labels are optical SDSS proxy/denominator labels.

## Key mechanical results

- S/N threshold counts in cached sample: S/N>=3 = {int((df['sn_min'] >= 3).sum()):,}; S/N>=5 = {int((df['sn_min'] >= 5).sum()):,}; S/N>=10 = {int((df['sn_min'] >= 10).sum()):,}.
- Boundary-near flags at S/N>=3: {near_kauffmann:,} rows within 0.05 dex of the Kauffmann line; {near_kewley:,} rows within 0.05 dex of the Kewley line.
- Matched BPT-AGN minus star-forming median log-sSFR offset: S/N>=3 {float(baseline['median_delta_log_sSFR_target_minus_control']):.3f} dex (CI {float(baseline['median_delta_ci95_low']):.3f}, {float(baseline['median_delta_ci95_high']):.3f}); S/N>=10 {float(sn10['median_delta_log_sSFR_target_minus_control']):.3f} dex.
- High-excitation proxy (AGN with log[OIII]/Hb>0.25) matched offset at S/N>=3: {float(high025['median_delta_log_sSFR_target_minus_control']):.3f} dex across {int(high025['target_n']):,} targets.
- NII Seyfert-like proxy matched offset at S/N>=3: {float(seyfert['median_delta_log_sSFR_target_minus_control']):.3f} dex across {int(seyfert['target_n']):,} targets.
- Selection overlay inherited Tori public-SDSS attrition count: strict S/N>=3 four-line eligible rows = {selection_strict_total if selection_strict_total is not None else 'not available'}; cached coverage = {cached_coverage if cached_coverage is not None else 'not available'}.

## Output artifacts

- summary_json: `{paths['summary_json']}`
- tick_report_md: `{paths['tick_report_md']}`
- bpt_sensitivity_matched_csv: `{paths['bpt_sensitivity_matched_csv']}`
- matched_strata_csv: `{paths['matched_strata_csv']}`
- stratified_counts_csv: `{paths['stratified_counts_csv']}`
- bootstrap_summary_csv: `{paths['bootstrap_summary_csv']}`
- selection_overlay_csv: `{paths['selection_overlay_csv']}`
- inventory_csv: `{paths['inventory_csv']}`
- latex_fragment: `{paths['latex_fragment']}`
- figures: `{figure_paths.get('bpt_boundary_sensitivity_png')}`, `{figure_paths.get('matched_offset_sensitivity_png')}`

## Safety / interpretation guard

{PROXY_GUARD}

No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission changes. Lane-local writes only, with the separate required concise append to `OVERNIGHT_LEDGER.md` to be performed after verification.
"""
    paths["tick_report_md"].write_text(report, encoding="utf-8")
    print(json.dumps({"marker": marker, "summary_json": str(paths["summary_json"]), "tick_report_md": str(paths["tick_report_md"]), "row_counts": summary["row_counts"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
