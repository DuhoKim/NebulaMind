# V121 APPENDIX FIFTH READ — GPT56

## Verdict

**DEFECTIVE.** I recomputed both required identities before inspection: `gates/KNOWN_DEBT_APPENDIX.md` is `c8fa3dfa99f3b7339fb6b1a08e9b84e17159dbc524c490221e2d860f2fc81af5`, and `PREREG_SUCCESSOR_DRAFT_V121_20260831.md` is `316f23dcaafeb16ec7fd4fa3bcbc56630d2fef4f3fcd0ecf163f59670594a941`. The authorization anchor repair is complete, and the short/tab/newline/450-character controls all bite per form through the shipped `form_check`; however, the new “ANY length” grammar is still not implemented for candidates longer than the fixed kind-adjacent window.

## 1. The two repairs

### Authorization passage

**REPAIRED.** `LIMIT_ANCHORS` now ends the caller-pair authorization passage at `a partial run is not a smaller run, it is a different experiment.` Independent extraction produced the 1,051-character source slice beginning at `**Recorded limit (CODEX-V34-2),` and ending at that exact sentence. It includes the complete tail: the file-integrity/not-authority qualification, the blocked-live-path qualification, the deliberately-unbuilt authorization record, frozen `successor_ref_v9.py`, `require_complete_sample()`'s every-parent receipt requirement, and the different-experiment sentence. The generated appendix contains that whole slice. `gen_known_debt.py --selftest` reports 8/8 and `--check` reports byte equality.

### Candidate grammar

**PARTIAL, DEFECTIVE.** V121 §11 and appendix §4 both state the same intended grammar: every backticked exact `(kind,`-opening candidate in a kind-adjacent window, any length and any internal whitespace, must normalize into the asserted-present whitelist, with one named exemption for the literal three-dot metavariable; they also state that controls use the one shipped function. The implementation removes the old literal-space and 10–400 bounds with ``r"`\(kind,[^)]*\)`"`` and checks the exact normalized `` `(kind, ...)` `` exemption.

Independent per-form calls to shipped `form_check` caught the short, tabbed, newline-after-comma, and 450-character attacks for all four forms, while the literal metavariable stayed exempt. But `_win` is still sliced to 900 bytes on either side of the kind match before the unbounded regex runs. A corrupt candidate whose opening follows the kind immediately but whose closing backtick is 1,200 characters later is truncated out of `_win`; with a clean exact tuple immediately before the kind to satisfy `_pair`, `form_check` returned `[]` for every form. Thus the regex is locally unbounded but the shipped predicate is not: a candidate can open inside the declared 900-byte adjacency and evade comparison solely because of its length. The shipped “overlength” control uses only 450 characters, so it crosses the retired 400 cap without testing the remaining window-imposed cap.

## 2. New defects in changed regions only

The V120→V121 draft changes otherwise hold: the title advances, the V119→V120 trace row is inserted, and §11 accurately names the intended candidate grammar and controls. Appendix v4→v5 otherwise adds the complete authorization tail and mirrors that intended grammar. `gen_known_debt.py` changes only the end anchor and generated FORM description in scope, both correctly. `ref/gen_string_field_registry.py` correctly removes the old explicit regex bounds, adds the exact exemption, and adds four per-form attacks, but its changed claim of “ANY length” overlooks the unchanged finite `_win` slice that bounds what the new regex can ever see. No other changed-region defect was found.

## Failed attacks and evidence

- Both required SHA-256 pins matched before reading.
- The extracted authorization block ends at the demanded sentence and includes every intervening Recorded-limit tail clause; generation self-test and byte check are green.
- The 15 normalized known tuples remain asserted-present; the ordinary registry run reports 315 found, 315 classified, zero forbidden-by-default, and zero stale.
- For each of the four forms, shipped `form_check` caught short, tabbed, newline-after-comma, 450-character, and one-shared-field corruptions, and accepted only the named literal three-dot metavariable exemption among those probes.
- The V120→V121, appendix v4→v5, and both generator diffs disclosed no further scoped defect.

## Signature question

No—the package is not safe to sign while a backticked `(kind,` candidate opening next to a form-kind mention can evade the advertised any-length whitelist rule merely by extending beyond the verifier's finite window slice.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V121-APPENDIX
VERDICT: DEFECTIVE
COUNT: 1
F1 | HIGH | ref/gen_string_field_registry.py:581–591, 663–670 / V121 §11:1569 / KNOWN_DEBT_APPENDIX.md §4:636 | The new regex has no explicit length bound, but it runs only after `_win` is truncated to ±900 bytes; per-form 1,200-character corrupt candidates opening immediately beside the kind are cut before their closing backtick and shipped `form_check` returns no problem, contradicting the stated ANY-length grammar while the 450-character “overlength” controls remain green.
<!-- END FINDINGS-BLOCK -->
