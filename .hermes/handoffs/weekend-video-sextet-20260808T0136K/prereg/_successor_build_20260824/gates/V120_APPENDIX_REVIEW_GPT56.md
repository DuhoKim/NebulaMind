# V120 APPENDIX FOURTH READ — GPT56

## Verdict

**DEFECTIVE.** I verified the required identities before reading: `gates/KNOWN_DEBT_APPENDIX.md` is `9fd78c205e3c769060431ac39646c0f453411b7fb70881b7bee6f0a4ea721cd2`, and `PREREG_SUCCESSOR_DRAFT_V120_20260831.md` is `f647cdb19c4ea43ee64774c4117aa9336009da7342154181af193b4aaaf4d2fa`. The Stage-P, numerical-route, and count-only passages now span the demanded blocks, the all-four seeded controls call the shipped `form_check`, and the V120/appendix FORM descriptions agree; however, one declared limitation extraction still ends in the middle of its source sentence, and the advertised all-candidate FORM rule still has an unadvertised short/whitespace candidate hole.

## 1. Full passages by anchored extraction

The generator has four unique ordered start/end pairs, `extract_limitations()` refuses missing/duplicate or reversed anchors, the live self-test reports 8/8, and `--check` reports byte equality. The numerical passage contains both failed premises and the explicit `UNRESOLVED` sentence; the 2,156-character Stage-P passage contains the shared-null/code-precedence definition, the exact-per-trial prose definition, the conflict, and the complete design-and-implementation tail; the count-only passage carries its full recorded-limit tail.

The authorization passage is still not whole. Its declared end anchor is `**deliberately not built here** (principal direction, 2026-08-29)`, but the source continues immediately, in the same sentence, `, and
\`successor_ref_v9.py\` remains frozen;`. The generated appendix stops before that comma and clause. Anchored extraction proves inclusion between chosen anchors; choosing an end anchor mid-sentence does not prove passage completeness and leaves one of the two Recorded-limit tails truncated.

## 2. FORM echo v5

The prior one-shared-field attack is repaired for all four forms, the whitelist's 15 concrete tuples are all present in the draft/spec corpus, `crosscheck_declared()` is green, `_domain_echo_selftest()` is green, and the controls reach the single shipped `form_check` through the thin `_form_probs` wrapper. V120 §11 and appendix §4 both state the same all-candidate whitelist contract.

The shipped candidate extractor is nevertheless narrower than that contract: `r"`\(kind, [^)]{10,400}\)`"` requires a literal space after the comma and at least ten interior characters. Through `form_check` itself, a corrupt kind-adjacent `` `(kind, x)` `` beside the clean exact tuple returns `[]`; so does `` `(kind,\talien_alpha)` ``. The longer zero-field and one-shared-field controls correctly refuse. Thus this is not a test-twin issue: production silently ignores genuine backticked `(kind, ...)` candidates solely because they are short or use non-space whitespace, despite promising EVERY candidate and whitespace normalization.

## 3. Changed-region review and failed attacks

The V119→V120 title change, inserted V118→V119 history row, and revised §11 FORM sentence introduced no further scoped defect. Appendix v3→v4 correctly expands three of four passages and accurately states the current intended FORM contract. The whitelist is neither missing nor carrying a stale concrete corpus tuple, and the one-shared-field corruption, first-field deletion with distant decoy, prefix rename, tuple deletion, and cross-form substitution controls all bite per form. No additional changed-region defect was found.

## 4. Signature question

Yes—the appendix fails to disclose that one supposedly whole Recorded-limit passage ends mid-sentence and that the shipped FORM predicate ignores short or non-space-whitespace kind-opening tuples while claiming all-candidate coverage.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V120-APPENDIX
VERDICT: DEFECTIVE
COUNT: 2
F1 | MEDIUM | gen_known_debt.py LIMIT_ANCHORS:189–192 / KNOWN_DEBT_APPENDIX.md §3:583–593 / V120 §5:561–570 | The authorization passage's end anchor stops before the same sentence's `successor_ref_v9.py remains frozen` clause, so anchored extraction still truncates one demanded Recorded-limit tail while calling the passage whole.
F2 | HIGH | ref/gen_string_field_registry.py:577–584 / V120 §11 / KNOWN_DEBT_APPENDIX.md §4 | The advertised EVERY-candidate whitelist rule only scans backticked tuples with a literal post-comma space and 10–400 interior characters; shipped `form_check` accepts kind-adjacent `(kind, x)` and `(kind,\talien_alpha)` corruptions beside a clean tuple, contradicting the all-candidate contract.
<!-- END FINDINGS-BLOCK -->