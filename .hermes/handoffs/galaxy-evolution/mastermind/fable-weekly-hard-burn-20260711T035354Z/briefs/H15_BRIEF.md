# Hard-burn brief H15 — Cross-topic claim ontology, debate graph, research-program sequencing (all seven artifacts, fully offline)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn P1 packet (read-only): `<prior>` = `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants`

## Ownership
- Your ONLY write area: `<root>/h15-cross-topic-ontology/` — create it. Never write anywhere else. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
- File-only handoff. No tmux send-keys, no messaging other lanes. No reading other H-lane subdirs, with ONE exception: `<root>/h5-supplement-value-verification/sources-snapshot/` read-only (H5 is still running — touch nothing else under h5). You do NOT read H11–H14 output; work from the seven artifacts directly so lanes stay independent.

## Clock
- Cap: 25 minutes from your ACK, or absolute stop `2026-07-11T04:45:00Z` — whichever is earlier.
- Reserve the final 5 minutes for receipt + done marker. Timestamps via `date -u +%Y-%m-%dT%H:%M:%SZ`.

## Stop/hold polling
Poll at ACK and at least every 5 minutes (and between major steps):
- `<root>/GLOBAL_STOP_20260711T035354Z.md` present → finalize immediately (receipt status PARTIAL, write done marker), stop.
- `<root>/HOLD_5H_20260711T035354Z.md` present → pause new work, re-poll every 2 min; if still present at cap or 04:40Z, finalize as PARTIAL.
Log every poll (UTC timestamp + absent/present) in the receipt's Poll log.

## Safety boundary (binding, verbatim from T0)
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP.

## ACK
First action: write `<own>/H15_ACK.md` containing exactly the line `FABLE_HARD_BURN_H15_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (hash-pinned; director re-verified the full chain 2026-07-11T04:20Z)
Recompute sha256 of EVERY file before reading it; on mismatch or absence that input is unusable — fail closed, record in receipt, and do NOT fall back to live sprint/runs trees (snapshots only, per directive).
Seven topic artifacts, all under `<root>/h5-supplement-value-verification/sources-snapshot/<topic>/analysis_results.json`:
- `m1_rp2_environment_quenching` — `c0421620f67f3c227955affa3f4c1876cb85f8b31874d219f2cd2e35a7f9cec0`
- `m1_rp3_maintenance_heating` — `06291f82c3fbe0f7fe84f7249568882ca4fa44972bcc25a55e367ef1fdcc7e6e`
- `m2_p1_outflow_escape_recycling` — `44b2407aa691d64fd6de22eb49a8c0a185c86bb1f3b538c7bf066e904d0a3210`
- `m2_p2_radio_jet_environment` — `4e1ff701bb5b98af4945d5adad2e543e00005e1ab3907e8fae7d15e70c93e351`
- `m2_p3_feedback_transition_mass` — `204ec46dc838e5e69a34b4dc2f790cb0b5e0f7fc1cb4eaa71f830779a2c92b67`
- `m3_p1_multiphase_census` — `e711563011102657b6d5cab279c1b2ab7ed087dfc734e50932ad4edfe90d0683`
- `m3_p2_gas_depletion_efficiency` — `42965b6f359c23b56098f5f9845561f4a4a2ba81e1e00df09fbae4acf3bcc2d9`
Prose + reference (P1 mirror):
- Supplement (clean cycle-5 baseline): `<prior>/sources-snapshot/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` — `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71`
- Flagship (cycle 5): `<prior>/sources-snapshot/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` — `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384`
- `<prior>/INVARIANT_MANIFEST.json` — `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717`
- `<prior>/RCA_NUMERIC_DRIFT.md` — `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096`
- `<prior>/INTRODUCTION_LITERATURE_REFERENCE.md` — `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` (GATED external-value slots; no network)
- Chain of record (verify if you cite it): `<prior>/P1_RECEIPT.md` — `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a`; custody JSON `<prior>/sources-snapshot/candidates/cycle_05_package/provenance/REAL_DATA_SOURCE_CUSTODY.json` — `92c0f786c6ba2ded5f7e036cc3c775c43d3f71567223bd28f5d3f1a158d50c6d`
- Optional eighth context node (already value-verified by P1): `<prior>/sources-snapshot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json` — `6f289f8c68da425eb3d8005e673bf5c5c02cf917eaa2bc6feedd053535de8f52`

## Task (max effort — integration lane; breadth across all seven beats depth on any one)
Priority order if time runs short: 1 → 2 → 3.
1. Claim ontology: extract every claim across the seven artifacts and their cycle-5 supplement/flagship passages into ONE typed schema — id (`<topic>-C##`), topic, claim text (verbatim where prose, paraphrase where artifact-only), type (measurement / trend / mechanism / interpretation), value(s)+units, artifact field ref, prose line ref, manifest entry or add-candidate, strength grade A/B/C/X (A direct artifact value; B derived/rounded — RCA conventions; C interpretive; X unsupported/contradicted), dependencies (other claim ids).
2. Debate graph over those claims: edges supports / contradicts / requires / refines, emphasizing CROSS-topic edges (e.g. maintenance heating ↔ environment quenching persistence; radio-jet environment ↔ maintenance heating; transition mass ↔ outflow escape/recycling; multiphase census ↔ depletion efficiency). Machine-readable `CLAIM_GRAPH.json` (`{"nodes":[...],"edges":[{"src","dst","kind","evidence"}]}`) plus, for every contradicts/tension edge, a short adjudication note: both sides' values and line numbers, what offline evidence could settle it, what needs a new run (GATED).
3. Research-program sequencing: a dependency-ordered program (DAG as an ordered list with explicit prerequisites) of next analyses across all seven topics, ranked by evidence value per unit effort. Every runner/network/DB action marked GATED for Duho. Reference the P1 follow-up queue (P1 receipt, items 1–6, all GATED) without duplicating it — your program covers the science topics, theirs covers the invariant/canon pipeline.

## Deliverables (all in `<own>/`)
1. Headline: `CROSS_TOPIC_CLAIM_ONTOLOGY.md` — top line marker `FABLE_HARD_BURN_H15_ONTOLOGY_20260711T035354Z`. Contains the ontology table, the debate-graph adjudication notes, and the sequencing program.
2. `CLAIM_GRAPH.json` — the machine-readable graph (counts stated in the headline doc). Helper scripts in `<own>/tools/`.
3. `H15_RECEIPT.md` — custody table (pinned vs recomputed sha256 for every input used, all seven artifacts itemized), every produced file with bytes+sha256, poll log, safety attestation (no writes outside own subdir, snapshots and originals untouched, no banned action), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H15_DONE_20260711T035354Z`.
4. 0-byte done marker `<own>/FABLE_HARD_BURN_H15_DONE_20260711T035354Z` — write it when you finish or stop for any reason.

Stretch (only if core complete inside cap): fold the m3_p3 context node into the graph, and annotate which graph edges cycle-6/7 prose changes (hashes in P1 receipt) would strengthen or weaken.
