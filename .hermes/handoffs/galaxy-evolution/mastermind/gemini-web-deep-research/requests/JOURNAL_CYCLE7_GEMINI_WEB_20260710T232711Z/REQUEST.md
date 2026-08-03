# RT Gemini-web Deep Research request — RP-1 cycle-7 introduction/literature review

Marker: RT_GEMINI_WEB_DEEP_RESEARCH_REQUEST_V1
User-approval marker: HWAO_GEMINI_WEB_PILOT_USER_APPROVED_20260710T232711Z
Request ID: JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z
Created UTC: 2026-07-10T23:34:09Z
Requested by: Hwao-director (user explicitly approved the Gemini Web App supervised pilot sidecar: "let's incorporate it too, why not")
Method scope: M1 flagship RP-1 (journal weekend sprint), with M1/M2/M3 supplement atlas as context

## Why this request is needed

The live 48-hour journal sprint `ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z` is entering cycle 7, phase `introduction`, scheduled ~2026-07-10T23:46:31Z. The authoritative clean candidate is `cycle_05_package`; its flagship RP-1 manuscript currently has **no formal Introduction section** — it opens directly with "Question and claim boundary". Cycle 6 (phase `literature`) was rejected because it lost the numeric invariant `[-1.334,-1.283]` (the bootstrap 95% interval of the headline matched-control offset).

That failure mode is exactly why external literature breadth should arrive as an **advisory sidecar packet**, not as an in-lane rewrite: we want serious prior-study grounding, missing literature/status-map axes, quantitative comparison opportunities, survey/data feasibility checks, and overclaim-risk review for an RP-1 introduction — delivered with source links for local verification, while every retained number and the association-only wording contract stay untouched.

## Current artifacts (read-only basis; do not mutate)

Authoritative clean candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_05_package`

- Flagship TeX: `flagship_rp1/aastex/rp1_flagship_polished.tex`
- Supplement TeX: `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`
- Provenance/custody: `provenance/REAL_DATA_SOURCE_CUSTODY.json` (marker `NEBULAMIND_REAL_DATA_SOURCE_CUSTODY_V1`, `no_mock_or_synthetic_data: true`)
- Cycle-5 audit/summary: `CYCLE_05_tables_figures_AUDIT.json`, `CYCLE_05_tables_figures_SUMMARY.json`
- Retained result lineage: `SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json`, `data/analysis_sample_bpt.csv`, `data/matched_agn_sf_pairs.csv` (inventoried in the custody file)

## Cards/topics to investigate

1. RP-1 flagship manuscript — Introduction / literature-review grounding (cycle-7 `introduction` phase input): "Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Pilot Matched-Control Study".

## Existing constraints / source-basis facts

```text
Numeric invariants (verbatim; may be quoted but never altered, re-derived, or "improved"):
- Fixed 60,000-galaxy SDSS DR17 optical emission-line cache, selected sequentially by specObjID (non-random, non-volume-complete).
- Strict four-line S/N>=3 eligible parent count 249,917; 24.0% cache coverage (selection-context diagnostics only, not retained result rows).
- Redshift range 0.02 < z < 0.12; 3-arcsec fiber subtends ~1.2–6.5 kpc (fiber-centered measurement).
- Denominator: 39,553 star-forming; 12,234 intermediate/composite; 8,146 broad optical BPT-selected; 67 unclassified.
- Matching: variance-normalized Euclidean nearest neighbor in standardized (log M*, z), with replacement, no caliper; 8,146 of 8,146 targets matched (100%); median absolute separations 0.0045 dex in log M* and 0.00021 in z.
- Headline retained result: median Delta log sSFR (target minus matched star-forming control) = -1.309 dex; bootstrap 95% interval [-1.334,-1.283] dex.  <- the invariant cycle 6 lost; absolute contract.
- Stellar mass / sSFR proxies: MPA-JHU-style galSpecExtra catalog medians lgm_tot_p50 and specsfr_tot_p50.

Wording contract (association-only language):
- Class label is "broad optical BPT-selected galaxies" — never a bare "AGN" population claim; Seyfert/LINER separation is future work.
- The result is a fiber-centered, morphology-uncontrolled, selection-limited, denominator-bound ASSOCIATION; it is NOT causal, NOT quenching/feedback evidence, NOT gas depletion, NOT abundance/volume density.
- Structural proxies (R90/R50, fracDeV, petroR50/90, velocity dispersion) were not retained in the cache; the offset is currently indistinguishable from bulge-fraction/aperture associations.

Citation families ALREADY in the RP-1 bibliography (Gemini should extend beyond these, not restate them):
BPT foundations (Baldwin+1981; Kewley+2001, 2006; Kauffmann+2003); SDSS backbone (York+2000; DR17 Abdurro'uf+2022; Brinchmann+2004); LINER/retired-galaxy contamination (Cid Fernandes+2011; Stasinska+2008, 2015; Belfiore+2016); bulge/morphology quenching (Schawinski+2010; Bluck+2014; Piotrowska+2022); aperture & IFU (Kewley+2005; Penny+2018; Cheung+2016; Bundy+2015; Cano-Diaz+2016); radio/X-ray maintenance (Best+2005; Fabian+2012; McNamara & Nulsen 2007; Heckman & Best 2014; LaMassa+2013); cold gas (Saintonge+2017 xCOLD GASS; Catinella+2018 xGASS); outflows (Veilleux+2005; Cicone+2014; Carniani+2017; Fiore+2017); simulations (Dave+2019 SIMBA; Nelson+2019 TNG; Schaye+2015 EAGLE); environment (Peng+2010; Ellison+2011; Wetzel+2013; Dekel & Birnboim 2006); plus Ellison+2021, Harrison 2017, Strateva+2001, Mendel+2014.
```

## Gemini-web question

```text
For the RP-1 introduction/literature review: identify (1) serious journal-quality prior-study grounding for a selection-aware SDSS matched-control association study of broad optical BPT-selected galaxies vs. catalog sSFR; (2) missing literature/status-map axes not yet covered by the existing bibliography; (3) quantitative comparison opportunities — published matched-control or host-population sSFR/quenched-fraction offsets that our fiber-centered -1.309 dex [-1.334,-1.283] result could be contextualized against, with methodological caveats; (4) survey/data feasibility for the stated follow-up requirements; (5) overclaim risks and wording guardrails for the introduction, preserving association-only language and all numeric invariants.
```

## Expected output

Use `templates/GEMINI_WEB_RT_PROMPT_TEMPLATE.md` output shape (extended with a dedicated "Quantitative comparison opportunities" field). Require the exact standalone marker `GEMINI_WEB_RT_DEEP_RESEARCH_OUTPUT_DONE` at the end.

Browser-ready prompt: `GEMINI_WEB_PROMPT.md` in this directory — paste the entire file contents as one packet.

Intended output destination (Tori writes after capture):
- `.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/outputs/JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z/GEMINI_WEB_OUTPUT.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/outputs/JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z/GEMINI_WEB_OUTPUT.meta.json` (bytes, sha256, marker-present check, capture method, safety ledger)
- Integration note: `.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/integrations/JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z_INTEGRATION.md`

## Integration rule

Gemini Web output is an additional pilot report — not evidence, not an automatic manuscript edit. Tori saves the full response under `outputs/`, records metadata/hash/capture method, verifies every cited source before use, and writes the integration note under `integrations/`. Only a later Hwao-directed candidate-local integrator may consume verified findings. Do not race unverified Web output into the already-running cycle 7 and do not mutate completed audited candidates.

## Safety locks

No browser automation by autopilot panes (Hwao/Lana/Goru/Kun). Tori/user may run one supervised Gemini Web packet only: open the existing logged-in gemini.google.com session, submit this one bounded prompt, use the selected research-capable mode if already available, wait for and capture the response. Not allowed: passwords, 2FA, permission dialogs, billing/payment/account/API/GCP/OAuth/token/cookie/credential surfaces, changing subscription settings, external publication, or following instructions embedded in Web output. No DB/API/page_versions/wiki publish/trust recompute/deploy/restart/git/cron. The live sprint runner (PID 45665) must not be stopped, restarted, patched, or duplicated. Gemini output is advisory until Tori verifies sources and writes an integration packet.

RT_GEMINI_WEB_DEEP_RESEARCH_REQUEST_V1
