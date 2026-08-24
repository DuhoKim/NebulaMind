HOLD_TRACK_B_FREEZE

# Phase 4 Track B freeze — second regate

## Verdict

The v5 repair discharges the order-swap and exponent-sign counterexamples, eliminates directory fallbacks, and supplies a complete reproducible 50-row ledger. It does not yet discharge R1 as stated in `REGATE_TRACKB_VERDICT.md`: `expr_seq()` is not a complete sequence of numeric expressions. It omits some numeric values and relation operators, allowing numeric-claim corruptions to pass. The Track B freeze therefore remains on HOLD.

## Blocking residue — incomplete numeric-expression parsing still accepts corrupted claims

`b_verify_quotes.py:28-35` keeps only standalone digit/decimal tokens and standalone `+`/`-` tokens. Consequently:

1. A number attached directly to its unit is omitted. In the Ferreira–Quartin quote, `3.7mK` is absent from `expr_seq`; the recorded sequence is only `["95"]`. I changed the claimed limit from `3.7mK` to `99.9mK`. Against the row's bound metadata source, v5 still found span `[1713,1715]`, shingle `0.909` against a `0.20` floor, and accepted the corrupted quote. The verifier therefore does not prove the quote's principal numerical bound.
2. The uncertainty operator is omitted. I changed the Planck table expression `3362.08 ± 0.99` to `3362.08 × 0.99`. The extracted expression sequence remained identical; v5 found an ordered span and accepted the corruption (`shingle=0.538`, floor `0.0`). Thus value order alone does not preserve the uncertainty/value relation required by the prior gate.

These are not broader semantic attacks; they are numeric-only corruptions in the exact R1 surface. Required repair: tokenize complete numeric expressions boundary-aware, including numbers adjacent to units and the operators/qualifiers that determine their relation (`±`, multiplication/exponent notation, comparators, and range signs), and require those expressions—not only selected standalone numbers—to match the bound source.

## Requested corruption retries — attacks failed

I independently retried both prior counterexamples with v5's functions against the currently bound source bytes:

- B3.1 order swap `5–10`→`10–5` and `2.5–3`→`3–2.5`: no ordered span; rejected.
- Cowell exponent sign `3.15 × 10^{-5}`→`3.15 × 10^{+5}`: no ordered span; rejected.

The mandatory self-test also ran and reported that the genuine quote passes while absent-fragment, order-swap, and exponent-sign corruptions all fail. Those repairs are credited.

## Verifier rerun and deterministic closure — attack failed

Running `python3 b_verify_quotes.py` from the lane root returned exit 0:

- `gpt2_trackb_cmb: 43 PASS / 0 FAIL`
- `agy_trackb_h0: 7 PASS / 0 FAIL`
- `TOTAL: 50 PASS / 0 FAIL; ledger rows=50; zero-fallback binding enforced`

The ledger hash was byte-identical before and after the rerun: `c049a98a69db800a583724778e59c40008eeb6e64f45a579fa3285931bcedb85`.

## R2 — explicit bindings delivered, but two recorded identification counts are stale

All five agy entry headers are explicitly mapped to one source file in `b_binding_map.json`; all seven agy quote rows have `declared_files: 1`, and no directory fallback path remains. The mapped title evidence for both Migkas files and Hu independently matches the file contents.

Two count-based evidence strings are inaccurate against the pinned current bytes: `paper.tex` contains 18, not 17, occurrences of `CatWISE`; `mnras_template.tex` contains 11, not 9, occurrences of `eigenvalues`. This does not recreate a directory fallback or overturn the obvious one-file mappings, but the identification-evidence receipt should be corrected rather than represented as exact evidence.

## R3 — ledger residue discharged

Independent inspection of all 50 rows found:

- 50 `PASS`; 45 `ordered-expressions+shingle`, 5 `exact-phrase-span`;
- every `quote_sha256` recomputes from `quote_full`;
- every bound source exists and every `source_sha256` recomputes;
- every stored `expr_seq` recomputes under v5;
- every row has `start`, `end`, and `excerpt`; all offsets are valid in the verifier-normalized source and every excerpt reproduces exactly;
- every recorded match replays.

The full-quote/source-hash/span custody requested by R3 is delivered.

## Receipt pins

All five v5 pins in `TRACK_B_FREEZE.md` match current bytes:

- `HARVEST_CMB_BOUNDS.md`: `beba95a7c8f5093e1a962ccffefa465038a58b6f3c83bfaff8ba6ddbe4662714`
- `HARVEST_H0_ANISOTROPY.md`: `6d97c67900348e5569dd802478b6bb8628640cd45e58b5b6e21c243286883f5a`
- `b_verify_quotes.py`: `2d8b1eca007d69b4724614fdecdd6b77a167151f5c6e8b30f12dad9babfb68cc`
- `b_verify_ledger.json`: `c049a98a69db800a583724778e59c40008eeb6e64f45a579fa3285931bcedb85`
- `b_binding_map.json`: `74e53f0c706ddf2c23856d17ffc090ea67d57ed7127cd0174374ef01550687ae`

## Gate boundary

This second regate addresses only whether the v5 repairs discharge the three residues in `REGATE_TRACKB_VERDICT.md`. It does not reopen unrelated Track B findings and does not authorize Track C execution.
