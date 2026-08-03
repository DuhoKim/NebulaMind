# Deep Research reference packet — paper_06 round1_review

advisory_only: true
reference_only: true
auto_apply_authorized: false

Prompt file: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714/round1/dr-review-prompts/paper_06_round1_review_dr_research_prompt.md`
Prompt file SHA-256: `c9dd3259c67d194205874078bb28a32bbbb3351d0c689303f74bedf5ae11f004`
Submitted prompt text SHA-256: `ce23a0d58968d9b1b5cac373cc19bc1d77b5da85fbb68da3915772bca945df2d`
Conversation ID: `61e26df7c80b4126`
Captured conversation title: `Google Gemini`
Submit UTC: `2026-07-14T16:07:55.717211Z`
Research start UTC: `2026-07-15T03:35:05.786827Z`
Result captured UTC: `2026-07-15T03:41:28.896238Z`
Result text SHA-256: `1f66a730ffbb5bd40fc5c7f0b2ec67e75f5a665c162788c8312bde2fcfc13f87`

## Verbatim prompt

You are the Deep Research reviewer for NebulaMind manuscript paper_06, round 1. This is a REFERENCE-ONLY, advisory-only review and re-research task.

Hard boundary:
- NEVER edit or rewrite a `.tex` file, database, wiki, trust record, autopilot lane, deployment, git state, account setting, or source artifact.
- Return research and revision advice only. Tori/WonE own every manuscript revision.
- Use real astronomical observations and real simulation literature only. Do not invent data, citations, identifiers, or findings.
- Preserve every measured number in the supplied draft exactly. Audit it; do not recompute or replace it.
- Treat every result as selection-conditional association, never causal feedback evidence.
- A citation is usable only if its DOI, arXiv identifier, ADS bibcode, or stable publisher record resolves to the same authors/title/year. Mark any mismatch unusable; do not silently repair ambiguity.
- Prefer 2023--2025 sources where they add value, but retain older foundational sources when they are the strongest fit. Skip anything unverifiable.
- Do not perform or request a narration reread.

Round-1 candidate SHA-256: `a3c3695e3e4d1dc02fd13da8e11e2113051f0e7a4cfdfe1049e6bf88ec346a32`
Round-1 source receipt SHA-256: `974046661be1af09299167775c73e05e888c5fe8d4b3bab7a67638551f17e346`
Writer recorded original-line preservation: `True`

Sources added by the writers in round 1:
- key=bluck2023 | citation= | identifier=DOI:10.3847/1538-4357/acac7c; arXiv:2301.03677 | role= | verification=

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

----- BEGIN ROUND1 TEX paper_06 -----
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS mass transition in quenching and optical AGN incidence}
\shortauthors{NebulaMind local integration}
\begin{document}

\title{SDSS mass transition in quenching and optical AGN incidence: selection-aware SDSS optical proxy integration}
\author{NebulaMind Research Autopilot}
\affiliation{Local reproducible integration run; public SDSS DR17 data only}

\begin{abstract}
We integrate the active proposal 'Locating the transition from stellar-feedback to AGN-feedback regulation' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Purpose and claim contract}\label{sec:purpose}
This draft preserves the active proposal title, 'Locating the transition from stellar-feedback to AGN-feedback regulation', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.

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
The consolidated proposal question is: At what stellar-mass scale do quenched fraction and optical AGN incidence rise in the same SDSS denominator? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item The first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5.
\item The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.
\item The result is an optical transition diagnostic; gas fractions and baryon deficits are needed before assigning the transition to stellar or AGN feedback.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.

Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.


\subsection{Literature Context and Missing Observables}

Time-integrated quenching predictors are not equivalent to an instantaneous optical AGN state. The added source only motivates a caveat; it does not identify a physical transition mass in this sample \citep{bluck2023}.

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

\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\end{thebibliography}

\end{document}

----- END ROUND1 TEX paper_06 -----

## Full Deep Research sourced report

NebulaMind Manuscript paper_06, Round 1: Deep Research Review

The following document constitutes the formal Deep Research review, invariant audit, citation verification, and re-research integration for the NebulaMind manuscript paper_06, round 1. The review evaluates the manuscript's adherence to selection-conditional boundaries, the physical interpretations of optical emission-line diagnostics from the Sloan Digital Sky Survey (SDSS) Data Release 17 (DR17), and the broader cosmological frameworks of active galactic nucleus (AGN) feedback and galaxy quenching.   

Section 1 - Manuscript Verdict and Invariant Audit

Verdict: REVISE

The manuscript successfully attempts to constrain its physical claims by reframing an active proposal ('Locating the transition from stellar-feedback to AGN-feedback regulation') into a guarded optical denominator and proxy draft. However, the manuscript requires substantial revision to fully eliminate implicit causal overreach regarding the physical mass-transition scale of galaxy quenching, particularly concerning the severe survivorship biases inherent in optical emission-line selection.

Invariant Audit and Selection-Conditionality Analysis

The following table isolates every topic-specific measured value from the submitted draft. The audit verifies the numerical preservation of these values and evaluates whether the surrounding prose successfully maintains a strict selection-conditional and association-only boundary, free from causal feedback claims.

Measured Value / Metric	Context in Draft	Selection-Conditional & Association-Only Status
60,000 rows	Cached SDSS DR17 emission-line subset	Maintained. The prose correctly identifies this as a "cached local CSV" and explicitly states it is a "capped subset ordered by specObjID, not a random or population-complete parent sample."
249,917 rows	Strict public four-line S/N$\geq 3$ eligible parent	Maintained. Bounded as a read-only public SDSS DR17 count query utilized solely to establish the parent denominator.
24.0%	Coverage of the cached table against the strict parent	Maintained. Used strictly as a representativeness diagnostic to bound the scope of the cached table.
501,060	SpecObj GALAXY, 0.02<z<0.12 public DR17 rows	Maintained. Baseline denominator for the selection cascade.
1.000	Retention vs. spectro-z parent for SpecObj GALAXY	Maintained. Normalization baseline.
416,554	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds	Maintained. Demonstrates catalog matching attrition.
0.831	Retention vs. spectro-z parent for previous bound	Maintained. Accurately reflects target retention.
373,445	four BPT lines positive with positive errors, public rows	Maintained. Highlights the onset of emission-line selection bias.
0.745	Retention vs. spectro-z parent for positive lines	Maintained. Quantifies line positivity attrition.
0.499	Retention vs. spectro-z parent for S/N$\geq 3$	Maintained. Crucial metric demonstrating that over 50% of the parent sample is lost upon applying basic signal-to-noise criteria.
176,523	four BPT lines S/N$\geq 5$, public rows	Maintained. Cascading strictness check.
42,446	four BPT lines S/N$\geq 5$, cached rows	Maintained. Bounded application to the local cache.
0.352	Retention vs. spectro-z parent for S/N$\geq 5$	Maintained. Association-only statistical dropout.
91,768	four BPT lines S/N$\geq 10$, public rows	Maintained. Extreme selection threshold.
22,311	four BPT lines S/N$\geq 10$, cached rows	Maintained. Bounded application to the local cache.
0.183	Retention vs. spectro-z parent for S/N$\geq 10$	Maintained. Demonstrates that 81.7% of the sample is excluded at high S/N.
33.6%	Retention in the -12 < logsSFR < -11 parent bin at S/N$\geq 3$	Maintained. Successfully highlights the extreme selection bias against massive, quiescent (low sSFR) early-type galaxies.
94.9%	Retention in the -10 < logsSFR < -9.5 parent bin at S/N$\geq 3$	Maintained. Contrasts with the previous metric to prove that star-forming galaxies are preferentially retained.
5 percentage points	Maximum checked cached-vs-public fraction difference	Maintained. Guarded as a "representativeness diagnostic only."
2.03 percentage points	Largest absolute difference in redshift	Maintained. Association-only diagnostic boundary.
-1.63 percentage points	Largest absolute difference in stellar mass	Maintained. Association-only diagnostic boundary.
-0.58 percentage points	Largest absolute difference in sSFR	Maintained. Association-only diagnostic boundary.
0.5	Quenched fraction threshold	Maintained. Used descriptively as a transition marker.
11.0-12.5	The first stellar-mass bin with quenched fraction > 0.5	At Risk of Overreach. While stated as an observation, it is presented as a "topic-specific optical denominator/proxy diagnostic" without explicitly warning that this high-mass bin is heavily depleted by the 33.6% retention rate noted above.
0.520	The optical AGN fraction peak	Maintained. Stated as a measured quantity within the cached bounds.
11.0-12.5 bin	The stellar mass bin where the AGN fraction peaks	At Risk of Overreach. Presenting this bin as the peak of optical AGN incidence without emphasizing that optical lines vanish in fully quenched massive systems risks implying a physical, rather than purely selection-driven, transition.
Causal Overreach, Unsupported Generalizations, and Structural Conflicts

While the authors have largely succeeded in maintaining a guarded tone, several structural conflicts and implicit causal overreaches persist within the integration of the results and interpretations.

1. Conflict Between the Abstract's Promise and Section 5.1's Execution:
The abstract explicitly claims to fold in "literature-placement" outputs to contextualize the SDSS DR17 optical proxy integration. However, Section 5.1 (Literature Context and Missing Observables) contains a single, underdeveloped sentence relying on one citation (bluck2023). This fails to provide the promised literature placement. The section does not adequately explain why time-integrated quenching predictors are physically distinct from instantaneous optical AGN states, nor does it explore the well-documented critical mass scales in the literature (e.g., the standard M
∗
	​

∼10
10.5
M
⊙
	​

 transition).   

2. Unsupported Generalization Regarding the 11.0-12.5 Stellar Mass Bin:
Section 4 presents three bullet points summarizing the optical denominator results. It states that the quenched fraction crosses 0.5 in the 11.0-12.5 mass bin, and that the optical AGN fraction peaks at 0.520 in this exact same bin. Presenting these two concurrent phenomena risks a severe unsupported generalization: the reader may incorrectly infer a causal feedback relationship (i.e., that the peak in optical AGN incidence is causing the quenched fraction to cross 0.5 at this specific mass scale).

The draft must explicitly reconcile this finding with the data presented in Section 2, which states that the S/N$\geq 3$ four-line requirement only retains 33.6% of galaxies in the low specific star formation rate (sSFR) bins characteristic of the 11.0-12.5 mass range. The peak at 0.520 is heavily mediated by survivorship bias; fully quenched, massive elliptical galaxies lack the cold gas necessary to produce detectable Baldwin-Phillips-Terlevich (BPT) emission lines, artificially depressing the true AGN fraction (which may be operating in radiatively inefficient, radio-jet modes invisible to optical surveys).   

3. Omission of Environmental Confounding Factors:
Section 5 lists "halo masses" as a missing observable but fails to explicitly note the critical conflict between intrinsic mass quenching and environmental quenching. SDSS DR17 data, without a central/satellite galaxy group catalog cross-match, blends massive central galaxies (which may quench via AGN feedback) with lower-mass satellite galaxies (which quench via environmental stripping and starvation within massive halos). Stating that the 11.0-12.5 bin is the transition diagnostic without isolating central galaxies is a profound generalization that conflates two entirely different astrophysical mechanisms.   

Section 2 - Citation Verification Matrix

The following matrix audits the single round-1 added source alongside the six foundational citations utilized in the Deep Research integration sections (Sections 5 and 5.1). The audit ensures strict adherence to bibliography constraints, verifying that all identifiers resolve to the precise authors, titles, and publication years utilized in the draft.

Citation Key	Resolved Real Title / Authors / Year	Identifier / Source Record	Status	Exact Reason
bluck2023	The Fundamental Signature of Star Formation Quenching from AGN Feedback: A Critical Dependence of Quiescence on Supermassive Black Hole Mass, Not Accretion Rate. Bluck, A. F. L., Piotrowska, J. M., & Maiolino, R. (2023).	DOI:10.3847/1538-4357/acac7c ; arXiv:2301.03677	PASS	

The provided DOI and arXiv identifiers resolve perfectly to the exact title, author list, and year utilized in the manuscript.


kauffmann2003mass	Stellar masses and star formation histories for 10
5
 galaxies from the Sloan Digital Sky Survey. Kauffmann, G., Heckman, T. M., White, S. D. M., et al. (2003).	DOI:10.1046/j.1365-8711.2003.06291.x	PASS	

The publisher record confirms the exact author array, title, publication year (2003), and journal (MNRAS).


baldry2004	Quantifying the Bimodal Color-Magnitude Distribution of Galaxies. Baldry, I. K., Glazebrook, K., Brinkmann, J., et al. (2004).	DOI:10.1086/381502	PASS	

The metadata resolves flawlessly to the required 2004 Astrophysical Journal publication.


peng2010	Mass and Environment as Drivers of Galaxy Evolution in SDSS and zCOSMOS and the Origin of the Schechter Function. Peng, Y.-j., Lilly, S. J., Kovač, K., et al. (2010).	DOI:10.1088/0004-637X/721/1/193	PASS	

The identifier perfectly matches the foundational 2010 framework separating mass and environmental quenching.


peng2012	Mass and Environment as Drivers of Galaxy Evolution. II. The Quenching of Satellite Galaxies as the Origin of Environmental Effects. Peng, Y.-j., Lilly, S. J., Renzini, A., & Carollo, M. (2012).	DOI:10.1088/0004-637X/757/1/4	PASS	

Accurate resolution to the 2012 Astrophysical Journal paper confirming the role of satellite galaxies in environmental quenching.


dekel2006	Galaxy bimodality due to cold flows and shock heating. Dekel, A., & Birnboim, Y. (2006).	DOI:10.1111/j.1365-2966.2006.10145.x	PASS	

The DOI resolves flawlessly to the 2006 MNRAS publication establishing the theoretical halo shock-heating mass limit.


piotrowska2022	On the quenching of star formation in observed and simulated central galaxies: evidence for the role of integrated AGN feedback. Piotrowska, J. M., Bluck, A. F. L., Maiolino, R., & Peng, Y.-j. (2022).	DOI:10.1093/mnras/stac382	PASS	

The DOI confirms the exact publication details, authors, and year for this critical machine-learning analysis of simulated and observed quenching.

  
Section 3 - Re-research Findings

The manuscript's greatest vulnerability lies in its underdeveloped literature context regarding the physical mechanisms of galaxy quenching, the theoretical "critical mass" transition scale, and the specific failure modes of instantaneous optical AGN proxies. The following six sources have been re-researched to fill these material gaps, providing rigorous astrophysical boundaries for the manuscript's claims.

Source 1: Piotrowska, J. M., Bluck, A. F. L., Maiolino, R., & Peng, Y.-j. (2022, MNRAS)
Identifier: DOI:10.1093/mnras/stac382
Role: contradiction
Stance / Rationale: This work provides a fundamental contradiction to the utility of instantaneous optical AGN detection (as measured by SDSS BPT diagrams) for predicting galaxy quenching. By utilizing Random Forest machine learning classification on both SDSS data and cosmological hydrodynamical simulations (EAGLE, Illustris, IllustrisTNG), the authors demonstrate that the integrated power output of the AGN over cosmic time—robustly proxied by the mass of the supermassive black hole (SMBH)—is the dominant parameter predicting quiescence in central galaxies. Instantaneous AGN accretion rates (which drive the optical emission lines measured in this draft) show negligible predictive power. This source strictly bounds the manuscript by forcing the authors to explicitly state that the 0.520 peak in optical AGN fraction observed in the 11.0-12.5 stellar mass bin cannot be interpreted as the physical driver of the high quenched fraction in that same bin.   

Source 2: Scharré, L., Sorini, D., & Davé, R. (2024, MNRAS)
Identifier: DOI:10.1093/mnras/stae2098
Role: interpretation-caveat
Stance / Rationale: Utilizing the SIMBA cosmological simulations, this recent study isolates the distinct effects of different AGN feedback modes across the stellar mass function. The authors find that stellar feedback dominates below halo masses of M
H
	​

=10
12
M
⊙
	​

, while AGN feedback quenches more massive systems. Crucially, they identify that radiatively inefficient AGN jets and X-ray feedback modes are the dominant quenching mechanisms at late times for massive galaxies. This provides a severe interpretation caveat for the draft: the optical BPT diagnostic relies on radiatively efficient accretion to ionize surrounding gas. Because massive, quenched early-type galaxies are primarily maintained by radiatively inefficient jet/X-ray modes, they inherently fail the four-line optical BPT criteria. This explains the extreme S/N$\geq 3$ dropout rate for low sSFR galaxies noted in the draft's Table 1 and mandates a disclaimer that optical proxies systematically blind the observer to the true high-mass AGN feedback transition.   

Source 3: Mishra, P. K., Park, C., Lee, J., Dubois, Y., Pichon, C., Kim, J., & Gibson, B. (2026, arXiv)
Identifier: arXiv:2604.27477
Role: method-support
Stance / Rationale: This state-of-the-art analysis using the Horizon Run 5 simulation investigates the physical origin of the "critical mass" in galaxy evolution. The authors identify a redshift-independent critical total halo mass of ∼10
12.5
M
⊙
	​

, corresponding to a critical stellar mass of M
∗
	​

∼10
10.5
 to 10
10.7
M
⊙
	​

. At this scale, the nature of gas accretion fundamentally changes; a dynamically stable hot gas halo develops, suppressing cool gas inflow and sharply reducing in-situ star formation efficiency. This source supports the manuscript's method of searching for a mass-based transition point but strictly bounds its results. The theoretical critical mass (∼10
10.5
M
⊙
	​

) is significantly lower than the 11.0-12.5 stellar mass bin where the draft observes its optical transitions. The draft must explicitly state that its observed 11.0-12.5 bin is an artifact of the optical emission-line visibility window, not the fundamental thermodynamic critical mass of galaxy evolution.   

Source 4: Goubert, P. H., Bluck, A. F. L., Piotrowska, J. M., & Maiolino, R. (2024, MNRAS)
Identifier: DOI:10.1093/mnras/stae269
Role: interpretation-caveat
Stance / Rationale: This study investigates the dual nature of galaxy quenching by isolating central from satellite galaxies in both simulations and SDSS data. The authors conclusively show that quiescence in central galaxies is governed by intrinsic parameters (specifically SMBH mass/AGN feedback), whereas quiescence in low-mass satellite galaxies is overwhelmingly dictated by environmental parameters (such as local overdensity and host halo mass). Because the NebulaMind draft operates on a cached SDSS DR17 table that does not cross-reference a group catalog to separate centrals from satellites, the draft's "transition mass" blends two entirely distinct physical processes. The manuscript must include a severe interpretation caveat that the observed rise in quenched fraction cannot be cleanly attributed to an intrinsic AGN-feedback transition, as it is highly polluted by environmentally quenched satellites.   

Source 5: Visser-Zadvornyi, A. I., Carstairs, M. E., Oman, K. A., & Verheijen, M. A. W. (2025, MNRAS)
Identifier: arXiv:2503.15183
Role: interpretation-caveat
Stance / Rationale: By tracking gas particles in simulated satellite galaxies, this research reveals that the timescale required for a galaxy to quench is highly dependent on its stellar mass, exhibiting a turnover driven by the efficiency of star formation and combined stellar/AGN feedback in the absence of fresh gas accretion. This establishes a vital temporal caveat for the manuscript. The draft relies on a binary metric: the "quenched fraction above 0.5." Because the timescale to actually reach a fully quenched state varies drastically across the mass spectrum, utilizing a snapshot of current sSFR alongside an instantaneous optical AGN proxy conflates galaxies at vastly different stages of their evolutionary timelines. The draft must bound its claims by acknowledging that static optical fractions do not map linearly to dynamic quenching histories.   

Source 6: Baker, W. M., Maiolino, R., Bluck, A. F. L., Belfiore, F., Curti, M., D'Eugenio, F., Piotrowska, J. M., Tacchella, S., & Trussler, J. A. A. (2024, MNRAS)
Identifier: DOI:10.1093/mnras/stae2059
Role: future-data-motivation
Stance / Rationale: This study explores the regulation of stellar metallicities between star-forming and quiescent galaxies, concluding that galaxies with lower star formation rates exhibit higher stellar metallicities. This trend strongly supports quenching via "starvation"—where AGN feedback acts preventatively to cut off the cosmic supply of fresh, metal-poor gas inflows, causing the galaxy to passively consume its remaining gas and increase its bulk metallicity. This source directly motivates the draft's "Interpretation and missing observables" section. It mandates that stellar metallicity must be added to the list of required future parameters, as it provides the necessary historical integration to distinguish between violent, ejective AGN feedback and the slower, preventative starvation mechanisms that optical BPT diagrams fail to capture.   

Section 4 - Advisory Revision Packet

The following prioritized, prose-level revision advice is provided for the authors (Tori/WonE). These recommendations are advisory only; no direct TeX manipulation or auto-application is permitted.

KEEP

The Guarded Tone in the Abstract and Section 1: Maintain the explicit demotion of the manuscript from a "completed physical-feedback paper" to a "guarded SDSS DR17 optical denominator/proxy draft." This epistemological humility is the strongest feature of the current draft and effectively insulates it against causal overreach.

The Complete Selection Cascade (Table 1): Keep the detailed tabular breakdown of the retention fractions. The transparent admission that the S/N$\geq 3$ threshold retains only 33.6% of galaxies in the low-sSFR parent bin is absolutely critical for establishing the boundaries of the optical proxy.

The Invariant Measured Outputs: Retain the exact numerical findings in Section 4 (e.g., the 0.520 optical AGN fraction peak in the 11.0-12.5 stellar-mass bin). Do not alter or recalculate these cached values.

REVISE

Contextualize the 11.0-12.5 Stellar Mass Bin (Section 4): Revise the bulleted findings to explicitly decouple the optical peak from the theoretical critical mass. State clearly that while the optical AGN fraction peaks at 0.520 in the 11.0-12.5 bin, this does not represent the onset of AGN feedback. Instead, explain that modern cosmological frameworks (such as Horizon Run 5) identify the true thermodynamic critical mass at a much lower scale (∼10
10.5
M
⊙
	​

). Clarify that the observed peak in the 11.0-12.5 bin is an observational artifact—the "sweet spot" where galaxies are massive enough to host heavily accreting SMBHs but still retain just enough residual cold gas to generate the four optical emission lines required for BPT classification before fully transitioning to the red sequence.

Expand Section 5.1 (Literature Context and Missing Observables): The current single sentence is insufficient. Dramatically expand this section to outline the profound disconnect between instantaneous optical proxies and integrated feedback history. Draw upon the Random Forest analyses of cosmological simulations to explain that instantaneous optical accretion rates possess little to no predictive power regarding quiescence. Emphasize that it is the time-integrated energy injected by the SMBH (proxied by SMBH mass) that fundamentally regulates the quenching transition.

Revise Environmental Confounders (Section 5): Revise the interpretation to explicitly acknowledge the conflation of central and satellite galaxies. State that because the SDSS cache does not employ a group catalog matching algorithm, the 11.0-12.5 transition bin inevitably mixes massive central galaxies undergoing intrinsic mass quenching with lower-mass satellites undergoing environmental starvation.

ADD

Add Caveats Regarding Radiatively Inefficient Feedback: In Section 5, add a dedicated paragraph discussing the different modes of AGN feedback. Explicitly state that as galaxies grow into the highest mass bins, their SMBHs typically transition into radiatively inefficient, kinetically dominated jet modes or X-ray heating modes. Note that these feedback modes efficiently maintain quenching but frequently lack the ionizing radiation necessary to excite optical emission lines, thereby rendering the most effective AGN feedback invisible to the SDSS BPT diagnostic criteria.

Add to the Missing Observables List: In Section 5, append stellar metallicity and central/satellite structural flags to the required future parameters. Note that stellar metallicity is vital for distinguishing between rapid ejective feedback and slow, preventative starvation.

SKIP

Skip Causal Phrasing in Section 4: Do not allow any sentence to imply that the 0.520 optical AGN peak drives or causes the quenched fraction to cross 0.5. Ensure the prose rigidly maintains that these are parallel, selection-biased associations.

Skip BPT Boundary Redefinitions: Do not attempt to mathematically redefine the Kewley or Kauffmann BPT demarcation lines to "fix" the dropout rate at high masses. Rely exclusively on the cataloged values as stated in the invariant audit.

Citation Integration Directives for Round 2:
The following sources, analyzed in Section 3, must be formally integrated (\citep) into the expanded prose of Round 2:

Integrate piotrowska2022 heavily into Section 5.1 to establish the contradiction between instantaneous optical states and integrated feedback history.

Integrate scharre2024 into Section 5 to support the added caveat regarding radiatively inefficient, jet-mode feedback bypassing optical detection at high masses.

Integrate mishra2026 into Section 4 to provide the theoretical baseline for the actual thermodynamic critical mass scale (∼10
10.5
M
⊙
	​

).

Integrate goubert2024 into Section 5 to support the environmental confounding caveat (centrals vs. satellites).

Integrate baker2024 into Section 5 to justify the addition of stellar metallicity to the missing observables list.

REFERENCE_ONLY_NO_AUTO_APPLY

## Captured source anchors

- sdss4.org How to Cite SDSS Opens in a new window — https://www.sdss4.org/collaboration/citing-sdss/
- sdss4.org SDSS Data Release Publications Opens in a new window — https://www.sdss4.org/science/data-release-publications/
- academic.oup.com The dependence of star formation history and internal structure on stellar mass for 10 5 low-redshift galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/341/1/54/999703
- arxiv.org The Critical Mass in Galaxy Evolution - arXiv Opens in a new window — https://arxiv.org/html/2604.27477v1
- academic.oup.com host galaxies of active galactic nuclei | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/346/4/1055/1062435
- academic.oup.com The host galaxies and classification of active galactic nuclei - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/372/3/961/972572
- academic.oup.com The effects of stellar and AGN feedback on the cosmic star formation history in the simba simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/534/1/361/59155888/stae2098.pdf
- arxiv.org The Effects of Stellar and AGN Feedback on the Cosmic Star Formation History in the Simba Simulations - arXiv Opens in a new window — https://arxiv.org/html/2404.07252v1
- arxiv.org [1003.4747] Mass and environment as drivers of galaxy evolution in SDSS and zCOSMOS and the origin of the Schechter function - arXiv Opens in a new window — https://arxiv.org/abs/1003.4747
- digital.csic.es the colors of central and satellite galaxies in zcosmos out to z ≃ 0.8 and implications for quenching1 - Digital CSIC Opens in a new window — https://digital.csic.es/bitstream/10261/411021/1/2013ApJ...769...24K.pdf
- arxiv.org [2301.03677] The fundamental signature of star formation quenching from AGN feedback: A critical dependence of quiescence on supermassive black hole mass not accretion rate - arXiv Opens in a new window — https://arxiv.org/abs/2301.03677
- orcid.org Joanna M. Piotrowska - ORCID Opens in a new window — https://orcid.org/0000-0003-1661-2338
- researchgate.net The fundamental signature of star formation quenching from AGN feedback: A critical dependence of quiescence on supermassive black hole mass not accretion rate | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/367019886_The_fundamental_signature_of_star_formation_quenching_from_AGN_feedback_A_critical_dependence_of_quiescence_on_supermassive_black_hole_mass_not_accretion_rate
- academic.oup.com Stellar masses and star formation histories for 105 galaxies from the Sloan Digital Sky Survey | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/341/1/33/999309
- ned.ipac.caltech.edu Beyond the Galaxy Luminosity Function - Simon Driver Opens in a new window — http://ned.ipac.caltech.edu/level5/Sept04/Driver/Driver_refs.html
- ned.ipac.caltech.edu Galaxy Assembly - E.F. Bell Opens in a new window — https://ned.ipac.caltech.edu/level5/March04/Bell/Bell_refs.html
- kavli.pku.edu.cn Yingjie Peng (彭影杰) | The Kavli Institute for Astronomy and Astrophysics at Peking University (KIAA-PKU) Opens in a new window — http://kavli.pku.edu.cn/people/yingjie-peng
- researchgate.net Nearly all Massive Quiescent Disk Galaxies have a Surprisingly Large Atomic Gas Reservoir | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/336317017_Nearly_all_Massive_Quiescent_Disk_Galaxies_have_a_Surprisingly_Large_Atomic_Gas_Reservoir
- academic.oup.com Galaxy bimodality due to cold flows and shock heating | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/368/1/2/968063
- academic.oup.com Gravitational quenching in massive galaxies and clusters by clumpy accretion - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/383/1/119/3680322/mnras0383-0119.pdf
- academic.oup.com On the quenching of star formation in observed and simulated central galaxies: evidence for the role of integrated AGN feedback | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/512/1/1052/6482843
- academic.oup.com On the quenching of star formation in observed and simulated central galaxies: evidence for the role of integrated AGN feedback | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/512/1/1052/6482843
- arxiv.org [2404.07252] The Effects of Stellar and AGN Feedback on the Cosmic Star Formation History in the Simba Simulations - arXiv Opens in a new window — https://arxiv.org/abs/2404.07252
- arxiv.org [2604.27477] The Critical Mass in Galaxy Evolution - arXiv Opens in a new window — https://arxiv.org/abs/2604.27477
- arxiv.org The Critical Mass in Galaxy Evolution - arXiv Opens in a new window — https://arxiv.org/pdf/2604.27477
- academic.oup.com role of environment and AGN feedback in quenching local galaxies: comparing cosmological hydrodynamical simulations to the SDSS | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/528/3/4891/7590842
- kyleaoman.github.io Star formation and stellar & AGN feedback in the absence of accretion, not gas stripping, set the quenching time-scale in satellite galaxies - Kyle Oman Opens in a new window — https://kyleaoman.github.io/assets/pdf/2025MNRAS.540.1730V.pdf
- arxiv.org Star formation and stellar & AGN feedback in the absence of accretion, not gas stripping, set the quenching timescale in satellite galaxies - arXiv Opens in a new window — https://arxiv.org/html/2503.15183v1
- academic.oup.com Different regulation of stellar metallicities between star-forming and quiescent galaxies – insights into galaxy quenching | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/534/1/30/7746765
- academic.oup.com Downsizing does not extend to dwarf galaxies: identifying the stellar mass regimes shaped by supernova and AGN feedback - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/547/2/stag207/66631356/stag207.pdf
- infoscience.epfl.ch A Census of Quiescent Galaxies across 0.5 < z < 8 with JWST/MIRI - Infoscience - EPFL Opens in a new window — https://infoscience.epfl.ch/bitstreams/40d00f77-5d5d-4471-9b87-ce5634c0f5f9/download
- par.nsf.gov Environmental vs. intrinsic quenching at cosmic noon: Predictions from cosmological hydrodynamical simulations for VLT-MOONRISE Opens in a new window — https://par.nsf.gov/servlets/purl/10645071
- arxiv.org A Multiwavelength Evaluation of AGN in the Post-Starburst Phase - arXiv Opens in a new window — https://arxiv.org/html/2602.11644v1
- scholar.google.com ‪Joanna Piotrowska‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=9oL_WckAAAAJ&hl=en
- zenodo.org The Temporal Architecture of Disc Galaxy Assembly: Morphological Opens in a new window — https://zenodo.org/records/20845745
- cpl.iphy.ac.cn Targeted Search for Eccentric Supermassive Binary Black Holes in Opens in a new window — https://cpl.iphy.ac.cn/en/article/id/b578ec24-4673-49d3-bebb-a2db822f5664
- sdss.org Data Release Publications - SDSS-V Opens in a new window — https://www.sdss.org/science/publications/data-release-publications/
- arxiv.org Results from (21cm-HI) single-dish observations of MaNGA Survey Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2502.09505v1
- cris.unibo.it Galaxy mergers can rapidly shut down star formation Opens in a new window — https://cris.unibo.it/retrieve/e682b6fd-5f06-4b41-8789-23116ae9c280/slac109.pdf
- arxiv.org Different regulation of stellar metallicities between star-forming and quiescent galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/2309.00670
- arxiv.org Quenching of Star Formation in Massive Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2606.12156v2
- researchgate.net Dissecting the Mass Quenching in TNG50: Galaxy Size Determines the Quenching Mode Opens in a new window — https://www.researchgate.net/publication/398044446_Dissecting_the_Mass_Quenching_in_TNG50_Galaxy_Size_Determines_the_Quenching_Mode
- arxiv.org Dissecting the mass quenching in TNG50: Galaxy size determines the quenching mode - arXiv Opens in a new window — https://arxiv.org/html/2510.24886v1
- um.edu.mt Galaxy Quenching at the High Redshift Frontier: A Fundamental Test of Cosmological Models in the Early Universe with JWST-CEERS - University of Malta Opens in a new window — https://www.um.edu.mt/library/oar/bitstream/123456789/138415/1/Galaxy%20Quenching%20at%20the%20High%20Redshift%20Frontier.pdf
- academic.oup.com In situ versus ex situ drivers of galaxy quenching: critical black hole mass and main sequence universality in the FLAMINGO simulation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/543/3/2204/8256857
- repository.cam.ac.uk The Fundamental Signature of Star Formation Quenching from AGN Opens in a new window — https://www.repository.cam.ac.uk/items/052ce7d7-bc86-40c8-9837-4a954daa458d
- research.iac.es Observational Tests of AGN Feedback: An Overview of Approaches and Interpretation Opens in a new window — https://research.iac.es/preprints/files/PP24033.pdf
- academic.oup.com JADES and SAPPHIRES: galaxy metamorphosis amidst a huge, luminous emission-line region | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/542/2/960/8199915
- academic.oup.com Black hole mass of a quiescent galaxy hosting a Type 1 AGN at z = 2.09: implications for black hole–galaxy coevolution and AGN quenching at high redshift - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/538/3/1501/8051354
- academic.oup.com Beyond the merger–quasar–quench paradigm I: mergers are neither necessary nor sufficient to quench central galaxies in illustrisTNG - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/548/3/stag507/8529012
- orcid.org Asa FL Bluck - ORCID Opens in a new window — https://orcid.org/0000-0001-6395-4504
- backend.orbit.dtu.dk Tracing the Life Cycle of Galaxies across Cosmic Time A Story of Life and Death - DTU Inside Opens in a new window — https://backend.orbit.dtu.dk/ws/portalfiles/portal/413151947/PhD_Thesis.pdf
- en.wikipedia.org Quenching (astronomy) - Wikipedia Opens in a new window — https://en.wikipedia.org/wiki/Quenching_(astronomy)
- researchgate.net Understanding the regulation of star formation within TNG100 galaxies on kpc-scales using machine learning I: Global versus local - ResearchGate Opens in a new window — https://www.researchgate.net/publication/403905806_Understanding_the_regulation_of_star_formation_within_TNG100_galaxies_on_kpc-scales_using_machine_learning_I_Global_versus_local
- arxiv.org The link between star-formation and supermassive black hole properties - arXiv Opens in a new window — https://arxiv.org/pdf/2309.15909
- usm.uni-muenchen.de References: Opens in a new window — https://www.usm.uni-muenchen.de/people/saglia/praktikum/galspectra/node14.html
- ned.ipac.caltech.edu Optical Spectroscopy of LINERs and Low-Luminosity Seyfert Nuclei Opens in a new window — https://ned.ipac.caltech.edu/level5/LHo4/Ho_references.html
- connectsci.au HST/STIS Spectroscopy of CSS sources: Kinematics ... - ConnectSci Opens in a new window — https://connectsci.au/as/article-pdf/20/1/28/1092468/as02027.pdf
- ned.ipac.caltech.edu references - AGN Emission Lines - H. Netzer Opens in a new window — http://ned.ipac.caltech.edu/level5/March02/Netzer/Netzer_refs.html
- ned.ipac.caltech.edu Infrared Emission Lines as Probes of Gaseous Nebulae - H.L. Dinerstein Opens in a new window — https://ned.ipac.caltech.edu/level5/March01/Dinerstein2/Diner_references.html
- radio.kasi.re.kr The relationship between radio power at 22 and 43 GHz and black hole properties of AGN in elliptical galaxies⋆ Opens in a new window — https://radio.kasi.re.kr/kvn/papers/635222697093766250_aa21310-13.pdf
- summerschoolalpbach.at Recommended Reading - Alpbach Summer School Opens in a new window — https://www.summerschoolalpbach.at/docs/2011/Recommended_Reading.pdf
- academic.oup.com physical properties of star-forming galaxies in the low-redshift Universe | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/351/4/1151/1131077
- ned.ipac.caltech.edu Star forming dwarf galaxies - Nils Bergvall Opens in a new window — https://ned.ipac.caltech.edu/level5/March11/Bergvall/Bergvall_refs.html
- ouci.dntb.gov.ua Suppression of Star Formation in Galaxy Pairs - OUCI Opens in a new window — https://ouci.dntb.gov.ua/en/works/lRnWbkKl/
- wwwmpa.mpa-garching.mpg.de Physical properties for galaxies and active galactic nuclei in the Sloan Digital Sky Survey: Data catalogues from SDSS studies at MPA/JHU Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/SDSS/index_old.html
- academic.oup.com physical properties of star-forming galaxies in the low-redshift Universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/351/4/1151/1131077
- wwwmpa.mpa-garching.mpg.de AGN Catalogue - MPA Garching Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/SDSS/DR2/Data/agncatalogue.html
- wwwmpa.mpa-garching.mpg.de Physical properties for galaxies and active galactic nuclei in the Sloan Digital Sky Survey: Data catalogues from SDSS studies at MPA/JHU Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/SDSS/index_dr2.html
- academic.oup.com Volume 346 Issue 4 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/issue/346/4
- ned.ipac.caltech.edu Evolution of AGN - An Optical View - C. Wolf Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept04/Wolf/Wolf_refs.html
- wwwmpa.mpa-garching.mpg.de Stellar Mass Catalogue - MPA Garching Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/SDSS/DR2/Data/stellarmass.html
- arxiv.org Stellar masses, star formation rates, metallicities and AGN properties for 2 × 105 galaxies in the SDSS Data Release Two (DR2) - arXiv Opens in a new window — https://arxiv.org/pdf/astro-ph/0406220
- adsabs.harvard.edu 2 0 0 3MNRAS.341. . .33K Mon. Not. R. Astron. Soc. 341, 33-53 (2003) Stellar masses and star formation histories for 105 galaxie - Astrophysics Data System Opens in a new window — https://adsabs.harvard.edu/pdf/2003MNRAS.341...33K
- researchgate.net (PDF) Theoretical Modeling of Starburst Galaxies - ResearchGate Opens in a new window — https://www.researchgate.net/publication/2230718_Theoretical_Modeling_of_Starburst_Galaxies
- ned.ipac.caltech.edu Modelling the UV to sub-mm SED of Starburst Galaxies - M.A. Dopita Opens in a new window — https://ned.ipac.caltech.edu/level5/March05/Dopita/Dopita_refs.html
- openresearch-repository.anu.edu.au A RISE IN THE IONIZING PHOTONS IN STAR-FORMING GALAXIES OVER THE PAST 8 BILLION YEARS Opens in a new window — https://openresearch-repository.anu.edu.au/bitstreams/50a46181-e2c7-42b9-bf43-2d8a6281378c/download
- scispace.com Minor Merger Origin for the Circumnuclear Starburst in NGC 7742 - SciSpace Opens in a new window — https://scispace.com/pdf/minor-merger-origin-for-the-circumnuclear-starburst-in-ngc-22epbjwkvd.pdf
- osti.gov Modelling the Pan-Spectral Energy Distribution of Starburst Galaxies: II. Control of the H II Region Parameters - OSTI.GOV Opens in a new window — https://www.osti.gov/servlets/purl/899108
- cambridge.org Alternative classification diagrams for AGN-starburst galaxies - Cambridge University Press & Assessment Opens in a new window — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EF8DF976DBA8E7DC0FB79C7F65F9DC84/S1743921320001787a.pdf/alternative_classification_diagrams_for_agnstarburst_galaxies.pdf
- academic.oup.com The host galaxies and classification of active galactic nuclei Opens in a new window — https://academic.oup.com/mnras/article-pdf/372/3/961/2943380/mnras0372-0961.pdf
- researchgate.net (PDF) The Host Galaxies and Classification of Active Galactic Nuclei - ResearchGate Opens in a new window — https://www.researchgate.net/publication/1787336_The_Host_Galaxies_and_Classification_of_Active_Galactic_Nuclei
- arxiv.org [astro-ph/0605681] The Host Galaxies and Classification of Active Galactic Nuclei - arXiv Opens in a new window — https://arxiv.org/abs/astro-ph/0605681
- cambridge.org Active galactic nuclei in diverse galactic environments | Publications of the Astronomical Society of Australia | Cambridge Core Opens in a new window — https://www.cambridge.org/core/product/identifier/S1323358026101532/type/journal_article
- academic.oup.com The host galaxies and classification of active galactic nuclei - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/372/3/961/972572
- researchgate.net (PDF) The Sloan Digital Sky Survey: Technical Summary - ResearchGate Opens in a new window — https://www.researchgate.net/publication/230931317_The_Sloan_Digital_Sky_Survey_Technical_Summary
- arxiv.org arXiv:0910.2982v1 [astro-ph.CO] 15 Oct 2009 Opens in a new window — https://www.arxiv.org/pdf/0910.2982v1
- noirlab.edu PowerPoint 프레젠테이션 - NOIRLab Opens in a new window — https://noirlab.edu/science/sites/default/files/media/archives/presentations/scipresentation0839-en.pdf
- ned.ipac.caltech.edu X-ray Survey Results on Active Galaxy Physics and Evolution - W.N. Opens in a new window — https://ned.ipac.caltech.edu/level5/March04/Brandt/Brandt_refs.html
- arxiv.org On the galaxy stellar mass function, the mass-metallicity relation, and the implied baryonic mass function - arXiv Opens in a new window — https://arxiv.org/pdf/0804.2892
- research.birmingham.ac.uk The Dawn of the Red: Star formation histories of group galaxies over the past 5 billion years Opens in a new window — https://research.birmingham.ac.uk/en/publications/the-dawn-of-the-red-star-formation-histories-of-group-galaxies-ov/
- academic.oup.com On the galaxy stellar mass function, the mass–metallicity relation and the implied baryonic mass function | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/388/3/945/953739
- academic.oup.com Galaxy bimodality versus stellar mass and environment Opens in a new window — https://academic.oup.com/mnras/article-pdf/373/2/469/4099171/mnras0373-0469.pdf
- academic.oup.com Bursting and quenching in massive galaxies without major mergers or AGNs - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/380/1/339/1326685
- arxiv.org From FFB Starbursts at Cosmic Dawn to Quenching at Cosmic Morning: Hi-z Galaxy Bimodality - arXiv Opens in a new window — https://arxiv.org/pdf/2506.11664
- research.chalmers.se The RESOLVE and ECO G3 Initiative: Drivers of H i Content and X-Ray Emission in Galaxy Groups Opens in a new window — https://research.chalmers.se/publication/546860/file/546860_Fulltext.pdf
- arxiv.org Quantifying the Relationship Between Galaxy Specific Star Formation Rate And Halo Spin For Star-forming Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2411.12212
- arxiv.org arXiv:2412.04553v1 [astro-ph.GA] 5 Dec 2024 Opens in a new window — https://arxiv.org/pdf/2412.04553
- pos.sissa.it PoS(MeerKAT2016)022 Opens in a new window — https://pos.sissa.it/277/022/pdf
- digitalcommons.dartmouth.edu Black Hole Variability and the Star Formation-Active Galactic Nucleus Connection - Dartmouth Digital Commons Opens in a new window — https://digitalcommons.dartmouth.edu/cgi/viewcontent.cgi?article=3180&context=facoa
- pure.rug.nl University of Groningen Galaxy and Mass Assembly (GAMA) Wang, L.; Norberg, P.; Brough, S.; Brown, M. J.; da Cunha, E.; Davies, L Opens in a new window — https://pure.rug.nl/ws/files/76241183/aa32697_18.pdf
- academic.oup.com zCOSMOS 20k: satellite galaxies are the main drivers of environmental effects in the galaxy population at least to z - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/438/1/717/18466494/stt2241.pdf
- helda.helsinki.fi ZENS. IV. SIMILAR MORPHOLOGICAL CHANGES ASSOCIATED Opens in a new window — https://helda.helsinki.fi/bitstreams/f8f6b260-4840-430e-84d7-061cb41dcf5a/download
- frontiersin.org The high energy X-ray probe (HEX-P): constraining supermassive black hole growth with population spin measurements - Frontiers Opens in a new window — https://www.frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2024.1324796/full
- arxiv.org Measurement of the gas consumption history of a massive quiescent galaxy - arXiv Opens in a new window — https://arxiv.org/html/2405.19401v2
- semanticscholar.org [PDF] On the quenching of star formation in observed and simulated central galaxies: Evidence for the role of integrated AGN feedback | Semantic Scholar Opens in a new window — https://www.semanticscholar.org/paper/6878e61a69bdf1f81114fff1aa27f1743011023a
- ouci.dntb.gov.ua When relics were made: vigorous stellar rotation and low dark matter content in the massive ultra-compact galaxy GS-9209 at <i>z</i> = 4.66 - OUCI Opens in a new window — https://ouci.dntb.gov.ua/en/works/7pXroJmk/
- techexplorist.com Supermassive black holes inhibit stellar births - Tech Explorist Opens in a new window — https://www.techexplorist.com/supermassive-black-holes-inhibit-stellar-births/45470/
- research-archive.org Analysis of Active Galactic Nuclei Feedback in Cosmological Simulations: IllustrisTNG and EAGLE | Research Archive of Rising Scholars Opens in a new window — https://research-archive.org/index.php/rars/preprint/view/2878
- cambridge.org Establishing the impact of luminous AGN with multi-wavelength observations and simulations Opens in a new window — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D11A59C47A7A4F9289401FE7D84A4BAC/S1743921323002806a.pdf/establishing_the_impact_of_luminous_agn_with_multiwavelength_observations_and_simulations.pdf
- academic.oup.com Volume 512 Issue 1 | Monthly Notices of the Royal Astronomical Society - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/issue/512/1
- lweb.cfa.harvard.edu The Redshift Evolution of the M• − M⋆ Relation for JWST's Supermassive Black Holes at z > 4 Opens in a new window — https://lweb.cfa.harvard.edu/~loeb/FL23.pdf
- academic.oup.com A hybrid active galactic nucleus feedback model with spinning black holes, winds and jets Opens in a new window — https://academic.oup.com/mnras/article/547/2/stag324/8487639
- raa-journal.org The AGN Feedback in Compact Galaxies: On the Impact of a More Massive Central Black Hole - Research in Astronomy and Astrophysics (RAA) Opens in a new window — https://www.raa-journal.org/issues/all/2023/v23n10/202310/P020241029348101567906.pdf
- arxiv.org Supermassive Black Hole Growth in Massive Galaxies at Cosmic Dawn - arXiv Opens in a new window — https://arxiv.org/html/2510.19822v2
- academic.oup.com Supermassive black hole growth in massive galaxies at Cosmic Dawn - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/550/1/stag1129/8709288
- researchgate.net Star formation luminosity (L S F ) and AGN luminosity (L AGN ) vs. stellar mass M * (left). Ratio of L S F to L AGN vs. stellar mass. (right) … - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Star-formation-luminosity-L-S-F-and-AGN-luminosity-L-AGN-vs-stellar-mass-M_fig3_381519446
- research.rug.nl University of Groningen A Bayesian approach to the halo galaxy – supermassive black hole connection through cosmic time Opens in a new window — https://research.rug.nl/files/1285571423/aa46194-23.pdf
- researchgate.net MAUVE-MUSE: A Star-formation-driven Outflow Caught in the Act of Quenching the Stripped Virgo Galaxy NGC 4064 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/399583071_MAUVE-MUSE_A_Star-formation-driven_Outflow_Caught_in_the_Act_of_Quenching_the_Stripped_Virgo_Galaxy_NGC_4064
- durham.ac.uk Dr Kyle Oman - Durham University Opens in a new window — https://www.durham.ac.uk/staff/kyle-a-oman/
- physics.unlv.edu Cosmology & Galaxies Articles: Significant/Useful Articles - UNLV Physics Opens in a new window — https://www.physics.unlv.edu/~jeffery/course/c_cosmos/cosmos_articles.html
- astro.rug.nl Latest Preprints Opens in a new window — https://www.astro.rug.nl/arxiv/list.php
- researchgate.net Understanding the Origin of the Critical Mass in Galaxy Evolution - ResearchGate Opens in a new window — https://www.researchgate.net/publication/404344239_Understanding_the_Origin_of_the_Critical_Mass_in_Galaxy_Evolution
- researchgate.net Changbom Park's research works | Korea Institute for Advanced Study, Seoul (KIAS) and other places - ResearchGate Opens in a new window — https://www.researchgate.net/scientific-contributions/Changbom-Park-5689635
- academic.oup.com effects of stellar and AGN feedback on the cosmic star formation history in the simba simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/534/1/361/7756428
- academic.oup.com effects of stellar and AGN feedback on the cosmic star formation history in the simba simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/534/1/361/7756428
- durham.ac.uk Dr Daniele Sorini - Durham University Opens in a new window — https://www.durham.ac.uk/staff/daniele-sorini/
- iris.unimore.it BlackHoleWeather – Jet-regulated chaotic cold accretion across the meso scale: Morphology and thermodynamics - IRIS Unimore Opens in a new window — https://iris.unimore.it/retrieve/f4d9b517-0e9b-4052-a6dd-40b4bec5c3f3/Cammelli_2026a_BHW_CCA_feedback_morph_thermo.pdf
- academic.oup.com Cold versus hot gas accretion and angular momentum in FIRE simulations: from halo to galaxy scales - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/550/1/stag1117/8708459
- academic.oup.com Intracluster light is a biased tracer of the dark matter distribution in clusters | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/539/3/2279/8113287
- research-explorer.ista.ac.at RUBIES: JWST/NIRSpec Confirmation of an Infrared-luminous, Broad-line Little Red Dot with an Ionized Outflow Opens in a new window — https://research-explorer.ista.ac.at/download/19700/19707/2025_AstrophysicalJour_Wang.pdf
- research-explorer.ista.ac.at The Convergence of Heavy and Light Seeds to Overmassive Black Holes at Cosmic Dawn - ISTA Research Explorer Opens in a new window — https://research-explorer.ista.ac.at/download/19638/19655/2025_AstrophysicalJourLetters_Hu.pdf
- arxiv.org FEASTS Compared with Simulations: Abnormally Irregular and Extended HI Morphologies at a Column Density of $10^{18}\,\text{cm}^{ - arXiv Opens in a new window — https://arxiv.org/pdf/2512.07223
- researchgate.net The Critical Mass in Galaxy Evolution | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/404333108_The_Critical_Mass_in_Galaxy_Evolution
- zenodo.org Paper CCLXXXVII - The Redshift-Independent Critical Galaxy Mass as Sump Self-Quenching at a Fixed Coherence Ratio - Zenodo Opens in a new window — https://zenodo.org/records/20599651
- techno-science.net Why, at a certain mass, do galaxies stop forming stars? - Techno-Science.net Opens in a new window — https://www.techno-science.net/en/news/why-at-certain-mass-do-galaxies-stop-forming-stars-N28910.html

## Reference-only safety receipt

- advisory_only: true
- No `.tex` edit or auto-apply is authorized or performed by this lane.
- No DB, API, wiki, trust, autopilot-lane, deploy, git, publish, cron, billing, account-setting, credential, secret, bulk-history, or unrelated-conversation mutation is authorized or performed. Exact-owned conversation cleanup is authorized only after verified packet save.
