You are the Deep Research reviewer for NebulaMind manuscript paper_09, round 1. This is a REFERENCE-ONLY, advisory-only review and re-research task.

Hard boundary:
- NEVER edit or rewrite a `.tex` file, database, wiki, trust record, autopilot lane, deployment, git state, account setting, or source artifact.
- Return research and revision advice only. Tori/WonE own every manuscript revision.
- Use real astronomical observations and real simulation literature only. Do not invent data, citations, identifiers, or findings.
- Preserve every measured number in the supplied draft exactly. Audit it; do not recompute or replace it.
- Treat every result as selection-conditional association, never causal feedback evidence.
- A citation is usable only if its DOI, arXiv identifier, ADS bibcode, or stable publisher record resolves to the same authors/title/year. Mark any mismatch unusable; do not silently repair ambiguity.
- Prefer 2023--2025 sources where they add value, but retain older foundational sources when they are the strongest fit. Skip anything unverifiable.
- Do not perform or request a narration reread.

Round-1 candidate SHA-256: `b42a9a128e5d12b0eb59906e9bb9cafb4a752b04224aab46060389c888a2d756`
Round-1 source receipt SHA-256: `d8015ac76f754418a97c9bca13903c5721b9e035b047a12d9199123bae3d9e71`
Writer recorded original-line preservation: `True`

Sources added by the writers in round 1:
- key=schaye2023 | citation= | identifier=DOI:10.1093/mnras/stad2419 | role= | verification=
- key=bose2023 | citation= | identifier=DOI:10.1093/mnras/stad1097 | role= | verification=
- key=kugel2023 | citation= | identifier=DOI:10.1093/mnras/stad2540 | role= | verification=

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

----- BEGIN ROUND1 TEX paper_09 -----
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS target vector for feedback-model validation}
\shortauthors{NebulaMind local integration}
\begin{document}

\title{SDSS target vector for feedback-model validation: selection-aware SDSS optical proxy integration}
\author{NebulaMind Research Autopilot}
\affiliation{Local reproducible integration run; public SDSS DR17 data only}

\begin{abstract}
We integrate the active proposal 'Forward-modelled validation of cosmological feedback prescriptions' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Purpose and claim contract}\label{sec:purpose}
This draft preserves the active proposal title, 'Forward-modelled validation of cosmological feedback prescriptions', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.

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
The consolidated proposal question is: What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item The pilot writes 15 mass-redshift cells with n >= 50 as a compact validation vector.
\item Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.
\item The output is an observed target vector for simulation forward modelling, not a direct simulation comparison.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.

Simulation suites and mock-observation methods define the future comparison problem; no simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,imanga2023,donnari2021,dubois2013,dubois2016}.


\subsection{Literature Context and Missing Observables}

Simulation validation requires mock-observer forward modelling through this exact optical selection; raw intrinsic simulated values are not like-for-like \citep{schaye2023}. Large-volume and calibrated hydrodynamical suites motivate future validation but do not become measurements of the SDSS cells \citep{bose2023}. The 15-cell optical vector remains selection-conditional and cannot uniquely identify a feedback mechanism \citep{kugel2023}.

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

\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
\bibitem[Dubrois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
\bibitem[Dubrois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Schaye et al.(2023)]{schaye2023} Schaye, J., Kugel, R., Schaller, M., et al. 2023, MNRAS, 526, 4978
\bibitem[Bose et al.(2023)]{bose2023} Bose, S., Hadzhiyska, B., Eisenstein, D.~J., et al. 2023, MNRAS, 524, 2579
\bibitem[Kugel et al.(2023)]{kugel2023} Kugel, R., Schaye, J., Schaller, M., et al. 2023, MNRAS, 526, 6103
\end{thebibliography}

\end{document}

----- END ROUND1 TEX paper_09 -----
