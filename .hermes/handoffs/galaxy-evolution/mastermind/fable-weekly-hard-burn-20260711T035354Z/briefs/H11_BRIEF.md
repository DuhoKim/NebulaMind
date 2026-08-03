# Hard-burn brief H11 — Deep synthesis: environment quenching (m1_rp2, fully offline)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn P1 packet (read-only): `<prior>` = `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants`

## Ownership
- Your ONLY write area: `<root>/h11-environment-quenching-synthesis/` — create it. Never write anywhere else. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
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
First action: write `<own>/H11_ACK.md` containing exactly the line `FABLE_HARD_BURN_H11_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (hash-pinned; director re-verified the full chain 2026-07-11T04:20Z)
Recompute sha256 of EVERY file before reading it; on mismatch or absence that input is unusable — fail closed, record in receipt, and do NOT fall back to live sprint/runs trees (snapshots only, per directive).
- Topic artifact: `<root>/h5-supplement-value-verification/sources-snapshot/m1_rp2_environment_quenching/analysis_results.json` — `c0421620f67f3c227955affa3f4c1876cb85f8b31874d219f2cd2e35a7f9cec0`
- Supplement prose (clean cycle-5 baseline): `<prior>/sources-snapshot/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` — `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71`
- Flagship (cycle 5): `<prior>/sources-snapshot/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` — `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384`
- `<prior>/INVARIANT_MANIFEST.json` — `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717`
- `<prior>/RCA_NUMERIC_DRIFT.md` — `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096` (rounding/drift conventions)
- `<prior>/INTRODUCTION_LITERATURE_REFERENCE.md` — `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` (GATED external-value slots; no network)
- Chain of record (verify if you cite it): `<prior>/P1_RECEIPT.md` — `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a`; custody JSON `<prior>/sources-snapshot/candidates/cycle_05_package/provenance/REAL_DATA_SOURCE_CUSTODY.json` — `92c0f786c6ba2ded5f7e036cc3c775c43d3f71567223bd28f5d3f1a158d50c6d`

## Task (max effort — deep synthesis, not a value audit; H5 owns value-level verification)
Priority order if time runs short: 1 → 2 → 3 → 4 → 5.
1. Artifact anatomy: parse every field of the m1_rp2 `analysis_results.json`. Restate the measurement design in plain language (sample, denominators, statistic, uncertainties). Enumerate every numeric with units and role.
2. Claim inventory: locate every cycle-5 supplement and flagship passage about environment quenching (grep for the topic key, section headings, and its values). Table: claim text (verbatim, line no.) → supporting artifact field(s) → manifest entry (ID if present, else add-candidate) → strength grade A (direct artifact value) / B (derived or rounded — show the derivation, RCA conventions) / C (interpretive, no direct number) / X (unsupported or contradicted).
3. Physics synthesis: what these numbers do and do not establish about environmental quenching (satellite vs central, density/halo trends, quenched-fraction excess). Every sentence tagged DATA-SUPPORTED / INTERPRETATION / GATED-EXTERNAL (literature slots only — no network).
4. Confounders and alternatives: selection effects, aperture, SFR indicator, mass-matching, environment-metric choice. Each marked "addressable with current artifact (how)" or "requires new run (GATED)".
5. Falsifiable predictions + next analyses as a dependency-ordered list; anything touching runner/network/DB is GATED for Duho.

## Deliverables (all in `<own>/`)
1. Headline: `ENVIRONMENT_QUENCHING_SYNTHESIS.md` — top line marker `FABLE_HARD_BURN_H11_SYNTHESIS_20260711T035354Z`. Substantial: complete claim inventory + all five sections. Any helper scripts in `<own>/tools/`.
2. `H11_RECEIPT.md` — custody table (pinned vs recomputed sha256 for every input used), every produced file with bytes+sha256, poll log, safety attestation (no writes outside own subdir, snapshots and originals untouched, no banned action), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H11_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H11_DONE_20260711T035354Z` — write it when you finish or stop for any reason.

Stretch (only if core complete inside cap): diff cycle-6/7 supplement snapshots (hashes in P1 receipt) for environment-quenching passages and note any topic-relevant wording/value changes.
