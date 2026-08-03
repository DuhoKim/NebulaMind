# Integrated 9-paper local handoff

Marker: `INTEGRATED_9_PAPERS_HANDOFF_20260709T013015Z`

Run ID: `INTEGRATED_9_PAPERS_20260709T012051Z`

## User directive

Proceed with the recommended integration order from the overnight 9-paper swarm report:

1. Create a new local integration run directory.
2. Integrate the shared selection-function module into all 9 manuscripts.
3. Make M1 RP-1 the flagship short paper.
4. Convert the other 8 into a guarded denominator/proxy suite or appendices.
5. Integrate citations by role: actual method support vs future-data motivation.
6. Recompile all local PDFs.
7. Run a Kun-style audit.
8. Stop before public replacement/publish.

## Result

Completed as a local-only integration run.

- New local run directory: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z`
- Generated integrated AASTeX sources for 9 active consolidated Galaxy Evolution paper drafts.
- Compiled 9/9 PDFs with Tectonic.
- Ran a Kun-style audit: 9/9 PDFs valid, 9/9 compile logs clean of fatal/error markers, 9/9 source JSON files parsed, 10/10 figures present/nonzero, 0 fatal failures.

## Scientific packaging decision implemented

### Flagship

1. `m1_rp1_sdss_agn_sfr`
   - Status: flagship short-paper draft.
   - Claim: broad optical BPT AGN hosts in the capped SDSS DR17 four-line emission subset have lower catalog sSFR than mass-redshift matched star-forming controls.
   - Guard: association only; not causal AGN feedback.

### Guarded proxy / denominator suite

2. `m1_rp2_environment_quenching`
   - SDSS nearest-neighbour density proxy for environmental quenching.
   - Not a halo/group/central-satellite quenching proof.

3. `m1_rp3_maintenance_heating`
   - Optical AGN denominator for maintenance-heating follow-up.
   - Not a radio/X-ray/cavity/hot-gas heating measurement.

4. `m2_p1_outflow_escape_recycling`
   - High-excitation optical AGN denominator.
   - Not an outflow velocity/escape/recycling measurement.

5. `m2_p2_radio_jet_environment`
   - Optical BPT-AGN fraction versus internal density proxy in massive hosts.
   - Not a radio jet coupling or hot-gas test.

6. `m2_p3_feedback_transition_mass`
   - SDSS mass-vector and optical incidence diagnostic.
   - Not a causal feedback-transition proof.

7. `m3_p1_multiphase_census`
   - Optical tracer-threshold denominator.
   - Not a multiphase outflow census.

8. `m3_p2_gas_depletion_efficiency`
   - Optical denominator/H-alpha proxy baseline for gas follow-up.
   - Not a gas-fraction, depletion-time, or star-formation-efficiency measurement.

9. `m3_p3_simulation_validation`
   - Observed SDSS target vector.
   - Not a simulation validation/rejection/ranking paper.

## Shared selection module integrated into every manuscript

Every generated TeX source includes a shared section titled `Shared parent sample and selection function` with these core numbers:

- Cached row-level table: 60,000 rows.
- Strict public four-line S/N>=3 eligible parent: 249,917 rows.
- Cached coverage of strict public parent: 24.0%.
- Public spectro-z parent, 0.02<z<0.12: 501,060 rows.
- Positive four-line flux/error parent: 373,445 rows.
- S/N>=5 parent: 176,523 rows.
- S/N>=10 parent: 91,768 rows.
- Four-line selection is sSFR-dependent: S/N>=3 keeps 33.6% of the `-12 < log sSFR < -11` parent bin and 94.9% of the `-10 < log sSFR < -9.5` parent bin.
- Cached-vs-public marginal differences did not exceed 5 percentage points in redshift, stellar mass, or sSFR, but the cache remains capped and non-random.

## Flagship RP-1 integrated result numbers

The RP-1 manuscript now uses overnight Goru robustness numbers:

- Broad BPT optical AGN vs star-forming controls at S/N>=3:
  - matched pairs: 8,146
  - median delta log sSFR: -1.309 dex
  - 95% bootstrap interval: [-1.334, -1.283] dex
- Moderate mass-redshift caliper:
  - retained pairs: 7,867
  - target coverage: 96.6%
  - median offset: -1.318 dex
- No-replacement stress test:
  - pairs: 7,419
  - median offset: -1.446 dex
  - explicitly described as a diagnostic with poorer balance, not preferred estimator
- S/N>=10 sensitivity:
  - pairs: 1,530
  - median offset: -0.744 dex
- Narrower [N II] Seyfert-like proxy:
  - pairs: 2,114
  - median offset: -0.763 dex

## Compiled PDFs

1. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf`
   - SHA256: `775111b2b7802dfa562eefe96f7b85b43e6d7513a712eec6bf4026babcd4be7a`

2. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf`
   - SHA256: `4f21a374f59c5242789dd9f2c371d2ff0e79242f76668a5300fd82cda0c4b1d2`

3. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf`
   - SHA256: `5c0f16a7bf37dc5a8826eb155df75079dd591e07c905f11d911364d9ec3344b5`

4. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf`
   - SHA256: `853b83d305b2c6ab2f69ef3f0f97edd84e9876ae1a7e88edd8589ee59176bb45`

5. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf`
   - SHA256: `a686c95f782f669a9af7863ecded77bd5b890abf06d925cf6138934055ef307b`

6. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf`
   - SHA256: `6e6606eaa61c90b2eb5a4b19650e3bd32e21acb4060252473a6606142782e31f`

7. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf`
   - SHA256: `50f4c5dee581c6b93c5b2fcb5f1e33b445b0353392f96f6fc489037b66ca809f`

8. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf`
   - SHA256: `f5c970a0307410b5f35ce9a5b22470adbfae621850650c80b41244d99d717444`

9. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf`
   - SHA256: `d9fe74cac5aaaab5bc1f8ea994752d6f92d8d2431559d50411e38830584be958`

## Verification artifacts

- Precompile manifest: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_MANIFEST_PRECOMPILE.json`
- Audit JSON: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_AUDIT.json`
- Audit Markdown: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/INTEGRATION_AUDIT.md`
- Generator script: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/build_integrated_9_papers.py`

## Compile/audit status

From `INTEGRATION_AUDIT.md`:

- papers: 9
- pdfs_ok: 9
- compile_logs_ok: 9
- json_ok: 9
- total_figures: 10
- figures_ok: 10
- fatal_failures: 0

Warnings remain AASTeX/line-break style warnings only. They are recorded in each compile log; no fatal/error/halted markers are present after the fix.

## What changed relative to the previous public-linked PDFs

This integration created new local PDFs only. It did not replace the 9 public-linked PDFs. The new drafts are more scientifically honest and better integrated because they:

- put the shared selection-function disclosure before topic results;
- explicitly state that the 60,000-row cache is capped and non-random;
- classify RP-1 as the only flagship short-paper candidate;
- demote the other 8 active consolidated proposals to guarded denominator/proxy drafts;
- separate citations that support actual SDSS/BPT/catalog methods from citations that only motivate future radio/X-ray/CO/outflow/simulation observables;
- preserve exact local reproducibility paths and hashes.

## Recommended next decision

Do not publish/replace public PDFs yet without a human science review.

Recommended next local step:

1. Have Lana/Hwao review the RP-1 integrated PDF as the candidate flagship paper.
2. Decide whether the other 8 should remain standalone guarded PDFs or become appendices/supplementary denominator notes under one combined suite paper.
3. If approved, run a final prose-polish pass on RP-1 only, then recompile and audit.
4. Only after explicit approval, replace public-linked PDFs or add a new public `Integrated local drafts` section.

## Safety ledger

No DB writes, SQL, `/api/pages`, `page_versions`, wiki publish, trust recompute, public/live page mirroring, deploy/restart, git commit/push/merge, cron creation/update, billing/cloud/OAuth/API-key changes, or external manuscript submission were performed.
