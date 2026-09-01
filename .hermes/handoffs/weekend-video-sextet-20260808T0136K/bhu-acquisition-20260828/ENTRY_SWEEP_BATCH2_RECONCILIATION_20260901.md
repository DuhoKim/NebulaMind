# BHU sweep — BATCH 2 / completion reconciliation (Tori, 2026-09-01)

Resolves the batch-1 open items under Duho's rulings **A(a), B(a), C(a)** (RELAY). Completes the
27-onward sweep. Seat files: `ENTRY_SWEEP_BATCH2_agy_RESULT.md` (53/55/56/57), `ENTRY45_kimi_RESULT.md`.

## Rulings applied

**B(a) — entry 27 → QUALITATIVE-DIRECTIONAL (TIER CHANGE, landed).** Both seats found CONSISTENCY-ONLY
too weak; it is the SAME Gaztañaga causal-horizon CMB cutoff (θ≈60°, cf. measured Θ_H=66±9°) as entries
25/26, ruled QUALITATIVE-DIRECTIONAL at q3. Promoted to match, no calibration (no C_ℓ amplitude).
Bibliography tier line + §0 tally updated (directional 7→8, consistency 32→31, sums to 51). codex
`2204.11608_clean.txt:12-13,292-306,331-339`.

**A(a) — closure counts as directional only when DERIVED, not assumed. Entries 40/41/52 → CONSISTENCY-ONLY (tier holds).**
codex read all three as *assumed* closed-FLRW ansatz, not mapped to an observable; agy's batch-1 flags
were the lenient "it's closed = directional" that A(a) rejects. **Corroborated independently:** the record
already carries a 2026-08-28 blind-flag on 40 and 41 proposing promotion to QUALITATIVE-DIRECTIONAL that
was *deliberately not acted on* ("a candidate from a biased instrument, not a finding. Do not promote on
it."). A(a) confirms that standing decision. No tier change.

**C(a) — entry 45 third read (kimi) → CONSISTENCY-ONLY (tier holds).** Split was codex (too-weak) vs agy
(confirmed). kimi (`ENTRY45_kimi_RESULT.md`): the |C₁|²coth(πω̃/κ) departure from Planck is derived and
signed (codex right on the math), but the authors disclaim relevance to our universe (line 41 "may not be
directly relevant to observable Universe", line 97 WH "may not exist in current observable Universe"), so
it fails the "observable in OUR universe" conjunct AND the falsifiability leg (a null can't contradict it —
non-detection is explained by WH instability). Baseline T_H=1/(8πGM) is the borrowed Hawking result.
**Tally: codex too-weak, agy + kimi CONFIRMED (2–1) → CONSISTENCY-ONLY.**

## Reliable re-read of the batch-1 agy-degraded tail — all CONFIRMED

The 12-entry batch-1 overloaded agy (wrong source on 53, hallucinated identities on 55/56/57). Re-run as
a small batch with exact source paths, agy now reads the correct papers (receipts verify) and CONFIRMS
all four, matching codex's batch-1 reads:

| entry | codex (b1) | agy (b2, reliable) | outcome |
|---|---|---|---|
| 53 (`1906.11824`) | CONFIRMED | CONFIRMED | tier holds |
| 55 (`2007.06664`) | CONFIRMED | CONFIRMED | tier holds |
| 56 (`gaztanaga_mass_mnras.pdf`) | CONFIRMED | CONFIRMED | tier holds (stays QUALITATIVE-DIRECTIONAL) |
| 57 (`smoller_temple_1997`) | CONFIRMED | CONFIRMED | tier holds |

## Sweep result (entry 27 onward) — COMPLETE

12 entries audited blind-double. **Exactly ONE tier change: entry 27 → QUALITATIVE-DIRECTIONAL.** Eleven
confirmed at their existing tier:
- CONFIRMED CONSISTENCY-ONLY: 36, 40, 41, 45, 46, 49, 52, 53, 55, 57.
- CONFIRMED QUALITATIVE-DIRECTIONAL: 56.
Excluded (with reason): support 29/30/32/33/34/35/58; already-swept 28/31/37/38/39/43/48/50/54; sourceless
holdouts 42/47; Duho-ruled+gated calibrated-falsifiers 44/51.

Operational lesson recorded: cap agy at ~5 entries per `--print` turn and always hand it exact source
paths (the 12-batch degradation was source-location failure under load, not a reasoning failure).
Bibliography annotations for the 11 confirmed entries are recorded here (batched, per the no-per-entry-Fable
discipline); only the entry-27 tier change is written into the entry + tally.
