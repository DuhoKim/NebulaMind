HOLD_UNSOUND_NUMBERS_FIRST_VERIFICATION

# Phase 4 Track B adversarial gate (codex)

## Verdict

The sampled frozen values are faithful, the two disputed literatures are represented on both sides, and the B1 demotion matches the amended Track A gate. The freeze nevertheless does not pass: its universal verification receipt rests on a numeric checker that demonstrably accepts numerically corrupted quotations. Because the Track B brief requires every frozen directional/numeric claim to be source-verified, the current `38/50 by machine` claim cannot support the freeze.

## Blocking objection — the advertised numbers-first verifier is not numbers-first for many load-bearing values

Fact: `b_verify_quotes.py:17-19` retains only decimals with at least three digits after removing the point, or integers with at least three digits. It therefore ignores common frozen quantities such as `5`, `10`, `40`, `95`, `2.5`, `3`, `4.9`, and `8`, as well as the small pieces of scientific notation. At `b_verify_quotes.py:61`, a quote with no retained numeric tokens passes solely on a 70% prose-shingle match. At `b_verify_quotes.py:56`, retained tokens are checked as unbounded substrings rather than numeric tokens (`3.6` matches inside `13.6`).

Independent counterexample: I took the exact Planck-2013 B3.1 harvest quote and changed only its values from `5–10% at ℓ ≲ 40; 2.5–3σ` to `99–88% at ℓ ≲ 99; 9.9–8.8σ`. Under the verifier's own normalization/token/shingle rules, both the original and corrupted quote produced `numtokens=[]`, a 0.75 shingle score, and `accepted=True`. Thus the acceptance criterion does not establish numeric fidelity.

Re-execution from the lane root produced the receipt's aggregate split but exposed the issue directly:

- gpt2 harvest: 32/43 machine-verified;
- agy harvest: 6/7 machine-verified;
- total: 38/50 machine-verified, 12 misses.

The freeze then labels six misses accepted by an all-distinctive-numbers criterion and six hand-verified, but no machine-checkable residue ledger is included in the frozen artifact. The six numeric-only misses visible in the run do have all of the checker's retained tokens in a source; that does not cure the token-coverage defect above.

Required repair: replace the numeric extractor with boundary-aware parsing that preserves signed integers, decimals of every length, percentages, uncertainties, ranges, scientific notation, multipoles, units, and confidence levels; bind each harvest entry to its declared source rather than searching the whole source directory; emit a per-quote ledger of extracted tokens and source spans; rerun all 50 quotes; then update and re-pin the freeze receipt. Any manual acceptance must identify the quote, source file, source span, and exact reason.

## Fidelity spot checks — attacks failed

I independently checked eight frozen rows, spanning both B2 and B3, against both the harvest quotation and the named local primary-source text. No sampled number differed.

| Row | Frozen value checked | Local-source result |
|---|---|---|
| B2.1 | 3362.08 ± 0.99 µK; 369.82 ± 0.11 km/s | Exact values present in the Planck 2018 layout text. |
| B2.2 | 3.6/3.7 mK at 95% CI | Exact SMICA and NILC table limits present. |
| B2.5 | over twice expected; 4.9σ | Exact abstract framing and significance present in Secrest et al. 2021. |
| B2.9 | 331 and 399 km/s, reported consistent with the CMB velocity | Exact central values and consistency statement present in Darling 2022. |
| B3.1 | 5–10% at ℓ ≲ 40; 2.5–3σ | Exact Planck 2013 abstract values present. |
| B3.3 | ≤0.33% PR3; ≤1.76% PR4; no T+P simulation as low | Exact values and finite-ensemble framing present in Billi et al. 2024. |
| B3.5 | cumulative 0.824; full-sky C(θ) within 95% | Exact WMAP-team statements present. |
| B3.7 | 8% full-sky; 0.065% masked; “unconvincing evidence” | Exact estimator-dependent values and conclusion present in Efstathiou, Ma & Hanson 2010. |

I also recomputed the eight corresponding PDF SHA-256 values. The Planck, Ferreira–Quartin, and all five anomaly hashes matched the hashes stated in their harvest receipts/index; the radio hashes were independently recomputed against the held files. The three freeze-level artifact pins for both harvests and `b_verify_quotes.py` also match the current bytes.

The 12 verifier misses are not evidence that those quotations are false. Direct inspection confirmed the hand-residue examples across PDF line breaks (Planck's Solar-dipole definition, Ferreira–Quartin's SMICA/NILC and null/directness passages, Planck's approximately 1% summary, and Bennett et al.'s 95% full-sky statements). The blocker is that the frozen universal verification claim is not reproducibly established by the stated method and residue record.

## Balance — attack failed, with one custody advisory

B2 preserves pro-excess results and multiple counter/reassessment results, explicitly says the dispute remains unresolved, and forbids Track C from resolving it. B3 likewise carries high-significance and low-significance/estimator-dependent positions, calls the significance contested, and forbids adjudication. I found no sentence that converts either dispute into the coordinator's conclusion.

Advisory: the compact B2.9 row drops Darling's asymmetric uncertainties while the harvest retains them. That does not reverse the paper's stated consistency result, but a repaired freeze should retain those uncertainties in the table so counter-evidence has the same numerical custody as excess claims.

## B1 scope — attack failed

`TRACK_A_VERDICT.md` Amendment 1 limits the exact H0 null to sources whose complete light paths remain interior and leaves boundary-crossing or boundary-influenced probes uncalibrated. `REGATE3_TRACKA_VERDICT.md` passes that amended scope. The Track B freeze uses the same boundary: B1 is reference-only for the wholly-interior model, cannot be used as a discriminant, and may reopen for a future boundary-influenced calculation. It is neither wider nor narrower than the binding Track A result.

## Omissions — no Track C-biasing class omission found

B2 contains the direct intrinsic-CMB-dipole limit required for a photon-channel statement. B3 contains direct low-ℓ power/variance/correlation measurements and the contested-significance counterrecord needed for the cap-morphology comparison. B1 is not enumerated as a full table in the freeze—it names four entries and delegates the remainder to the pinned H0 harvest—but Track C is expressly barred from using B1 as a discriminant, so this presentation defect does not currently bias Track C. A repaired freeze should still enumerate all B1 entries instead of saying “remaining harvest entries” to make the frozen set closed and auditable.

## Gate boundary

This HOLD concerns the Track B freeze and its verification custody. It does not overturn the amended Track A gate, does not adjudicate either literature dispute, and does not authorize Track C execution.
