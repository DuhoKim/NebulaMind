# V119 APPENDIX THIRD READ — GPT56

## Verdict

**DEFECTIVE.** I verified the required identities before reading: `gates/KNOWN_DEBT_APPENDIX.md` is `c2a5cacacac5f059964932b27c0f170db0677c9794320072e6200a5a22cc4bf7`, and `PREREG_SUCCESSOR_DRAFT_V119_20260831.md` is `b2cad7fa875b3e0e8388a8e409611c3c480d40363d9f112a4357d7c1b1b7256a`. The per-finding enumeration, U+2019 restoration, generation-time substring refusal, closing-total refusal, real word boundaries, four-form controls, and V119 §11 wording all hold. The package remains defective because its four “quoted in full” limitations are excerpts rather than the full limitation passages, and the changed form guard both admits a one-shared-field corrupt tuple shadowed by a clean decoy and disagrees with the appendix’s stronger stated contract.

## 1. The eight repairs

1. **Per-finding enumeration — REPAIRED.** Independent parsing found 63 pre-convention ledger rows summing to 334. All 63 named reports exist and have parseable final-block F-lines; their counts match the ledger. The appendix contains exactly 334 quoted F-lines, in report order, and that sequence is byte-for-byte equal to the independently extracted source sequence. The 330 unique strings are not a shortfall: four texts are genuine duplicates across source reports. No mismatch, pre-block, or absent-report note is needed for this corpus.

2. **GPT56-F3 U+2019 and generation-time verbatim verification — REPAIRED.** The quote contains source U+2019 in `form’s`; all six V116 eligibility quotes are whitespace-normalized substrings of the correct seat report. `verify_verbatim()` is called for all six during ordinary generation, and the planted false-verbatim control refuses. The live `--selftest` reports 6/6 and `--check` is byte-equal.

3. **Four acknowledged limitations as full passages — NOT REPAIRED.** All four snippets are genuine normalized substrings, so the new verifier proves fidelity of the selected bytes, not completeness. The numerical-route quote stops after “Both failed” and omits the same draft paragraph’s two failed premises as well as the following explicit `UNRESOLVED` limitation. The Stage-P quote consists only of the tail sentence at draft lines 283–284 and omits lines 276–282 that state the two operative definitions and why wording cannot close them. The authorization excerpt stops before “It is a file-integrity check, not a test of authority” and the remaining qualification at lines 565–570; the count excerpt stops before its same-shape/frozen-v9 qualification at lines 577–579. Calling these four selected substrings “quoted in full” repeats V118A F2’s substance.

4. **Form echo v4 — PARTIAL, DEFECTIVE.** Both-side boundaries are real: `(?<![\w-])…(?![\w-])` rejects word- or hyphen-prefixed/suffixed renames. First-field deletion now shares the remaining fields and is caught. Prefix rename, tuple deletion, first-field-corruption-plus-decoy, and cross-form substitution execute separately for all four forms, and all controls are green. But the changed production predicate only treats a tuple as a divergent candidate when it shares at least two non-`kind` fields with the current form. For each of the four forms, I placed a corrupt adjacent tuple of the shape ``(kind, <one real field>, alien_alpha, alien_beta)`` beside a clean exact tuple within 900 bytes. The exact tuple satisfies `_pair`; the corruption has `_shared == 1`, so it is ignored; shipped logic returns no problem. Thus “divergence = equals-no-mapped-form” is not implemented for all kind-adjacent tuple-shaped candidates—only for the undocumented/qualified ≥2-shared-field subset.

5. **Contradictory closing total — REPAIRED.** A synthetic row sum of 7 with a closing claim of 334 is refused by `parse_ledger()` with the contradictory-populations error; the missing-closing-line path also refuses. The planted control is live.

6. **V119 §11 claim sentence — REPAIRED AS A DESCRIPTION OF THE SHIPPED CODE.** It states the actual ≥2-shared-field candidate rule, some-mapped-form equality, real boundaries, 900-byte window, all-four per-form controls, and non-claims. This is materially narrower than the requested all-candidate divergence rule, but it accurately describes the bytes that shipped.

7. **Appendix form-contract repair — NOT REPAIRED.** Appendix §4 still says “every kind-adjacent tuple-shaped string byte-equal to the mapped form.” The changed generator/code and V119 §11 instead inspect only tuple strings sharing at least two current-form fields and permit exact tuples belonging to any mapped form. The appendix therefore overstates both candidate coverage and the equality target of the mechanism it is meant to disclose.

8. **Population and regeneration closure — REPAIRED on the claimed surface.** `gen_known_debt.py --selftest` is 6/6, `--check` is byte-equal, the parsed total is 334, the enumerated source sequence is 334, and the current string-field registry run reports 315 found / 315 classified / 0 forbidden / 0 stale.

## 2. New defects in changed regions only

The V118→V119 draft diff has three changed regions: the title, the newly legal V117→V118 trace row, and the §11 form-contract sentence. The title and trace row held. The §11 sentence accurately states the implementation, but the changed ≥2-shared-field candidate filter introduces the four-form clean-decoy bypass above relative to the claimed equals-no-mapped-form repair.

The appendix v2→v3/generator changes correctly add the 334 source F-lines, U+2019, source-substring checks, closing-total check, and limitation section. The changed limitation section’s “quoted in full” assertion is false because it emits selected substrings, and the appendix’s carried form-contract sentence remains inconsistent with the changed v4 implementation.

No further defect was found in the scoped changed regions.

## 3. Signature question

Yes—the appendix does not name that its four “full” limitation quotations omit material parts of those limitations or that the form echo ignores a corrupt kind-adjacent tuple sharing only one mapped field while a clean nearby decoy satisfies the pair check.

## Failed attacks and evidence

- Recounted all 63 pre-convention rows and all 334 source F-lines; no missing, extra, reordered, count-mismatched, absent-report, or pre-block case was found.
- Rechecked all six eligibility quotes and four limitation snippets as normalized source substrings; every selected byte sequence is faithful, including GPT56 F3’s U+2019.
- Exercised left/right word and hyphen boundaries, first-field deletion, tuple deletion, distant decoy, and cross-form substitution on every form; those named controls held.
- Re-ran the registry against V119: 315/315 classified, zero forbidden, zero stale.
- Re-ran the known-debt controls and byte check: 6/6 and byte-equal.
- Recomputed the two required hashes before reading and did not modify the pinned draft, appendix, ledger, source reports, or generators. The only write was this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V119-APPENDIX
VERDICT: DEFECTIVE
COUNT: 3
F1 | MEDIUM | KNOWN_DEBT_APPENDIX.md §3 / gen_known_debt.py LIMITATIONS / V119 draft §2.6 and §5 | All four selected strings are faithful substrings, but they omit material parts of the limitation passages while the appendix claims each is quoted in full; notably the numerical quote omits the failed premises and UNRESOLVED statement, and Stage-P omits the two-definition conflict.
F2 | HIGH | ref/gen_string_field_registry.py:847–862 / V119 §11 | The changed decoy guard examines only tuples sharing at least two current-form fields; for every form, a corrupt adjacent tuple sharing one real field plus a clean exact tuple within 900 bytes returns no problem, so equals-no-mapped-form divergence is not enforced over all adjacent tuple candidates.
F3 | MEDIUM | KNOWN_DEBT_APPENDIX.md §4 / gen_known_debt.py RESIDUES:74–83 / ref/gen_string_field_registry.py:847–862 | The appendix says every kind-adjacent tuple must equal the mapped form, while shipped v4 checks only ≥2-field-sharing candidates and accepts any mapped form’s exact tuple, overstating the contract frozen by the appendix.
<!-- END FINDINGS-BLOCK -->
