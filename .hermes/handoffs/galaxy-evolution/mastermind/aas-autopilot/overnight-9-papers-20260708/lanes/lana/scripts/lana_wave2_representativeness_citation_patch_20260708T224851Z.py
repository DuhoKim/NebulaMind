#!/usr/bin/env python3
"""Lana Wave-2 representativeness/citation manuscript patch.

Writes only under lanes/lana, except the separately required root overnight-ledger
append performed after verification. It does not modify current public-linked run
manuscripts/PDFs, public pages, DB/API/page_versions, deploy, git, billing/OAuth,
external submissions, or cron jobs.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
from pathlib import Path
from textwrap import dedent

TS = "20260708T224851Z"
REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
WORK = AUTOPILOT / "overnight-9-papers-20260708"
LANA = WORK / "lanes/lana"
RUN1 = AUTOPILOT / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
RUN8 = AUTOPILOT / "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
REP = WORK / "lanes/tori/cached-public-representativeness/20260708T220242Z"

ACTIVE = {
    "m1_rp1_sdss_agn_sfr": {
        "tex": RUN1 / "aastex/sdss_agn_sfr_pilot_aas.tex",
        "json": RUN1 / "analysis_results.json",
    },
    "m1_rp2_environment_quenching": {
        "tex": RUN8 / "m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_aas.tex",
        "json": RUN8 / "m1_rp2_environment_quenching/analysis_results.json",
    },
    "m1_rp3_maintenance_heating": {
        "tex": RUN8 / "m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_aas.tex",
        "json": RUN8 / "m1_rp3_maintenance_heating/analysis_results.json",
    },
    "m2_p1_outflow_escape_recycling": {
        "tex": RUN8 / "m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_aas.tex",
        "json": RUN8 / "m2_p1_outflow_escape_recycling/analysis_results.json",
    },
    "m2_p2_radio_jet_environment": {
        "tex": RUN8 / "m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_aas.tex",
        "json": RUN8 / "m2_p2_radio_jet_environment/analysis_results.json",
        "fig_dir": RUN8 / "m2_p2_radio_jet_environment/figures",
    },
    "m2_p3_feedback_transition_mass": {
        "tex": RUN8 / "m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_aas.tex",
        "json": RUN8 / "m2_p3_feedback_transition_mass/analysis_results.json",
    },
    "m3_p1_multiphase_census": {
        "tex": RUN8 / "m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_aas.tex",
        "json": RUN8 / "m3_p1_multiphase_census/analysis_results.json",
    },
    "m3_p2_gas_depletion_efficiency": {
        "tex": RUN8 / "m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_aas.tex",
        "json": RUN8 / "m3_p2_gas_depletion_efficiency/analysis_results.json",
        "fig_dir": RUN8 / "m3_p2_gas_depletion_efficiency/figures",
    },
    "m3_p3_simulation_validation": {
        "tex": RUN8 / "m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_aas.tex",
        "json": RUN8 / "m3_p3_simulation_validation/analysis_results.json",
        "fig_dir": RUN8 / "m3_p3_simulation_validation/figures",
    },
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def starts_with_pdf(path: Path) -> bool:
    try:
        return path.read_bytes()[:5] == b"%PDF-"
    except FileNotFoundError:
        return False


def read_inventory() -> list[dict]:
    """Read current AASTeX sources and analysis_results.json for all 9 papers."""
    rows = []
    for slug, paths in ACTIVE.items():
        tex_text = paths["tex"].read_text(encoding="utf-8", errors="replace")
        json_text = paths["json"].read_text(encoding="utf-8", errors="replace")
        data = json.loads(json_text)
        title_match = re.search(r"\\title\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", tex_text, re.S)
        title = " ".join(title_match.group(1).split()) if title_match else data.get("short_title") or data.get("proposal_title")
        rows.append({
            "slug": slug,
            "tex": str(paths["tex"].relative_to(AUTOPILOT)),
            "tex_bytes": paths["tex"].stat().st_size,
            "tex_sha256": sha256(paths["tex"]),
            "tex_line_count": tex_text.count("\n") + 1,
            "parsed_title": title,
            "analysis_json": str(paths["json"].relative_to(AUTOPILOT)),
            "analysis_bytes": paths["json"].stat().st_size,
            "analysis_sha256": sha256(paths["json"]),
            "analysis_keys": sorted(data.keys()),
            "sample_rows": data.get("sample_rows"),
            "proposal_title": data.get("proposal_title"),
            "short_title": data.get("short_title"),
        })
    return rows


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n <= 0:
        return (float("nan"), float("nan"))
    phat = k / n
    denom = 1 + z * z / n
    centre = phat + z * z / (2 * n)
    half = z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)
    return ((centre - half) / denom, (centre + half) / denom)


def fmt_interval(k: int, n: int) -> str:
    lo, hi = wilson(k, n)
    return f"{k}/{n} ({k/n:.3f}; [{lo:.3f}, {hi:.3f}])"


def compact_rep_table(label: str) -> str:
    return rf'''
\begin{{deluxetable*}}{{llrrrrr}}
\tablecaption{{Cached sample versus public SDSS four-line parent: largest marginal deviations for {label}\label{{tab:{label}-cached-public}}}}
\tablehead{{\colhead{{Dimension}} & \colhead{{Bin}} & \colhead{{Public $N$}} & \colhead{{Cached $N$}} & \colhead{{Public frac.}} & \colhead{{Cached frac.}} & \colhead{{$\Delta$ pp}}}}
\startdata
redshift & 0.080--0.120 & 92,343 & 23,385 & 36.9\% & 39.0\% & +2.0 \\
stellar mass & 8.0--9.5 & 37,970 & 8,139 & 15.2\% & 13.6\% & -1.6 \\
sSFR & $-10.0$--$-9.5$ & 84,488 & 19,934 & 33.8\% & 33.2\% & -0.6 \\
\enddata
\tablecomments{{Public counts are read-only SDSS DR17 SkyServer counts for the same redshift, mass, sSFR, and four-line S/N$\geq3$ constraints.  The full public four-line parent has 249,917 rows; the cached SpecObjID-ordered pilot subset has 60,000 rows, or 24.0\% coverage.  No checked marginal bin exceeds a 5 percentage-point deviation, but the subset is still row-capped and non-random.}}
\end{{deluxetable*}}
'''


M2P2_TEX = rf'''
% LANA_WAVE2_REPRESENTATIVENESS_CITATION_PATCH_{TS}
% Paper: m2_p2_radio_jet_environment
% Lane-local revision draft only; does not overwrite public-linked manuscripts or PDFs.
\documentclass[twocolumn]{{aastex631}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\graphicspath{{{{{(RUN8 / "m2_p2_radio_jet_environment/figures").resolve()}/}}}}
\shorttitle{{Representativeness-flagged optical AGN environments}}
\shortauthors{{NebulaMind Autopilot}}

\begin{{document}}

\title{{A Representativeness-Flagged Optical AGN Environment Denominator for Radio/X-ray Jet-Coupling Follow-up in SDSS DR17}}
\author{{NebulaMind Research Autopilot}}
\affiliation{{Local reproducible pilot run; public SDSS DR17 data and overnight local artifacts only}}

\begin{{abstract}}
This Lana revision patches the Wave-2 M2 P2 draft after external review.  The science product is explicitly an optical denominator: BPT optical-AGN incidence versus an internal nearest-neighbour density ranking among massive SDSS emission-line hosts.  It is not a radio-jet coupling measurement.  The shared public SDSS check finds 249,917 galaxies satisfying the strict four-line S/N$\geq3$ parent selection, while the cached pilot uses a SpecObjID-ordered 60,000-row subset (24.0\% coverage).  A cached-versus-public marginal check finds no redshift, stellar-mass, or sSFR bin above a 5 percentage-point discrepancy, but the subset remains capped and non-random.  For $\log M_\star\geq10.8$ hosts, the high-minus-low BPT optical-AGN fraction is 0.138--0.152 across $k=5$, 10, and 20 internal density rankings.  The safe conclusion is a target-selection one: environment-stratified radio/X-ray follow-up should preserve the optical selection function before discussing jet power, hot gas, or coupling efficiency.
\end{{abstract}}

\keywords{{galaxies: active --- galaxies: evolution --- galaxies: environments --- surveys --- methods: data analysis}}

\section{{Scope and citation boundary}}\label{{sec:m2p2-scope}}
The parent proposal asks whether gaseous environment changes radio-jet coupling efficiency.  This SDSS-only manuscript cannot answer that directly because it contains neither radio jet powers nor X-ray cavity/hot-gas measurements.  The public SDSS DR17 release anchors the observed optical parent \citep{{abdurrouf2022,york2000}}, and BPT diagnostics anchor the optical classification \citep{{baldwin1981,kauffmann2003,kewley2001,kewley2006}}.  Radio-mode and hot-atmosphere studies are used only to define the follow-up data still needed \citep{{best2005,mcnamara2007,santoro2020,eckert2024}}.

The allowed manuscript headline is: in a capped four-line SDSS denominator, massive hosts in the high internal-density quartile have a higher BPT optical-AGN fraction than massive hosts in the low-density quartile.  Forbidden headlines include radio jet coupling efficiency, hot-gas heating balance, cavity power, or causal environmental triggering.

\section{{Data, selection, and representativeness}}\label{{sec:m2p2-data}}
The cached analysis sample requires spectroscopic class \texttt{{GALAXY}}, $0.02<z<0.12$, finite catalog stellar mass and sSFR, and S/N$\geq3$ in H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$.  The public strict four-line parent has 249,917 rows; the cached analysis table has 60,000 rows produced by a \texttt{{TOP 60000 ... ORDER BY specObjID}} query.  For the massive-host cut used here, $\log(M_\star/M_\odot)\geq10.8$, public SDSS has 85,225 mass-selected rows, 35,482 four-line S/N$\geq3$ eligible rows, and 9,298 cached rows.

{compact_rep_table("m2p2")}

All reported optical-AGN fractions are therefore conditional on four-line emission detection and the SpecObjID-ordered cap.  The representativeness check reduces one external-review concern in broad z/mass/sSFR marginals, but it does not make the cached table spatially random, volume complete, edge corrected, or halo selected.

\section{{Density method and known confounds}}\label{{sec:m2p2-methods}}
Density is an internal rank proxy.  The original batch code uses an $H_0=70$ low-redshift distance proxy to convert $(\alpha,\delta,z)$ into approximate Cartesian coordinates and then ranks galaxies by nearest-neighbour distance.  For this patch, the result table keeps the Goru/Tori $k=5$, 10, and 20 neighbour-count checks.  No survey mask, angular edge correction, redshift-space distortion model, fiber-collision correction, halo mass, group catalogue, central/satellite label, or radio morphology enters the density estimate.  Density quartiles are assigned inside the cached 60,000-row emission-line sample and then intersected with $\log M_\star\geq10.8$ hosts; low- and high-density denominators are not required to be equal.

These method limits are especially important because massive hosts vary with redshift and stellar mass across density bins.  The table below should be integrated with a z--mass balance diagnostic before any stronger environment language is used.

\section{{Results}}\label{{sec:m2p2-results}}
\begin{{deluxetable*}}{{lccc}}
\tablecaption{{Massive-host BPT optical-AGN fraction by internal density ranking\label{{tab:m2p2-density}}}}
\tablehead{{\colhead{{Density proxy}} & \colhead{{Low-density massive hosts}} & \colhead{{High-density massive hosts}} & \colhead{{$\Delta f_{{\rm BPT\,AGN}}$ high--low}}}}
\startdata
$k=5$ nearest neighbours & 959/2,604 (0.368) & 1,002/1,980 (0.506) & 0.138 [0.107, 0.166] \\
$k=10$ nearest neighbours & 1,007/2,746 (0.367) & 948/1,864 (0.509) & 0.142 [0.114, 0.171] \\
$k=20$ nearest neighbours & 1,062/2,906 (0.365) & 942/1,819 (0.518) & 0.152 [0.123, 0.181] \\
\enddata
\tablecomments{{Rows are restricted to cached massive hosts with $\log M_\star\geq10.8$.  Fractions are BPT optical-AGN fractions inside the emission-line denominator.  The stability across $k$ is a neighbour-count sensitivity check, not proof of a physical gas-density scale.}}
\end{{deluxetable*}}

\begin{{figure}}
\centering
\includegraphics[width=\columnwidth]{{m2\_p2\_radio\_jet\_environment\_figure1.pdf}}
\caption{{Preserved batch-run SDSS diagnostic.  In this patched draft the figure is an optical/environment denominator visualization only; it does not encode radio morphology, jet power, cavity energetics, or hot-gas coupling.}}
\label{{fig:m2p2-original}}
\end{{figure}}

\section{{Discussion outline}}\label{{sec:m2p2-discussion}}
The useful result is a follow-up design statement.  If a radio/X-ray program wants to test jet coupling across environment, this SDSS table supplies massive optical-AGN candidate counts and a reproducible internal-density stratification.  The physical test still needs cross-matched radio luminosity/morphology, X-ray gas or cavity information, redshift-space and edge corrections, and nondetection accounting.  Best et al.-style massive-host radio demographics \citep{{best2005}} and hot-atmosphere energetics \citep{{mcnamara2007,eckert2024}} should appear in the future-observable paragraph, not as evidence for the optical fraction itself.

\section{{Conclusions}}\label{{sec:m2p2-conclusions}}
\begin{{enumerate}}
\item The draft now contains a cached-versus-public representativeness table: the largest checked marginal differences are +2.0 pp in redshift, -1.6 pp in stellar mass, and -0.6 pp in sSFR.
\item The $k=5$, 10, and 20 density rankings give high-minus-low massive-host BPT optical-AGN contrasts of 0.138--0.152.
\item The result remains an optical target-denominator association and must not be written as a radio-jet coupling-efficiency measurement.
\end{{enumerate}}

\section*{{Reproducibility and safety note}}
Source analysis summary: \texttt{{m2\_p2\_radio\_jet\_environment/analysis\_results.json}} under run SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z.  Draft marker: LANA\_WAVE2\_REPRESENTATIVENESS\_CITATION\_PATCH\_{TS}.  This file is lane-local and did not overwrite public-linked manuscripts or PDFs.

\acknowledgments
This pilot used public SDSS DR17 data products and local open-source tooling.

\begin{{thebibliography}}{{}}
\bibitem[Abdurro'uf et al.(2022)]{{abdurrouf2022}} Abdurro'uf, A., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{{baldwin1981}} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{{best2005}} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Eckert et al.(2024)]{{eckert2024}} Eckert, D., et al. 2024, arXiv:2403.17145
\bibitem[Kauffmann et al.(2003)]{{kauffmann2003}} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{{kewley2001}} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{{kewley2006}} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[McNamara \& Nulsen(2007)]{{mcnamara2007}} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Santoro et al.(2020)]{{santoro2020}} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, arXiv:2009.11175
\bibitem[York et al.(2000)]{{york2000}} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{{thebibliography}}

\end{{document}}
'''


M3P2_TEX = rf'''
% LANA_WAVE2_REPRESENTATIVENESS_CITATION_PATCH_{TS}
% Paper: m3_p2_gas_depletion_efficiency
% Lane-local revision draft only; does not overwrite public-linked manuscripts or PDFs.
\documentclass[twocolumn]{{aastex631}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\graphicspath{{{{{(RUN8 / "m3_p2_gas_depletion_efficiency/figures").resolve()}/}}}}
\shorttitle{{Representativeness-flagged gas-follow-up denominators}}
\shortauthors{{NebulaMind Autopilot}}

\begin{{document}}

\title{{A Representativeness-Flagged Optical Denominator for Molecular-Gas Depletion and Efficiency Follow-up in SDSS DR17}}
\author{{NebulaMind Research Autopilot}}
\affiliation{{Local reproducible pilot run; public SDSS DR17 data and overnight local artifacts only}}

\begin{{abstract}}
This Lana revision patches the M3 P2 gas-depletion/SFE draft by making the selection-convolved denominator and H$\alpha$ proxy explicit.  SDSS DR17 optical spectra do not measure CO, H~I, dust gas mass, molecular gas fraction, depletion time, or star-formation efficiency.  The strict public four-line S/N$\geq3$ parent contains 249,917 rows; the cached pilot uses a SpecObjID-ordered 60,000-row subset (24.0\%).  A z/mass/sSFR marginal check finds no bin above a 5 percentage-point cached-minus-public discrepancy, but the denominator remains four-line-selected and non-random.  In massive low-sSFR selections, cached denominators range from 2,941 to 10,270 galaxies and BPT optical-AGN fractions range from 0.509 to 0.649.  These high fractions are conditional on requiring all four optical lines; weak-line quiescent systems are excluded.  The H$\alpha$ column is an approximate observed-flux luminosity proxy, not a gas mass or SFE measurement.
\end{{abstract}}

\keywords{{galaxies: evolution --- galaxies: star formation --- galaxies: active --- surveys --- methods: data analysis}}

\section{{Scope and citation boundary}}\label{{sec:m3p2-scope}}
The parent proposal asks how to distinguish molecular-gas depletion from suppressed star-formation efficiency.  This SDSS-only pilot can only build an optical follow-up denominator.  DR17 and catalog physical-property work anchor the actual measurements \citep{{abdurrouf2022,york2000,brinchmann2004}}.  COLD GASS, xCOLD GASS, and xGASS are cited only to define the missing CO/H~I measurements and depletion-time quantities required for the full test \citep{{saintonge2011a,saintonge2011b,saintonge2017,catinella2018}}.  No gas-fraction or SFE result is claimed here.

\section{{Selection function and cached-public check}}\label{{sec:m3p2-selection}}
The cached table requires four BPT lines with S/N$\geq3$.  This matters more for M3 P2 than for most other overnight pilots because weak-line quiescent systems are exactly the population that a gas-depletion paper would otherwise need to count.  Earlier public selection checks found strong sSFR-dependent four-line retention: 33.56\% retention in the $-12<\log {{\rm sSFR}}<-11$ bin versus 94.85\% in the $-10<\log {{\rm sSFR}}<-9.5$ bin.  Therefore all rows in Table~\ref{{tab:m3p2-grid}} are emission-line-detected target denominators, not complete massive-quiescent-galaxy fractions.

{compact_rep_table("m3p2")}

\section{{Measured optical quantities}}\label{{sec:m3p2-methods}}
The threshold grid varies $\log M_\star\geq10.6, 10.8, 11.0$ and $\log {{\rm sSFR}}<-10.7$ or $<-11.0$.  For each row we report the public parent count, the public four-line S/N$\geq3$ count, the cached count, the cached BPT optical-AGN fraction, and a median H$\alpha$ luminosity proxy.

The H$\alpha$ proxy is now defined from the batch code rather than left implicit.  The script reads the observed SDSS \texttt{{h\_alpha\_flux}} column in $10^{{-17}}\,{{\rm erg\,s^{{-1}}\,cm^{{-2}}}}$ units, multiplies by $4\pi D_L^2$ using a low-redshift $H_0=70\,{{\rm km\,s^{{-1}}\,Mpc^{{-1}}}}$ luminosity-distance approximation, and stores $\log_{{10}}L_{{\rm H\alpha}}$ in ${{\rm erg\,s^{{-1}}}}$.  The overnight pilot did not apply dust-extinction correction, aperture correction, Balmer-decrement correction, or a gas-mass conversion.  The uncertainties shown for $f_{{\rm BPT\,AGN}}$ are binomial-only; they do not include selection-bootstrap or calibration errors.

\section{{Results}}\label{{sec:m3p2-results}}
\begin{{deluxetable*}}{{lrrrrcc}}
\tabletypesize{{\scriptsize}}
\tablecaption{{Massive low-sSFR emission-line denominators and optical proxy quantities\label{{tab:m3p2-grid}}}}
\tablehead{{\colhead{{$\log M_\star$ cut}} & \colhead{{$\log {{\rm sSFR}}$ cut}} & \colhead{{Public parent $N$}} & \colhead{{Public S/N$\geq3$ $N$}} & \colhead{{Cached $N$}} & \colhead{{Cached/S/N}} & \colhead{{$f_{{\rm BPT\,AGN}}$; median $\log L_{{\rm H\alpha}}$}}}}
\startdata
$\geq10.6$ & $<-10.7$ & 121,533 & 40,797 & 10,270 & 25.2\% & 0.509$\pm$0.005; 40.03 \\
$\geq10.6$ & $<-11.0$ & 111,172 & 33,564 & 8,400 & 25.0\% & 0.574$\pm$0.005; 39.97 \\
$\geq10.8$ & $<-10.7$ & 74,070 & 26,170 & 6,729 & 25.7\% & 0.549$\pm$0.006; 40.06 \\
$\geq10.8$ & $<-11.0$ & 68,649 & 22,324 & 5,695 & 25.5\% & 0.607$\pm$0.006; 40.01 \\
$\geq11.0$ & $<-10.7$ & 35,092 & 12,692 & 3,334 & 26.3\% & 0.600$\pm$0.008; 40.09 \\
$\geq11.0$ & $<-11.0$ & 33,125 & 11,288 & 2,941 & 26.1\% & 0.649$\pm$0.009; 40.05 \\
\enddata
\tablecomments{{Public counts come from read-only SDSS DR17 count checks.  Cached counts and optical AGN fractions come from the preserved 60,000-row sample and Goru/Tori threshold tables.  The BPT-AGN fractions are selection-convolved because weak-line systems are removed before the denominator is formed.}}
\end{{deluxetable*}}

\begin{{figure}}
\centering
\includegraphics[width=\columnwidth]{{m3\_p2\_gas\_depletion\_efficiency\_figure1.pdf}}
\caption{{Preserved batch-run diagnostic for the M3 P2 pilot.  It is now interpreted only as an optical baseline for CO/H~I/dust follow-up target selection; it is not a gas-fraction, depletion-time, or star-formation-efficiency measurement.}}
\label{{fig:m3p2-original}}
\end{{figure}}

\section{{Discussion outline}}\label{{sec:m3p2-discussion}}
The threshold grid is useful because it gives observers a feasible target-list scale for CO or dust follow-up.  It is also a warning: BPT-AGN fractions of 0.509--0.649 should not be read as the prevalence of AGN among all massive quiescent galaxies.  They are conditional fractions among systems with four measurable optical lines, and the public selection-function check shows that this condition removes many low-sSFR galaxies.  Gas-survey citations should therefore appear in the missing-observable paragraph: a real depletion/SFE paper needs molecular or total cold-gas masses, aperture-matched SFRs, nondetections, and matched morphology/environment controls \citep{{saintonge2011a,saintonge2011b,saintonge2017,catinella2018}}.

\section{{Conclusions}}\label{{sec:m3p2-conclusions}}
\begin{{enumerate}}
\item The draft now states that all fractions are conditional on a four-line optical emission denominator and the 60,000-row SpecObjID cap.
\item The cached-versus-public marginal check found no z/mass/sSFR bin above 5 pp, but it does not repair weak-line/quiescent selection loss.
\item The H$\alpha$ proxy is an observed-flux luminosity proxy in ${{\rm erg\,s^{{-1}}}}$ without extinction, aperture, or gas-mass correction.
\item The paper should remain a CO/H~I/dust follow-up denominator, not a molecular-gas depletion or SFE result.
\end{{enumerate}}

\section*{{Reproducibility and safety note}}
Source analysis summary: \texttt{{m3\_p2\_gas\_depletion\_efficiency/analysis\_results.json}} under run SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z.  H$\alpha$ proxy definition read from \texttt{{run\_remaining\_topic\_pilots.py}}.  Draft marker: LANA\_WAVE2\_REPRESENTATIVENESS\_CITATION\_PATCH\_{TS}.  This file is lane-local and did not overwrite public-linked manuscripts or PDFs.

\acknowledgments
This pilot used public SDSS DR17 data products and local open-source tooling.

\begin{{thebibliography}}{{}}
\bibitem[Abdurro'uf et al.(2022)]{{abdurrouf2022}} Abdurro'uf, A., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{{baldwin1981}} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{{brinchmann2004}} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Catinella et al.(2018)]{{catinella2018}} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, arXiv:1802.02373
\bibitem[Kauffmann et al.(2003)]{{kauffmann2003}} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{{kewley2001}} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Saintonge et al.(2011a)]{{saintonge2011a}} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011, arXiv:1103.1642
\bibitem[Saintonge et al.(2011b)]{{saintonge2011b}} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011, arXiv:1104.0019
\bibitem[Saintonge et al.(2017)]{{saintonge2017}} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, arXiv:1710.02157
\bibitem[York et al.(2000)]{{york2000}} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{{thebibliography}}

\end{{document}}
'''


SMALL_A = {
    "n": 300,
    "fq": fmt_interval(2, 300),
    "fagn": fmt_interval(3, 300),
    "fhigh": fmt_interval(0, 300),
}
SMALL_B = {
    "n": 390,
    "fq": fmt_interval(334, 390),
    "fagn": fmt_interval(238, 390),
    "fhigh": fmt_interval(85, 390),
}

M3P3_TEX = rf'''
% LANA_WAVE2_REPRESENTATIVENESS_CITATION_PATCH_{TS}
% Paper: m3_p3_simulation_validation
% Lane-local revision draft only; does not overwrite public-linked manuscripts or PDFs.
\documentclass[twocolumn]{{aastex631}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\graphicspath{{{{{(RUN8 / "m3_p3_simulation_validation/figures").resolve()}/}}}}
\shorttitle{{Representativeness-flagged SDSS target vector}}
\shortauthors{{NebulaMind Autopilot}}

\begin{{document}}

\title{{A Representativeness-Flagged Observed SDSS Target Vector for Future Feedback-Model Forward Modelling}}
\author{{NebulaMind Research Autopilot}}
\affiliation{{Local reproducible pilot run; public SDSS DR17 data and overnight local artifacts only}}

\begin{{abstract}}
This Lana revision patches the M3 P3 target-vector draft after external review.  The artifact is an observed SDSS vector, not a validation of any cosmological feedback model.  The vector is measured in a four-line S/N$\geq3$ optical-emission sample: public SDSS contains 249,917 strict eligible rows, and the cached SpecObjID-ordered pilot uses 60,000 rows (24.0\%).  Cached-versus-public z/mass/sSFR marginals show no bin above a 5 percentage-point deviation, but all fractions remain conditional on emission-line detection and the row cap.  The 15 mass--redshift cells span $f_Q\simeq0.001$--0.856 and $f_{{\rm BPT\,AGN}}\simeq0.001$--0.610 in the cached table.  Two cells have cached $N<500$; this draft now prints Wilson intervals for their quenched, BPT-AGN, and high-excitation fractions.  A future model paper must forward-model the SDSS selection, aperture, and noise before accepting, rejecting, or ranking simulations.
\end{{abstract}}

\keywords{{galaxies: evolution --- galaxies: active --- surveys --- methods: data analysis --- methods: statistical}}

\section{{Scope and citation boundary}}\label{{sec:m3p3-scope}}
DR17 anchors the observed SDSS target vector \citep{{abdurrouf2022,york2000}}, while simulation-suite papers only motivate future mock construction and comparison \citep{{nelson2018,schaye2014,dave2019,nanni2022,donnari2020,dubois2016}}.  No EAGLE, IllustrisTNG, SIMBA, Horizon-AGN, or iMaNGA mock catalogue was generated in this pilot.  Therefore no model is validated, falsified, ranked, or tuned here.

The allowed headline is: the pilot writes a reproducible 15-cell observed SDSS vector that future mocks must reproduce under the same selection.  Forbidden headlines include direct simulation validation, model rejection, or proof of AGN feedback from high-mass cells.

\section{{Selection function and representativeness}}\label{{sec:m3p3-selection}}
The vector is built from the same 60,000-row cached SDSS emission-line table used by the other overnight pilots.  The required four-line S/N$\geq3$ cut means that $f_Q$ is a quenched fraction among emission-line-detected galaxies, not a native all-galaxy simulation quenched fraction.  This distinction must travel with any future mock-comparison request: a simulation should be observed through a comparable line-detection, aperture, redshift, mass, and noise model before Table~\ref{{tab:m3p3-vector}} is used.

{compact_rep_table("m3p3")}

\section{{Small-cell uncertainty check}}\label{{sec:m3p3-small}}
External review flagged small cells because extrema such as $f_Q=0.856$ and $f_{{\rm BPT\,AGN}}=0.610$ could otherwise look overprecise.  Table~\ref{{tab:m3p3-smallcells}} reports Wilson 95\% intervals for the two cached cells with $N<500$.  The intervals are still conditional-binomial intervals; they do not include selection-function uncertainty, catalog-systematic uncertainty, or simulation-forward-modelling error.

\begin{{deluxetable*}}{{llrccc}}
\tablecaption{{Small cached cells requiring visible interval and minimum-N caution\label{{tab:m3p3-smallcells}}}}
\tablehead{{\colhead{{$\log M_\star$ bin}} & \colhead{{$z$ bin}} & \colhead{{Cached $N$}} & \colhead{{$f_Q$ Wilson interval}} & \colhead{{$f_{{\rm BPT\,AGN}}$ Wilson interval}} & \colhead{{$f_{{\rm high\,exc.}}$ Wilson interval}}}}
\startdata
8.0--9.5 & 0.08--0.12 & 300 & {SMALL_A['fq']} & {SMALL_A['fagn']} & {SMALL_A['fhigh']} \\
11.0--12.5 & 0.02--0.05 & 390 & {SMALL_B['fq']} & {SMALL_B['fagn']} & {SMALL_B['fhigh']} \\
\enddata
\tablecomments{{Intervals are Wilson 95\% binomial intervals computed from the cached cell counts.  The first row corresponds to 300 cached of 1,252 public S/N$\geq3$ eligible rows; the second to 390 cached of 1,553 public S/N$\geq3$ eligible rows.}}
\end{{deluxetable*}}

\section{{Observed target vector}}\label{{sec:m3p3-results}}
\begin{{deluxetable*}}{{llccccc}}
\tabletypesize{{\scriptsize}}
\tablecaption{{Observed SDSS mass--redshift target vector with minimum-N flags\label{{tab:m3p3-vector}}}}
\tablehead{{\colhead{{$\log M_\star$ bin}} & \colhead{{$z$ bin}} & \colhead{{$N$}} & \colhead{{$f_Q$}} & \colhead{{$f_{{\rm BPT\,AGN}}$}} & \colhead{{$f_{{\rm high\,exc.}}$}} & \colhead{{Flag}}}}
\startdata
8.0--9.5 & 0.02--0.05 & 6,201 & 0.006 & 0.003 & 0.002 & \nodata \\
8.0--9.5 & 0.05--0.08 & 1,638 & 0.001 & 0.001 & 0.001 & \nodata \\
8.0--9.5 & 0.08--0.12 & 300 & 0.007 & 0.010 & 0.000 & $N<500$ \\
9.5--10.0 & 0.02--0.05 & 3,607 & 0.061 & 0.030 & 0.027 & \nodata \\
9.5--10.0 & 0.05--0.08 & 6,059 & 0.013 & 0.008 & 0.007 & \nodata \\
9.5--10.0 & 0.08--0.12 & 2,187 & 0.003 & 0.001 & 0.001 & \nodata \\
10.0--10.5 & 0.02--0.05 & 2,962 & 0.256 & 0.154 & 0.104 & \nodata \\
10.0--10.5 & 0.05--0.08 & 7,581 & 0.161 & 0.090 & 0.064 & \nodata \\
10.0--10.5 & 0.08--0.12 & 8,593 & 0.062 & 0.040 & 0.029 & \nodata \\
10.5--11.0 & 0.02--0.05 & 1,895 & 0.581 & 0.430 & 0.215 & \nodata \\
10.5--11.0 & 0.05--0.08 & 5,083 & 0.451 & 0.297 & 0.160 & \nodata \\
10.5--11.0 & 0.08--0.12 & 9,861 & 0.326 & 0.209 & 0.119 & \nodata \\
11.0--12.5 & 0.02--0.05 & 390 & 0.856 & 0.610 & 0.218 & $N<500$ \\
11.0--12.5 & 0.05--0.08 & 1,199 & 0.805 & 0.563 & 0.228 & \nodata \\
11.0--12.5 & 0.08--0.12 & 2,444 & 0.672 & 0.485 & 0.198 & \nodata \\
\enddata
\tablecomments{{Observed SDSS quantities only.  The fractions are conditional on four-line emission detection and the cached row cap.  A future validation paper must compare simulations to this vector only after constructing mocks with matching selection, aperture, and noise models.}}
\end{{deluxetable*}}

\begin{{figure}}
\centering
\includegraphics[width=\columnwidth]{{m3\_p3\_simulation\_validation\_figure1.pdf}}
\caption{{Preserved batch-run diagnostic for the M3 P3 pilot.  It should be read as a visualization of the observed SDSS target vector, not as a test passed or failed by any simulation.}}
\label{{fig:m3p3-original}}
\end{{figure}}

\section{{Discussion outline}}\label{{sec:m3p3-discussion}}
The table is useful as an observation target for forward modelling because it is compact and reproducible.  Its physical interpretation is deliberately deferred.  High-mass cells have large low-sSFR and BPT-AGN fractions in this emission-line sample, but those numbers convolve galaxy physics, optical-line detectability, aperture effects, stellar-mass distribution, redshift distribution, and the SpecObjID cap.  A model-comparison manuscript should generate synthetic observations from public simulation suites \citep{{nelson2018,schaye2014,dave2019}} and then apply SDSS-like emission-line cuts, aperture/noise models, and, where relevant, MaNGA/ALMA/X-ray/radio mock selections \citep{{nanni2022,donnari2020}}.

\section{{Conclusions}}\label{{sec:m3p3-conclusions}}
\begin{{enumerate}}
\item The draft now states that $f_Q$ is an emission-line-detected quenched fraction, not an all-galaxy simulation quenched fraction.
\item The cached-versus-public marginal check is visible before the target vector and shows no z/mass/sSFR bin above a 5 pp discrepancy, while preserving the non-random cap caveat.
\item The two cached cells with $N<500$ now show Wilson intervals in the manuscript table.
\item Simulation citations are placed only in the future-forward-modelling paragraph; no model is validated or rejected here.
\end{{enumerate}}

\section*{{Reproducibility and safety note}}
Source analysis summary: \texttt{{m3\_p3\_simulation\_validation/analysis\_results.json}} under run SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z.  Draft marker: LANA\_WAVE2\_REPRESENTATIVENESS\_CITATION\_PATCH\_{TS}.  This file is lane-local and did not overwrite public-linked manuscripts or PDFs.

\acknowledgments
This pilot used public SDSS DR17 data products and local open-source tooling.

\begin{{thebibliography}}{{}}
\bibitem[Abdurro'uf et al.(2022)]{{abdurrouf2022}} Abdurro'uf, A., et al. 2022, ApJS, 259, 35
\bibitem[Dave et al.(2019)]{{dave2019}} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, arXiv:1901.10203
\bibitem[Donnari et al.(2020)]{{donnari2020}} Donnari, M., Pillepich, A., Nelson, D., et al. 2020, arXiv:2008.00004
\bibitem[Dubois et al.(2016)]{{dubois2016}} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, arXiv:1606.03086
\bibitem[Nanni et al.(2022)]{{nanni2022}} Nanni, L., Thomas, D., Trayford, J., et al. 2022, arXiv:2203.11575
\bibitem[Nelson et al.(2018)]{{nelson2018}} Nelson, D., Springel, V., Pillepich, A., et al. 2018, arXiv:1812.05609
\bibitem[Schaye et al.(2014)]{{schaye2014}} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2014, arXiv:1407.7040
\bibitem[York et al.(2000)]{{york2000}} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{{thebibliography}}

\end{{document}}
'''


TEX_MAP = {
    "m2_p2_radio_jet_environment": ("m2_p2_radio_jet_environment_lana_representativeness_citation_patch", M2P2_TEX),
    "m3_p2_gas_depletion_efficiency": ("m3_p2_gas_depletion_efficiency_lana_representativeness_citation_patch", M3P2_TEX),
    "m3_p3_simulation_validation": ("m3_p3_simulation_validation_lana_representativeness_citation_patch", M3P3_TEX),
}

CHANGE_TEXT = {
    "m2_p2_radio_jet_environment": f"""# Lana Wave-2 representativeness/citation patch — M2 P2 — {TS}\n\n## What changed\n- Added a cached-vs-public representativeness table for the largest z/mass/sSFR marginal deviations: +2.0 pp redshift, -1.6 pp stellar mass, -0.6 pp sSFR; preserved the 249,917 public strict parent, 60,000 cached rows, and 24.0% coverage.\n- Rewrote methods to describe the internal nearest-neighbour density proxy, H0=70 low-redshift coordinate approximation, redshift-space/edge limitations, and lack of halo/group/radio/X-ray observables.\n- Integrated Wave-2 citations as method/future-observable anchors only: DR17/BPT support actual optical methods; Best/McNamara/Santoro/Eckert motivate missing radio/X-ray/group data.\n- Preserved the k=5/10/20 optical AGN density table while forbidding radio-jet coupling or causal environment headlines.\n\n## Paper-specific critique\nThe paper is useful as a radio/X-ray target-selection denominator, but the density contrast remains confounded by redshift-space positions, survey boundaries, mass/redshift balance, and optical-line selection.  It should not be merged without a z--mass balance diagnostic next to the density table.\n""",
    "m3_p2_gas_depletion_efficiency": f"""# Lana Wave-2 representativeness/citation patch — M3 P2 — {TS}\n\n## What changed\n- Added the cached-vs-public representativeness table before the threshold grid and explicitly states all fractions are four-line-emission conditional.\n- Added the sSFR-dependent line-retention warning and guarded 0.509--0.649 BPT-AGN fractions as selection-convolved.\n- Defined the H-alpha proxy units from the batch code: observed h_alpha_flux in 1e-17 erg/s/cm^2, low-z H0=70 luminosity approximation, log10 erg/s; no aperture, extinction, Balmer-decrement, or gas-mass correction.\n- Integrated DR17/Brinchmann as actual-method anchors and COLD GASS/xCOLD GASS/xGASS as future gas-data anchors only.\n\n## Paper-specific critique\nThe draft now works as a CO/HI/dust follow-up target-list denominator.  It still cannot support gas fraction, depletion time, or SFE claims until actual gas masses and aperture-matched SFRs are added with nondetection accounting.\n""",
    "m3_p3_simulation_validation": f"""# Lana Wave-2 representativeness/citation patch — M3 P3 — {TS}\n\n## What changed\n- Added cached-vs-public representativeness table and explicit warning that f_Q is an emission-line-detected quenched fraction, not an all-galaxy simulation fraction.\n- Added Wilson 95% intervals for the two cached N<500 cells: 8.0--9.5 / z=0.08--0.12 and 11.0--12.5 / z=0.02--0.05.\n- Kept the 15-cell observed SDSS vector while moving all IllustrisTNG/EAGLE/SIMBA/iMaNGA/Donnari/Horizon citations into future-forward-modelling context only.\n- Strengthened no-validate/no-reject/no-rank wording for simulations until mocks pass through matching selection, aperture, and noise models.\n\n## Paper-specific critique\nThis should be treated as a target-vector appendix or denominator-suite artifact, not an independent model-validation paper.  Its next real science step is synthetic-observation construction, not stronger prose.\n""",
}


def compile_tex(tex_path: Path) -> dict:
    cmd = ["tectonic", "--keep-logs", "--keep-intermediates", tex_path.name]
    proc = subprocess.run(cmd, cwd=tex_path.parent, text=True, capture_output=True, timeout=240)
    compile_log = tex_path.parent / f"compile_{TS}.log"
    compile_log.write_text(
        "$ " + " ".join(cmd) + "\n\n[STDOUT]\n" + proc.stdout + "\n[STDERR]\n" + proc.stderr,
        encoding="utf-8",
    )
    pdf = tex_path.with_suffix(".pdf")
    log_text = compile_log.read_text(encoding="utf-8", errors="replace")
    fatal_markers = [m for m in ["! LaTeX Error", "Emergency stop", "Fatal error"] if m in log_text]
    return {
        "compile_exit_code": proc.returncode,
        "compile_log": str(compile_log.relative_to(WORK)),
        "pdf": str(pdf.relative_to(WORK)) if pdf.exists() else None,
        "pdf_bytes": pdf.stat().st_size if pdf.exists() else None,
        "pdf_sha256": sha256(pdf) if pdf.exists() else None,
        "pdf_starts_with_pdf": starts_with_pdf(pdf) if pdf.exists() else False,
        "fatal_markers": fatal_markers,
    }


def main() -> int:
    (LANA / "scripts").mkdir(parents=True, exist_ok=True)
    (LANA / "ticks").mkdir(parents=True, exist_ok=True)
    inventory = read_inventory()
    rep_summary = json.loads((REP / "cached_public_representativeness_summary_20260708T220242Z.json").read_text(encoding="utf-8"))
    drafts = []
    for slug, (base_name, tex) in TEX_MAP.items():
        out_dir = LANA / "revision-drafts" / slug / "aastex"
        out_dir.mkdir(parents=True, exist_ok=True)
        tex_path = out_dir / f"{base_name}_{TS}.tex"
        tex_path.write_text(dedent(tex).lstrip(), encoding="utf-8")
        changes = out_dir.parent / f"CHANGES_{TS}.md"
        changes.write_text(CHANGE_TEXT[slug], encoding="utf-8")
        result = compile_tex(tex_path)
        drafts.append({
            "paper_slug": slug,
            "source_tex": str(ACTIVE[slug]["tex"].relative_to(AUTOPILOT)),
            "source_json": str(ACTIVE[slug]["json"].relative_to(AUTOPILOT)),
            "draft_tex": str(tex_path.relative_to(WORK)),
            "changes_md": str(changes.relative_to(WORK)),
            **result,
        })
    manifest = {
        "timestamp_utc": TS,
        "lane": "lana",
        "marker": f"LANA_WAVE2_REPRESENTATIVENESS_CITATION_PATCH_{TS}",
        "scope": "Wave-2 blocker patches for M2 P2, M3 P2, and M3 P3: cached-vs-public representativeness, selection-convolved fraction guards, citation placement, M2P2 density-method caveats, M3P2 H-alpha proxy units, and M3P3 small-cell intervals. Public-linked manuscripts/PDFs were not overwritten.",
        "source_read_confirmation": {
            "brief": "OVERNIGHT_BRIEF.md",
            "swarm_board": "SWARM_BOARD.md",
            "all_9_current_aastex_sources_read_by_lane_tick": len(inventory) == 9,
            "all_9_analysis_json_read_by_lane_tick": len(inventory) == 9,
            "source_inventory": inventory,
            "additional_sources": [
                "lanes/hwao/HWAO_DIRECTOR_TICK_20260708T222441Z.md",
                "lanes/external-cli/EXTERNAL_CLI_TICK_20260708T212455Z.md",
                "lanes/tori/cached-public-representativeness/20260708T220242Z/CACHED_PUBLIC_REPRESENTATIVENESS_20260708T220242Z.md",
                "lanes/literature/literature_citation_placement_wave2_20260708T211901Z.md",
                "run_remaining_topic_pilots.py",
            ],
        },
        "representativeness_summary": {
            "marker": rep_summary.get("marker"),
            "public_total": rep_summary.get("public_total"),
            "cached_total": rep_summary.get("cached_total"),
            "global_cached_coverage": rep_summary.get("global_cached_coverage"),
            "flagged_bins": rep_summary.get("flagged_bins"),
            "dimension_summary": rep_summary.get("dimension_summary"),
        },
        "small_cell_wilson_intervals": {
            "8.0-9.5_z0.08-0.12_N300": SMALL_A,
            "11.0-12.5_z0.02-0.05_N390": SMALL_B,
        },
        "drafts": drafts,
        "safety": "Lane-local revision drafts/artifacts only, plus the required one-line OVERNIGHT_LEDGER.md append after verification. No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs.",
    }
    manifest_path = LANA / f"lana_wave2_representativeness_revision_manifest_{TS}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    pdf_lines = []
    for d in drafts:
        pdf_lines.append(f"- `{d['pdf']}` — exit {d['compile_exit_code']}, bytes {d['pdf_bytes']}, SHA256 `{d['pdf_sha256']}`, %PDF={d['pdf_starts_with_pdf']}, fatal markers={d['fatal_markers']}")
    tick = LANA / "ticks" / f"TICK_{TS}.md"
    tick.write_text(dedent(f"""
    # Lana manuscript tick — {TS}

    Marker: `LANA_WAVE2_REPRESENTATIVENESS_CITATION_PATCH_{TS}`

    ## Scope read before writing
    Read and used `OVERNIGHT_BRIEF.md`, `SWARM_BOARD.md`, current AASTeX sources and `analysis_results.json` for all 9 active papers, latest Hwao direction, external Wave-2 critique, Tori cached-vs-public representativeness packet, Wave-2 citation-placement packet, and the original batch script for H-alpha proxy units.

    This tick performed deep manuscript-writing/review work for three Wave-2 blocker papers:
    1. M2 P2 — `m2_p2_radio_jet_environment`
    2. M3 P2 — `m3_p2_gas_depletion_efficiency`
    3. M3 P3 — `m3_p3_simulation_validation`

    ## Lane-local artifacts written
    - Script: `lanes/lana/scripts/lana_wave2_representativeness_citation_patch_{TS}.py`
    - Manifest: `lanes/lana/lana_wave2_representativeness_revision_manifest_{TS}.json`
    - Per-paper revised AASTeX drafts and `CHANGES_{TS}.md` files under `lanes/lana/revision-drafts/<paper-slug>/`

    ## Manuscript improvements made
    - M2 P2: added cached-vs-public representativeness table, density-method caveats, Wave-2 citations, and no-radio-coupling headline contract.
    - M3 P2: added selection-convolved fraction warning, H-alpha proxy units/correction status, cached-vs-public table, and gas-survey citations as future-data anchors only.
    - M3 P3: added emission-line-conditional f_Q warning, cached-vs-public table, Wilson intervals for both N<500 cells, and future-only simulation citation placement.

    ## Verification
    {chr(10).join(pdf_lines)}

    ## Safety
    No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs were touched. Current linked manuscripts/PDFs were not overwritten. Only lane-local Lana artifacts were written, plus the required one-line overnight ledger append after verification. No active execution phrase.
    """).strip() + "\n", encoding="utf-8")

    bad = [d for d in drafts if d["compile_exit_code"] != 0 or not d["pdf_starts_with_pdf"] or d["fatal_markers"]]
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
