# Hard-burn brief H6 — Adversarial audit of P1 invariant manifest + RCA (stretch wave)

Burn: `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`)
Root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z`
Prior burn root (read-only inputs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`

## Ownership
- Your ONLY write area (`<own>`): `<root>/h6-p1-invariant-rca-audit/` — create it. Never write anywhere else on the machine. Do not modify T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. Do not create STOP/HOLD files.
- Independent lane: no dependency on H1–H5 or the other stretch lanes. File-only handoff; no tmux send-keys; do not read any other `h*` subdir.

## Clock
- Cap: 35 minutes from your ACK, or absolute stop `2026-07-11T04:45:00Z` — whichever is earlier.
- Reserve the final 5 minutes for receipt + done marker. Timestamps via `date -u +%Y-%m-%dT%H:%M:%SZ`.

## Stop/hold polling
Poll at ACK and at least every 5 minutes (and between major steps):
- `<root>/GLOBAL_STOP_20260711T035354Z.md` present → finalize immediately (receipt status PARTIAL, write done marker), stop.
- `<root>/HOLD_5H_20260711T035354Z.md` present → pause new work, re-poll every 2 min; if still present at cap or 04:45Z, finalize as PARTIAL.
Log every poll (UTC timestamp + absent/present) in the receipt's Poll log.

## Safety boundary (binding, verbatim from T0)
Safe offline artifacts only. No network/browser, runner/candidate writes, DB/API/wiki publication, deploy/restart, git, cron/launchd/background jobs, billing/account/credentials, cloud/GCP. This audit is read-only on every input and performs ZERO network calls.

## ACK
First action: write `<own>/H6_ACK.md` containing exactly the line `FABLE_HARD_BURN_H6_ACK_20260711T035354Z` plus your UTC start timestamp.

## Inputs (verify pinned sha256 before use; on mismatch, record in receipt and treat that input as unusable — fail closed)
All under the prior burn root, `p1-rp1-invariants/`:
- `INVARIANT_MANIFEST.json` — `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717`
- `RCA_NUMERIC_DRIFT.md` — `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096`
- `INTRODUCTION_LITERATURE_REFERENCE.md` — `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d`
- `P1_RECEIPT.md` — `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a`

## Task (adversarial, max effort — hunt defects, do not summarize; prefer exhaustive coverage over early finish)
Try to break the P1 packet. Checks, each recorded with verdict CLEAN / DEFECT / UNVERIFIABLE-OFFLINE plus evidence:
1. Manifest integrity: valid JSON; unique invariant ids; legal status values used consistently; every entry carries value, units, provenance/source; no duplicate or mutually contradictory invariants.
2. Arithmetic recompute: every derivable number in manifest and RCA (counts, deltas, drift magnitudes, percentages) recomputed by hand; mismatches are DEFECTs.
3. RCA causal chain: each root-cause claim in `RCA_NUMERIC_DRIFT.md` must be backed by evidence inside the packet; flag unsupported leaps, circular reasoning, and alternative causes the RCA ignores.
4. Cross-doc consistency: manifest ↔ RCA ↔ EXT-1…EXT-4 slots in the literature reference — same fact must carry the same value everywhere.
5. Receipt custody recheck: recompute sha256 + bytes for every file `P1_RECEIPT.md` lists and compare against its claims.

## Deliverables (all in `<own>/`)
1. Headline: `P1_INVARIANT_RCA_ADVERSARIAL_AUDIT.md` — top line marker `FABLE_HARD_BURN_H6_P1_AUDIT_20260711T035354Z`. Must contain: findings table (id H6-F01…, severity BLOCKER/MAJOR/MINOR/NOTE, exact file+line/quote, why wrong, proposed disposition), the full check log (all 5 check families with per-check verdicts — clean checks count as content), and a packet verdict: PASS / PASS-WITH-FIXES / FAIL.
2. `H6_RECEIPT.md` — input custody results (pinned vs recomputed sha256), every produced file with bytes+sha256, poll log, safety attestation (no writes outside `<own>`, no banned action, zero network calls, prior burn root untouched), status COMPLETE or PARTIAL, ending with the exact line `FABLE_HARD_BURN_H6_DONE_20260711T035354Z`.
3. 0-byte done marker `<own>/FABLE_HARD_BURN_H6_DONE_20260711T035354Z` — write it when you finish or stop for any reason; the receipt status carries COMPLETE/PARTIAL.
