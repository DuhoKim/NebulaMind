# Trio overnight report — BHU half (Tori, 2026-08-25 10:50 KST)

Evidence classes: [M] = measured/computed with receipt in-lane; [A] = asserted/testimony.
Gate states quoted at artifact-first-line strength only.

## Plain-language lead (for the merged report's BHU section)

The night settled one thing for the BHU lane: the frozen bounds table for Phase 4 is now
guarded by a verifier that eight kinds of quote corruption cannot get past — because one
reviewing engine spent the whole night inventing corruptions and won five rounds before this
morning's version finally held them all. The physics freeze itself never changed; what got
rebuilt, five times, was the proof that its fifty quotes are real.

## Timeline (git-stamped [M])

- 08-24 18:49–18:50 — verifier v4 committed after codex's first HOLD proved v3 could pass a
  numerically corrupted quote; freeze receipt binding claim corrected (43 declared / 7
  flagged), both Track B gates relaunched after the 18:00 tmux topology reboot killed the
  first kimi run. [M: commits 4445e363, 9ac99685]
- 08-24 19:04 — kimi gate verdict, first line: **PASS_TRACK_B_FREEZE**. [M: KGATE_TRACKB_VERDICT.md]
- 08-24 22:14 — v5: ordered signed expressions, explicit per-entry bindings
  (b_binding_map.json), 50-row span ledger. [M: fc03ddd9]
- 08-24 22:36 — v6: operator conflict-detection (± cannot become ×); three quotes whose PDF
  text layers scramble reading order re-verified against fetched arXiv LaTeX sources. [M: dcd7a8e5]
- 08-24 22:40 — Track C brief committed: judgment criteria PRE-REGISTERED before any
  comparison (four morphology criteria, verdict ceiling fixed at consistency-only-with-
  surface, literature disputes fenced). [M: ae0af84b]
- overnight — codex regate3 deliberated; verdict landed by 10:14 with the operator-DELETION
  hole. [M: REGATE3 file; A: exact landing time not stamped]
- 08-25 10:18 — v7: tight-pair deletion asymmetry + sentence-level matching. [M: a3a2b2c4]
- 08-25 10:41 — regate4 verdict read: sentence-final numeric loss, two actual-row corruptions
  demonstrated. [M: REGATE4 file]
- 08-25 10:42 — v8: sentence-final numbers retained; BOTH of the gate's actual-row corruptions
  embedded as self-tests through the corpus row path. Eight corruption cases, all failing.
  [M: 736007f0; self-test output in commit tree]

## Current gate state (first lines, verbatim [M])

- Track A (the strict interior model): **PASS_TRACK_A_AMENDED** (codex regate3 of Track A) +
  **PASS_TRACK_A** (kimi). CLOSED.
- Track B freeze: kimi **PASS_TRACK_B_FREEZE**; codex chain GATE→REGATE4 all first-line HOLD
  (latest: HOLD_TRACK_B_FREEZE, sentence-final residue, repaired in v8); **REGATE5 RUNNING
  now** — no stronger claim is available at publish time.
- Track C: brief committed, pre-registered; NOT STARTED (starts on Duho's go after the freeze
  passes).

## Numbers for Goru's cross-check (all [M], receipts in bhu-theory-phase4-anisotropy-20260823/)

- 50/50 quotes verified, 0 manual acceptances, 0 directory fallbacks (b_verify_ledger.json,
  50 rows; verifier v8 sha256 ecadfb540edd8410…, ledger 6106ab889df4a61c…).
- 8 corruption self-tests failing (6 classes + 2 actual-row cases).
- Frozen bounds rows: B2 = 11 entries, B3 = 7 entries, B1 = reference tier (TRACK_B_FREEZE.md).
- Verifier versions in the night: v4→v8 (5 rebuilds); codex verdicts: 1 gate + 4 regates, all
  HOLD; kimi: 1 gate, PASS.
- Watch: verified for Aug 31 tick (lane state last_run 2026-08-24T06:07:24Z, last_error null,
  seen 25). Nothing fired overnight (weekly schedule; next Monday 10:00 KST).

## Handoff notes for the merge

- The BHU section must NOT say the freeze "passed" — kimi passed it, codex has it on HOLD with
  regate5 running. Say exactly that.
- If regate5 lands before publish, update the line to its first word and nothing more.
