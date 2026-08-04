#!/usr/bin/env python3
"""Read-only SDSS selection-function attrition check for overnight 9-paper work.

This retry version uses short, single-count SkyServer SQL queries because a first
aggregate/subquery attempt timed out. It writes lane-local artifacts only.
"""
from __future__ import annotations

import csv
import hashlib
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Tuple

WORK_ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708")
SOURCE_CSV = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv")
BASE_URL = "https://skyserver.sdss.org/dr17/SkyServerWS/SearchTools/SqlSearch"
MARKER = "SELECTION_FUNCTION_ATTRITION_TICK"

SPEC_FROM = "SpecObj s"
EXTRA_FROM = "SpecObj s JOIN galSpecInfo i ON s.specObjID=i.specObjID JOIN PhotoObj p ON s.bestObjID=p.objID JOIN galSpecExtra x ON s.specObjID=x.specObjID"
LINE_FROM = EXTRA_FROM + " JOIN galSpecLine l ON s.specObjID=l.specObjID"
BASE_Z = "s.class='GALAXY' AND s.z BETWEEN 0.02 AND 0.12"
MASS_SSFR = "x.lgm_tot_p50 BETWEEN 8 AND 12.5 AND x.specsfr_tot_p50 BETWEEN -14 AND -7"
ERR_POS = " AND ".join([
    "l.h_alpha_flux_err>0",
    "l.h_beta_flux_err>0",
    "l.oiii_5007_flux_err>0",
    "l.nii_6584_flux_err>0",
])
POS = " AND ".join([
    ERR_POS,
    "l.h_alpha_flux>0",
    "l.h_beta_flux>0",
    "l.oiii_5007_flux>0",
    "l.nii_6584_flux>0",
])

def sn(th: int) -> str:
    return " AND ".join([
        ERR_POS,
        f"l.h_alpha_flux>={th}*l.h_alpha_flux_err",
        f"l.h_beta_flux>={th}*l.h_beta_flux_err",
        f"l.oiii_5007_flux>={th}*l.oiii_5007_flux_err",
        f"l.nii_6584_flux>={th}*l.nii_6584_flux_err",
    ])


def pct(x: int, y: int) -> str:
    return "" if not y else f"{100*x/y:.2f}%"


def frac(x: int, y: int) -> float | None:
    return None if not y else x / y


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys()) if rows else ["empty"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            w.writerow(row)


def fnum(v: str) -> float:
    try:
        return float(v)
    except Exception:
        return float("nan")


def read_local_rows() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with SOURCE_CSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["_z"] = fnum(row.get("z", "nan"))
            row["_logm"] = fnum(row.get("lgm_tot_p50", "nan"))
            row["_ssfr"] = fnum(row.get("specsfr_tot_p50", "nan"))
            try:
                row["_sn_min"] = min(
                    fnum(row["h_alpha_flux"]) / fnum(row["h_alpha_flux_err"]),
                    fnum(row["h_beta_flux"]) / fnum(row["h_beta_flux_err"]),
                    fnum(row["oiii_5007_flux"]) / fnum(row["oiii_5007_flux_err"]),
                    fnum(row["nii_6584_flux"]) / fnum(row["nii_6584_flux_err"]),
                )
            except Exception:
                row["_sn_min"] = float("nan")
            rows.append(row)
    return rows


def local_count(rows: Iterable[Dict[str, Any]], pred: Callable[[Dict[str, Any]], bool]) -> int:
    return sum(1 for row in rows if pred(row))


def fetch_count(name: str, from_clause: str, where_clause: str, raw_dir: Path, delay_s: float = 0.2) -> int:
    raw_dir.mkdir(parents=True, exist_ok=True)
    sql = f"SELECT COUNT(*) n FROM {from_clause} WHERE {where_clause}"
    (raw_dir / f"{name}.sql").write_text(sql + "\n", encoding="utf-8")
    url = BASE_URL + "?" + urllib.parse.urlencode({"cmd": sql, "format": "json"})
    last_error = None
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NebulaMind-local-readonly-selection-check/1.0"})
            with urllib.request.urlopen(req, timeout=150) as response:
                payload = response.read()
            (raw_dir / f"{name}.json").write_bytes(payload)
            parsed = json.loads(payload.decode("utf-8"))
            n = int(parsed[0]["Rows"][0]["n"])
            time.sleep(delay_s)
            return n
        except Exception as exc:
            last_error = exc
            time.sleep(1.5 * attempt)
    raise RuntimeError(f"SDSS count failed for {name}: {last_error}")


def main() -> int:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = WORK_ROOT / "lanes" / "tori" / "selection-function-attrition" / ts
    raw_dir = out_dir / "raw_sdss_payloads"
    tables_dir = out_dir / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = read_local_rows()
    local_total = len(rows)

    stage_defs = [
        ("spectro_galaxy_z_window", "SpecObj GALAXY, 0.02<z<0.12", SPEC_FROM, BASE_Z, ""),
        ("join_complete_mass_ssfr_bounds", "plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds", EXTRA_FROM, f"{BASE_Z} AND {MASS_SSFR}", ""),
        ("join_complete_with_line_table", "plus galSpecLine join", LINE_FROM, f"{BASE_Z} AND {MASS_SSFR}", ""),
        ("positive_four_bpt_fluxes_and_errors", "four BPT lines positive with positive errors", LINE_FROM, f"{BASE_Z} AND {MASS_SSFR} AND {POS}", local_total),
        ("sn_ge_3_four_bpt_lines", "four BPT lines S/N>=3", LINE_FROM, f"{BASE_Z} AND {MASS_SSFR} AND {sn(3)}", local_total),
        ("sn_ge_5_four_bpt_lines", "four BPT lines S/N>=5", LINE_FROM, f"{BASE_Z} AND {MASS_SSFR} AND {sn(5)}", local_count(rows, lambda r: r["_sn_min"] >= 5)),
        ("sn_ge_10_four_bpt_lines", "four BPT lines S/N>=10", LINE_FROM, f"{BASE_Z} AND {MASS_SSFR} AND {sn(10)}", local_count(rows, lambda r: r["_sn_min"] >= 10)),
    ]
    stage_rows: List[Dict[str, Any]] = []
    prev = None
    first_n = None
    for key, label, frm, wh, cached in stage_defs:
        n = fetch_count(key, frm, wh, raw_dir)
        if first_n is None:
            first_n = n
        stage_rows.append({
            "stage_key": key,
            "stage_label": label,
            "sdss_dr17_count": n,
            "retention_vs_previous_stage": "" if prev is None else frac(n, prev),
            "retention_vs_spectro_z_parent": frac(n, first_n or n),
            "cached_sample_count_at_matching_stage": cached,
            "cached_coverage_of_sdss_stage": "" if cached == "" else frac(int(cached), n),
            "query_scope": "SpecObj+galSpecInfo+PhotoObj+galSpecExtra+galSpecLine where relevant; read-only public SDSS DR17 SkyServer count.",
        })
        prev = n
    stage_csv = tables_dir / f"selection_stage_counts_{ts}.csv"
    write_csv(stage_csv, stage_rows)

    mass_cuts = [10.6, 10.8, 11.0]
    ssfr_cuts = [-10.7, -11.0]
    gas_rows: List[Dict[str, Any]] = []
    for m in mass_cuts:
        for s in ssfr_cuts:
            base = f"{BASE_Z} AND x.lgm_tot_p50>={m:g} AND x.lgm_tot_p50<=12.5 AND x.specsfr_tot_p50>=-14 AND x.specsfr_tot_p50<{s:g}"
            parent = fetch_count(f"m3p2_parent_m{str(m).replace('.','p')}_s{str(abs(s)).replace('.','p')}", EXTRA_FROM, base, raw_dir)
            sn3 = fetch_count(f"m3p2_sn3_m{str(m).replace('.','p')}_s{str(abs(s)).replace('.','p')}", LINE_FROM, f"{base} AND {sn(3)}", raw_dir)
            cached = local_count(rows, lambda r, m=m, s=s: r["_logm"] >= m and r["_ssfr"] < s and r["_sn_min"] >= 3)
            gas_rows.append({
                "paper": "M3 P2 gas-depletion/SFE denominator",
                "mass_cut_logM_ge": m,
                "ssfr_cut_log_ssfr_lt": s,
                "sdss_parent_mass_ssfr_count": parent,
                "sdss_sn_ge_3_count": sn3,
                "sn_ge_3_retention_vs_parent": frac(sn3, parent),
                "cached_sn_ge_3_count": cached,
                "cached_coverage_of_sdss_sn_ge_3": frac(cached, sn3),
                "guard": "This is an emission-line selected optical denominator, not a gas mass or SFE measurement.",
            })
    gas_csv = tables_dir / f"m3_p2_massive_low_ssfr_attrition_{ts}.csv"
    write_csv(gas_csv, gas_rows)

    massive_rows: List[Dict[str, Any]] = []
    for m in mass_cuts:
        base = f"{BASE_Z} AND x.lgm_tot_p50>={m:g} AND x.lgm_tot_p50<=12.5 AND x.specsfr_tot_p50 BETWEEN -14 AND -7"
        parent = fetch_count(f"massive_parent_m{str(m).replace('.','p')}", EXTRA_FROM, base, raw_dir)
        sn3 = fetch_count(f"massive_sn3_m{str(m).replace('.','p')}", LINE_FROM, f"{base} AND {sn(3)}", raw_dir)
        cached = local_count(rows, lambda r, m=m: r["_logm"] >= m and r["_sn_min"] >= 3)
        massive_rows.append({
            "papers": "M1 RP-3 maintenance-heating denominator; M2 P2 radio-jet environment denominator",
            "mass_cut_logM_ge": m,
            "sdss_parent_mass_count": parent,
            "sdss_sn_ge_3_count": sn3,
            "sn_ge_3_retention_vs_parent": frac(sn3, parent),
            "cached_sn_ge_3_count": cached,
            "cached_coverage_of_sdss_sn_ge_3": frac(cached, sn3),
            "guard": "Massive-host optical denominator only; no X-ray cavity/radio jet/coupling measurement.",
        })
    massive_csv = tables_dir / f"massive_host_attrition_m1rp3_m2p2_{ts}.csv"
    write_csv(massive_csv, massive_rows)

    ssfr_bins: List[Tuple[float, float, str]] = [
        (-14, -12, "-14.0_to_-12.0"),
        (-12, -11, "-12.0_to_-11.0"),
        (-11, -10.5, "-11.0_to_-10.5"),
        (-10.5, -10, "-10.5_to_-10.0"),
        (-10, -9.5, "-10.0_to_-9.5"),
        (-9.5, -9, "-9.5_to_-9.0"),
        (-9, -7, "-9.0_to_-7.0"),
    ]
    ssfr_rows: List[Dict[str, Any]] = []
    for lo, hi, label in ssfr_bins:
        base = f"{BASE_Z} AND x.lgm_tot_p50 BETWEEN 8 AND 12.5 AND x.specsfr_tot_p50>={lo:g} AND x.specsfr_tot_p50<{hi:g}"
        parent = fetch_count(f"ssfr_parent_{label.replace('-','m').replace('.','p')}", EXTRA_FROM, base, raw_dir)
        sn3 = fetch_count(f"ssfr_sn3_{label.replace('-','m').replace('.','p')}", LINE_FROM, f"{base} AND {sn(3)}", raw_dir)
        cached = local_count(rows, lambda r, lo=lo, hi=hi: lo <= r["_ssfr"] < hi and r["_sn_min"] >= 3)
        ssfr_rows.append({
            "ssfr_bin": label,
            "sdss_parent_count": parent,
            "sdss_sn_ge_3_count": sn3,
            "sn_ge_3_retention_vs_parent": frac(sn3, parent),
            "cached_sn_ge_3_count": cached,
            "cached_coverage_of_sdss_sn_ge_3": frac(cached, sn3),
            "guard": "Four-line emission selection is sSFR-dependent; disclose before quenched/gas-denominator prose.",
        })
    ssfr_csv = tables_dir / f"ssfr_bin_line_selection_attrition_{ts}.csv"
    write_csv(ssfr_csv, ssfr_rows)

    # Full public counts only for locally small M3 P3 cells, to keep the tick bounded.
    mass_bins = [(8.0, 9.5), (9.5, 10.0), (10.0, 10.5), (10.5, 11.0), (11.0, 12.5)]
    z_bins = [(0.02, 0.05), (0.05, 0.08), (0.08, 0.12)]
    cell_rows: List[Dict[str, Any]] = []
    for mlo, mhi in mass_bins:
        for zlo, zhi in z_bins:
            cached = local_count(rows, lambda r, mlo=mlo, mhi=mhi, zlo=zlo, zhi=zhi: mlo <= r["_logm"] < mhi and zlo <= r["_z"] < zhi and r["_sn_min"] >= 3)
            if cached >= 500:
                continue
            base = f"s.class='GALAXY' AND s.z>={zlo:g} AND s.z<{zhi:g} AND x.lgm_tot_p50>={mlo:g} AND x.lgm_tot_p50<{mhi:g} AND x.specsfr_tot_p50 BETWEEN -14 AND -7"
            parent = fetch_count(f"m3p3_small_parent_m{str(mlo).replace('.','p')}_{str(mhi).replace('.','p')}_z{str(zlo).replace('.','p')}_{str(zhi).replace('.','p')}", EXTRA_FROM, base, raw_dir)
            sn3 = fetch_count(f"m3p3_small_sn3_m{str(mlo).replace('.','p')}_{str(mhi).replace('.','p')}_z{str(zlo).replace('.','p')}_{str(zhi).replace('.','p')}", LINE_FROM, f"{base} AND {sn(3)}", raw_dir)
            cell_rows.append({
                "paper": "M3 P3 simulation-validation target vector",
                "mass_bin_logM": f"{mlo:.1f}-{mhi:.1f}",
                "z_bin": f"{zlo:.2f}-{zhi:.2f}",
                "cached_target_vector_count": cached,
                "sdss_parent_count": parent,
                "sdss_sn_ge_3_count": sn3,
                "cached_coverage_of_sdss_sn_ge_3": frac(cached, sn3),
                "flag": "CACHED_N_LT_500_ADD_UNCERTAINTY_OR_MIN_N_FLAG",
                "guard": "Observed target-vector cell only; no model validation without forward-modelled mocks.",
            })
    cells_csv = tables_dir / f"m3_p3_small_cell_attrition_{ts}.csv"
    write_csv(cells_csv, cell_rows or [{"empty": "no cached target-vector cells below 500"}])

    strict_total = next(r for r in stage_rows if r["stage_key"] == "sn_ge_3_four_bpt_lines")["sdss_dr17_count"]
    cached_coverage = local_total / int(strict_total)
    low_bin = next(r for r in ssfr_rows if r["ssfr_bin"] == "-12.0_to_-11.0")
    sf_bin = next(r for r in ssfr_rows if r["ssfr_bin"] == "-10.0_to_-9.5")
    gas_default = next(r for r in gas_rows if r["mass_cut_logM_ge"] == 10.6 and r["ssfr_cut_log_ssfr_lt"] == -10.7)
    gas_strict = next(r for r in gas_rows if r["mass_cut_logM_ge"] == 11.0 and r["ssfr_cut_log_ssfr_lt"] == -11.0)

    tex_path = out_dir / f"selection_attrition_table_fragment_{ts}.tex"
    tex_lines = [
        "% SELECTION_FUNCTION_ATTRITION_TICK table fragment; lane-local only, not merged.",
        "\\begin{deluxetable*}{lrrrr}",
        "\\tablecaption{Public SDSS DR17 selection-function counts for the optical-denominator pilot}",
        "\\tablehead{\\colhead{Stage} & \\colhead{SDSS DR17 $N$} & \\colhead{Prev. retention} & \\colhead{Cached $N$} & \\colhead{Cached/SDSS}}",
        "\\startdata",
    ]
    for row in stage_rows:
        ret = "--" if row["retention_vs_previous_stage"] == "" else f"{100*float(row['retention_vs_previous_stage']):.1f}\\%"
        cached = row["cached_sample_count_at_matching_stage"]
        cached_tex = "--" if cached == "" else f"{int(cached):,}"
        cov = "--" if row["cached_coverage_of_sdss_stage"] == "" else f"{100*float(row['cached_coverage_of_sdss_stage']):.1f}\\%"
        label = str(row["stage_label"]).replace("_", "\\_")
        tex_lines.append(f"{label} & {int(row['sdss_dr17_count']):,} & {ret} & {cached_tex} & {cov} \\\\")
    tex_lines += [
        "\\enddata",
        "\\tablecomments{The cached pilot sample is capped at 60,000 rows selected by SpecObjID order from the S/N$\\geq$3 four-line-eligible set. These counts diagnose the selection function; they are not causal feedback evidence.}",
        "\\end{deluxetable*}",
    ]
    tex_path.write_text("\n".join(tex_lines) + "\n", encoding="utf-8")

    md_path = out_dir / f"selection_function_attrition_summary_{ts}.md"
    md = f"""# Selection-function attrition check — {ts}

Marker: `{MARKER}_{ts}`

## What this tick did

- Ran public/read-only SDSS DR17 SkyServer `COUNT(*)` queries only.
- Quantified the parent-to-four-line-S/N selection cascade behind the cached 60,000-row SDSS sample used by the 9 active AAS-style pilots.
- Focused downstream checks on the external-review blockers: M3 P2 gas-denominator attrition, massive-host denominator attrition for M1 RP-3/M2 P2, sSFR-dependent line-selection bias, and small M3 P3 target-vector cells.
- Wrote lane-local CSV/JSON/Markdown/AASTeX-fragment artifacts only; no public-linked manuscript/PDF was overwritten.

## Key results

1. Public SDSS DR17 has **{int(strict_total):,}** rows satisfying the same four-line S/N$\\geq$3 redshift/mass/sSFR cuts; the cached sample has 60,000 rows, so it covers **{100*cached_coverage:.1f}%** of the strict eligible set and is a `TOP 60000 ... ORDER BY s.specObjID` capped subset, not a random sample.
2. The four-line S/N selection is sSFR-dependent: S/N$\\geq$3 keeps **{pct(int(low_bin['sdss_sn_ge_3_count']), int(low_bin['sdss_parent_count']))}** of the `-12.0_to_-11.0` sSFR parent bin versus **{pct(int(sf_bin['sdss_sn_ge_3_count']), int(sf_bin['sdss_parent_count']))}** of the `-10.0_to_-9.5` bin.
3. M3 P2 default (`logM>=10.6`, `log sSFR<-10.7`): **{int(gas_default['sdss_parent_mass_ssfr_count']):,}** public parent rows, **{int(gas_default['sdss_sn_ge_3_count']):,}** four-line S/N$\\geq$3 rows, **{int(gas_default['cached_sn_ge_3_count']):,}** cached rows.
4. M3 P2 strict (`logM>=11.0`, `log sSFR<-11.0`): **{int(gas_strict['sdss_parent_mass_ssfr_count']):,}** public parent rows, **{int(gas_strict['sdss_sn_ge_3_count']):,}** four-line S/N$\\geq$3 rows, **{int(gas_strict['cached_sn_ge_3_count']):,}** cached rows.
5. M3 P3 cached target-vector cells with `N<500` checked against public DR17: **{len(cell_rows)}** cells; these need minimum-N/uncertainty flags before manuscript merge.

## Files

- `{stage_csv}`
- `{gas_csv}`
- `{massive_csv}`
- `{ssfr_csv}`
- `{cells_csv}`
- `{tex_path}`
- Raw SQL/JSON payloads: `{raw_dir}`

## Interpretation guard

Selection-function counts improve denominator honesty only. They do not establish causal AGN feedback, gas depletion, radio-jet coupling, outflow escape/recycling, or simulation-validation conclusions.

## Safety

No NebulaMind/product DB writes, SQL apply packets, `/api/pages`, page_versions, live wiki publish, trust recompute, public/live frontend mirroring, deploy/restart, git commit/push/merge/rebase, cron creation, billing/cloud/OAuth/API-key changes, or external submission actions were performed.
"""
    md_path.write_text(md, encoding="utf-8")

    summary = {
        "marker": f"{MARKER}_{ts}",
        "timestamp_utc": ts,
        "source_csv": str(SOURCE_CSV),
        "sdss_endpoint": BASE_URL,
        "cached_rows": local_total,
        "strict_sdss_sn_ge_3_total": int(strict_total),
        "cached_coverage_of_strict_sdss_sn_ge_3": cached_coverage,
        "stage_counts": stage_rows,
        "m3_p2_default_denominator": gas_default,
        "m3_p2_strict_denominator": gas_strict,
        "ssfr_low_bin_reference": low_bin,
        "ssfr_star_forming_bin_reference": sf_bin,
        "m3_p3_small_cell_count": len(cell_rows),
        "files": {
            "selection_stage_counts_csv": str(stage_csv),
            "m3_p2_massive_low_ssfr_attrition_csv": str(gas_csv),
            "massive_host_attrition_csv": str(massive_csv),
            "ssfr_bin_line_selection_attrition_csv": str(ssfr_csv),
            "m3_p3_small_cell_attrition_csv": str(cells_csv),
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
            {"path": str(p), "bytes": p.stat().st_size, "sha256": sha256_path(p)} for p in artifact_paths
        ],
        "raw_payload_count_json": len(list(raw_dir.glob("*.json"))),
        "raw_payload_count_sql": len(list(raw_dir.glob("*.sql"))),
        "first_attempt_note": "Earlier aggregate/subquery version timed out before producing a report; this split-query run succeeded.",
    }
    manifest_json = out_dir / f"selection_function_attrition_artifact_manifest_{ts}.json"
    manifest_json.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "timestamp_utc": ts,
        "out_dir": str(out_dir),
        "summary_md": str(md_path),
        "summary_json": str(summary_json),
        "manifest_json": str(manifest_json),
        "strict_sdss_sn_ge_3_total": int(strict_total),
        "cached_coverage_of_strict_sdss_sn_ge_3": cached_coverage,
        "raw_payload_count_json": manifest["raw_payload_count_json"],
    }, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
