# FLAGSHIP RUN-SIDE STATUS — what stands between now and the real spin-parity measurement
Hwao, 2026-09-03 11:4x KST. Plain words; digits. Nothing here starts work, opens a pixel, or changes frozen text.
Sources: V134 (P0-signed 2026-08-31 19:33 KST), DECISIONS_FOR_DUHO.md, ACQUISITION_COMPLETE_20260902.md,
STAGE2_REOPEN_OUTCOME_20260902.md, the run/ receipts, this lane's freeze record.

**Short answer to "spin comparison done?": no.** The Tier-A spin-parity measurement has not started. No real
image pixel has been read by any lane. What is done: all data is on disk, the text is frozen, and the
side-study (Tier-C concordance) is frozen and its gates are running today.

## 1. What the Tier-C concordance result gates or informs — and what it does not
It measures, on 17,947 bricks of galaxies OUTSIDE the flagship sample, how often the frozen machine
instrument and Galaxy Zoo 1 humans agree on winding direction. Receipt expected ~2026-09-04 (crossmatch
~23:30 KST tonight, then rendering + verdict after the seal gate). It **informs** one thing: whether a
SUCCESSOR preregistration could use GZ1 labels for calibration. It **gates nothing** on the flagship and
**feeds nothing** into it (your ruling "a"; V134 §14.4–14.6 forbid it). The flagship's calibration must come
from the hand-check committee named in V134 — no other actor is admitted.

## 2. Tier-A brick acquisition — DONE
| | |
|---|---|
| bricks | 12,117 of 12,117 (direction #52 closure) |
| on disk | 143.37 GiB, every brick SHA-256-verified against NERSC, 0 mismatches, 0 failures, 0 extras |
| finished | 2026-09-02 06:24 KST |
Sample: 49,211 galaxies (sealed mask, N_eq = 110,983) inside a 65,060-row parent. Pixels untouched.

## 3. Pre-pixel gates for the flagship (V134 §7 class P) — where each stands
Satisfied / receipted: **BS-2m** manifest closure (2026-08-26). Candidate receipts present in run/ for
**BS-1b, BS-2o, BS-2s, BS-3, BS-4, BS-5p, BS-7p** (their acceptance is checked at freeze-of-run, not
claimed here). **BS-1** (release branch) resolves BY RULE on **2026-09-05**: DR10.1 / Branch B auto-selects
unless DR11 photo-z appears first (measured absent 2026-08-30).
NOT satisfied — the real blockers, all **DESIGN** slots, each needing a text revision under the amendment
machinery (new version → hostile referee → your signature): **BS-2a** acceptance thresholds, **BS-2k**
custody provisioner (constants and rosters ruled; implementation unfilled), **BS-3g** sensitivity-gradient
control, **BS-2v** VOID converter (candidate REJECTED-UNBUILT-V1; BS-2c count closure is design-gated on
it). Then **BS-6** image-transport approval, which releases the first image byte.
Order of what follows once BS-6 exists: instrument runs χ on all 49,211 (machine only) → strata (χ tertiles ×
committee state) → hand-check allocation 3 × 9 → **BS-8f** calibration receipt → Stage C power (BS-5f) →
**BS-L** lock (you sign) → unblinding → verdict.

## 4. The measurement itself
Runtime: not measured on real bricks — the frozen instrument (successor_ref_v9, sha 6a9abbbd…) has only run on
fixtures. Known costs: the Stage-P nested permutation kernel measured ≈ 9 h per prefix (why Stage P uses one
20,000-permutation null per prefix); rendering + χ for 49,211 cutouts at 128×128 is hours, not days, on the
Studio. Blind protocol: V134 §6.1 lifecycle table — every χ-bearing object sealed, every read logged with a
chained access log, 11 refusal codes, unenumerated catch-all refusals block the lock. Unblinding rule: only
after BS-L, only if every calibration bin has a_LB ≥ 0.85 and Stage-C power passes; otherwise the run halts
INCONCLUSIVE-BY-CALIBRATION or INCONCLUSIVE-BY-POWER before any real-sky statistic exists. Verdict = frozen
decide() on Â_L against the Longo amplitude 0.0408.

## 5. Where your decisions fall (options, in order)
1. **The hand-check committee — the true wall.** V134 needs ≥ 30 real human labels per live stratum (9 strata)
   and ≥ 10 per non-empty joint cell (3 × 9): roughly 300–800 human labels by admitted checkers, blind, on
   the allocated sample only. Options: (a) name the 3 checkers now (you + 2) so BS-8p allocation can be
   built; (b) run the machine half first (after BS-6) and decide the committee when the strata are known;
   (c) defer the flagship image half and let the Tier-C result inform a successor design using GZ1 labels.
   Note: (b) is allowed by the text — strata need χ first — so the committee is not what blocks starting.
2. **The 4 DESIGN slots.** Each is a signed text revision. Options: (a) authorise Hwao to draft all 4 as
   V135–V138 back-to-back with codex/agy rounds, you sign each; (b) one at a time, BS-2v first (it gates
   BS-2c).
3. **BS-6 image-transport approval** once the slots close — you approve the closed manifest sha and byte
   ceiling. Options: approve as filed / hold.
4. **BS-1 on 2026-09-05** — nothing to decide unless you want to override the by-rule branch (direction #19
   said no override before the date).
5. **BS-L** at the end — your lock signature; then the one-use unblinding receipt.

## 6. Seat / cost budget (estimates)
Text revisions: ~3 hostile rounds each ≈ 1 h wall, ~4 codex + 4 agy calls; the 4 DESIGN slots ≈ 1–2 days of
seat work at today's cadence, Fable judgment only at gates. Machine half: Studio compute, hours; NOIRLab/NERSC
traffic nil (bricks are local). Human half: 300–800 labels ≈ 5–15 person-hours across 3 checkers. Tier-C
side-study finishes on its own by ~2026-09-04 with ~2 more seat rounds (render verdict + referee).

**Next, if you say "go":** V135 = BS-2v (VOID converter) draft under §17.6 discipline; nothing else moves.

---
**Correction (Hwao, 11:5x KST, after re-reading the run/ record):** §3 above understates BS-2v. The
candidate was REJECTED-UNBUILT-V1 on 09-01 15:51 KST, then REBUILT the same day by codex on the frozen
text's mandated path (a successor-layer `receipt_strict` schema `BS2V-V1`, six authenticated fields) and
verified **SOUND** by agy (AGY_BANK_VERIFY_20260901.md); `run/classp_candidates/BS-2v.json` exists and
passes its gate. What BS-2v still lacks is exactly what §7 says a DESIGN slot needs: the **text revision**
that pins the registry digest and the successor schema and marks the slot FILLED — that is V135. BS-2c's
candidate receipt is still absent (its count-closure run was relaunched 09-01; no `BS-2c.json` yet).
