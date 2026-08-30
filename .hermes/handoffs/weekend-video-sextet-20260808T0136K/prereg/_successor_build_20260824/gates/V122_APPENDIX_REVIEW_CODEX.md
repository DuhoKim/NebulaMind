# V122 APPENDIX SIXTH READ — CODEX

## Verdict

**DEFECTIVE.** I recomputed both required identities before inspection: `gates/KNOWN_DEBT_APPENDIX.md` is `b876a514c9a3c7dfb90edf3228ccb13f7ee2a334422f8edfceceeaf31aaa2f71`, and `PREREG_SUCCESSOR_DRAFT_V122_20260831.md` is `8be032bf358d0895caea42a4ef77ce001119a0e23fed105486c3b1c106193d8c`. The read-5 1,200-character truncation defect is repaired for all four forms: adjacency is evaluated before candidate filtering, the regex runs over the full corpus, and each long candidate is read through its closing backtick and refused by the shipped `form_check()`. One new defect remains in the changed opening-adjacency predicate: it measures candidate-opening to the **start** of the kind match in Python characters, not byte-distance to the kind mention span.

## 1. The one repair

`ref/gen_string_field_registry.py` lines 583–590 no longer slices a ±900 window before matching candidates. It first records kind-match positions, then scans the full corpus with ``r"`\(kind,[^)]*\)`"`` and filters by candidate-opening adjacency. The shipped per-form controls at lines 670–678 now include the 1,200-character attack and call the one shipped `form_check()` through the one-line `_form_probs()` alias. Independently, all four 1,200-character candidates opening immediately beside their respective form-kind mentions were read whole and returned `NO known schema tuple`; `_domain_echo_selftest()` returned `[]`, live `form_check(V122, LIFECYCLE_GUARANTEE_SPEC)` returned `[]`, and live `crosscheck_declared(V122)` returned zero problems.

V122 §11 and generated appendix §4 both explicitly say the candidate's opening lies in the 900-byte adjacency and the candidate is read whole from the full corpus wherever it closes. `gates/gen_known_debt.py --selftest` reported 8/8, and `--check` reported the appendix byte-equal.

## 2. New defect in changed regions

The new predicate is ``abs(_tm.start() - kp) <= 900``, where `kp` is only `m2.start()` for the kind. That is not distance from the candidate-opening point to the matched kind-mention span. For each of the four forms, I put the clean exact tuple before the kind to satisfy the independent pair requirement, then opened a corrupt candidate 896 ASCII bytes after the **end** of the kind mention. The opening is within the declared 900-byte adjacency to the mention, but 912–922 bytes after the mention's start; shipped `form_check()` returned `[]` in all four cases. This is a regression from the former post-kind window boundary and leaves an edge strip equal to the kind literal's length unexamined.

The same changed expression also counts Unicode code points while the contract says bytes. With 450 `é` characters plus one space between the kind's end and candidate opening, the gap is 901 UTF-8 bytes but only 451 Python characters; all four out-of-scope corrupt candidates were classified as adjacent and refused. Both counterexamples arise from the one changed distance predicate: it neither computes distance to the mention span nor computes bytes.

The V121→V122 draft diff otherwise holds: the title advances, the V120→V121 history row accurately records read 4, and the §11 replacement states the intended repair and fifth control. The appendix v6 FORM line matches the changed generator text. `gates/gen_known_debt.py`'s changed FORM prose accurately states the intended opening/whole-read contract. `ref/gen_string_field_registry.py`'s whole-corpus scan and long control repair the read-5 truncation, but its changed adjacency filter does not implement the stated boundary exactly. No other scoped defect was found.

## Failed attacks that held

- Both required SHA-256 pins matched before reading.
- The 1,200-character beyond-window corruption was caught for all four forms by the shipped `form_check()`.
- The short, tabbed, newline-after-comma, 450-character, one-shared-field, rename, deletion, distant-decoy, and cross-form controls remain routed through the shipped function; the seeded FORM suite is green.
- The named literal three-dot metavariable remains the sole explicit exemption in the changed function.
- Live V122/spec FORM and declared cross-checks are green.
- The known-debt generator reports 8/8 and regenerates the current appendix byte-for-byte.
- Draft §11, appendix §4, and the two generators agree on the intended opening-adjacency/whole-read rule; the defect is implementation of the adjacency distance, not textual drift.

## Signature question

No—the package is not safe to sign while a corrupt candidate opening within 900 bytes of a kind mention's end can evade the advertised all-candidate rule at the changed adjacency boundary.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V122-APPENDIX
VERDICT: DEFECTIVE
COUNT: 1
F1 | HIGH | ref/gen_string_field_registry.py:587–590 / V122 §11 / KNOWN_DEBT_APPENDIX.md §4 | The changed opening-adjacency predicate compares Python character offsets from the candidate opening to only the kind match's start, not byte-distance to the matched mention span: per-form corrupt candidates opening 896 ASCII bytes after the mention's end evade `form_check()` (while 901-byte UTF-8 gaps can be falsely included), contradicting the declared 900-byte all-candidate boundary.
<!-- END FINDINGS-BLOCK -->
