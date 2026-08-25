HOLD_TRACK_B_FREEZE

# Phase 4 Track B freeze — third regate

## Verdict

The v6 delta repairs both corruptions from `REGATE2_TRACKB_VERDICT.md`, reruns deterministically at 50/50 with zero fallbacks, corrects both identification occurrence counts, and binds the three scrambled-reading-order quotations to fetched arXiv LaTeX sources where their recorded matches replay. The freeze nevertheless remains on HOLD because the same numeric-relation surface still accepts operator deletion: an asserted `±` can be removed from the quote and the verifier silently accepts the now-relationless number pair against a source that explicitly contains `pm`.

## Blocking residue — operator deletion bypasses conflict detection

Against the normalized pinned Planck source text `3362.08 pm 0.99`:

- genuine `3362.08 ± 0.99` parses as `["3362.08", "pm", "0.99"]` and matches span `(19594, 19609)`;
- substituted `3362.08 × 0.99` parses as `["3362.08", "times", "0.99"]` and correctly fails;
- deleted-operator `3362.08 0.99` parses as `["3362.08", "0.99"]` and incorrectly matches the same `(19594, 19609)` span containing `3362.08 pm 0.99`.

The cause is in `find_ordered()` (`b_verify_quotes.py:79-85`): source-gap relations are compared only while iterating relations present in `want`. If the corrupted quote omits the operator, `want=[]`, `have=["pm"]` is never examined, and line 85 is an inert `if not want and False`. Thus the checker distinguishes one asserted operator from a different asserted operator, but does not distinguish an asserted source operator from operator deletion in the quote.

The receipt's rendering-loss allowance is directional: a silent SOURCE gap may be tolerated when the quote carries the relation because PDF rendering can lose the glyph. It does not justify a silent QUOTE gap when the bound source explicitly carries the operator. Required repair: when `want` is empty and `have` is nonempty between consecutive quote numbers, fail (or encode an explicit, narrowly receipted exception). Add operator deletion as a mandatory self-test alongside substitution.

## Five mandatory corruption retries — all attacks failed

I independently invoked the current parser and matcher for all five required classes:

1. absent fragments (`99–88`, `9.9–8.8`, `99`) — no match;
2. range order swaps (`5–10`→`10–5`, `2.5–3`→`3–2.5`) — no match;
3. exponent sign flip (`3.15 × 10^-5`→`3.15 × 10^+5`) — no match;
4. glued-unit value change (`3.7mK`→`99.9mK`) — no match;
5. operator substitution (`3362.08 ± 0.99`→`3362.08 × 0.99`) — no match.

The built-in mandatory self-test reports the same five failures. The two specific REGATE2 corruptions are repaired.

## Verifier rerun and ledger inspection

Running `python3 b_verify_quotes.py` from the lane root returned exit 0:

- `gpt2_trackb_cmb: 43 PASS / 0 FAIL`;
- `agy_trackb_h0: 7 PASS / 0 FAIL`;
- `TOTAL: 50 PASS / 0 FAIL; ledger rows=50; zero-fallback binding enforced`.

The ledger SHA-256 was byte-identical before and after the rerun: `0ca5467891bd6613988a1e828bf348a742cfae73a41929eb9efed304a89da643`.

Independent closure over all 50 rows found:

- 50 `PASS`: 45 `ordered-expressions+shingle`, 5 `exact-phrase-span`;
- 43 gpt2 rows and 7 agy rows;
- `declared_files` ranges from 1 to 3; zero rows have zero bound files;
- every quote SHA and source SHA recomputes;
- every stored expression sequence recomputes;
- every recorded span/excerpt is valid;
- every row replays under the verifier's actual single/composite-segment path.

## LaTeX-source bindings and corrected identification counts

The ledger chooses the fetched LaTeX source for exactly the three named quotations:

- Darling row: `radio_darling_2022_source.tex`, strict ordered match `(1920, 2203)`, source SHA valid;
- Efstathiou quote 1: `anomaly_efstathiou2003_source.tex`, strict ordered match `(11455, 11640)`, source SHA valid;
- Efstathiou quote 2: `anomaly_efstathiou2003_source.tex`, strict ordered match `(21515, 21957)`, source SHA valid.

The LaTeX candidates also have higher prose-shingle scores than their PDF-text counterparts for all three rows (Darling `0.250` vs `0.167`; Efstathiou `0.533` vs `0.400` and `0.652` vs `0.304`), so the recorded source selections are deterministic rather than manual substitutions.

The binding-map evidence now matches the pinned files: `paper.tex` contains 18 occurrences of `CatWISE`; `mnras_template.tex` contains 11 occurrences of `eigenvalues`.

## Receipt pins

All five v6 pins in `TRACK_B_FREEZE.md` match current bytes:

- `HARVEST_CMB_BOUNDS.md`: `beba95a7c8f5093e1a962ccffefa465038a58b6f3c83bfaff8ba6ddbe4662714`;
- `HARVEST_H0_ANISOTROPY.md`: `6d97c67900348e5569dd802478b6bb8628640cd45e58b5b6e21c243286883f5a`;
- `b_verify_quotes.py`: `1c9886ea208c383339f4a0274c3197f7558a9fb126a65d85f40ba147ce35fd44`;
- `b_verify_ledger.json`: `0ca5467891bd6613988a1e828bf348a742cfae73a41929eb9efed304a89da643`;
- `b_binding_map.json`: `37775c9ac4f7da98ae0c44238932495b0e8b28791033a487efef910c07da53f7`.

## Failed attacks and gate boundary

The v6 unit splitting, integer leading-zero handling, ordered matching, explicit five-class self-test, deterministic 50-row ledger, zero-fallback bindings, corrected occurrence evidence, and three LaTeX selections all held. This regate is confined to the current Track B v6 freeze and the REGATE2 numeric-relation residue; it does not reopen unrelated Track B findings and does not authorize Track C execution.
