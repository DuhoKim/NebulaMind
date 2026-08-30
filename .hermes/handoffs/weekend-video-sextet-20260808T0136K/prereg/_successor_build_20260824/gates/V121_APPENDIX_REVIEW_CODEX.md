# V121 APPENDIX FIFTH READ — CODEX

## Verdict

**SOUND.** I recomputed both required identities before inspection: `gates/KNOWN_DEBT_APPENDIX.md` is `c8fa3dfa99f3b7339fb6b1a08e9b84e17159dbc524c490221e2d860f2fc81af5`, and `PREREG_SUCCESSOR_DRAFT_V121_20260831.md` is `316f23dcaafeb16ec7fd4fa3bcbc56630d2fef4f3fcd0ecf163f59670594a941`. Both read-4 defects are repaired, and I found no new defect in the scoped V120→V121, appendix v4→v5, or two generator changed regions.

## 1. The two repairs

### Authorization Recorded-limit block

`gates/gen_known_debt.py` now anchors the authorization passage through `a partial run is not a smaller run, it is a different experiment.` (line 193), rather than stopping at the parenthesized date. The generated appendix reproduces the entire source slice through that tail (appendix lines 585–595; draft lines 561–571), including the frozen-v9 clause and `require_complete_sample()` clause. The next Recorded-limit block begins only after the completed sentence. `gates/gen_known_debt.py --selftest` reported 8/8 and `--check` reported byte-equal.

### Candidate grammar and controls

The shipped `form_check()` candidate extractor is now ``r"`\(kind,[^)]*\)`"`` (registry generator line 583): literal backticked `(kind,` opening, zero-or-more interior characters, including tabs/newlines and without an upper bound. Whitespace normalization precedes whitelist comparison. The sole exemption is the whitespace-normalized literal three-dot metavariable `` `(kind, ...)` ``, documented in the function contract and implemented by its named equality check; no second exemption appears.

I exercised short, tab-after-comma, newline-after-comma, and 450-character overlength corruptions independently for each of the four forms through the shipped `form_check()`—16/16 were refused as matching no known schema tuple while a clean exact tuple remained adjacent. The literal three-dot metavariable stayed green for all four forms. `_domain_echo_selftest()` returned `[]`, live `form_check(draft, spec)` returned `[]`, and live `crosscheck_declared(draft)` returned zero problems. The built-in per-form controls at lines 663–670 call `_form_probs()`, whose only operation is the shipped `form_check()` call.

V121 §11 line 1569 and appendix §4 line 636 state the same grammar: every backticked `(kind,`-opening candidate, any length and any internal whitespace, with the one named three-dot metavariable exemption. Both also preserve the same 900-byte kind-adjacency boundary and stated non-claims.

## 2. Changed-region review

The V120→V121 draft changes are confined to the V121 title, the V119→V120 history row, and the repaired §11 FORM sentence; those changes agree with the generators and appendix. The appendix v4→v5 changes contain the complete authorization tail and the exact repaired FORM contract. In `gates/gen_known_debt.py`, the end-anchor extension and matching residue prose introduce no new inconsistency. In `ref/gen_string_field_registry.py`, the generalized candidate regex, documented exemption, and four added per-form attack controls agree and run through the production predicate. No additional scoped defect was found.

## Failed attacks that held

- Required SHA-256 pins matched before reading.
- The authorization extraction reaches the final period and remains byte-identical to the corresponding draft slice.
- Missing/duplicated/out-of-order limitation-anchor behavior remains covered by the 8/8 generator self-test; appendix regeneration check is byte-equal.
- All 16 per-form short/tab/newline/overlength attacks were caught by the one shipped `form_check()`.
- The named three-dot metavariable exemption stayed green for all four forms, while no other divergent candidate tested escaped.
- Production corpus checks are green: FORM self-test `[]`, live form check `[]`, full declared cross-check count 0.
- Draft §11 and appendix §4 match the shipped candidate grammar and its sole exemption.

## Signature question

No—this fifth read finds no scoped appendix-package defect that makes the already approved run-end terminal-signature ceremony unsafe.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V121-APPENDIX
VERDICT: SOUND
COUNT: 0
<!-- END FINDINGS-BLOCK -->
