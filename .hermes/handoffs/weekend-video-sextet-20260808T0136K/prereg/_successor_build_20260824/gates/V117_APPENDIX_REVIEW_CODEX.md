# V117 APPENDIX MINI-ROUND — CODEX

## 1. The appendix

The required appendix digest was verified before reading: `3237631836e95b1b3d22f7c6b851f59db06efc297c55433cd61c0a81d4b20e63`. The six quoted passages are faithful verbatim excerpts of the two V116 reports, and the named V116 severities and debt-eligibility positions are faithful.

The ledger summary is not honest against the ledger it names. `gen_known_debt.py` reads only `gen_repair_ledger.py.DISPOSITIONS`, which starts at V100, then calls its 34 `(round, seat)` keys “rounds,” reports only their 177 findings, and concludes that every disposition is REPAIRED. The generated `REPAIR_LEDGER.md` has a materially larger population: 177 REPAIRED findings, 192 findings marked `MAPPED-BY-CITATION`, and 334 findings explicitly “enumerated as audit debt” across 63 PRE-CONVENTION report entries (703 findings represented in total). Section 3 omits that 334-finding audit debt entirely, despite the stopping ruling requiring every remaining finding or acknowledged limitation in the generated appendix; section 1 also hides the 192 non-REPAIRED-by-name mapped findings and mislabels 34 seat-round keys as 34 rounds rather than 17 rounds × two seats.

One listed residue also misstates its source: section 3 says every echo control, including the form echo, is “demoted in its own text,” but `ref/gen_string_field_registry.py` demotes the preimage echo at lines 533–537 while its FORM-SCHEMA ECHO at lines 783–807 is still asserted as a kind-qualified exact-tuple control, not demoted as a tripwire. The appendix's “within 900 bytes” description matches the shipped code, but `FINDINGS_MAP.md` V116→V117 says 400 bytes, so the cited source record is internally inconsistent.

## 2. The V117 fold

The required V117 digest was verified before reading: `67dd1d9070586a313d1b902f73df64765c59f6dbb5d3dc1fece58b9b47a51662`. The changed T1 region correctly implements CODEX F1: V117 §11 now says the interleaving is a chain-undetectable T1 violation, testimony-plus-fixture, with only the W0 consequence bounded.

The count-oracle changed regions implement release binding, exact-buffer receipt construction, non-null pre-dispatch refusal, receipt/plan substitution refusal, stale/foreign fixtures, and DESIGN-gating in §2.3 and the BS-2c row. They do not implement the claimed inventory repair: V117 §2.3 says `gates/count_oracle_harness.py` is “a class-P build item in §11's inventory,” but the path occurs only at lines 179, 915, and the retroactively edited V99→V100 history row 1131; it is absent from §11's actual build inventory. Thus GPT56 F1 / CODEX F2 remains incomplete on the exact omission the reports required, and editing an old transition row to say the harness “joined at V117” introduces a historical-source mutation rather than an inventory item.

The fold does not implement either seat's form-echo repair in the draft's changed bytes: the only §11 change is the T1 sentence, while the existing FORM-SCHEMA paragraph remains unchanged and still claims deletion, addition, and cross-form-substitution controls. The separately changed generator is also weaker than the V116 required repair and the map's description: lines 787–807 require only that the kind occur somewhere and that at least one matching tuple lie within 900 bytes, so they do not extract a unique authoritative `(kind, tuple)` declaration, reject duplicate kind declarations or duplicate tuples, or prevent a nearby decoy tuple from shadowing a corrupted declaration; the self-test exercises only the first schema's rename and one distant-shadow shape, not deletion/addition/cross-form swap through all four shipped mappings. The map's stated 400-byte window is 900 bytes in both live and self-test logic.

No other new defect was found in the changed regions: the version heading is correct, the BS-2c row is consistently DESIGN-gated, the T1 mirror is semantically aligned with the spec, and the inserted V115→V116 history row is correctly positioned as the predecessor transition.

## 3. The signature question

Yes: signing is unsafe for reasons not already honestly named in the appendix—the appendix suppresses 334 findings it calls audit debt (and 192 mapped-only findings), V117 falsely claims the required count-oracle harness is in §11's build inventory, and the form-echo repair remains neither uniquely kind-bound nor accurately described by the fold map.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V117-APPENDIX
VERDICT: DEFECTIVE
COUNT: 3
F1 | HIGH | KNOWN_DEBT_APPENDIX.md §§1,3; REPAIR_LEDGER.md | The appendix summarizes only V100+ DISPOSITIONS and hides 334 pre-convention audit-debt findings plus 192 MAPPED-BY-CITATION findings while claiming every disposition is REPAIRED.
F2 | HIGH | V117 §2.3 L179, §7 L915, §10 L1131; §11 inventory | V117 claims count_oracle_harness.py is a class-P §11 build item, but the path is absent from §11's actual inventory, leaving the named prerequisite unregistered there.
F3 | MEDIUM | V117 §11 L1565; gen_string_field_registry.py L555–592, L783–807; FINDINGS_MAP L325–327; appendix §3 | The form fold is absent from V117's changed prose and the 900-byte existence/proximity check still permits nearby decoy shadowing, lacks unique pair binding and advertised controls, and contradicts the map's stated 400-byte window.
<!-- END FINDINGS-BLOCK -->
