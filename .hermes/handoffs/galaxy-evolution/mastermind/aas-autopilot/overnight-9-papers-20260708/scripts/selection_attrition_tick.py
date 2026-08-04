#!/usr/bin/env python3
"""Read-only SDSS selection-function attrition tick for the 9-paper overnight run.

Writes durable lane-local artifacts only. Uses public SDSS DR17 SkyServer SQL
counts; does not write to NebulaMind product DB/API/git/live/public roots.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Tuple

WORK_ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708")
SOURCE_CSV = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv")
RUN_MARKER = "SELECTION_FUNCTION_ATTRITION_TICK"
BASE_URL = "https://skyserver.sdss.org/dr17/SkyServerWS/SearchTools/SqlSearch"

BASE_SPEC = "s.class='GALAXY' AND s.z BETWEEN 0.02 AND 0.12"
MASS_SFR = "x.lgm_tot_p50 BETWEEN 8.0 AND 12.5 AND x.specsfr_tot_p50 BETWEEN -14.0 AND -7.0"
POSITIVE_LINES = " AND ".join([
    "l.h_alpha_flux > 0", "l.h_beta_flux > 0", "l.oiii_5007_flux > 0", "l.nii_6584_flux > 0",
    "l.h_alpha_flux_err > 0", "l.h_beta_flux_err > 0", "l.oiii_5007_flux_err > 0", "l.nii_6584_flux_err > 0",
])

def sn_cond(threshold: float) -> str:
    t = f"{threshold:.1f}"
    return " AND ".join([
        POSITIVE_LINES,
        f"l.h_alpha_flux / l.h_alpha_flux_err >= {t}",
        f"l.h_beta_flux / l.h_beta_flux_err >= {t}",
        f"l.oiii_5007_flux / l.oiii_5007_flux_err >= {t}",
        f"l.nii_6584_flux / l.nii_6584_flux_err >= {t}",
    ])

SPEC_FROM = "FROM SpecObj AS s"
EXTRA_FROM = (
    "FROM SpecObj AS s "
    "JOIN galSpecInfo AS i ON s.specObjID=i.specObjID "
    "JOIN PhotoObj AS p ON s.bestObjID=p.objID "
    "JOIN galSpecExtra AS x ON s.specObjID=x.specObjID"
)
LINE_FROM = EXTRA_FROM + " JOIN galSpecLine AS l ON s.specObjID=l.specObjID"

def q_count(from_clause: str, where_clause: str) -> str:
    return f"(SELECT COUNT(*) {from_clause} WHERE {where_clause})"


def safe_int(v: Any) -> int:
    if v is None or v == "":
        return 0
    return int(float(v))


def safe_float(v: Any) -> float:
    if v is None or v == "":
        return float("nan")
    return float(v)


def pct(n: int, d: int) -> str:
    if not d:
        return ""
    return f"{100.0*n/d:.2f}%"


def frac(n: int, d: int) -> float | None:
    return None if not d else n / d


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_csv(path: Path, fieldnames: List[str], rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow(row)


def read_local_rows() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with SOURCE_CSV.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                row["_z"] = safe_float(row["z"])
                row["_logm"] = safe_float(row["lgm_tot_p50"])
                row["_ssfr"] = safe_float(row["specsfr_tot_p50"])
                sns = [
                    safe_float(row["h_alpha_flux"]) / safe_float(row["h_alpha_flux_err"]),
                    safe_float(row["h_beta_flux"]) / safe_float(row["h_beta_flux_err"]),
                    safe_float(row["oiii_5007_flux"]) / safe_float(row["oiii_5007_flux_err"]),
                    safe_float(row["nii_6584_flux"]) / safe_float(row["nii_6584_flux_err"]),
                ]
                row["_sn_min"] = min(sns)
            except Exception:
                row["_z"] = row["_logm"] = row["_ssfr"] = row["_sn_min"] = float("nan")
            rows.append(row)
    return rows


def local_count(rows: Iterable[Dict[str, Any]], pred: Callable[[Dict[str, Any]], bool]) -> int:
    return sum(1 for row in rows if pred(row))


def fetch_sdss_json(name: str, sql: str, raw_dir: Path, timeout: int = 90) -> Dict[str, Any]:
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / f"{name}.sql").write_text(sql + "\n", encoding="utf-8")
    url = BASE_URL + "?" + urllib.parse.urlencode({"cmd": sql, "format": "json"})
    with urllib.request.urlopen(url, timeout=timeout) as response:
        payload = response.read()
    (raw_dir / f"{name}.json").write_bytes(payload)
    parsed = json.loads(payload.decode("utf-8"))
    if not isinstance(parsed, list) or not parsed or "Rows" not in parsed[0]:
        raise RuntimeError(f"Unexpected SDSS JSON shape for {name}: {parsed!r}")
    rows = parsed[0]["Rows"]
    if not rows:
        raise RuntimeError(f"No rows in SDSS JSON for {name}")
    return rows[0]


def count_query_sql(name_to_expr: Dict[str, str]) -> str:
    cols = [f"{expr} AS {name}" for name, expr in name_to_expr.items()]
    return "SELECT\n  " + ",\n  ".join(cols)


def main() -> int:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = WORK_ROOT / "lanes" / "tori" / "selection-function-attrition" / ts
    raw_dir = out_dir / "raw_sdss_payloads"
    tables_dir = out_dir / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)

    local_rows = read_local_rows()

    # 1) Global stage-count query: exact public DR17 counts for the pilot selection cascade.
    stage_sql = count_query_sql({
        "spectro_galaxy_z_window": q_count(SPEC_FROM, BASE_SPEC),
        "join_complete_mass_ssfr_bounds": q_count(EXTRA_FROM, f"{BASE_SPEC} AND {MASS_SFR}"),
        "join_complete_with_line_table": q_count(LINE_FROM, f"{BASE_SPEC} AND {MASS_SFR}"),
        "positive_four_bpt_fluxes_and_errors": q_count(LINE_FROM, f"{BASE_SPEC} AND {MASS_SFR} AND {POSITIVE_LINES}"),
        "sn_ge_3_four_bpt_lines": q_count(LINE_FROM, f"{BASE_SPEC} AND {MASS_SFR} AND {sn_cond(3.0)}"),
        "sn_ge_5_four_bpt_lines": q_count(LINE_FROM, f"{BASE_SPEC} AND {MASS_SFR} AND {sn_cond(5.0)}"),
        "sn_ge_10_four_bpt_lines": q_count(LINE_FROM, f"{BASE_SPEC} AND {MASS_SFR} AND {sn_cond(10.0)}"),
    })
    stage_counts_raw = fetch_sdss_json("global_selection_stage_counts", stage_sql, raw_dir)
    time.sleep(0.25)

    cached_total = len(local_rows)
    stage_rows: List[Dict[str, Any]] = []
    stage_order = [
        ("spectro_galaxy_z_window", "SpecObj GALAXY, 0.02<z<0.12"),
        ("join_complete_mass_ssfr_bounds", "plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds"),
        ("join_complete_with_line_table", "plus galSpecLine join"),
        ("positive_four_bpt_fluxes_and_errors", "four BPT lines positive with positive errors"),
        ("sn_ge_3_four_bpt_lines", "four BPT lines S/N>=3"),
        ("sn_ge_5_four_bpt_lines", "four BPT lines S/N>=5"),
        ("sn_ge_10_four_bpt_lines", "four BPT lines S/N>=10"),
    ]
    stage_sql_counts = {k: safe_int(stage_counts_raw.get(k)) for k, _ in stage_order}
    previous = None
    for key, label in stage_order:
        sql_n = stage_sql_counts[key]
        cached_n = ""
        if key == "sn_ge_3_four_bpt_lines":
            cached_n = cached_total
        elif key == "sn_ge_5_four_bpt_lines":
            cached_n = local_count(local_rows, lambda r: r["_sn_min"] >= 5.0)
        elif key == "sn_ge_10_four_bpt_lines":
            cached_n = local_count(local_rows, lambda r: r["_sn_min"] >= 10.0)
        elif key == "positive_four_bpt_fluxes_and_errors":
            cached_n = cached_total
        retention_from_prev = "" if previous is None or previous == 0 else sql_n / previous
        stage_rows.append({
            "stage_key": key,
            "stage_label": label,
            "sdss_dr17_count": sql_n,
            "retention_vs_previous_stage": retention_from_prev,
            "retention_vs_spectro_z_parent": frac(sql_n, stage_sql_counts["spectro_galaxy_z_window"]),
            "cached_sample_count_at_matching_stage": cached_n,
            "cached_coverage_of_sdss_stage": ("" if cached_n == "" or sql_n == 0 else int(cached_n) / sql_n),
            "source_note": "Public SDSS DR17 SkyServer SQL count; cached sample is TOP 60000 ORDER BY specObjID for the S/N>=3 stage.",
        })
        previous = sql_n

    stage_csv = tables_dir / f"selection_stage_counts_{ts}.csv"
    write_csv(stage_csv, list(stage_rows[0].keys()), stage_rows)

    # 2) Massive low-sSFR attrition, focused on the M3 P2 gas-depletion denominator critique.
    mass_cuts = [10.6, 10.8, 11.0]
    ssfr_cuts = [-10.7, -11.0]
    gas_rows: List[Dict[str, Any]] = []
    for mcut in mass_cuts:
        for scut in ssfr_cuts:
            subset = f"{BASE_SPEC} AND x.lgm_tot_p50 >= {mcut:.1f} AND x.specsfr_tot_p50 < {scut:.1f} AND {MASS_SFR}"
            sql = count_query_sql({
                "parent_mass_ssfr": q_count(EXTRA_FROM, subset),
                "positive_lines": q_count(LINE_FROM, f"{subset} AND {POSITIVE_LINES}"),
                "sn_ge_3": q_count(LINE_FROM, f"{subset} AND {sn_cond(3.0)}"),
                "sn_ge_5": q_count(LINE_FROM, f"{subset} AND {sn_cond(5.0)}"),
                "sn_ge_10": q_count(LINE_FROM, f"{subset} AND {sn_cond(10.0)}"),
            })
            raw = fetch_sdss_json(f"gas_denominator_m{str(mcut).replace('.', 'p')}_ssfr_lt_{str(abs(scut)).replace('.', 'p')}", sql, raw_dir)
            time.sleep(0.25)
            parent = safe_int(raw["parent_mass_ssfr"])
            sn3 = safe_int(raw["sn_ge_3"])
            sn5 = safe_int(raw["sn_ge_5"])
            sn10 = safe_int(raw["sn_ge_10"])
            local_sn3 = local_count(local_rows, lambda r, mc=mcut, sc=scut: r["_logm"] >= mc and r["_ssfr"] < sc and r["_sn_min"] >= 3.0)
            local_sn5 = local_count(local_rows, lambda r, mc=mcut, sc=scut: r["_logm"] >= mc and r["_ssfr"] < sc and r["_sn_min"] >= 5.0)
            local_sn10 = local_count(local_rows, lambda r, mc=mcut, sc=scut: r["_logm"] >= mc and r["_ssfr"] < sc and r["_sn_min"] >= 10.0)
            gas_rows.append({
                "mass_cut_logM_ge": f"{mcut:.1f}",
                "ssfr_cut_log_ssfr_lt": f"{scut:.1f}",
                "sdss_parent_mass_ssfr_count": parent,
                "sdss_positive_line_count": safe_int(raw["positive_lines"]),
                "sdss_sn_ge_3_count": sn3,
                "sdss_sn_ge_5_count": sn5,
                "sdss_sn_ge_10_count": sn10,
                "sn_ge_3_retention_vs_parent": frac(sn3, parent),
                "sn_ge_5_retention_vs_parent": frac(sn5, parent),
                "sn_ge_10_retention_vs_parent": frac(sn10, parent),
                "cached_sn_ge_3_count": local_sn3,
                "cached_sn_ge_5_count": local_sn5,
                "cached_sn_ge_10_count": local_sn10,
                "cached_coverage_of_sdss_sn_ge_3": frac(local_sn3, sn3),
                "interpretation_guard": "Emission-line detected massive low-sSFR denominator only; not molecular gas depletion or SFE.",
            })
    gas_csv = tables_dir / f"m3_p2_massive_low_ssfr_attrition_{ts}.csv"
    write_csv(gas_csv, list(gas_rows[0].keys()), gas_rows)

    # 3) Massive-host attrition for maintenance/radio-jet denominator papers.
    massive_rows: List[Dict[str, Any]] = []
    for mcut in mass_cuts:
        subset = f"{BASE_SPEC} AND x.lgm_tot_p50 >= {mcut:.1f} AND {MASS_SFR}"
        sql = count_query_sql({
            "parent_mass": q_count(EXTRA_FROM, subset),
            "sn_ge_3": q_count(LINE_FROM, f"{subset} AND {sn_cond(3.0)}"),
            "sn_ge_5": q_count(LINE_FROM, f"{subset} AND {sn_cond(5.0)}"),
            "sn_ge_10": q_count(LINE_FROM, f"{subset} AND {sn_cond(10.0)}"),
        })
        raw = fetch_sdss_json(f"massive_host_attrition_m{str(mcut).replace('.', 'p')}", sql, raw_dir)
        time.sleep(0.25)
        parent = safe_int(raw["parent_mass"])
        sn3 = safe_int(raw["sn_ge_3"])
        massive_rows.append({
            "mass_cut_logM_ge": f"{mcut:.1f}",
            "sdss_parent_mass_count": parent,
            "sdss_sn_ge_3_count": sn3,
            "sdss_sn_ge_5_count": safe_int(raw["sn_ge_5"]),
            "sdss_sn_ge_10_count": safe_int(raw["sn_ge_10"]),
            "sn_ge_3_retention_vs_parent": frac(sn3, parent),
            "cached_sn_ge_3_count": local_count(local_rows, lambda r, mc=mcut: r["_logm"] >= mc and r["_sn_min"] >= 3.0),
            "cached_coverage_of_sdss_sn_ge_3": frac(local_count(local_rows, lambda r, mc=mcut: r["_logm"] >= mc and r["_sn_min"] >= 3.0), sn3),
            "interpretation_guard": "Massive-host optical denominator only; no radio jet, X-ray cavity, or heating coupling measurement.",
        })
    massive_csv = tables_dir / f"massive_host_attrition_m1rp3_m2p2_{ts}.csv"
    write_csv(massive_csv, list(massive_rows[0].keys()), massive_rows)

    # 4) sSFR-bin attrition: selection-bias check for quenched/low-sSFR emphasis.
    ssfr_bins: List[Tuple[float, float, str]] = [
        (-14.0, -12.0, "-14.0_to_-12.0"),
        (-12.0, -11.0, "-12.0_to_-11.0"),
        (-11.0, -10.5, "-11.0_to_-10.5"),
        (-10.5, -10.0, "-10.5_to_-10.0"),
        (-10.0, -9.5, "-10.0_to_-9.5"),
        (-9.5, -9.0, "-9.5_to_-9.0"),
        (-9.0, -7.0, "-9.0_to_-7.0"),
    ]
    ssfr_rows: List[Dict[str, Any]] = []
    for lo, hi, label in ssfr_bins:
        # Lower inclusive, upper exclusive, mirroring analysis bin language.
        subset = f"{BASE_SPEC} AND x.lgm_tot_p50 BETWEEN 8.0 AND 12.5 AND x.specsfr_tot_p50 >= {lo:.1f} AND x.specsfr_tot_p50 < {hi:.1f}"
        sql = count_query_sql({
            "parent": q_count(EXTRA_FROM, subset),
            "sn_ge_3": q_count(LINE_FROM, f"{subset} AND {sn_cond(3.0)}"),
            "sn_ge_5": q_count(LINE_FROM, f"{subset} AND {sn_cond(5.0)}"),
            "sn_ge_10": q_count(LINE_FROM, f"{subset} AND {sn_cond(10.0)}"),
        })
        raw = fetch_sdss_json(f"ssfr_bin_attrition_{label.replace('-', 'm').replace('.', 'p')}", sql, raw_dir)
        time.sleep(0.25)
        parent = safe_int(raw["parent"])
        sn3 = safe_int(raw["sn_ge_3"])
        sn5 = safe_int(raw["sn_ge_5"])
        sn10 = safe_int(raw["sn_ge_10"])
        local_sn3 = local_count(local_rows, lambda r, a=lo, b=hi: a <= r["_ssfr"] < b and r["_sn_min"] >= 3.0)
        ssfr_rows.append({
            "ssfr_bin": label,
            "sdss_parent_count": parent,
            "sdss_sn_ge_3_count": sn3,
            "sdss_sn_ge_5_count": sn5,
            "sdss_sn_ge_10_count": sn10,
            "sn_ge_3_retention_vs_parent": frac(sn3, parent),
            "sn_ge_5_retention_vs_parent": frac(sn5, parent),
            "sn_ge_10_retention_vs_parent": frac(sn10, parent),
            "cached_sn_ge_3_count": local_sn3,
            "cached_coverage_of_sdss_sn_ge_3": frac(local_sn3, sn3),
            "interpretation_guard": "Four-line emission selection is not neutral in sSFR; use this before gas-depletion/quenched-denominator prose.",
        })
    ssfr_csv = tables_dir / f"ssfr_bin_line_selection_attrition_{ts}.csv"
    write_csv(ssfr_csv, list(ssfr_rows[0].keys()), ssfr_rows)

    # 5) M3 P3 target-vector cells: cached local target-vector N versus full SDSS strict eligible N.
    mass_bins: List[Tuple[float, float, str]] = [
        (8.0, 9.5, "8p0_9p5"),
        (9.5, 10.0, "9p5_10p0"),
        (10.0, 10.5, "10p0_10p5"),
        (10.5, 11.0, "10p5_11p0"),
        (11.0, 12.5, "11p0_12p5"),
    ]
    z_bins: List[Tuple[float, float, str]] = [
        (0.02, 0.05, "0p02_0p05"),
        (0.05, 0.08, "0p05_0p08"),
        (0.08, 0.12, "0p08_0p12"),
    ]
    cell_rows: List[Dict[str, Any]] = []
    for mlo, mhi, mlab in mass_bins:
        for zlo, zhi, zlab in z_bins:
            subset = f"s.class='GALAXY' AND s.z >= {zlo:.2f} AND s.z < {zhi:.2f} AND x.lgm_tot_p50 >= {mlo:.1f} AND x.lgm_tot_p50 < {mhi:.1f} AND x.specsfr_tot_p50 BETWEEN -14.0 AND -7.0"
            sql = count_query_sql({
                "parent": q_count(EXTRA_FROM, subset),
                "sn_ge_3": q_count(LINE_FROM, f"{subset} AND {sn_cond(3.0)}"),
                "sn_ge_5": q_count(LINE_FROM, f"{subset} AND {sn_cond(5.0)}"),
                "sn_ge_10": q_count(LINE_FROM, f"{subset} AND {sn_cond(10.0)}"),
            })
            raw = fetch_sdss_json(f"m3p3_cell_attrition_m{mlab}_z{zlab}", sql, raw_dir)
            time.sleep(0.25)
            parent = safe_int(raw["parent"])
            sn3 = safe_int(raw["sn_ge_3"])
            local_sn3 = local_count(local_rows, lambda r, a=mlo, b=mhi, c=zlo, d=zhi: a <= r["_logm"] < b and c <= r["_z"] < d and r["_sn_min"] >= 3.0)
            cell_rows.append({
                "mass_bin_logM": f"{mlo:.1f}-{mhi:.1f}",
                "z_bin": f"{zlo:.2f}-{zhi:.2f}",
                "sdss_parent_count": parent,
                "sdss_sn_ge_3_count": sn3,
                "sdss_sn_ge_5_count": safe_int(raw["sn_ge_5"]),
                "sdss_sn_ge_10_count": safe_int(raw["sn_ge_10"]),
                "sn_ge_3_retention_vs_parent": frac(sn3, parent),
                "cached_target_vector_count": local_sn3,
                "cached_coverage_of_sdss_sn_ge_3": frac(local_sn3, sn3),
                "cached_small_cell_flag": "YES" if local_sn3 < 500 else "NO",
                "interpretation_guard": "Observed target-vector cell only; simulation validation still requires forward-modelled mocks and matching selection.",
            })
    cells_csv = tables_dir / f"m3_p3_target_vector_cell_attrition_{ts}.csv"
    write_csv(cells_csv, list(cell_rows[0].keys()), cell_rows)

    # 6) Integration snippets and summary.
    strict_total = stage_sql_counts["sn_ge_3_four_bpt_lines"]
    cached_coverage_strict = cached_total / strict_total if strict_total else None
    low_bin = next(r for r in ssfr_rows if r["ssfr_bin"] == "-12.0_to_-11.0")
    sf_bin = next(r for r in ssfr_rows if r["ssfr_bin"] == "-10.0_to_-9.5")
    gas_default = next(r for r in gas_rows if r["mass_cut_logM_ge"] == "10.6" and r["ssfr_cut_log_ssfr_lt"] == "-10.7")
    gas_strict = next(r for r in gas_rows if r["mass_cut_logM_ge"] == "11.0" and r["ssfr_cut_log_ssfr_lt"] == "-11.0")
    small_cells = [r for r in cell_rows if r["cached_small_cell_flag"] == "YES"]

    tex_path = out_dir / f"selection_attrition_table_fragment_{ts}.tex"
    tex_lines = [
        "% SELECTION_FUNCTION_ATTRITION_TICK table fragment; lane-local only, not merged.",
        "\\begin{deluxetable*}{lrrrr}",
        "\\tablecaption{Public SDSS DR17 selection-function counts for the four-line optical-denominator pilot}",
        "\\tablehead{\\colhead{Stage} & \\colhead{SDSS DR17 $N$} & \\colhead{Retention from previous} & \\colhead{Cached $N$} & \\colhead{Cached/SDSS}}",
        "\\startdata",
    ]
    for row in stage_rows:
        cached = row["cached_sample_count_at_matching_stage"] if row["cached_sample_count_at_matching_stage"] != "" else "--"
        ret = "--" if row["retention_vs_previous_stage"] == "" else f"{100*row['retention_vs_previous_stage']:.1f}\\%"
        cov = "--" if row["cached_coverage_of_sdss_stage"] == "" else f"{100*row['cached_coverage_of_sdss_stage']:.1f}\\%"
        label = row["stage_label"].replace("_", "\\_")
        cached_tex = cached if cached == "--" else f"{int(cached):,}"
        tex_lines.append(f"{label} & {row['sdss_dr17_count']:,} & {ret} & {cached_tex} & {cov} \\\\")
    tex_lines += [
        "\\enddata",
        "\\tablecomments{The cached pilot sample is capped at 60,000 rows selected by SpecObjID order from the S/N$\\geq$3 four-line-eligible set. These counts are selection-function diagnostics, not causal feedback evidence.}",
        "\\end{deluxetable*}",
    ]
    tex_path.write_text("\n".join(tex_lines) + "\n", encoding="utf-8")

    md_path = out_dir / f"selection_function_attrition_summary_{ts}.md"
    md = f"""# Selection-function attrition check — {ts}

Marker: `{RUN_MARKER}_{ts}`

## What this tick did

- Queried public SDSS DR17 SkyServer with read-only `COUNT(*)` SQL only.
- Compared full public DR17 selection counts against the cached 60,000-row four-line S/N pilot sample used by the 9 active AAS-style papers.
- Wrote tables for global selection stages, massive/low-sSFR denominator attrition, massive-host attrition, sSFR-bin line-selection bias, and M3 P3 target-vector cell coverage.
- Did not edit public-linked manuscripts or PDFs in this tick.

## Key results to carry forward

1. The original cached sample is a capped subset: SDSS DR17 has **{strict_total:,}** rows satisfying the same four-line S/N$\\geq$3, mass, sSFR, and redshift cuts; the cached 60,000 rows cover **{100*cached_coverage_strict:.1f}%** of that strict eligible set and were selected by `TOP 60000 ... ORDER BY s.specObjID`, not by a random draw.
2. The four-line S/N selection is strongly sSFR-dependent. In the `-12.0_to_-11.0` sSFR bin, S/N$\\geq$3 retains **{pct(int(low_bin['sdss_sn_ge_3_count']), int(low_bin['sdss_parent_count']))}** of the public SDSS parent; in the `-10.0_to_-9.5` bin it retains **{pct(int(sf_bin['sdss_sn_ge_3_count']), int(sf_bin['sdss_parent_count']))}**. This must be disclosed before using the sample as a quenched/gas-depletion denominator.
3. For the M3 P2 default massive low-sSFR denominator (`logM>=10.6`, `log sSFR<-10.7`), public DR17 has **{int(gas_default['sdss_parent_mass_ssfr_count']):,}** parent rows but **{int(gas_default['sdss_sn_ge_3_count']):,}** four-line S/N$\\geq$3 rows; the cached sample contains **{int(gas_default['cached_sn_ge_3_count']):,}** of those strict rows.
4. For the stricter M3 P2 denominator (`logM>=11.0`, `log sSFR<-11.0`), public DR17 has **{int(gas_strict['sdss_parent_mass_ssfr_count']):,}** parent rows but **{int(gas_strict['sdss_sn_ge_3_count']):,}** four-line S/N$\\geq$3 rows; the cached sample contains **{int(gas_strict['cached_sn_ge_3_count']):,}**.
5. M3 P3 target-vector table rows with cached `N<500`: **{len(small_cells)}** cells. Those cells need minimum-N or uncertainty flags before any merge into an active manuscript.

## Interpretation guard

These are selection-function and denominator diagnostics. They do not establish causal AGN feedback, gas depletion, radio-jet coupling, escape/recycling, or simulation validation. They improve the manuscripts by making the SDSS optical denominator honest and by warning where the 60,000-row cached sample is a capped, emission-line-selected subset of the public DR17 parent.

## Output files

- Global stage counts CSV: `{stage_csv}`
- M3 P2 massive low-sSFR attrition CSV: `{gas_csv}`
- Massive-host attrition CSV: `{massive_csv}`
- sSFR-bin line-selection attrition CSV: `{ssfr_csv}`
- M3 P3 target-vector cell attrition CSV: `{cells_csv}`
- AASTeX table fragment: `{tex_path}`
- Raw SDSS SQL/JSON payloads: `{raw_dir}`

## Safety

No NebulaMind/product DB writes, SQL apply packets, `/api/pages`, page_versions, live wiki publish, trust recompute, public/live frontend mirroring, deploy/restart, git commit/push/merge/rebase, cron creation, billing/cloud/OAuth/API-key changes, or external submission actions were performed.
"""
    md_path.write_text(md, encoding="utf-8")

    summary = {
        "marker": f"{RUN_MARKER}_{ts}",
        "timestamp_utc": ts,
        "work_root": str(WORK_ROOT),
        "source_csv": str(SOURCE_CSV),
        "sdss_endpoint": BASE_URL,
        "sdss_raw_payload_dir": str(raw_dir),
        "cached_rows": cached_total,
        "strict_sdss_sn_ge_3_total": strict_total,
        "cached_coverage_of_strict_sdss_sn_ge_3": cached_coverage_strict,
        "stage_counts": stage_rows,
        "m3_p2_default_denominator": gas_default,
        "m3_p2_strict_denominator": gas_strict,
        "ssfr_low_bin_reference": low_bin,
        "ssfr_star_forming_bin_reference": sf_bin,
        "m3_p3_cached_small_cell_count": len(small_cells),
        "files": {
            "selection_stage_counts_csv": str(stage_csv),
            "m3_p2_massive_low_ssfr_attrition_csv": str(gas_csv),
            "massive_host_attrition_csv": str(massive_csv),
            "ssfr_bin_line_selection_attrition_csv": str(ssfr_csv),
            "m3_p3_target_vector_cell_attrition_csv": str(cells_csv),
            "aastex_table_fragment": str(tex_path),
            "summary_md": str(md_path),
        },
        "safety": "Read-only public SDSS counts plus local file reads; lane-local artifact writes only. No product DB/API/page_versions/live wiki/deploy/git/cron/billing/OAuth/external submission changes.",
    }
    summary_json = out_dir / f"selection_function_attrition_summary_{ts}.json"
    summary_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    artifact_paths = [stage_csv, gas_csv, massive_csv, ssfr_csv, cells_csv, tex_path, md_path, summary_json]
    manifest = {
        "marker": f"SELECTION_FUNCTION_ATTRITION_ARTIFACT_MANIFEST_{ts}",
        "timestamp_utc": ts,
        "artifact_count": len(artifact_paths),
        "artifacts": [
            {"path": str(path), "bytes": path.stat().st_size, "sha256": sha256_path(path)} for path in artifact_paths
        ],
        "raw_payload_count_json": len(list(raw_dir.glob("*.json"))),
        "raw_payload_count_sql": len(list(raw_dir.glob("*.sql"))),
    }
    manifest_path = out_dir / f"selection_function_attrition_artifact_manifest_{ts}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "timestamp_utc": ts,
        "out_dir": str(out_dir),
        "summary_md": str(md_path),
        "summary_json": str(summary_json),
        "manifest_json": str(manifest_path),
        "strict_sdss_sn_ge_3_total": strict_total,
        "cached_coverage_of_strict_sdss_sn_ge_3": cached_coverage_strict,
        "m3_p3_cached_small_cells": len(small_cells),
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
