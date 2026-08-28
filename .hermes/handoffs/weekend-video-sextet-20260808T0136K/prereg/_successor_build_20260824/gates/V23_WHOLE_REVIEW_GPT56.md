# V23 WHOLE-DOCUMENT REVIEW — GPT56

Verdict: **NOT CLEAR.** V23 is a correct preregistration in its count repair and remains honest about being an unfinished programme, but the two central BS-2v repairs asserted for this round are not actually operative: the converter still authors the alleged reference registry, and §11 still contains no BS-2v `SLOT_SCHEMA` addition or authenticated receipt fields. Consequently a gate cannot test converter coverage against an independently authored normative set, and BS-2v is not lawfully inspectable under the document's own closed-list rule. The standing blocks remain effective: Findings 1, 2, 2b and 3 are unresolved; BS-2a is refused; Rows C2 and E cannot run; BS-6 and the first image byte remain blocked.

## Digest-first comparison

I recomputed SHA-256 over the current bytes of `PREREG_SUCCESSOR_DRAFT_V23_20260827.md` and compared it directly with the value on line 7 of `gates/runner_v23_chain.log`:

- live V23: `134433199c85ea4566eab7aae146455518d92d314893b3cba7a6a413163454b7`
- runner pin: `134433199c85ea4566eab7aae146455518d92d314893b3cba7a6a413163454b7`
- comparison: **MATCH**

I also recomputed V22 and compared it with V23 lines 3–4:

- live V22: `9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3`
- V23 predecessor pin: `9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3`
- comparison: **MATCH**

The predecessor pins in V17 through V23 also match the live predecessor bytes. The V22→V23 diff is not a pure count-only repair: it adds 77 lines and removes 9, including the 53-row antecedent registry and the trace assertions discussed below.

## Independent §7 recount

I counted contiguous data rows in each binding-slot table, excluding the header and delimiter and stopping at the end of that table rather than keying on a `BS-` prefix.

- Class P: **15 data rows** (V23 lines 676–690).
- Class E: **8 data rows** (V23 lines 696–703).
- The eighth Class-E row is line 701, whose first cell is **`Unblinding receipt`**, not a `BS-` identifier.

Thus V23 line 672's prose numbers, 15 and 8, match the actual binding-slot tables.

## Numbered findings

### 1. HIGH / BLOCKING — §7 and §11, lines 680, 705–763, 910 — the antecedent registry is not independent of the converter

Why it fails:

- V23 inserts a 53-ID table at lines 705–763 and calls it canonical.
- But the operative BS-2v slot at line 680 still says: **“The converter must define a canonical closed antecedent registry.”**
- The required equality remains only `set(fixture.antecedent_id) == set(converter.branch_id)`. This compares two converter-side products to each other; it never requires either set to equal the fixed IDs in §7.1.
- Section 11 line 910 repeats the same ownership and same two-set comparison: the converter defines the registry, then the fixture manifest is compared with exercised/converter IDs. This preserves the self-reference identified in the preceding round.
- Merely placing a table elsewhere in the document does not remove converter authorship when both operative requirements still assign authorship to the converter and never name the table as a separately owned equality operand.

Independent coverage attack that held: the inserted table has **53 unique IDs**. It accounts for the 48 semicolon-delimited “what voids the run” antecedents in §6.1 Rows A–S, plus three §5 categories, the §2.7 threshold-change antecedent, and the §6.3 binding-change antecedent. The defect is therefore not obvious row omission; it is custody and comparison direction.

Smallest sufficient repair:

1. State that §7.1 itself is the immutable normative registry authored by the preregistration text, with a canonical serialization/digest that the converter cannot emit, replace, or derive as its authority.
2. Require two separate equalities against that normative set: `set(converter.branch_id) == set(normative_registry.id)` and `set(fixture.antecedent_id) == set(normative_registry.id)`.
3. Require uniqueness before set conversion, exact source/phase/failure-effect equality for every ID, and refusal on missing, duplicate, extra, non-`VOID`, or metadata-mismatched rows.
4. Remove “the converter must define” from lines 680 and 910.

### 2. HIGH / BLOCKING — §6.1 and §11, lines 503–511, 680, 891, 898–910 — BS-2v is named in the closed list but has no pinned slot schema or authenticated receipt contract

Why it fails:

- Line 505 newly adds BS-2v to the exhaustive non-χ-bearing slot-receipt list. Under lines 503–511, however, membership is conditional on conformity to an authenticated pinned `SLOT_SCHEMA`; naming a slot is not itself a schema.
- Section 11's actual `SLOT_SCHEMA` item at line 900 requires additions for BS-L and BS-2k, defers BS-2a, and discusses BS-2f/BS-L. It does **not mention BS-2v**.
- The generic converter item at line 910 specifies intent and coverage behavior but does not define BS-2v canonical receipt fields, authenticated decoded fields, canonical serialization, schema version, normative-registry digest, converter implementation digest, fixture receipt digest, or the separately evaluated equality/uniqueness results needed to reject a non-conforming receipt.
- Therefore a gate cannot inspect a BS-2v receipt under the document's own “everything else is χ-bearing by default” rule. An unfilled BS-2v remains unable to unlock BS-6, which is safe, but V23 has not supplied the claimed lawful inspectability.

Smallest sufficient repair: add an explicit BS-2v entry to §11's `SLOT_SCHEMA` work item and enumerate/authenticate at least the schema/version, normative §7.1 registry digest, converter implementation/protocol digest, converter branch records with ID/source/phase/effect/outcome, fixture identity and exercised records, duplicate counts, both independent equality results, and a fail-closed terminal gate result. Bind those schema bytes into the pinned implementation/schema digest.

### 3. MEDIUM / BLOCKING TO A CLEAN ROUND — §10 line 891 versus §11 lines 898–910 — the V22→V23 repair trace makes a materially false completion claim

Why it fails:

- The V22→V23 trace says V23 **“Added `BS-2v` to … §11's `SLOT_SCHEMA` additions with its authenticated fields.”**
- The actual V22→V23 diff changes no §11 line at all. Section 11 line 900 still omits BS-2v, and line 910 is byte-identical to V22's converter item.
- The same trace says the registry is independent, contradicted by lines 680 and 910 as described in Finding 1.

Smallest sufficient repair: implement Findings 1–2, then retain the trace claim; or, if the implementation remains open, rewrite the V22→V23 trace to say only that §7.1 was inserted and BS-2v was added to §6.1's name list, with independence and schema closure still open.

### 4. MEDIUM — §7 line 672 and `runner_v23_chain.log` lines 9–17 — the revised linter still does not count the two slot classes correctly

Why it fails:

- The document asserts at line 672 that the prose count equals the parsed table count.
- The runner instead reports Class P = 15 and Class E = 62, then emits a prose-count disagreement. Its “independent recount” repeats 15/62.
- The immediate Class-E binding-slot table has 8 rows. The 62 arises because the counter runs beyond the Class-E slot table into the new §7.1 registry instead of stopping at line 703. Thus the two printed checks again share one parser-boundary error.

Smallest sufficient repair: scope each counter to its immediate markdown table (header through the first non-table line), rerun it, and require a clean 15/8 result before claiming the lint assertion. Keep the separate first-cell-agnostic row counter; do not restore identifier matching.

## Trace audit — all seven transitions

I compared the live predecessor/successor bytes for V16→V17, V17→V18, V18→V19, V19→V20, V20→V21, V21→V22, and V22→V23.

- The corrected V16→V17 count row is true: V16 had 14 Class-P rows and 8 Class-E rows while its prose said 14/7; V17 retained 14/8 table rows and corrected the prose to 14/8.
- V18, V19, and V20 retained 14/8 tables and prose.
- V21 added the converter row, creating 15/8 table rows, while its prose remained 14/8.
- The corrected V21→V22 row is true: V22 assigned `BS-2v`, moved prose to 15/7, and thereby introduced the Class-E mismatch despite the table remaining 15/8. Its converter language stated intent but did not create an independent gate.
- The V17→V18, V18→V19, V19→V20, and V20→V21 trace descriptions match their actual changed regions.
- The seventh entry, V22→V23, is not wholly accurate because its independence and §11-schema assertions are false (Findings 1–3).

Accordingly, the two specifically corrected historical rows are now true, but **all seven trace entries are not accurate**.

## Clause 10, §§0–11, both directions

Forward termination: the non-VOID paths retain named outcomes and failure effects. The new registry gives every listed VOID antecedent a `VOID` effect and a phase. No V22→V23 change alters a numeric decision threshold or its neighboring branch consequence.

Reverse reachability: still unresolved at `VOID`, exactly as V23 admits at §5 lines 472–474 and Clause 10 line 567. A 53-row prose inventory does not make `VOID` executable. Because BS-2v is unfilled, self-referential, and lacks an inspectable slot schema, no pinned producer/conversion presently reaches `VOID` for all antecedents. Clause 10 therefore remains non-executable, and BS-6 plus the first image byte remain blocked. This is honest unfinished-programme status, not permission to proceed.

Threshold-neighbour sweep: the V22→V23 diff changes no threshold value, phase, or failure effect. Existing neighbors remain explicit: calibration `< 0.85` is evaluated at P5 before Stage C and halts `INCONCLUSIVE-BY-CALIBRATION`; spread `> 0.03` selects the profile path only after the calibration floor; Stage-C fewer than 962/1,000 at P5 halts `INCONCLUSIVE-BY-POWER`; post-unblinding removal at P8 halts `INCONCLUSIVE-BY-CALIBRATION` without a Stage-C rerun; numeric p/amplitude bands are post-unblinding verdict rules; and protocol/non-finite deviations assigned to VOID remain blocked on the missing converter. The refused BS-2a confidence threshold remains deliberately unset and blocks BS-6 rather than becoming a post-data choice.

## Failed attacks / checks that held

1. Digest substitution attack failed: both the runner's V23 pin and V23's V22 predecessor pin match live bytes.
2. First-cell identifier attack failed: direct row counting finds the phrase-led Unblinding receipt and closes Class E at 8.
3. Registry omission/duplication attack failed at the textual inventory level: 53 rows, 53 unique IDs, with count closure against 48 §6.1 row antecedents plus five antecedents from §5/§2.7/§6.3.
4. Corrected-history attack failed for V16→V17 and V21→V22: the live diffs support V23's corrected descriptions.
5. Hidden threshold-delta attack failed: V22→V23 changes no threshold or neighboring branch consequence.
6. Premature-execution attack failed: V23 continues to state that BS-2a is refused, Rows C2/E cannot run, VOID is not executable, and BS-6/first image byte are blocked.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/` and performed no fetch.
- I treated prior referee statements as testimony unless independently checked against the draft sequence. I independently checked the seven draft transitions and their available predecessor digest pins; I did not re-run the science code or inspect χ-bearing data.
- The asserted authorization chronology, source citation verification, measured geometry, fixture results, and prior referee verdict times were not re-established in this bounded review and remain Testimony.
- The review wrote only this report in the assigned gates directory; it did not modify the subject draft.

**NOT CLEAR**