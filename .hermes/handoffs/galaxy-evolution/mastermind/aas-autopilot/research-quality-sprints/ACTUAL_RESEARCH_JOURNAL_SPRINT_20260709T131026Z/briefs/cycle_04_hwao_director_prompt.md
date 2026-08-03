You are Hwao/Fable, director for the NebulaMind actual-data journal-paper quality sprint.

Task: produce a paper-quality triage plan for this cycle. Work in read-only review mode.

Output marker: ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_04

Required output:
- publication-readiness verdict for the RP-1 flagship and the supplementary denominator/proxy atlas
- top 12 concrete quality improvements, ranked by scientific value
- what can be improved now using real local SDSS data already inventoried
- what requires new real data and therefore must not be written as a result yet
- exact guidance for the integrator: safe wording/citation changes only
- a no-mock-data receipt and safety ledger

Hard rules:
- Never use or propose mock/synthetic/fake/placeholder/toy data.
- Do not invent numbers, sample sizes, citations, URLs, DOIs, arXiv IDs, or ADS bibcodes.
- Preserve the association-only boundary for RP-1 unless a real added dataset justifies more.
- Read-only: do not edit files, publish, deploy, write DB/API/wiki/git/cron, or touch public/live roots.

Context follows:
Sprint: ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z cycle 4

REAL-DATA-ONLY POLICY:
- Never use mock, synthetic, fake, placeholder, or toy data.
- Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.
- New quantitative claims must be traceable to the real local SDSS artifacts inventoried by this sprint or to a cited public source with URL/DOI/arXiv/ADS metadata.
- If a value is not present in the local real-data inventory or a cited public source, write 'not measured here' or 'needs real data'.
- Literature-only sources may motivate future work; they do not become measured NebulaMind results.
- The RP-1 flagship remains an optical SDSS/BPT association pilot unless real additional observables are supplied.

SAFETY LOCKS:
- write only under this sprint directory and candidate copies
- no public pages, public PDF replacement, or live/static root edits
- no product DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation
- no deploy/restart
- no git commit/push/merge/rebase/history rewrite
- no cron creation/update
- no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads
- no external manuscript submission

Primary candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_04_package
Flagship TeX: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex
Supplement TeX: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
Integrated nine-paper context root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z

REAL-DATA INVENTORY COUNTS:
{
  "csv_files": 35,
  "json_files": 155,
  "integrated_tex_files": 9,
  "pdf_files": 43
}

INTEGRATED DRAFT SUMMARIES:
- Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot
  path: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
  abstract: We integrate the strongest Galaxy Evolution pilot into a selection-aware short-paper draft: a matched-control comparison of catalog specific star formation in broad BPT optical AGN hosts and star-forming controls in SDSS DR17. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a flagship short-paper draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- SDSS density proxy for environmental quenching: selection-aware SDSS optical proxy integration
  path: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
  abstract: We integrate the active proposal 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- Optical-AGN denominator for maintenance-heating follow-up: selection-aware SDSS optical proxy integration
  path: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
  abstract: We integrate the active proposal 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- SDSS high-excitation AGN denominator for outflow escape tests: selection-aware SDSS optical proxy integration
  path: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
  abstract: We integrate the active proposal 'Escape versus recycling: the fate of AGN-driven multiphase outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- Environment proxy for optical AGN in massive SDSS hosts: selection-aware SDSS optical proxy integration
  path: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
  abstract: We integrate the active proposal 'Environmental dependence of radio-jet coupling efficiency in galaxy gas' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- SDSS mass transition in quenching and optical AGN incidence: selection-aware SDSS optical proxy integration
  path: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
  abstract: We integrate the active proposal 'Locating the transition from stellar-feedback to AGN-feedback regulation' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- Common-denominator optical tracer census in SDSS: selection-aware SDSS optical proxy integration
  path: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
  abstract: We integrate the active proposal 'A multiphase, common-denominator census of AGN-driven outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- Optical denominator for gas-fraction versus efficiency tests: selection-aware SDSS optical proxy integration
  path: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
  abstract: We integrate the active proposal 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- SDSS target vector for feedback-model validation: selection-aware SDSS optical proxy integration
  path: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
  abstract: We integrate the active proposal 'Forward-modelled validation of cosmological feedback prescriptions' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.

FLAGSHIP EXCERPT:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Selection-aware SDSS BPT/sSFR study}
\shortauthors{NebulaMind}
\begin{document}

\title{Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Pilot Matched-Control Study}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We present a selection-aware SDSS DR17 pilot matched-control analysis of the association between broad optical BPT-selected galaxies and catalog specific star-formation rate. The analysis is shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts, and by a non-random, 60,000-galaxy computational pilot cap sequentially selected by \texttt{specObjID} from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies; this is an arbitrary cache limit, not a physically motivated or volume-complete subsample. Broad optical BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, with no morphology or aperture-fraction control. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex. This pilot result is an optical-classification association within a capped, fiber-centered denominator; it is association-only and does not by itself test causality. Any causal interpretation would require additional observables beyond this dataset, and any causal star-formation suppression claim remains unsupported here. An accompanying supplement organizes the structural and multiwavelength observables needed for future follow-up tests.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper addresses a narrow association-only question within a low-redshift SDSS DR17 optical emission-line denominator: do broad optical BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a strong negative sSFR offset within the analyzed denominator. The result is not a causal claim or inference; it is an association in a capped optical sample and does not test AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling in this dataset.
The 60,000-galaxy computational pilot cap is an arbitrary cache limit rather than a volume-complete census, so it is not normalized into a luminosity or mass function.


The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT-selected galaxies'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\subsection{Scope and limitations}
The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a 60,000-galaxy computational pilot cap selected sequentially by \texttt{specObjID}. It is a local pilot subset used to validate the analysis workflow and establish the relative association within an arbitrary fixed cache budget, not a volume-limited census. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this cap is not a random sky sample and introduces survey-plate and sky-coverage bias. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the cap is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy; if broad optical BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a global star-formation comparison.
The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade for the flagship analysis sample.\label{tab:selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines with valid flux measurements (\texttt{ivar} $> 0$) & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The 416,554-to-373,445 drop when requiring \texttt{ivar} $> 0$ reflects the removal of rows with unusable line-flux uncertainties; this table does not distinguish masking, edge-of-chip loss, or missing spectral coverage. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the fixed-size-sample limitation.

\section{Classification and matching}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Here, the star-forming control pool is defined as objects below the Kauffmann et al.\ (2003) demarcation. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control by variance-normalized Euclidean distance in standardized $(\log M_\star,z)$ space, with replacement. In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements. The preferred estimate does not impose a maximum mass--redshift caliper; the caliper row in Table~\ref{tab:robust} is a sensitivity variant. The moderate mass--redshift caliper sensitivity variant uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.
Here, ``broad optical BPT-selected'' means the inclusive optical-emission-line class under the standard BPT demarcations, while the Seyfert-like sensitivity check uses the stricter Kewley et al.\ (2006) high-excitation cut to remove the low-excitation LINER/retired branch by construction.

\begin{figure*}
\centering
\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the SDSS DR17 analysis denominator. The matched controls are paired in stellar mass and redshift only, not in morphology, so the diagram verifies the optical-excitation classes used for matching but does not by itself prove accretion-driven feedback.}
\label{fig:bpt}
\end{figure*}

\section{Matched-control result}
The preferred broad optical BPT comparison gives a large negative catalog-sSFR offset for the broad optical BPT-selected galaxies relative to star-forming controls.
\par\noindent\textbf{Morphology and aperture caveat.} A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the observed sSFR offset is highly degenerate with the morphological transition from disk-dominated to bulge-dominated systems \citep{bluck2014,belfiore2016}. The robustness interval in Table~\ref{tab:robust} is a 95\% confidence interval on the median offset.

\begin{deluxetable*}{lrrrr}
\tabletypesize{\scriptsize}
\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
\startdata
Broad optical BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
Broad optical BPT-selected targets, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
\enddata
\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$, and it leaves the median offset essentially unchanged at -1.318 dex for 7,867 pairs. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
\end{deluxetable*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT-selected galaxies minus nearest star-forming controls ($N=8{,}146$ pairs). The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
\label{fig:offsets}
\end{figure*}

\section{Interpretation}
The result is directly measured in the capped sample and remains falsifiable within the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper, which is already reflected by the 7,867-pair, -1.318 dex sensitivity row.
Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. In this sample, the Kewley et al.\ (2006) Seyfert-like cut trims away the low-excitation LINER/retired branch that is present in the broader BPT denominator, so the smaller offset reflects a narrower emission-line selection rather than a change in feedback strength. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad optical BPT-selected sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global star-formation suppression signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size 60,000-galaxy pilot sample. Any causal star-formation suppression claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{Conclusion}
RP-1 is a selection-aware pilot association paper. Its key results are the preferred -1.309 dex offset, the persistence of the offset under a moderate mass--redshift caliper, and the reduction to -0.763 dex under stricter line-S/N and Seyfert-like subsets. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} collects the missing-observable requirements for future physical tests. See Supplement Sections 3.1 and 3.7 for the neighbor-rank/fiber-collision caveat and CO/HI follow-up requirements.
In practice, that means future work needs the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation comparisons passed through the same selection functions \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,piotrowska2022,wetzel2013,dekel2006}; these references are cited as examples of the missing observables, not as validation of any mechanism in this SDSS-only denominator.

\section*{Data Availability}
This paper uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. The 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and the manuscript conclusions remain conditional on the optical-emission-line denominator.

\facilities{SDSS}

\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Belfiore et al.(2016)]{belfiore2016} Belfiore, A., Maiolino, R., Maraston, C., et al. 2016, MNRAS, 461, 3111
\bibitem[Bluck et al.(2014)]{bluck2014} Bluck, A.~F.~L., Bruce, V.~A., Pilkington, K., et al. 2014, MNRAS, 441, 599
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et

[TRUNCATED at 18000 chars from /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex]


SUPPLEMENT EXCERPT:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS denominator/proxy atlas}
\shortauthors{NebulaMind}
\begin{document}

\title{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
This supplement organizes eight SDSS DR17 denominator and proxy notes into one coherent atlas built around the same 60,000-galaxy computational pilot cap and selection-function caveats. The 60,000-galaxy sample is a local, non-random computational pilot cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this cap is not a random sky sample and introduces survey-plate and sky-coverage bias. The atlas preserves follow-up targets for environment, BPT-defined AGN/composite incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-based comparison data are treated as missing observables for future tests rather than as measurements in this package. The sample coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one atlas with eight linked entries, not eight independent causal-feedback papers. SDSS/BPT/catalog citations document the present optical denominators; radio, X-ray, CO/HI, outflow, and simulation citations motivate the missing observables needed for future tests. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an association between BPT classification and catalog sSFR. These eight entries are distinct baseline-and-follow-up atlas notes: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the entries span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. Keeping the notes in one supplement keeps the atlas coherent and gives future work a single checklist of what still must be added.

\section{Shared denominator}
The atlas uses the same analyzed public-data backbone as the main paper: 60,000 galaxies in a computational pilot cap from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, i.e. 24.0\% sample coverage. The four-line selection is sSFR-dependent and the sample is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The galaxy-by-galaxy stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing. The 60,000-row cache is an arbitrary computational pilot cap, not a physical selection threshold.

The eight subsections below are intentionally parallel baseline-plus-follow-up notes: each one states the observed optical denominator or target vector, then names the missing observables that a future multiwavelength or simulation-based test would need before any physical inference can be made. In other words, the sections are distinct follow-up domains bounded by the same optical selection effect, and their role is to organize the atlas rather than to stand as separate papers.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade shared by the atlas; the cache cap is summarized in the main paper.\label{tab:supp-selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines with valid flux measurements (\texttt{ivar} $> 0$) & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The 416,554-to-373,445 drop when requiring \texttt{ivar} $> 0$ reflects the removal of rows with unusable line-flux uncertainties; this table does not distinguish masking, edge-of-chip loss, or missing spectral coverage. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

\section{Atlas notes}
As a reminder, each atlas entry is a baseline-plus-follow-up checklist, not a standalone physical-feedback result.

\subsection{Relative neighbor-count baseline: SDSS 10th-neighbor index for low-sSFR incidence}
We establish a relative neighbor-count baseline within the emission-line denominator that can later be joined to group catalogs and halo masses. The 10th-neighbor index is the rank of the 10th nearest companion in projected sky separation within this redshift-limited sample; it is an internal ordinal rank within this selection-biased sample and does not map to physical environmental volume density or halo density. The SDSS 55-arcsec fiber-collision limit systematically removes close neighbors in dense regions, so the 10th-neighbor proxy is biased before any physical interpretation is attempted. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004. The follow-up ingredients are group catalogues, robust central/satellite labels, halo masses, a spectroscopic fiber-collision correction at the 55-arcsec scale, morphology, and multi-redshift selection functions. Within this selection-biased emission-line sample, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.
\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up.}
\label{fig:m1-rp2-neighbor-count-baseline}
\end{figure}


\subsection{Maintenance-heating denominator: BPT-defined AGN/composite hosts in massive SDSS galaxies}
We isolate the BPT-defined AGN/composite duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the BPT-defined AGN/composite fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The BPT-defined AGN/composite fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. See the next subsection for the related radio-jet baseline that uses the same projected-density proxy. The follow-up ingredients are X-ray cavity or cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements.}
\label{fig:m1-rp3-maintenance-heating}
\end{figure}


\subsection{High-excitation optical AGN baseline: resolved kinematics follow-up}
We isolate the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The follow-up ingredients are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
\caption{SDSS optical emission-line denominator: the high-excitation AGN subset used to define an observational baseline for future resolved-kinematic measurements.}
\label{fig:m2-p1-outflow-escape-recycling}
\end{figure}


\subsection{Radio-jet environment baseline: BPT-defined AGN/composite fraction vs. 10th-neighbor index in massive hosts}
We define the environment-stratified optical denominator that future radio and X-ray work could test. This subsection reuses the same projected-neighbor ranking described in the relative neighbor-count baseline above and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has a BPT-defined AGN/composite fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The follow-up ingredients are radio jet morphology and age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
\caption{SDSS optical emission-line denominator: the high- and low-density quartile comparison among massive SDSS hosts, used as a baseline for future radio-jet and X-ray work.}
\label{fig:m2-p2-radio-jet-environment}
\end{figure}


\subsection{Stellar-mass selection diagnostic: low-sSFR and BPT-defined AGN/composite incidence}
In this optical-emission-line denominator, the 11.0--12.5 dex peak is consistent with a selection-function effect: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is concentrated in that mass bin. It must not be interpreted as a universal feedback threshold. We identify the mass bin where a future gas-inclusive study should look for an apparent incidence change. The note measures the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the BPT-defined AGN/composite incidence peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The follow-up ingredients are gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions. The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and BPT-defined AGN/composite incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up.}
\label{fig:m2-p3-feedback-transition-mass}
\end{figure}


\subsection{Tracer-threshold census for multiphase follow-up}
We compare optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The follow-up ingredients are ionized, molecular, and neutral tracers, X-ray or radio tracers, a shared parent denominator, and a consistent aperture model. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work.}
\label{fig:m3-p1-multiphase-census}
\end{figure}


\subsection{Low-sSFR optical denominator: baseline for future CO/HI gas measurements}
We define the denominator for CO/HI gas-fraction and depletion-time follow-up. The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its BPT-defined AGN/composite fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency \citep{tacconi2018}; this note identifies the CO/HI follow-up denominator and optical baseline required for spatially resolved gas tests. The follow-up ingredients are CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
\caption{SDSS optical emission-line denominator: the massive low-sSFR SDSS galaxies available for CO/HI depletion-time follow-up.}
\label{fig:m3-p2-gas-depletion-efficiency}
\end{figure}


\subsection{Simulation target vector for forward-model comparison}
We provide a compact observed target vector for forward modelling. The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, BPT-defined AGN/composite incidence, and colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and BPT-defined AGN/composite fractions span 0.003-0.520. The follow-up ingredients are simulations \citep{schaye2015} passed through the exact optical S/N and fiber-aperture selection function used here, then through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions, together with aperture models and noise models. Without those matched selection steps, any simulation comparison is not a valid test. This entry remains an optical baseline only; the missing observables listed in Table~\ref{tab:atlas-summary} are required before any physical inference.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
\caption{SDSS optical emission-line denominator: low-sSFR fraction, BPT-defined AGN/composite incidence, and colour versus mass and redshift in the SDSS emission-line sample. This is an observed target vector for forward modelling.}
\label{fig:m3-p3-simulation-validation}
\end{figure}

\section{Atlas summary}
Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight entries. All eight entries are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or forward-model comparison data are added, so their present role is to organize follow-up rather than to establish causal physical claims.

\begin{deluxetable*}{llll}
\tabletypesize{\scriptsize}
\tablecaption{Atlas-level follow-up menu. Each row summarizes the present optical role and the missing observables needed before any physical inference.\label{tab:atlas-summary}}
\tablehead{\colhead{Topic} & \colhead{Observed baseline} & \colhead{Missing observables} & \colhead{Future Follow-up Domain}}
\startdata
Environment & low-sSFR vs.\ 10th-neighbor rank (60,000 total; 15,000 per quartile) & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test \\
Maintenance heating & optical AGN in massive low-sSFR hosts (9,298 massive; 5,695 low-sSFR) & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
Outflow kinematics & high-excitation AGN subset (4,440/60,000) & resolved velocities; halo potentials; multiphase gas; CGM tracers & kinematic follow-up \\
Env.\ jets & density-stratified AGN fraction in massive hosts & radio morphology/age; cavity energetics; hot-gas density & radio-jet follow-up \\
Mass bin & low-sSFR and AGN by $M_\star$ bin (15 cells with $n\geq50$) & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
Tracer census & tracer prevalence in 60k sample (0.136 to 0.418) & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
Gas depletion & massive low-sSFR baseline; H$\alpha$ proxy (6,729 galaxies) & CO/dust gas masses; aperture-matched SFRs; morphology; environment & CO/HI follow-up \\
Simulation vector & mass-redshift target vector (15 cells with $n\geq50$) & simulations through SDSS/MaNGA/ALMA/X-ray/radio selection; aperture/noise models & forward model \\
\enddata
\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects the optical emission-line selection function, which preferentially removes low-equivalent-width or passive systems from the denominator; the surviving sample therefore becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}


\section{Package decision}
These eight entries should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.

\section*{Data Availability}
This atlas uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. The 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and all eight notes remain conditional on the optical-selection denominators summarized in this atlas.

\facilities{SDSS}

\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 

[TRUNCATED at 22000 chars from /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex]

