# Hard-burn brief H13 — Deep synthesis: outflow escape/recycling + feedback transition mass (m2_p1 + m2_p3, fully offline)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn P1 packet (read-only): `<prior>` = `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants`

## Ownership
- Your ONLY write area: `<root>/h13-outflow-transition-synthesis/` — create it. Never write anywhere else. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
- File-only handoff. No tmux send-keys, no messaging other lanes. No reading other H-lane subdirs, with ONE exception: `<root>/h5-supplement-value-verification/sources-snapshot/` read-only (H5 is still running — touch nothing else under h5).

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
First action: write `<own>/H13_ACK.md` containing exactly the line `FABLE_HARD_BURN_H13_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (hash-pinned; director re-verified the full chain 2026-07-11T04:20Z)
Recompute sha256 of EVERY file before reading it; on mismatch or absence that input is unusable — fail closed, record in receipt, and do NOT fall back to live sprint/runs trees (snapshots only, per directive).
- Topic artifact A: `<root>/h5-supplement-value-verification/sources-snapshot/m2_p1_outflow_escape_recycling/analysis_results.json` — `44b2407aa691d64fd6de22eb49a8c0a185c86bb1f3b538c7bf066e904d0a3210`
- Topic artifact B: `<root>/h5-supplement-value-verification/sources-snapshot/m2_p3_feedback_transition_mass/analysis_results.json` — `204ec46dc838e5e69a34b4dc2f790cb0b5e0f7fc1cb4eaa71f830779a2c92b67`
- Supplement prose (clean cycle-5 baseline): `<prior>/sources-snapshot/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` — `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71`
- Flagship (cycle 5): `<prior>/sources-snapshot/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` — `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384`
- `<prior>/INVARIANT_MANIFEST.json` — `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717`
- `<prior>/RCA_NUMERIC_DRIFT.md` — `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096`
- `<prior>/INTRODUCTION_LITERATURE_REFERENCE.md` — `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` (GATED external-value slots; no network)
- Chain of record (verify if you cite it): `<prior>/P1_RECEIPT.md` — `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a`; custody JSON `<prior>/sources-snapshot/candidates/cycle_05_package/provenance/REAL_DATA_SOURCE_CUSTODY.json` — `92c0f786c6ba2ded5f7e036cc3c775c43d3f71567223bd28f5d3f1a158d50c6d`

## Task (max effort — deep synthesis, not a value audit; H5 owns value-level verification)
Priority order if time runs short: 1 → 2 → 3 → 4 → 5.
1. Artifact anatomy for BOTH artifacts: parse every field; restate each measurement design in plain language (sample, denominators, statistic, uncertainties); enumerate every numeric with units and role. Include an explicit unit/dimension audit of every quantity (velocities, masses, fractions, thresholds).
2. Claim inventory for both topics from cycle-5 supplement + flagship: claim text (verbatim, line no.) → artifact field(s) → manifest entry or add-candidate → strength grade A / B (show derivation, RCA rounding conventions) / C / X.
3. JOINT synthesis — the lane's center of mass: does the feedback transition mass actually partition the outflow escape vs recycling regimes as the prose implies? Cross-checks: any shared mass scales/thresholds quoted in both artifacts or both prose sections (exact values, line numbers); regime boundaries mutually consistent; offline energetics/bookkeeping sanity checks that need no external data. Consistency table (agrees / independent / in tension) + tension list.
4. Confounders per topic (outflow tracer choice, projection, escape-velocity assumptions, mass-bin edges) — each "addressable with current artifact (how)" or "requires new run (GATED)".
5. Falsifiable predictions + next analyses, dependency-ordered; runner/network/DB actions GATED.

## Deliverables (all in `<own>/`)
1. Headline: `OUTFLOW_TRANSITION_MASS_SYNTHESIS.md` — top line marker `FABLE_HARD_BURN_H13_SYNTHESIS_20260711T035354Z`. Substantial: both claim inventories + joint regime-consistency analysis. Helper scripts in `<own>/tools/`.
2. `H13_RECEIPT.md` — custody table (pinned vs recomputed sha256 for every input used), every produced file with bytes+sha256, poll log, safety attestation (no writes outside own subdir, snapshots and originals untouched, no banned action), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H13_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H13_DONE_20260711T035354Z` — write it when you finish or stop for any reason.

Stretch (only if core complete inside cap): diff cycle-6/7 supplement snapshots (hashes in P1 receipt) for passages on either topic; note wording/value changes.
