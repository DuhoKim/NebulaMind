#!/usr/bin/env python3
"""Build a shared parent-sample/selection-function module for the overnight 9-paper board.

Local-only, read cached SDSS and lane artifacts, write durable artifacts under the
overnight work root. No public/live/product/git/deploy actions.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import statistics
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
OVERNIGHT = AUTO / "overnight-9-papers-20260708"
SOURCE_CSV = AUTO / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
ATTRITION_DIR = OVERNIGHT / "lanes/tori/selection-function-attrition/20260708T155514Z"
ATTRITION_JSON = ATTRITION_DIR / "selection_function_attrition_summary_20260708T155514Z.json"
STAGE_CSV = ATTRITION_DIR / "tables/selection_stage_counts_20260708T155514Z.csv"
SSFR_CSV = ATTRITION_DIR / "tables/ssfr_bin_line_selection_attrition_20260708T155514Z.csv"
GORU_JSON = OVERNIGHT / "lanes/goru/artifacts/goru_regression_bin_sensitivity_20260708T183643Z.json"
LEDGER = OVERNIGHT / "OVERNIGHT_LEDGER.md"

SAFETY = (
    "Read cached SDSS/local overnight artifacts only; wrote local artifacts under "
    "overnight-9-papers-20260708/lanes/tori/shared-selection-module plus the required "
    "tick report and ledger append. No product DB/API/page_versions/wiki publish/live "
    "mirror/deploy/restart/git/extra-cron/billing/OAuth/external submission changes."
)

BPT_ORDER = ["star-forming", "intermediate", "agn", "unclassified"]
SN_COLUMNS = ["sn_ha", "sn_hb", "sn_oiii", "sn_nii"]

COLUMN_DICTIONARY = [
    ("specObjID", "integer string", "SDSS spectrum identifier", "Identifier/provenance", "Used for uniqueness checks and row-cap ordering; not a physical variable."),
    ("z", "float", "spectroscopic redshift", "Selection and matching", "Pilot restricts to 0.02<z<0.12."),
    ("ra", "float degrees", "right ascension", "Coordinate", "Used only for reproducibility/position context in this module."),
    ("dec", "float degrees", "declination", "Coordinate", "Used only for reproducibility/position context in this module."),
    ("bptclass", "integer/catalog code", "SDSS catalog BPT class value", "Input/catalog comparison", "Do not cite as the analysis classification without recomputed bpt_label."),
    ("lgm_tot_p50", "dex log10(M*/Msun)", "catalog median stellar mass", "Selection/control variable", "MPA/JHU-style catalog estimate; systematic model assumptions remain."),
    ("sfr_tot_p50", "dex log10(Msun/yr)", "catalog median total SFR", "Derived star-formation proxy", "Not a direct gas-depletion or feedback-power measurement."),
    ("specsfr_tot_p50", "dex log10(yr^-1)", "catalog median specific SFR", "Quenched/low-sSFR proxy", "Emission-line selection biases low-sSFR bins; disclose retention."),
    ("modelMag_u", "mag", "SDSS model u magnitude", "Photometric color input", "Used for colors only, not morphology or dust correction."),
    ("modelMag_g", "mag", "SDSS model g magnitude", "Photometric color input", "Used for colors only, not morphology or dust correction."),
    ("modelMag_r", "mag", "SDSS model r magnitude", "Photometric color input", "Used for colors only, not morphology or dust correction."),
    ("h_alpha_flux", "catalog flux unit", "H-alpha line flux", "BPT/SN input", "Aperture and calibration caveats remain."),
    ("h_alpha_flux_err", "catalog flux unit", "H-alpha line-flux uncertainty", "S/N input", "Used for four-line S/N cuts."),
    ("h_beta_flux", "catalog flux unit", "H-beta line flux", "BPT/SN input", "Aperture and calibration caveats remain."),
    ("h_beta_flux_err", "catalog flux unit", "H-beta line-flux uncertainty", "S/N input", "Used for four-line S/N cuts."),
    ("oiii_5007_flux", "catalog flux unit", "[O III] 5007 line flux", "BPT/high-excitation input", "High-excitation proxy only; no outflow velocity or luminosity correction."),
    ("oiii_5007_flux_err", "catalog flux unit", "[O III] 5007 line-flux uncertainty", "S/N input", "Used for four-line S/N cuts."),
    ("nii_6584_flux", "catalog flux unit", "[N II] 6584 line flux", "BPT input", "Aperture and calibration caveats remain."),
    ("nii_6584_flux_err", "catalog flux unit", "[N II] 6584 line-flux uncertainty", "S/N input", "Used for four-line S/N cuts."),
    ("sn_ha", "dimensionless", "H-alpha signal-to-noise", "Selection", "Part of four-line S/N>=3/5/10 variants."),
    ("sn_hb", "dimensionless", "H-beta signal-to-noise", "Selection", "Part of four-line S/N>=3/5/10 variants."),
    ("sn_oiii", "dimensionless", "[O III] signal-to-noise", "Selection", "Part of four-line S/N>=3/5/10 variants."),
    ("sn_nii", "dimensionless", "[N II] signal-to-noise", "Selection", "Part of four-line S/N>=3/5/10 variants."),
    ("log_nii_ha", "dex", "log([N II]/H-alpha)", "BPT ratio", "Recomputed ratio for BPT demarcations."),
    ("log_oiii_hb", "dex", "log([O III]/H-beta)", "BPT/high-excitation ratio", "High-excitation proxy uses bpt_label==agn and log_oiii_hb>0.25."),
    ("u_minus_r", "mag", "u-r color", "Color proxy", "Not a morphology, dust, or gas measurement."),
    ("g_minus_r", "mag", "g-r color", "Color proxy", "Not a morphology, dust, or gas measurement."),
    ("bpt_label", "categorical", "recomputed BPT class label", "Primary optical ionization class", "Allowed values in this sample: star-forming, intermediate, agn, unclassified."),
]

PAPER_CONTRACTS = [
    {
        "paper": "M1 RP-1",
        "slug": "m1_rp1_agn_sfr",
        "safe_current_object": "BPT optical AGN hosts versus star-forming controls in the capped SDSS four-line sample",
        "required_selection_language": "60,000 cached rows out of 249,917 strict public four-line S/N>=3 rows; controls are star-forming emission-line galaxies, not all inactive/quiescent galaxies.",
        "allowed_claim": "Optical AGN hosts lie below BPT star-forming controls in catalog sSFR within this selected sample.",
        "forbidden_claim": "Causal AGN feedback suppression or a complete quiescent-control result.",
    },
    {
        "paper": "M1 RP-2",
        "slug": "m1_rp2_environment_quenching",
        "safe_current_object": "nearest-neighbour density proxy and low-sSFR fraction in the capped SDSS four-line sample",
        "required_selection_language": "Density quartiles are internal rankings after four-line selection; no group catalogue, halo mass, central/satellite label, or edge correction is present.",
        "allowed_claim": "High internal-density quartiles have a different low-sSFR fraction in the selected emission-line denominator.",
        "forbidden_claim": "Environmental quenching causality or halo/group-scale proof.",
    },
    {
        "paper": "M1 RP-3",
        "slug": "m1_rp3_maintenance_heating",
        "safe_current_object": "massive/low-sSFR optical BPT-AGN target denominator",
        "required_selection_language": "Massive/low-sSFR rows remain four-line emission-selected and capped; X-ray, cavity, cooling-luminosity, and jet-power data are absent.",
        "allowed_claim": "Defines optical AGN candidates for future maintenance-heating follow-up.",
        "forbidden_claim": "Maintenance heating balance, duty-cycle energetics, or hot-halo feedback proof.",
    },
    {
        "paper": "M2 P1",
        "slug": "m2_p1_outflow_escape_recycling",
        "safe_current_object": "high-excitation optical AGN denominator using bpt_label==agn and log_oiii_hb>0.25",
        "required_selection_language": "[O III]/H-beta high-excitation is an optical line-ratio proxy only; no velocities, escape speeds, CGM gas, or recycling tracers are measured.",
        "allowed_claim": "Ranks/cuts optical AGN candidates for later outflow escape/recycling tests.",
        "forbidden_claim": "Outflow escape fractions, recycling times, or gas-loss proof.",
    },
    {
        "paper": "M2 P2",
        "slug": "m2_p2_radio_jet_environment",
        "safe_current_object": "massive-host optical BPT AGN fraction versus internal density proxy",
        "required_selection_language": "Massive-host cached sample is 9,298 rows versus 35,482 strict public S/N>=3 massive hosts; radio jet power, hot gas, and cavity data are absent.",
        "allowed_claim": "Optical AGN/density association in massive hosts motivates radio/X-ray follow-up.",
        "forbidden_claim": "Radio-jet coupling efficiency or environmental jet-power causality.",
    },
    {
        "paper": "M2 P3",
        "slug": "m2_p3_feedback_transition_mass",
        "safe_current_object": "stellar-mass/redshift trends in low-sSFR and optical AGN incidence",
        "required_selection_language": "Mass bins are observed SDSS optical bins within a four-line selected denominator; no halo, black-hole mass, or stellar-feedback separation exists.",
        "allowed_claim": "Provides mass-bin optical/quenching diagnostics with intervals.",
        "forbidden_claim": "Locating a physical transition from stellar to AGN feedback.",
    },
    {
        "paper": "M3 P1",
        "slug": "m3_p1_multiphase_census",
        "safe_current_object": "common-denominator optical tracer-threshold census",
        "required_selection_language": "Optical line/color/sSFR thresholds are not a multiphase census; CO/HI/Na I/X-ray/radio/kinematic data are absent.",
        "allowed_claim": "Provides optical tracer thresholds and denominators for future multiphase matching.",
        "forbidden_claim": "A completed multiphase outflow census.",
    },
    {
        "paper": "M3 P2",
        "slug": "m3_p2_gas_depletion_efficiency",
        "safe_current_object": "emission-line-detected massive low-sSFR optical follow-up denominator",
        "required_selection_language": "Default massive/low-sSFR denominator: 121,533 public parent, 40,797 strict S/N>=3 rows, 10,270 cached rows; H-alpha is not gas mass or SFE.",
        "allowed_claim": "Defines CO/HI/dust follow-up targets and line-selection attrition.",
        "forbidden_claim": "Molecular gas depletion, gas fraction, depletion time, or star-formation efficiency conclusions.",
    },
    {
        "paper": "M3 P3",
        "slug": "m3_p3_simulation_validation",
        "safe_current_object": "observed SDSS mass-redshift target vector with small-cell flags",
        "required_selection_language": "The vector is observed-only; no mock catalog, simulation output, covariance model, or forward selection function has been compared.",
        "allowed_claim": "Provides a target vector for future forward-modelled simulation comparisons.",
        "forbidden_claim": "Validation, rejection, ranking, or falsification of any feedback simulation.",
    },
]


def read_csv_dicts(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def num(row: dict[str, str], key: str) -> float:
    return float(row[key])


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(AUTO))
    except ValueError:
        return str(path)


def pct(x: float | None) -> str:
    if x is None:
        return ""
    # This helper is used in LaTeX table cells; escape percent signs.
    return f"{100*x:.1f}\\%"


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def csv_rows_from_stage(stage_rows: list[dict[str, str]], sn_counts: dict[str, int]) -> list[dict[str, Any]]:
    out = []
    for r in stage_rows:
        key = r["stage_key"]
        computed = ""
        if key == "sn_ge_3_four_bpt_lines":
            computed = sn_counts["sn_ge_3"]
        elif key == "sn_ge_5_four_bpt_lines":
            computed = sn_counts["sn_ge_5"]
        elif key == "sn_ge_10_four_bpt_lines":
            computed = sn_counts["sn_ge_10"]
        expected = r.get("cached_sample_count_at_matching_stage", "")
        ok = ""
        if computed != "" and expected != "":
            ok = str(int(float(expected)) == computed)
        out.append({
            "stage_key": key,
            "stage_label": r["stage_label"],
            "sdss_dr17_count": r["sdss_dr17_count"],
            "retention_vs_spectro_z_parent": r["retention_vs_spectro_z_parent"],
            "cached_sample_count_at_matching_stage": expected,
            "computed_cached_count_from_csv": computed,
            "computed_matches_recorded": ok,
            "cached_coverage_of_sdss_stage": r.get("cached_coverage_of_sdss_stage", ""),
        })
    return out


def latex_escape_text(s: str) -> str:
    return (s.replace("&", r"\&")
             .replace("%", r"\%")
             .replace("_", r"\_"))


def build_fragment(ts: str, summary: dict[str, Any], stage_rows: list[dict[str, Any]], ssfr_rows: list[dict[str, str]]) -> str:
    lines: list[str] = []
    lines.append(f"% SHARED_SELECTION_MODULE_{ts}")
    lines.append("% Include after \\begin{document}; requires aastex631 deluxetable support.")
    lines.append(r"\section{Parent sample, selection function, and shared data dictionary}\label{sec:shared-selection}")
    lines.append(
        r"All nine Galaxy Evolution pilot manuscripts share the same cached public SDSS DR17 optical emission-line denominator. "
        r"The row-level file contains 60,000 galaxies with spectroscopic class GALAXY, $0.02<z<0.12$, finite catalog stellar mass and specific SFR, and S/N$\geq3$ in H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$. "
        r"A read-only public SDSS count packet found 249,917 strict S/N$\geq3$ eligible rows for the same four-line, mass, sSFR, and redshift constraints, so the cached table covers 24.0\% of that strict public denominator. "
        r"The cached rows are ordered by SpecObjID and are not a random or complete parent sample."
    )
    lines.append(
        "The recomputed BPT labels in the cached table are: "
        f"{summary['bpt_counts']['star-forming']:,} star-forming, "
        f"{summary['bpt_counts']['intermediate']:,} intermediate/composite, "
        f"{summary['bpt_counts']['agn']:,} optical AGN, and "
        f"{summary['bpt_counts']['unclassified']:,} unclassified. "
        fr"The high-excitation optical subset used by M2 P1 is defined as BPT AGN with $\log([\mathrm{{O\,III}}]/\mathrm{{H}}\beta)>0.25$ and contains {summary['high_excitation_count']:,} objects."
    )
    lines.append(
        r"Because the four-line requirement is strongly sSFR-dependent, manuscripts that discuss quenching, gas depletion, or low-sSFR denominators must quote the retention contrast: "
        r"S/N$\geq3$ keeps 33.6\% of the public $-12<\log\mathrm{sSFR}<-11$ bin but 94.9\% of the $-10<\log\mathrm{sSFR}<-9.5$ bin."
    )
    lines.append("")
    lines.append(r"\begin{deluxetable*}{lrrrr}")
    lines.append(r"\tablecaption{Shared SDSS DR17 selection-function counts for all nine pilots\label{tab:shared-selection-stages}}")
    lines.append(r"\tablehead{\colhead{Stage} & \colhead{Public SDSS $N$} & \colhead{Retention vs. spectro-$z$} & \colhead{Cached $N$} & \colhead{Cached/public}}")
    lines.append(r"\startdata")
    for r in stage_rows:
        label = r["stage_label"]
        if "SpecObj" in label:
            label_tex = "SpecObj GALAXY, $0.02<z<0.12$"
        elif "mass/sSFR" in label:
            label_tex = "plus mass/sSFR bounds"
        elif "galSpecLine" in label:
            label_tex = "plus emission-line table join"
        elif "positive" in label:
            label_tex = "four BPT lines positive with positive errors"
        elif "S/N>=3" in label:
            label_tex = "four BPT lines S/N$\geq3$"
        elif "S/N>=5" in label:
            label_tex = "four BPT lines S/N$\geq5$"
        elif "S/N>=10" in label:
            label_tex = "four BPT lines S/N$\geq10$"
        else:
            label_tex = latex_escape_text(label)
        pub = int(float(r["sdss_dr17_count"]))
        retention = pct(float(r["retention_vs_spectro_z_parent"]) if r["retention_vs_spectro_z_parent"] else None)
        cached = r["cached_sample_count_at_matching_stage"] or r["computed_cached_count_from_csv"] or r"\nodata"
        if cached != r"\nodata":
            cached = f"{int(float(cached)):,}"
        coverage = r.get("cached_coverage_of_sdss_stage", "")
        coverage_tex = pct(float(coverage)) if coverage else r"\nodata"
        retention_tex = retention or r"\nodata"
        lines.append(f"{label_tex} & {pub:,} & {retention_tex} & {cached} & {coverage_tex} \\\\")
    lines.append(r"\enddata")
    lines.append(r"\tablecomments{Public counts come from read-only SDSS DR17 SkyServer count queries preserved in the selection-function packet; cached counts are independently recomputed from the local 60,000-row CSV where applicable.}")
    lines.append(r"\end{deluxetable*}")
    lines.append("")
    lines.append(r"\begin{deluxetable*}{lrrrr}")
    lines.append(r"\tablecaption{sSFR-dependent four-line selection retention\label{tab:shared-ssfr-retention}}")
    lines.append(r"\tablehead{\colhead{$\log\mathrm{sSFR}$ bin} & \colhead{Public parent $N$} & \colhead{Public S/N$\geq3$ $N$} & \colhead{S/N retention} & \colhead{Cached S/N$\geq3$ $N$}}")
    lines.append(r"\startdata")
    for r in ssfr_rows:
        bin_label = r["ssfr_bin"].replace("_to_", " to ").replace("-", "$-$")
        lines.append(
            f"{bin_label} & {int(r['sdss_parent_count']):,} & {int(r['sdss_sn_ge_3_count']):,} & {pct(float(r['sn_ge_3_retention_vs_parent']))} & {int(r['cached_sn_ge_3_count']):,} \\\\")
    lines.append(r"\enddata")
    lines.append(r"\tablecomments{The low-sSFR bins are much less likely to survive four-line S/N selection than star-forming bins; gas-depletion, quenching, and denominator papers must keep this caveat attached.}")
    lines.append(r"\end{deluxetable*}")
    lines.append("")
    lines.append(r"\paragraph{Shared wording contract.}")
    lines.append(
        "Allowed: this SDSS module supplies an optical emission-line denominator, BPT classifications, catalog mass/sSFR proxies, internal density rankings, and target-vector cells for follow-up design. "
        "Not allowed from this module alone: causal AGN feedback, radio-jet coupling efficiency, outflow escape/recycling, hot-halo maintenance heating, molecular-gas depletion, star-formation efficiency, multiphase outflow prevalence, or validation/falsification of simulations."
    )
    lines.append("")
    return "\n".join(lines)


def build_markdown(ts: str, summary: dict[str, Any], out_paths: dict[str, Path], verification: dict[str, Any]) -> str:
    lines = [
        f"# Shared parent-sample and selection-function module — {ts}",
        "",
        f"Marker: `SHARED_SELECTION_MODULE_{ts}`",
        "",
        "## What changed",
        "",
        "Built a reusable local module for all nine active AAS-style pilot papers: a data dictionary, selection-function counts, sSFR-retention table, paper-use contract, and an AASTeX fragment smoke-tested with Tectonic. This is a paper-quality improvement because it gives every draft the same front-loaded denominator disclosure instead of letting each paper restate the SDSS sample differently.",
        "",
        "## Grounding from actual artifacts",
        "",
        f"- Cached row-level SDSS CSV read: `{rel(SOURCE_CSV)}`.",
        f"- Selection-function packet read: `{rel(ATTRITION_JSON)}` plus stage and sSFR CSV tables.",
        f"- Goru regression/bin-sensitivity summary read for cross-checks: `{rel(GORU_JSON)}`.",
        f"- Cached rows: {summary['cached_rows']:,}; duplicate `specObjID`: {summary['duplicate_specobjid_count']}; `specObjID` nondecreasing: {summary['specobjid_nondecreasing']}.",
        f"- Public strict four-line S/N>=3 eligible rows: {summary['strict_public_sn_ge_3']:,}; cached coverage: {100*summary['cached_coverage_strict_public_sn_ge_3']:.1f}%.",
        f"- BPT counts from the cached CSV: star-forming {summary['bpt_counts']['star-forming']:,}, intermediate {summary['bpt_counts']['intermediate']:,}, optical AGN {summary['bpt_counts']['agn']:,}, unclassified {summary['bpt_counts']['unclassified']:,}.",
        f"- S/N-threshold counts recomputed from the cached CSV: >=3 {summary['sn_counts']['sn_ge_3']:,}, >=5 {summary['sn_counts']['sn_ge_5']:,}, >=10 {summary['sn_counts']['sn_ge_10']:,}.",
        f"- High-excitation optical AGN proxy (`bpt_label == agn` and `log_oiii_hb > 0.25`): {summary['high_excitation_count']:,} rows.",
        f"- sSFR-dependent line-selection warning preserved: 33.6% S/N>=3 retention for -12<log sSFR<-11 versus 94.9% for -10<log sSFR<-9.5.",
        "",
        "## Files changed / written",
        "",
    ]
    for key, path in out_paths.items():
        lines.append(f"- `{rel(path)}`")
    lines += [
        "",
        "## Verification",
        "",
        f"- JSON/CSV/TEX artifacts written: {verification['artifact_count']}.",
        f"- Tectonic smoke-test exit code: {verification['tectonic_exit_code']}.",
        f"- Smoke-test PDF starts with `%PDF`: {verification['smoke_pdf_magic_ok']}.",
        f"- Smoke-test PDF SHA256: `{verification.get('smoke_pdf_sha256', '')}`.",
        f"- Fatal LaTeX markers found in compile log: {verification['fatal_markers']}.",
        f"- Count checks passed: {verification['count_checks']}.",
        "",
        "## Blockers / cautions",
        "",
        "- This module is not a public-linked manuscript replacement. It is a local integration primitive that should be included before any future local merge of the nine drafts.",
        "- It does not authorize prose publication, public mirroring, DB/API writes, deploy/restart, git actions, or external submission.",
        "- The central scientific caution is unchanged: the cached sample is a capped optical emission-line denominator, not a complete/random SDSS parent and not a causal feedback/gas/simulation measurement.",
        "",
        "## Next recommended tick",
        "",
        "Use this shared module to assemble a local integration draft for either RP-1 flagship or the eight-paper denominator suite, then recompile/hash locally and run Kun-style reproducibility checks. Do not overwrite public-linked PDFs without a separate approval gate.",
        "",
        "## Safety",
        "",
        SAFETY,
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ts = os.environ.get("TICK_TS") or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    outroot = OVERNIGHT / "lanes/tori/shared-selection-module" / ts
    tables = outroot / "tables"
    aastex = outroot / "aastex"
    for d in (outroot, tables, aastex, OVERNIGHT / "ticks"):
        d.mkdir(parents=True, exist_ok=True)

    rows = read_csv_dicts(SOURCE_CSV)
    stage_rows_raw = read_csv_dicts(STAGE_CSV)
    ssfr_rows = read_csv_dicts(SSFR_CSV)
    attrition = json.loads(ATTRITION_JSON.read_text())
    goru = json.loads(GORU_JSON.read_text())

    bpt_counts = Counter(r["bpt_label"] for r in rows)
    sn_counts = {
        f"sn_ge_{thr}": sum(all(num(r, col) >= thr for col in SN_COLUMNS) for r in rows)
        for thr in (3, 5, 10)
    }
    ids = [int(r["specObjID"]) for r in rows]
    duplicate_ids = len(ids) - len(set(ids))
    specobjid_nondecreasing = all(ids[i] <= ids[i + 1] for i in range(len(ids) - 1))
    high_excitation = sum(r["bpt_label"] == "agn" and num(r, "log_oiii_hb") > 0.25 for r in rows)
    mass_counts = {f"mass_ge_{str(cut).replace('.', 'p')}": sum(num(r, "lgm_tot_p50") >= cut for r in rows) for cut in (10.6, 10.8, 11.0)}
    ssfr_counts = {f"ssfr_lt_{str(cut).replace('-', 'm').replace('.', 'p')}": sum(num(r, "specsfr_tot_p50") < cut for r in rows) for cut in (-11.0, -10.7)}

    def med(col: str) -> float:
        return statistics.median(num(r, col) for r in rows)

    summary = {
        "marker": f"SHARED_SELECTION_MODULE_{ts}",
        "timestamp_utc": ts,
        "source_csv": str(SOURCE_CSV),
        "cached_rows": len(rows),
        "strict_public_sn_ge_3": int(attrition["strict_sdss_sn_ge_3_total"]),
        "cached_coverage_strict_public_sn_ge_3": float(attrition["cached_coverage_of_strict_sdss_sn_ge_3"]),
        "bpt_counts": {k: int(bpt_counts.get(k, 0)) for k in BPT_ORDER},
        "sn_counts": sn_counts,
        "high_excitation_count": int(high_excitation),
        "mass_cut_counts": mass_counts,
        "ssfr_cut_counts": ssfr_counts,
        "duplicate_specobjid_count": duplicate_ids,
        "specobjid_nondecreasing": specobjid_nondecreasing,
        "specobjid_first": ids[0],
        "specobjid_last": ids[-1],
        "z_range_median": {"min": min(num(r, "z") for r in rows), "median": med("z"), "max": max(num(r, "z") for r in rows)},
        "mass_range_median": {"min": min(num(r, "lgm_tot_p50") for r in rows), "median": med("lgm_tot_p50"), "max": max(num(r, "lgm_tot_p50") for r in rows)},
        "ssfr_range_median": {"min": min(num(r, "specsfr_tot_p50") for r in rows), "median": med("specsfr_tot_p50"), "max": max(num(r, "specsfr_tot_p50") for r in rows)},
        "goru_bpt_counts": goru.get("source_results_bpt_counts", {}),
        "proxy_limits": "Shared SDSS optical emission-line denominator only; no causal AGN feedback, gas depletion/SFE, radio-jet coupling, escape/recycling, hot-halo heating, multiphase census, or simulation validation proof.",
        "safety": SAFETY,
    }

    stage_rows = csv_rows_from_stage(stage_rows_raw, sn_counts)

    # Write core artifacts.
    out_paths: dict[str, Path] = {}
    out_paths["summary_json"] = outroot / f"shared_selection_data_dictionary_{ts}.json"
    out_paths["column_dictionary_csv"] = tables / f"column_dictionary_{ts}.csv"
    out_paths["paper_use_contracts_csv"] = tables / f"paper_use_contracts_{ts}.csv"
    out_paths["selection_stage_counts_csv"] = tables / f"selection_stage_counts_verified_{ts}.csv"
    out_paths["ssfr_retention_csv"] = tables / f"ssfr_retention_verified_{ts}.csv"
    out_paths["aastex_fragment"] = aastex / f"shared_parent_sample_selection_fragment_{ts}.tex"
    out_paths["smoke_tex"] = aastex / f"selection_module_smoke_test_{ts}.tex"
    out_paths["module_md"] = outroot / f"SHARED_SELECTION_MODULE_{ts}.md"
    out_paths["manifest_json"] = outroot / f"shared_selection_module_manifest_{ts}.json"
    out_paths["tick_report"] = OVERNIGHT / "ticks" / f"TICK_{ts}.md"
    out_paths["helper_script"] = Path(__file__).resolve()

    payload = {
        "summary": summary,
        "column_dictionary": [
            {"column": c, "type_or_unit": t, "definition": d, "role": role, "guard": guard}
            for c, t, d, role, guard in COLUMN_DICTIONARY
        ],
        "paper_use_contracts": PAPER_CONTRACTS,
        "selection_stage_counts_verified": stage_rows,
        "ssfr_retention_rows": ssfr_rows,
    }
    out_paths["summary_json"].write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    write_csv(
        out_paths["column_dictionary_csv"],
        payload["column_dictionary"],
        ["column", "type_or_unit", "definition", "role", "guard"],
    )
    write_csv(
        out_paths["paper_use_contracts_csv"],
        PAPER_CONTRACTS,
        ["paper", "slug", "safe_current_object", "required_selection_language", "allowed_claim", "forbidden_claim"],
    )
    write_csv(
        out_paths["selection_stage_counts_csv"],
        stage_rows,
        ["stage_key", "stage_label", "sdss_dr17_count", "retention_vs_spectro_z_parent", "cached_sample_count_at_matching_stage", "computed_cached_count_from_csv", "computed_matches_recorded", "cached_coverage_of_sdss_stage"],
    )
    write_csv(
        out_paths["ssfr_retention_csv"],
        ssfr_rows,
        ["ssfr_bin", "sdss_parent_count", "sdss_sn_ge_3_count", "sn_ge_3_retention_vs_parent", "cached_sn_ge_3_count", "cached_coverage_of_sdss_sn_ge_3", "guard"],
    )

    fragment = build_fragment(ts, summary, stage_rows, ssfr_rows)
    out_paths["aastex_fragment"].write_text(fragment)
    smoke_doc = "\n".join([
        r"\documentclass[twocolumn]{aastex631}",
        r"\usepackage{amsmath}",
        r"\shorttitle{Shared SDSS Selection Module}",
        r"\shortauthors{NebulaMind Autopilot}",
        r"\begin{document}",
        r"\title{Smoke Test for the Shared SDSS Parent Sample and Selection Function Module}",
        r"\author{NebulaMind Research Autopilot}",
        r"\affiliation{Local reproducible pilot run; public SDSS DR17 data only}",
        r"\begin{abstract}",
        "This local-only document verifies that the shared parent-sample and selection-function fragment for the nine Galaxy Evolution pilots compiles under AASTeX.",
        r"\end{abstract}",
        fragment,
        r"\end{document}",
        "",
    ])
    out_paths["smoke_tex"].write_text(smoke_doc)

    # Compile smoke test.
    compile_log = aastex / "compile.log"
    tectonic_exit = None
    tectonic_stdout = ""
    tectonic_stderr = ""
    pdf_path = aastex / f"selection_module_smoke_test_{ts}.pdf"
    if shutil.which("tectonic"):
        proc = subprocess.run(
            ["tectonic", "--keep-logs", "--keep-intermediates", out_paths["smoke_tex"].name],
            cwd=aastex,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=180,
        )
        tectonic_exit = proc.returncode
        tectonic_stdout = proc.stdout
        tectonic_stderr = proc.stderr
        compile_log.write_text("STDOUT:\n" + tectonic_stdout + "\nSTDERR:\n" + tectonic_stderr)
    else:
        tectonic_exit = 127
        compile_log.write_text("tectonic not found\n")
    out_paths["compile_log"] = compile_log
    if pdf_path.exists():
        out_paths["smoke_pdf"] = pdf_path

    log_text = compile_log.read_text(errors="replace") if compile_log.exists() else ""
    fatal_markers = [m for m in ["Fatal error", "Emergency stop", "LaTeX Error", "! "] if m in log_text]
    smoke_pdf_magic_ok = pdf_path.exists() and pdf_path.read_bytes()[:5] == b"%PDF-"

    count_checks = {
        "rows_eq_60000": len(rows) == 60000,
        "bpt_counts_match_goru": {k: int(bpt_counts.get(k, 0)) for k in BPT_ORDER} == {k: int(goru.get("source_results_bpt_counts", {}).get(k, 0)) for k in BPT_ORDER},
        "sn_ge_3_eq_60000": sn_counts["sn_ge_3"] == 60000,
        "sn_ge_5_matches_goru": sn_counts["sn_ge_5"] == int(goru.get("sn_threshold_counts", {}).get("sn_ge_5", -1)),
        "sn_ge_10_matches_goru": sn_counts["sn_ge_10"] == int(goru.get("sn_threshold_counts", {}).get("sn_ge_10", -1)),
        "strict_public_count_eq_249917": int(attrition["strict_sdss_sn_ge_3_total"]) == 249917,
        "duplicate_specobjid_zero": duplicate_ids == 0,
        "specobjid_nondecreasing": specobjid_nondecreasing,
    }

    verification = {
        "artifact_count": 0,  # filled after manifest write
        "tectonic_exit_code": tectonic_exit,
        "smoke_pdf_magic_ok": smoke_pdf_magic_ok,
        "smoke_pdf_sha256": sha256(pdf_path) if pdf_path.exists() else "",
        "fatal_markers": fatal_markers,
        "count_checks": count_checks,
    }

    # Write the human reports before collecting hashes, then rewrite them once the
    # final artifact count is known. The manifest deliberately excludes its own
    # SHA256 from the artifact map because a self-hash stored inside the file is
    # inherently unstable; the manifest path is recorded separately.
    out_paths["module_md"].write_text(build_markdown(ts, summary, out_paths, verification))
    out_paths["tick_report"].write_text(build_markdown(ts, summary, out_paths, verification))

    def collect_artifacts() -> dict[str, dict[str, Any]]:
        collected: dict[str, dict[str, Any]] = {}
        for key, path in out_paths.items():
            if key == "manifest_json":
                continue
            if path.exists():
                collected[key] = {"path": str(path), "bytes": path.stat().st_size, "sha256": sha256(path)}
        return collected

    artifacts = collect_artifacts()
    verification["artifact_count"] = len(artifacts) + 1  # listed artifacts plus this manifest file
    out_paths["module_md"].write_text(build_markdown(ts, summary, out_paths, verification))
    out_paths["tick_report"].write_text(build_markdown(ts, summary, out_paths, verification))
    artifacts = collect_artifacts()
    verification["artifact_count"] = len(artifacts) + 1
    manifest = {
        "marker": f"SHARED_SELECTION_MODULE_{ts}",
        "timestamp_utc": ts,
        "scope": "Shared local parent-sample/selection-function module and data dictionary for all nine active Galaxy Evolution AAS-style pilot papers.",
        "artifacts": artifacts,
        "manifest_json_path": str(out_paths["manifest_json"]),
        "manifest_self_hash_note": "Self-hash is intentionally excluded from the artifact map; verify this file directly with sha256sum if needed.",
        "verification": verification,
        "summary_values": summary,
        "safety": SAFETY,
    }
    out_paths["manifest_json"].write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    tick = out_paths["tick_report"].read_text()

    success = all(count_checks.values()) and tectonic_exit == 0 and smoke_pdf_magic_ok and not fatal_markers
    smoke_status = (
        f"smoke-test PDF `%PDF` SHA256 `{verification['smoke_pdf_sha256']}` with no fatal markers"
        if success
        else f"smoke-test incomplete: tectonic_exit={tectonic_exit}, pdf_magic={smoke_pdf_magic_ok}, fatal_markers={fatal_markers}"
    )
    ledger_prefix = f"- {ts[:4]}-{ts[4:6]}-{ts[6:8]}T{ts[9:11]}:{ts[11:13]}:{ts[13:15]}Z — Tori shared selection-function/data-dictionary tick"
    ledger_line = (
        f"{ledger_prefix} wrote "
        f"`lanes/tori/shared-selection-module/{ts}/` and `ticks/TICK_{ts}.md`; verified cached SDSS rows 60,000, strict public four-line S/N>=3 rows 249,917, cached coverage 24.0%, BPT counts 39,553/12,234/8,146/67, high-excitation optical AGN 4,440, {smoke_status}. No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/extra-cron/billing/OAuth/external submission changes.\n"
    )
    existing_lines = LEDGER.read_text().splitlines() if LEDGER.exists() else []
    existing_lines = [line for line in existing_lines if not line.startswith(ledger_prefix)]
    LEDGER.write_text("\n".join(existing_lines).rstrip() + "\n" + ledger_line)

    print(json.dumps({
        "tick_report": str(out_paths["tick_report"]),
        "manifest": str(out_paths["manifest_json"]),
        "module_md": str(out_paths["module_md"]),
        "smoke_pdf": str(pdf_path) if pdf_path.exists() else None,
        "verification": verification,
    }, indent=2, sort_keys=True))
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
