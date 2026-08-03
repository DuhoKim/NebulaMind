# codex-kun-cycle-5
Started UTC: 2026-07-09T02:39:47Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

Reading additional input from stdin...
OpenAI Codex v0.143.0
--------
workdir: /Users/duhokim/NebulaMind/NebulaMind
model: gpt-5.4-mini
provider: openai
approval: never
sandbox: read-only
reasoning effort: none
reasoning summaries: none
session id: 019f44be-e0ce-7f80-8fd4-71c4ed081c5e
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_05.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m inspecting the package for TeX, compilation, figure, and reproducibility risks, then I’ll verify the required numeric claims against the manuscript text and handoff notes. After that I’ll give exact, safe edit recommendations that preserve the association-only guardrail.
exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
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
This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60,000-row optical emission-line cache and the same selection-function caveats. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. These counts and fractions are conditional on the SDSS optical selection used here, not global volume-limited statistics. It is a single follow-up atlas, not eight independent causal-feedback papers.
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. Keeping them in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.

\section{Shared denominator}
The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}.

The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
\enddata
\end{deluxetable*}

\section{Atlas notes}

\subsection{SDSS density proxy for low-sSFR incidence}
This note isolates an environmental denominator that can later be joined to group catalogs and halo masses. The nearest-neighbour density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the missing observables are:
\begin{itemize}
\item group catalogues
\item robust central/satellite labels
\item halo masses
\item morphology
\item multi-redshift selection functions
\end{itemize}
These are still needed for a physical environmental interpretation \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m1\_rp2\_environment\_quenching. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m1-rp2-environment-quenching}
\end{figure}


\subsection{Optical-AGN denominator for maintenance-heating follow-up}
This note identifies the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can be used as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The missing observables are:
\begin{itemize}
\item X-ray cavity or cooling-luminosity measurements
\item radio jet powers
\item halo-selected parent catalogues
\item nondetection modelling
\end{itemize}
These are still needed for a physical maintenance-heating interpretation \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m1\_rp3\_maintenance\_heating. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m1-rp3-maintenance-heating}
\end{figure}


\subsection{SDSS high-excitation AGN denominator for outflow tests}
This note isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are:
\begin{itemize}
\item resolved outflow velocities
\item halo potentials
\item molecular, ionized, and neutral gas phases
\item CGM recycling tracers
\end{itemize}
These are still needed for a physical outflow interpretation \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m2\_p1\_outflow\_escape\_recycling. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m2-p1-outflow-escape-recycling}
\end{figure}


\subsection{Environment proxy for optical AGN in massive SDSS hosts}
This note defines the environment-stratified optical denominator that future radio and X-ray work could test. The local-density proxy is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-density quartile has an optical AGN fraction of 0.509, while the low-density quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency. The missing observables are:
\begin{itemize}
\item radio jet morphology and age
\item cavity or shock energetics
\item hot-gas density
\item calibrated jet-power estimates
\end{itemize}
These are still needed for a physical radio-jet interpretation \citep{best2005,mcnamara2007,heckmanbest2014}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m2\_p2\_radio\_jet\_environment. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m2-p2-radio-jet-environment}
\end{figure}


\subsection{Stellar-mass distribution of low-sSFR and optical AGN incidence}
This note pins down the mass bin where a future gas-inclusive study should look for an incidence change. At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator? The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\). The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The missing observables are:
\begin{itemize}
\item gas fractions
\item baryon deficits
\item halo masses
\item stellar-feedback observables
\item high-redshift extensions
\end{itemize}
The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a physical transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m2\_p3\_feedback\_transition\_mass. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m2-p3-feedback-transition-mass}
\end{figure}


\subsection{Common-denominator optical tracer census in SDSS}
This note compares optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are:
\begin{itemize}
\item ionized, molecular, and neutral tracers
\item X-ray or radio tracers
\item a shared parent denominator
\item a consistent aperture model
\end{itemize}
These are still needed for a physical multiphase interpretation \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m3\_p1\_multiphase\_census. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m3-p1-multiphase-census}
\end{figure}


\subsection{Optical denominator for gas-fraction versus efficiency tests}
This note defines the denominator for CO/HI gas-fraction and depletion-time follow-up. How many massive low-sSFR or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up? The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The missing observables are:
\begin{itemize}
\item CO or dust-based molecular gas masses
\item aperture-matched SFRs
\item morphology
\item environment labels
\end{itemize}
These are still needed for a physical gas-fraction or depletion-time interpretation \citep{xcoldgass2017,xgass2018,piotrowska2022}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m3\_p2\_gas\_depletion\_efficiency. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m3-p2-gas-depletion-efficiency}
\end{figure}


\subsection{SDSS target vector for feedback-model validation}
This note provides a compact observed target vector for forward modelling, not a direct simulation comparison. What compact SDSS target vector of low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift can be used for forward-model validation? The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact validation vector. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The missing observables are:
\begin{itemize}
\item simulation mocks passed through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions
\item aperture models
\item noise models
\end{itemize}
These are still needed for a physical simulation-validation interpretation \citep{simba2019,tng2019,eagle2015}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m3\_p3\_simulation\_validation. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m3-p3-simulation-validation}
\end{figure}


\section{Package decision}
These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.

\section{Local reproducibility}
This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
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
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}

exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Selection-aware SDSS optical AGN/sSFR pilot}
\shortauthors{NebulaMind}
\begin{document}

\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Pilot}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, both of which can bias fiber-based sSFR comparisons. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish causal AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.

The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and LINER-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The cached analysis table is capped at 60,000 rows and ordered by \texttt{specObjID}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the cache covers 24.0\% of that strict parent.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade for the flagship denominator. The 60,000-row cache is an artificial pilot cap, not a physical selection effect.\label{tab:selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Cached-versus-public marginal checks show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.

\section{Classification and matching}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical AGN host is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.

\begin{figure*}
\centering
\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
\label{fig:bpt}
\end{figure*}

\section{Matched-control result}
The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the optical AGN hosts relative to star-forming controls.
A median $\Delta\log {\rm sSFR}$ of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR, but this manuscript does not convert that proxy offset into a global quenching threshold.

\begin{deluxetable*}{lrrrr}
\tabletypesize{\scriptsize}
\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
\startdata
Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity \\
\enddata
\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. All values are conditional on the optical emission-line denominator.}
\end{deluxetable*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT AGN hosts minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions.}
\label{fig:offsets}
\end{figure*}

\section{Interpretation}
The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper. For readability, that caliper is $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude to roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including LINER-like ionization from retired stellar populations and post-AGB stars, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets suggests that the broad-BPT result still mixes in a LINER-like, retired-stellar component rather than tracing a clean active-accretion population. The most robust conclusion is therefore: broad optical BPT AGN classification is associated with lower catalog sSFR in this capped SDSS emission-line sample. Claims about causal quenching require additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{Conclusion}
RP-1 is best treated as a concise, selection-aware association paper. Related topic notes belong in a supplementary denominator/proxy atlas until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
In practice, that means future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; they are not part of the present SDSS-only denominator.

\section{Local reproducibility}
This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
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
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}

exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/PACKAGE_AUDIT.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# Decision package audit

Package: `RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`
Audit UTC: 2026-07-09T01:41:23Z

## Counts
- outputs: 2
- pdfs_ok: 2
- logs_ok: 2
- figures_ok: 10
- total_figures: 10
- fatal_failures: 0

## Outputs
- flagship: PDF bytes 236847; SHA256 `3392f53534d8452ebb3db4191dff7855ebb13428dff768d45d847be9d5d8efac`; warnings 10; figures 2
- supplement: PDF bytes 527135; SHA256 `403a69d8fcf02c56bd3266db0de0363ea9c45c659d5a305861cfba7144b705e2`; warnings 19; figures 8

## Failures
- none

Safety: local decision package only; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes.

exec
/bin/zsh -lc "rg -n \"8,146|8146|-1\\.309|\\[-1\\.334,\\s*-1\\.283\\]|60,000|249,917|24\\.0%|association-only|guardrail|strict parent|cached rows|coverage|dex\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package -S" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_04_SUMMARY.md:9:- codex-kun-cycle-4: exit=0 elapsed=135.1s output=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_04.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_02_SUMMARY.json:92:      "codex",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_02_SUMMARY.json:102:    "label": "codex-integrator-cycle-2",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_02_SUMMARY.json:147:        "codex",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_02_SUMMARY.json:157:      "label": "codex-kun-cycle-2",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_02_SUMMARY.json:158:      "output_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_02.md",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_01_SUMMARY.md:9:- codex-kun-cycle-1: exit=0 elapsed=136.8s output=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_01.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_03_SUMMARY.json:92:      "codex",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_03_SUMMARY.json:102:    "label": "codex-integrator-cycle-3",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_03_SUMMARY.json:147:        "codex",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_03_SUMMARY.json:157:      "label": "codex-kun-cycle-3",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_03_SUMMARY.json:158:      "output_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_03.md",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_04_SUMMARY.json:92:      "codex",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_04_SUMMARY.json:102:    "label": "codex-integrator-cycle-4",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_04_SUMMARY.json:147:        "codex",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_04_SUMMARY.json:157:      "label": "codex-kun-cycle-4",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_04_SUMMARY.json:158:      "output_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_04.md",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, both of which can bias fiber-based sSFR comparisons. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:24:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The cached analysis table is capped at 60,000 rows and ordered by \texttt{specObjID}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the cache covers 24.0\% of that strict parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:30:\tablecaption{Selection cascade for the flagship denominator. The 60,000-row cache is an artificial pilot cap, not a physical selection effect.\label{tab:selection}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:36:four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:37:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:41:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Cached rows are shown only where the cache applies.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:47:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical AGN host is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:58:A median $\Delta\log {\rm sSFR}$ of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR, but this manuscript does not convert that proxy offset into a global quenching threshold.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:65:Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:66:Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_02_SUMMARY.md:9:- codex-kun-cycle-2: exit=0 elapsed=135.4s output=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_02.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_03_SUMMARY.md:9:- codex-kun-cycle-3: exit=0 elapsed=137.4s output=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_03.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_01_REVIEW_RESPONSE.md:7:- Kept the numerical results unchanged in RP-1: 8,146 pairs, -1.309 dex, and the same bootstrap interval.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_04_REVIEW_RESPONSE.md:7:- In [rp1_flagship_polished.tex](./flagship_rp1/aastex/rp1_flagship_polished.tex), I clarified that the 60,000-row cache is non-random and that the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_04_REVIEW_RESPONSE.md:8:- In [rp1_flagship_polished.tex](./flagship_rp1/aastex/rp1_flagship_polished.tex), I added a short Table 1 caption note that the 60,000-row cap is an artificial pilot constraint, not a physical selection effect.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_04_REVIEW_RESPONSE.md:20:- I did not alter the core association-only boundary in the flagship paper.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_01_SUMMARY.json:109:      "codex",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_01_SUMMARY.json:119:    "label": "codex-integrator-cycle-1",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_01_SUMMARY.json:164:        "codex",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_01_SUMMARY.json:174:      "label": "codex-kun-cycle-1",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_01_SUMMARY.json:175:      "output_path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_01.md",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_02_REVIEW_RESPONSE.md:8:  - marked the 60,000-row emission-line cache as non-random in the abstract;
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_02_REVIEW_RESPONSE.md:10:  - added a short context sentence that `-1.309 dex` is roughly a 20-fold catalog-sSFR suppression without converting it into a physical quenching threshold;
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_02_REVIEW_RESPONSE.md:19:  - tightened the package-decision sentence to preserve the association-only boundary.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/FINAL_HANDOFF.md:84:- Main number: 8,146 matched pairs, median delta log sSFR = -1.309 dex, bootstrap interval [-1.334, -1.283] dex.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/FINAL_HANDOFF.md:86:- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/FINAL_HANDOFF.md:159:1. Read the polished RP-1 PDF for scientific wording, especially whether the association-only claim is clear enough.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:13:This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60,000-row optical emission-line cache and the same selection-function caveats. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. These counts and fractions are conditional on the SDSS optical selection used here, not global volume-limited statistics. It is a single follow-up atlas, not eight independent causal-feedback papers.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:22:The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:29:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:34:four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:35:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:44:This note isolates an environmental denominator that can later be joined to group catalogs and halo masses. The nearest-neighbour density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the missing observables are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:81:This note isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:136:This note compares optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:154:This note defines the denominator for CO/HI gas-fraction and depletion-time follow-up. How many massive low-sSFR or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up? The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The missing observables are:

exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/FINAL_HANDOFF.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# RP-1 flagship + supplementary atlas final handoff

Marker: `RP1_FLAGSHIP_SUPPLEMENT_FINAL_HANDOFF_20260709T014249Z`

Completed at: 2026-07-09 10:42 KST / 2026-07-09T01:42Z

## User directive

Proceed with the recommended next decision after the integrated 9-paper local run.

The prior recommendation was:

1. Review RP-1 as the candidate flagship paper.
2. Decide whether the other 8 should stay standalone guarded PDFs or become appendices/supplementary denominator notes under one combined suite paper.
3. If approved, run a final prose-polish pass on RP-1 only, then recompile and audit.
4. Stop before public replacement/publish unless separately approved.

## Decision made

Proceed with **one flagship paper plus one supplementary denominator/proxy atlas**.

Reason:

- RP-1 is the only current active paper with a direct, coherent SDSS row-level result strong enough for a short-paper draft.
- The other 8 are useful, but they are not 8 independent causal physical-feedback papers with the current SDSS-only data.
- Their correct packaging is as a combined denominator/proxy atlas: target definitions, selection-aware baselines, and missing-observable checklists for future radio/X-ray/CO/HI/outflow/halo/simulation work.

Decision packet:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/FLAGSHIP_REVIEW_DECISION_20260709T013510Z.md`

## Local package created

Package ID:

`RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`

Package root:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`

Package generator:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py`

Precompile manifest:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_MANIFEST_PRECOMPILE.json`

Audit Markdown:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.md`

Audit JSON:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.json`

## Output 1: polished RP-1 flagship draft

PDF:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.pdf`

Source:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.tex`

Compile log:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.compile.log`

Audit result:

- PDF bytes: 236,847
- SHA256: `3392f53534d8452ebb3db4191dff7855ebb13428dff768d45d847be9d5d8efac`
- Compile warnings: 10 AASTeX/line-break warnings only
- Figures: 2
- Fatal failures: 0

Scientific status:

- Candidate flagship short-paper draft.
- Core claim: broad optical BPT AGN hosts in the capped SDSS DR17 optical emission-line denominator have lower catalog sSFR than mass-redshift matched star-forming controls.
- Main number: 8,146 matched pairs, median delta log sSFR = -1.309 dex, bootstrap interval [-1.334, -1.283] dex.
- Guard: association only, not causal AGN feedback.
- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
- Required caveat: S/N>=10 and narrower Seyfert-like definitions reduce the offset magnitude, so subclass/selection dependence is real.

## Output 2: supplementary denominator/proxy atlas

PDF:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf`

Source:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`

Compile log:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log`

Audit result:

- PDF bytes: 527,135
- SHA256: `403a69d8fcf02c56bd3266db0de0363ea9c45c659d5a305861cfba7144b705e2`
- Compile warnings: 19 AASTeX/line-break warnings only
- Figures: 8
- Fatal failures: 0

Scientific status:

The atlas combines the other 8 active drafts as guarded denominator/proxy notes:

1. `m1_rp2_environment_quenching` — density proxy / environment denominator, not halo/group quenching proof.
2. `m1_rp3_maintenance_heating` — optical AGN denominator, not radio/X-ray maintenance-heating measurement.
3. `m2_p1_outflow_escape_recycling` — high-excitation optical AGN denominator, not outflow escape/recycling measurement.
4. `m2_p2_radio_jet_environment` — optical AGN fraction vs internal density proxy, not radio-jet coupling test.
5. `m2_p3_feedback_transition_mass` — mass-vector optical incidence diagnostic, not causal transition-mass physics.
6. `m3_p1_multiphase_census` — optical tracer-threshold census, not multiphase gas census.
7. `m3_p2_gas_depletion_efficiency` — optical/H-alpha denominator for CO/gas follow-up, not gas depletion-time measurement.
8. `m3_p3_simulation_validation` — observed SDSS target vector, not simulation validation/rejection.

## Package audit

From `PACKAGE_AUDIT.md`:

- outputs: 2
- pdfs_ok: 2
- logs_ok: 2
- figures_ok: 10
- total_figures: 10
- fatal_failures: 0

Failures: none.

## Compile/debug note

During compile, the supplement built cleanly first. The flagship initially failed because a generated table row began with `[N II]`, which TeX parsed as optional row spacing after a line break. The generator was fixed to use `N II Seyfert-like proxy` instead. Both PDFs then compiled successfully.

## What changed from the previous integrated 9-paper run

Previous state:

- 9 separate integrated PDFs.
- RP-1 was already flagged as strongest.
- Other 8 were guarded but still emitted as separate paper PDFs.

Current state:

- 1 polished flagship RP-1 paper.
- 1 combined supplementary denominator/proxy atlas containing the other 8.
- Cleaner science package: one real flagship result plus one honest atlas of follow-up denominators and missing observables.

## Next gate

Recommended next step is a human/Hwao/Lana science review of the two-PDF package:

1. Read the polished RP-1 PDF for scientific wording, especially whether the association-only claim is clear enough.
2. Read the supplement as an atlas, not as eight papers.
3. Decide whether to:
   - keep this package local only;
   - do another local prose-polish pass;
   - add a local cover note/README for reviewers;
   - or explicitly approve public replacement/addition of these PDFs.

Publishing/public update is **not** approved by this handoff.

## Safety ledger

No public pages, live roots, public PDF replacement, database writes, SQL, `/api/pages`, `page_versions`, wiki publish, trust recompute, deploy/restart, git commit/push/merge, cron creation/update, billing/cloud/OAuth/API-key changes, or external manuscript submission were performed.

codex
I’ve confirmed the core counts are internally repeated consistently across the flagship, supplement, audit, and handoff. I’m now checking for any phrases that accidentally step over the association-only line or make the cached denominator sound population-complete.
exec
/bin/zsh -lc 'rg -n "causal|feedback|quenching|prove|establish|directly measured|reproducible|falsifiable|global|population-complete|volume-limited|must|requires|associated with|answer is yes|This paper asks|The result is|The most robust conclusion|physical" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex -S' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:13:This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60,000-row optical emission-line cache and the same selection-function caveats. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. These counts and fractions are conditional on the SDSS optical selection used here, not global volume-limited statistics. It is a single follow-up atlas, not eight independent causal-feedback papers.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:19:The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. Keeping them in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:22:The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:24:The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:52:These are still needed for a physical environmental interpretation \citep{peng2010,wetzel2013,dekel2006}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:57:\caption{SDSS optical denominator/proxy diagnostic for m1\_rp2\_environment\_quenching. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:58:\label{fig:m1-rp2-environment-quenching}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:70:These are still needed for a physical maintenance-heating interpretation \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:75:\caption{SDSS optical denominator/proxy diagnostic for m1\_rp3\_maintenance\_heating. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:88:These are still needed for a physical outflow interpretation \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:93:\caption{SDSS optical denominator/proxy diagnostic for m2\_p1\_outflow\_escape\_recycling. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:106:These are still needed for a physical radio-jet interpretation \citep{best2005,mcnamara2007,heckmanbest2014}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:111:\caption{SDSS optical denominator/proxy diagnostic for m2\_p2\_radio\_jet\_environment. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:117:This note pins down the mass bin where a future gas-inclusive study should look for an incidence change. At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator? The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\). The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The missing observables are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:122:\item stellar-feedback observables
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:125:The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a physical transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:130:\caption{SDSS optical denominator/proxy diagnostic for m2\_p3\_feedback\_transition\_mass. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:131:\label{fig:m2-p3-feedback-transition-mass}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:136:This note compares optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:143:These are still needed for a physical multiphase interpretation \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:148:\caption{SDSS optical denominator/proxy diagnostic for m3\_p1\_multiphase\_census. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:161:These are still needed for a physical gas-fraction or depletion-time interpretation \citep{xcoldgass2017,xgass2018,piotrowska2022}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:166:\caption{SDSS optical denominator/proxy diagnostic for m3\_p2\_gas\_depletion\_efficiency. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:171:\subsection{SDSS target vector for feedback-model validation}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:178:These are still needed for a physical simulation-validation interpretation \citep{simba2019,tng2019,eagle2015}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:183:\caption{SDSS optical denominator/proxy diagnostic for m3\_p3\_simulation\_validation. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:189:These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, both of which can bias fiber-based sSFR comparisons. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:19:This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish causal AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:24:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The cached analysis table is capped at 60,000 rows and ordered by \texttt{specObjID}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the cache covers 24.0\% of that strict parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:25:Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:26:The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:30:\tablecaption{Selection cascade for the flagship denominator. The 60,000-row cache is an artificial pilot cap, not a physical selection effect.\label{tab:selection}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:52:\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:58:A median $\Delta\log {\rm sSFR}$ of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR, but this manuscript does not convert that proxy offset into a global quenching threshold.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex:82:The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper. For readability, that caliper is $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude to roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including LINER-like ionization from retired stellar populations and post-AGB stars, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets suggests that the broad-BPT result still mixes in a LINER-like, retired-stellar component rather than tracing a clean active-accretion population. The most robust conclusion is therefore: broad optical BPT AGN classification is associated with lower catalog sSFR in this capped SDSS emission-line sample. Claims about causal quenching require additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex | nl -ba | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Selection-aware SDSS optical AGN/sSFR pilot}
     5	\shortauthors{NebulaMind}
     6	\begin{document}
     7	
     8	\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Pilot}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, both of which can bias fiber-based sSFR comparisons. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}
    17	
    18	\section{Question and claim boundary}
    19	This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish causal AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
    20	
    21	The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and LINER-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.
    22	
    23	\section{Data and shared selection}
    24	The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The cached analysis table is capped at 60,000 rows and ordered by \texttt{specObjID}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the cache covers 24.0\% of that strict parent.
    25	Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
    26	The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Selection cascade for the flagship denominator. The 60,000-row cache is an artificial pilot cap, not a physical selection effect.\label{tab:selection}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Cached-versus-public marginal checks show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.
    45	
    46	\section{Classification and matching}
    47	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical AGN host is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
    48	
    49	\begin{figure*}
    50	\centering
    51	\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
    52	\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
    53	\label{fig:bpt}
    54	\end{figure*}
    55	
    56	\section{Matched-control result}
    57	The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the optical AGN hosts relative to star-forming controls.
    58	A median $\Delta\log {\rm sSFR}$ of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR, but this manuscript does not convert that proxy offset into a global quenching threshold.
    59	
    60	\begin{deluxetable*}{lrrrr}
    61	\tabletypesize{\scriptsize}
    62	\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
    63	\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
    64	\startdata
    65	Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
    66	Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
    67	Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
    68	Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
    69	N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity \\
    70	\enddata
    71	\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. All values are conditional on the optical emission-line denominator.}
    72	\end{deluxetable*}
    73	
    74	\begin{figure*}
    75	\centering
    76	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    77	\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT AGN hosts minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions.}
    78	\label{fig:offsets}
    79	\end{figure*}
    80	
    81	\section{Interpretation}
    82	The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper. For readability, that caliper is $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude to roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including LINER-like ionization from retired stellar populations and post-AGB stars, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets suggests that the broad-BPT result still mixes in a LINER-like, retired-stellar component rather than tracing a clean active-accretion population. The most robust conclusion is therefore: broad optical BPT AGN classification is associated with lower catalog sSFR in this capped SDSS emission-line sample. Claims about causal quenching require additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
    83	
    84	\section{Conclusion}
    85	RP-1 is best treated as a concise, selection-aware association paper. Related topic notes belong in a supplementary denominator/proxy atlas until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
    86	In practice, that means future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; they are not part of the present SDSS-only denominator.
    87	
    88	\section{Local reproducibility}
    89	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
    90	
    91	
    92	\begin{thebibliography}{}
    93	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    94	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    95	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    96	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    97	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
    98	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
    99	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   100	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   101	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   102	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   103	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   104	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   105	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   106	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   107	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   108	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   109	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   110	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   111	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   112	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   113	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   114	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   115	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   116	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   117	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   118	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   119	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   120	\end{thebibliography}
   121	
   122	\end{document}

exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | nl -ba | sed -n '1,240p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS denominator/proxy atlas}
     5	\shortauthors{NebulaMind}
     6	\begin{document}
     7	
     8	\title{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60,000-row optical emission-line cache and the same selection-function caveats. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. These counts and fractions are conditional on the SDSS optical selection used here, not global volume-limited statistics. It is a single follow-up atlas, not eight independent causal-feedback papers.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}
    17	
    18	\section{Purpose}
    19	The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. Keeping them in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.
    20	
    21	\section{Shared denominator}
    22	The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}.
    23	
    24	The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.
    25	
    26	\begin{deluxetable*}{lrrr}
    27	\tabletypesize{\scriptsize}
    28	\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
    29	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    30	\startdata
    31	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    32	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    33	plus galSpecLine join & 416,554 & -- & 0.831 \\
    34	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    35	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    36	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    37	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    38	\enddata
    39	\end{deluxetable*}
    40	
    41	\section{Atlas notes}
    42	
    43	\subsection{SDSS density proxy for low-sSFR incidence}
    44	This note isolates an environmental denominator that can later be joined to group catalogs and halo masses. The nearest-neighbour density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the missing observables are:
    45	\begin{itemize}
    46	\item group catalogues
    47	\item robust central/satellite labels
    48	\item halo masses
    49	\item morphology
    50	\item multi-redshift selection functions
    51	\end{itemize}
    52	These are still needed for a physical environmental interpretation \citep{peng2010,wetzel2013,dekel2006}.
    53	
    54	\begin{figure}
    55	\centering
    56	\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
    57	\caption{SDSS optical denominator/proxy diagnostic for m1\_rp2\_environment\_quenching. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    58	\label{fig:m1-rp2-environment-quenching}
    59	\end{figure}
    60	
    61	
    62	\subsection{Optical-AGN denominator for maintenance-heating follow-up}
    63	This note identifies the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can be used as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The missing observables are:
    64	\begin{itemize}
    65	\item X-ray cavity or cooling-luminosity measurements
    66	\item radio jet powers
    67	\item halo-selected parent catalogues
    68	\item nondetection modelling
    69	\end{itemize}
    70	These are still needed for a physical maintenance-heating interpretation \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.
    71	
    72	\begin{figure}
    73	\centering
    74	\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
    75	\caption{SDSS optical denominator/proxy diagnostic for m1\_rp3\_maintenance\_heating. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    76	\label{fig:m1-rp3-maintenance-heating}
    77	\end{figure}
    78	
    79	
    80	\subsection{SDSS high-excitation AGN denominator for outflow tests}
    81	This note isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are:
    82	\begin{itemize}
    83	\item resolved outflow velocities
    84	\item halo potentials
    85	\item molecular, ionized, and neutral gas phases
    86	\item CGM recycling tracers
    87	\end{itemize}
    88	These are still needed for a physical outflow interpretation \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.
    89	
    90	\begin{figure}
    91	\centering
    92	\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
    93	\caption{SDSS optical denominator/proxy diagnostic for m2\_p1\_outflow\_escape\_recycling. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    94	\label{fig:m2-p1-outflow-escape-recycling}
    95	\end{figure}
    96	
    97	
    98	\subsection{Environment proxy for optical AGN in massive SDSS hosts}
    99	This note defines the environment-stratified optical denominator that future radio and X-ray work could test. The local-density proxy is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-density quartile has an optical AGN fraction of 0.509, while the low-density quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency. The missing observables are:
   100	\begin{itemize}
   101	\item radio jet morphology and age
   102	\item cavity or shock energetics
   103	\item hot-gas density
   104	\item calibrated jet-power estimates
   105	\end{itemize}
   106	These are still needed for a physical radio-jet interpretation \citep{best2005,mcnamara2007,heckmanbest2014}.
   107	
   108	\begin{figure}
   109	\centering
   110	\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
   111	\caption{SDSS optical denominator/proxy diagnostic for m2\_p2\_radio\_jet\_environment. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   112	\label{fig:m2-p2-radio-jet-environment}
   113	\end{figure}
   114	
   115	
   116	\subsection{Stellar-mass distribution of low-sSFR and optical AGN incidence}
   117	This note pins down the mass bin where a future gas-inclusive study should look for an incidence change. At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator? The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\). The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The missing observables are:
   118	\begin{itemize}
   119	\item gas fractions
   120	\item baryon deficits
   121	\item halo masses
   122	\item stellar-feedback observables
   123	\item high-redshift extensions
   124	\end{itemize}
   125	The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a physical transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}.
   126	
   127	\begin{figure}
   128	\centering
   129	\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
   130	\caption{SDSS optical denominator/proxy diagnostic for m2\_p3\_feedback\_transition\_mass. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   131	\label{fig:m2-p3-feedback-transition-mass}
   132	\end{figure}
   133	
   134	
   135	\subsection{Common-denominator optical tracer census in SDSS}
   136	This note compares optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are:
   137	\begin{itemize}
   138	\item ionized, molecular, and neutral tracers
   139	\item X-ray or radio tracers
   140	\item a shared parent denominator
   141	\item a consistent aperture model
   142	\end{itemize}
   143	These are still needed for a physical multiphase interpretation \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.
   144	
   145	\begin{figure}
   146	\centering
   147	\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
   148	\caption{SDSS optical denominator/proxy diagnostic for m3\_p1\_multiphase\_census. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   149	\label{fig:m3-p1-multiphase-census}
   150	\end{figure}
   151	
   152	
   153	\subsection{Optical denominator for gas-fraction versus efficiency tests}
   154	This note defines the denominator for CO/HI gas-fraction and depletion-time follow-up. How many massive low-sSFR or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up? The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The missing observables are:
   155	\begin{itemize}
   156	\item CO or dust-based molecular gas masses
   157	\item aperture-matched SFRs
   158	\item morphology
   159	\item environment labels
   160	\end{itemize}
   161	These are still needed for a physical gas-fraction or depletion-time interpretation \citep{xcoldgass2017,xgass2018,piotrowska2022}.
   162	
   163	\begin{figure}
   164	\centering
   165	\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
   166	\caption{SDSS optical denominator/proxy diagnostic for m3\_p2\_gas\_depletion\_efficiency. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   167	\label{fig:m3-p2-gas-depletion-efficiency}
   168	\end{figure}
   169	
   170	
   171	\subsection{SDSS target vector for feedback-model validation}
   172	This note provides a compact observed target vector for forward modelling, not a direct simulation comparison. What compact SDSS target vector of low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift can be used for forward-model validation? The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact validation vector. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The missing observables are:
   173	\begin{itemize}
   174	\item simulation mocks passed through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions
   175	\item aperture models
   176	\item noise models
   177	\end{itemize}
   178	These are still needed for a physical simulation-validation interpretation \citep{simba2019,tng2019,eagle2015}.
   179	
   180	\begin{figure}
   181	\centering
   182	\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
   183	\caption{SDSS optical denominator/proxy diagnostic for m3\_p3\_simulation\_validation. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   184	\label{fig:m3-p3-simulation-validation}
   185	\end{figure}
   186	
   187	
   188	\section{Package decision}
   189	These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.
   190	
   191	\section{Local reproducibility}
   192	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
   193	
   194	
   195	\begin{thebibliography}{}
   196	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   197	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   198	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   199	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   200	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   201	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   202	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   203	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   204	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   205	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   206	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   207	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   208	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   209	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   210	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   211	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   212	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   213	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   214	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   215	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   216	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   217	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   218	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   219	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   220	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   221	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   222	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   223	\end{thebibliography}
   224	
   225	\end{document}

exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/PACKAGE_AUDIT.md | nl -ba | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	# Decision package audit
     2	
     3	Package: `RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`
     4	Audit UTC: 2026-07-09T01:41:23Z
     5	
     6	## Counts
     7	- outputs: 2
     8	- pdfs_ok: 2
     9	- logs_ok: 2
    10	- figures_ok: 10
    11	- total_figures: 10
    12	- fatal_failures: 0
    13	
    14	## Outputs
    15	- flagship: PDF bytes 236847; SHA256 `3392f53534d8452ebb3db4191dff7855ebb13428dff768d45d847be9d5d8efac`; warnings 10; figures 2
    16	- supplement: PDF bytes 527135; SHA256 `403a69d8fcf02c56bd3266db0de0363ea9c45c659d5a305861cfba7144b705e2`; warnings 19; figures 8
    17	
    18	## Failures
    19	- none
    20	
    21	Safety: local decision package only; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes.

codex
The manuscript is structurally clean: no fatal compile issues were recorded, but the package audit still shows AASTeX warnings. I’m pulling the compile logs now to see whether those warnings are purely line-break noise or if any indicate figure/table/layout fragility that should be fixed before release.
exec
/bin/zsh -lc 'rg -n "Warning|Overfull|Underfull|LaTeX Warning|Undefined|float specifier|too large|line break|Paragraph ended|Missing|Reference|Citation" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log -S' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
3:warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
4:warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
7:warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
8:warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
11:warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
12:warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86

exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
note: Running TeX ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
note: Rerunning TeX because "rp1_flagship_polished.aux" changed ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
note: Rerunning TeX because "rp1_flagship_polished.aux" changed ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
warning: warnings were issued by the TeX engine; use --print and/or --keep-logs for details.
note: Running xdvipdfmx ...
note: Writing `rp1_flagship_polished.pdf` (231.2958984375 KiB)
note: Skipped writing 2 intermediate files (use --keep-intermediates to keep them)

 succeeded in 0ms:
note: Running TeX ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232
note: Rerunning TeX because "supplementary_denominator_atlas.out" changed ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232
warning: warnings were issued by the TeX engine; use --print and/or --keep-logs for details.
note: Running xdvipdfmx ...
note: Writing `supplementary_denominator_atlas.pdf` (514.7802734375 KiB)
note: Skipped writing 2 intermediate files (use --keep-intermediates to keep them)

exec
/bin/zsh -lc 'rg -n "Warning|Overfull|Underfull|LaTeX Warning|Undefined|float specifier|too large|line break|Paragraph ended|Missing|Reference|Citation" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log -S' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
3:warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
4:warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
5:warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
6:warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
7:warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
8:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
9:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
10:warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232
13:warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
14:warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
15:warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
16:warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
17:warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
18:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
19:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
20:warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232

codex
I’ve got the compile diagnostics: both PDFs build, but each has only underfull-box and UTF-8/lineno warnings, no fatal LaTeX errors. I’m doing one last numeric sanity pass now so the review can separate genuine manuscript risk from harmless typesetting noise.
exec
/bin/zsh -lc "awk 'BEGIN{printf \"%.4f\\n\", 249917/501060*100}'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "awk 'BEGIN{printf \"%.4f\\n\", 60000/249917*100}'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
49.8777

 succeeded in 0ms:
24.0080

exec
/bin/zsh -lc "awk 'BEGIN{printf \"%.4f\\n\", 42446/176523*100; printf \"%.4f\\n\", 22311/91768*100}'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
24.0456
24.3124

codex
CODEX_KUN_REVIEW_CYCLE_05

**Findings**
- Low-severity TeX/layout risk: both PDFs compile, but the logs contain only `Underfull \hbox` warnings plus one repeated `lineno.sty` UTF-8 replacement warning in each build. See [flagship compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log) and [supplement compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log). No fatal compile failures or broken figure paths were reported.
- Guardrail risk is contained, but a few sentences are slightly more assertive than the rest of the package. The main one is [flagship abstract / claim boundary](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13) and [the “answer is yes” sentence](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L19). They are not wrong, but they read stronger than the association-only posture unless kept tightly tied to the cached denominator.
- The supplement is structurally safe and consistently guarded. The only wording to watch is the set of section titles and captions that include terms like `quenching`, `maintenance_heating`, `outflow`, and `feedback` in internal labels. Those are acceptable because every subsection explicitly says the note is a denominator/proxy baseline, but they should not be promoted into standalone causal language.

**Numeric Check**
- `8,146` pairs are consistent across the abstract and robustness table in [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13) and [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L65).
- `-1.309 dex` is consistent in the abstract, the main result section, the table, and the final handoff. The bootstrap interval `[-1.334, -1.283]` is also consistent everywhere it appears.
- `60,000` cached rows and `249,917` strict parent rows are repeated consistently in both manuscripts. The stated `24.0%` coverage is the correct one-decimal rounding of `60,000 / 249,917 = 24.0080%`.
- The flagship denominator sums correctly: `39,553 + 12,234 + 8,146 + 67 = 60,000`.
- The supplement repeats the same cached-parent numbers and coverage consistently in [supplementary_denominator_atlas.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L22).

**Safe Edit Recommendations**
1. In [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L19), replace:
   - `The answer is yes for the cached denominator analyzed here.`
   - with `Within the cached denominator analyzed here, the answer is yes.`
   This keeps the result but removes the strongest standalone phrasing.
2. In [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L82), replace:
   - `The result is directly measured, reproducible, and falsifiable inside the stated denominator.`
   - with `The result is measured inside the stated denominator, and the same local selection can be rerun exactly.`
   This preserves reproducibility without overstating independent replication.
3. In [supplementary_denominator_atlas.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L189), if you want a stricter guardrail, replace:
   - `not as independent causal-feedback papers`
   - with `not as independent causal-feedback claims`
   This is a wording-only softening and does not change substance.
4. If the `lineno.sty` UTF-8 warning recurs in future builds, normalize the package inputs to UTF-8 and re-run the TeX build once. The current source appears mostly ASCII, so this is likely a line-numbering-layer artifact rather than a manuscript-content defect.

**Bottom Line**
- Scientifically, the package is internally consistent and safely framed as association-only.
- Technically, it compiles cleanly with non-fatal layout/encoding warnings.
- No numeric inconsistency or broken figure linkage was found in the reviewed local files.

**Safety Ledger**
- Read-only review only.
- No file edits, git writes, deploys, publishes, API calls, credential access, or public/live-root access.
- Inspected only local package files under the requested cycle-05 directory.
tokens used
50,137
CODEX_KUN_REVIEW_CYCLE_05

**Findings**
- Low-severity TeX/layout risk: both PDFs compile, but the logs contain only `Underfull \hbox` warnings plus one repeated `lineno.sty` UTF-8 replacement warning in each build. See [flagship compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log) and [supplement compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log). No fatal compile failures or broken figure paths were reported.
- Guardrail risk is contained, but a few sentences are slightly more assertive than the rest of the package. The main one is [flagship abstract / claim boundary](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13) and [the “answer is yes” sentence](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L19). They are not wrong, but they read stronger than the association-only posture unless kept tightly tied to the cached denominator.
- The supplement is structurally safe and consistently guarded. The only wording to watch is the set of section titles and captions that include terms like `quenching`, `maintenance_heating`, `outflow`, and `feedback` in internal labels. Those are acceptable because every subsection explicitly says the note is a denominator/proxy baseline, but they should not be promoted into standalone causal language.

**Numeric Check**
- `8,146` pairs are consistent across the abstract and robustness table in [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13) and [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L65).
- `-1.309 dex` is consistent in the abstract, the main result section, the table, and the final handoff. The bootstrap interval `[-1.334, -1.283]` is also consistent everywhere it appears.
- `60,000` cached rows and `249,917` strict parent rows are repeated consistently in both manuscripts. The stated `24.0%` coverage is the correct one-decimal rounding of `60,000 / 249,917 = 24.0080%`.
- The flagship denominator sums correctly: `39,553 + 12,234 + 8,146 + 67 = 60,000`.
- The supplement repeats the same cached-parent numbers and coverage consistently in [supplementary_denominator_atlas.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L22).

**Safe Edit Recommendations**
1. In [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L19), replace:
   - `The answer is yes for the cached denominator analyzed here.`
   - with `Within the cached denominator analyzed here, the answer is yes.`
   This keeps the result but removes the strongest standalone phrasing.
2. In [rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L82), replace:
   - `The result is directly measured, reproducible, and falsifiable inside the stated denominator.`
   - with `The result is measured inside the stated denominator, and the same local selection can be rerun exactly.`
   This preserves reproducibility without overstating independent replication.
3. In [supplementary_denominator_atlas.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L189), if you want a stricter guardrail, replace:
   - `not as independent causal-feedback papers`
   - with `not as independent causal-feedback claims`
   This is a wording-only softening and does not change substance.
4. If the `lineno.sty` UTF-8 warning recurs in future builds, normalize the package inputs to UTF-8 and re-run the TeX build once. The current source appears mostly ASCII, so this is likely a line-numbering-layer artifact rather than a manuscript-content defect.

**Bottom Line**
- Scientifically, the package is internally consistent and safely framed as association-only.
- Technically, it compiles cleanly with non-fatal layout/encoding warnings.
- No numeric inconsistency or broken figure linkage was found in the reviewed local files.

**Safety Ledger**
- Read-only review only.
- No file edits, git writes, deploys, publishes, API calls, credential access, or public/live-root access.
- Inspected only local package files under the requested cycle-05 directory.


# command_result
exit_code=0
elapsed_s=126.9
timed_out=False
finished_utc=2026-07-09T02:41:54Z
