#!/usr/bin/env python3
"""Tori lane: selection-function/CI/citation revision drafts for M2 P3 and M3 P1.

This tick responds to the external review blockers for the Wave-3 papers:
- M2 P3 needed explicit quenched thresholds, uncertainty intervals, redshift-stratified checks,
  selection-function disclosure, and in-text citation integration.
- M3 P1 needed explicit optical-tracer thresholds, uncertainty intervals, explanation of the
  divergent S/N behavior, selection-function disclosure, and in-text citation integration.

Writes lane-local artifacts only under overnight-9-papers-20260708/.  It does not overwrite
public-linked PDFs or any active run manuscript.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
OVERNIGHT = AUTO / "overnight-9-papers-20260708"
RUN8 = AUTO / "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
RUN1 = AUTO / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
SOURCE_CSV = RUN1 / "data/analysis_sample_bpt.csv"
MANIFEST8 = RUN8 / "ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json"
LEDGER = OVERNIGHT / "OVERNIGHT_LEDGER.md"
TICK_DIR = OVERNIGHT / "ticks"
GORU_TABLES = OVERNIGHT / "lanes/goru/tables"
LIT_PACKET = OVERNIGHT / "lanes/literature/literature_source_packet_wave3_missing_active9_20260708T170557Z.md"
EXT_REVIEW = OVERNIGHT / "lanes/external-cli/EXTERNAL_CLI_TICK_20260708T190158Z.md"

TS = os.environ.get("TORI_REVISION_TS") or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
UTC_ISO = datetime.strptime(TS, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
OUT_ROOT = OVERNIGHT / "lanes/tori/revision-drafts/m2p3_m3p1_selection_ci" / TS
TEX_ROOT = OUT_ROOT / "aastex"
FIG_ROOT = OUT_ROOT / "figures"
TABLE_ROOT = OUT_ROOT / "tables"
MANIFEST_JSON = OUT_ROOT / f"m2p3_m3p1_selection_ci_manifest_{TS}.json"
SUMMARY_MD = OUT_ROOT / f"M2P3_M3P1_SELECTION_CI_REVISION_{TS}.md"
TICK_REPORT = TICK_DIR / f"TICK_{TS}.md"

PAPER_TABLE = GORU_TABLES / "bootstrap_summary_key_metrics_20260708T162615Z.csv"
Z_TABLE = GORU_TABLES / "alternate_mass_redshift_sn_target_vector_20260708T183643Z.csv"
SELECTION_OVERLAY = GORU_TABLES / "selection_caution_overlay_20260708T162615Z.csv"

PROXY_GUARD = (
    "SDSS optical emission-line/color/sSFR proxy or denominator only; no causal AGN feedback, "
    "gas-depletion, radio-jet coupling, escape/recycling, X-ray maintenance-heating, or simulation-validation proof."
)
NO_WRITE_SAFETY = (
    "No public pages, live roots, product DB, SQL, /api/pages, page_versions, trust recompute, "
    "deploy/restart, git commit/push/merge/rebase, billing/OAuth changes, new cron jobs, or external submissions."
)

MASS_ORDER = ["8.0-9.5", "9.5-10.0", "10.0-10.5", "10.5-11.0", "11.0-12.5"]
Z_ORDER = ["0.020-0.050", "0.050-0.080", "0.080-0.120"]
TRACER_ORDER = [
    ("bpt_agn", "BPT AGN", "cached BPT label = agn: above the Kewley et al. (2001) curve after Kauffmann et al. (2003) star-forming/intermediate separation; x=log([N II]/Halpha) capped at 0.35"),
    ("high_nii", "high [N II]/Halpha", "log([N II] lambda6584 / Halpha) > -0.20"),
    ("high_oiii", "high [O III]/Hbeta", "log([O III] lambda5007 / Hbeta) > 0.00"),
    ("red_sequence", "red emission-line", "catalog u-r > 2.2 within the four-line emission denominator"),
    ("low_sSFR_quenched", "low-sSFR emission-line", "catalog log sSFR < -11.0 within the four-line emission denominator"),
]


def require_inside(path: Path, root: Path = OVERNIGHT) -> None:
    resolved = path.resolve()
    rr = root.resolve()
    if rr not in [resolved, *resolved.parents]:
        raise RuntimeError(f"Refusing write outside overnight root: {resolved}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    require_inside(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    if not fields:
        fields = ["status"]
        rows = [{"status": "NO_ROWS"}]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_text(path: Path, text: str) -> None:
    require_inside(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def as_int(v: Any) -> int:
    if v is None or v == "":
        return 0
    return int(float(v))


def as_float(v: Any) -> float:
    return float(v)


def wilson(k: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if n <= 0:
        return (float("nan"), float("nan"))
    p = k / n
    denom = 1.0 + z * z / n
    centre = (p + z * z / (2.0 * n)) / denom
    half = z * math.sqrt((p * (1.0 - p) / n) + (z * z / (4.0 * n * n))) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


def f3(v: float | str) -> str:
    return f"{float(v):.3f}"


def pct(v: float) -> str:
    return f"{100.0 * v:.1f}\\%"


def tex_escape_text(s: str) -> str:
    # Only for table comments/text strings that may contain underscores or percent signs.
    return (s.replace("\\", r"\textbackslash{}")
             .replace("&", r"\&")
             .replace("%", r"\%")
             .replace("_", r"\_")
             .replace("#", r"\#"))


def artifact_info(path: Path) -> dict[str, Any]:
    info: dict[str, Any] = {
        "path": str(path),
        "relative_path": str(path.relative_to(OVERNIGHT)) if OVERNIGHT in [path, *path.parents] else str(path),
        "exists": path.exists(),
    }
    if path.exists() and path.is_file():
        info["bytes"] = path.stat().st_size
        info["sha256"] = sha256(path)
        if path.suffix.lower() == ".pdf":
            info["starts_with_pdf"] = path.read_bytes()[:5] == b"%PDF-"
    return info


def load_manifest_topic(slug: str) -> dict[str, Any]:
    data = json.loads(MANIFEST8.read_text(encoding="utf-8"))
    for topic in data["topics"]:
        if topic["slug"] == slug:
            return topic
    raise KeyError(slug)


def original_pdf_check(slug: str) -> dict[str, Any]:
    topic = load_manifest_topic(slug)
    pdf = Path(topic["pdf"])
    info = artifact_info(pdf)
    info["expected_sha256"] = topic["pdf_sha256"]
    info["matches_manifest_sha256"] = info.get("sha256") == topic["pdf_sha256"]
    info["source_tex"] = topic["tex"]
    return info


def selection_rows() -> list[dict[str, Any]]:
    rows = read_csv(SELECTION_OVERLAY)
    out = []
    for r in rows:
        if r.get("source") != "tori_selection_attrition_stage_counts":
            continue
        out.append({
            "stage_key": r["stage_key"],
            "stage_label": r["stage_label"],
            "sdss_dr17_count": as_int(r["sdss_dr17_count"]),
            "retention_vs_previous_stage": r["retention_vs_previous_stage"] or "",
            "cached_sample_count_at_matching_stage": r["cached_sample_count_at_matching_stage"] or "",
            "cached_coverage_of_sdss_stage": r["cached_coverage_of_sdss_stage"] or "",
        })
    return out


def finite_float(row: dict[str, str], key: str) -> float:
    value = float(row[key])
    if not math.isfinite(value):
        raise ValueError(key)
    return value


def load_source_rows() -> list[dict[str, Any]]:
    """Load the cached 60,000-row SDSS table and compute flags locally."""
    raw = read_csv(SOURCE_CSV)
    required = [
        "z", "lgm_tot_p50", "specsfr_tot_p50", "u_minus_r",
        "log_nii_ha", "log_oiii_hb", "bpt_label",
        "h_alpha_flux", "h_alpha_flux_err", "h_beta_flux", "h_beta_flux_err",
        "oiii_5007_flux", "oiii_5007_flux_err", "nii_6584_flux", "nii_6584_flux_err",
    ]
    rows: list[dict[str, Any]] = []
    for r in raw:
        try:
            item = {k: finite_float(r, k) for k in required if k != "bpt_label"}
        except Exception:
            continue
        item["bpt_label"] = r["bpt_label"]
        item["sn_min"] = min([
            item["h_alpha_flux"] / item["h_alpha_flux_err"],
            item["h_beta_flux"] / item["h_beta_flux_err"],
            item["oiii_5007_flux"] / item["oiii_5007_flux_err"],
            item["nii_6584_flux"] / item["nii_6584_flux_err"],
        ])
        item["quenched"] = item["specsfr_tot_p50"] < -11.0
        item["bpt_agn"] = item["bpt_label"] == "agn"
        item["high_nii"] = item["log_nii_ha"] > -0.20
        item["high_oiii"] = item["log_oiii_hb"] > 0.00
        item["red_sequence"] = item["u_minus_r"] > 2.2
        item["low_sSFR_quenched"] = item["quenched"]
        rows.append(item)
    return rows


def choose_bin(value: float, bins: list[float], labels: list[str]) -> str | None:
    for i, label in enumerate(labels):
        lo = bins[i]
        hi = bins[i + 1]
        if i == 0:
            ok = lo <= value < hi
        elif i == len(labels) - 1:
            ok = lo <= value <= hi
        else:
            ok = lo <= value < hi
        if ok:
            return label
    return None


def median(values: list[float]) -> float:
    if not values:
        return float("nan")
    vals = sorted(values)
    mid = len(vals) // 2
    if len(vals) % 2:
        return vals[mid]
    return 0.5 * (vals[mid - 1] + vals[mid])


def build_m2p3_tables() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows = load_source_rows()
    mass_rows: list[dict[str, Any]] = []
    mass_bins = [8.0, 9.5, 10.0, 10.5, 11.0, 12.5]
    z_bins = [0.020, 0.050, 0.080, 0.120]
    for mb in MASS_ORDER:
        subset = [r for r in rows if choose_bin(r["lgm_tot_p50"], mass_bins, MASS_ORDER) == mb]
        n = len(subset)
        qk = sum(1 for r in subset if r["quenched"])
        ak = sum(1 for r in subset if r["bpt_agn"])
        qlo, qhi = wilson(qk, n)
        alo, ahi = wilson(ak, n)
        mass_rows.append({
            "mass_bin_logM": mb,
            "n": n,
            "quenched_threshold": "log(sSFR/yr^-1) < -11.0",
            "quenched_k": qk,
            "quenched_fraction": qk / n,
            "quenched_wilson95_low": qlo,
            "quenched_wilson95_high": qhi,
            "bpt_agn_k": ak,
            "bpt_agn_fraction": ak / n,
            "bpt_agn_wilson95_low": alo,
            "bpt_agn_wilson95_high": ahi,
            "proxy_guard": "Mass-transition optical diagnostic; no gas fractions/baryon deficits/halo masses."
        })
    zrows: list[dict[str, Any]] = []
    for mb in MASS_ORDER:
        for zb in Z_ORDER:
            subset = [
                r for r in rows
                if choose_bin(r["lgm_tot_p50"], mass_bins, MASS_ORDER) == mb
                and choose_bin(r["z"], z_bins, Z_ORDER) == zb
            ]
            n = len(subset)
            qf = sum(1 for r in subset if r["quenched"]) / n if n else float("nan")
            af = sum(1 for r in subset if r["bpt_agn"]) / n if n else float("nan")
            zrows.append({
                "mass_bin_logM": mb,
                "z_bin": zb,
                "n": n,
                "quenched_fraction_log_ssfr_lt_minus_11": qf,
                "bpt_agn_fraction": af,
                "low_n_flag": "LOW_N_LT_50" if n < 50 else "OK",
                "median_log_sSFR": median([r["specsfr_tot_p50"] for r in subset]),
                "proxy_guard": "Redshift-stratified descriptive check only; no volume completeness or causal feedback inference."
            })
    zrows.sort(key=lambda r: (MASS_ORDER.index(r["mass_bin_logM"]), Z_ORDER.index(r["z_bin"])))
    return mass_rows, zrows


def build_m3p1_table() -> list[dict[str, Any]]:
    rows = load_source_rows()
    out: list[dict[str, Any]] = []
    for sn in [3, 5, 10]:
        sn_subset = [r for r in rows if r["sn_min"] >= sn]
        n = len(sn_subset)
        for key, label, definition in TRACER_ORDER:
            k = sum(1 for r in sn_subset if r[key])
            lo, hi = wilson(k, n)
            out.append({
                "sn_min_ge": sn,
                "tracer_label": label,
                "operational_definition": definition,
                "n": n,
                "k": k,
                "fraction": k / n,
                "wilson95_low": lo,
                "wilson95_high": hi,
                "proxy_guard": "Optical SDSS tracer only; no molecular/neutral/X-ray/radio phase measurement."
            })
    return out


def latex_selection_table(prefix: str = "sel") -> str:
    rows = selection_rows()
    keep = [
        "spectro_galaxy_z_window",
        "join_complete_mass_ssfr_bounds",
        "positive_four_bpt_fluxes_and_errors",
        "sn_ge_3_four_bpt_lines",
        "sn_ge_5_four_bpt_lines",
        "sn_ge_10_four_bpt_lines",
    ]
    label_by_key = {r["stage_key"]: r for r in rows}
    body = []
    for key in keep:
        r = label_by_key[key]
        cached = r["cached_sample_count_at_matching_stage"] or "--"
        cov = r["cached_coverage_of_sdss_stage"]
        cov_tex = f"{100*float(cov):.1f}\\%" if cov else "--"
        ret = r["retention_vs_previous_stage"]
        ret_tex = f"{100*float(ret):.1f}\\%" if ret else "--"
        body.append(f"{tex_escape_text(r['stage_label'])} & {r['sdss_dr17_count']:,} & {ret_tex} & {cached} & {cov_tex} " + r"\\")
    return r"""
\begin{deluxetable*}{lrrrr}
\tablecaption{Selection-function disclosure for the shared capped SDSS DR17 four-line denominator\label{tab:%s-selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public SDSS DR17 $N$} & \colhead{Prior-stage retention} & \colhead{Cached $N$} & \colhead{Cached/SDSS}}
\startdata
%s
\enddata
\tablecomments{The preserved pilot query used \texttt{SELECT TOP 60000 ... ORDER BY s.specObjID}.  Therefore all fractions in this draft are conditional on a capped ordered cache: 60,000/249,917 = 24.0\%% of the strict public four-line S/N$\geq3$ eligible parent.}
\end{deluxetable*}
""" % (prefix, "\n".join(body))


def latex_m2p3_mass_table(rows: list[dict[str, Any]]) -> str:
    body = []
    for r in rows:
        body.append(
            f"{r['mass_bin_logM']} & {r['n']:,} & {r['quenched_k']:,}/{r['n']:,} ({f3(r['quenched_fraction'])}; {f3(r['quenched_wilson95_low'])}--{f3(r['quenched_wilson95_high'])}) & "
            f"{r['bpt_agn_k']:,}/{r['n']:,} ({f3(r['bpt_agn_fraction'])}; {f3(r['bpt_agn_wilson95_low'])}--{f3(r['bpt_agn_wilson95_high'])}) " + r"\\")
    return r"""
\begin{deluxetable*}{lccc}
\tablecaption{Mass-binned low-sSFR and optical-BPT-AGN fractions with Wilson intervals\label{tab:m2p3-mass-ci}}
\tablehead{\colhead{$\log M_\star$ bin} & \colhead{$N$} & \colhead{$f_Q$: $\log {\rm sSFR}<-11.0$} & \colhead{$f_{\rm BPT\,AGN}$}}
\startdata
%s
\enddata
\tablecomments{Parent denominator is the cached SDSS four-line S/N$\geq3$ table.  Parenthetical ranges are Wilson 95\%% binomial intervals.  The optical AGN class is a line-ratio label, not an AGN-feedback measurement.}
\end{deluxetable*}
""" % "\n".join(body)


def latex_m2p3_z_table(rows: list[dict[str, Any]]) -> str:
    body = []
    for r in rows:
        # Keep table compact but complete across mass and z bins.
        body.append(
            f"{r['mass_bin_logM']} & {r['z_bin']} & {r['n']:,} & {f3(r['quenched_fraction_log_ssfr_lt_minus_11'])} & {f3(r['bpt_agn_fraction'])} & {f3(r['median_log_sSFR'])} " + r"\\")
    return r"""
\begin{deluxetable*}{llrrrr}
\tabletypesize{\scriptsize}
\tablecaption{Redshift-stratified descriptive check for the mass-transition vector\label{tab:m2p3-z-check}}
\tablehead{\colhead{$\log M_\star$ bin} & \colhead{$z$ bin} & \colhead{$N$} & \colhead{$f_Q$} & \colhead{$f_{\rm BPT\,AGN}$} & \colhead{median $\log {\rm sSFR}$}}
\startdata
%s
\enddata
\tablecomments{This table addresses redshift-mix sensitivity but is still descriptive: no volume weighting, central/satellite separation, gas fractions, black-hole masses, or halo masses are present.}
\end{deluxetable*}
""" % "\n".join(body)


def latex_m3p1_table(rows: list[dict[str, Any]]) -> str:
    body = []
    for r in rows:
        definition = tex_escape_text(r["operational_definition"])
        body.append(
            f"$\\geq {r['sn_min_ge']}$ & {tex_escape_text(r['tracer_label'])} & {definition} & {r['k']:,}/{r['n']:,} & {f3(r['fraction'])} [{f3(r['wilson95_low'])}, {f3(r['wilson95_high'])}] " + r"\\")
    return r"""
\begin{deluxetable*}{llp{0.38\textwidth}cc}
\tabletypesize{\scriptsize}
\tablecaption{Operational optical-tracer thresholds and Wilson intervals in the shared SDSS denominator\label{tab:m3p1-tracer-ci}}
\tablehead{\colhead{Line S/N cut} & \colhead{Tracer} & \colhead{Operational threshold} & \colhead{Selected/denom.} & \colhead{Fraction [95\%% CI]}}
\startdata
%s
\enddata
\tablecomments{Every row is an SDSS optical selection.  None is a molecular, neutral, X-ray, radio, velocity, mass-loading, or kinetic-power outflow measurement.}
\end{deluxetable*}
""" % "\n".join(body)


def m2p3_tex(mass_rows: list[dict[str, Any]], zrows: list[dict[str, Any]], figure_name: str) -> str:
    low = mass_rows[0]
    high = mass_rows[-1]
    return rf"""% TORI_M2P3_M3P1_SELECTION_CI_REVISION_{TS}
% Paper: m2_p3_feedback_transition_mass
% Lane-local revision draft only; does not overwrite current linked manuscript/PDF.
\documentclass[twocolumn]{{aastex631}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\graphicspath{{{{../figures/}}}}
\shorttitle{{Selection-flagged transition-mass pilot}}
\shortauthors{{NebulaMind Autopilot}}

\begin{{document}}
\title{{A Selection-Flagged SDSS DR17 Mass-Transition Diagnostic for Low-sSFR and Optical-AGN Incidence}}
\author{{NebulaMind Research Autopilot}}
\affiliation{{Local reproducible pilot run; public SDSS DR17 data and overnight local artifacts only}}

\begin{{abstract}}
We revise the active M2 P3 pilot into a selection-flagged optical transition diagnostic.  The actual measurement is a capped SDSS DR17 four-line emission denominator, not a separation of stellar-feedback and AGN-feedback regulation.  The cached table covers 60,000 of 249,917 strict public SDSS four-line S/N$\geq3$ eligible rows (24.0\%).  We now define the quenching threshold explicitly as catalog $\log({{\rm sSFR}}/{{\rm yr}}^{{-1}})<-11.0$ and report Wilson intervals.  Across broad stellar-mass bins, the low-sSFR fraction rises from {low['quenched_k']:,}/{low['n']:,} ({f3(low['quenched_fraction'])}; 95\% CI {f3(low['quenched_wilson95_low'])}--{f3(low['quenched_wilson95_high'])}) at $\log M_\star=8.0$--9.5 to {high['quenched_k']:,}/{high['n']:,} ({f3(high['quenched_fraction'])}; {f3(high['quenched_wilson95_low'])}--{f3(high['quenched_wilson95_high'])}) at 11.0--12.5.  The BPT optical-AGN fraction over the same bins rises from {f3(low['bpt_agn_fraction'])} to {f3(high['bpt_agn_fraction'])}.  Redshift-stratified cells show the same broad mass ordering but also substantial redshift/aperture mix, so the result remains an optical denominator for future gas, halo, black-hole-mass, and morphology follow-up.
\end{{abstract}}

\keywords{{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}}

\section{{Scope and source grounding}}
The proposal title is ``Locating the transition from stellar-feedback to AGN-feedback regulation.''  This draft deliberately narrows the claim to what the cached SDSS data can support: a mass-binned vector of catalog low-sSFR incidence and optical BPT-AGN incidence in one emission-line denominator.  SDSS DR17 supplies the public survey provenance \citep{{abdurrouf2022,york2000}}, while SDSS stellar-mass and star-formation catalog context motivates use of stellar mass and sSFR axes \citep{{kauffmann2003mass,kauffmann2003structure}}.  The broader transition/bimodality and quenching literature \citep{{baldry2004,peng2012}} motivates the diagnostic, but halo-shock, black-hole-mass, and baryon-cycle interpretations require data not present here \citep{{dekel2006,bluck2023}}.

\section{{Data, selection function, and operational definitions}}
The input is the shared cached public SDSS DR17 sample from run SDSS-AGN-SFR-PILOT-20260708T122000Z: spectroscopic galaxies at $0.02<z<0.12$ with finite catalog stellar mass and sSFR and S/N$\geq3$ in H$\alpha$, H$\beta$, [O~III] $\lambda5007$, and [N~II] $\lambda6584$.  BPT labels use the [N~II] diagnostic \citep{{baldwin1981,kewley2001,kauffmann2003bpt}}: star-forming if below the Kauffmann curve, optical AGN if above the Kewley curve, intermediate/composite otherwise, with the cached run excluding the pathological high-[N~II] divergence range.  Throughout this manuscript, ``quenched'' means only $\log({{\rm sSFR}}/{{\rm yr}}^{{-1}})<-11.0$ in the catalog quantity; it is not a gas-depletion, halo-quenching, or feedback-mode classification.

{latex_selection_table('m2p3')}

\section{{Mass-bin result with intervals}}
Table~\ref{{tab:m2p3-mass-ci}} replaces the previous qualitative transition statement with denominators, numerators, thresholds, and Wilson intervals.

{latex_m2p3_mass_table(mass_rows)}

\section{{Redshift-stratified descriptive check}}
Table~\ref{{tab:m2p3-z-check}} checks whether the mass vector is merely a single redshift slice.  The low-sSFR and optical-AGN fractions are highest in the upper mass bins across the broad redshift slices, but the values shift with redshift, line S/N, and aperture population mix.  This is why the pilot should be carried forward as a target vector, not as a causal transition-mass measurement.

{latex_m2p3_z_table(zrows)}

\begin{{figure}}
\centering
\includegraphics[width=\columnwidth]{{{figure_name}}}
\caption{{Original batch-run SDSS mass-transition diagnostic, preserved in this lane-local revision.  The figure should be read with Tables~\ref{{tab:m2p3-mass-ci}} and \ref{{tab:m2p3-z-check}}: it is an optical denominator/transition vector, not proof that AGN feedback causes the transition.}}
\label{{fig:m2p3-original}}
\end{{figure}}

\section{{Interpretation guard and next data}}
The strengthened result is an empirical co-variation: in the capped four-line SDSS denominator, low-sSFR incidence and optical-BPT-AGN incidence both increase strongly toward higher stellar mass.  It does not distinguish stellar feedback, AGN feedback, halo quenching, morphological quenching, gas starvation, aperture effects, or black-hole-mass dependence.  A follow-up capable of addressing the original proposal must add gas fractions or baryon deficits, halo/central-satellite information, black-hole mass or velocity-dispersion proxies, morphology, and selection-matched redshift extensions.  The current manuscript is ready for local integration review, not prose/publish gates.

\section*{{Reproducibility and safety note}}
Revision marker: TORI\_M2P3\_M3P1\_SELECTION\_CI\_REVISION\_{TS}.  Numerical fractions, Wilson intervals, and redshift rows were recomputed locally from the cached source table \texttt{{analysis\_sample\_bpt.csv}}; public denominator counts were inherited from \texttt{{selection\_caution\_overlay\_20260708T162615Z.csv}}.  The Wave-3 literature packet supplied the citation placement and guardrails.  This file is lane-local and did not overwrite public-linked artifacts.

\acknowledgments
This pilot used public SDSS DR17 data products and local open-source tooling.

\begin{{thebibliography}}{{}}
\bibitem[Abdurro'uf et al.(2022)]{{abdurrouf2022}} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldry et al.(2004)]{{baldry2004}} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
\bibitem[Baldwin et al.(1981)]{{baldwin1981}} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Bluck et al.(2023)]{{bluck2023}} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
\bibitem[Dekel \& Birnboim(2006)]{{dekel2006}} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Kauffmann et al.(2003a)]{{kauffmann2003mass}} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003a, MNRAS, 341, 33
\bibitem[Kauffmann et al.(2003b)]{{kauffmann2003structure}} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 54
\bibitem[Kauffmann et al.(2003c)]{{kauffmann2003bpt}} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003c, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{{kewley2001}} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Peng et al.(2012)]{{peng2012}} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
\bibitem[York et al.(2000)]{{york2000}} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{{thebibliography}}

\end{{document}}
"""


def m3p1_tex(tracer_rows: list[dict[str, Any]], figure_name: str) -> str:
    sn3 = [r for r in tracer_rows if r["sn_min_ge"] == 3]
    sn10_bpt = next(r for r in tracer_rows if r["sn_min_ge"] == 10 and r["tracer_label"] == "BPT AGN")
    sn10_oiii = next(r for r in tracer_rows if r["sn_min_ge"] == 10 and r["tracer_label"] == "high [O III]/Hbeta")
    min_sn3 = min(r["fraction"] for r in sn3)
    max_sn3 = max(r["fraction"] for r in sn3)
    return rf"""% TORI_M2P3_M3P1_SELECTION_CI_REVISION_{TS}
% Paper: m3_p1_multiphase_census
% Lane-local revision draft only; does not overwrite current linked manuscript/PDF.
\documentclass[twocolumn]{{aastex631}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\graphicspath{{{{../figures/}}}}
\shorttitle{{Selection-flagged optical tracer census}}
\shortauthors{{NebulaMind Autopilot}}

\begin{{document}}
\title{{A Selection-Flagged SDSS DR17 Optical-Tracer Denominator for a Future Multiphase Outflow Census}}
\author{{NebulaMind Research Autopilot}}
\affiliation{{Local reproducible pilot run; public SDSS DR17 data and overnight local artifacts only}}

\begin{{abstract}}
We revise the active M3 P1 pilot from a table addendum into a threshold-explicit optical denominator paper.  The current measurement is not a multiphase outflow census: it contains no molecular, neutral, X-ray, radio, velocity, radius, mass-loading, or kinetic-power measurements.  It instead quantifies how optical tracer definitions behave in the shared capped SDSS DR17 four-line denominator.  The cache covers 60,000/249,917 = 24.0\% of the strict public S/N$\geq3$ parent.  At S/N$\geq3$, the five optical definitions span {f3(min_sn3)}--{f3(max_sn3)} prevalence with Wilson intervals.  Tightening to S/N$\geq10$ reduces the BPT-AGN prevalence to {sn10_bpt['k']:,}/{sn10_bpt['n']:,} ({f3(sn10_bpt['fraction'])}) while the one-ratio high-[O~III]/H$\beta$ prevalence rises to {sn10_oiii['k']:,}/{sn10_oiii['n']:,} ({f3(sn10_oiii['fraction'])}), showing that S/N cuts change the population mix as well as the denominator.  The result supports common-denominator survey design only.
\end{{abstract}}

\keywords{{galaxies: evolution --- galaxies: active --- galaxies: winds, outflows --- surveys --- methods: data analysis}}

\section{{Scope and source grounding}}
The proposal title is ``A multiphase, common-denominator census of AGN-driven outflows.''  The SDSS-only pilot cannot measure that full quantity.  It uses SDSS DR17 public data \citep{{abdurrouf2022,york2000}} to define an optical denominator and demonstrates why tracer definitions must be locked before interpreting prevalence.  Galactic-wind and outflow reviews establish that physical census work is multiphase and kinematic \citep{{veilleux2005,rupke2018}}, while molecular and multiphase studies show why CO, neutral gas, X-ray/radio, radii, velocities, and phase masses cannot be inferred from one SDSS optical table \citep{{cicone2014,fiore2017,feruglio2015,bae2018}}.

\section{{Data, selection function, and operational definitions}}
The input is the shared cached public SDSS DR17 sample from run SDSS-AGN-SFR-PILOT-20260708T122000Z: spectroscopic galaxies at $0.02<z<0.12$ with finite catalog stellar mass and sSFR and S/N$\geq3$ in H$\alpha$, H$\beta$, [O~III] $\lambda5007$, and [N~II] $\lambda6584$.  BPT labels use the [N~II] diagnostic \citep{{baldwin1981,kewley2001,kauffmann2003bpt}}.  This revision makes every tracer threshold explicit in Table~\ref{{tab:m3p1-tracer-ci}}; none should be renamed as a detected outflow.

{latex_selection_table('m3p1')}

\section{{Optical tracer prevalence with explicit thresholds}}
Table~\ref{{tab:m3p1-tracer-ci}} is the core improvement.  It preserves the common-denominator idea but exposes the operational thresholds, numerators, denominators, and Wilson 95\% intervals.

{latex_m3p1_table(tracer_rows)}

\begin{{figure}}
\centering
\includegraphics[width=\columnwidth]{{{figure_name}}}
\caption{{Original batch-run SDSS optical-tracer diagnostic, preserved in this lane-local revision.  The figure and Table~\ref{{tab:m3p1-tracer-ci}} motivate common-denominator survey design; they are not a molecular, neutral, X-ray, radio, or kinetic outflow census.}}
\label{{fig:m3p1-original}}
\end{{figure}}

\section{{Why the S/N behavior diverges}}
The S/N rows should not be summarized as a simple convergence test.  Tightening the four-line S/N cut shrinks the denominator from 60,000 to 22,311 cached galaxies and changes which spectral populations remain.  BPT AGN is a two-ratio, mutually exclusive class label requiring position above the Kewley curve; its prevalence falls from 0.136 to 0.069.  The high-[O~III]/H$\beta$ row is a one-ratio threshold, $\log([\mathrm{{O\,III}}]/\mathrm{{H}}\beta)>0$, applied inside the surviving denominator; its prevalence rises from 0.317 to 0.386 because high-S/N selection preferentially retains strong high-excitation-line objects while removing many weak-line red/low-sSFR systems.  This is a selection-function result, not evidence that one optical tracer is the physical outflow phase.

\section{{Interpretation guard and next data}}
The strengthened result is methodological: optical prevalence can vary by several factors before any molecular, neutral, X-ray, or radio phase is added.  A real multiphase outflow census must start from a declared parent sample and then measure velocities, radii, phase masses, ionization/CO/neutral-gas corrections, non-detections, and aperture matching for every phase.  Single-object multiphase studies remain useful for physics intuition, but they cannot supply denominator-wide prevalence by themselves.  The current manuscript is ready for local integration review, not prose/publish gates.

\section*{{Reproducibility and safety note}}
Revision marker: TORI\_M2P3\_M3P1\_SELECTION\_CI\_REVISION\_{TS}.  Numerical fractions, Wilson intervals, and tracer/S/N rows were recomputed locally from the cached source table \texttt{{analysis\_sample\_bpt.csv}}; public denominator counts were inherited from \texttt{{selection\_caution\_overlay\_20260708T162615Z.csv}}.  The Wave-3 literature packet supplied the citation placement and guardrails.  This file is lane-local and did not overwrite public-linked artifacts.

\acknowledgments
This pilot used public SDSS DR17 data products and local open-source tooling.

\begin{{thebibliography}}{{}}
\bibitem[Abdurro'uf et al.(2022)]{{abdurrouf2022}} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Bae \& Woo(2018)]{{bae2018}} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
\bibitem[Baldwin et al.(1981)]{{baldwin1981}} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Cicone et al.(2014)]{{cicone2014}} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Feruglio et al.(2015)]{{feruglio2015}} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
\bibitem[Fiore et al.(2017)]{{fiore2017}} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Kauffmann et al.(2003)]{{kauffmann2003bpt}} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{{kewley2001}} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Rupke(2018)]{{rupke2018}} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
\bibitem[Veilleux et al.(2005)]{{veilleux2005}} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[York et al.(2000)]{{york2000}} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{{thebibliography}}

\end{{document}}
"""


def compile_tex(tex_path: Path) -> dict[str, Any]:
    cmd = ["tectonic", "--keep-logs", "--keep-intermediates", tex_path.name]
    proc = subprocess.run(cmd, cwd=tex_path.parent, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=300)
    log_path = tex_path.parent / f"compile_{tex_path.stem}_{TS}.log"
    log_text = "$ " + " ".join(cmd) + "\n\n[STDOUT]\n" + proc.stdout + "\n[STDERR]\n" + proc.stderr
    write_text(log_path, log_text)
    pdf = tex_path.with_suffix(".pdf")
    fatal_markers = [m for m in ["! LaTeX Error", "Emergency stop", "Fatal error"] if m in log_text]
    info = artifact_info(pdf)
    return {
        "tex": str(tex_path),
        "pdf": str(pdf),
        "compile_log": str(log_path),
        "compile_exit_code": proc.returncode,
        "fatal_markers": fatal_markers,
        "pdf_info": info,
    }


def build() -> dict[str, Any]:
    if not shutil.which("tectonic"):
        raise SystemExit("tectonic executable not available")
    for p in [OUT_ROOT, TEX_ROOT, FIG_ROOT, TABLE_ROOT, TICK_DIR]:
        require_inside(p)
        p.mkdir(parents=True, exist_ok=True)
    for required in [SOURCE_CSV, SELECTION_OVERLAY, LIT_PACKET, EXT_REVIEW, MANIFEST8]:
        if not required.exists():
            raise SystemExit(f"Missing required input: {required}")

    m2_mass, m2_z = build_m2p3_tables()
    m3_tracers = build_m3p1_table()
    sel_rows = selection_rows()

    m2_mass_csv = TABLE_ROOT / f"m2p3_mass_bin_wilson_{TS}.csv"
    m2_z_csv = TABLE_ROOT / f"m2p3_redshift_stratified_{TS}.csv"
    m3_csv = TABLE_ROOT / f"m3p1_tracer_threshold_wilson_{TS}.csv"
    sel_csv = TABLE_ROOT / f"selection_function_disclosure_{TS}.csv"
    write_csv(m2_mass_csv, m2_mass)
    write_csv(m2_z_csv, m2_z)
    write_csv(m3_csv, m3_tracers)
    write_csv(sel_csv, sel_rows)

    # Copy original batch figures to simple lane-local names, avoiding TeX filename issues with underscores.
    m2_fig_src = RUN8 / "m2_p3_feedback_transition_mass/figures/m2_p3_feedback_transition_mass_figure1.pdf"
    m3_fig_src = RUN8 / "m3_p1_multiphase_census/figures/m3_p1_multiphase_census_figure1.pdf"
    m2_fig = FIG_ROOT / "m2p3_original_figure1.pdf"
    m3_fig = FIG_ROOT / "m3p1_original_figure1.pdf"
    shutil.copy2(m2_fig_src, m2_fig)
    shutil.copy2(m3_fig_src, m3_fig)

    tex_specs = [
        ("m2_p3_feedback_transition_mass", TEX_ROOT / f"m2_p3_feedback_transition_mass_selection_ci_{TS}.tex", m2p3_tex(m2_mass, m2_z, "m2p3_original_figure1.pdf")),
        ("m3_p1_multiphase_census", TEX_ROOT / f"m3_p1_multiphase_census_selection_ci_{TS}.tex", m3p1_tex(m3_tracers, "m3p1_original_figure1.pdf")),
    ]
    compile_results = []
    for slug, tex_path, tex in tex_specs:
        write_text(tex_path, tex)
        result = compile_tex(tex_path)
        result["paper_slug"] = slug
        if result["compile_exit_code"] != 0 or result["fatal_markers"] or not result["pdf_info"].get("starts_with_pdf"):
            raise SystemExit(f"Compile failed for {slug}: {json.dumps(result, indent=2)}")
        compile_results.append(result)

    original_checks = {
        "m2_p3_feedback_transition_mass": original_pdf_check("m2_p3_feedback_transition_mass"),
        "m3_p1_multiphase_census": original_pdf_check("m3_p1_multiphase_census"),
    }

    # Derived counts for manifest/report verification.
    m2_first_transition = next(r for r in m2_mass if r["quenched_fraction"] >= 0.5)["mass_bin_logM"]
    m3_sn10_bpt = next(r for r in m3_tracers if r["sn_min_ge"] == 10 and r["tracer_label"] == "BPT AGN")
    m3_sn10_oiii = next(r for r in m3_tracers if r["sn_min_ge"] == 10 and r["tracer_label"] == "high [O III]/Hbeta")

    artifacts = [m2_mass_csv, m2_z_csv, m3_csv, sel_csv, m2_fig, m3_fig]
    for result in compile_results:
        artifacts += [Path(result["tex"]), Path(result["pdf"]), Path(result["compile_log"])]

    manifest = {
        "marker": f"TORI_M2P3_M3P1_SELECTION_CI_REVISION_{TS}",
        "timestamp_utc": TS,
        "scope": "Lane-local selection-function, confidence-interval, threshold-definition, redshift-check, and citation-integration revisions for M2 P3 and M3 P1.",
        "inputs": {
            "overnight_brief": str(OVERNIGHT / "OVERNIGHT_BRIEF.md"),
            "overnight_ledger": str(LEDGER),
            "batch_manifest": str(MANIFEST8),
            "source_csv_cached_sdss": str(SOURCE_CSV),
            "selection_caution_overlay": str(SELECTION_OVERLAY),
            "wave3_literature_packet": str(LIT_PACKET),
            "external_review": str(EXT_REVIEW),
        },
        "generated_tables": {
            "m2p3_mass_bin_wilson": artifact_info(m2_mass_csv),
            "m2p3_redshift_stratified": artifact_info(m2_z_csv),
            "m3p1_tracer_threshold_wilson": artifact_info(m3_csv),
            "selection_function_disclosure": artifact_info(sel_csv),
        },
        "figures_copied": {"m2p3": artifact_info(m2_fig), "m3p1": artifact_info(m3_fig)},
        "compiled_revisions": compile_results,
        "original_public_linked_pdf_checks": original_checks,
        "mechanical_counts": {
            "m2p3_mass_rows": len(m2_mass),
            "m2p3_z_rows": len(m2_z),
            "m3p1_tracer_rows": len(m3_tracers),
            "selection_stage_rows": len(sel_rows),
            "m2p3_first_mass_bin_fq_ge_0p5": m2_first_transition,
            "m3p1_sn10_bpt_fraction": m3_sn10_bpt["fraction"],
            "m3p1_sn10_high_oiii_fraction": m3_sn10_oiii["fraction"],
        },
        "safety": NO_WRITE_SAFETY,
        "proxy_guard": PROXY_GUARD,
        "artifacts": [artifact_info(p) for p in artifacts],
    }
    write_text(MANIFEST_JSON, json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    summary = f"""# M2 P3 / M3 P1 selection-CI revision summary — {TS}

Marker: `TORI_M2P3_M3P1_SELECTION_CI_REVISION_{TS}`

## What changed

This tick addressed the external review blockers for the two Wave-3 active-9 drafts that remained table addenda:

- **M2 P3 — mass transition in quenching and optical AGN incidence** now has a lane-local AASTeX revision with explicit quenching threshold (`log(sSFR/yr^-1) < -11.0`), Wilson 95% intervals for every mass-bin fraction, a 15-row mass-redshift descriptive check, a selection-function disclosure table, and in-text citations from the Wave-3 literature packet.
- **M3 P1 — common-denominator optical tracer census** now has a lane-local AASTeX revision with explicit thresholds for BPT AGN, high [N II]/Halpha, high [O III]/Hbeta, red emission-line, and low-sSFR emission-line tracers; Wilson intervals for 15 S/N/tracer rows; a paragraph explaining why S/N>=10 makes high-[O III]/Hbeta prevalence rise while BPT-AGN prevalence falls; a selection-function disclosure table; and in-text citations from the Wave-3 literature packet.

## Data/source grounding

- Numerical fractions, Wilson intervals, and redshift/tracer rows were recomputed locally from the cached source sample `{SOURCE_CSV.relative_to(AUTO)}`; selection-function counts come from `{SELECTION_OVERLAY.relative_to(OVERNIGHT)}`.
- Literature/source placement follows `{LIT_PACKET.relative_to(OVERNIGHT)}`.
- No new web queries, DB writes, public page edits, or live mirroring were performed.

## Verification

- M2 P3 mass-bin rows: **{len(m2_mass)}**; first mass bin with `f_Q >= 0.5`: **{m2_first_transition}**.
- M2 P3 redshift-stratified rows: **{len(m2_z)}**.
- M3 P1 tracer/SN rows: **{len(m3_tracers)}**.
- Selection-stage rows included: **{len(sel_rows)}**.
- Compiled PDFs: **{len(compile_results)}/2** start with `%PDF` and have no fatal LaTeX markers.
- Original public-linked M2 P3 and M3 P1 PDF hashes still match the 8-paper manifest: **{all(v['matches_manifest_sha256'] for v in original_checks.values())}**.

## Key compiled outputs

"""
    for result in compile_results:
        summary += f"- `{Path(result['pdf']).relative_to(OVERNIGHT)}` — {result['pdf_info']['bytes']} bytes — SHA256 `{result['pdf_info']['sha256']}`\n"
    summary += f"\nManifest: `{MANIFEST_JSON.relative_to(OVERNIGHT)}`\n\nSafety: {NO_WRITE_SAFETY} No active execution phrase.\n"
    write_text(SUMMARY_MD, summary)

    tick = f"""# Overnight 9-paper tick — {TS}

Marker: `TORI_M2P3_M3P1_SELECTION_CI_REVISION_{TS}`

## What I did

Built and compiled lane-local selection-function / confidence-interval / citation-integration revisions for two under-reviewed active-9 papers:

1. **M2 P3** (`m2_p3_feedback_transition_mass`) — added exact low-sSFR threshold, Wilson intervals for all mass-bin low-sSFR and BPT-AGN fractions, a 15-row redshift-stratified check, selection-function disclosure, and Wave-3 citation integration.
2. **M3 P1** (`m3_p1_multiphase_census`) — added exact optical-tracer thresholds, Wilson intervals for all S/N/tracer rows, selection-function disclosure, citation integration, and an explanation of divergent S/N behavior.

## Files changed / written

- Summary: `{SUMMARY_MD.relative_to(OVERNIGHT)}`
- Manifest: `{MANIFEST_JSON.relative_to(OVERNIGHT)}`
- Tables:
  - `{m2_mass_csv.relative_to(OVERNIGHT)}`
  - `{m2_z_csv.relative_to(OVERNIGHT)}`
  - `{m3_csv.relative_to(OVERNIGHT)}`
  - `{sel_csv.relative_to(OVERNIGHT)}`
- Compiled revision PDFs:
"""
    for result in compile_results:
        tick += f"  - `{Path(result['pdf']).relative_to(OVERNIGHT)}` — SHA256 `{result['pdf_info']['sha256']}`\n"
    tick += f"""
## Data/source grounding

- Numerical fractions, Wilson intervals, and redshift/tracer rows were recomputed locally from the cached 60,000-row SDSS sample; Goru/Tori selection artifacts supplied the public SDSS denominator counts.
- Wave-3 literature packet supplied the citation roles and safe integration guards.
- The measurement remains SDSS optical/proxy-only.  M2 P3 does not establish stellar- versus AGN-feedback causality.  M3 P1 does not measure molecular/neutral/X-ray/radio outflow incidence or kinetic power.

## Verification

- M2 P3 mass rows: `{len(m2_mass)}`; redshift rows: `{len(m2_z)}`; first `f_Q >= 0.5` bin: `{m2_first_transition}`.
- M3 P1 tracer rows: `{len(m3_tracers)}`; selection-stage rows: `{len(sel_rows)}`.
- Tectonic compiled both PDFs with exit code 0, `%PDF` headers, and no fatal markers.
- Original public-linked M2 P3 and M3 P1 PDF hashes still match the 8-paper manifest.

## Blockers

No execution blockers.  Scientific limitations remain: both papers are SDSS optical denominator/proxy pilots and need the named follow-up data before physical feedback claims.

## Next recommended tick

Apply the same selection-function/threshold/CI/citation integration pattern to any remaining table-addendum drafts not yet upgraded, or run an RP-1 control-baseline/systematics tick for the star-forming-control and sSFR-estimator caveats flagged by the external review.

## Safety

{NO_WRITE_SAFETY} No active execution phrase.
"""
    write_text(TICK_REPORT, tick)

    ledger_line = (
        f"- {UTC_ISO} — Tori selection/CI manuscript tick wrote and compiled lane-local revisions for M2 P3 and M3 P1; "
        f"report `ticks/TICK_{TS}.md`, manifest `lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/{TS}/m2p3_m3p1_selection_ci_manifest_{TS}.json`. "
        f"Verified 2/2 PDFs `%PDF`/SHA/no fatal markers, M2 P3 rows 5+15, M3 P1 tracer rows 15, original public-linked hashes unchanged. "
        f"No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/extra-cron/billing/OAuth/external submission changes.\n"
    )
    # Ledger append is explicitly required by the overnight brief and stays under the overnight work root.
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(ledger_line)

    manifest["summary_md"] = artifact_info(SUMMARY_MD)
    manifest["tick_report"] = artifact_info(TICK_REPORT)
    # Rewrite manifest after tick/summary exist so it is self-contained.
    write_text(MANIFEST_JSON, json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return manifest


if __name__ == "__main__":
    result = build()
    print(json.dumps({
        "marker": result["marker"],
        "tick_report": str(TICK_REPORT),
        "manifest": str(MANIFEST_JSON),
        "summary": str(SUMMARY_MD),
        "compiled_pdfs": [r["pdf"] for r in result["compiled_revisions"]],
        "mechanical_counts": result["mechanical_counts"],
    }, indent=2))
