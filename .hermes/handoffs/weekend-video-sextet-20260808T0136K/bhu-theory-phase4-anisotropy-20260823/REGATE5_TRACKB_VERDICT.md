PASS_TRACK_B_FREEZE

# Phase 4 Track B freeze — fifth regate

## Verdict

The v8 repair discharges the sole REGATE4 residue. Sentence-final numeric punctuation is removed without damaging internal decimal points, both previously passing actual-row corruptions now alter the parsed expression sequence and fail through `verify_quote_row()`, all eight corruption cases fail, the genuine versions pass, the verifier reruns at 50/50 with zero fallbacks, the regenerated ledger is deterministic and closes independently, and all five v8 receipt pins match recomputed `shasum` values. No blocking residue remains within this fifth-regate brief.

## Sentence-final numeric repair

`norm()` now applies `re.sub(r"(?<=\d)\.(?!\d)", " ", s)`. An independent probe normalizes `1. 20. 3.14.` to `1 20 3.14`: terminal punctuation is stripped while the internal decimal point remains.

The two repaired frozen rows now retain the formerly lost values and relations:

- Abghari's ledger expression sequence ends `['50', '1', 'gt', '1']`; the terminal `1` and preceding `gt` are present.
- Efstathiou's ledger expression sequence ends `['700', '4', '1', '10', '1', '20']`; the terminal `20` is present.

## Eight independent row-path corruption retries

I independently selected each genuine corpus row, reconstructed its normal bound-file set, verified the genuine quote through `verify_quote_row()`, mutated it, and sent the mutation through that same function. All eight genuine rows passed; all eight corruptions failed; every mutation changed `expr_seq`:

1. absent fragments (`5–10`, `2.5–3`, `40` to absent values) — FAIL;
2. range order swap (`5–10`→`10–5`, `2.5–3`→`3–2.5`) — FAIL;
3. exponent sign flip (`3.15 × 10^-5`→`3.15 × 10^+5`) — FAIL;
4. glued-unit value change (`3.7mK`→`99.9mK`) — FAIL;
5. operator substitution (`3362.08 ± 0.99`→`3362.08 × 0.99`) — FAIL;
6. operator deletion (`3362.08 ± 0.99`→`3362.08 0.99`) — FAIL;
7. Abghari actual-row sentence-end operator flip (`ℓ > 1.`→`ℓ < 1.`) — FAIL;
8. Efstathiou actual-row sentence-final value change (`1 in 20.`→`1 in 99.`) — FAIL.

The mandatory built-in self-test also executes successfully and explicitly includes the two REGATE4 actual frozen rows through `verify_quote_row()`.

## Verifier rerun and deterministic ledger

Running `python3 b_verify_quotes.py` returned exit 0:

- `gpt2_trackb_cmb: 43 PASS / 0 FAIL`;
- `agy_trackb_h0: 7 PASS / 0 FAIL`;
- `TOTAL: 50 PASS / 0 FAIL; ledger rows=50; zero-fallback binding enforced`.

The ledger SHA-256 was `6106ab889df4a61c7484543b8c8f9c1fc1ea0bcaa3ecb71805c935f2cdf5b061` before the rerun and remained identical afterward.

Independent closure over all 50 rows found:

- 50 `PASS`: 46 `ordered-expressions+shingle`, 4 `exact-phrase-span`;
- 43 gpt2 rows and 7 agy rows;
- `declared_files` range 1–3; zero rows have zero bound files;
- every quote SHA and selected-source SHA recomputes;
- every stored expression sequence recomputes under v8;
- every row has valid span bounds and an exact normalized-source excerpt;
- every row replays successfully through `verify_quote_row()` against its selected source;
- the special selected sources remain Darling LaTeX once and Efstathiou LaTeX twice.

The binding-map identification evidence also rechecks at 18 occurrences of `CatWISE` in `paper.tex` and 11 occurrences of `eigenvalues` in `mnras_template.tex`.

## v8 receipt pins

All five pins in `TRACK_B_FREEZE.md` match independently recomputed SHA-256 values:

- `HARVEST_CMB_BOUNDS.md`: `beba95a7c8f5093e1a962ccffefa465038a58b6f3c83bfaff8ba6ddbe4662714`;
- `HARVEST_H0_ANISOTROPY.md`: `6d97c67900348e5569dd802478b6bb8628640cd45e58b5b6e21c243286883f5a`;
- `b_verify_quotes.py`: `ecadfb540edd84104f6c2a93ce47086dfede92912e781f2f4a9f4a4d00ae13ec`;
- `b_verify_ledger.json`: `6106ab889df4a61c7484543b8c8f9c1fc1ea0bcaa3ecb71805c935f2cdf5b061`;
- `b_binding_map.json`: `37775c9ac4f7da98ae0c44238932495b0e8b28791033a487efef910c07da53f7`.

## Failed attacks and gate boundary

The terminal-period parser attack, both REGATE4 actual-row corruptions, all six prior corruption classes, deterministic regeneration, complete ledger replay, zero-fallback binding, special LaTeX selections, identification counts, and receipt pins all held. This verdict addresses only the current fifth-regate order and does not authorize Track C execution or reopen unrelated sibling findings.
