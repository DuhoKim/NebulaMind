#!/usr/bin/env python3
"""Goru lane: flux-error Monte Carlo BPT stability for the overnight 9-paper SDSS sample.

Reads only cached SDSS-derived local CSVs and writes Goru lane-local artifacts.
This tick quantifies how catalog line-flux uncertainties can move rows across
NII-BPT star-forming/intermediate/AGN/unclassified labels, then checks how much
of the already-cached RP-1 matched AGN-minus-SF offset survives when existing
matched pairs are filtered to high class-stability rows.

All quantities are SDSS optical emission-line proxy diagnostics. They are not
causal AGN feedback, gas-depletion, radio-jet, outflow-escape, X-ray heating,
or simulation-validation evidence.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import random
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
WORK_ROOT = AUTO / "overnight-9-papers-20260708"
GORU_ROOT = WORK_ROOT / "lanes/goru"
SOURCE_CSV = AUTO / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
MATCHED_CSV = AUTO / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv"

MARKER_BASE = "GORU_BPT_FLUX_ERROR_MONTE_CARLO_TICK"
BPT_ORDER = ["star-forming", "intermediate", "agn", "unclassified"]
N_DRAWS = 128
RNG_SEED = 20260708232006
BOOT_DRAWS = 400
STABILITY_THRESHOLDS = [0.50, 0.68, 0.84, 0.95]
PROXY_GUARD = (
    "SDSS optical emission-line flux-error/BPT stability and matched-pair association checks only; "
    "no causal AGN feedback, molecular gas depletion, radio-jet coupling, outflow escape/recycling, "
    "X-ray heating, or simulation-validation proof."
)
SAFETY = (
    "Read cached SDSS/local CSV artifacts only; wrote under overnight-9-papers-20260708/lanes/goru only. "
    "No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission."
)


def utc_ts() -> str:
    return os.environ.get("GORU_TICK_TS") or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def assert_goru_write(path: Path) -> None:
    resolved = path.resolve()
    goru = GORU_ROOT.resolve()
    if goru not in [resolved, *resolved.parents]:
        raise RuntimeError(f"Refusing non-Goru-lane write: {resolved}")


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


def write_text(path: Path, text: str) -> None:
    assert_goru_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    assert_goru_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def safe_float(value: Any) -> float | None:
    try:
        x = float(value)
    except Exception:
        return None
    return x if math.isfinite(x) else None


def fnum(row: dict[str, str], key: str) -> float:
    value = float(row[key])
    if not math.isfinite(value):
        raise ValueError(f"nonfinite {key}={row[key]!r}")
    return value


def safe_div(num: float, den: float) -> float | None:
    if den == 0:
        return None
    out = num / den
    return out if math.isfinite(out) else None


def ratio_log10(num: float, den: float) -> float | None:
    if num <= 0 or den <= 0:
        return None
    out = math.log10(num / den)
    return out if math.isfinite(out) else None


def bpt_label_from_xy(x: float | None, y: float | None) -> str:
    # Mirrors run_sdss_agn_sfr_pilot.py: Kauffmann/Kewley curves plus x>0.35 unclassified guard.
    if x is None or y is None or not math.isfinite(x) or not math.isfinite(y):
        return "unclassified"
    if x > 0.35:
        return "unclassified"
    label = "intermediate"
    try:
        kauffmann = 0.61 / (x - 0.05) + 1.30
        kewley = 0.61 / (x - 0.47) + 1.19
    except ZeroDivisionError:
        return "unclassified"
    if y < kauffmann:
        label = "star-forming"
    if y > kewley:
        label = "agn"
    return label


def median(values: Iterable[float]) -> float | None:
    vals = sorted(v for v in values if isinstance(v, (int, float)) and math.isfinite(v))
    if not vals:
        return None
    n = len(vals)
    mid = n // 2
    if n % 2:
        return float(vals[mid])
    return float((vals[mid - 1] + vals[mid]) / 2.0)


def mean(values: Iterable[float]) -> float | None:
    vals = [v for v in values if isinstance(v, (int, float)) and math.isfinite(v)]
    if not vals:
        return None
    return float(sum(vals) / len(vals))


def percentile(values: Iterable[float], pct: float) -> float | None:
    vals = sorted(v for v in values if isinstance(v, (int, float)) and math.isfinite(v))
    if not vals:
        return None
    if len(vals) == 1:
        return float(vals[0])
    pos = (len(vals) - 1) * pct / 100.0
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return float(vals[lo])
    frac = pos - lo
    return float(vals[lo] * (1 - frac) + vals[hi] * frac)


def bootstrap_median_ci(values: list[float], *, seed: int, draws: int = BOOT_DRAWS) -> tuple[float | None, float | None]:
    vals = [v for v in values if math.isfinite(v)]
    n = len(vals)
    if n == 0:
        return None, None
    rng = random.Random(seed + n)
    medians: list[float] = []
    for _ in range(draws):
        sample = [vals[rng.randrange(n)] for _ in range(n)]
        m = median(sample)
        if m is not None:
            medians.append(m)
    return percentile(medians, 2.5), percentile(medians, 97.5)


def ci_label(threshold: float) -> str:
    return str(threshold).replace(".", "p")


def sn_bin(sn_min: float) -> str:
    if sn_min < 5:
        return "3<=minSN<5"
    if sn_min < 10:
        return "5<=minSN<10"
    return "minSN>=10"


def load_sample() -> list[dict[str, Any]]:
    required = [
        "specObjID", "z", "lgm_tot_p50", "specsfr_tot_p50",
        "h_alpha_flux", "h_alpha_flux_err", "h_beta_flux", "h_beta_flux_err",
        "oiii_5007_flux", "oiii_5007_flux_err", "nii_6584_flux", "nii_6584_flux_err",
        "sn_ha", "sn_hb", "sn_oiii", "sn_nii", "log_nii_ha", "log_oiii_hb", "bpt_label",
    ]
    rows: list[dict[str, Any]] = []
    with SOURCE_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in required if c not in (reader.fieldnames or [])]
        if missing:
            raise SystemExit(f"Cached source CSV missing required columns: {missing}")
        for raw in reader:
            try:
                ha = fnum(raw, "h_alpha_flux")
                ha_err = fnum(raw, "h_alpha_flux_err")
                hb = fnum(raw, "h_beta_flux")
                hb_err = fnum(raw, "h_beta_flux_err")
                oiii = fnum(raw, "oiii_5007_flux")
                oiii_err = fnum(raw, "oiii_5007_flux_err")
                nii = fnum(raw, "nii_6584_flux")
                nii_err = fnum(raw, "nii_6584_flux_err")
                z = fnum(raw, "z")
                logm = fnum(raw, "lgm_tot_p50")
                logssfr = fnum(raw, "specsfr_tot_p50")
                sn_values = [fnum(raw, "sn_ha"), fnum(raw, "sn_hb"), fnum(raw, "sn_oiii"), fnum(raw, "sn_nii")]
                x = fnum(raw, "log_nii_ha")
                y = fnum(raw, "log_oiii_hb")
            except Exception:
                continue
            rows.append({
                "specObjID": str(raw["specObjID"]),
                "z": z,
                "logM": logm,
                "log_sSFR": logssfr,
                "ha": ha,
                "ha_err": ha_err,
                "hb": hb,
                "hb_err": hb_err,
                "oiii": oiii,
                "oiii_err": oiii_err,
                "nii": nii,
                "nii_err": nii_err,
                "sn_min": min(sn_values),
                "log_nii_ha": x,
                "log_oiii_hb": y,
                "bpt_label": raw["bpt_label"],
                "recomputed_bpt_label": bpt_label_from_xy(x, y),
            })
    return rows


def run_flux_mc(rows: list[dict[str, Any]]) -> dict[str, Any]:
    rng = random.Random(RNG_SEED)
    transition: Counter[tuple[str, str]] = Counter()
    recomputed_mismatches = 0
    row_probs: dict[str, dict[str, Any]] = {}
    class_counts = Counter(row["bpt_label"] for row in rows)
    recomputed_counts = Counter(row["recomputed_bpt_label"] for row in rows)
    for row in rows:
        orig = row["bpt_label"]
        if row["recomputed_bpt_label"] != orig:
            recomputed_mismatches += 1
        local: Counter[str] = Counter()
        for _ in range(N_DRAWS):
            ha = rng.gauss(row["ha"], row["ha_err"])
            hb = rng.gauss(row["hb"], row["hb_err"])
            oiii = rng.gauss(row["oiii"], row["oiii_err"])
            nii = rng.gauss(row["nii"], row["nii_err"])
            x = ratio_log10(nii, ha)
            y = ratio_log10(oiii, hb)
            label = bpt_label_from_xy(x, y)
            local[label] += 1
            transition[(orig, label)] += 1
        probs: dict[str, Any] = {label: local[label] / N_DRAWS for label in BPT_ORDER}
        probs["p_original"] = probs.get(orig, 0.0)
        probs["original_label"] = orig
        probs["sn_min"] = row["sn_min"]
        probs["sn_bin"] = sn_bin(row["sn_min"])
        probs["logM"] = row["logM"]
        probs["z"] = row["z"]
        probs["log_sSFR"] = row["log_sSFR"]
        row_probs[row["specObjID"]] = probs
    return {
        "transition": transition,
        "row_probs": row_probs,
        "class_counts": class_counts,
        "recomputed_counts": recomputed_counts,
        "recomputed_mismatches": recomputed_mismatches,
    }


def transition_rows(transition: Counter[tuple[str, str]], class_counts: Counter[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    total_draws = sum(transition.values())
    for orig in BPT_ORDER:
        orig_draws = class_counts[orig] * N_DRAWS
        for mc in BPT_ORDER:
            cnt = int(transition[(orig, mc)])
            rows.append({
                "deterministic_bpt_label": orig,
                "mc_bpt_label": mc,
                "source_rows_with_deterministic_label": int(class_counts[orig]),
                "draw_count": cnt,
                "expected_rows_from_draws": cnt / N_DRAWS,
                "fraction_within_deterministic_label_draws": (cnt / orig_draws) if orig_draws else None,
                "fraction_of_all_row_draws": (cnt / total_draws) if total_draws else None,
            })
    return rows


def stability_rows(row_probs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for p in row_probs.values():
        orig = p["original_label"]
        # Overlapping S/N threshold groups and disjoint bins.
        groups[("all", orig)].append(p)
        for threshold in [3, 5, 10]:
            if p["sn_min"] >= threshold:
                groups[(f"minSN>={threshold}", orig)].append(p)
        groups[(p["sn_bin"], orig)].append(p)
    order_sn = ["all", "minSN>=3", "minSN>=5", "minSN>=10", "3<=minSN<5", "5<=minSN<10", "minSN>=10"]
    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for sn_group in order_sn:
        for orig in BPT_ORDER:
            key = (sn_group, orig)
            if key in seen:
                continue
            seen.add(key)
            vals = groups.get(key, [])
            if not vals:
                continue
            p_orig_vals = [v["p_original"] for v in vals]
            row: dict[str, Any] = {
                "sn_group": sn_group,
                "deterministic_bpt_label": orig,
                "rows": len(vals),
                "median_p_original_label": median(p_orig_vals),
                "p10_p_original_label": percentile(p_orig_vals, 10),
                "p90_p_original_label": percentile(p_orig_vals, 90),
                "expected_mc_star_forming_rows": sum(v["star-forming"] for v in vals),
                "expected_mc_intermediate_rows": sum(v["intermediate"] for v in vals),
                "expected_mc_agn_rows": sum(v["agn"] for v in vals),
                "expected_mc_unclassified_rows": sum(v["unclassified"] for v in vals),
            }
            for threshold in STABILITY_THRESHOLDS:
                label = ci_label(threshold)
                n_ge = sum(1 for v in vals if v["p_original"] >= threshold)
                row[f"rows_p_original_ge_{label}"] = n_ge
                row[f"fraction_p_original_ge_{label}"] = n_ge / len(vals)
            rows.append(row)
    return rows


def load_matched_pairs() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with MATCHED_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for raw in reader:
            rows.append({
                "agn_specObjID": str(raw["agn_specObjID"]),
                "control_specObjID": str(raw["control_specObjID"]),
                "delta": float(raw["delta_log_sSFR_agn_minus_control"]),
                "distance": float(raw["match_distance_scaled"]),
            })
    return rows


def matched_sensitivity_rows(row_probs: dict[str, dict[str, Any]], pairs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for threshold in STABILITY_THRESHOLDS:
        vals: list[float] = []
        distances: list[float] = []
        missing = 0
        for pair in pairs:
            agn_p = row_probs.get(pair["agn_specObjID"])
            sf_p = row_probs.get(pair["control_specObjID"])
            if agn_p is None or sf_p is None:
                missing += 1
                continue
            if agn_p["agn"] >= threshold and sf_p["star-forming"] >= threshold:
                vals.append(pair["delta"])
                distances.append(pair["distance"])
        lo, hi = bootstrap_median_ci(vals, seed=RNG_SEED + int(threshold * 1000))
        rows.append({
            "paper_scope": "M1 RP-1",
            "matched_pair_filter": f"target p(AGN)>={threshold:.2f} and control p(SF)>={threshold:.2f} under {N_DRAWS}-draw flux-error MC",
            "threshold": threshold,
            "baseline_pairs": len(pairs),
            "retained_pairs": len(vals),
            "retained_fraction_of_baseline_pairs": (len(vals) / len(pairs)) if pairs else None,
            "missing_pair_ids": missing,
            "median_delta_log_sSFR_agn_minus_control": median(vals),
            "median_delta_bootstrap_ci95_low": lo,
            "median_delta_bootstrap_ci95_high": hi,
            "mean_delta_log_sSFR_agn_minus_control": mean(vals),
            "share_delta_negative": (sum(1 for v in vals if v < 0) / len(vals)) if vals else None,
            "median_match_distance_scaled": median(distances),
            "proxy_guard": PROXY_GUARD,
        })
    return rows


def paper_metric_rows(row_probs: dict[str, dict[str, Any]], class_counts: Counter[str]) -> list[dict[str, Any]]:
    probs = list(row_probs.values())
    rows: list[dict[str, Any]] = []
    rows.append({
        "metric": "deterministic_cached_bpt_counts",
        "all_rows": len(probs),
        "star_forming_rows": int(class_counts["star-forming"]),
        "intermediate_rows": int(class_counts["intermediate"]),
        "agn_rows": int(class_counts["agn"]),
        "unclassified_rows": int(class_counts["unclassified"]),
        "interpretation_guard": PROXY_GUARD,
    })
    rows.append({
        "metric": f"expected_counts_from_{N_DRAWS}_draw_flux_error_mc",
        "all_rows": len(probs),
        "star_forming_rows": sum(p["star-forming"] for p in probs),
        "intermediate_rows": sum(p["intermediate"] for p in probs),
        "agn_rows": sum(p["agn"] for p in probs),
        "unclassified_rows": sum(p["unclassified"] for p in probs),
        "interpretation_guard": PROXY_GUARD,
    })
    for threshold in STABILITY_THRESHOLDS:
        rows.append({
            "metric": f"row_level_high_confidence_probability_ge_{threshold:.2f}",
            "all_rows": len(probs),
            "star_forming_rows": sum(1 for p in probs if p["star-forming"] >= threshold),
            "intermediate_rows": sum(1 for p in probs if p["intermediate"] >= threshold),
            "agn_rows": sum(1 for p in probs if p["agn"] >= threshold),
            "unclassified_rows": sum(1 for p in probs if p["unclassified"] >= threshold),
            "original_label_stable_rows": sum(1 for p in probs if p["p_original"] >= threshold),
            "original_label_unstable_rows": sum(1 for p in probs if p["p_original"] < threshold),
            "interpretation_guard": PROXY_GUARD,
        })
    return rows


def line_snr_rows(rows: list[dict[str, Any]], row_probs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    by_group: dict[tuple[str, str], list[float]] = defaultdict(list)
    by_porig: dict[tuple[str, str], list[float]] = defaultdict(list)
    for row in rows:
        orig = row["bpt_label"]
        p = row_probs[row["specObjID"]]
        for group in ["all", sn_bin(row["sn_min"]), "minSN>=5" if row["sn_min"] >= 5 else "minSN<5", "minSN>=10" if row["sn_min"] >= 10 else "minSN<10"]:
            by_group[(group, orig)].append(row["sn_min"])
            by_porig[(group, orig)].append(p["p_original"])
    out: list[dict[str, Any]] = []
    for (group, orig), vals in sorted(by_group.items()):
        out.append({
            "sn_group": group,
            "deterministic_bpt_label": orig,
            "rows": len(vals),
            "sn_min_median": median(vals),
            "sn_min_p10": percentile(vals, 10),
            "sn_min_p90": percentile(vals, 90),
            "p_original_median": median(by_porig[(group, orig)]),
            "p_original_p10": percentile(by_porig[(group, orig)], 10),
            "p_original_p90": percentile(by_porig[(group, orig)], 90),
        })
    return out


def make_svg(path: Path, stability: list[dict[str, Any]]) -> None:
    assert_goru_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    wanted_groups = ["all", "3<=minSN<5", "5<=minSN<10", "minSN>=10"]
    wanted_classes = ["star-forming", "intermediate", "agn"]
    by_key = {(r["sn_group"], r["deterministic_bpt_label"]): r for r in stability}
    bar_w = 32
    gap = 10
    group_gap = 42
    left = 72
    top = 44
    plot_h = 210
    width = left + len(wanted_groups) * (len(wanted_classes) * (bar_w + gap) + group_gap) + 40
    height = 360
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="20" y="24" font-family="Arial" font-size="15" font-weight="bold">BPT label stability under 128-draw line-flux perturbations</text>',
        f'<line x1="{left}" y1="{top+plot_h}" x2="{width-28}" y2="{top+plot_h}" stroke="#333"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}" stroke="#333"/>',
    ]
    for frac in [0.0, 0.25, 0.5, 0.75, 1.0]:
        y = top + plot_h * (1 - frac)
        parts.append(f'<line x1="{left-4}" y1="{y:.1f}" x2="{width-28}" y2="{y:.1f}" stroke="#ddd"/>')
        parts.append(f'<text x="18" y="{y+4:.1f}" font-family="Arial" font-size="11">{frac:.2f}</text>')
    colors = {"star-forming": "#4c78a8", "intermediate": "#f58518", "agn": "#e45756"}
    x = left + 12
    for group in wanted_groups:
        gx0 = x
        for cls in wanted_classes:
            r = by_key.get((group, cls))
            frac = 0.0
            rows = 0
            if r:
                frac = float(r.get("fraction_p_original_ge_0p84") or 0.0)
                rows = int(r.get("rows") or 0)
            h = plot_h * max(0.0, min(1.0, frac))
            y = top + plot_h - h
            parts.append(f'<rect x="{x}" y="{y:.1f}" width="{bar_w}" height="{h:.1f}" fill="{colors[cls]}"/>')
            parts.append(f'<text transform="translate({x+bar_w/2:.1f},{top+plot_h+45}) rotate(-50)" text-anchor="end" font-family="Arial" font-size="10">{cls}</text>')
            parts.append(f'<text x="{x+bar_w/2:.1f}" y="{max(y-3, top+10):.1f}" text-anchor="middle" font-family="Arial" font-size="9">{frac:.2f}</text>')
            parts.append(f'<text x="{x+bar_w/2:.1f}" y="{top+plot_h+12}" text-anchor="middle" font-family="Arial" font-size="8">n={rows}</text>')
            x += bar_w + gap
        parts.append(f'<text x="{(gx0+x-gap)/2:.1f}" y="{height-18}" text-anchor="middle" font-family="Arial" font-size="11">{group}</text>')
        x += group_gap
    parts.append('<text x="20" y="340" font-family="Arial" font-size="11">Bar height: fraction of rows whose original deterministic BPT label has MC probability >=0.84. Optical proxy only.</text>')
    parts.append('</svg>')
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def inventory_rows(outputs: dict[str, Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for name, path in sorted(outputs.items()):
        exists = path.exists()
        rows.append({
            "artifact_name": name,
            "path": str(path),
            "exists": exists,
            "bytes": path.stat().st_size if exists else None,
            "sha256": "SELF_REFERENTIAL_OMITTED" if name == "inventory_csv" and exists else (sha256_path(path) if exists else None),
        })
    return rows


def main() -> None:
    ts = utc_ts()
    marker = f"{MARKER_BASE}_{ts}"
    for sub in ["scripts", "tables", "artifacts", "figures", "ticks"]:
        (GORU_ROOT / sub).mkdir(parents=True, exist_ok=True)

    rows = load_sample()
    mc = run_flux_mc(rows)
    trans = transition_rows(mc["transition"], mc["class_counts"])
    stability = stability_rows(mc["row_probs"])
    matched_pairs = load_matched_pairs()
    matched = matched_sensitivity_rows(mc["row_probs"], matched_pairs)
    paper_metrics = paper_metric_rows(mc["row_probs"], mc["class_counts"])
    sn_summary = line_snr_rows(rows, mc["row_probs"])

    transition_csv = GORU_ROOT / "tables" / f"bpt_flux_error_mc_transition_{ts}.csv"
    stability_csv = GORU_ROOT / "tables" / f"bpt_flux_error_mc_stability_by_sn_{ts}.csv"
    matched_csv = GORU_ROOT / "tables" / f"bpt_flux_error_mc_matched_pair_sensitivity_{ts}.csv"
    paper_metrics_csv = GORU_ROOT / "tables" / f"bpt_flux_error_mc_paper_metrics_{ts}.csv"
    sn_summary_csv = GORU_ROOT / "tables" / f"bpt_flux_error_mc_sn_summary_{ts}.csv"
    figure_svg = GORU_ROOT / "figures" / f"bpt_flux_error_mc_stability_{ts}.svg"
    summary_json = GORU_ROOT / "artifacts" / f"goru_bpt_flux_error_mc_{ts}.json"
    inventory_csv = GORU_ROOT / "tables" / f"goru_bpt_flux_error_mc_inventory_{ts}.csv"
    tick_report = GORU_ROOT / "ticks" / f"GORU_TICK_{ts}.md"
    script_path = Path(__file__).resolve()

    write_csv(transition_csv, trans)
    write_csv(stability_csv, stability)
    write_csv(matched_csv, matched)
    write_csv(paper_metrics_csv, paper_metrics)
    write_csv(sn_summary_csv, sn_summary)
    make_svg(figure_svg, stability)

    class_counts = {label: int(mc["class_counts"][label]) for label in BPT_ORDER}
    expected_counts = {
        label: sum(p[label] for p in mc["row_probs"].values()) for label in BPT_ORDER
    }
    stable84 = {
        label: sum(1 for p in mc["row_probs"].values() if p["original_label"] == label and p["p_original"] >= 0.84)
        for label in BPT_ORDER
    }
    key_matched = {str(r["threshold"]): r for r in matched}
    key_results = {
        "source_rows": len(rows),
        "monte_carlo_draws_per_row": N_DRAWS,
        "total_row_draws": len(rows) * N_DRAWS,
        "deterministic_bpt_counts": class_counts,
        "expected_mc_bpt_counts": expected_counts,
        "recomputed_bpt_mismatches_vs_cached_label": int(mc["recomputed_mismatches"]),
        "stable_original_label_rows_p_ge_0p84": stable84,
        "rp1_baseline_matched_pairs": len(matched_pairs),
        "rp1_matched_pair_stability_threshold_0p84": key_matched.get("0.84"),
        "rp1_matched_pair_stability_threshold_0p95": key_matched.get("0.95"),
    }

    outputs: dict[str, Path] = {
        "script": script_path,
        "transition_csv": transition_csv,
        "stability_csv": stability_csv,
        "matched_pair_sensitivity_csv": matched_csv,
        "paper_metrics_csv": paper_metrics_csv,
        "sn_summary_csv": sn_summary_csv,
        "stability_svg": figure_svg,
        "summary_json": summary_json,
        "inventory_csv": inventory_csv,
        "tick_report_md": tick_report,
    }

    summary_payload = {
        "marker": marker,
        "timestamp_utc": ts,
        "source_csv": str(SOURCE_CSV),
        "source_csv_sha256": sha256_path(SOURCE_CSV),
        "matched_pairs_csv": str(MATCHED_CSV),
        "matched_pairs_csv_sha256": sha256_path(MATCHED_CSV),
        "method": {
            "draws_per_row": N_DRAWS,
            "rng_seed": RNG_SEED,
            "bpt_classification": "Mirrors run_sdss_agn_sfr_pilot.py: Kauffmann/Kewley NII-BPT curves plus x=log([NII]/Halpha)>0.35 unclassified guard.",
            "matched_pair_sensitivity": "Filters existing cached RP-1 nearest-neighbour matched AGN/SF pairs by MC class-stability probabilities; it does not rematch after perturbation.",
        },
        "key_results": key_results,
        "row_counts": {
            "transition_rows": len(trans),
            "stability_rows": len(stability),
            "matched_pair_sensitivity_rows": len(matched),
            "paper_metrics_rows": len(paper_metrics),
            "sn_summary_rows": len(sn_summary),
        },
        "outputs": {name: str(path) for name, path in outputs.items()},
        "proxy_limits": PROXY_GUARD,
        "safety": SAFETY,
    }
    write_json(summary_json, summary_payload)
    # Inventory after summary exists.
    write_csv(inventory_csv, inventory_rows(outputs))

    matched84 = key_matched.get("0.84") or {}
    matched95 = key_matched.get("0.95") or {}
    report = f"""# Goru BPT flux-error Monte Carlo tick — {ts}

Marker: `{marker}`

## Work completed

- Read cached SDSS DR17-derived sample only (`analysis_sample_bpt.csv`, {len(rows):,} rows) plus cached RP-1 matched-pairs CSV ({len(matched_pairs):,} rows); no network, DB, API, deploy, git, cron, billing, OAuth, or external submission action.
- Ran a reproducible {N_DRAWS}-draw per-row Gaussian flux-error perturbation of H-alpha, H-beta, [O III] 5007, and [N II] 6584, using the same cached NII-BPT demarcation logic as the original pilot.
- Wrote lane-local CSV/JSON/SVG inventory so manuscript lanes can disclose BPT class-stability limits and filter existing RP-1 matched-pair offsets by high class-confidence rows.

## Key mechanical results

- Deterministic cached BPT counts: star-forming {class_counts['star-forming']:,}; intermediate {class_counts['intermediate']:,}; AGN {class_counts['agn']:,}; unclassified {class_counts['unclassified']:,}; recomputed-label mismatches versus cached label {mc['recomputed_mismatches']}.
- Expected MC counts over {N_DRAWS} flux-error draws/row: star-forming {expected_counts['star-forming']:.1f}; intermediate {expected_counts['intermediate']:.1f}; AGN {expected_counts['agn']:.1f}; unclassified {expected_counts['unclassified']:.1f}.
- Original-label stability p>=0.84 rows: star-forming {stable84['star-forming']:,}/{class_counts['star-forming']:,}; intermediate {stable84['intermediate']:,}/{class_counts['intermediate']:,}; AGN {stable84['agn']:,}/{class_counts['agn']:,}; unclassified {stable84['unclassified']:,}/{class_counts['unclassified']:,}.
- RP-1 existing matched pairs retained with target p(AGN)>=0.84 and control p(SF)>=0.84: {matched84.get('retained_pairs'):,}/{len(matched_pairs):,} with median delta log-sSFR {matched84.get('median_delta_log_sSFR_agn_minus_control'):.3f} dex (bootstrap CI {matched84.get('median_delta_bootstrap_ci95_low'):.3f}, {matched84.get('median_delta_bootstrap_ci95_high'):.3f}).
- Stricter p>=0.95 filter retains {matched95.get('retained_pairs'):,}/{len(matched_pairs):,} pairs; median delta {matched95.get('median_delta_log_sSFR_agn_minus_control'):.3f} dex.

## Output artifacts

- summary_json: `{summary_json}`
- tick_report_md: `{tick_report}`
- transition_csv: `{transition_csv}`
- stability_csv: `{stability_csv}`
- matched_pair_sensitivity_csv: `{matched_csv}`
- paper_metrics_csv: `{paper_metrics_csv}`
- sn_summary_csv: `{sn_summary_csv}`
- stability_svg: `{figure_svg}`
- inventory_csv: `{inventory_csv}`

## Safety / interpretation guard

{PROXY_GUARD}

{SAFETY}
"""
    write_text(tick_report, report)

    # Refresh summary/inventory now that tick report exists and inventory CSV has final content.
    write_json(summary_json, summary_payload)
    write_csv(inventory_csv, inventory_rows(outputs))

    print(json.dumps({
        "marker": marker,
        "tick_report": str(tick_report),
        "summary_json": str(summary_json),
        "source_rows": len(rows),
        "draws_per_row": N_DRAWS,
        "rp1_pairs_p84": matched84.get("retained_pairs"),
        "rp1_median_delta_p84": matched84.get("median_delta_log_sSFR_agn_minus_control"),
        "safety": SAFETY,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
