# V122 APPENDIX SIXTH READ — GPT56

## Verdict

**DEFECTIVE.** I recomputed both required identities before inspection: `gates/KNOWN_DEBT_APPENDIX.md` is `b876a514c9a3c7dfb90edf3228ccb13f7ee2a334422f8edfceceeaf31aaa2f71`, and `PREREG_SUCCESSOR_DRAFT_V122_20260831.md` is `8be032bf358d0895caea42a4ef77ce001119a0e23fed105486c3b1c106193d8c`. The read-5 1,200-character truncation finding is repaired, but the changed whole-corpus candidate scanner still does not implement its stated all-candidate grammar for a candidate containing an interior right parenthesis before its actual closing `)`-backtick.

## 1. The one repair

**REPAIRED.** `form_check()` now enumerates candidate matches over the full corpus, records every form-kind match position, and tests adjacency at each candidate match's opening backtick. The fixed ±900 slice no longer truncates the candidate before matching. Independent calls through the shipped `form_check()` caught a 1,200-character corrupt candidate for each of the four forms with the clean exact tuple placed before the kind, so `_pair` was independently satisfied and the refusal came from the all-candidate comparison. `_domain_echo_selftest()` returned `[]`; its per-form attack list includes the 1,200-character case and calls the one `_form_probs()` alias whose body is the shipped `form_check()` call. Draft V122 §11 and appendix §4 both state opening-backtick adjacency and whole-corpus reading. `gen_known_debt.py --selftest` reported 8/8 and `--check` reported byte equality.

## 2. New defects in changed regions only

The candidate scanner still uses ``r"`\(kind,[^)]*\)`"``. Because `[^)]*` cannot cross any interior `)`, it does not enumerate a backticked candidate such as `` `(kind, sealed_enumeration_digest, alien(foo), alien_beta)` ``: that candidate has the required literal opening and a later closing `)`-backtick, but the interior `)` after `foo` prevents the regex from reaching it. With a clean exact tuple before the adjacent form-kind mention, the shipped `form_check()` returned `[]` for this attack for all four forms. This contradicts the changed scanner docstring, V122 §11, and appendix §4, each of which quantifies over **EVERY** backticked `(kind,`-opening candidate and names only the literal three-dot metavariable as exempt. The shipped controls do not include an interior-parenthesis attack, so they remain green.

The other scoped changes hold: V121→V122 advances the title, adds the V120→V121 trace row, and mirrors the opening-adjacency/whole-read repair in §11; appendix v5→v6 mirrors that rule; `gen_known_debt.py` emits the repaired FORM description; and the registry generator's full-corpus position check and 1,200-character per-form control repair the exact read-5 defect. No further changed-region defect was found.

## Failed attacks and evidence

- Both required SHA-256 pins matched before reading.
- The 1,200-character beyond-window corruption was refused with `NO known schema tuple` for each of the four forms through shipped `form_check()`.
- The registry's shipped FORM self-test returned no failures.
- The known-debt generator self-test was 8/8 and its non-writing regeneration check was byte-equal.
- The opening-adjacency/whole-read wording agrees across the registry generator, V122 §11, `gen_known_debt.py`, and appendix §4.

## Signature question

No—the package is not safe to sign while an adjacent backticked `(kind,` candidate with an interior right parenthesis can evade the purported all-candidate whitelist and its sole-exemption rule.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V122-APPENDIX
VERDICT: DEFECTIVE
COUNT: 1
F1 | HIGH | ref/gen_string_field_registry.py:583–599, 670–678 / PREREG_SUCCESSOR_DRAFT_V122_20260831.md §11 / gates/KNOWN_DEBT_APPENDIX.md §4 | The changed full-corpus scanner still matches candidates with `[^)]*`, so any backticked `(kind,`-opening candidate containing an interior `)` before its actual closing `)`-backtick is never enumerated; an adjacent nested-parenthesis corruption returned `[]` through shipped `form_check()` for all four forms, contradicting the EVERY-candidate contract while the controls remain green.
<!-- END FINDINGS-BLOCK -->
