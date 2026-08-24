HOLD_UNSOUND_NUMERIC_RELATIONS_AND_SOURCE_BINDING_RESIDUE

# Phase 4 Track B freeze regate (codex)

## Verdict

The v4 repair does not discharge `GATE_TRACKB_VERDICT.md`. It fixes the original short-number omission and embeds the exact corrupted-value control, but it still verifies only an unordered set of unsigned numeric fragments, not the signed/ranged/associated numerical claims in each quote. I produced two new numeric-only corruptions that v4 accepts. In addition, 7/50 rows remain directory-wide fallbacks rather than per-entry source bindings, and the purported per-quote ledger lacks source spans for 42/50 rows. These are direct residues against the prior gate's required repair, so the Track B freeze remains on HOLD.

## Blocking residue 1 — value order and sign are erased, so corrupted numerical claims still pass

`b_verify_quotes.py:18-29` normalizes range dashes and minus signs and then deletes all non-alphanumeric punctuation before extracting bare digit strings. `numtokens()` returns a sorted set. `shingles()` removes numeric words before prose comparison (`b_verify_quotes.py:31-33`). Acceptance therefore proves only that each distinct unsigned numeric fragment occurs somewhere in one source file; it does not prove sign, range direction, uncertainty/value association, exponent sign, repetition, or token order.

Independent counterexamples against the currently pinned source bytes:

1. B3.1 genuine quote: `5–10% at ℓ ≲ 40 ... 2.5–3 σ`.
   Corrupted quote: `10–5% at ℓ ≲ 40 ... 3–2.5 σ`.
   Both produce tokens `['10', '2.5', '3', '40', '5']`, shingle score `0.750`, and `accepted=True` against `anomaly_planck2013_1303.5075v2_pages.txt`.
2. Cowell quote: changing `3.15 × 10^{-5}` to `3.15 × 10^{+5}` changes the quoted value by ten orders of magnitude. Both forms produce the same token set, shingle score `0.529`, and `accepted=True` against `mnras_template.tex`; neither normalized form retains the exponent sign.

The mandatory self-test did run and held: the genuine B3.1 quote passed and the prior `99–88% ... 9.9–8.8σ` counterexample failed. That control tests replacement with absent numeric fragments. It does not test whether the verifier preserves relations among fragments, and the two counterexamples above demonstrate that it does not.

Required repair remains: represent and match complete numeric expressions, preserving sign, exponent, range endpoints and direction, uncertainty/value association, repetition, and adjacent units/confidence qualifiers. A set-membership test over bare fragments is not boundary-aware claim verification.

## Blocking residue 2 — 7 entries are not bound to their own declared source

The rerun ledger has exactly 43 rows with `bound_to_declared: true` and 7 with `false`. At `b_verify_quotes.py:72-73`, an entry with no resolved declaration is bound to the entire source-directory corpus. The seven fallback rows span Migkas 2020, Migkas 2021, Dam 2023 (two quotes), Hu 2024 (two quotes), and Cowell 2023.

The freeze receipt honestly flags this 43/50 split, and the selected best filenames appear plausible. Honesty is credited, but a flagged directory-wide fallback is not the per-entry source binding required by the prior HOLD. Each of those seven entries already carries enough bibliographic identity (author/year, DOI, arXiv ID) to declare and pin its exact local source explicitly.

## Blocking residue 3 — the ledger is not a per-quote source-span ledger

The regenerated JSON has 50 rows, but `b_verify_quotes.py:107-109` stores only `q[:100]`; 49/50 stored quote fields are exactly 100 characters long. Only 8/50 rows contain `best.spans`; 42 automatically accepted rows contain no source span at all. The seven `PASS_NUMERIC` rows record snippets around only up to two individual tokens (`b_verify_quotes.py:90-96`), which need not be one quote-local span and do not establish the association among all values.

Thus the file is a 50-row acceptance ledger, but it does not satisfy the prior requirement for each quote's complete identity, extracted expressions, and source span(s). Required repair: store the full quote (or immutable quote ID plus full-quote hash and exact harvest offsets), exact bound source path/hash, and a coherent source offset/span or expression-level offsets sufficient to reproduce every accepted relation.

## Manual acceptance accounting — attack failed

Manual acceptance is explicitly identified as zero. `MANUAL_ACCEPT = {}` and no ledger row has a `manual:` basis. The rerun basis closure is 42 `auto` + 7 `PASS_NUMERIC` + 1 `PASS_PHRASE` = 50. This part of the required repair is discharged.

## Rerun, ledger closure, and pins — attacks failed

I reran the current `b_verify_quotes.py` from the lane root. It executed the mandatory self-test, then reported:

- `gpt2_trackb_cmb: 43 PASS / 0 FAIL`
- `agy_trackb_h0: 7 PASS / 0 FAIL`
- `TOTAL: 50 PASS / 0 FAIL; ledger rows=50`

The rerun reproduced `b_verify_ledger.json` byte-for-byte. Independent ledger counts are: 50 PASS, 0 FAIL; 42 auto, 7 PASS_NUMERIC, 1 PASS_PHRASE; 43 declared bindings, 7 fallbacks; 8 rows with spans, 42 without.

All four pins printed in the updated freeze receipt match the current bytes:

- `HARVEST_CMB_BOUNDS.md`: `beba95a7c8f5093e1a962ccffefa465038a58b6f3c83bfaff8ba6ddbe4662714`
- `HARVEST_H0_ANISOTROPY.md`: `6d97c67900348e5569dd802478b6bb8628640cd45e58b5b6e21c243286883f5a`
- `b_verify_quotes.py`: `f1664ce081392c21a2050249eeb16c6a813adcb0981f60a1518a19105732d81c`
- `b_verify_ledger.json`: `8155de4a143266abdc856bc796c7ace3efc86605e50e973b6c96dcb1a4844adb`

The receipt's aggregate counts, explicit fallback disclosure, rerun determinism, and pins are sound. They do not cure the acceptance predicate or missing binding/span evidence.

## Gate boundary

This regate addresses only whether the v4 repair discharges the prior numbers-first verification objection. It does not reopen the prior fidelity/balance/B1-scope findings that held, and it does not authorize Track C execution.
