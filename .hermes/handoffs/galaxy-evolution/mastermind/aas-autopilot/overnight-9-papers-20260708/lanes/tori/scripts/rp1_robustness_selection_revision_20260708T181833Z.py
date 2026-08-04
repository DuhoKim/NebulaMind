#!/usr/bin/env python3
"""Build a lane-local RP-1 robustness/selection-function AASTeX revision.

Reads existing RP-1 manuscript and prior overnight Goru/Tori artifacts, writes a
new draft under lanes/tori/revision-drafts/, compiles it with tectonic, and
records a manifest. Does not overwrite public-linked PDFs or live/public pages.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

TS = "20260708T181833Z"
UTC_ISO = "2026-07-08T18:18:33Z"
LOCAL_NOTE = "2026-07-09 03:18:33 KST"

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
OVERNIGHT = AUTO / "overnight-9-papers-20260708"
RUN = AUTO / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
ORIG_TEX = RUN / "aastex/sdss_agn_sfr_pilot_aas.tex"
OUT_ROOT = OVERNIGHT / "lanes/tori/revision-drafts/rp1_robustness_selection" / TS
TEX_DIR = OUT_ROOT / "aastex"
FIG_DIR = OUT_ROOT / "figures"
SUMMARY_MD = OUT_ROOT / f"RP1_ROBUSTNESS_SELECTION_REVISION_{TS}.md"
MANIFEST_JSON = OUT_ROOT / f"rp1_robustness_selection_manifest_{TS}.json"

GORU_FIG = OVERNIGHT / "lanes/goru/figures/matched_offset_sensitivity_20260708T162615Z.pdf"
SELECTION_JSON = OVERNIGHT / "lanes/tori/selection-function-attrition/20260708T155514Z/selection_function_attrition_summary_20260708T155514Z.json"
GORU_TABLE = OVERNIGHT / "lanes/goru/tables/bpt_class_sensitivity_matched_offsets_20260708T162615Z.csv"
LIT_PACKET = OVERNIGHT / "lanes/literature/literature_source_packet_wave3_missing_active9_20260708T170557Z.md"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_unique_replacement(tex: str, old: str, new: str, label: str) -> str:
    count = tex.count(old)
    if count != 1:
        raise SystemExit(f"Expected one match for {label}, found {count}")
    return tex.replace(old, new)


def build_tex() -> str:
    tex = ORIG_TEX.read_text()
    tex = ensure_unique_replacement(
        tex,
        "\\title{A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts}",
        "\\title{A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts: Selection-Function and Robustness Revision}",
        "title",
    )
    tex = ensure_unique_replacement(
        tex,
        "A simple linear model adjusted for stellar mass and redshift gives an AGN coefficient of $-1.20\\pm 0.01$ dex.  The result demonstrates a reproducible survey-analysis path from the proposal to a measurable quantity, but it should not be read as causal evidence for AGN feedback: optical selection, aperture effects, star-formation estimator assumptions, morphology, halo environment, and AGN duty-cycle timing remain uncontrolled.",
        "A simple linear model adjusted for stellar mass and redshift gives an AGN coefficient of $-1.20\\pm 0.01$ dex.  A selection-function and robustness pass materially qualifies the headline number: public SDSS count checks show that the capped 60,000-row cache covers only 24.0\\% of the 249,917 strict four-line S/N$\\geq3$ eligible rows, and the median matched offset weakens to $-1.16$ dex at S/N$\\geq5$, $-0.74$ dex at S/N$\\geq10$, and $-0.76$ dex for a Seyfert-like [N~II]-branch proxy.  The result demonstrates a reproducible survey-analysis path from the proposal to a measurable quantity, but it should not be read as causal evidence for AGN feedback: optical selection, aperture effects, star-formation estimator assumptions, retired/LINER-like ionization, morphology, halo environment, and AGN duty-cycle timing remain uncontrolled.",
        "abstract robustness insertion",
    )
    tex = ensure_unique_replacement(
        tex,
        "This paper is a first autopilot execution of that proposal.  We use public SDSS DR17 spectroscopy and photometry to build an emission-line galaxy sample, classify sources on the [N~II] BPT diagram \\citep{baldwin1981,kewley2001,kauffmann2003}, and compare optical AGN hosts to star-forming controls matched in stellar mass and redshift.  The analysis deliberately stops at a pilot association measurement.  It does not attempt to measure molecular-gas depletion, mechanical-energy coupling, halo environment, or the AGN duty cycle.",
        "This paper is a first local execution of that proposal, now revised to expose the selection function and robustness envelope before any physical interpretation.  We use public SDSS DR17 spectroscopy and photometry \\citep{abdurrouf2022} to build an emission-line galaxy sample, classify sources on the [N~II] BPT diagram \\citep{baldwin1981,kewley2001,kauffmann2003,kewley2006}, and compare optical AGN hosts to star-forming controls matched in stellar mass and redshift.  Prior low-redshift work on the AGN--star-formation connection \\citep{lamassa2013} motivates the association test, but the analysis deliberately stops at a pilot association measurement.  It does not attempt to measure molecular-gas depletion, mechanical-energy coupling, halo environment, or the AGN duty cycle.",
        "intro citation/source guard insertion",
    )
    tex = ensure_unique_replacement(
        tex,
        "The sample is queried from SDSS DR17 SkyServer through \\texttt{astroquery.sdss}.  We join SDSS spectroscopic objects, photometric model magnitudes, emission-line measurements, and derived stellar-mass/star-formation quantities exposed through the public catalog tables.  The local query is preserved with the data products in the run directory.",
        "The sample is queried from SDSS DR17 SkyServer through \\texttt{astroquery.sdss}; SDSS DR17 is the public survey release described by \\citet{abdurrouf2022}.  We join SDSS spectroscopic objects, photometric model magnitudes, emission-line measurements, and derived stellar-mass/star-formation quantities exposed through the public catalog tables.  The stellar-mass and star-formation quantities follow the SDSS physical-property/catalog context of \\citet{brinchmann2004}.  The local query is preserved with the data products in the run directory.",
        "data citation insertion",
    )
    selection_block = r"""

\subsection{Selection-function disclosure}\label{sec:selection_function}
This revision adds an explicit denominator audit because the cached sample is not a random draw from all low-redshift SDSS galaxies.  A read-only public SDSS DR17 count query finds 501,060 spectroscopic galaxies at $0.02<z<0.12$; after joins, mass/sSFR bounds, positive four-line flux/error requirements, and four BPT lines at S/N$\geq3$, the strict eligible parent contains 249,917 rows.  The preserved pilot query uses \texttt{SELECT TOP 60000 ... ORDER BY s.specObjID}, so the cached analysis table covers 60,000/249,917 = 24.0\% of the strict four-line eligible parent rather than the full denominator.  The four-line requirement is also sSFR-dependent: the public count audit retains only 33.56\% of the $-12<\log\mathrm{sSFR}<-11$ parent bin at S/N$\geq3$, compared with 94.85\% for $-10<\log\mathrm{sSFR}<-9.5$.  Therefore all incidence and matched-offset statements below are statements about this capped, emission-line selected optical denominator.

\begin{deluxetable*}{lrrrr}
\tablecaption{Public SDSS DR17 selection-function counts for the optical-denominator pilot\label{tab:selectionfunction}}
\tablehead{\colhead{Stage} & \colhead{SDSS DR17 $N$} & \colhead{Prev. retention} & \colhead{Cached $N$} & \colhead{Cached/SDSS}}
\startdata
SpecObj GALAXY, $0.02<z<0.12$ & 501,060 & -- & -- & -- \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & 83.1\% & -- & -- \\
plus galSpecLine join & 416,554 & 100.0\% & -- & -- \\
four BPT lines positive with positive errors & 373,445 & 89.7\% & 60,000 & 16.1\% \\
four BPT lines S/N$\geq3$ & 249,917 & 66.9\% & 60,000 & 24.0\% \\
four BPT lines S/N$\geq5$ & 176,523 & 70.6\% & 42,446 & 24.0\% \\
four BPT lines S/N$\geq10$ & 91,768 & 52.0\% & 22,311 & 24.3\% \\
\enddata
\tablecomments{Counts come from the overnight read-only public SDSS count audit.  They diagnose the denominator and cached-row cap; they are not evidence for a causal feedback mechanism.}
\end{deluxetable*}
"""
    tex = ensure_unique_replacement(
        tex,
        "The selection requires spectroscopic class \\texttt{GALAXY}, $0.02<z<0.12$, positive H$\\alpha$, H$\\beta$, [O~III]$\\lambda5007$, and [N~II]$\\lambda6584$ fluxes, and signal-to-noise ratio $\\geq3$ in all four lines.  We also require $8.0 < \\log(M_\\star/M_\\odot) < 12.5$ and $-14 < \\log({\\rm sSFR}/{\\rm yr}^{-1}) < -7$ in the catalog median estimates.  The query returns 60,000 rows; all satisfy the analysis cuts after finite-value filtering.",
        "The selection requires spectroscopic class \\texttt{GALAXY}, $0.02<z<0.12$, positive H$\\alpha$, H$\\beta$, [O~III]$\\lambda5007$, and [N~II]$\\lambda6584$ fluxes, and signal-to-noise ratio $\\geq3$ in all four lines.  We also require $8.0 < \\log(M_\\star/M_\\odot) < 12.5$ and $-14 < \\log({\\rm sSFR}/{\\rm yr}^{-1}) < -7$ in the catalog median estimates.  The query returns 60,000 rows; all satisfy the analysis cuts after finite-value filtering." + selection_block,
        "selection-function section insertion",
    )
    tex = ensure_unique_replacement(
        tex,
        "Objects between those curves are labeled intermediate/composite.  For each optical AGN host, we identify the nearest star-forming control in standardized $(\\log M_\\star,z)$ space using a KD-tree.",
        "Objects between those curves are labeled intermediate/composite.  This revision keeps the original broad BPT-AGN label for reproducibility, but interprets it as an optical ionization proxy: Seyfert/LINER separation and retired-galaxy contamination are known limitations of line-ratio-only classifications \\citep{kewley2006,stasinska2015}.  For each optical AGN host, we identify the nearest star-forming control in standardized $(\\log M_\\star,z)$ space using a KD-tree.",
        "classification guard insertion",
    )
    robustness_block = r"""

\subsection{Robustness to line strength and optical-AGN proxy}\label{sec:robustness}
Table~\ref{tab:robustness} and Figure~\ref{fig:robustness} summarize the overnight robustness pass.  The sign of the matched offset remains negative across the tested optical definitions, but the magnitude changes substantially.  Raising the four-line threshold from S/N$\geq3$ to S/N$\geq10$ reduces the broad-BPT matched median from $-1.31$ dex to $-0.74$ dex.  Within the S/N$\geq3$ cached sample, a high-excitation proxy gives $-1.14$ dex, while an [N~II]-branch Seyfert-like proxy gives $-0.76$ dex and a LINER-like proxy gives $-1.47$ dex.  The latter split is especially important: the large broad-BPT offset is partly a statement about which low-ionization systems enter the optical-AGN side, not a direct measurement of feedback shutting off star formation.

\begin{deluxetable*}{llrrrr}
\tablecaption{BPT/S/N sensitivity of matched optical-class sSFR offsets\label{tab:robustness}}
\tablehead{\colhead{S/N cut} & \colhead{Target definition} & \colhead{$N_{target}$} & \colhead{$N_{ctrl}$} & \colhead{Median $\Delta\log\mathrm{sSFR}$} & \colhead{95\% CI}}
\startdata
$\geq$3 & broad BPT AGN vs. BPT star-forming & 8,146 & 39,553 & -1.31 & [-1.33, -1.28] \\
$\geq$5 & broad BPT AGN vs. BPT star-forming & 4,032 & 31,252 & -1.16 & [-1.21, -1.13] \\
$\geq$10 & broad BPT AGN vs. BPT star-forming & 1,530 & 18,131 & -0.74 & [-0.78, -0.72] \\
$\geq$3 & high-excitation $\log([\mathrm{O\,III}]/\mathrm{H}\beta)>0.25$ proxy & 4,440 & 39,553 & -1.14 & [-1.18, -1.10] \\
$\geq$3 & [N~II]-branch Seyfert-like proxy & 2,114 & 39,553 & -0.76 & [-0.82, -0.72] \\
$\geq$3 & [N~II]-branch LINER-like proxy & 6,032 & 39,553 & -1.47 & [-1.49, -1.44] \\
\enddata
\tablecomments{All rows match the target optical class to star-forming controls in stellar-mass/redshift space.  Values are association checks in the capped SDSS emission-line denominator, not causal feedback evidence.}
\end{deluxetable*}

\begin{figure*}
\centering
\includegraphics[width=0.92\textwidth]{../figures/matched_offset_sensitivity_20260708T162615Z.pdf}
\caption{Matched sSFR offset sensitivity from the overnight Goru robustness artifact.  The figure is included in this lane-local revision to make the selection/proxy dependence visible in the manuscript itself.  It should travel with any later integration draft before the headline $-1.31$ dex result is used.}
\label{fig:robustness}
\end{figure*}
"""
    tex = ensure_unique_replacement(
        tex,
        "As a simple regression cross-check, we fit $\\log{\\rm sSFR} = \\beta_0 + \\beta_1 I_{\\rm AGN} + \\beta_2\\log M_\\star + \\beta_3 z$ to the star-forming plus AGN classes.  The AGN indicator coefficient is $-1.20\\pm0.01$ dex, with a nominal 95\\% interval of $[-1.21,-1.19]$ dex.  Both the matched and regression summaries therefore recover a large optical-AGN-associated sSFR deficit in this bounded pilot sample.",
        "As a simple regression cross-check, we fit $\\log{\\rm sSFR} = \\beta_0 + \\beta_1 I_{\\rm AGN} + \\beta_2\\log M_\\star + \\beta_3 z$ to the star-forming plus AGN classes.  The AGN indicator coefficient is $-1.20\\pm0.01$ dex, with a nominal 95\\% interval of $[-1.21,-1.19]$ dex.  Both the matched and regression summaries therefore recover a large optical-AGN-associated sSFR deficit in this bounded pilot sample, but the robustness pass below shows that its magnitude is not invariant to line-strength and optical-subclass choices." + robustness_block,
        "robustness results insertion",
    )
    tex = ensure_unique_replacement(
        tex,
        "The pilot result is qualitatively consistent with the idea that optical AGN hosts often occupy lower-sSFR regions than emission-line star-forming galaxies at similar redshift and stellar mass.  However, the interpretation is intentionally narrow.  BPT-selected optical AGN include heterogeneous ionization sources and may overlap with LINER-like systems.  SDSS fiber apertures probe central regions whose physical scale varies with redshift.  The catalog sSFR estimates depend on modeling assumptions that can interact with AGN contamination and weak star formation.  The matching used here controls only stellar mass and redshift; morphology, environment, halo mass, gas mass, dust, and AGN luminosity are not included.",
        "The pilot result is qualitatively consistent with the idea that optical AGN hosts often occupy lower-sSFR regions than emission-line star-forming galaxies at similar redshift and stellar mass.  However, the interpretation is intentionally narrow.  BPT-selected optical AGN include heterogeneous ionization sources and may overlap with LINER-like or retired-galaxy systems \\citep{kewley2006,stasinska2015}.  SDSS fiber apertures probe central regions whose physical scale varies with redshift.  The catalog sSFR estimates depend on modeling assumptions that can interact with AGN contamination and weak star formation.  The matching used here controls only stellar mass and redshift; morphology, environment, halo mass, gas mass, dust, aperture covering fraction, stellar-continuum ionization, and AGN luminosity are not included.\n\nThe new selection and robustness checks change how the headline number should be carried forward.  The $-1.31$ dex median is the broad-BPT, S/N$\\geq3$, capped-cache estimate.  The smaller S/N$\\geq10$ and Seyfert-like values show that a more conservative optical-AGN definition yields a still-negative but substantially weaker association.  Conversely, the LINER-like branch yields a stronger deficit but is exactly where retired/old-stellar-population ionization is a stronger concern.  A later publishable analysis should therefore report a bracketed optical-association range rather than a single causal-sounding deficit.",
        "discussion robustness guard insertion",
    )
    tex = ensure_unique_replacement(
        tex,
        "\\item Nearest-neighbor matching in stellar mass and redshift gives a median optical-AGN sSFR offset of -1.31 dex relative to star-forming controls, with bootstrap 95\\% interval $[-1.33,-1.28]$ dex.\n\\item The analysis supports a real survey-measurement path for the proposal, but it remains an association pilot and does not establish causal AGN feedback.",
        "\\item Nearest-neighbor matching in stellar mass and redshift gives a median broad-BPT optical-AGN sSFR offset of -1.31 dex relative to star-forming controls, with bootstrap 95\\% interval $[-1.33,-1.28]$ dex.\n\\item Selection-function and robustness checks are now manuscript-visible: the cached table is 60,000/249,917 = 24.0\\% of the strict public SDSS four-line S/N$\\geq3$ denominator, and the matched median weakens to -0.74 dex at S/N$\\geq10$ and -0.76 dex for a Seyfert-like proxy.\n\\item The analysis supports a real survey-measurement path for the proposal, but it remains an association pilot and does not establish causal AGN feedback.",
        "conclusion robustness insertion",
    )
    tex = ensure_unique_replacement(
        tex,
        "The run identifier is SDSS-AGN-SFR-PILOT-20260708T122000Z.  The preserved artifacts include the SQL query, CSV tables, figures, JSON summary, manuscript source, and compiled PDF.  The workflow used a read-only public SDSS query plus local artifact writes only.",
        "The source run identifier is SDSS-AGN-SFR-PILOT-20260708T122000Z.  This lane-local revision identifier is RP1-ROBUSTNESS-SELECTION-REVISION-20260708T181833Z.  The preserved artifacts include the original SQL query, CSV tables, figures, JSON summary, manuscript source, compiled PDF, the overnight selection-function audit, and the overnight Goru robustness tables/figure.  The workflow used read-only public SDSS/literature artifacts plus local artifact writes only.",
        "reproducibility note insertion",
    )
    extra_bib = r"""
\bibitem[Abdurro'uf et al.(2022)]{abdurrouf2022} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJ, 765, L33
\bibitem[Stasi\'nska et al.(2015)]{stasinska2015} Stasi\'nska, G., Costa-Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodr\'e, L. 2015, MNRAS, 449, 559
"""
    tex = ensure_unique_replacement(
        tex,
        "\\begin{thebibliography}{}\n\\bibitem[Baldwin et al.(1981)]{baldwin1981}",
        "\\begin{thebibliography}{}\n" + extra_bib + "\\bibitem[Baldwin et al.(1981)]{baldwin1981}",
        "bibliography source insertion",
    )
    return tex


def main() -> None:
    if not ORIG_TEX.exists():
        raise SystemExit(f"Missing original TeX: {ORIG_TEX}")
    if not GORU_FIG.exists():
        raise SystemExit(f"Missing Goru robustness figure: {GORU_FIG}")
    if not shutil.which("tectonic"):
        raise SystemExit("tectonic executable not available")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    TEX_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    # Preserve source figures and robustness figure inside the lane-local revision packet.
    copied_figures = []
    for fig in [
        RUN / "figures/figure1_bpt.pdf",
        RUN / "figures/figure2_matched_offsets.pdf",
        GORU_FIG,
    ]:
        dest = FIG_DIR / fig.name
        shutil.copy2(fig, dest)
        copied_figures.append(str(dest))

    tex = build_tex()
    tex_name = f"sdss_agn_sfr_pilot_rp1_robustness_selection_{TS}.tex"
    tex_path = TEX_DIR / tex_name
    tex_path.write_text(tex)

    proc = subprocess.run(
        ["tectonic", tex_path.name],
        cwd=TEX_DIR,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=240,
    )
    compile_log = TEX_DIR / "compile.log"
    compile_log.write_text(proc.stdout)
    pdf_path = TEX_DIR / tex_path.with_suffix(".pdf").name
    pdf_magic_ok = pdf_path.exists() and pdf_path.read_bytes().startswith(b"%PDF")
    fatal_markers = [m for m in ["! LaTeX Error", "Fatal error", "Emergency stop", "No pages of output"] if m in proc.stdout]

    manifest = {
        "marker": f"RP1_ROBUSTNESS_SELECTION_REVISION_{TS}",
        "utc": UTC_ISO,
        "local": LOCAL_NOTE,
        "scope": "Lane-local RP-1 manuscript revision adding selection-function disclosure, BPT/SN robustness table/figure, source guardrails, and safer interpretation.",
        "source_tex": str(ORIG_TEX),
        "output_root": str(OUT_ROOT),
        "tex": str(tex_path),
        "pdf": str(pdf_path),
        "compile_log": str(compile_log),
        "compile_exit_code": proc.returncode,
        "pdf_magic_ok": pdf_magic_ok,
        "fatal_markers": fatal_markers,
        "pdf_bytes": pdf_path.stat().st_size if pdf_path.exists() else 0,
        "pdf_sha256": sha256(pdf_path) if pdf_path.exists() else None,
        "copied_figures": copied_figures,
        "inputs": {
            "source_run": str(RUN),
            "selection_summary_json": str(SELECTION_JSON),
            "goru_bpt_sensitivity_csv": str(GORU_TABLE),
            "goru_sensitivity_figure_pdf": str(GORU_FIG),
            "literature_wave3_packet": str(LIT_PACKET),
        },
        "inserted_key_values": {
            "strict_sdss_sn_ge_3_total": 249917,
            "cached_rows": 60000,
            "cached_coverage": 0.24007970646254556,
            "ssfr_low_bin_sn3_retention": 0.33556547619047616,
            "ssfr_starforming_bin_sn3_retention": 0.948504069604266,
            "baseline_bpt_sn3_median_delta": -1.3088869999999995,
            "bpt_sn5_median_delta": -1.1604679999999998,
            "bpt_sn10_median_delta": -0.7444849999999992,
            "high_excitation_sn3_median_delta": -1.13591,
            "nii_seyfert_like_sn3_median_delta": -0.7630850000000002,
            "nii_liner_like_sn3_median_delta": -1.468985,
        },
        "safety": "Local lane artifact only. No public/live page changes, DB/API/page_versions/trust, deploy/restart, git, cron, billing/OAuth, or external submission.",
    }
    MANIFEST_JSON.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    summary = f"""# RP-1 robustness/selection-function revision

Marker: `RP1_ROBUSTNESS_SELECTION_REVISION_{TS}`

UTC: {UTC_ISO}  
Local: {LOCAL_NOTE}

## What changed

Created a lane-local AASTeX revision for **M1 RP-1 — SDSS AGN/sSFR matched-control pilot**. The revision does not replace the public-linked PDF. It adds:

- an explicit selection-function subsection and SDSS denominator table;
- a BPT/S/N robustness subsection, table, and Goru sensitivity figure;
- source/citation guardrails from the Wave-3 literature packet: SDSS DR17, Brinchmann catalog-property context, Kewley et al. optical classification, LaMassa AGN--SFR context, and Stasińska retired/LINER caveat;
- safer abstract/discussion/conclusion language saying the headline $-1.31$ dex is broad-BPT/S/N$\\geq3$/capped-cache only, not causal AGN-feedback proof.

## Key inserted quantitative guardrails

- Public SDSS strict four-line S/N$\\geq3$ eligible rows: **249,917**.
- Cached pilot rows: **60,000** (**24.0%** of strict eligible parent), selected by `TOP 60000 ... ORDER BY specObjID`.
- Four-line retention is sSFR-dependent: **33.56%** for $-12<\\log\\mathrm{{sSFR}}<-11$ versus **94.85%** for $-10<\\log\\mathrm{{sSFR}}<-9.5$.
- Matched median offsets: broad BPT S/N$\\geq3$ **-1.31 dex**, S/N$\\geq5$ **-1.16 dex**, S/N$\\geq10$ **-0.74 dex**, high-excitation S/N$\\geq3$ **-1.14 dex**, Seyfert-like proxy **-0.76 dex**, LINER-like proxy **-1.47 dex**.

## Outputs

- TeX: `{tex_path}`
- PDF: `{pdf_path}`
- Compile log: `{compile_log}`
- Manifest: `{MANIFEST_JSON}`

## Verification

- `tectonic` exit code: **{proc.returncode}**
- PDF magic `%PDF`: **{pdf_magic_ok}**
- PDF bytes: **{manifest['pdf_bytes']}**
- PDF SHA256: `{manifest['pdf_sha256']}`
- Fatal LaTeX markers: **{len(fatal_markers)}** (`{fatal_markers}`)

## Safety

Local lane artifact only. No public/live page changes, DB/API/page_versions/trust, deploy/restart, git, cron, billing/OAuth, or external submission.
"""
    SUMMARY_MD.write_text(summary)
    print(json.dumps(manifest, indent=2, sort_keys=True))

    if proc.returncode != 0 or not pdf_magic_ok or fatal_markers:
        raise SystemExit("Compile/PDF verification failed")


if __name__ == "__main__":
    main()
