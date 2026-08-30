# V117 APPENDIX MINI-ROUND — GPT56

## 1. The appendix

The pinned appendix was verified before reading: sha256 `3237631836e95b1b3d22f7c6b851f59db06efc297c55433cd61c0a81d4b20e63`.

**DEFECTIVE.** `gen_known_debt.py --check`, its 2/2 self-test, and `gen_repair_ledger.py --check` pass, but the derivation is not an honest summary of the ledger it names. `gen_known_debt.py` reads only `DISPOSITIONS` (V100–V116), so §1 reports 177 findings, zero non-REPAIRED, and “every dispositioned finding reads REPAIRED”; the generated `REPAIR_LEDGER.md` independently and expressly carries **334 pre-convention findings as standing audit debt** (generator lines 401–410; ledger final line). None of those 334 appears as live debt or a §3 residue. This violates the stopping ruling’s “every remaining finding or acknowledged limitation,” “quoted in full,” and “honest bounded list, not a hidden one” requirements.

The V116 excerpts are not all verbatim and are not quoted in full. GPT56 F1’s source continues with a semicolon — “freeze itself; an appendix…” — while the appendix changes that semicolon to a period and truncates the argument; GPT56 F3 changes source-initial “The defect” to “the defect”; CODEX F3 changes source-initial “A control” to “a control.” The other four excerpted sentences are faithful substrings, but sentence extraction is not the ruling’s required full quotation of each eligibility argument.

Section 3 is also non-exhaustive independently of the 334 historical findings: V117 itself expressly acknowledges the unresolved pre-unblinding numerical-route question (§5 line 535), the caller-pair-only authorization guard (§5 lines 559–569), the count-only rather than partition-complete sample guard (§5 lines 570–579), and the still-dual-valued Stage-P contract (§2.6 lines 275–295); none is named in §3 or the open-build inventory. In addition, the listed echo residue misstates its source: it says every echo is demoted to a tripwire, while `ref/gen_string_field_registry.py` lines 790–807 calls the form echo’s co-located pair “the authoritative declaration” and contains no corresponding form-echo demotion (only `_preimage_echo` is expressly called a tripwire at lines 532–537).

## 2. The V117 fold

The pinned V117 draft was verified before reading: sha256 `67dd1d9070586a313d1b902f73df64765c59f6dbb5d3dc1fece58b9b47a51662`.

The count-oracle and T1 changed regions implement their mapped repairs: §2.3 names `gates/count_oracle_harness.py` as REQUIRED/absent/class-P, makes it the only production entry, binds exact argument buffers and the §2.4 universe digest/cardinality, adds stale/substitution fixtures, and DESIGN-gates BS-2c; §7 agrees; §11 now says the interleaving is a T1 violation with only its consequence bounded.

The form-echo fold is not byte-faithful to the FINDINGS_MAP entry: the map requires co-location within **400 bytes** (lines 325–327), while both the draft/source implementation use **900 bytes** (`gen_string_field_registry.py` lines 578 and 792–803). The source’s seeded form controls also exercise only `FORM_SCHEMAS[:1]`, despite the shipped table containing four kinds. The changed check does bind kind to a nearby tuple and rejects the current authoritative-declaration corruption attacks, but it does not implement the mapped 400-byte contract.

The fold introduced a new repair-trace defect in a changed region: V117 edits the historical **V99→V100** §10 cell by appending a V117 count-harness disposition. That statement is true of V117, not of the V99→V100 transition, and it contradicts the appendix’s own assertion that §10 historical cells are “as-written.” A current repair belongs in V116→V117 provenance, not in an old transition’s historical bytes.

## 3. The signature question

- **Appendix:** Yes—its hidden 334-item audit-debt population, omitted acknowledged limitations, and altered/truncated “verbatim” quotations make signing this appendix as the ruling’s exhaustive known-debt instrument unsafe.
- **Fold:** Yes—the unacknowledged 400→900 contract drift and mutation of the V99→V100 historical trace cell are changed-region defects not themselves named in the appendix.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V117-APPENDIX
VERDICT: DEFECTIVE
COUNT: 6
F1 | HIGH | appendix §1 / gen_known_debt.py:18–23,107–136 / REPAIR_LEDGER.md final line | The appendix filters out the ledger’s 334 expressly standing pre-convention audit-debt findings, then reports zero non-REPAIRED and an all-REPAIRED disposition set.
F2 | MEDIUM | appendix §2 / V116 GPT56 F1,F3 and CODEX F3 | Three claimed-verbatim excerpts alter punctuation or capitalization, and the eligibility arguments are excerpted rather than quoted in full as the stopping ruling requires.
F3 | HIGH | appendix §3 / V117 §2.6:275–295 and §5:535,559–579 | Section 3 omits acknowledged Stage-P, numerical-route, authorization, and sample-completeness limitations, so the signed debt inventory is not exhaustive.
F4 | MEDIUM | appendix §3 echo residue / ref/gen_string_field_registry.py:532–537,790–807 | The appendix says every echo is demoted to a tripwire, but the form echo’s source calls its pair authoritative and does not contain that demotion.
F5 | MEDIUM | FINDINGS_MAP:325–327 / V117 §11 / ref/gen_string_field_registry.py:578,792–803 | The fold implements a 900-byte form co-location window where the V116→V117 map specifies 400 bytes, so its bytes do not implement the mapped repair.
F6 | MEDIUM | V117 §10 V99→V100 row | The fold injects a V117 count-harness disposition into the historical V99→V100 transition, newly falsifying an as-written repair-trace cell.
<!-- END FINDINGS-BLOCK -->