# codex-kun-cycle-6
Started UTC: 2026-07-09T03:37:07Z
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
session id: 019f44f3-5ef6-7242-8f87-a61908a4ed98
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_06.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

2026-07-09T03:37:08.487728Z ERROR rmcp::transport::worker: worker quit with fatal: unexpected server response: HTTP 503: upstream connect error or disconnect/reset before headers. retried and the latest reset reason: remote connection failure, transport failure reason: delayed connect error: Connection refused, when send initialized notification
codex
I’m inspecting the manuscript package for TeX, compile, figure, and reproducibility risks, with a specific pass on the numeric claims and any wording that could violate the association-only guardrail. I’ll read the core files and then give exact, safe edit recommendations for the integrator.
exec
/bin/zsh -lc "rg -n \"8,146|8146|-1\\.309|1\\.334|1\\.283|60,000|60000|249,917|249917|24\\.0%|24%|coverage|association|associate|only\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_06_REVIEW_RESPONSE.md:3:Changed safely in the candidate package only:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_06_REVIEW_RESPONSE.md:6:- Flagship abstract and Section 4 now say the comparison is between broad BPT-selected galaxies and star-forming controls, preserving the same 8,146 pair result and `-1.309 dex` median offset.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_06_REVIEW_RESPONSE.md:9:- Flagship interpretation now quotes the narrower-proxy reduction as `-1.309 dex` to `-0.763 dex` from Table 2, without changing the underlying numbers.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_06_REVIEW_RESPONSE.md:16:- Any causal-feedback, quenching, gas-depletion, or maintenance-heating claim beyond association-only or denominator/proxy wording.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_08_REVIEW_RESPONSE.md:6:- Reframed the flagship matched-result discussion to keep the association-only boundary while reiterating that the offset is fiber-centered.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_05_REVIEW_RESPONSE.md:6:- Added a short bridge in the interpretation section to keep the result explicitly at the denominator-level association boundary.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_05_REVIEW_RESPONSE.md:16:- No numeric values were changed, including 8,146 pairs, -1.309 dex, [-1.334,-1.283], 60,000 cached rows, 249,917 strict parent rows, or 24.0% coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:10:\affiliation{Public SDSS DR17 data only}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60k-row pilot cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities or luminosity functions. The arbitrary cap also means the sample cannot be normalized into absolute volume densities. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, so the known bulge/disk mismatch and 3-arcsec fiber aperture effect between BPT-selected hosts and star-forming controls can inflate the apparent offset. Broad low-ionization classes can also include LINER-like emission from retired stellar populations. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, consistent with contamination of the broad low-ionization class by Low-Ionization Nuclear Emission-line Region (LINER)-like emission from retired stellar populations, especially in massive bulges. Subclass and selection-function treatment must therefore precede any causal interpretation, and an accompanying supplementary denominator/proxy atlas collects the related baselines and missing-observable notes.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:27:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a capped 60k-row pilot cache selected sequentially by \texttt{specObjID} after an arbitrary pilot-query row limit; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the pilot cache covers 24.0\% of that strict parent. Because the cap is arbitrary and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:29:Because the 3-arcsec fiber samples only the central regions at low redshift, disk emission can be omitted and the catalog-derived total sSFR can be biased differently for bulge-dominated and disk-dominated systems.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:40:four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:41:four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:45:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:51:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical BPT galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:62:A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR within this fiber-centered matched comparison, but this manuscript does not convert that proxy offset into a global quenching threshold.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:70:Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:71:Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:72:Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:76:\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects systematic removal of the most quenched, bulge-dominated LINER-like systems, not just a random fluctuation. All values are conditional on the optical emission-line denominator.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:88:Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:90:At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including low-ionization nuclear emission-line region (LINER)-like ionization from retired stellar populations and post-AGB stars in massive bulges, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global quenching signal. The broad contamination primarily affects the broad low-ionization selection, which is why the narrower Seyfert-like proxy yields the smaller offset. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this capped 60k-row pilot cache. Any quenching-causality claim requires additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:93:RP-1 is best treated as a concise, selection-aware association paper, not a causal study. An accompanying supplementary denominator/proxy atlas holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex:94:In practice, that means future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_03_REVIEW_RESPONSE.md:4:- Tightened the flagship abstract and claim-boundary language to keep the result explicitly association-only and removed extra causal phrasing.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/PACKAGE_AUDIT.md:21:Safety: local decision package only; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/PACKAGE_MANIFEST_PRECOMPILE.json:24:  "safety": "local-only files under handoff tree; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes",
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_01_REVIEW_RESPONSE.md:6:- Strengthened the RP-1 matching and interpretation sections so the -1.309 dex offset is explicitly described as vulnerable to bulge-dominated versus disk-dominated structural mismatch, not just fiber coverage.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_01_REVIEW_RESPONSE.md:8:- Reframed the supplement abstract, purpose, and shared-denominator text so SDSS/BPT/catalog citations are clearly separated from radio/X-ray/CO/HI/outflow/simulation citations used only for future-data motivation.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_01_REVIEW_RESPONSE.md:14:- No numeric results, figure paths, table counts, or core association claims were changed.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:15:3. If approved, run a final prose-polish pass on RP-1 only, then recompile and audit.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:24:- RP-1 is the only current active paper with a direct, coherent SDSS row-level result strong enough for a short-paper draft.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:25:- The other 8 are useful, but they are not 8 independent causal physical-feedback papers with the current SDSS-only data.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:76:- Compile warnings: 10 AASTeX/line-break warnings only
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:84:- Main number: 8,146 matched pairs, median delta log sSFR = -1.309 dex, bootstrap interval [-1.334, -1.283] dex.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:85:- Guard: association only, not causal AGN feedback.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:86:- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:107:- Compile warnings: 19 AASTeX/line-break warnings only
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:159:1. Read the polished RP-1 PDF for scientific wording, especially whether the association-only claim is clear enough.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md:162:   - keep this package local only;
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_02_REVIEW_RESPONSE.md:5:- Updated the flagship abstract and conclusion to explicitly say the paper is an association-only result and that an accompanying supplementary denominator/proxy atlas carries the related baselines and missing-observable notes.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_02_REVIEW_RESPONSE.md:6:- Tightened the flagship matched-control caveat to state that the `-1.309 dex` offset is a relative fiber-aperture comparison, not a global quenching measurement.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_02_REVIEW_RESPONSE.md:8:- Revised the supplement abstract to state that the `60,000`-row cache is an arbitrary pilot-query cap, not a physical or volume-limited selection effect.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_02_REVIEW_RESPONSE.md:16:- I did not attempt to resolve the aperture-bias question, radio/X-ray maintenance-heating baseline, or any other issue that requires new observables beyond the current SDSS-only package.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_04_REVIEW_RESPONSE.md:3:Changed safely in the candidate package only:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_04_REVIEW_RESPONSE.md:6:- Flagship abstract and conclusion now say the result is an association paper, not a causal study, while preserving the same 8,146-pair result, `-1.309 dex` median offset, and `[-1.334,-1.283]` bootstrap interval.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_04_REVIEW_RESPONSE.md:18:- Any causal-feedback, quenching, gas-depletion, maintenance-heating, or outflow-escape claim beyond association-only or denominator/proxy wording.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_07_REVIEW_RESPONSE.md:3:Changed safely in the candidate package only:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_07_REVIEW_RESPONSE.md:8:- Flagship table caption and interpretation now keep the association-only boundary explicit while retaining the same `8,146` pairs, `-1.309 dex` median offset, and bootstrap interval.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_07_REVIEW_RESPONSE.md:9:- Supplement abstract now ends with an explicit atlas caveat: it provides observational baselines only and cannot confirm or refute feedback models without the missing observables.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/CYCLE_07_REVIEW_RESPONSE.md:16:- Any causal-feedback, quenching, gas-depletion, maintenance-heating, or outflow claim beyond association-only or denominator/proxy wording.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:10:\affiliation{Public SDSS DR17 data only}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:13:This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. These counts and fractions are conditional on the SDSS optical selection used here, not global volume-limited statistics, and the cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is a single follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:19:The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are therefore role-separated as future-data motivation, not validation of the present optical denominators. Keeping them in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:22:The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:34:four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:35:four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:39:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:45:This note isolates an internal environmental denominator that can later be joined to group catalogs and halo masses. Within this selection-biased emission-line denominator, the relative 10th-neighbor index covaries with the catalog low-sSFR fraction; this index is only an internal ordinal rank and does not map to physical environmental volume density or halo density. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the missing observables are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:53:Within this selection-biased emission-line cache, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:84:This note isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:139:This note compares optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:151:\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work, not a molecular or neutral gas census.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:212:These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.

exec
/bin/zsh -lc "sed -n '1,260p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/PACKAGE_AUDIT.md\"" in /Users/duhokim/NebulaMind/NebulaMind
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
/bin/zsh -lc "sed -n '1,260p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/FINAL_HANDOFF.md\"" in /Users/duhokim/NebulaMind/NebulaMind
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
I have the high-level package context. Next I’m checking the exact manuscript wording around the numbers and any phrases that drift from association-only into causal or mechanistic language, plus the compile log for structural TeX risks.
exec
/bin/zsh -lc "sed -n '1,220p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Selection-aware SDSS BPT/sSFR study}
\shortauthors{NebulaMind}
\begin{document}

\title{Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Study}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60k-row pilot cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities or luminosity functions. The arbitrary cap also means the sample cannot be normalized into absolute volume densities. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, so the known bulge/disk mismatch and 3-arcsec fiber aperture effect between BPT-selected hosts and star-forming controls can inflate the apparent offset. Broad low-ionization classes can also include LINER-like emission from retired stellar populations. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, consistent with contamination of the broad low-ionization class by Low-Ionization Nuclear Emission-line Region (LINER)-like emission from retired stellar populations, especially in massive bulges. Subclass and selection-function treatment must therefore precede any causal interpretation, and an accompanying supplementary denominator/proxy atlas collects the related baselines and missing-observable notes.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
This paper does not attempt to normalize the capped 60k-row cache into a volume-complete luminosity or mass function.

The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling.

The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a capped 60k-row pilot cache selected sequentially by \texttt{specObjID} after an arbitrary pilot-query row limit; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the pilot cache covers 24.0\% of that strict parent. Because the cap is arbitrary and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
Because the 3-arcsec fiber samples only the central regions at low redshift, disk emission can be omitted and the catalog-derived total sSFR can be biased differently for bulge-dominated and disk-dominated systems.
The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade for the flagship denominator. The 60k-row pilot cache is an artificial pilot-query cap, not a physical selection effect.\label{tab:selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.

\section{Classification and matching}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical BPT galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.

\begin{figure*}
\centering
\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
\label{fig:bpt}
\end{figure*}

\section{Matched-control result}
The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the broad BPT-selected galaxies relative to star-forming controls.
A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR within this fiber-centered matched comparison, but this manuscript does not convert that proxy offset into a global quenching threshold.
Because the comparison is fiber-centered and the matching ignores morphology, the measured offset is a relative difference between the broad-BPT and control samples within the fiber aperture; it will suffer from the known bulge/disk mismatch between broad-BPT hosts and star-forming controls and can therefore be inflated relative to a galaxy-wide suppression signal.

\begin{deluxetable*}{lrrrr}
\tabletypesize{\scriptsize}
\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
\startdata
Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
\enddata
\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects systematic removal of the most quenched, bulge-dominated LINER-like systems, not just a random fluctuation. All values are conditional on the optical emission-line denominator.}
\end{deluxetable*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT-selected galaxies minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
\label{fig:offsets}
\end{figure*}

\section{Interpretation}
The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper.
Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference.

At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including low-ionization nuclear emission-line region (LINER)-like ionization from retired stellar populations and post-AGB stars in massive bulges, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global quenching signal. The broad contamination primarily affects the broad low-ionization selection, which is why the narrower Seyfert-like proxy yields the smaller offset. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this capped 60k-row pilot cache. Any quenching-causality claim requires additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{Conclusion}
RP-1 is best treated as a concise, selection-aware association paper, not a causal study. An accompanying supplementary denominator/proxy atlas holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
In practice, that means future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.

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
/bin/zsh -lc "sed -n '1,260p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex\"" in /Users/duhokim/NebulaMind/NebulaMind
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
This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. These counts and fractions are conditional on the SDSS optical selection used here, not global volume-limited statistics, and the cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is a single follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are therefore role-separated as future-data motivation, not validation of the present optical denominators. Keeping them in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.

\section{Shared denominator}
The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing.

The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

\section{Atlas notes}

\subsection{Environment baseline: SDSS density proxy for low-sSFR incidence}
This note isolates an internal environmental denominator that can later be joined to group catalogs and halo masses. Within this selection-biased emission-line denominator, the relative 10th-neighbor index covaries with the catalog low-sSFR fraction; this index is only an internal ordinal rank and does not map to physical environmental volume density or halo density. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the missing observables are:
\begin{itemize}
\item group catalogues
\item robust central/satellite labels
\item halo masses
\item morphology
\item multi-redshift selection functions
\end{itemize}
Within this selection-biased emission-line cache, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement.
At the densest cluster cores, the SDSS 55-arcsec spectroscopic fiber-collision limit makes this proxy incomplete unless collision corrections are applied; no such correction is applied here.
These are still needed for a future environmental test \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor density proxy in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up, not a physical-feedback measurement.}
\label{fig:m1-rp2-environment-quenching}
\end{figure}


\subsection{Maintenance-heating denominator: optical AGN in massive SDSS hosts}
This note identifies the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can be used as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The missing observables are:
\begin{itemize}
\item X-ray cavity or cooling-luminosity measurements
\item radio jet powers
\item halo-selected parent catalogues
\item nondetection modelling
\end{itemize}
These are still needed for a future maintenance-heating test \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements, not a heating-to-cooling result.}
\label{fig:m1-rp3-maintenance-heating}
\end{figure}


\subsection{Outflow-kinematics denominator: high-excitation SDSS AGN}
This note isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are:
\begin{itemize}
\item resolved outflow velocities
\item halo potentials
\item molecular, ionized, and neutral gas phases
\item CGM recycling tracers
\end{itemize}
These are still needed for a future outflow test \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
\caption{SDSS optical emission-line denominator: the high-excitation AGN subset used to define an observational baseline for future resolved-kinematic measurements, not an escape or recycling result.}
\label{fig:m2-p1-outflow-escape-recycling}
\end{figure}


\subsection{Radio-jet environment baseline: optical AGN fraction vs. density proxy in massive hosts}
This note defines the environment-stratified optical denominator that future radio and X-ray work could test. The local-density proxy is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-density quartile has an optical AGN fraction of 0.509, while the low-density quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The missing observables are:
\begin{itemize}
\item radio jet morphology and age
\item cavity or shock energetics
\item hot-gas density
\item calibrated jet-power estimates
\end{itemize}
These are still needed for a future radio-jet test \citep{best2005,mcnamara2007,heckmanbest2014}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
\caption{SDSS optical emission-line denominator: the high- and low-density quartile comparison among massive SDSS hosts, used as a baseline for future radio-jet and X-ray work, not a coupling measurement.}
\label{fig:m2-p2-radio-jet-environment}
\end{figure}


\subsection{Mass-bin diagnostic: low-sSFR and optical AGN incidence}
This note pins down the mass bin where a future gas-inclusive study should look for an incidence change. We measure the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. What stellar-mass bin contains the highest representation of low-sSFR and optical AGN classifications within this selection-biased SDSS denominator? The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\). The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The missing observables are:
\begin{itemize}
\item gas fractions
\item baryon deficits
\item halo masses
\item stellar-feedback observables
\item high-redshift extensions
\end{itemize}
The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. In this optical-emission-line denominator, the 11.0--12.5 dex peak is most plausibly a selection-function artifact because the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and optical AGN incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up, not a physical transition-mass measurement. The 11.0--12.5 dex peak is a selection-function artifact in this emission-line cache, not a universal feedback threshold.}
\label{fig:m2-p3-feedback-transition-mass}
\end{figure}


\subsection{Tracer-threshold census for multiphase follow-up}
This note compares optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are:
\begin{itemize}
\item ionized, molecular, and neutral tracers
\item X-ray or radio tracers
\item a shared parent denominator
\item a consistent aperture model
\end{itemize}
These are still needed for a future multiphase test \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work, not a molecular or neutral gas census.}
\label{fig:m3-p1-multiphase-census}
\end{figure}


\subsection{Gas-depletion denominator: optical baseline for CO/HI follow-up}
This note defines the denominator for CO/HI gas-fraction and depletion-time follow-up. How many massive low-sSFR or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up? The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The missing observables are:
\begin{itemize}
\item CO or dust-based molecular gas masses
\item aperture-matched SFRs
\item morphology
\item environment labels
\end{itemize}
These are still needed for a future gas-fraction or depletion-time test \citep{xcoldgass2017,xgass2018,piotrowska2022}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
\caption{SDSS optical emission-line denominator: the massive low-sSFR SDSS galaxies available for CO/HI depletion-time follow-up, not a gas-depletion-efficiency measurement.}
\label{fig:m3-p2-gas-depletion-efficiency}
\end{figure}


\subsection{Simulation target vector for forward-model comparison}
This note provides a compact observed target vector for forward modelling, not a direct simulation comparison. What compact SDSS target vector of low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift can be used for forward-model comparison? The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The missing observables are:
\begin{itemize}
\item simulation mocks passed through the same optical S/N and fiber-aperture selection function used here, then through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions
\item aperture models
\item noise models
\end{itemize}
Without those matched selection steps, any simulation comparison is not a valid test. These are still needed for a future simulation-comparison test \citep{simba2019,tng2019,eagle2015}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
\caption{SDSS optical emission-line denominator: low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift in the SDSS emission-line sample. This is an observed target vector for forward modelling, not a direct simulation comparison.}
\label{fig:m3-p3-simulation-validation}
\end{figure}

\section{Atlas summary}
Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight notes. All eight notes are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or mock-observation data are added, so their present role is to organize follow-up rather than to establish causal physical claims.

\begin{deluxetable*}{llll}
\tabletypesize{\scriptsize}
\tablecaption{Atlas-level follow-up menu. Each row summarizes the present optical role and the missing observables needed before any physical inference.\label{tab:atlas-summary}}
\tablehead{\colhead{Topic} & \colhead{Observed baseline} & \colhead{Missing observables} & \colhead{Role}}
\startdata
Environment & low-sSFR vs.\ 10th-neighbor rank & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test \\
Maintenance heating & optical AGN in massive low-sSFR hosts & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
Outflow kinematics & high-excitation AGN subset & resolved velocities; halo potentials; multiphase gas; CGM tracers & kinematic follow-up \\
Env.\ jets & density-stratified AGN fraction & radio morphology/age; cavity energetics; hot-gas density & radio-jet follow-up \\
Mass bin & low-sSFR and AGN by $M_\star$ bin & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
Tracer census & tracer prevalence in 60k sample & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
Gas depletion & massive low-sSFR baseline; H$\alpha$ proxy & CO/dust gas masses; aperture-matched SFRs; morphology; environment & CO/HI follow-up \\
Simulation vector & mass-redshift target vector & mocks through SDSS/MaNGA/ALMA/X-ray/radio selection; aperture/noise models & forward model \\
\enddata
\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}


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
/bin/zsh -lc "sed -n '1,220p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log\"" in /Users/duhokim/NebulaMind/NebulaMind
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

codex
I’ve confirmed the core numbers are internally repeated consistently. I’m now pinning exact line numbers for the few places where the wording is closest to overclaiming, so the edit recommendations are concrete.
exec
/bin/zsh -lc "nl -ba \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex\" | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Selection-aware SDSS BPT/sSFR study}
     5	\shortauthors{NebulaMind}
     6	\begin{document}
     7	
     8	\title{Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Study}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60k-row pilot cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities or luminosity functions. The arbitrary cap also means the sample cannot be normalized into absolute volume densities. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, so the known bulge/disk mismatch and 3-arcsec fiber aperture effect between BPT-selected hosts and star-forming controls can inflate the apparent offset. Broad low-ionization classes can also include LINER-like emission from retired stellar populations. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, consistent with contamination of the broad low-ionization class by Low-Ionization Nuclear Emission-line Region (LINER)-like emission from retired stellar populations, especially in massive bulges. Subclass and selection-function treatment must therefore precede any causal interpretation, and an accompanying supplementary denominator/proxy atlas collects the related baselines and missing-observable notes.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}
    17	
    18	\section{Question and claim boundary}
    19	This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
    20	This paper does not attempt to normalize the capped 60k-row cache into a volume-complete luminosity or mass function.
    21	
    22	The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling.
    23	
    24	The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.
    25	
    26	\section{Data and shared selection}
    27	The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a capped 60k-row pilot cache selected sequentially by \texttt{specObjID} after an arbitrary pilot-query row limit; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the pilot cache covers 24.0\% of that strict parent. Because the cap is arbitrary and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
    28	Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
    29	Because the 3-arcsec fiber samples only the central regions at low redshift, disk emission can be omitted and the catalog-derived total sSFR can be biased differently for bulge-dominated and disk-dominated systems.
    30	The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.
    31	
    32	\begin{deluxetable*}{lrrr}
    33	\tabletypesize{\scriptsize}
    34	\tablecaption{Selection cascade for the flagship denominator. The 60k-row pilot cache is an artificial pilot-query cap, not a physical selection effect.\label{tab:selection}}
    35	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    36	\startdata
    37	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
    38	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
    39	plus galSpecLine join & 416,554 & -- & 83.1\% \\
    40	four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
    41	four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
    42	four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
    43	four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
    44	\enddata
    45	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies.}
    46	\end{deluxetable*}
    47	
    48	The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.
    49	
    50	\section{Classification and matching}
    51	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical BPT galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
    52	
    53	\begin{figure*}
    54	\centering
    55	\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
    56	\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
    57	\label{fig:bpt}
    58	\end{figure*}
    59	
    60	\section{Matched-control result}
    61	The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the broad BPT-selected galaxies relative to star-forming controls.
    62	A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR within this fiber-centered matched comparison, but this manuscript does not convert that proxy offset into a global quenching threshold.
    63	Because the comparison is fiber-centered and the matching ignores morphology, the measured offset is a relative difference between the broad-BPT and control samples within the fiber aperture; it will suffer from the known bulge/disk mismatch between broad-BPT hosts and star-forming controls and can therefore be inflated relative to a galaxy-wide suppression signal.
    64	
    65	\begin{deluxetable*}{lrrrr}
    66	\tabletypesize{\scriptsize}
    67	\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
    68	\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
    69	\startdata
    70	Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
    71	Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
    72	Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
    73	Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
    74	N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
    75	\enddata
    76	\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects systematic removal of the most quenched, bulge-dominated LINER-like systems, not just a random fluctuation. All values are conditional on the optical emission-line denominator.}
    77	\end{deluxetable*}
    78	
    79	\begin{figure*}
    80	\centering
    81	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    82	\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT-selected galaxies minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
    83	\label{fig:offsets}
    84	\end{figure*}
    85	
    86	\section{Interpretation}
    87	The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper.
    88	Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference.
    89	
    90	At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including low-ionization nuclear emission-line region (LINER)-like ionization from retired stellar populations and post-AGB stars in massive bulges, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global quenching signal. The broad contamination primarily affects the broad low-ionization selection, which is why the narrower Seyfert-like proxy yields the smaller offset. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this capped 60k-row pilot cache. Any quenching-causality claim requires additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
    91	
    92	\section{Conclusion}
    93	RP-1 is best treated as a concise, selection-aware association paper, not a causal study. An accompanying supplementary denominator/proxy atlas holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
    94	In practice, that means future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.
    95	
    96	\section{Local reproducibility}
    97	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
    98	
    99	
   100	\begin{thebibliography}{}
   101	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   102	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   103	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   104	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   105	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   106	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   107	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   108	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   109	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   110	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   111	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   112	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   113	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   114	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   115	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   116	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   117	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   118	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   119	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   120	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   121	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   122	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   123	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   124	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   125	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   126	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   127	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   128	\end{thebibliography}
   129	
   130	\end{document}

exec
/bin/zsh -lc "sed -n '1,220p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log\"" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "nl -ba \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex\" | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
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
    13	This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. These counts and fractions are conditional on the SDSS optical selection used here, not global volume-limited statistics, and the cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is a single follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}
    17	
    18	\section{Purpose}
    19	The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are therefore role-separated as future-data motivation, not validation of the present optical denominators. Keeping them in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.
    20	
    21	\section{Shared denominator}
    22	The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing.
    23	
    24	The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.
    25	
    26	\begin{deluxetable*}{lrrr}
    27	\tabletypesize{\scriptsize}
    28	\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
    29	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    30	\startdata
    31	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
    32	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
    33	plus galSpecLine join & 416,554 & -- & 83.1\% \\
    34	four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
    35	four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
    36	four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
    37	four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
    38	\enddata
    39	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
    40	\end{deluxetable*}
    41	
    42	\section{Atlas notes}
    43	
    44	\subsection{Environment baseline: SDSS density proxy for low-sSFR incidence}
    45	This note isolates an internal environmental denominator that can later be joined to group catalogs and halo masses. Within this selection-biased emission-line denominator, the relative 10th-neighbor index covaries with the catalog low-sSFR fraction; this index is only an internal ordinal rank and does not map to physical environmental volume density or halo density. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the missing observables are:
    46	\begin{itemize}
    47	\item group catalogues
    48	\item robust central/satellite labels
    49	\item halo masses
    50	\item morphology
    51	\item multi-redshift selection functions
    52	\end{itemize}
    53	Within this selection-biased emission-line cache, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement.
    54	At the densest cluster cores, the SDSS 55-arcsec spectroscopic fiber-collision limit makes this proxy incomplete unless collision corrections are applied; no such correction is applied here.
    55	These are still needed for a future environmental test \citep{peng2010,wetzel2013,dekel2006}.
    56	
    57	\begin{figure}
    58	\centering
    59	\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
    60	\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor density proxy in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up, not a physical-feedback measurement.}
    61	\label{fig:m1-rp2-environment-quenching}
    62	\end{figure}
    63	
    64	
    65	\subsection{Maintenance-heating denominator: optical AGN in massive SDSS hosts}
    66	This note identifies the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can be used as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The missing observables are:
    67	\begin{itemize}
    68	\item X-ray cavity or cooling-luminosity measurements
    69	\item radio jet powers
    70	\item halo-selected parent catalogues
    71	\item nondetection modelling
    72	\end{itemize}
    73	These are still needed for a future maintenance-heating test \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.
    74	
    75	\begin{figure}
    76	\centering
    77	\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
    78	\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements, not a heating-to-cooling result.}
    79	\label{fig:m1-rp3-maintenance-heating}
    80	\end{figure}
    81	
    82	
    83	\subsection{Outflow-kinematics denominator: high-excitation SDSS AGN}
    84	This note isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are:
    85	\begin{itemize}
    86	\item resolved outflow velocities
    87	\item halo potentials
    88	\item molecular, ionized, and neutral gas phases
    89	\item CGM recycling tracers
    90	\end{itemize}
    91	These are still needed for a future outflow test \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.
    92	
    93	\begin{figure}
    94	\centering
    95	\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
    96	\caption{SDSS optical emission-line denominator: the high-excitation AGN subset used to define an observational baseline for future resolved-kinematic measurements, not an escape or recycling result.}
    97	\label{fig:m2-p1-outflow-escape-recycling}
    98	\end{figure}
    99	
   100	
   101	\subsection{Radio-jet environment baseline: optical AGN fraction vs. density proxy in massive hosts}
   102	This note defines the environment-stratified optical denominator that future radio and X-ray work could test. The local-density proxy is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-density quartile has an optical AGN fraction of 0.509, while the low-density quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The missing observables are:
   103	\begin{itemize}
   104	\item radio jet morphology and age
   105	\item cavity or shock energetics
   106	\item hot-gas density
   107	\item calibrated jet-power estimates
   108	\end{itemize}
   109	These are still needed for a future radio-jet test \citep{best2005,mcnamara2007,heckmanbest2014}.
   110	
   111	\begin{figure}
   112	\centering
   113	\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
   114	\caption{SDSS optical emission-line denominator: the high- and low-density quartile comparison among massive SDSS hosts, used as a baseline for future radio-jet and X-ray work, not a coupling measurement.}
   115	\label{fig:m2-p2-radio-jet-environment}
   116	\end{figure}
   117	
   118	
   119	\subsection{Mass-bin diagnostic: low-sSFR and optical AGN incidence}
   120	This note pins down the mass bin where a future gas-inclusive study should look for an incidence change. We measure the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. What stellar-mass bin contains the highest representation of low-sSFR and optical AGN classifications within this selection-biased SDSS denominator? The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\). The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The missing observables are:
   121	\begin{itemize}
   122	\item gas fractions
   123	\item baryon deficits
   124	\item halo masses
   125	\item stellar-feedback observables
   126	\item high-redshift extensions
   127	\end{itemize}
   128	The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. In this optical-emission-line denominator, the 11.0--12.5 dex peak is most plausibly a selection-function artifact because the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold.
   129	
   130	\begin{figure}
   131	\centering
   132	\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
   133	\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and optical AGN incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up, not a physical transition-mass measurement. The 11.0--12.5 dex peak is a selection-function artifact in this emission-line cache, not a universal feedback threshold.}
   134	\label{fig:m2-p3-feedback-transition-mass}
   135	\end{figure}
   136	
   137	
   138	\subsection{Tracer-threshold census for multiphase follow-up}
   139	This note compares optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are:
   140	\begin{itemize}
   141	\item ionized, molecular, and neutral tracers
   142	\item X-ray or radio tracers
   143	\item a shared parent denominator
   144	\item a consistent aperture model
   145	\end{itemize}
   146	These are still needed for a future multiphase test \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.
   147	
   148	\begin{figure}
   149	\centering
   150	\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
   151	\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work, not a molecular or neutral gas census.}
   152	\label{fig:m3-p1-multiphase-census}
   153	\end{figure}
   154	
   155	
   156	\subsection{Gas-depletion denominator: optical baseline for CO/HI follow-up}
   157	This note defines the denominator for CO/HI gas-fraction and depletion-time follow-up. How many massive low-sSFR or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up? The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The missing observables are:
   158	\begin{itemize}
   159	\item CO or dust-based molecular gas masses
   160	\item aperture-matched SFRs
   161	\item morphology
   162	\item environment labels
   163	\end{itemize}
   164	These are still needed for a future gas-fraction or depletion-time test \citep{xcoldgass2017,xgass2018,piotrowska2022}.
   165	
   166	\begin{figure}
   167	\centering
   168	\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
   169	\caption{SDSS optical emission-line denominator: the massive low-sSFR SDSS galaxies available for CO/HI depletion-time follow-up, not a gas-depletion-efficiency measurement.}
   170	\label{fig:m3-p2-gas-depletion-efficiency}
   171	\end{figure}
   172	
   173	
   174	\subsection{Simulation target vector for forward-model comparison}
   175	This note provides a compact observed target vector for forward modelling, not a direct simulation comparison. What compact SDSS target vector of low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift can be used for forward-model comparison? The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The missing observables are:
   176	\begin{itemize}
   177	\item simulation mocks passed through the same optical S/N and fiber-aperture selection function used here, then through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions
   178	\item aperture models
   179	\item noise models
   180	\end{itemize}
   181	Without those matched selection steps, any simulation comparison is not a valid test. These are still needed for a future simulation-comparison test \citep{simba2019,tng2019,eagle2015}.
   182	
   183	\begin{figure}
   184	\centering
   185	\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
   186	\caption{SDSS optical emission-line denominator: low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift in the SDSS emission-line sample. This is an observed target vector for forward modelling, not a direct simulation comparison.}
   187	\label{fig:m3-p3-simulation-validation}
   188	\end{figure}
   189	
   190	\section{Atlas summary}
   191	Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight notes. All eight notes are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or mock-observation data are added, so their present role is to organize follow-up rather than to establish causal physical claims.
   192	
   193	\begin{deluxetable*}{llll}
   194	\tabletypesize{\scriptsize}
   195	\tablecaption{Atlas-level follow-up menu. Each row summarizes the present optical role and the missing observables needed before any physical inference.\label{tab:atlas-summary}}
   196	\tablehead{\colhead{Topic} & \colhead{Observed baseline} & \colhead{Missing observables} & \colhead{Role}}
   197	\startdata
   198	Environment & low-sSFR vs.\ 10th-neighbor rank & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test \\
   199	Maintenance heating & optical AGN in massive low-sSFR hosts & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
   200	Outflow kinematics & high-excitation AGN subset & resolved velocities; halo potentials; multiphase gas; CGM tracers & kinematic follow-up \\
   201	Env.\ jets & density-stratified AGN fraction & radio morphology/age; cavity energetics; hot-gas density & radio-jet follow-up \\
   202	Mass bin & low-sSFR and AGN by $M_\star$ bin & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
   203	Tracer census & tracer prevalence in 60k sample & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
   204	Gas depletion & massive low-sSFR baseline; H$\alpha$ proxy & CO/dust gas masses; aperture-matched SFRs; morphology; environment & CO/HI follow-up \\
   205	Simulation vector & mass-redshift target vector & mocks through SDSS/MaNGA/ALMA/X-ray/radio selection; aperture/noise models & forward model \\
   206	\enddata
   207	\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
   208	\end{deluxetable*}
   209	
   210	
   211	\section{Package decision}
   212	These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.
   213	
   214	\section{Local reproducibility}
   215	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
   216	
   217	
   218	\begin{thebibliography}{}
   219	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   220	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   221	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   222	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   223	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   224	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   225	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   226	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   227	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   228	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   229	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   230	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   231	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   232	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   233	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   234	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   235	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   236	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   237	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   238	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   239	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   240	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   241	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   242	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   243	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   244	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   245	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   246	\end{thebibliography}
   247	
   248	\end{document}

codex
CODEX_KUN_REVIEW_CYCLE_06

**Findings**
- **Medium: sensitivity numbers are compressed too aggressively in the flagship text.** In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13), [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L73), [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L76), and [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L90), the text reads as if the stricter S/N cut and the Seyfert-like proxy both reduce the offset to `-0.763 dex`. The table is more precise: `S/N>=10` gives `-0.744 dex`, while the `N II Seyfert-like proxy` gives `-0.763 dex`. This should be separated explicitly so the manuscript does not blur two distinct sensitivity checks.

- **Medium: a few sentences are still close to the association-only boundary.** The highest-risk phrasing is in [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L63), [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L76), and [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L90), where the text uses mechanistic phrasing like “systematic removal of the most quenched, bulge-dominated LINER-like systems” and “the broad contamination primarily affects the broad low-ionization selection.” That is still defensible, but it is the sort of language that can be read as a physical explanation rather than a selection-function statement.

- **Low: TeX reproducibility warnings are nonfatal but real.** Both compile logs report `lineno.sty:296: Invalid UTF-8 byte or sequence ... replaced by U+FFFD`, and the supplement also has several underfull `\hbox` warnings. The PDFs built successfully, so this is not a blocker, but it is a portability risk if the final submission is compiled under a different engine or stricter settings. See the flagship compile log and the supplement compile log in the package. The source warnings are concentrated around long paragraphs and tables, e.g. flagship source lines 25 and 86, and supplement source lines 43, 47, 100, 159, 186, 216, and 232.

**Numeric consistency**
- The headline numbers are internally consistent: `8,146` matched pairs, median `-1.309 dex`, bootstrap interval `[-1.334, -1.283]`, `60,000` cached rows, `249,917` strict parent rows, and `24.0%` coverage all match the manuscript text.
- The selection-cascade percentages `49.9%`, `35.2%`, and `18.3%` are also consistent if they are read as retention versus the `501,060` spectro-z parent, not versus the `60,000` cache.
- The one numeric ambiguity is the `-0.744 dex` vs `-0.763 dex` sensitivity pair noted above. That should be made explicit.

**Exact safe edits for the integrator**
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13), replace:
  - “Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to `-0.763 dex`...”
  - with:
  - “Sensitivity checks show that the `S/N>=10` variant yields `-0.744 dex`, while the Seyfert-like proxy yields `-0.763 dex`; both are consistent with narrower selection cuts excluding more low-ionization objects by construction.”
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L76), replace:
  - “The drop from `-1.309 dex` to `-0.763 dex` therefore reflects systematic removal of the most quenched, bulge-dominated LINER-like systems...”
  - with:
  - “The `-0.763 dex` Seyfert-like proxy is consistent with excluding a larger share of LINER-like, bulge-dominated objects by construction; the manuscript does not infer a physical mechanism from that change.”
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L90), replace:
  - “The broad contamination primarily affects the broad low-ionization selection, which is why the narrower Seyfert-like proxy yields the smaller offset.”
  - with:
  - “The narrower Seyfert-like proxy yields the smaller offset because it excludes more low-ionization objects by construction.”
- If you want the prose to be stricter still, soften [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L63) from “can therefore be inflated relative to a galaxy-wide suppression signal” to “can therefore differ from any galaxy-wide suppression signal.”
- For the supplement, no numeric correction is needed, but if you want a tighter guardrail, keep the phrases “denominator,” “proxy,” and “not a physical measurement” and avoid adding any new language that implies feedback, quenching, heating, or escape as a result rather than a future test target.

**Bottom line**
- Scientifically, the package is coherent and the key counts/checks are consistent.
- The main cleanup needed is wording precision around the `-0.744` vs `-0.763` sensitivity results and a slight tightening of the association-only language.

**Safety ledger**
- Read-only review only.
- No file edits.
- No git writes, deploys, publishes, API calls, credential access, or live/public-root access.
- Local TeX logs and manuscript sources inspected only.
tokens used
49,977
CODEX_KUN_REVIEW_CYCLE_06

**Findings**
- **Medium: sensitivity numbers are compressed too aggressively in the flagship text.** In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13), [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L73), [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L76), and [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L90), the text reads as if the stricter S/N cut and the Seyfert-like proxy both reduce the offset to `-0.763 dex`. The table is more precise: `S/N>=10` gives `-0.744 dex`, while the `N II Seyfert-like proxy` gives `-0.763 dex`. This should be separated explicitly so the manuscript does not blur two distinct sensitivity checks.

- **Medium: a few sentences are still close to the association-only boundary.** The highest-risk phrasing is in [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L63), [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L76), and [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L90), where the text uses mechanistic phrasing like “systematic removal of the most quenched, bulge-dominated LINER-like systems” and “the broad contamination primarily affects the broad low-ionization selection.” That is still defensible, but it is the sort of language that can be read as a physical explanation rather than a selection-function statement.

- **Low: TeX reproducibility warnings are nonfatal but real.** Both compile logs report `lineno.sty:296: Invalid UTF-8 byte or sequence ... replaced by U+FFFD`, and the supplement also has several underfull `\hbox` warnings. The PDFs built successfully, so this is not a blocker, but it is a portability risk if the final submission is compiled under a different engine or stricter settings. See the flagship compile log and the supplement compile log in the package. The source warnings are concentrated around long paragraphs and tables, e.g. flagship source lines 25 and 86, and supplement source lines 43, 47, 100, 159, 186, 216, and 232.

**Numeric consistency**
- The headline numbers are internally consistent: `8,146` matched pairs, median `-1.309 dex`, bootstrap interval `[-1.334, -1.283]`, `60,000` cached rows, `249,917` strict parent rows, and `24.0%` coverage all match the manuscript text.
- The selection-cascade percentages `49.9%`, `35.2%`, and `18.3%` are also consistent if they are read as retention versus the `501,060` spectro-z parent, not versus the `60,000` cache.
- The one numeric ambiguity is the `-0.744 dex` vs `-0.763 dex` sensitivity pair noted above. That should be made explicit.

**Exact safe edits for the integrator**
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L13), replace:
  - “Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to `-0.763 dex`...”
  - with:
  - “Sensitivity checks show that the `S/N>=10` variant yields `-0.744 dex`, while the Seyfert-like proxy yields `-0.763 dex`; both are consistent with narrower selection cuts excluding more low-ionization objects by construction.”
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L76), replace:
  - “The drop from `-1.309 dex` to `-0.763 dex` therefore reflects systematic removal of the most quenched, bulge-dominated LINER-like systems...”
  - with:
  - “The `-0.763 dex` Seyfert-like proxy is consistent with excluding a larger share of LINER-like, bulge-dominated objects by construction; the manuscript does not infer a physical mechanism from that change.”
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L90), replace:
  - “The broad contamination primarily affects the broad low-ionization selection, which is why the narrower Seyfert-like proxy yields the smaller offset.”
  - with:
  - “The narrower Seyfert-like proxy yields the smaller offset because it excludes more low-ionization objects by construction.”
- If you want the prose to be stricter still, soften [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L63) from “can therefore be inflated relative to a galaxy-wide suppression signal” to “can therefore differ from any galaxy-wide suppression signal.”
- For the supplement, no numeric correction is needed, but if you want a tighter guardrail, keep the phrases “denominator,” “proxy,” and “not a physical measurement” and avoid adding any new language that implies feedback, quenching, heating, or escape as a result rather than a future test target.

**Bottom line**
- Scientifically, the package is coherent and the key counts/checks are consistent.
- The main cleanup needed is wording precision around the `-0.744` vs `-0.763` sensitivity results and a slight tightening of the association-only language.

**Safety ledger**
- Read-only review only.
- No file edits.
- No git writes, deploys, publishes, API calls, credential access, or live/public-root access.
- Local TeX logs and manuscript sources inspected only.


# command_result
exit_code=0
elapsed_s=151.5
timed_out=False
finished_utc=2026-07-09T03:39:39Z
