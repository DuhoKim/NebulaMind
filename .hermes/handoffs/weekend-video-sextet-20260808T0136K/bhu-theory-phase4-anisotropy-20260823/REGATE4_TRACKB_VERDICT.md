HOLD_TRACK_B_FREEZE

# Phase 4 Track B freeze — fourth regate

## Verdict

v7 repairs the exact REGATE3 operator-deletion counterexample and preserves the intended asymmetry: a bare quote pair fails against a source that tightly joins the pair through `pm`, while a loose source gap containing column-interleave noise is not treated as an asserted relation. The six embedded corruption examples all fail, the verifier reruns at 50/50 with zero fallbacks, every ledger row closes, and all v7 pins match. The freeze nevertheless remains on HOLD because numeric tokens immediately followed by sentence-final `.` are silently omitted from `expr_seq`. Two corruptions of actual frozen quotations therefore pass the full row checker unchanged: `ℓ > 1.` → `ℓ < 1.` and `1 in 20.` → `1 in 99.`. Thus operator substitution and absent/value corruption are not dead across the frozen 50-row corpus, and relations are not universally enforced within each sentence as the v7 receipt asserts.

## Blocking residue — sentence-final numeric token loss

`norm()` preserves a period when it is preceded by a digit (`b_verify_quotes.py:29-31`), so a sentence-final token such as `1.` or `20.` survives normalization with its trailing period. `parse_items()` accepts only `\d+(?:\.\d+)?` (`b_verify_quotes.py:38-47`), which rejects `1.` and `20.`. The final value, and any relation whose adjacency depends on it, disappear before matching.

This is not only a synthetic parser edge. It permits two independent corruptions of current frozen rows:

1. **Actual operator substitution passes** — ledger row 17, Abghari et al.
   - Genuine clause: `the power estimate at ℓ = 1 contains significant contributions from ℓ > 1.`
   - Corruption: `ℓ > 1.` → `ℓ < 1.`
   - Genuine and corrupted quotes both parse to the same row sequence `['50', '1']`; the terminal `1.` and its `>`/`<` relation are absent.
   - Re-executing `check()` on the corrupted quote against its normal bound source returns `1 PASS / 0 FAIL`, source `radio_abghari_et_al_2024_v2.txt`, span `(1140, 1266)`, shingle `0.769`.

2. **Actual absent/value corruption passes** — ledger row 30, Efstathiou 2003.
   - Genuine clause: `the odds is more like 1 in 10 or 1 in 20.`
   - Corruption: `1 in 20.` → `1 in 99.`
   - Genuine and corrupted quotes both parse to `['3', '1', '700', '4', '1', '10', '1']`; the sentence-final value is absent from both sequences.
   - Re-executing `check()` on the corrupted quote returns `1 PASS / 0 FAIL`, source `anomaly_efstathiou2003_source.tex`, span `(21515, 21957)`, shingle `0.652`.

The shingle gate does not save either row: numeric tokens are excluded from shingles, and the operator mutation leaves the score unchanged in the Abghari row.

Required repair: strip a period unless it is internal to a decimal (or equivalently strip terminal punctuation before numeric classification), regenerate the ledger and v8 pins, and add both actual-row corruptions above as mandatory self-tests. The repair must demonstrate that every numeric token in the two genuine clauses is retained and that both mutated rows fail through the same `check()` path, not only through a synthetic `find_ordered()` assertion.

## REGATE3 deletion retry and all six mandatory corruptions

I independently invoked the current parser/matcher rather than relying on the built-in self-test. Results:

1. genuine B3.1 quote — PASS;
2. absent-fragment corruption (`99–88`, `9.9–8.8`, `99`) — FAIL;
3. range order swaps (`5–10`→`10–5`, `2.5–3`→`3–2.5`) — FAIL;
4. exponent sign flip (`3.15 × 10^-5`→`3.15 × 10^+5`) — FAIL;
5. glued-unit value change (`3.7mK`→`99.9mK`) — FAIL;
6. operator substitution (`3362.08 ± 0.99`→`3362.08 × 0.99`) — FAIL;
7. REGATE3 operator deletion (`3362.08 ± 0.99`→`3362.08 0.99`) — FAIL.

The built-in mandatory self-test independently prints that all six corruption classes fail. The specific deletion repair is therefore credited; the HOLD is for the untested sentence-final realization of already-governed corruption classes.

## Tight/loose deletion asymmetry

Synthetic boundary checks confirm the v7 rule behaves as stated:

- bare quote `12 3` against tight source `12 pm 3` — FAIL;
- bare quote `12 3` against a loose source gap containing prose/column noise and `pm` — PASS;
- quote `12 pm 3` against a source whose operator is silent — PASS.

The repair is directional and narrow: a digital quote cannot delete an operator from a tightly operator-joined source pair, while source-side rendering loss remains tolerated and loose interleave noise does not fire.

## Sentence-level interleave checks

No current ledger row required the sentence-level fallback on this rerun: 42 numeric rows replayed by the direct path, 3 by the composite-segment path, and 5 nonnumeric rows by exact phrase. I therefore exercised the fallback synthetically with more than 400 characters of source interleave between two sentences.

When the numeric expressions were followed by units (`10 ± 2 units.` and `30 < 40 units.`), direct whole-quote matching failed as intended, per-sentence matching succeeded, and within-sentence order and operator corruptions failed. But the same test with sentence-final bare numerics (`10 ± 2.` and `30 < 40.`) exposed the blocker: each terminal value was omitted, so order and relation corruptions within those sentences still matched. The receipt's unqualified statement that order and relations are enforced within each sentence is therefore false for a normal punctuation form already present in the frozen corpus.

## Verifier rerun and ledger closure

`python3 b_verify_quotes.py` returned exit 0:

- `gpt2_trackb_cmb: 43 PASS / 0 FAIL`;
- `agy_trackb_h0: 7 PASS / 0 FAIL`;
- `TOTAL: 50 PASS / 0 FAIL; ledger rows=50; zero-fallback binding enforced`.

The ledger was byte-identical before and after rerun at SHA-256 `1a4a397838789e55c991156f93be782aa0a4d54626e8b418e9b3e4bfc5f4cafa`.

Independent closure over all 50 rows found:

- 50 `PASS`: 45 `ordered-expressions+shingle`, 5 `exact-phrase-span`;
- 43 gpt2 rows and 7 agy rows;
- `declared_files` range 1–3; zero rows have zero bound files;
- every quote SHA and source SHA recomputes;
- every stored expression sequence recomputes under the current parser;
- every stored span/excerpt is valid;
- all 45 numeric rows replay under the verifier's actual direct/composite path;
- the selected special sources are exactly Darling LaTeX once and Efstathiou LaTeX twice.

The binding-map occurrence evidence also rechecks: `paper.tex` contains 18 occurrences of `CatWISE`; `mnras_template.tex` contains 11 occurrences of `eigenvalues`.

## v7 receipt pins

All five pins in `TRACK_B_FREEZE.md` match current bytes:

- `HARVEST_CMB_BOUNDS.md`: `beba95a7c8f5093e1a962ccffefa465038a58b6f3c83bfaff8ba6ddbe4662714`;
- `HARVEST_H0_ANISOTROPY.md`: `6d97c67900348e5569dd802478b6bb8628640cd45e58b5b6e21c243286883f5a`;
- `b_verify_quotes.py`: `148d55464b1e63818a48f29feb8cdd8796d6e0b68ab9d297c0a91645cf10f3b3`;
- `b_verify_ledger.json`: `1a4a397838789e55c991156f93be782aa0a4d54626e8b418e9b3e4bfc5f4cafa`;
- `b_binding_map.json`: `37775c9ac4f7da98ae0c44238932495b0e8b28791033a487efef910c07da53f7`.

## Failed attacks and gate boundary

The v7 tight-pair deletion guard, loose-gap non-firing behavior, source-silent tolerance, all six embedded examples, deterministic 50-row ledger, zero-fallback bindings, source hashes, special LaTeX selections, and corrected identification counts held. The only content-changing write by this regate is this verdict file; the verifier rewrote the ledger byte-identically. This HOLD is confined to the current Track B v7 quote-verifier contract and does not authorize Track C execution.
