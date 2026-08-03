# codex-kun-cycle-15
Started UTC: 2026-07-09T04:35:55Z
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
session id: 019f4529-33bb-7863-8192-b3fc18fbdf31
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_15.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m checking the two TeX sources plus the audit and handoff notes to verify numeric consistency, compile risk, and any prose that weakens the association-only constraint. First pass is file structure and the specific figures you flagged, then I’ll cross-check wording against the guardrail.
exec
/bin/zsh -lc "sed -n '1,260p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/PACKAGE_AUDIT.md\"" in /Users/duhokim/NebulaMind/NebulaMind
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
/bin/zsh -lc "rg -n \"8,146|8146|-1\\.309|1\\.334|1\\.283|60,000|249,917|24\\.0%|association|only association|guardrail|parent|coverage|dex|cached rows\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/PACKAGE_AUDIT.md\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/FINAL_HANDOFF.md\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/FINAL_HANDOFF.md:84:- Main number: 8,146 matched pairs, median delta log sSFR = -1.309 dex, bootstrap interval [-1.334, -1.283] dex.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/FINAL_HANDOFF.md:85:- Guard: association only, not causal AGN feedback.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/FINAL_HANDOFF.md:86:- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/FINAL_HANDOFF.md:159:1. Read the polished RP-1 PDF for scientific wording, especially whether the association-only claim is clear enough.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:13:This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same fixed-size 60,000-galaxy pilot sample and the same selection-function caveats. The 60,000-galaxy sample is a computational, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-mock data are treated as missing observables for future tests rather than as measurements in this package. The sample coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:19:The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the topics span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. Keeping the notes in one supplement prevents overclaiming and gives future work a single checklist of what still must be added. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:22:The atlas uses the same analyzed public-data backbone as the main paper: 60,000 galaxies in a fixed-size pilot sample from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, i.e. 24.0\% sample coverage. The four-line selection is sSFR-dependent and the sample is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The galaxy-by-galaxy stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing. The 60,000-row cache is an arbitrary computational pilot cap, not a physical selection threshold.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:29:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:34:four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:35:four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:39:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:45:\subsection{Relative neighbor-count baseline: SDSS 10th-neighbor index for low-sSFR incidence}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:46:We establish a relative neighbor-count baseline within the emission-line denominator that can later be joined to group catalogs and halo masses. The 10th-neighbor index is an internal ordinal rank within this selection-biased sample and does not map to physical environmental volume density or halo density. SDSS fiber collisions can also suppress close-pair counts in dense environments, so the proxy is biased before any physical interpretation is attempted. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:61:\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:71:\item halo-selected parent catalogues
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:85:We isolate the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:102:\subsection{Radio-jet environment baseline: optical AGN fraction vs. 10th-neighbor index in massive hosts}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:103:We define the environment-stratified optical denominator that future radio and X-ray work could test. The 10th-neighbor index is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has an optical AGN fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:121:In this optical-emission-line denominator, the 11.0--12.5 dex peak is a selection-function artifact: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold. We identify the mass bin where a future gas-inclusive study should look for an apparent incidence change. The note measures the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the optical AGN fraction peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:134:\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and optical AGN incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up, not a physical transition-mass measurement. The 11.0--12.5 dex peak is a selection-function artifact in this emission-line sample, not a universal feedback threshold.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:140:We compare optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:144:\item a shared parent denominator
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:152:\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work, not a molecular or neutral gas census.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:158:We define the denominator for CO/HI gas-fraction and depletion-time follow-up. The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:200:Maintenance heating & optical AGN in massive low-sSFR hosts & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:208:\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving sample becomes less representative of quiescent hosts as the cut tightens.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, fixed-size 60,000-galaxy pilot sample sequentially selected by \texttt{specObjID} as a computational pilot cap from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot sample rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:15:Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, indicating that the result depends on the chosen emission-line denominator and on the exclusion of LINER-like, retired, bulge-dominated hosts with weak central star formation. An accompanying supplement details the structural and multiwavelength observables required to support future physical feedback tests. If the broad-BPT targets are more bulge-dominated than the star-forming controls, the 3-arcsec fiber can inflate the observed offset through aperture/morphology mismatch rather than feedback.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:22:This paper does not attempt to normalize the fixed-size 60,000-galaxy sample into a volume-complete luminosity or mass function.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:28:The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:31:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a fixed-size 60,000-galaxy pilot sample selected sequentially by \texttt{specObjID}. It is a computationally convenient, non-random subset used to establish the relative association, not a volume-limited census. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the cap is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:38:\tablecaption{Selection cascade for the flagship denominator. The fixed-size 60,000-galaxy pilot sample is an artificial pilot-query cap, not a physical selection effect, and it cannot be used to derive volume-complete luminosity functions.\label{tab:selection}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:39:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:44:four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:45:four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:49:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:52:The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the fixed-size-sample limitation.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:55:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:67:A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the -1.309 dex offset may be partially or entirely driven by comparing bulge-dominated broad-BPT hosts to disk-dominated star-forming controls.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:74:Broad BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:75:Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:80:\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:92:Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. Within this sample, that $\sim$0.55 dex reduction is a practical estimate of how much LINER-like or retired-galaxy contamination is embedded in the broader broad-BPT denominator, rather than evidence for a different active feedback mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global star-formation suppression signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size 60,000-galaxy pilot sample. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:95:RP-1 is best treated as a concise, selection-aware association paper, not a causal study. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:96:In practice, that means future work needs the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation-mock comparisons \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,piotrowska2022,wetzel2013,dekel2006}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.

exec
/bin/zsh -lc "sed -n '1,260p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/FINAL_HANDOFF.md\"" in /Users/duhokim/NebulaMind/NebulaMind
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
I’ve confirmed the headline numbers are present in both the flagship and the handoff notes. Next I’m reading the surrounding prose and table captions to separate ordinary scientific framing from phrases that could be read as causal or feedback claims.
exec
/bin/zsh -lc "nl -ba \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex\" | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
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
    13	We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, fixed-size 60,000-galaxy pilot sample sequentially selected by \texttt{specObjID} as a computational pilot cap from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot sample rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim.
    14	
    15	Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, indicating that the result depends on the chosen emission-line denominator and on the exclusion of LINER-like, retired, bulge-dominated hosts with weak central star formation. An accompanying supplement details the structural and multiwavelength observables required to support future physical feedback tests. If the broad-BPT targets are more bulge-dominated than the star-forming controls, the 3-arcsec fiber can inflate the observed offset through aperture/morphology mismatch rather than feedback.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}
    19	
    20	\section{Question and claim boundary}
    21	This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a strong negative sSFR offset within the analyzed denominator. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
    22	This paper does not attempt to normalize the fixed-size 60,000-galaxy sample into a volume-complete luminosity or mass function.
    23	
    24	
    25	The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT-selected galaxies'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.
    26	
    27	\subsection{Scope and limitations}
    28	The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.
    29	
    30	\section{Data and shared selection}
    31	The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a fixed-size 60,000-galaxy pilot sample selected sequentially by \texttt{specObjID}. It is a computationally convenient, non-random subset used to establish the relative association, not a volume-limited census. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the cap is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
    32	Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
    33	Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy; if broad-BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a global star-formation comparison.
    34	The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.
    35	
    36	\begin{deluxetable*}{lrrr}
    37	\tabletypesize{\scriptsize}
    38	\tablecaption{Selection cascade for the flagship denominator. The fixed-size 60,000-galaxy pilot sample is an artificial pilot-query cap, not a physical selection effect, and it cannot be used to derive volume-complete luminosity functions.\label{tab:selection}}
    39	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    40	\startdata
    41	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
    42	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
    43	plus galSpecLine join & 416,554 & -- & 83.1\% \\
    44	four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
    45	four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
    46	four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
    47	four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
    48	\enddata
    49	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
    50	\end{deluxetable*}
    51	
    52	The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the fixed-size-sample limitation.
    53	
    54	\section{Classification and matching}
    55	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
    56	Here, ``broad optical BPT-selected'' means the inclusive optical-emission-line class under the standard BPT demarcations, while the Seyfert-like sensitivity check uses the stricter Kewley et al.\ (2006) high-excitation cut and therefore excludes LINER-like systems by construction.
    57	
    58	\begin{figure*}
    59	\centering
    60	\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
    61	\caption{BPT line-ratio diagram for the SDSS DR17 analysis denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
    62	\label{fig:bpt}
    63	\end{figure*}
    64	
    65	\section{Matched-control result}
    66	The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the broad BPT-selected galaxies relative to star-forming controls.
    67	A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the -1.309 dex offset may be partially or entirely driven by comparing bulge-dominated broad-BPT hosts to disk-dominated star-forming controls.
    68	
    69	\begin{deluxetable*}{lrrrr}
    70	\tabletypesize{\scriptsize}
    71	\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
    72	\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
    73	\startdata
    74	Broad BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
    75	Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
    76	Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
    77	Broad BPT-selected targets, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
    78	N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
    79	\enddata
    80	\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
    81	\end{deluxetable*}
    82	
    83	\begin{figure*}
    84	\centering
    85	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    86	\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT-selected galaxies minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
    87	\label{fig:offsets}
    88	\end{figure*}
    89	
    90	\section{Interpretation}
    91	The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper.
    92	Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. Within this sample, that $\sim$0.55 dex reduction is a practical estimate of how much LINER-like or retired-galaxy contamination is embedded in the broader broad-BPT denominator, rather than evidence for a different active feedback mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global star-formation suppression signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size 60,000-galaxy pilot sample. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
    93	
    94	\section{Conclusion}
    95	RP-1 is best treated as a concise, selection-aware association paper, not a causal study. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
    96	In practice, that means future work needs the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation-mock comparisons \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,piotrowska2022,wetzel2013,dekel2006}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.
    97	
    98	\begin{thebibliography}{}
    99	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   100	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   101	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   102	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   103	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   104	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   105	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   106	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   107	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   108	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   109	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   110	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   111	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   112	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   113	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   114	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   115	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   116	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   117	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   118	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   119	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   120	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   121	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   122	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   123	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   124	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   125	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   126	\end{thebibliography}
   127	
   128	\end{document}

exec
/bin/zsh -lc "nl -ba \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex\" | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
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
    13	This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same fixed-size 60,000-galaxy pilot sample and the same selection-function caveats. The 60,000-galaxy sample is a computational, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-mock data are treated as missing observables for future tests rather than as measurements in this package. The sample coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}
    17	
    18	\section{Purpose}
    19	The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the topics span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. Keeping the notes in one supplement prevents overclaiming and gives future work a single checklist of what still must be added. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
    20	
    21	\section{Shared denominator}
    22	The atlas uses the same analyzed public-data backbone as the main paper: 60,000 galaxies in a fixed-size pilot sample from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, i.e. 24.0\% sample coverage. The four-line selection is sSFR-dependent and the sample is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The galaxy-by-galaxy stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing. The 60,000-row cache is an arbitrary computational pilot cap, not a physical selection threshold.
    23	
    24	The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made. In other words, the sections are distinct follow-up domains bounded by the same optical selection effect.
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
    43	\textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
    44	
    45	\subsection{Relative neighbor-count baseline: SDSS 10th-neighbor index for low-sSFR incidence}
    46	We establish a relative neighbor-count baseline within the emission-line denominator that can later be joined to group catalogs and halo masses. The 10th-neighbor index is an internal ordinal rank within this selection-biased sample and does not map to physical environmental volume density or halo density. SDSS fiber collisions can also suppress close-pair counts in dense environments, so the proxy is biased before any physical interpretation is attempted. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the required missing multiwavelength observables for physical inference are:
    47	\begin{itemize}
    48	\item group catalogues
    49	\item robust central/satellite labels
    50	\item halo masses
    51	\item spectroscopic fiber-collision correction at the 55-arcsec scale
    52	\item morphology
    53	\item multi-redshift selection functions
    54	\end{itemize}
    55	Within this selection-biased emission-line sample, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement.
    56	These are still needed for a future environmental test \citep{peng2010,wetzel2013,dekel2006}.
    57	
    58	\begin{figure}
    59	\centering
    60	\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
    61	\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up, not a physical-feedback measurement.}
    62	\label{fig:m1-rp2-neighbor-count-baseline}
    63	\end{figure}
    64	
    65	
    66	\subsection{Maintenance-heating denominator: optical AGN in massive SDSS hosts}
    67	We isolate the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The required missing multiwavelength observables for physical inference are:
    68	\begin{itemize}
    69	\item X-ray cavity or cooling-luminosity measurements
    70	\item radio jet powers
    71	\item halo-selected parent catalogues
    72	\item nondetection modelling
    73	\end{itemize}
    74	These are still needed for a future maintenance-heating test \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.
    75	
    76	\begin{figure}
    77	\centering
    78	\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
    79	\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements, not a heating-to-cooling result.}
    80	\label{fig:m1-rp3-maintenance-heating}
    81	\end{figure}
    82	
    83	
    84	\subsection{High-excitation optical AGN baseline: resolved kinematics follow-up}
    85	We isolate the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The required missing multiwavelength observables for physical inference are:
    86	\begin{itemize}
    87	\item resolved outflow velocities
    88	\item halo potentials
    89	\item molecular, ionized, and neutral gas phases
    90	\item CGM recycling tracers
    91	\end{itemize}
    92	These are still needed for a future outflow test \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.
    93	
    94	\begin{figure}
    95	\centering
    96	\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
    97	\caption{SDSS optical emission-line denominator: the high-excitation AGN subset used to define an observational baseline for future resolved-kinematic measurements, not an escape or recycling result.}
    98	\label{fig:m2-p1-outflow-escape-recycling}
    99	\end{figure}
   100	
   101	
   102	\subsection{Radio-jet environment baseline: optical AGN fraction vs. 10th-neighbor index in massive hosts}
   103	We define the environment-stratified optical denominator that future radio and X-ray work could test. The 10th-neighbor index is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has an optical AGN fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The required missing multiwavelength observables for physical inference are:
   104	\begin{itemize}
   105	\item radio jet morphology and age
   106	\item cavity or shock energetics
   107	\item hot-gas density
   108	\item calibrated jet-power estimates
   109	\end{itemize}
   110	These are still needed for a future radio-jet test \citep{best2005,mcnamara2007,heckmanbest2014}.
   111	
   112	\begin{figure}
   113	\centering
   114	\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
   115	\caption{SDSS optical emission-line denominator: the high- and low-density quartile comparison among massive SDSS hosts, used as a baseline for future radio-jet and X-ray work, not a coupling measurement.}
   116	\label{fig:m2-p2-radio-jet-environment}
   117	\end{figure}
   118	
   119	
   120	\subsection{Stellar-mass selection diagnostic: low-sSFR and optical AGN incidence}
   121	In this optical-emission-line denominator, the 11.0--12.5 dex peak is a selection-function artifact: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold. We identify the mass bin where a future gas-inclusive study should look for an apparent incidence change. The note measures the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the optical AGN fraction peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The required missing multiwavelength observables for physical inference are:
   122	\begin{itemize}
   123	\item gas fractions
   124	\item baryon deficits
   125	\item halo masses
   126	\item stellar-feedback observables
   127	\item high-redshift extensions
   128	\end{itemize}
   129	The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}.
   130	
   131	\begin{figure}
   132	\centering
   133	\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
   134	\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and optical AGN incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up, not a physical transition-mass measurement. The 11.0--12.5 dex peak is a selection-function artifact in this emission-line sample, not a universal feedback threshold.}
   135	\label{fig:m2-p3-feedback-transition-mass}
   136	\end{figure}
   137	
   138	
   139	\subsection{Tracer-threshold census for multiphase follow-up}
   140	We compare optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The required missing multiwavelength observables for physical inference are:
   141	\begin{itemize}
   142	\item ionized, molecular, and neutral tracers
   143	\item X-ray or radio tracers
   144	\item a shared parent denominator
   145	\item a consistent aperture model
   146	\end{itemize}
   147	These are still needed for a future multiphase test \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.
   148	
   149	\begin{figure}
   150	\centering
   151	\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
   152	\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work, not a molecular or neutral gas census.}
   153	\label{fig:m3-p1-multiphase-census}
   154	\end{figure}
   155	
   156	
   157	\subsection{Low-sSFR optical denominator: baseline for future CO/HI gas measurements}
   158	We define the denominator for CO/HI gas-fraction and depletion-time follow-up. The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The required missing multiwavelength observables for physical inference are:
   159	\begin{itemize}
   160	\item CO or dust-based molecular gas masses
   161	\item aperture-matched SFRs
   162	\item morphology
   163	\item environment labels
   164	\end{itemize}
   165	These are still needed for a future gas-fraction or depletion-time test \citep{xcoldgass2017,xgass2018,piotrowska2022}.
   166	
   167	\begin{figure}
   168	\centering
   169	\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
   170	\caption{SDSS optical emission-line denominator: the massive low-sSFR SDSS galaxies available for CO/HI depletion-time follow-up, not a gas-depletion-efficiency measurement.}
   171	\label{fig:m3-p2-gas-depletion-efficiency}
   172	\end{figure}
   173	
   174	
   175	\subsection{Simulation target vector for forward-model comparison}
   176	We provide a compact observed target vector for forward modelling, not a direct simulation comparison. The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The required missing multiwavelength observables for physical inference are:
   177	\begin{itemize}
   178	\item simulation mocks passed through the same optical S/N and fiber-aperture selection function used here, then through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions
   179	\item aperture models
   180	\item noise models
   181	\end{itemize}
   182	Without those matched selection steps, any simulation comparison is not a valid test. These are still needed for a future simulation-comparison test \citep{simba2019,tng2019,eagle2015}.
   183	
   184	\begin{figure}
   185	\centering
   186	\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
   187	\caption{SDSS optical emission-line denominator: low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift in the SDSS emission-line sample. This is an observed target vector for forward modelling, not a direct simulation comparison.}
   188	\label{fig:m3-p3-simulation-validation}
   189	\end{figure}
   190	
   191	\section{Atlas summary}
   192	Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight notes. All eight notes are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or mock-observation data are added, so their present role is to organize follow-up rather than to establish causal physical claims.
   193	
   194	\begin{deluxetable*}{llll}
   195	\tabletypesize{\scriptsize}
   196	\tablecaption{Atlas-level follow-up menu. Each row summarizes the present optical role and the missing observables needed before any physical inference.\label{tab:atlas-summary}}
   197	\tablehead{\colhead{Topic} & \colhead{Observed baseline} & \colhead{Missing observables} & \colhead{Role}}
   198	\startdata
   199	Environment & low-sSFR vs.\ 10th-neighbor rank & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test \\
   200	Maintenance heating & optical AGN in massive low-sSFR hosts & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
   201	Outflow kinematics & high-excitation AGN subset & resolved velocities; halo potentials; multiphase gas; CGM tracers & kinematic follow-up \\
   202	Env.\ jets & density-stratified AGN fraction & radio morphology/age; cavity energetics; hot-gas density & radio-jet follow-up \\
   203	Mass bin & low-sSFR and AGN by $M_\star$ bin & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
   204	Tracer census & tracer prevalence in 60k sample & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
   205	Gas depletion & massive low-sSFR baseline; H$\alpha$ proxy & CO/dust gas masses; aperture-matched SFRs; morphology; environment & CO/HI follow-up \\
   206	Simulation vector & mass-redshift target vector & mocks through SDSS/MaNGA/ALMA/X-ray/radio selection; aperture/noise models & forward model \\
   207	\enddata
   208	\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving sample becomes less representative of quiescent hosts as the cut tightens.}
   209	\end{deluxetable*}
   210	
   211	
   212	\section{Package decision}
   213	These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.
   214	
   215	\begin{thebibliography}{}
   216	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   217	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   218	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   219	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   220	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   221	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   222	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   223	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   224	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   225	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   226	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   227	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   228	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   229	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   230	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   231	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   232	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   233	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   234	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   235	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   236	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   237	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   238	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   239	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   240	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   241	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   242	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   243	\end{thebibliography}
   244	
   245	\end{document}

codex
I’ve got the main prose now. I’m checking compile logs just enough to separate harmless AASTeX layout warnings from actual build risk, and I’m verifying the arithmetic on the sample fractions and matching counts.
exec
/bin/zsh -lc 'rg -n "Warning|Overfull|Underfull|Undefined|Citation|Reference|Package" "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package" -g "*.log"' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.quality.compile.log:3:warning: rp1_flagship_polished.tex:35: Underfull \hbox (badness 1342) in paragraph at lines 31--35
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.quality.compile.log:4:warning: rp1_flagship_polished.tex:57: Underfull \hbox (badness 1635) in paragraph at lines 55--57
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.quality.compile.log:5:warning: rp1_flagship_polished.tex:57: Underfull \hbox (badness 1533) in paragraph at lines 55--57
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.quality.compile.log:8:warning: rp1_flagship_polished.tex:35: Underfull \hbox (badness 1342) in paragraph at lines 31--35
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log:3:warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log:4:warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log:7:warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log:8:warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log:11:warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log:12:warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:3:warning: supplementary_denominator_atlas.tex:44: Underfull \hbox (badness 1708) in paragraph at lines 43--44
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:4:warning: supplementary_denominator_atlas.tex:130: Underfull \hbox (badness 1859) in paragraph at lines 129--130
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:5:warning: supplementary_denominator_atlas.tex:130: Underfull \hbox (badness 1681) in paragraph at lines 129--130
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:6:warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 2150) in paragraph at lines 158--159
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:7:warning: supplementary_denominator_atlas.tex:170: Underfull \hbox (badness 2096) in paragraph at lines 170--170
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:10:warning: supplementary_denominator_atlas.tex:44: Underfull \hbox (badness 1708) in paragraph at lines 43--44
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:11:warning: supplementary_denominator_atlas.tex:130: Underfull \hbox (badness 1859) in paragraph at lines 129--130
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:12:warning: supplementary_denominator_atlas.tex:130: Underfull \hbox (badness 1681) in paragraph at lines 129--130
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:13:warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 2150) in paragraph at lines 158--159
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:14:warning: supplementary_denominator_atlas.tex:170: Underfull \hbox (badness 2096) in paragraph at lines 170--170
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:17:warning: supplementary_denominator_atlas.tex:44: Underfull \hbox (badness 1708) in paragraph at lines 43--44
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:18:warning: supplementary_denominator_atlas.tex:130: Underfull \hbox (badness 1859) in paragraph at lines 129--130
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:19:warning: supplementary_denominator_atlas.tex:130: Underfull \hbox (badness 1681) in paragraph at lines 129--130
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:20:warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 2150) in paragraph at lines 158--159
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.quality.compile.log:21:warning: supplementary_denominator_atlas.tex:170: Underfull \hbox (badness 2096) in paragraph at lines 170--170
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:3:warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:4:warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:5:warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:6:warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:7:warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:8:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:9:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:10:warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:13:warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:14:warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:15:warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:16:warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:17:warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:18:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:19:warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log:20:warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232

codex
The compile logs are clean in the only way that matters here: underfull-hbox layout warnings, no undefined references or fatal LaTeX errors. I hit a shell limitation trying to use a heredoc, so I’m switching to one-line arithmetic checks for the sample coverage and table ratios.
exec
/bin/zsh -lc "awk 'BEGIN{printf \"60,000 / 249,917 = %.4f%%\\n\", 60000/249917*100; printf \"373,445 / 501,060 = %.4f%%\\n\", 373445/501060*100; printf \"249,917 / 501,060 = %.4f%%\\n\", 249917/501060*100; printf \"176,523 / 501,060 = %.4f%%\\n\", 176523/501060*100; printf \"91,768 / 501,060 = %.4f%%\\n\", 91768/501060*100; printf \"8,146 / 39,553 = %.4f%%\\n\", 8146/39553*100; printf \"2,114 / 60,000 = %.4f%%\\n\", 2114/60000*100 }'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
60,000 / 249,917 = 24.0080%
373,445 / 501,060 = 74.5310%
249,917 / 501,060 = 49.8777%
176,523 / 501,060 = 35.2299%
91,768 / 501,060 = 18.3148%
8,146 / 39,553 = 20.5952%
2,114 / 60,000 = 3.5233%

exec
/bin/zsh -lc "sed -n '1,120p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log\" && printf '\\n---\\n' && sed -n '1,120p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log\"" in /Users/duhokim/NebulaMind/NebulaMind
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

---
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

codex
I have enough to separate the actual risk from the safe caveats. I’m doing one last targeted sweep for `feedback`, `causal`, and `quenching` language so I can point to the exact phrases that should be left as-is versus rewritten more defensively.
exec
/bin/zsh -lc 'rg -n "feedback|causal|quench|quenching|maintenance heating|candidate" "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex" "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex"' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:13:This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same fixed-size 60,000-galaxy pilot sample and the same selection-function caveats. The 60,000-galaxy sample is a computational, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-mock data are treated as missing observables for future tests rather than as measurements in this package. The sample coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:19:The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the topics span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. Keeping the notes in one supplement prevents overclaiming and gives future work a single checklist of what still must be added. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:43:\textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:61:\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up, not a physical-feedback measurement.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:67:We isolate the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:85:We isolate the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:121:In this optical-emission-line denominator, the 11.0--12.5 dex peak is a selection-function artifact: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold. We identify the mass bin where a future gas-inclusive study should look for an apparent incidence change. The note measures the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the optical AGN fraction peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:126:\item stellar-feedback observables
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:134:\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and optical AGN incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up, not a physical transition-mass measurement. The 11.0--12.5 dex peak is a selection-function artifact in this emission-line sample, not a universal feedback threshold.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:135:\label{fig:m2-p3-feedback-transition-mass}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:140:We compare optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:192:Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight notes. All eight notes are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or mock-observation data are added, so their present role is to organize follow-up rather than to establish causal physical claims.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:203:Mass bin & low-sSFR and AGN by $M_\star$ bin & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:213:These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, fixed-size 60,000-galaxy pilot sample sequentially selected by \texttt{specObjID} as a computational pilot cap from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot sample rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:15:Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, indicating that the result depends on the chosen emission-line denominator and on the exclusion of LINER-like, retired, bulge-dominated hosts with weak central star formation. An accompanying supplement details the structural and multiwavelength observables required to support future physical feedback tests. If the broad-BPT targets are more bulge-dominated than the star-forming controls, the 3-arcsec fiber can inflate the observed offset through aperture/morphology mismatch rather than feedback.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:21:This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a strong negative sSFR offset within the analyzed denominator. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:61:\caption{BPT line-ratio diagram for the SDSS DR17 analysis denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:92:Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. Within this sample, that $\sim$0.55 dex reduction is a practical estimate of how much LINER-like or retired-galaxy contamination is embedded in the broader broad-BPT denominator, rather than evidence for a different active feedback mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global star-formation suppression signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size 60,000-galaxy pilot sample. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:95:RP-1 is best treated as a concise, selection-aware association paper, not a causal study. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.

exec
/bin/zsh -lc "rg -n \"8,146|1\\.309|1\\.334|1\\.283|60,000|249,917|24\\.0%|24\\.008|249,917|49\\.9|74\\.5|0\\.763|0\\.744|0\\.55|0\\.520|0\\.418|0\\.136\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, fixed-size 60,000-galaxy pilot sample sequentially selected by \texttt{specObjID} as a computational pilot cap from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot sample rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:15:Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, indicating that the result depends on the chosen emission-line denominator and on the exclusion of LINER-like, retired, bulge-dominated hosts with weak central star formation. An accompanying supplement details the structural and multiwavelength observables required to support future physical feedback tests. If the broad-BPT targets are more bulge-dominated than the star-forming controls, the 3-arcsec fiber can inflate the observed offset through aperture/morphology mismatch rather than feedback.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:22:This paper does not attempt to normalize the fixed-size 60,000-galaxy sample into a volume-complete luminosity or mass function.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:31:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a fixed-size 60,000-galaxy pilot sample selected sequentially by \texttt{specObjID}. It is a computationally convenient, non-random subset used to establish the relative association, not a volume-limited census. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the cap is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:38:\tablecaption{Selection cascade for the flagship denominator. The fixed-size 60,000-galaxy pilot sample is an artificial pilot-query cap, not a physical selection effect, and it cannot be used to derive volume-complete luminosity functions.\label{tab:selection}}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:44:four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:45:four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:55:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:67:A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the -1.309 dex offset may be partially or entirely driven by comparing bulge-dominated broad-BPT hosts to disk-dominated star-forming controls.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:74:Broad BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:77:Broad BPT-selected targets, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:78:N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:80:\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex:92:Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. Within this sample, that $\sim$0.55 dex reduction is a practical estimate of how much LINER-like or retired-galaxy contamination is embedded in the broader broad-BPT denominator, rather than evidence for a different active feedback mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global star-formation suppression signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size 60,000-galaxy pilot sample. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:13:This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same fixed-size 60,000-galaxy pilot sample and the same selection-function caveats. The 60,000-galaxy sample is a computational, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-mock data are treated as missing observables for future tests rather than as measurements in this package. The sample coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:22:The atlas uses the same analyzed public-data backbone as the main paper: 60,000 galaxies in a fixed-size pilot sample from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, i.e. 24.0\% sample coverage. The four-line selection is sSFR-dependent and the sample is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The galaxy-by-galaxy stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing. The 60,000-row cache is an arbitrary computational pilot cap, not a physical selection threshold.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:34:four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:35:four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:46:We establish a relative neighbor-count baseline within the emission-line denominator that can later be joined to group catalogs and halo masses. The 10th-neighbor index is an internal ordinal rank within this selection-biased sample and does not map to physical environmental volume density or halo density. SDSS fiber collisions can also suppress close-pair counts in dense environments, so the proxy is biased before any physical interpretation is attempted. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:85:We isolate the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:121:In this optical-emission-line denominator, the 11.0--12.5 dex peak is a selection-function artifact: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold. We identify the mass bin where a future gas-inclusive study should look for an apparent incidence change. The note measures the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the optical AGN fraction peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:140:We compare optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The required missing multiwavelength observables for physical inference are:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:152:\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work, not a molecular or neutral gas census.}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:176:We provide a compact observed target vector for forward modelling, not a direct simulation comparison. The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The required missing multiwavelength observables for physical inference are:

codex
CODEX_KUN_REVIEW_CYCLE_15

**Bottom Line**
The package is numerically self-consistent, and both PDFs build successfully. I did not find any hard TeX breakage or figure-missing problem. The only material risks are:
- a non-fatal compile fragility from `lineno.sty` UTF-8 warnings in both build logs, and
- a small amount of wording in the supplement that could be read as stronger than the intended association-only guardrail.

**Findings**
- Medium: Build logs show `lineno.sty:296: Invalid UTF-8 byte or sequence` in both flagship and supplement compile logs, alongside only underfull-hbox layout warnings. The current PDFs are fine, but this is the one reproducibility/build fragility worth tracking because it can change behavior if the TeX engine or line-numbering package handling changes. See [flagship compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log#L1) and [supplement compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log#L1).
- Medium: The supplement line [140](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L140) says, “Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence...”. `feedback-candidate prevalence` is the only phrase I’d flag as guardrail-weakening because it can be read as a feedback claim rather than an optical-selection statement.
- Low: The flagship line [92](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L92) says the `~0.55 dex` reduction is “a practical estimate of how much LINER-like or retired-galaxy contamination is embedded...”. That is directionally correct, but “estimate of how much contamination is embedded” is a bit stronger than needed. It would be safer to frame it as a sensitivity of the broad denominator to removing LINER-like/retired systems.

**Numeric Check**
All requested figures are consistent:
- `8,146` matched pairs appears consistently in the abstract, table, and handoff.
- `-1.309 dex` lies inside the bootstrap interval `[-1.334, -1.283]`.
- `60,000 / 249,917 = 24.0080%`, so the stated `24.0%` coverage is correct rounding.
- `373,445 / 501,060 = 74.5310%`, matching `74.5%`.
- `249,917 / 501,060 = 49.8777%`, matching `49.9%`.
- `176,523 / 501,060 = 35.2299%`, matching `35.2%`.
- `91,768 / 501,060 = 18.3148%`, matching `18.3%`.
- `2,114 / 60,000 = 3.5233%`, consistent with the Seyfert-like subset.
- The `-1.309` to `-0.763` change is `0.546 dex`, so the prose shorthand `~0.55 dex` is fine.

**TeX / Figure / Reproducibility Risks**
- TeX: no fatal errors, no undefined references reported in the logs I checked, only underfull-hbox warnings plus the `lineno.sty` UTF-8 warning.
- Figures: all figure slots appear accounted for in the audit (`10/10`), and the figure captions themselves are strongly guarded against physical-overclaiming.
- Reproducibility: the fixed-size `60,000` cache sequentially selected by `specObjID` is explicitly non-random, so exact reruns depend on preserving the same cache and query snapshot. That is acceptable as long as it stays stated as a pilot cap, not a population sample.
- Reproducibility: the manuscript is correctly explicit that the `3-arcsec` fiber and lack of morphology/aperture matching can inflate offsets, which is good, but it also means the result is inherently denominator-sensitive and not galaxy-wide.

**Safe Edit Recommendations**
1. In [supplementary_denominator_atlas.tex:140](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L140), replace:
   `Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator.`
   with:
   `Simple optical tracer definitions change the inferred AGN-classification prevalence within one common SDSS denominator.`

2. In [rp1_flagship_polished.tex:15](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L15), replace:
   `An accompanying supplement details the structural and multiwavelength observables required to support future physical feedback tests.`
   with:
   `An accompanying supplement details the structural and multiwavelength observables required for future physical follow-up tests.`

3. In [rp1_flagship_polished.tex:92](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L92), replace:
   `a practical estimate of how much LINER-like or retired-galaxy contamination is embedded in the broader broad-BPT denominator`
   with:
   `a practical indication that the broader broad-BPT denominator is sensitive to LINER-like or retired-galaxy removal`

4. Optional conservative cleanup in the supplement: replace any standalone `causal-feedback papers` wording with `causal physical papers` or `causal follow-up papers` if you want the atlas to remain uniformly association-first even in negated context.

**Safety Ledger**
- Read-only review only.
- No files modified.
- No git writes, commits, pushes, or merges.
- No network access, API calls, deploys, or public/live roots touched.
- Only the four requested local files and their compile logs were inspected.
tokens used
52,549
CODEX_KUN_REVIEW_CYCLE_15

**Bottom Line**
The package is numerically self-consistent, and both PDFs build successfully. I did not find any hard TeX breakage or figure-missing problem. The only material risks are:
- a non-fatal compile fragility from `lineno.sty` UTF-8 warnings in both build logs, and
- a small amount of wording in the supplement that could be read as stronger than the intended association-only guardrail.

**Findings**
- Medium: Build logs show `lineno.sty:296: Invalid UTF-8 byte or sequence` in both flagship and supplement compile logs, alongside only underfull-hbox layout warnings. The current PDFs are fine, but this is the one reproducibility/build fragility worth tracking because it can change behavior if the TeX engine or line-numbering package handling changes. See [flagship compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log#L1) and [supplement compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log#L1).
- Medium: The supplement line [140](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L140) says, “Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence...”. `feedback-candidate prevalence` is the only phrase I’d flag as guardrail-weakening because it can be read as a feedback claim rather than an optical-selection statement.
- Low: The flagship line [92](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L92) says the `~0.55 dex` reduction is “a practical estimate of how much LINER-like or retired-galaxy contamination is embedded...”. That is directionally correct, but “estimate of how much contamination is embedded” is a bit stronger than needed. It would be safer to frame it as a sensitivity of the broad denominator to removing LINER-like/retired systems.

**Numeric Check**
All requested figures are consistent:
- `8,146` matched pairs appears consistently in the abstract, table, and handoff.
- `-1.309 dex` lies inside the bootstrap interval `[-1.334, -1.283]`.
- `60,000 / 249,917 = 24.0080%`, so the stated `24.0%` coverage is correct rounding.
- `373,445 / 501,060 = 74.5310%`, matching `74.5%`.
- `249,917 / 501,060 = 49.8777%`, matching `49.9%`.
- `176,523 / 501,060 = 35.2299%`, matching `35.2%`.
- `91,768 / 501,060 = 18.3148%`, matching `18.3%`.
- `2,114 / 60,000 = 3.5233%`, consistent with the Seyfert-like subset.
- The `-1.309` to `-0.763` change is `0.546 dex`, so the prose shorthand `~0.55 dex` is fine.

**TeX / Figure / Reproducibility Risks**
- TeX: no fatal errors, no undefined references reported in the logs I checked, only underfull-hbox warnings plus the `lineno.sty` UTF-8 warning.
- Figures: all figure slots appear accounted for in the audit (`10/10`), and the figure captions themselves are strongly guarded against physical-overclaiming.
- Reproducibility: the fixed-size `60,000` cache sequentially selected by `specObjID` is explicitly non-random, so exact reruns depend on preserving the same cache and query snapshot. That is acceptable as long as it stays stated as a pilot cap, not a population sample.
- Reproducibility: the manuscript is correctly explicit that the `3-arcsec` fiber and lack of morphology/aperture matching can inflate offsets, which is good, but it also means the result is inherently denominator-sensitive and not galaxy-wide.

**Safe Edit Recommendations**
1. In [supplementary_denominator_atlas.tex:140](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L140), replace:
   `Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator.`
   with:
   `Simple optical tracer definitions change the inferred AGN-classification prevalence within one common SDSS denominator.`

2. In [rp1_flagship_polished.tex:15](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L15), replace:
   `An accompanying supplement details the structural and multiwavelength observables required to support future physical feedback tests.`
   with:
   `An accompanying supplement details the structural and multiwavelength observables required for future physical follow-up tests.`

3. In [rp1_flagship_polished.tex:92](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L92), replace:
   `a practical estimate of how much LINER-like or retired-galaxy contamination is embedded in the broader broad-BPT denominator`
   with:
   `a practical indication that the broader broad-BPT denominator is sensitive to LINER-like or retired-galaxy removal`

4. Optional conservative cleanup in the supplement: replace any standalone `causal-feedback papers` wording with `causal physical papers` or `causal follow-up papers` if you want the atlas to remain uniformly association-first even in negated context.

**Safety Ledger**
- Read-only review only.
- No files modified.
- No git writes, commits, pushes, or merges.
- No network access, API calls, deploys, or public/live roots touched.
- Only the four requested local files and their compile logs were inspected.


# command_result
exit_code=0
elapsed_s=170.5
timed_out=False
finished_utc=2026-07-09T04:38:46Z
