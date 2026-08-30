# V118 APPENDIX RE-READ — CODEX

## Verdict

**DEFECTIVE.** Before reading, I recomputed the two required SHA-256 identities: `gates/KNOWN_DEBT_APPENDIX.md` is `0727c126d40f3b89835bf616fe419bc7f7e78a9997d8f9ffd2078e6e4eff491a`, and `PREREG_SUCCESSOR_DRAFT_V118_20260831.md` is `fb07f3f975ec0bccbddb345455e39b59015c265aa009f42923faa099c99ce5d0`. The V118 history and inventory repairs hold, the four omitted limitations are now present, and the appendix's per-echo description is honest about the intended contracts; however, the full-ledger repair still substitutes 63 aggregate count lines for the 334 findings the ruling requires to be enumerated and quoted in full, one claimed-verbatim V116 paragraph still changes a source byte, and the hardened form echo remains bypassable.

## 1. The nine mini-round repairs

1. **GPT56 F1 — not repaired; CODEX F1 — not repaired.** The parser/live appendix correctly count 177 `REPAIRED`, 192 `MAPPED-BY-CITATION`, 63 pre-convention ledger rows summing to 334, 703 total, and 84 two-seat rounds; all 63 pre-convention ledger rows are copied exactly. But those rows contain only `(version, seat, count)` — for example, `V77/GPT56: ... 11 finding(s)` — not eleven finding identifiers, texts, or dispositions. Thus the appendix does not surface 334 findings verbatim or quote them in full as `STOPPING_RULE_RULING_20260830.md` lines 16–19 requires; it exposes that a hidden population exists while leaving the population's actual findings hidden. The new generator also does not enforce its advertised population reconciliation: a synthetic ledger whose parsed pre-convention rows sum to 7 but whose closing line says 334 is accepted and emitted with both contradictory totals while `selftest()` remains green.

2. **GPT56 F2 — not fully repaired.** Five eligibility paragraphs match their V116 sources after whitespace normalization. GPT56 F3 does not: the V116 source says `current form’s fields` with U+2019, while `gen_known_debt.py` and the appendix say `current form's fields` with ASCII U+0027. The paragraph is complete, but the claimed byte-faithful/verbatim repair is false by one source byte.

3. **GPT56 F3 — repaired.** Appendix §3 now names all four draft-acknowledged limitations: the unresolved pre-unblinding numerical route, caller-pair-only authorization, count-only/non-partition-complete sample guard, and dual-valued Stage-P contract, with the corresponding draft sections.

4. **GPT56 F4 — repaired on the stated surface.** Appendix §3 no longer blanket-demotes every echo; it separately describes PREIMAGE, CLOSE-CLASS, FORM, R02, and retired-token contracts. The FORM source now expressly disclaims a unique authoritative site and semantic coverage outside kind-adjacent windows.

5. **GPT56 F5 — not fully repaired; CODEX F3 — not fully repaired.** `FINDINGS_MAP.md` now records the 400→900 correction, and the live form check uses 900 bytes. But the claimed boundary-aware/decoy/all-four hardening is incomplete. `_kpat = re.escape(kind) + r"(?!-)"` has no left boundary: changing the only exact `successor-export` kind to `xsuccessor-export` leaves one regex match and produces zero form-schema findings; the same prefix attack passes for `successor-export-prelock`. The decoy guard checks a divergent candidate only if it retains `_fields[1]`; replacing that first non-kind field with `alien_field` while planting an exact nearby tuple makes the corrupt declaration plus decoy pass with zero form-schema findings. Finally, the self-test runs rename over all four forms, but adjacent-corruption and cross-form substitution only on `FORM_SCHEMAS[0]`, and it has no separate form-deletion loop, despite V118 claiming all four controls run for all four forms.

6. **GPT56 F6 — repaired.** The V118 `V99 → V100` row is byte-for-byte equal to V116's row (same 2,318-byte line and SHA-256 `d09f0ed2390f7bdf6fc888041122ad7886768c41a7c05a7a694615a0a62f327a`); V117's appended V117 claim is gone. V118 records the fold in a new `V116 → V117` row rather than mutating old history.

7. **CODEX F2 — repaired.** The real §11 inventory now carries `count_oracle_harness_sha256` beside the replay-harness discipline, names `gates/count_oracle_harness.py` REQUIRED/DOES NOT EXIST/class P, binds its §2.3 build contract, and keeps BS-2c DESIGN-gated. Section 2.3's inventory claim is consequently true.

The remaining overlap among the nine rows is accounted for above: GPT56 F1/CODEX F1 share the hidden-population defect; GPT56 F5/CODEX F3 share the form-echo defect; and GPT56 F6/CODEX F2 jointly cover the history/inventory repair.

## 2. New defects in changed regions only

- The v2 appendix generator accepts contradictory parsed and closing population totals; its new “population arithmetic must reconcile” control checks only that a `**0 undisposed; ...**` line exists, not that the number in that line equals `pre_total` or that its stated populations equal the parsed populations.
- The V118 form hardening's right-only kind boundary and `_fields[1]` candidate precondition create new documented-contract bypasses in the changed code, while the new self-test overstates all-four-form coverage.
- No additional defect was found in the V117→V118 draft edits: the title, §2.3 citation, byte-reverted historical row, new V116→V117 trace row, and §11 count-harness inventory insertion are internally consistent; the normal prereg linter reports 16 class P / 9 class E and zero blocking findings.

## 3. Signature question

Yes: signing remains unsafe for reasons the appendix does not name—the purported live 334-finding inventory contains only aggregate counts, the form echo accepts prefixed kind renames and a first-field-corruption-plus-nearby-decoy attack, and its advertised all-four control coverage is not implemented.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V118-APPENDIX
VERDICT: DEFECTIVE
COUNT: 4
F1 | HIGH | KNOWN_DEBT_APPENDIX.md §1 L11–81; STOPPING_RULE_RULING L16–19 | Sixty-three verbatim aggregate count rows sum to 334 but do not enumerate or quote the 334 underlying findings, so the signed debt population remains content-hidden.
F2 | MEDIUM | KNOWN_DEBT_APPENDIX.md §2 L95–97; V116_WHOLE_REVIEW_GPT56.md F3 | The claimed full-verbatim GPT56 F3 paragraph changes source `form’s` (U+2019) to `form's` (U+0027).
F3 | HIGH | ref/gen_string_field_registry.py L571–614, L821–848; V118 §11 L1566 | Right-only kind boundaries, the first-field candidate prerequisite, and form-0-only deep controls leave prefix-rename and corrupt-declaration-plus-decoy bypasses while claiming all-four-form closure.
F4 | MEDIUM | gates/gen_known_debt.py L128–147, L206–225 | The v2 parser/emitter accepts a closing audit-debt total inconsistent with parsed rows, so its advertised population reconciliation and self-test do not prevent another hidden or contradictory ledger summary.
<!-- END FINDINGS-BLOCK -->