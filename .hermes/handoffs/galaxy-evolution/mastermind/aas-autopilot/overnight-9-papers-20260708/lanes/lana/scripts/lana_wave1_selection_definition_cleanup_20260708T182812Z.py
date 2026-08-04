#!/usr/bin/env python3
"""Lana lane Wave-1 selection/definition cleanup drafts.

Writes only under lanes/lana, except the separate overnight ledger append that is
performed outside this script after verification. It does not modify active run
manuscripts, public-linked PDFs, live pages, DB, git, or cron jobs.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from textwrap import dedent

TS = "20260708T182812Z"
REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTOPILOT = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
WORK = AUTOPILOT / "overnight-9-papers-20260708"
LANA = WORK / "lanes/lana"
RUN8 = AUTOPILOT / "runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"
RUN1 = AUTOPILOT / "runs/SDSS_AGN_SFR_PILOT_20260708T122000Z"
GORU_FIGS = WORK / "lanes/goru/figures"

PAPERS = {
    "m1_rp2_environment_quenching": {
        "tex_name": f"m1_rp2_environment_quenching_lana_selection_definitions_revision_{TS}.tex",
        "run_tex": RUN8 / "m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_aas.tex",
        "analysis_json": RUN8 / "m1_rp2_environment_quenching/analysis_results.json",
        "fig_dir": RUN8 / "m1_rp2_environment_quenching/figures",
    },
    "m1_rp3_maintenance_heating": {
        "tex_name": f"m1_rp3_maintenance_heating_lana_selection_definitions_revision_{TS}.tex",
        "run_tex": RUN8 / "m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_aas.tex",
        "analysis_json": RUN8 / "m1_rp3_maintenance_heating/analysis_results.json",
        "fig_dir": RUN8 / "m1_rp3_maintenance_heating/figures",
    },
    "m2_p1_outflow_escape_recycling": {
        "tex_name": f"m2_p1_outflow_escape_recycling_lana_selection_definitions_revision_{TS}.tex",
        "run_tex": RUN8 / "m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_aas.tex",
        "analysis_json": RUN8 / "m2_p1_outflow_escape_recycling/analysis_results.json",
        "fig_dir": RUN8 / "m2_p1_outflow_escape_recycling/figures",
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


RP2_TEX = r'''
% LANA_SELECTION_DEFINITION_CLEANUP_20260708T182812Z
% Paper: M1 RP-2 / m1_rp2_environment_quenching
% Lane-local revision draft only; does not overwrite the current linked manuscript or PDF.
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\graphicspath{{__RP2FIG__/}}

\shorttitle{Selection-Flagged Density-Proxy Quenching}
\shortauthors{NebulaMind Autopilot}

\begin{document}

\title{A Selection-Flagged Nearest-Neighbour Density Proxy for Quenching in an SDSS DR17 Emission-Line Pilot Sample}

\author{NebulaMind Research Autopilot}
\affiliation{Local reproducible pilot run; public SDSS DR17 data only}

\begin{abstract}
We revise the M1 RP-2 pilot into a bounded, selection-flagged SDSS density-proxy paper.  The active measurement is not a halo-environment or central/satellite test; it asks whether an internally computed 10th-nearest-neighbour density ranking is associated with the quenched fraction inside a capped SDSS DR17 four-line emission sample.  Public SDSS count checks show 249,917 galaxies satisfying the strict four-BPT-line S/N$\geq3$ selection, while the cached pilot contains the first 60,000 rows returned by the preserved \texttt{TOP 60000 ... ORDER BY specObjID} query, i.e. 24.0\% of that strict parent.  Quenching is now explicitly defined as catalog $\log({\rm sSFR}/{\rm yr}^{-1})< -11.0$.  Within the cached denominator, the high-density quartile contains 3,456 quenched galaxies out of 15,000 ($f_Q=0.230$), while the low-density quartile contains 2,710 out of 15,000 ($f_Q=0.181$).  The high-minus-low difference is 0.049 with bootstrap 95\% interval [0.041, 0.059], and a linear-probability diagnostic adjusted for stellar mass and redshift gives $0.032\pm0.004$.  The result is a reproducible local-density association, not causal proof of environmental quenching.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: environments --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Purpose and Scope}\label{sec:scope}
Mass and environment are long-standing organizing axes for galaxy quenching \citep{peng2010,baldry2006}.  This pilot deliberately tests only the part that the preserved SDSS data can support: a within-sample density ranking versus a catalog-sSFR quenching flag.  It does not include group catalogues, halo masses, satellite infall histories, morphology, or forward-modeled survey boundaries, all of which are needed before interpreting the association as environmental quenching in the stronger sense \citep{wetzel2013,goubert2024}.

\section{Data, Selection Function, and Operational Definitions}\label{sec:data}
The underlying measurements come from public SDSS DR17 spectroscopy and value-added catalog quantities \citep{abdurrouf2022,york2000,brinchmann2004}.  The local run uses galaxies with spectroscopic class \texttt{GALAXY}, $0.02<z<0.12$, finite catalog stellar mass and sSFR, and positive H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ fluxes with S/N$\geq3$ in all four lines.  BPT line-ratio classes are recomputed with the standard Kauffmann and Kewley demarcations \citep{baldwin1981,kauffmann2003,kewley2001}, but the density result below depends on the quenching flag rather than the optical-AGN class.

Table~\ref{tab:rp2_selection} is mandatory context for any incidence wording.  The cached 60,000-row table is a capped, ordered subset of the strict four-line SDSS parent, not a random or complete local-galaxy sample.  Four-line retention is also sSFR-dependent: the public SDSS count check retains 32,021 of 95,424 galaxies (33.56\%) in the $-12<\log{\rm sSFR}<-11$ bin, but 84,488 of 89,075 (94.85\%) in the $-10<\log{\rm sSFR}<-9.5$ bin.  That differential retention is especially relevant for a quenching paper.

\begin{deluxetable*}{lrrl}
\tablecaption{Selection-function disclosure for the shared SDSS four-line denominator\label{tab:rp2_selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public SDSS DR17 count} & \colhead{Cached count used here} & \colhead{Manuscript implication}}
\startdata
Spectroscopic \texttt{GALAXY}, $0.02<z<0.12$ & 501,060 & --- & Redshift-window parent only \\
Joined catalog with mass/sSFR bounds & 416,554 & --- & Value-added-property parent \\
Positive four BPT fluxes and errors & 373,445 & 60,000 & Four-line emission denominator begins to exclude weak-line systems \\
Four BPT lines with S/N$\geq3$ & 249,917 & 60,000 & Cached sample covers 24.0\% of strict parent \\
Four BPT lines with S/N$\geq5$ & 176,523 & 42,446 & Robustness subset, not the headline denominator \\
Four BPT lines with S/N$\geq10$ & 91,768 & 22,311 & High-S/N subset changes population mix \\
\enddata
\tablecomments{Counts are inherited from the read-only Tori/Goru selection-function packets.  The cached query used \texttt{TOP 60000 ... ORDER BY specObjID}; therefore all fractions in this draft are conditional on the cached denominator.}
\end{deluxetable*}

The quenching flag is now explicit: a galaxy is counted as quenched when \texttt{specsfr\_tot\_p50}$<-11.0$.  The density observable is likewise explicit: approximate low-redshift comoving Cartesian positions are built from $(\alpha,\delta,z)$, the distance to the 10th nearest neighbour is measured, and the local-density proxy is proportional to $10/(4\pi d_{10}^{3}/3)$.  Quartiles are computed inside the cached sample.  Because survey masks, edge corrections, fiber-collision corrections, volume completeness, and group membership are not modeled, this is a rank-order density proxy only.

\section{Results}\label{sec:results}
The high-density quartile has a larger quenched fraction than the low-density quartile in the cached pilot measurement.  Table~\ref{tab:rp2_summary} replaces the earlier itemized result with explicit denominators, threshold language, and the interval convention.

\begin{deluxetable*}{lccc}
\tablecaption{Density-proxy quenching summary for the cached SDSS DR17 pilot\label{tab:rp2_summary}}
\tablehead{\colhead{Quantity} & \colhead{Low-density quartile} & \colhead{High-density quartile} & \colhead{Contrast or model term}}
\startdata
Galaxies in quartile & 15,000 & 15,000 & --- \\
Quenched definition & \multicolumn{3}{c}{\texttt{specsfr\_tot\_p50}$<-11.0$} \\
Quenched count & 2,710 & 3,456 & --- \\
Quenched fraction & 0.181 $\pm$ 0.003 & 0.230 $\pm$ 0.003 & $\Delta f_Q=0.049$ \\
Bootstrap interval for $\Delta f_Q$ & --- & --- & [0.041, 0.059] \\
Mass--redshift adjusted LPM coefficient & --- & --- & $0.032\pm0.004$ \\
Approximate 95\% interval for LPM coefficient & --- & --- & [0.025, 0.040] \\
\enddata
\tablecomments{Fractions and bootstrap intervals are copied from the preserved topic-specific JSON.  The linear-probability-model coefficient is a diagnostic adjusted for stellar mass and redshift; it is not a causal environmental-quenching estimate.}
\end{deluxetable*}

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{m1\_rp2\_environment\_quenching\_figure1.pdf}
\caption{Preserved topic-specific SDSS DR17 density-proxy diagnostic.  The plotted comparison should be interpreted as a cached-sample nearest-neighbour rank test with the quenching threshold in Table~\ref{tab:rp2_summary}, not as a calibrated halo-environment measurement.}
\label{fig:rp2_density}
\end{figure}

\section{Discussion and Integration Notes}\label{sec:discussion}
The result supports a cautious statement: within this cached emission-line denominator, the high-density quartile is more often low-sSFR than the low-density quartile.  It does not isolate the physical mechanism.  Morphology--density correlations, stellar age, halo mass, satellite status, aperture scale, and the sSFR-dependent line-selection function can all contribute.  The appropriate next integration step is to keep Peng/Baldry-style mass--environment context near the motivation, then reserve group-catalogue and simulation-comparison citations for the missing-data paragraph rather than for the measured result itself.

\section{Conclusions}\label{sec:conclusions}
\begin{enumerate}
\item The revised M1 RP-2 draft now names the key operational thresholds: four BPT lines with S/N$\geq3$, a cached \texttt{TOP 60000} denominator, \texttt{specsfr\_tot\_p50}$<-11.0$ for quenching, and a 10th-nearest-neighbour density rank.
\item The measured high-minus-low density-quartile quenched-fraction difference is 0.049 with bootstrap 95\% interval [0.041, 0.059].
\item Selection disclosure is central: the cached sample covers 24.0\% of the strict public S/N$\geq3$ parent and four-line retention is strongly sSFR-dependent.
\item The paper should remain an SDSS density-proxy association baseline, not a causal proof of environmental quenching.
\end{enumerate}

\section*{Reproducibility and Safety Note}
Source analysis summary: \texttt{m1\_rp2\_environment\_quenching/analysis\_results.json} under run SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z.  This Lana revision is lane-local and did not overwrite the public-linked manuscript or PDF.

\acknowledgments
This pilot used public SDSS DR17 data products and open-source Python tools.

\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{abdurrouf2022} Abdurro'uf, A., et al. 2022, ApJS, 259, 35
\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., et al. 2006, MNRAS, 373, 469
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., et al. 2024, arXiv:2401.12953
\bibitem[Kauffmann et al.(2003)]{kauffmann2003} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kova\v{c}, K., et al. 2010, ApJ, 721, 193
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}
'''

RP3_TEX = r'''
% LANA_SELECTION_DEFINITION_CLEANUP_20260708T182812Z
% Paper: M1 RP-3 / m1_rp3_maintenance_heating
% Lane-local revision draft only; does not overwrite the current linked manuscript or PDF.
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\graphicspath{{__RP3FIG__/}}

\shorttitle{Optical AGN Denominators for Maintenance Follow-up}
\shortauthors{NebulaMind Autopilot}

\begin{document}

\title{An Optical BPT-AGN Denominator for X-ray and Radio Maintenance-Heating Follow-up in Massive SDSS DR17 Hosts}

\author{NebulaMind Research Autopilot}
\affiliation{Local reproducible pilot run; public SDSS DR17 data only}

\begin{abstract}
We revise the M1 RP-3 manuscript so that it measures only what the SDSS DR17 pilot actually contains: optical BPT-AGN fractions in massive emission-line hosts.  The full maintenance-heating problem requires radio jet powers, X-ray cavity or shock energetics, cooling luminosities, halo-selected parent catalogues, and nondetection modeling; none of those quantities is measured here.  The shared four-line SDSS selection has 249,917 strict public S/N$\geq3$ parent rows, while the cached pilot uses 60,000 ordered rows (24.0\% coverage).  For massive hosts, public count checks find 85,225 galaxies with $\log M_\star\geq10.8$, 35,482 that also satisfy the four-line S/N$\geq3$ selection, and 9,298 in the cached sample.  The exact cached definitions are now explicit: massive means \texttt{lgm\_tot\_p50}$\geq10.8$, and low-sSFR means \texttt{specsfr\_tot\_p50}$<-11.0$.  In the cached sample, 3,997 of 9,298 massive emission-line hosts are BPT AGN ($f=0.430$), and 3,459 of 5,695 massive low-sSFR emission-line hosts are BPT AGN ($f=0.607$).  These are target-denominator fractions for X-ray/radio follow-up, not evidence that maintenance heating balances cooling.
\end{abstract}

\keywords{galaxies: active --- galaxies: evolution --- galaxies: halos --- surveys --- methods: data analysis}

\section{Purpose and Scope}\label{sec:scope}
Maintenance heating is a calorimetric and time-domain question: mechanical energy injection must be compared with halo-gas cooling and with the duty cycle of jet activity \citep{mcnamara2007,mcnamara2012}.  The present SDSS run does not have those data.  Its defensible product is a follow-up denominator: how many massive, emission-line-selected SDSS galaxies would be optical BPT-AGN candidates for later radio and X-ray work?  Radio-loud AGN demographics in massive hosts provide useful context \citep{best2005,heckmanbest2014}, but they do not convert the optical fraction below into jet power or heating efficiency.

\section{Data, Selection Function, and Definitions}\label{sec:data}
The source is the same public SDSS DR17-derived emission-line table used across the overnight pilot set \citep{abdurrouf2022,york2000}.  The four BPT lines are required to have S/N$\geq3$, and BPT classes are computed from the [N~II]/H$\alpha$ and [O~III]/H$\beta$ line ratios \citep{baldwin1981,kauffmann2003,kewley2001}.  Table~\ref{tab:rp3_selection} makes the shared selection-function caveat explicit.

\begin{deluxetable*}{lrrl}
\tablecaption{Selection-function disclosure for the shared SDSS four-line denominator\label{tab:rp3_selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public SDSS DR17 count} & \colhead{Cached count used here} & \colhead{Manuscript implication}}
\startdata
Spectroscopic \texttt{GALAXY}, $0.02<z<0.12$ & 501,060 & --- & Redshift-window parent only \\
Joined catalog with mass/sSFR bounds & 416,554 & --- & Value-added-property parent \\
Positive four BPT fluxes and errors & 373,445 & 60,000 & Weak-line systems already underrepresented \\
Four BPT lines with S/N$\geq3$ & 249,917 & 60,000 & Cached sample covers 24.0\% of strict parent \\
Four BPT lines with S/N$\geq5$ & 176,523 & 42,446 & Higher-S/N robustness subset \\
Four BPT lines with S/N$\geq10$ & 91,768 & 22,311 & High-S/N subset with different mix \\
\enddata
\tablecomments{The cached query used \texttt{TOP 60000 ... ORDER BY specObjID}; fractions below are conditional on the cached emission-line denominator.  Four-line retention is sSFR-dependent, so low-sSFR incidence claims need this caveat.}
\end{deluxetable*}

The operational cuts for this paper are now portable: massive means \texttt{lgm\_tot\_p50}$\geq10.8$, and low-sSFR means \texttt{specsfr\_tot\_p50}$<-11.0$.  A public/cached massive-host attrition check gives Table~\ref{tab:rp3_massive_attrition}.  The cached massive sample is not a complete halo-selected quiescent population; it is the subset of massive systems that survive the four-line optical-emission selection and the 60,000-row cap.

\begin{deluxetable}{lrrr}
\tablecaption{Massive-host attrition for the optical denominator\label{tab:rp3_massive_attrition}}
\tablehead{\colhead{Mass cut} & \colhead{Public parent} & \colhead{Public S/N$\geq3$} & \colhead{Cached}}
\startdata
$\log M_\star\geq10.6$ & 150,490 & 64,654 & 16,640 \\
$\log M_\star\geq10.8$ & 85,225 & 35,482 & 9,298 \\
$\log M_\star\geq11.0$ & 37,980 & 15,112 & 4,033 \\
\enddata
\tablecomments{The adopted row is $\log M_\star\geq10.8$.  For that row the public four-line S/N$\geq3$ retention is 41.6\% of the mass-selected parent, and the cached sample covers 26.2\% of the public S/N$\geq3$ subset.}
\end{deluxetable}

\section{Results}\label{sec:results}
Table~\ref{tab:rp3_fractions} gives the manuscript-ready result.  The intervals are normal approximations using the recorded binomial standard errors, suitable for target-planning language but not for a full selection-function error budget.

\begin{deluxetable*}{lrrrr}
\tablecaption{Optical BPT-AGN fractions for maintenance-heating follow-up denominators\label{tab:rp3_fractions}}
\tablehead{\colhead{Population} & \colhead{$N$} & \colhead{BPT AGN} & \colhead{AGN fraction} & \colhead{Approx. 95\% interval}}
\startdata
Massive emission-line hosts, \texttt{lgm\_tot\_p50}$\geq10.8$ & 9,298 & 3,997 & 0.430 & [0.420, 0.440] \\
Massive low-sSFR emission-line hosts, \texttt{specsfr\_tot\_p50}$<-11.0$ & 5,695 & 3,459 & 0.607 & [0.595, 0.620] \\
\enddata
\tablecomments{Counts and fractions are copied from the preserved topic-specific JSON.  These are optical BPT fractions inside an emission-line-selected denominator, not radio-mode duty-cycle measurements.}
\end{deluxetable*}

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{m1\_rp3\_maintenance\_heating\_figure1.pdf}
\caption{Preserved SDSS DR17 massive-host optical-AGN denominator diagnostic.  The plotted quantity helps plan radio/X-ray follow-up, but it does not measure jet power, cavity enthalpy, cooling luminosity, halo gas thermodynamics, or duty-cycle time averaging.}
\label{fig:rp3_denominator}
\end{figure}

\section{Discussion and Integration Notes}\label{sec:discussion}
The correct discussion order is denominator first, physics second.  First define the cached optical parent and its attrition.  Then use the high BPT-AGN fraction among massive low-sSFR emission-line hosts to motivate cross-matching against radio and X-ray catalogues.  Only a later halo-selected analysis with nondetection accounting can compare mechanical power to cooling requirements \citep{mcnamara2007,mcnamara2012,eckert2024}.  The current optical denominator must not be described as a heating/cooling balance, as a radio-jet coupling efficiency, or as a time-averaged mechanical duty cycle.

\section{Conclusions}\label{sec:conclusions}
\begin{enumerate}
\item The revised M1 RP-3 manuscript is now titled and framed as an optical BPT-AGN denominator for X-ray/radio follow-up, not as a maintenance-heating measurement.
\item Exact definitions are inserted: \texttt{lgm\_tot\_p50}$\geq10.8$ for massive and \texttt{specsfr\_tot\_p50}$<-11.0$ for low-sSFR.
\item In the cached sample, the massive optical BPT-AGN fraction is 0.430, rising to 0.607 among massive low-sSFR emission-line hosts.
\item The full maintenance-heating test still requires halo selection, X-ray cooling measurements, radio/cavity power, nondetections, and duty-cycle modeling.
\end{enumerate}

\section*{Reproducibility and Safety Note}
Source analysis summary: \texttt{m1\_rp3\_maintenance\_heating/analysis\_results.json} under run SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z.  This Lana revision is lane-local and did not overwrite the public-linked manuscript or PDF.

\acknowledgments
This pilot used public SDSS DR17 data products and open-source Python tools.

\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{abdurrouf2022} Abdurro'uf, A., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., et al. 2024, arXiv:2403.17145
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[Kauffmann et al.(2003)]{kauffmann2003} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New Journal of Physics, 14, 055023
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}
'''

M2P1_TEX = r'''
% LANA_SELECTION_DEFINITION_CLEANUP_20260708T182812Z
% Paper: M2 P1 / m2_p1_outflow_escape_recycling
% Lane-local revision draft only; does not overwrite the current linked manuscript or PDF.
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\graphicspath{{__M2P1FIG__/}{__GORUFIG__/}}

\shorttitle{High-Excitation Optical AGN Denominator}
\shortauthors{NebulaMind Autopilot}

\begin{document}

\title{A High-Excitation Optical-AGN Target Denominator for Resolved Escape-versus-Recycling Follow-up in SDSS DR17}

\author{NebulaMind Research Autopilot}
\affiliation{Local reproducible pilot run; public SDSS DR17 data only}

\begin{abstract}
We revise the M2 P1 pilot into a target-denominator paper for future outflow-fate work.  The SDSS run contains optical line ratios and catalog galaxy properties, not outflow velocities, halo escape speeds, multiphase gas masses, CGM tracers, mass loading, or recycling times.  The exact candidate definition is now inserted from the preserved analysis code: high-excitation optical AGN are recomputed BPT AGN with $\log([\mathrm{O\,III}]/\mathrm{H}\beta)>0.25$.  In the cached 60,000-galaxy four-line S/N$\geq3$ sample, this selects 4,440 galaxies, a fraction of 0.074.  Their median catalog $\log({\rm sSFR}/{\rm yr}^{-1})$ is -11.53, compared with -10.14 for the full denominator; this median difference is descriptive target characterization, not feedback evidence.  The shared selection-function warning remains central: public SDSS count checks find 249,917 strict four-line S/N$\geq3$ rows, so the cached query covers 24.0\% of that parent and is not a complete or random incidence denominator.  The pilot identifies a feasible optical parent sample for resolved follow-up, but it does not distinguish escaping from recycling gas.
\end{abstract}

\keywords{galaxies: active --- galaxies: evolution --- galaxies: outflows --- surveys --- methods: data analysis}

\section{Purpose and Scope}\label{sec:scope}
A true escape-versus-recycling test requires velocities, radii, gas-phase masses, halo potentials, geometry, and CGM or reaccretion tracers \citep{veilleux2005,cicone2014,fiore2017}.  This SDSS-only pilot supplies none of those quantities.  Its role is to define an optical target denominator and to state which follow-up measurements are required before any outflow-fate or feedback-efficiency claim can be made.  Literature on multiphase winds and AGN feedback should therefore be used as missing-data motivation, not as support for the measured optical fraction \citep{fabian2012,carniani2017}.

\section{Data, Selection Function, and Candidate Definition}\label{sec:data}
The parent table is the shared public SDSS DR17-derived emission-line sample \citep{abdurrouf2022,york2000}.  BPT classes are recomputed from the [N~II]/H$\alpha$ and [O~III]/H$\beta$ diagnostics \citep{baldwin1981,kauffmann2003,kewley2001}.  Optical classification caveats, including the Seyfert/LINER/composite structure of diagnostic diagrams, should remain explicit \citep{kewley2006}.

\begin{deluxetable*}{lrrl}
\tablecaption{Selection-function disclosure for the shared SDSS four-line denominator\label{tab:m2p1_selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public SDSS DR17 count} & \colhead{Cached count used here} & \colhead{Manuscript implication}}
\startdata
Spectroscopic \texttt{GALAXY}, $0.02<z<0.12$ & 501,060 & --- & Redshift-window parent only \\
Joined catalog with mass/sSFR bounds & 416,554 & --- & Value-added-property parent \\
Positive four BPT fluxes and errors & 373,445 & 60,000 & Optical-line denominator, not a full galaxy census \\
Four BPT lines with S/N$\geq3$ & 249,917 & 60,000 & Cached sample covers 24.0\% of strict parent \\
Four BPT lines with S/N$\geq5$ & 176,523 & 42,446 & Higher-S/N robustness subset \\
Four BPT lines with S/N$\geq10$ & 91,768 & 22,311 & High-S/N subset changes candidate mix \\
\enddata
\tablecomments{The cached query used \texttt{TOP 60000 ... ORDER BY specObjID}.  Four-line S/N selection and the 60,000-row cap mean that target fractions are conditional planning fractions, not complete prevalence estimates.}
\end{deluxetable*}

The adopted high-excitation definition is now fully specified: an object must be a recomputed BPT AGN and satisfy $\log([\mathrm{O\,III}]\lambda5007/\mathrm{H}\beta)>0.25$.  This is an optical excitation proxy, not a velocity, mass-loading, or escape criterion.  Alternative optical thresholds in Table~\ref{tab:m2p1_definitions} show why the wording must remain definition-dependent.

\section{Results}\label{sec:results}
\begin{deluxetable*}{lrrrl}
\tablecaption{Optical candidate-definition sensitivity in the cached S/N$\geq3$ sample\label{tab:m2p1_definitions}}
\tablehead{\colhead{Definition} & \colhead{Denominator} & \colhead{Candidates} & \colhead{Fraction} & \colhead{Use in this manuscript}}
\startdata
All BPT AGN & 60,000 & 8,146 & 0.136 & Broad optical-AGN comparison \\
BPT AGN with $\log([\mathrm{O\,III}]/\mathrm{H}\beta)>0.00$ & 60,000 & 7,730 & 0.129 & Looser excitation check \\
BPT AGN with $\log([\mathrm{O\,III}]/\mathrm{H}\beta)>0.25$ & 60,000 & 4,440 & 0.074 & Adopted high-excitation target denominator \\
BPT AGN with $\log([\mathrm{O\,III}]/\mathrm{H}\beta)>0.50$ & 60,000 & 1,586 & 0.026 & Stricter excitation check \\
NII Seyfert-like proxy within AGN branch & 60,000 & 2,114 & 0.035 & Classification-sensitivity check \\
\enddata
\tablecomments{All rows are optical line-ratio definitions from the Goru mechanical packet.  None measures outflow velocity, gas phase, escape speed, or recycling.}
\end{deluxetable*}

The adopted high-excitation sample has median catalog $\log {\rm sSFR}=-11.53$, compared with -10.14 for the full 60,000-row denominator.  That -1.39 dex median difference is a descriptive target-property contrast without a bootstrap interval in the topic JSON; it should not be converted into a feedback claim.  A matched-control sensitivity table from Goru provides a more useful robustness framing (Table~\ref{tab:m2p1_sn}).

\begin{deluxetable*}{lrrrr}
\tablecaption{High-excitation target denominator and matched-control sensitivity by line-S/N cut\label{tab:m2p1_sn}}
\tablehead{\colhead{Cached cut} & \colhead{Cached denominator} & \colhead{High-excitation targets} & \colhead{Target fraction} & \colhead{Matched $\Delta\log{\rm sSFR}$}}
\startdata
Four-line S/N$\geq3$ & 60,000 & 4,440 & 0.074 & -1.136 [ -1.177, -1.103 ] \\
Four-line S/N$\geq5$ & 42,446 & 2,491 & 0.0587 & -0.930 [ -0.974, -0.891 ] \\
Four-line S/N$\geq10$ & 22,311 & 1,285 & 0.0576 & -0.712 [ -0.741, -0.673 ] \\
\enddata
\tablecomments{Matched offsets compare the adopted high-excitation optical target class to star-forming controls matched in stellar mass and redshift.  They remain optical association diagnostics, not escape/recycling measurements.}
\end{deluxetable*}

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{m2\_p1\_outflow\_escape\_recycling\_figure1.pdf}
\caption{Preserved SDSS DR17 BPT diagnostic for the high-excitation optical-AGN target denominator.  The adopted threshold is $\log([\mathrm{O\,III}]/\mathrm{H}\beta)>0.25$ within the recomputed BPT AGN region.}
\label{fig:m2p1_denominator}
\end{figure}

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{matched_offset_sensitivity_20260708T162615Z.pdf}
\caption{Goru matched-offset sensitivity figure for optical AGN definitions and line-S/N cuts.  This figure supports robustness and scope-guard language only; SDSS optical line ratios do not measure gas escape, recycling, multiphase outflow rates, or CGM reaccretion.}
\label{fig:m2p1_sensitivity}
\end{figure}

\section{Discussion and Integration Notes}\label{sec:discussion}
The integrated manuscript should explicitly separate measured quantities from missing physics.  Measured here: an optical high-excitation target count, a target fraction, and catalog sSFR contrasts inside a capped SDSS denominator.  Needed for escape: resolved kinematics, geometry, phase-dependent outflow masses, and a halo potential or escape-speed estimate.  Needed for recycling: CGM gas tracers, time-scale modeling, and nondetections in a common parent sample.  This structure allows outflow literature to motivate follow-up without implying that a single-fiber optical denominator has measured the fate of expelled gas.

\section{Conclusions}\label{sec:conclusions}
\begin{enumerate}
\item The revised M2 P1 draft now inserts the exact high-excitation criterion: recomputed BPT AGN with $\log([\mathrm{O\,III}]/\mathrm{H}\beta)>0.25$.
\item The adopted target pool contains 4,440 of 60,000 cached S/N$\geq3$ emission-line galaxies, or 7.4\% of the cached denominator.
\item The target fraction and matched sSFR offsets change under stricter S/N cuts, reinforcing that the paper is a selection-flagged target baseline.
\item No outflow velocity, escape velocity, molecular/neutral/ionized mass budget, CGM tracer, or recycling timescale is measured in this SDSS-only pilot.
\end{enumerate}

\section*{Reproducibility and Safety Note}
Source analysis summary: \texttt{m2\_p1\_outflow\_escape\_recycling/analysis\_results.json} under run SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z.  This Lana revision is lane-local and did not overwrite the public-linked manuscript or PDF.

\acknowledgments
This pilot used public SDSS DR17 data products and open-source Python tools.

\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{abdurrouf2022} Abdurro'uf, A., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., et al. 2017, arXiv:1706.08987
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Kauffmann et al.(2003)]{kauffmann2003} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}
'''

CHANGE_TEXT = {
    "m1_rp2_environment_quenching": """# Lana Wave-1 cleanup changes — M1 RP-2 — 20260708T182812Z\n\n- Added universal selection-function disclosure: 249,917 strict public SDSS four-line S/N>=3 rows, 60,000 cached `TOP 60000` rows, 24.0% coverage, and sSFR-dependent line retention.\n- Inserted exact quenched definition from preserved code: `specsfr_tot_p50 < -11.0`.\n- Made the 10th-nearest-neighbour density calculation portable and explicitly non-causal/non-halo-calibrated.\n- Added Peng/Baldry context and Wetzel/Goubert future-data guards without treating them as proof of environmental quenching.\n- Replaced placeholder threshold/caption notes with manuscript-ready tables and guarded discussion text.\n""",
    "m1_rp3_maintenance_heating": """# Lana Wave-1 cleanup changes — M1 RP-3 — 20260708T182812Z\n\n- Demoted title/framing to an optical BPT-AGN denominator for X-ray/radio follow-up, not maintenance-heating evidence.\n- Added universal selection-function disclosure plus a massive-host attrition table: 85,225 public mass-selected, 35,482 public S/N>=3, 9,298 cached for logM>=10.8.\n- Inserted exact operational definitions: `lgm_tot_p50 >= 10.8` and `specsfr_tot_p50 < -11.0`.\n- Preserved BPT AGN fraction results (0.430 massive; 0.607 massive low-sSFR) while labeling intervals as target-planning approximations.\n- Added radio/X-ray/cavity literature only as future-data and missing-measurement context.\n""",
    "m2_p1_outflow_escape_recycling": """# Lana Wave-1 cleanup changes — M2 P1 — 20260708T182812Z\n\n- Replaced the previous missing-criterion note with the exact high-excitation definition: recomputed BPT AGN and log([OIII]/Hb)>0.25.\n- Added universal selection-function disclosure for the capped SDSS four-line denominator.\n- Added candidate-definition sensitivity table and S/N matched-offset robustness table from Goru outputs.\n- Made the median sSFR contrast explicitly descriptive/no-causal and added guards against escape/recycling overclaiming.\n- Integrated outflow/multiphase citations only as future-observable requirements, not evidence for the SDSS result.\n""",
}


def materialize_tex(slug: str, tex: str) -> Path:
    info = PAPERS[slug]
    out_dir = LANA / "revision-drafts" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    tex = tex.replace("__RP2FIG__", str((RUN8 / "m1_rp2_environment_quenching/figures").resolve()))
    tex = tex.replace("__RP3FIG__", str((RUN8 / "m1_rp3_maintenance_heating/figures").resolve()))
    tex = tex.replace("__M2P1FIG__", str((RUN8 / "m2_p1_outflow_escape_recycling/figures").resolve()))
    tex = tex.replace("__GORUFIG__", str(GORU_FIGS.resolve()))
    tex_path = out_dir / info["tex_name"]
    tex_path.write_text(dedent(tex).lstrip(), encoding="utf-8")
    (out_dir / f"CHANGES_{TS}.md").write_text(CHANGE_TEXT[slug], encoding="utf-8")
    return tex_path


def main() -> int:
    (LANA / "scripts").mkdir(parents=True, exist_ok=True)
    (LANA / "ticks").mkdir(parents=True, exist_ok=True)
    inputs_read = {
        "brief": str((WORK / "OVERNIGHT_BRIEF.md").relative_to(WORK)),
        "swarm_board": str((WORK / "SWARM_BOARD.md").relative_to(WORK)),
        "all_9_current_aastex_sources_read_by_lane_tick": True,
        "all_9_analysis_json_read_by_lane_tick": True,
        "additional_sources": [
            "lanes/hwao/HWAO_DIRECTOR_TICK_20260708T181425Z.md",
            "lanes/literature/literature_source_packet_20260708T143233Z.md",
            "lanes/tori/selection-function-attrition/20260708T155514Z/selection_function_attrition_summary_20260708T155514Z.json",
            "lanes/goru/tables/high_excitation_denominators_20260708T162615Z.csv",
            "lanes/goru/tables/bpt_class_sensitivity_matched_offsets_20260708T162615Z.csv",
            "lanes/external-cli/EXTERNAL_CLI_TICK_20260708T165503Z.md",
        ],
    }
    tex_map = {
        "m1_rp2_environment_quenching": RP2_TEX,
        "m1_rp3_maintenance_heating": RP3_TEX,
        "m2_p1_outflow_escape_recycling": M2P1_TEX,
    }
    drafts = []
    for slug, tex in tex_map.items():
        tex_path = materialize_tex(slug, tex)
        result = compile_tex(tex_path)
        info = PAPERS[slug]
        drafts.append({
            "paper_slug": slug,
            "source_tex": str(info["run_tex"].relative_to(AUTOPILOT)),
            "source_json": str(info["analysis_json"].relative_to(AUTOPILOT)),
            "draft_tex": str(tex_path.relative_to(WORK)),
            "changes_md": str((tex_path.parent / f"CHANGES_{TS}.md").relative_to(WORK)),
            **result,
            "primary_changes": CHANGE_TEXT[slug].splitlines()[2:],
        })
    manifest = {
        "timestamp_utc": TS,
        "lane": "lana",
        "marker": f"LANA_MANUSCRIPT_TICK_{TS}",
        "scope": "Wave-1 selection-function and exact-definition cleanup drafts for M1 RP-2, M1 RP-3, and M2 P1; public-linked manuscripts/PDFs were not overwritten.",
        "source_read_confirmation": inputs_read,
        "drafts": drafts,
        "safety": "Lane-local files only, plus the required one-line OVERNIGHT_LEDGER.md append performed after verification. No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs.",
    }
    manifest_path = LANA / f"lana_revision_manifest_{TS}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    tick = LANA / "ticks" / f"TICK_{TS}.md"
    pdf_lines = []
    for d in drafts:
        pdf_lines.append(
            f"- `{d['pdf']}` — exit {d['compile_exit_code']}, bytes {d['pdf_bytes']}, SHA256 `{d['pdf_sha256']}`, %PDF={d['pdf_starts_with_pdf']}, fatal markers={d['fatal_markers']}"
        )
    tick.write_text(
        dedent(f"""
        # Lana manuscript tick — {TS}

        Marker: `LANA_MANUSCRIPT_TICK_{TS}`

        ## Scope read before writing

        Read and used the required overnight context: `OVERNIGHT_BRIEF.md`, `SWARM_BOARD.md`, current AASTeX sources and `analysis_results.json` for all 9 active papers, latest Hwao direction, Wave-1 literature packet, Tori selection-function attrition packet, Goru BPT/S/N robustness tables, and External CLI critique.

        This tick performed deep manuscript-writing cleanup for three Wave-1 papers:
        1. M1 RP-2 — `m1_rp2_environment_quenching`
        2. M1 RP-3 — `m1_rp3_maintenance_heating`
        3. M2 P1 — `m2_p1_outflow_escape_recycling`

        ## Lane-local artifacts written

        Manifest:
        - `lanes/lana/lana_revision_manifest_{TS}.json`

        Revision drafts and change records:
        - `lanes/lana/revision-drafts/m1_rp2_environment_quenching/m1_rp2_environment_quenching_lana_selection_definitions_revision_{TS}.tex`
        - `lanes/lana/revision-drafts/m1_rp2_environment_quenching/CHANGES_{TS}.md`
        - `lanes/lana/revision-drafts/m1_rp3_maintenance_heating/m1_rp3_maintenance_heating_lana_selection_definitions_revision_{TS}.tex`
        - `lanes/lana/revision-drafts/m1_rp3_maintenance_heating/CHANGES_{TS}.md`
        - `lanes/lana/revision-drafts/m2_p1_outflow_escape_recycling/m2_p1_outflow_escape_recycling_lana_selection_definitions_revision_{TS}.tex`
        - `lanes/lana/revision-drafts/m2_p1_outflow_escape_recycling/CHANGES_{TS}.md`

        Compiled lane-local PDFs:
        {chr(10).join(pdf_lines)}

        ## Manuscript improvements made

        ### M1 RP-2 density-proxy quenching
        - Added mandatory selection-function disclosure: 249,917 strict public four-line S/N>=3 rows, 60,000 cached rows, 24.0% coverage, `TOP 60000 ... ORDER BY specObjID` caveat, and sSFR-dependent line retention.
        - Inserted exact quenched definition `specsfr_tot_p50 < -11.0` and a portable 10th-nearest-neighbour density-proxy method.
        - Kept the result as a density-proxy association and added Peng/Baldry context plus Wetzel/Goubert future-data guards.

        ### M1 RP-3 maintenance-heating follow-up denominator
        - Demoted title/framing to an optical BPT-AGN denominator for X-ray/radio follow-up, not a maintenance-heating measurement.
        - Added massive-host attrition counts and exact definitions: `lgm_tot_p50 >= 10.8` and `specsfr_tot_p50 < -11.0`.
        - Preserved optical fractions while guarding against jet-power, cooling-luminosity, cavity, halo-gas, and duty-cycle overclaims.

        ### M2 P1 outflow escape/recycling follow-up denominator
        - Replaced the missing-criterion note with the exact high-excitation definition: recomputed BPT AGN and `log([OIII]/Hb) > 0.25`.
        - Added candidate-definition sensitivity and S/N matched-offset robustness tables from Goru.
        - Guarded median sSFR and matched-offset contrasts as optical target characterization only, not escape/recycling evidence.

        ## Safety

        No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs were touched. Current linked manuscripts/PDFs were not overwritten. Only lane-local revision artifacts were written, plus the required one-line overnight ledger append after verification.
        """).strip() + "\n",
        encoding="utf-8",
    )
    bad = [d for d in drafts if d["compile_exit_code"] != 0 or not d["pdf_starts_with_pdf"] or d["fatal_markers"]]
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
