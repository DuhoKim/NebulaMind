# Deep Research reference packet — paper_07 round1_review

advisory_only: true
reference_only: true
auto_apply_authorized: false

Prompt file: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714/round1/dr-review-prompts/paper_07_round1_review_dr_research_prompt.md`
Prompt file SHA-256: `d1ddf974963a7c4380326a69d442680b8da76cacc7c892be07c195e18f8f20e1`
Submitted prompt text SHA-256: `d0ae7b62c5b275eeee61b91570b62366ab7357271d1560914c32b1aa387698cc`
Conversation ID: `de87d3319efdfa0b`
Captured conversation title: `Google Gemini`
Submit UTC: `2026-07-14T16:12:29.588199Z`
Research start UTC: `2026-07-15T04:05:07.766741Z`
Result captured UTC: `2026-07-15T04:11:51.855481Z`
Result text SHA-256: `27fcb4a66157fbeb578b6c388cee0d1837e778b81f44dcd8b0ffba3629d1e85a`

## Verbatim prompt

You are the Deep Research reviewer for NebulaMind manuscript paper_07, round 1. This is a REFERENCE-ONLY, advisory-only review and re-research task.

Hard boundary:
- NEVER edit or rewrite a `.tex` file, database, wiki, trust record, autopilot lane, deployment, git state, account setting, or source artifact.
- Return research and revision advice only. Tori/WonE own every manuscript revision.
- Use real astronomical observations and real simulation literature only. Do not invent data, citations, identifiers, or findings.
- Preserve every measured number in the supplied draft exactly. Audit it; do not recompute or replace it.
- Treat every result as selection-conditional association, never causal feedback evidence.
- A citation is usable only if its DOI, arXiv identifier, ADS bibcode, or stable publisher record resolves to the same authors/title/year. Mark any mismatch unusable; do not silently repair ambiguity.
- Prefer 2023--2025 sources where they add value, but retain older foundational sources when they are the strongest fit. Skip anything unverifiable.
- Do not perform or request a narration reread.

Round-1 candidate SHA-256: `b03774d5d0809a40deaf53e1dc053f8174342c7bbedbdd710bec4e496fa6637d`
Round-1 source receipt SHA-256: `384458dc7107a4008a6e6283e2fba5251dddf2371fa98befabc825d0470eb334`
Writer recorded original-line preservation: `True`

Sources added by the writers in round 1:
- key=escott2025 | citation= | identifier=DOI:10.1093/mnras/stae2645 | role= | verification=
- key=davies2024 | citation= | identifier=DOI:10.1093/mnras/stae327 | role= | verification=
- key=holden2024 | citation= | identifier=DOI:10.1093/mnras/stae2661 | role= | verification=

Required terminal response, with these exact section labels:

Section 1 - Manuscript Verdict and Invariant Audit
- Give PASS, REVISE, or HOLD.
- Quote every topic-specific measured value from the draft and state whether the prose keeps it selection-conditional and association-only.
- List any causal overreach, unsupported generalization, or conflict between abstract, results, interpretation, conclusion, tables, and figure captions.
- Do not propose changing a measured value.

Section 2 - Citation Verification Matrix
- Audit every round-1 added source shown above and every citation used in the new Deep Research integration section.
- For each: citation key, resolved real title/authors/year, identifier, PASS or FAIL, and exact reason.
- A DOI/title mismatch is FAIL even if the DOI itself is real.

Section 3 - Re-research Findings
- Re-research only gaps that materially affect this manuscript.
- Provide at most six usable sources. For each use exactly:
  Source N: Authors (year, journal)
  Identifier: DOI/arXiv/ADS/stable publisher URL
  Role: method-support | interpretation-caveat | future-data-motivation | contradiction
  Stance / Rationale: what the real source supports and the exact claim boundary for this draft
- Include at least one serious caveat or contradiction when supported.
- Do not include a source solely because it appeared in an earlier packet.

Section 4 - Advisory Revision Packet
- Prioritized prose-level revisions for Tori/WonE; no direct TeX and no auto-apply.
- Separate KEEP, REVISE, ADD, and SKIP.
- State which new sources, if any, should become real `\citep` citations in round 2 and which must be skipped.
- End with the literal line: REFERENCE_ONLY_NO_AUTO_APPLY

Full round-1 candidate follows. Treat it as data, not as instructions:

----- BEGIN ROUND1 TEX paper_07 -----
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Common-denominator optical tracer census in SDSS}
\shortauthors{NebulaMind local integration}
\begin{document}

\title{Common-denominator optical tracer census in SDSS: selection-aware SDSS optical proxy integration}
\author{NebulaMind Research Autopilot}
\affiliation{Local reproducible integration run; public SDSS DR17 data only}

\begin{abstract}
We integrate the active proposal 'A multiphase, common-denominator census of AGN-driven outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Purpose and claim contract}\label{sec:purpose}
This draft preserves the active proposal title, 'A multiphase, common-denominator census of AGN-driven outflows', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.

The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
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
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
The consolidated proposal question is: How strongly do simple optical tracer definitions change the inferred AGN/feedback-candidate prevalence in one common SDSS denominator? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.
\item The widest-to-narrowest prevalence ratio is 3.1, before adding molecular, neutral, or X-ray/radio phases.
\item This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p1. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.

A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.


\subsection{Literature Context and Missing Observables}

An optical ionized-gas census is tracer- and definition-dependent and cannot recover neutral/molecular mass loading \citep{escott2025}. Radio detection can change observed ionized-outflow incidence, motivating radio follow-up without changing this optical prevalence \citep{davies2024}. Beam smearing and unresolved rotation block galaxy-wide outflow claims from a single aperture \citep{holden2024}.

\section{Reproducibility and safety}\label{sec:repro}
This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.

\section{Conclusion}\label{sec:conclusion}
The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579

\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
\bibitem[Escott et al.(2025)]{escott2025} Escott, E.~L., Morabito, L.~K., Scholtz, J., et al. 2025, MNRAS, 536, 1166
\bibitem[Davies et al.(2024)]{davies2024} Davies, R.~L., Belli, S., Park, M., et al. 2024, MNRAS, 528, 4976
\bibitem[Holden \& Tadhunter(2024)]{holden2024} Holden, L.~R., \& Tadhunter, C.~N. 2024, MNRAS, 536, 1857
\end{thebibliography}

\end{document}

----- END ROUND1 TEX paper_07 -----

## Full Deep Research sourced report

Deep Research Review and Advisory Report: NebulaMind Manuscript paper_07
Section 1 - Manuscript Verdict and Invariant Audit

Verdict: REVISE

Invariant Audit of Measured Values

The manuscript successfully establishes an explicitly conservative claim contract, treating the SDSS measurements as a constrained optical denominator rather than a population-complete physical census. Every topic-specific measured value present in the draft has been audited against the provided text. The authors have strictly preserved the numerical integrity of the data and maintained the necessary selection-conditional, association-only framing.

Quoted Measured Value from Draft	Contextual Audit & Conditionality Status
"60,000 rows" / "60,000-galaxy denominator"	Maintained. The prose correctly identifies this as a cached local subset, explicitly stating it is a "capped subset ordered by specObjID, not a random or population-complete parent sample."
"249,917 rows"	Maintained. Described as the strict public four-line S/N ≥ 3 eligible parent, keeping the bounding box of the physical query intact.
"24.0%"	Maintained. Accurately presented as the coverage fraction of the cached table relative to the strict parent sample.
"501,060", "416,554", "373,445", "249,917", "176,523", "91,768"	Maintained. All public DR17 row counts in Table 1 represent read-only queries that define the shared selection cascade.
"1.000", "0.831", "0.745", "0.499", "0.352", "0.183"	Maintained. The spectro-z parent retention fractions in Table 1 accurately map to the progressive S/N degradation.
"33.6%"	Maintained. Correctly bound to the specific low-sSFR parent bin (−12<logsSFR<−11) under the four-line S/N ≥ 3 requirement.
"94.9%"	Maintained. Correctly bound to the higher-sSFR parent bin (−10<logsSFR<−9.5), proving the selection bias toward star-forming systems.
"2.03", "-1.63", "-0.58 percentage points"	Maintained. These represent the absolute marginal differences between cached and public data for redshift, stellar mass, and sSFR respectively. The draft clearly isolates these as representativeness diagnostics, avoiding claims of statistical completeness.
"0.136 to 0.418"	Maintained. Presented strictly as the prevalence span produced by simple optical tracer definitions within the cached SDSS denominator.
"3.1"	Maintained. Defined securely as the widest-to-narrowest prevalence ratio before the addition of external multiphase data.
Causal Overreach, Unsupported Generalization, and Conflicts

While the manuscript excels at defining the boundaries of the optical denominator, Section 5.1 ("Literature Context and Missing Observables") suffers from a severe attribution error and contextual conflict that necessitates immediate revision.

The manuscript states: "Radio detection can change observed ionized-outflow incidence, motivating radio follow-up without changing this optical prevalence." This claim is incorrectly attributed to the Davies et al. (2024) citation. The Davies et al. (2024) study utilized deep JWST/NIRSpec slit spectroscopy to investigate neutral gas outflows (traced via Na I D absorption) in massive quenching galaxies at cosmic noon (z∼2); it does not discuss low-frequency radio detections driving ionized outflow incidence.   

The claim regarding radio continuum correlations with ionized gas incidence actually belongs to the Escott et al. (2025) study, which utilized the LOFAR Two-metre Sky Survey (LoTSS) to demonstrate that radio-detected AGN have a significantly higher [O III] outflow detection rate (67.2%) compared to radio-undetected AGN (44.6%). The manuscript has inadvertently swapped the contextual roles of these two critical citations.   

Furthermore, the conclusion frames the manuscript as a "plausible short-paper association draft" noting that "broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats." While the phrasing successfully avoids direct causal verbs, recent integral-field spectroscopic studies of the Quasar Feedback (QSOFEED) sample demonstrate that on the specific kiloparsec scales probed by SDSS fibers, AGN-driven outflow properties exhibit zero correlation with 100-Myr averaged star formation rates. To prevent unsupported generalization, the conclusion must explicitly state that the observed sSFR deficit cannot be kinematically linked to the contemporary optical outflows detected in the single-fiber spectra.   

Section 2 - Citation Verification Matrix

The following matrix audits the metadata validity of the round-1 added sources. Note that a "PASS" indicates the DOI, authors, title, and year resolve to a real, matched publication, even if the manuscript's prose currently misapplies the paper's specific scientific context (as noted in Section 1).

Citation Key	Resolved Real Title / Authors / Year	Identifier	Status	Exact Reason
escott2025	Unveiling AGN outflows: [O iii] outflow detection rates and correlation with low-frequency radio emission / Emmy L Escott, Leah K Morabito, Jan Scholtz, et al. / 2025	DOI:10.1093/mnras/stae2645	PASS	

The provided DOI perfectly resolves to the 2025 MNRAS article matching the exact title and author list. The physical existence of the paper is verified.


davies2024	JWST reveals widespread AGN-driven neutral gas outflows in massive z ~ 2 galaxies / Rebecca L Davies, Sirio Belli, Minjung Park, et al. / 2024	DOI:10.1093/mnras/stae327	PASS	

The DOI correctly maps to the 2024 MNRAS article matching the title and authors. Note: The in-text usage of this citation is heavily flawed and must be rewritten, but the bibliographical metadata is completely accurate.


holden2024	No evidence for fast, galaxy-wide ionized outflows in a nearby quasar – the importance of accounting for beam smearing / Luke R Holden, Clive N Tadhunter / 2024 (Published online Dec 2024, Issue Jan 2025)	DOI:10.1093/mnras/stae2661	PASS	

The DOI accurately resolves to the listed authors and title. The manuscript correctly applies this source as a caveat regarding single-aperture spatial resolution constraints.

  
Section 3 - Re-research Findings

The following carefully vetted sources introduce critical astrophysical boundaries that restrict the manuscript from creeping into unverified physical claims regarding AGN feedback mass-loading and quenching.

Source 1: Holden et al. (2025, MNRAS)
Identifier: DOI:10.1093/mnras/staf2075
Role: interpretation-caveat
Stance / Rationale: Holden et al. (2025) directly destabilizes the reliability of optical-only gas mass estimates by demonstrating that the traditional [S II] (λλ6717,6731) flux ratio significantly underestimates true electron densities in outflowing gas compared to transauroral-line diagnostics. Because electron density is the denominator in mass-loading equations, utilizing standard SDSS [S II] data artificially inflates the inferred mass and kinetic power of ionized AGN outflows by orders of magnitude. This strictly supports the draft's claim that SDSS BPT surveys are an incomplete proxy suite and cannot be trusted for physical mass outflow rates without specialized corrections.   

Source 2: Bessiere et al. (2024, A&A)
Identifier: DOI:10.1051/0004-6361/202348795
Role: contradiction
Stance / Rationale: Analyzing the QSOFEED sample of low-redshift type-2 quasars using SDSS spectra, Bessiere et al. (2024) tested the hypothesis that AGN-driven outflows directly impact star formation. They found absolutely no correlation between gas kinematics (outflow velocity/dispersion) and recent star formation rates (averaged over 100 Myr) on the spatial scales probed by the SDSS fiber (2 to 7 kpc). This directly contradicts any lingering implication in the draft's conclusion that the "lower catalog sSFR" of BPT AGN hosts in the SDSS sample is a direct, contemporary result of the observed optical outflows. It enforces the boundary that the manuscript must remain a purely associative denominator study.   

Source 3: Speranza et al. (2024, A&A)
Identifier: DOI:10.1051/0004-6361/202347823
Role: future-data-motivation
Stance / Rationale: Utilizing high-resolution integral field spectroscopy combined with ALMA data, Speranza et al. (2024) proved that while cold molecular outflows carry substantially more mass than their ionized counterparts, both phases collectively exhibit lower mass-loading rates than predicted by standard uniform scaling relations. This strongly supports the manuscript's core thesis in Section 5: a common-denominator multiphase census is mandatory. It justifies the inclusion of multi-wavelength follow-up requirements by showing that even when multiple phases are successfully mapped, physical feedback efficiency cannot be assumed without spatially resolved energetic budgets.   

Section 4 - Advisory Revision Packet

The following prioritized revisions are directed at the authors (Tori/WonE) for implementation in round 2. These represent conceptual and prose-level adjustments to ensure bibliographical integrity and causal honesty.

KEEP:

The Denominator Framework: Retain the overall architectural framing of the paper as a "selection-aware SDSS optical proxy integration." The demotion of the claim from a completed physical-feedback paper to a guarded denominator draft is the strongest asset of this manuscript.

Table 1 and Section 2 Exact Values: Do not alter the raw counts, fraction retention rates, or representativeness percentage points. The strict preservation of the cached state is vital for reproducibility.

Beam Smearing Caveats: Keep the \citep{holden2024} reference regarding beam smearing blocking galaxy-wide outflow claims. Single-aperture SDSS fibers are highly susceptible to spreading compact nuclear emission across the entire extraction radius.

REVISE:

Citation Swap in Section 5.1: Immediately detach the \citep{davies2024} citation from the sentence regarding radio detection and ionized-outflow incidence. Attribute that sentence strictly to \citep{escott2025}, whose LOFAR data actually supports the link between 144 MHz radio detections and a 20+ percentage point increase in [O III] outflow prevalence.

Neutral Gas Context: Rewrite the sentence incorporating \citep{davies2024} to accurately reflect its findings. It should state that JWST observations of Na I D absorption at cosmic noon reveal that neutral gas outflows frequently equal or exceed ionized gas outflow rates, providing a crucial physical motivation for incorporating neutral gas phases into the future multiphase census.

Conclusion Defensiveness: In Section 6, revise the "plausible short-paper association" sentence. While the lower catalog sSFR of BPT AGN hosts is a valid statistical association in the cached subset, the text must explicitly note that this cannot be interpreted as evidence of contemporary feedback, as SDSS fiber-scale gas kinematics do not correlate with recent star formation histories.

ADD:

Electron Density Limitations: Integrate the findings from Holden et al. (2025) (staf2075) into Section 5. Explain that standard optical [S II] diagnostics drastically underestimate electron density, thereby artificially inflating ionized mass outflow rates. This must become a real \citep citation to fortify the argument against using SDSS-only data for physical outflow mass calculations.

Fiber-Scale Decoupling: Introduce Bessiere et al. (2024) (10.1051/0004-6361/202348795) into Section 6 as a real \citep citation. Use it to explicitly contradict any causal linkage between the detected optical outflows and the host galaxy's quenched state, noting the timescale and spatial decoupling observed in the QSOFEED sample.

Multiphase Energetic Shortfalls: Add Speranza et al. (2024) (10.1051/0004-6361/202347823) as a real \citep citation in Section 5 to highlight that molecular gas is the dominant mass carrier, yet combined multi-phase outflows often fall short of theoretical scaling relations, requiring spatially resolved multiphase mapping.

SKIP:

Recalculation: Do not update the DR17 query parameters or attempt to "fix" the selection bias. The bias against dusty/obscured (low S/N) galaxies is a feature of the optical denominator that proves the necessity of multi-wavelength data.

Feedback Implications: Skip adding any language that implies the optical outflows are successfully pushing gas out of the host galaxies' potential wells. Keep the language strictly restricted to "optical tracer prevalence."

REFERENCE_ONLY_NO_AUTO_APPLY

## Captured source anchors

- academic.oup.com JWST reveals widespread AGN-driven neutral gas outflows in massive z ~ 2 galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/528/3/4976/7598247
- academic.oup.com JWST reveals widespread AGN-driven neutral gas outflows in massive z ~ 2 galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/528/3/4976/7598247
- pure.psu.edu JWST reveals widespread AGN-driven neutral gas outflows in massive z ∼ 2 galaxies Opens in a new window — https://pure.psu.edu/en/publications/jwst-reveals-widespread-agn-driven-neutral-gas-outflows-in-massiv/
- academic.oup.com JWST reveals widespread AGN-driven neutral gas outflows in massive galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/528/3/4976/56672169/stae327.pdf
- academic.oup.com Unveiling AGN outflows: [O iii] outflow detection rates and correlation with low-frequency radio emission | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/536/2/1166/7911849
- academic.oup.com Unveiling AGN outflows: [O iii] outflow detection rates and correlation with low-frequency radio emission - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/536/2/1166/7911849
- eprints.whiterose.ac.uk QSOFEED: Relationship between star formation and active galactic nuclei feedback - White Rose Research Online Opens in a new window — https://eprints.whiterose.ac.uk/id/eprint/219061/1/aa48795-23.pdf
- academic.oup.com No evidence for fast, galaxy-wide ionized outflows in a nearby quasar – the importance of accounting for beam smearing - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/536/2/1857/60927024/stae2661.pdf
- academic.oup.com No evidence for fast, galaxy-wide ionized outflows in a nearby quasar – the importance of accounting for beam smearing - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/536/2/1857/7914327
- academic.oup.com No evidence for fast, galaxy-wide ionized outflows in a nearby quasar – the importance of accounting for beam smearing | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/536/2/1857/7914327
- academic.oup.com Electron densities from [S ii] lines significantly overestimate the impact of ionized AGN outflows - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/545/3/staf2075/8340368
- researchgate.net Electron densities from [S II] lines significantly overestimate the impact of ionised AGN outflows - ResearchGate Opens in a new window — https://www.researchgate.net/publication/397823961_Electron_densities_from_S_II_lines_significantly_overestimate_the_impact_of_ionised_AGN_outflows/fulltext/691fd76519b35058639be580/Electron-densities-from-S-II-lines-significantly-overestimate-the-impact-of-ionised-AGN-outflows.pdf?origin=scientificContributions
- arxiv.org [2511.15791] Electron densities from [S II] lines significantly overestimate the impact of ionised AGN outflows - arXiv Opens in a new window — https://arxiv.org/abs/2511.15791
- eprints.whiterose.ac.uk Multiphase characterization of AGN winds in five local type-2 quasars Opens in a new window — https://eprints.whiterose.ac.uk/id/eprint/210731/1/aa47715-23.pdf
- arxiv.org [2310.17939] JWST Reveals Widespread AGN-Driven Neutral Gas Outflows in Massive z ~ 2 Galaxies - arXiv Opens in a new window — https://arxiv.org/abs/2310.17939
- orcid.org Yijia Li - ORCID Opens in a new window — https://orcid.org/0000-0002-0682-3310
- durham.ac.uk Dr Rohit Kondapally - Durham University Opens in a new window — https://www.durham.ac.uk/staff/rohit-kondapally/
- durham.ac.uk Emmy Escott - Durham University Opens in a new window — https://www.durham.ac.uk/staff/emily-l-escott/
- orcid.org Marina Arnaudova - ORCID Opens in a new window — https://orcid.org/0000-0002-1128-0592
- academic.oup.com Volume 536 Issue 2 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/issue/536/2
- research.si.edu JWST reveals widespread AGN-driven neutral gas outflows in massive z 2 galaxies Opens in a new window — https://research.si.edu/publication-details/?id=177669
- experts.colorado.edu <i>JWST</i> reveals widespread AGN-driven neutral gas outflows in massive z ∼ 2 galaxies | CU Experts Opens in a new window — https://experts.colorado.edu/display/pubid_373001
- researchgate.net Simulating Jet-Feedback on Kpc Scales: A Review - ResearchGate Opens in a new window — https://www.researchgate.net/publication/391660843_Simulating_Jet-Feedback_on_kpc_Scales_A_Review
- uhra.herts.ac.uk Items where Author is "Holden, Luke" - University of Hertfordshire Research Archive Opens in a new window — https://uhra.herts.ac.uk/view/creators/Holden=3ALuke=3A=3A.html
- researchprofiles.herts.ac.uk Luke Holden - University of Hertfordshire (Research Profiles) Opens in a new window — https://researchprofiles.herts.ac.uk/en/persons/luke-holden/
- home.ifa.hawaii.edu Evolution of the Perturbed Spiral Galaxy NGC 1385 - Institute for Astronomy Opens in a new window — https://home.ifa.hawaii.edu/users/kud/research_papers/evo_5.pdf
- researchprofiles.herts.ac.uk Unlocking the Full Potential of SKAO Extra-galactic Science with High-multiplex Optical Spectroscopy - University of Hertfordshire (Research Profiles) Opens in a new window — https://researchprofiles.herts.ac.uk/files/80365168/2606.24744v1.pdf
- ricerca.sns.it GA-NIFS: Dissecting the multiple sub-structures and probing their complex interactions in the Lyα emitter galaxy CR7 at z = 6.6 - Scuola Normale Superiore Opens in a new window — https://ricerca.sns.it/bitstream/11384/164424/1/aa52994-24.pdf
- edoc.ub.uni-muenchen.de Distribution and Evolution of Molecular Gas in Galaxies Opens in a new window — https://edoc.ub.uni-muenchen.de/35969/1/Bollo_Doizi_Victoria.pdf
- researchgate.net Clump-like Structures in High-Redshift Galaxies: Mass Scaling and Radial Trends from JADES - ResearchGate Opens in a new window — https://www.researchgate.net/publication/400003097_Clump-like_Structures_in_High-Redshift_Galaxies_Mass_Scaling_and_Radial_Trends_from_JADES
- researchgate.net (PDF) Searching for Quiescent Galaxies over $3 < z < 6$ in JWST Surveys Using Manifold Learning - ResearchGate Opens in a new window — https://www.researchgate.net/publication/388081095_Searching_for_Quiescent_Galaxies_over_3_z_6_in_JWST_Surveys_Using_Manifold_Learning
- academic.oup.com Non-parametric attenuation curves in local star-forming galaxies: geometry effect, dust evolution, and intermediate-scale structures | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/545/2/staf2082/8341074
- researchgate.net MUSE-ALMA Haloes: XII. Molecular gas in z ∼ 0.5 H I – selected galaxies - ResearchGate Opens in a new window — https://www.researchgate.net/publication/400079306_MUSE-ALMA_Haloes_XII_Molecular_gas_in_z_05_H_I_-_selected_galaxies
- digital.csic.es J-HERTz: J-PLUS Heritage Exploration of Radio Targets at z $<$ 5 - Digital CSIC Opens in a new window — https://digital.csic.es/bitstream/10261/431174/1/2026ApJS..282...20F.pdf
- academic.oup.com The JWST EXCELS survey: the ages and abundances of 3 < z < 5 massive quiescent galaxies show that downsizing - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/doi/10.1093/mnras/stag827/68201502/stag827.pdf
- infoscience.epfl.ch Rapid, out-of-equilibrium metal enrichment indicated by a flat mass-metallicity relation at z ∼ 6 from NIRCam grism spectrosco Opens in a new window — https://infoscience.epfl.ch/bitstreams/c12a7e02-2b14-4744-ba22-b32809ac57f9/download
- arxiv.org SHELLQs. Bridging the Gap: JWST Unveils Obscured Quasars in the Most Luminous Galaxies at z > 6 - arXiv Opens in a new window — https://arxiv.org/pdf/2505.04825
- academic.oup.com Learning the Universe: cosmological and astrophysical parameter inference with galaxy luminosity functions and colours - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/544/4/3949/65049966/staf1888.pdf
- researchgate.net (PDF) The Cepheid Bias: Resolving the Hubble Tension - ResearchGate Opens in a new window — https://www.researchgate.net/publication/399664279_The_Cepheid_Bias_Resolving_the_Hubble_Tension
- researchgate.net THE EVOLUTION OF GALAXY NUMBER DENSITY AT z < 8 AND ITS IMPLICATIONS | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/305321948_THE_EVOLUTION_OF_GALAXY_NUMBER_DENSITY_AT_z_8_AND_ITS_IMPLICATIONS
- researchgate.net (PDF) BASS. XXXV. The M BH–σ* Relation of 105 Month Swift-BAT Type 1 AGNs Opens in a new window — https://www.researchgate.net/publication/374523673_BASS_XXXV_The_M_BH-s_Relation_of_105_Month_Swift-BAT_Type_1_AGNs
- research.rug.nl Possible environmental quenching in an interacting little red dot pair at z ∼ 7 - the University of Groningen research portal Opens in a new window — https://research.rug.nl/files/1381939447/aa53943-25.pdf
- arxiv.org Low-hard to high-soft spectral state transitions in the faintest early X-ray-detected optical tidal disruption event TDE 2025aarm - arXiv Opens in a new window — https://arxiv.org/html/2607.09850v1
- academic.oup.com Lord of LRDs: insights into a 'Little Red Dot' with a low-ionization spectrum at z = 0.1 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/545/3/staf2235/8382487
- researchgate.net (PDF) HECATEv2: An all-sky galaxy catalogue for multimessenger astrophysics Opens in a new window — https://www.researchgate.net/publication/402860682_HECATEv2_An_all-sky_galaxy_catalogue_for_multimessenger_astrophysics
- research.chalmers.se A z ≃ 0.4 Galaxy Reflecting the High-redshift Little Red Dots: An Extended Starburst with an Overmassive Black Hole - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/551007/file/551007_Fulltext.pdf
- academic.oup.com JWST EXCELS survey: the ages and abundances of 3 < z < 5 massive quiescent galaxies show that downsizing was already in place by z ≃ 4 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/549/1/stag827/8666392
- arxiv.org The JWST LEGGOS Survey – LEnsing and Galaxy Growth: Observing Substructures - arXiv Opens in a new window — https://arxiv.org/html/2606.20845v1
- research.iac.es Lord of LRDs: Insights into a "Little Red Dot" with a low-ionization spectrum at z = 0.1 - Instituto de Astrofísica de Canarias • IAC Opens in a new window — https://research.iac.es/preprints/files/PP26014.pdf
- arxiv.org arXiv:2407.00157v3 [astro-ph.GA] 25 Jan 2025 Opens in a new window — https://arxiv.org/pdf/2407.00157
- homepages.usm.uni-muenchen.de Everything from Nothing – Of Haloes and Voids Opens in a new window — https://homepages.usm.uni-muenchen.de/halos/theses/MA_seidel_benjamin.pdf
- bo.astro.it OU5: E-ELT MOS Opens in a new window — http://www.bo.astro.it/premiale.elt/sesto_2015_talks/Sesto_garilli.pdf
- oamonitor.ireland.openaire.eu Physics of Prodigious Lyman Continuum Leakers Opens in a new window — https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.3847%2F2041-8213%2Fab6560
- thesis.caltech.edu Unveiling the Structure of Active Galactic Nuclei with Hard X-ray Spectroscopy Opens in a new window — https://thesis.caltech.edu/10294/13/thesis_170606.pdf
- researchgate.net Luke R. Holden's research works | University of Hertfordshire and other places - ResearchGate Opens in a new window — https://www.researchgate.net/scientific-contributions/Luke-R-Holden-2240742221
- researchgate.net Patricia BESSIERE | PostDoc Position | Ph.D in Astronomy | Instituto de Astrofísica de Canarias, Santa Cruz de Tenerife | IAC | Department of Astrophysics Research | Research profile - ResearchGate Opens in a new window — https://www.researchgate.net/profile/Patricia-Bessiere
- alphaxiv.org Electron densities from [S II] lines significantly overestimate the Opens in a new window — https://www.alphaxiv.org/abs/2511.15791
- scispace.com Observational Tests of Active Galactic Nuclei Feedback: An Overview of Approaches and Interpretation - SciSpace Opens in a new window — https://scispace.com/papers/observational-tests-of-active-galactic-nuclei-feedback-an-1nvqpsbamd
- en.wikipedia.org 4C 61.23 - Wikipedia Opens in a new window — https://en.wikipedia.org/wiki/4C_61.23
- academic.oup.com Quasar Feedback Survey: revealing the importance of sensitive radio imaging for AGN identification deeper into the radio-quiet regime - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/546/4/stag097/8427327
- orcid.org Gabriela Canalizo - ORCID Opens in a new window — https://orcid.org/0000-0003-4693-6157
- zenodo.org QSOFEED: Relationship between star formation and active galactic nuclei feedback Opens in a new window — https://zenodo.org/records/11965868
- arxiv.org Kinematic detection of dusty outflows from active galactic nuclei: Polycyclic aromatic hydrocarbon kinematics of type 2 quasars with JWST/MIRI spectroscopy - arXiv Opens in a new window — https://arxiv.org/html/2606.28311v2
- scholar.google.com ‪Blessing Musiimenta‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=L-4gWEsAAAAJ&hl=en
- research.iac.es Cristina Ramos Almeida » QSOFEED - Instituto de Astrofísica de Canarias • IAC Opens in a new window — https://research.iac.es/galeria/cristina.ramos.almeida/qsofeed/
- researchgate.net Blessing MUSIIMENTA | PostDoc Position | Doctor of Philosophy | National Institute of Astrophysics, Rome | INAF | Research profile - ResearchGate Opens in a new window — https://www.researchgate.net/profile/Blessing-Musiimenta
- orcid.org Luke R Holden - ORCID Opens in a new window — https://orcid.org/0000-0002-1721-1918
- orcid.org Iván Ezequiel López - ORCID Opens in a new window — https://orcid.org/0000-0003-4687-8401
- scispace.com (PDF) Gap opening in protoplanetary discs: gas dynamics from Opens in a new window — https://scispace.com/papers/gap-opening-in-protoplanetary-discs-gas-dynamics-from-global-3bq6ad9u
- scispace.com Three-temperature radiation hydrodynamics with PLUTO. Tests and Opens in a new window — https://scispace.com/papers/three-temperature-radiation-hydrodynamics-with-pluto-tests-4vin3w4wxn
- academic.oup.com Dusty substructures induced by planets in ALMA discs: how dust growth and dynamics changes the picture - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/536/4/3322/7932351
- edoc.ub.uni-muenchen.de Modeling Dust Evolution in Hydrodynamic Simulations of Protoplanetary Disks - Elektronische Hochschulschriften der LMU München Opens in a new window — https://edoc.ub.uni-muenchen.de/33346/1/Pfeil_Thomas.pdf
- academic.oup.com Modelling shadows in scattered light observations as signals from companions in protoplanetary discs | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/540/4/3186/8157926
- arxiv.org Combined dispersion relation for Goldreich-Schubert-Fricke Instability and Convective Overstability in disks around young stars - arXiv Opens in a new window — https://arxiv.org/html/2404.15933v1

## Reference-only safety receipt

- advisory_only: true
- No `.tex` edit or auto-apply is authorized or performed by this lane.
- No DB, API, wiki, trust, autopilot-lane, deploy, git, publish, cron, billing, account-setting, credential, secret, bulk-history, or unrelated-conversation mutation is authorized or performed. Exact-owned conversation cleanup is authorized only after verified packet save.
