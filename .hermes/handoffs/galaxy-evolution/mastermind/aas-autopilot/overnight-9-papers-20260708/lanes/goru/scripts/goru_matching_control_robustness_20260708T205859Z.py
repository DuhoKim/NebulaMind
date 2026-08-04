#!/usr/bin/env python3
"""Goru lane: matched-control robustness diagnostics for the overnight active-9 papers.

Reads only cached SDSS-derived local CSVs and writes Goru lane-local artifacts.
This tick focuses on the RP-1 matched-control denominator, control reuse, calipers,
and no-replacement sensitivity, with high-excitation optical-AGN rows useful for M2 P1.
All quantities are SDSS optical proxy/denominator measurements, not causal feedback claims.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

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

MARKER_BASE = "GORU_MATCHING_CONTROL_ROBUSTNESS_TICK"
PROXY_GUARD = (
    "SDSS optical emission-line/sSFR matched-control association only; no causal AGN feedback, "
    "gas-depletion, radio-jet coupling, outflow escape/recycling, X-ray heating, or simulation-validation proof."
)
SN_THRESHOLDS = [3, 5, 10]
RNG_SEED = 20260708
NO_REPL_K = 1024

TARGET_DEFS = [
    ("bpt_agn", "bpt_agn", "M1 RP-1", "BPT AGN versus BPT star-forming controls"),
    ("high_excitation_ygt0p25", "high_excitation_agn_ygt0p25", "M2 P1", "BPT AGN with log([O III]/Hbeta)>0.25 versus BPT star-forming controls"),
    ("nii_seyfert_like_proxy", "nii_seyfert_like_proxy", "M2 P1", "NII-BPT Seyfert-like proxy versus BPT star-forming controls"),
    ("nii_liner_like_proxy", "nii_liner_like_proxy", "M1 RP-1", "NII-BPT LINER-like proxy versus BPT star-forming controls"),
]

CALIPERS = [
    ("none", "no caliper; all nearest-neighbour pairs", None),
    ("scaled_distance_le_0p02", "scaled (logM,z) nearest-neighbour distance <= 0.02", lambda p: p["match_distance_scaled"] <= 0.02),
    ("scaled_distance_le_0p05", "scaled (logM,z) nearest-neighbour distance <= 0.05", lambda p: p["match_distance_scaled"] <= 0.05),
    ("scaled_distance_le_0p10", "scaled (logM,z) nearest-neighbour distance <= 0.10", lambda p: p["match_distance_scaled"] <= 0.10),
    ("mass_z_tight", "abs(delta logM)<=0.03 and abs(delta z)<=0.001", lambda p: (p["abs_delta_logM"] <= 0.03) & (p["abs_delta_z"] <= 0.001)),
    ("mass_z_moderate", "abs(delta logM)<=0.05 and abs(delta z)<=0.002", lambda p: (p["abs_delta_logM"] <= 0.05) & (p["abs_delta_z"] <= 0.002)),
    ("mass_z_loose", "abs(delta logM)<=0.10 and abs(delta z)<=0.005", lambda p: (p["abs_delta_logM"] <= 0.10) & (p["abs_delta_z"] <= 0.005)),
]


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


def bootstrap_ci(values: Any, func: Callable[[np.ndarray], float] = np.nanmedian, n_boot: int = 1200, seed: int = RNG_SEED) -> tuple[float | None, float | None]:
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    if len(arr) == 0:
        return None, None
    rng = np.random.default_rng(seed + len(arr))
    draws = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        sample = arr[rng.integers(0, len(arr), len(arr))]
        draws[i] = float(func(sample))
    return safe_float(np.percentile(draws, 2.5)), safe_float(np.percentile(draws, 97.5))


def smd(a: Any, b: Any) -> float | None:
    aa = np.asarray(a, dtype=float)
    bb = np.asarray(b, dtype=float)
    aa = aa[np.isfinite(aa)]
    bb = bb[np.isfinite(bb)]
    if len(aa) < 2 or len(bb) < 2:
        return None
    pooled = math.sqrt((float(np.var(aa, ddof=1)) + float(np.var(bb, ddof=1))) / 2.0)
    if pooled == 0:
        return 0.0
    return safe_float((float(np.mean(aa)) - float(np.mean(bb))) / pooled)


def load_sample() -> pd.DataFrame:
    if not SOURCE_CSV.exists():
        raise SystemExit(f"Missing cached source CSV: {SOURCE_CSV}")
    df = pd.read_csv(SOURCE_CSV)
    required = [
        "specObjID", "z", "lgm_tot_p50", "specsfr_tot_p50",
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
    df["bpt_sf"] = df["bpt_label"].eq("star-forming")
    df["bpt_agn"] = df["bpt_label"].eq("agn")
    x = df["log_nii_ha"].to_numpy(dtype=float)
    y = df["log_oiii_hb"].to_numpy(dtype=float)
    seyfert_line = 1.01 * x + 0.48
    df["high_excitation_agn_ygt0p25"] = df["bpt_agn"] & (df["log_oiii_hb"] > 0.25)
    df["nii_seyfert_like_proxy"] = df["bpt_agn"] & ((y - seyfert_line) >= 0)
    df["nii_liner_like_proxy"] = df["bpt_agn"] & ((y - seyfert_line) < 0)
    return df


def match_with_replacement(df: pd.DataFrame, target_col: str, control_col: str = "bpt_sf") -> pd.DataFrame:
    targets = df[df[target_col]].copy().reset_index(drop=True)
    controls = df[df[control_col]].copy().reset_index(drop=True)
    columns = [
        "target_specObjID", "control_specObjID", "target_logM", "control_logM", "target_z", "control_z",
        "target_log_sSFR", "control_log_sSFR", "delta_log_sSFR_target_minus_control",
        "match_distance_scaled", "abs_delta_logM", "abs_delta_z",
    ]
    if len(targets) < 1 or len(controls) < 1:
        return pd.DataFrame(columns=columns)
    features = ["lgm_tot_p50", "z"]
    scale = controls[features].std().replace(0, 1.0)
    center = controls[features].mean()
    control_scaled = ((controls[features] - center) / scale).to_numpy(dtype=float)
    target_scaled = ((targets[features] - center) / scale).to_numpy(dtype=float)
    tree = cKDTree(control_scaled)
    dist, idx = tree.query(target_scaled, k=1)
    ctrl = controls.iloc[np.asarray(idx, dtype=int)].reset_index(drop=True)
    out = pd.DataFrame({
        "target_specObjID": targets["specObjID"].astype(str).to_numpy(),
        "control_specObjID": ctrl["specObjID"].astype(str).to_numpy(),
        "target_logM": targets["lgm_tot_p50"].to_numpy(dtype=float),
        "control_logM": ctrl["lgm_tot_p50"].to_numpy(dtype=float),
        "target_z": targets["z"].to_numpy(dtype=float),
        "control_z": ctrl["z"].to_numpy(dtype=float),
        "target_log_sSFR": targets["specsfr_tot_p50"].to_numpy(dtype=float),
        "control_log_sSFR": ctrl["specsfr_tot_p50"].to_numpy(dtype=float),
        "match_distance_scaled": np.asarray(dist, dtype=float),
    })
    out["delta_log_sSFR_target_minus_control"] = out["target_log_sSFR"] - out["control_log_sSFR"]
    out["abs_delta_logM"] = (out["target_logM"] - out["control_logM"]).abs()
    out["abs_delta_z"] = (out["target_z"] - out["control_z"]).abs()
    return out


def match_greedy_without_replacement(df: pd.DataFrame, target_col: str, control_col: str = "bpt_sf", k_neighbors: int = NO_REPL_K) -> pd.DataFrame:
    targets = df[df[target_col]].copy().reset_index(drop=True)
    controls = df[df[control_col]].copy().reset_index(drop=True)
    if len(targets) < 1 or len(controls) < 1:
        return match_with_replacement(df.iloc[0:0].copy(), target_col, control_col)
    features = ["lgm_tot_p50", "z"]
    scale = controls[features].std().replace(0, 1.0)
    center = controls[features].mean()
    control_scaled = ((controls[features] - center) / scale).to_numpy(dtype=float)
    target_scaled = ((targets[features] - center) / scale).to_numpy(dtype=float)
    tree = cKDTree(control_scaled)
    k = max(1, min(k_neighbors, len(controls)))
    dists, idxs = tree.query(target_scaled, k=k)
    if k == 1:
        dists = dists[:, None]
        idxs = idxs[:, None]
    # Match harder targets first. This is a deterministic greedy diagnostic, not a global optimum.
    order = np.argsort(dists[:, 0])[::-1]
    used: set[int] = set()
    rows: list[dict[str, Any]] = []
    for ti in order:
        chosen_j: int | None = None
        chosen_d: float | None = None
        for cand_d, cand_j in zip(dists[ti], idxs[ti]):
            cj = int(cand_j)
            if cj not in used:
                chosen_j = cj
                chosen_d = float(cand_d)
                break
        if chosen_j is None:
            continue
        used.add(chosen_j)
        t = targets.iloc[ti]
        c = controls.iloc[chosen_j]
        rows.append({
            "target_specObjID": str(t["specObjID"]),
            "control_specObjID": str(c["specObjID"]),
            "target_logM": float(t["lgm_tot_p50"]),
            "control_logM": float(c["lgm_tot_p50"]),
            "target_z": float(t["z"]),
            "control_z": float(c["z"]),
            "target_log_sSFR": float(t["specsfr_tot_p50"]),
            "control_log_sSFR": float(c["specsfr_tot_p50"]),
            "match_distance_scaled": chosen_d,
            "delta_log_sSFR_target_minus_control": float(t["specsfr_tot_p50"] - c["specsfr_tot_p50"]),
            "abs_delta_logM": abs(float(t["lgm_tot_p50"] - c["lgm_tot_p50"])),
            "abs_delta_z": abs(float(t["z"] - c["z"])),
        })
    return pd.DataFrame(rows)


def pair_summary(
    pairs: pd.DataFrame,
    *,
    source_rows: int,
    target_n: int,
    control_n: int,
    sn_min_ge: int,
    target_variant: str,
    paper_scope: str,
    target_definition: str,
    matching_scheme: str,
    caliper_name: str,
    caliper_note: str,
) -> dict[str, Any]:
    n = int(len(pairs))
    out: dict[str, Any] = {
        "paper_scope": paper_scope,
        "target_variant": target_variant,
        "target_definition": target_definition,
        "sn_min_ge": sn_min_ge,
        "matching_scheme": matching_scheme,
        "caliper_name": caliper_name,
        "caliper_note": caliper_note,
        "source_rows_after_sn_cut": source_rows,
        "target_n": target_n,
        "control_n": control_n,
        "matched_pairs": n,
        "target_coverage_fraction": safe_float(n / target_n) if target_n else None,
        "median_delta_log_sSFR": None,
        "median_delta_ci95_low": None,
        "median_delta_ci95_high": None,
        "mean_delta_log_sSFR": None,
        "mean_delta_ci95_low": None,
        "mean_delta_ci95_high": None,
        "share_delta_negative": None,
        "unique_controls_used": 0,
        "effective_control_n_inverse_simpson": None,
        "max_control_reuse": 0,
        "controls_reused_ge2": 0,
        "pair_assignments_to_reused_controls_fraction": None,
        "match_distance_scaled_median": None,
        "match_distance_scaled_p90": None,
        "match_distance_scaled_p95": None,
        "match_abs_delta_logM_median": None,
        "match_abs_delta_logM_p95": None,
        "match_abs_delta_z_median": None,
        "match_abs_delta_z_p95": None,
        "smd_logM_target_minus_control": None,
        "smd_z_target_minus_control": None,
        "proxy_guard": PROXY_GUARD,
    }
    if n == 0:
        return out
    delta = pairs["delta_log_sSFR_target_minus_control"].to_numpy(dtype=float)
    med_lo, med_hi = bootstrap_ci(delta, np.nanmedian)
    mean_lo, mean_hi = bootstrap_ci(delta, np.nanmean)
    counts = pairs["control_specObjID"].value_counts()
    total_assignments = float(counts.sum())
    effective = (total_assignments * total_assignments / float(np.sum(counts.to_numpy(dtype=float) ** 2))) if total_assignments > 0 else None
    reused = counts[counts >= 2]
    assignments_to_reused = int(counts[counts >= 2].sum()) if len(reused) else 0
    out.update({
        "median_delta_log_sSFR": safe_float(np.nanmedian(delta)),
        "median_delta_ci95_low": med_lo,
        "median_delta_ci95_high": med_hi,
        "mean_delta_log_sSFR": safe_float(np.nanmean(delta)),
        "mean_delta_ci95_low": mean_lo,
        "mean_delta_ci95_high": mean_hi,
        "share_delta_negative": safe_float(np.nanmean(delta < 0)),
        "unique_controls_used": int(len(counts)),
        "effective_control_n_inverse_simpson": safe_float(effective),
        "max_control_reuse": int(counts.max()) if len(counts) else 0,
        "controls_reused_ge2": int((counts >= 2).sum()),
        "pair_assignments_to_reused_controls_fraction": safe_float(assignments_to_reused / n),
        "match_distance_scaled_median": safe_float(np.nanmedian(pairs["match_distance_scaled"])),
        "match_distance_scaled_p90": safe_float(np.nanpercentile(pairs["match_distance_scaled"], 90)),
        "match_distance_scaled_p95": safe_float(np.nanpercentile(pairs["match_distance_scaled"], 95)),
        "match_abs_delta_logM_median": safe_float(np.nanmedian(pairs["abs_delta_logM"])),
        "match_abs_delta_logM_p95": safe_float(np.nanpercentile(pairs["abs_delta_logM"], 95)),
        "match_abs_delta_z_median": safe_float(np.nanmedian(pairs["abs_delta_z"])),
        "match_abs_delta_z_p95": safe_float(np.nanpercentile(pairs["abs_delta_z"], 95)),
        "smd_logM_target_minus_control": smd(pairs["target_logM"], pairs["control_logM"]),
        "smd_z_target_minus_control": smd(pairs["target_z"], pairs["control_z"]),
    })
    return out


def control_reuse_rows(pairs: pd.DataFrame, df: pd.DataFrame, ts: str) -> list[dict[str, Any]]:
    if len(pairs) == 0:
        return []
    counts = pairs["control_specObjID"].value_counts().rename_axis("specObjID").reset_index(name="reuse_count")
    props = df[["specObjID", "lgm_tot_p50", "z", "specsfr_tot_p50", "log_nii_ha", "log_oiii_hb", "sn_min"]].copy()
    merged = counts.merge(props, on="specObjID", how="left")
    bins = [0, 1, 2, 4, 9, 19, np.inf]
    labels = ["1", "2", "3-4", "5-9", "10-19", "20+"]
    merged["reuse_bin"] = pd.cut(merged["reuse_count"], bins=bins, labels=labels, include_lowest=True).astype(str)
    out: list[dict[str, Any]] = []
    total_assignments = int(merged["reuse_count"].sum())
    for bin_name, g in merged.groupby("reuse_bin", observed=True):
        if len(g) == 0:
            continue
        out.append({
            "timestamp_utc": ts,
            "scope": "baseline_bpt_agn_sn_ge_3_nearest_replacement_controls",
            "reuse_bin": str(bin_name),
            "controls_in_bin": int(len(g)),
            "pair_assignments_in_bin": int(g["reuse_count"].sum()),
            "share_pair_assignments": safe_float(g["reuse_count"].sum() / total_assignments) if total_assignments else None,
            "median_reuse_count": safe_float(g["reuse_count"].median()),
            "max_reuse_count": int(g["reuse_count"].max()),
            "median_control_logM": safe_float(g["lgm_tot_p50"].median()),
            "median_control_z": safe_float(g["z"].median()),
            "median_control_log_sSFR": safe_float(g["specsfr_tot_p50"].median()),
            "median_control_sn_min": safe_float(g["sn_min"].median()),
            "proxy_guard": PROXY_GUARD,
        })
    return out


def concise_paper_rows(all_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    keep_specs = [
        ("M1 RP-1", "bpt_agn", 3, "nearest_replacement", "none"),
        ("M1 RP-1", "bpt_agn", 3, "nearest_replacement", "mass_z_moderate"),
        ("M1 RP-1", "bpt_agn", 3, f"greedy_without_replacement_hard_first_k{NO_REPL_K}", "none"),
        ("M1 RP-1", "bpt_agn", 5, "nearest_replacement", "none"),
        ("M1 RP-1", "bpt_agn", 10, "nearest_replacement", "none"),
        ("M2 P1", "high_excitation_ygt0p25", 3, "nearest_replacement", "none"),
        ("M2 P1", "high_excitation_ygt0p25", 3, f"greedy_without_replacement_hard_first_k{NO_REPL_K}", "none"),
        ("M2 P1", "nii_seyfert_like_proxy", 3, "nearest_replacement", "none"),
        ("M1 RP-1", "nii_liner_like_proxy", 3, "nearest_replacement", "none"),
    ]
    out: list[dict[str, Any]] = []
    for rank, spec in enumerate(keep_specs, start=1):
        paper, variant, sn, scheme, caliper = spec
        match = next((r for r in all_rows if r["paper_scope"] == paper and r["target_variant"] == variant and int(r["sn_min_ge"]) == sn and r["matching_scheme"] == scheme and r["caliper_name"] == caliper), None)
        if not match:
            continue
        out.append({
            "candidate_rank": rank,
            "paper_scope": match["paper_scope"],
            "target_variant": match["target_variant"],
            "sn_min_ge": match["sn_min_ge"],
            "matching_scheme": match["matching_scheme"],
            "caliper_name": match["caliper_name"],
            "target_n": match["target_n"],
            "matched_pairs": match["matched_pairs"],
            "target_coverage_fraction": match["target_coverage_fraction"],
            "unique_controls_used": match["unique_controls_used"],
            "effective_control_n_inverse_simpson": match["effective_control_n_inverse_simpson"],
            "max_control_reuse": match["max_control_reuse"],
            "median_delta_log_sSFR": match["median_delta_log_sSFR"],
            "median_delta_ci95_low": match["median_delta_ci95_low"],
            "median_delta_ci95_high": match["median_delta_ci95_high"],
            "match_abs_delta_logM_median": match["match_abs_delta_logM_median"],
            "match_abs_delta_z_median": match["match_abs_delta_z_median"],
            "table_note": "Matched in logM and z; association/proxy only. Use control-reuse columns to disclose replacement sensitivity.",
            "proxy_guard": PROXY_GUARD,
        })
    return out


def make_figures(all_rows: list[dict[str, Any]], reuse_rows: list[dict[str, Any]], out_dir: Path, ts: str) -> dict[str, str]:
    assert_goru_write(out_dir / "dummy")
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs: dict[str, str] = {}
    base = [
        r for r in all_rows
        if r["paper_scope"] == "M1 RP-1" and r["target_variant"] == "bpt_agn" and int(r["sn_min_ge"]) == 3 and r["matching_scheme"] == "nearest_replacement"
    ]
    order = ["none", "scaled_distance_le_0p02", "scaled_distance_le_0p05", "scaled_distance_le_0p10", "mass_z_tight", "mass_z_moderate", "mass_z_loose"]
    base = sorted(base, key=lambda r: order.index(r["caliper_name"]) if r["caliper_name"] in order else 99)
    if base:
        labels = [r["caliper_name"].replace("scaled_distance_", "dist_").replace("mass_z_", "mz_") for r in base]
        coverage = [float(r["target_coverage_fraction"] or 0) for r in base]
        med = [float(r["median_delta_log_sSFR"] or np.nan) for r in base]
        lo = [float(r["median_delta_log_sSFR"] - r["median_delta_ci95_low"]) if r["median_delta_log_sSFR"] is not None and r["median_delta_ci95_low"] is not None else 0 for r in base]
        hi = [float(r["median_delta_ci95_high"] - r["median_delta_log_sSFR"]) if r["median_delta_log_sSFR"] is not None and r["median_delta_ci95_high"] is not None else 0 for r in base]
        x = np.arange(len(labels))
        fig, ax1 = plt.subplots(figsize=(8.0, 4.6))
        ax1.bar(x, coverage, color="#4c78a8", alpha=0.75, label="target coverage")
        ax1.set_ylim(0, 1.05)
        ax1.set_ylabel("matched target coverage")
        ax1.set_xticks(x)
        ax1.set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
        ax2 = ax1.twinx()
        ax2.errorbar(x, med, yerr=[lo, hi], color="#e45756", marker="o", lw=1.4, capsize=3, label="median delta log sSFR")
        ax2.axhline(0, color="0.4", ls="--", lw=0.8)
        ax2.set_ylabel("median target-control log sSFR offset (dex)")
        fig.suptitle("RP-1 BPT-AGN matched-control caliper sensitivity (S/N>=3)", fontsize=11)
        fig.tight_layout()
        png = out_dir / f"matched_control_caliper_sensitivity_{ts}.png"
        pdf = out_dir / f"matched_control_caliper_sensitivity_{ts}.pdf"
        fig.savefig(png, dpi=220)
        fig.savefig(pdf)
        plt.close(fig)
        outputs["caliper_sensitivity_png"] = str(png)
        outputs["caliper_sensitivity_pdf"] = str(pdf)
    if reuse_rows:
        labels = [r["reuse_bin"] for r in reuse_rows]
        assignments = [int(r["pair_assignments_in_bin"]) for r in reuse_rows]
        controls = [int(r["controls_in_bin"]) for r in reuse_rows]
        x = np.arange(len(labels))
        width = 0.38
        fig, ax = plt.subplots(figsize=(6.8, 4.2))
        ax.bar(x - width / 2, controls, width, label="controls", color="#72b7b2")
        ax.bar(x + width / 2, assignments, width, label="pair assignments", color="#f58518")
        ax.set_yscale("log")
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_xlabel("reuse count bin")
        ax.set_ylabel("count (log scale)")
        ax.set_title("RP-1 baseline control reuse distribution")
        ax.legend(fontsize=8)
        fig.tight_layout()
        png = out_dir / f"control_reuse_histogram_{ts}.png"
        pdf = out_dir / f"control_reuse_histogram_{ts}.pdf"
        fig.savefig(png, dpi=220)
        fig.savefig(pdf)
        plt.close(fig)
        outputs["control_reuse_histogram_png"] = str(png)
        outputs["control_reuse_histogram_pdf"] = str(pdf)
    return outputs


def output_inventory(paths: dict[str, Path], fig_paths: dict[str, str], ts: str) -> list[dict[str, Any]]:
    merged: dict[str, str] = {k: str(v) for k, v in paths.items()}
    merged.update(fig_paths)
    rows: list[dict[str, Any]] = []
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
    source_results: dict[str, Any] = {}
    if SOURCE_RESULTS.exists():
        with SOURCE_RESULTS.open("r", encoding="utf-8") as f:
            source_results = json.load(f)

    all_rows: list[dict[str, Any]] = []
    baseline_pairs_for_reuse: pd.DataFrame | None = None
    for sn in SN_THRESHOLDS:
        sn_df = df[df["sn_min"] >= sn].copy()
        source_rows = int(len(sn_df))
        control_n = int(sn_df["bpt_sf"].sum())
        for target_variant, target_col, paper_scope, target_definition in TARGET_DEFS:
            target_n = int(sn_df[target_col].sum())
            repl_pairs = match_with_replacement(sn_df, target_col, "bpt_sf")
            if sn == 3 and target_variant == "bpt_agn":
                baseline_pairs_for_reuse = repl_pairs.copy()
            for caliper_name, caliper_note, filt in CALIPERS:
                if filt is None:
                    use_pairs = repl_pairs
                else:
                    use_pairs = repl_pairs[filt(repl_pairs)].copy() if len(repl_pairs) else repl_pairs
                all_rows.append(pair_summary(
                    use_pairs,
                    source_rows=source_rows,
                    target_n=target_n,
                    control_n=control_n,
                    sn_min_ge=sn,
                    target_variant=target_variant,
                    paper_scope=paper_scope,
                    target_definition=target_definition,
                    matching_scheme="nearest_replacement",
                    caliper_name=caliper_name,
                    caliper_note=caliper_note,
                ))
            if target_variant in {"bpt_agn", "high_excitation_ygt0p25"}:
                norepl_pairs = match_greedy_without_replacement(sn_df, target_col, "bpt_sf", NO_REPL_K)
                all_rows.append(pair_summary(
                    norepl_pairs,
                    source_rows=source_rows,
                    target_n=target_n,
                    control_n=control_n,
                    sn_min_ge=sn,
                    target_variant=target_variant,
                    paper_scope=paper_scope,
                    target_definition=target_definition,
                    matching_scheme=f"greedy_without_replacement_hard_first_k{NO_REPL_K}",
                    caliper_name="none",
                    caliper_note="deterministic greedy no-replacement diagnostic; not a global optimal assignment",
                ))

    reuse = control_reuse_rows(baseline_pairs_for_reuse if baseline_pairs_for_reuse is not None else pd.DataFrame(), df, ts)
    paper_rows = concise_paper_rows(all_rows)

    paths = {
        "matching_caliper_sensitivity_csv": tables_dir / f"matched_control_caliper_sensitivity_{ts}.csv",
        "control_reuse_distribution_csv": tables_dir / f"control_reuse_distribution_{ts}.csv",
        "paper_ready_matching_rows_csv": tables_dir / f"paper_ready_matching_rows_{ts}.csv",
        "inventory_csv": tables_dir / f"goru_matching_control_inventory_{ts}.csv",
        "summary_json": artifacts_dir / f"goru_matching_control_robustness_{ts}.json",
        "tick_report_md": ticks_dir / f"GORU_TICK_{ts}.md",
    }
    for p in paths.values():
        assert_goru_write(p)

    write_csv(paths["matching_caliper_sensitivity_csv"], all_rows)
    write_csv(paths["control_reuse_distribution_csv"], reuse)
    write_csv(paths["paper_ready_matching_rows_csv"], paper_rows)
    fig_paths = make_figures(all_rows, reuse, figures_dir, ts)
    expected_inventory_count = len([k for k in paths if k != "inventory_csv"]) + len(fig_paths)

    def lookup(paper: str, variant: str, sn: int, scheme: str, caliper: str) -> dict[str, Any]:
        return next(
            r for r in all_rows
            if r["paper_scope"] == paper and r["target_variant"] == variant and int(r["sn_min_ge"]) == sn and r["matching_scheme"] == scheme and r["caliper_name"] == caliper
        )

    baseline = lookup("M1 RP-1", "bpt_agn", 3, "nearest_replacement", "none")
    moderate = lookup("M1 RP-1", "bpt_agn", 3, "nearest_replacement", "mass_z_moderate")
    no_repl = lookup("M1 RP-1", "bpt_agn", 3, f"greedy_without_replacement_hard_first_k{NO_REPL_K}", "none")
    high_exc = lookup("M2 P1", "high_excitation_ygt0p25", 3, "nearest_replacement", "none")
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
            "matching_caliper_sensitivity": len(all_rows),
            "control_reuse_distribution": len(reuse),
            "paper_ready_matching_rows": len(paper_rows),
            "inventory": expected_inventory_count,
        },
        "key_results": {
            "rp1_baseline_bpt_agn_sn3_nearest_replacement": baseline,
            "rp1_mass_z_moderate_caliper": moderate,
            "rp1_greedy_without_replacement": no_repl,
            "m2p1_high_excitation_sn3_nearest_replacement": high_exc,
        },
        "outputs": outputs,
        "proxy_limits": PROXY_GUARD,
        "safety": "Read cached SDSS/local artifacts only; wrote under lanes/goru only. No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission.",
    }
    paths["summary_json"].write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    report = f"""# Goru matched-control robustness tick — {ts}

Marker: `{marker}`

## Work completed

- Read cached SDSS DR17-derived sample only (`analysis_sample_bpt.csv`, {len(df):,} rows) and local source summary metadata; no network, DB, API, deploy, git, cron, billing, OAuth, or external submission action.
- Generated lane-local RP-1 matched-control caliper/replacement diagnostics, control-reuse distribution, greedy no-replacement sensitivity, and high-excitation optical-AGN matching rows for M2 P1.
- Wrote CSV/JSON/figure inventory with hashes so manuscript lanes can disclose replacement sensitivity and strict-caliper attrition without editing public-linked PDFs.

## Key mechanical results

- Cached sample S/N counts: S/N>=3 = {sn_counts['sn_ge_3']:,}; S/N>=5 = {sn_counts['sn_ge_5']:,}; S/N>=10 = {sn_counts['sn_ge_10']:,}.
- RP-1 baseline BPT-AGN vs star-forming nearest-replacement match: {int(baseline['matched_pairs']):,}/{int(baseline['target_n']):,} targets covered, median delta log-sSFR {float(baseline['median_delta_log_sSFR']):.3f} dex (CI {float(baseline['median_delta_ci95_low']):.3f}, {float(baseline['median_delta_ci95_high']):.3f}); {int(baseline['unique_controls_used']):,} unique controls, effective control n {float(baseline['effective_control_n_inverse_simpson']):.1f}, max reuse {int(baseline['max_control_reuse'])}.
- RP-1 moderate abs(delta logM)<=0.05 and abs(delta z)<=0.002 caliper retains {int(moderate['matched_pairs']):,}/{int(moderate['target_n']):,} targets (coverage {float(moderate['target_coverage_fraction']):.3f}) with median delta {float(moderate['median_delta_log_sSFR']):.3f} dex.
- RP-1 greedy no-replacement diagnostic covers {int(no_repl['matched_pairs']):,}/{int(no_repl['target_n']):,} targets with median delta {float(no_repl['median_delta_log_sSFR']):.3f} dex; this is deterministic/hard-first, not a global optimal assignment.
- M2 P1 high-excitation optical-AGN nearest-replacement row covers {int(high_exc['matched_pairs']):,}/{int(high_exc['target_n']):,} targets with median delta {float(high_exc['median_delta_log_sSFR']):.3f} dex.

## Output artifacts

- summary_json: `{paths['summary_json']}`
- tick_report_md: `{paths['tick_report_md']}`
- matching_caliper_sensitivity_csv: `{paths['matching_caliper_sensitivity_csv']}`
- control_reuse_distribution_csv: `{paths['control_reuse_distribution_csv']}`
- paper_ready_matching_rows_csv: `{paths['paper_ready_matching_rows_csv']}`
- inventory_csv: `{paths['inventory_csv']}`
- caliper_figure: `{fig_paths.get('caliper_sensitivity_png')}`
- reuse_figure: `{fig_paths.get('control_reuse_histogram_png')}`

## Safety / interpretation guard

{PROXY_GUARD}

No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission changes. Lane-local writes only, with the separate required concise append to `OVERNIGHT_LEDGER.md` to be performed after verification.
"""
    paths["tick_report_md"].write_text(report, encoding="utf-8")
    inventory = output_inventory({k: v for k, v in paths.items() if k != "inventory_csv"}, fig_paths, ts)
    write_csv(paths["inventory_csv"], inventory)
    print(json.dumps({
        "marker": marker,
        "summary_json": str(paths["summary_json"]),
        "tick_report_md": str(paths["tick_report_md"]),
        "row_counts": summary["row_counts"],
        "key_values": {
            "rp1_baseline_delta": baseline["median_delta_log_sSFR"],
            "rp1_baseline_unique_controls": baseline["unique_controls_used"],
            "rp1_baseline_effective_control_n": baseline["effective_control_n_inverse_simpson"],
            "rp1_moderate_caliper_pairs": moderate["matched_pairs"],
            "rp1_no_replacement_delta": no_repl["median_delta_log_sSFR"],
            "m2p1_high_excitation_delta": high_exc["median_delta_log_sSFR"],
        },
        "outputs": outputs,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
