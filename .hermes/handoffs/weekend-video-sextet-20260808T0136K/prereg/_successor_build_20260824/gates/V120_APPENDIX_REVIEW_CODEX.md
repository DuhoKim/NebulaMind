# V120 APPENDIX FOURTH READ — CODEX

## Verdict

**DEFECTIVE.** Before reading, I recomputed the required SHA-256 identities: `gates/KNOWN_DEBT_APPENDIX.md` is `9fd78c205e3c769060431ac39646c0f453411b7fb70881b7bee6f0a4ea721cd2`, and `PREREG_SUCCESSOR_DRAFT_V120_20260831.md` is `f647cdb19c4ea43ee64774c4117aa9336009da7342154181af193b4aaaf4d2fa`. The anchored extractor refuses missing, duplicated, and out-of-order anchors; three passages are complete and the Stage-P passage now includes both operative definitions and the full conflict. Two changed-region defects remain: the authorization passage's declared end anchor cuts a continuing sentence before its final two lines, and FORM ECHO v5's advertised all-candidate rule is bypassed by kind-opening candidates whose whitespace or length falls outside its undisclosed regex grammar.

## 1. Read-3's repaired classes

### Full passages by anchored extraction

The construction is real: `extract_limitations()` requires exactly one start and one end anchor and checks ordering. Independent probes refused missing-start, missing-end, duplicate-start, duplicate-end, and end-before-start inputs; `gates/gen_known_debt.py --selftest` reported 8/8, and `--check` reported the appendix byte-equal.

Three requested blocks are complete on the current bytes:

- The numerical-route extraction is 1,538 characters and includes both failed premises, the general closed-enumeration point, the explicit **UNRESOLVED** sentence, and the ruling basis for the deletion.
- The count-only Recorded-limit extraction is 759 characters and includes its tail through ``successor_ref_v9.py` stays frozen at `6a9abbbd`.``
- The Stage-P extraction is 2,156 characters and includes both operative definitions: the code-precedence/shared-null route and the prose-preferred exact per-trial route, plus the precedence conflict, `No wording change closes this`, both BS-5p consequences, and the complete implementation tail.

The authorization extraction is not whole. Its end anchor is the parenthesized date at draft line 569, so the generated passage stops at `(principal direction, 2026-08-29)` even though the same source sentence continues `, and` through lines 570–571: ``successor_ref_v9.py` remains frozen; `require_complete_sample()` refuses unless every parent object has a measurement receipt — a partial run is not a smaller run, it is a different experiment.` The appendix therefore ends a sentence before its declared source block ends and omits the transition/tail immediately preceding the next Recorded-limit block.

### FORM ECHO v5

The structural repairs hold on their stated paths. `form_check()` is the sole implementation; `_form_probs()` is a one-line alias to it; `crosscheck_declared()` invokes that same function; the 15-entry normalized whitelist equals the 15 concrete kind-opening tuples found in the draft/spec corpus after excluding the prose metavariable ``(kind, ...)``; all whitelist entries are asserted present; and the seeded suite is green across all four forms, including the one-shared-field seed.

The all-candidate contract does not hold. The shipped candidate regex is ``r"`\(kind, [^)]{10,400}\)`"``: it requires one literal ASCII space after the comma and silently excludes interiors shorter than 10 or longer than 400 characters. For each of the four forms independently, I placed the exact mapped tuple beside (a) a one-shared-field divergent candidate with a newline after `kind,` and (b) a one-shared-field divergent candidate over 400 characters; `form_check()` returned no problems in all eight attacks. These are kind-adjacent `(kind, ...)` candidates and the prose promises ALL candidates with whitespace normalization and no shared-field threshold, but they never reach normalization or whitelist comparison.

Appendix §4 and V120 §11 are aligned with each other, but both overstate the implementation in the same way: neither discloses the literal-space nor 10–400-character restriction.

## 2. New defects in changed regions only

The V119→V120 draft diff otherwise holds: the title is V120, the V118→V119 history row is correctly inserted, and §11 states the intended whitelist/single-function/per-form control contract. The appendix v3→v4 diff otherwise carries the demanded numerical, count, and Stage-P material, and its FORM wording matches §11. No additional defect was found in the changed regions of `gates/gen_known_debt.py` or `ref/gen_string_field_registry.py` beyond the premature authorization end anchor and the narrower-than-declared candidate regex.

## Failed attacks that held

- Both required input hashes matched before inspection.
- Missing, duplicated, and out-of-order limitation anchors refused independently.
- The numerical, count-only, and Stage-P extractions match their source slices exactly; Stage-P contains both definitions and the full blocker.
- The normalized whitelist has exact 15/15 corpus coverage with no missing or stale concrete tuple.
- `form_check()` is the production function used by `crosscheck_declared()` and by the one-line self-test alias; no duplicated predicate remains.
- The seeded all-four-form controls, including the named one-shared-field shape, are green.
- The generator reports 8/8, the appendix check is byte-equal, and the registry generator's ordinary V120 run reports 315/315 classified, zero forbidden-by-default, zero stale.

## Signature question

Yes: signing remains unsafe because one purportedly whole Recorded-limit passage cuts a continuing source sentence and the purported all-candidate FORM rule accepts newline-separated and overlength one-shared-field divergences that the appendix does not disclose.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V120-APPENDIX
VERDICT: DEFECTIVE
COUNT: 2
F1 | HIGH | gates/gen_known_debt.py lines 189–191; KNOWN_DEBT_APPENDIX.md lines 583–593; V120 lines 559–572 | The authorization end anchor stops inside a continuing sentence at the date parenthesis, omitting draft lines 570–571, so the claimed whole passage does not include its complete Recorded-limit tail.
F2 | HIGH | ref/gen_string_field_registry.py lines 550–585; KNOWN_DEBT_APPENDIX.md line 634; V120 §11 line 1568 | FORM ECHO v5 promises every kind-adjacent candidate but its literal-space/10–400 regex excludes newline-separated and overlength one-shared-field candidates; all eight per-form attacks passed with a clean exact tuple nearby.
<!-- END FINDINGS-BLOCK -->
