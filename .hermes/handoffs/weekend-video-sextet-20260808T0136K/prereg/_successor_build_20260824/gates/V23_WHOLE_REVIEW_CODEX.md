# V23 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** V23 repairs the binding-slot count and the two historical trace rows, but the central BS-2v repair is still self-referential at the enforceable equality check, and the claimed BS-2v `SLOT_SCHEMA` addition/authenticated fields do not exist in §11. The document remains an unfinished programme and is honest that `VOID` is unexecutable and that BS-6/the first image byte remain blocked; however, V23 is not yet a correct preregistration contract for the proposed BS-2v gate.

## Digest-first comparison

I computed SHA-256 over the current bytes of `../PREREG_SUCCESSOR_DRAFT_V23_20260827.md` and compared that 64-hex digest with the value after `V23 PINNED sha256:` in `runner_v23_chain.log` line 7.

- computed: `134433199c85ea4566eab7aae146455518d92d314893b3cba7a6a413163454b7`
- runner pin: `134433199c85ea4566eab7aae146455518d92d314893b3cba7a6a413163454b7`
- comparison: **byte-for-byte digest equality; MATCH**

I also computed V22 as `9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3` and compared it with V23 lines 3–4; **MATCH**. The V16→V23 predecessor banner chain was recomputed independently; every successor pin matched its predecessor's current bytes.

## Independent §7 recount

I bounded the recount to the two binding-slot tables under `## §7 Binding slots`, stopping the Class-E table before `### §7.1`. I counted each Markdown data row, not identifiers.

- Class P: **15 data rows** — BS-1, BS-1b, BS-2a, BS-2k, BS-2v, BS-2c, BS-2o, BS-5p, BS-2s, BS-2m, BS-3, BS-9, BS-4, BS-7p, BS-8p.
- Class E: **8 data rows** — BS-6, BS-2f, BS-8f, BS-5f, BS-L, **Unblinding receipt**, BS-7f, BS-V.

The prose at line 672 is correct: 15 Class-P slots and 8 Class-E slots. The eighth Class-E row is line 701 and its first cell is `Unblinding receipt`, not a BS identifier.

## Numbered findings

### 1. HIGH / BLOCKING — §7 and §11, lines 680, 705–763, 910 — the operative coverage test remains self-referential

Why it fails:

V23 now supplies a document-owned 53-row antecedent table at §7.1, so a converter-independent candidate set physically exists. But the enforceable requirements do not compare either produced set to that normative table:

- line 680 requires `set(fixture.antecedent_id) == set(converter.branch_id)`;
- line 680 simultaneously says **the converter must define** the canonical closed antecedent registry;
- line 910 again says the converter must define the registry and requires only equality between manifest IDs and exercised IDs.

Thus a converter that omits the same antecedent from its branch list and fixture set still passes the stated equality. The new §7.1 table is not named as an input to either equality. A gate is not required to decide coverage from a set the converter does not produce. This is the same common-author defect in a new location, not the requested three-way independent closure.

Smallest sufficient repair:

Make §7.1's exact stable-ID set the normative set `N`, bind its canonical serialization/digest outside the converter, and require both independent equalities:

- `set(converter.branch_id) == N`
- `set(fixture.antecedent_id) == N`

Require uniqueness before set conversion, so duplicate IDs cannot disappear. Delete “the converter must define” the registry from lines 680 and 910; the converter consumes the document-owned registry and cannot author or replace it.

### 2. HIGH / BLOCKING — §6.1, §10, §11, lines 503–505, 891, 900–910 — BS-2v is listed but has no canonical authenticated receipt schema

Why it fails:

Adding `BS-2v` to §6.1's closed list at line 505 makes eligibility conditional on conformance to a pinned `SLOT_SCHEMA`; it does not define that conformance. §11 line 900 names exact `SLOT_SCHEMA` additions for BS-L, BS-2k and deferred BS-2a, but not BS-2v. The BS-2v paragraph at line 910 describes converter behavior and a fixture coverage receipt without specifying canonical BS-2v receipt fields, authenticated serialization, registry identity/digest, converter identity/digest, fixture identity/digest, the three compared ID sets, uniqueness results, equality results, or terminal gate state.

Consequently a gate cannot authenticate decoded BS-2v fields or fail a malformed/non-conforming BS-2v slot receipt under §6.1's own closed-list rule. The V22→V23 trace at line 891 is materially false when it says V23 added BS-2v to “§11's `SLOT_SCHEMA` additions with its authenticated fields”; the V22→V23 diff contains no §11 change at all.

Smallest sufficient repair:

Add a dedicated §11 `SLOT_SCHEMA['BS-2v']` requirement with exact canonical authenticated fields, at minimum: schema/version; §7.1 registry serialization and digest; converter implementation/protocol digest; fixture battery digest; ordered normative, converter and exercised ID vectors; per-vector uniqueness/duplicate evidence; both equality results; per-ID source, phase and failure effect; converter result for every ID; and a terminal PASS/REFUSE state. Bind the schema bytes into the implementation/schema digest and require the verifier to recompute all fields. Correct the V22→V23 trace to describe only bytes actually changed.

### 3. LOW / PROCESS — §7 line 672 and `runner_v23_chain.log` lines 9–17 — the claimed lint assertion is not a passing independent check

Why it fails:

The document says the “Lint assertion” equates prose and parsed table counts. The pinned runner instead reports 15 Class P and **62 Class E**, then emits a prose-count disagreement because it sweeps the new §7.1 registry into the Class-E region. Its “independent recount” repeats the same 15/62 result. Those two outputs share the same faulty section boundary and are not independent checks. The underlying binding-slot prose is correct by the identifier-blind 15/8 recount above, but the document's assertion that its lint check establishes that fact is false.

Smallest sufficient repair:

Scope the slot counter structurally from each binding-table header to that table's end (Class E must stop before `### §7.1`), treat the first-cell content as opaque, and make the independent recount use a separately implemented boundary rule. Re-run and pin output showing 15/8.

## Seven-entry repair-trace audit

I diffed the current bytes for all seven transitions V16→V17 through V22→V23 and recomputed every predecessor banner pin.

- V16→V17: corrected row is true. V16 had 7 while the table had the non-BS `Unblinding receipt` eighth row; V17 changed prose to 8.
- V17→V18: trace matches the diff.
- V18→V19: trace matches the diff.
- V19→V20: trace matches the diff.
- V20→V21: trace matches the diff.
- V21→V22: the two corrected V23 descriptions are now true: V22 introduced 7 on the wrong instruction, and V22 gave BS-2v an ID/intent but did not create an independent enforceable gate.
- V22→V23: count and historical-row claims match the diff; the “independent” registry claim is not made enforceable (Finding 1), and the §11/schema-fields claim is false (Finding 2).

Therefore all predecessor pins match, and the two specifically corrected older rows are true, but **all seven current trace entries are not accurate because the newest V22→V23 entry overclaims two repairs**.

## Clause 10, both directions, §§0–11

Forward termination remains substantially enumerated: numeric regions, pre-statistic halts, accounting refusals, per-attempt consequences, table-row void conditions, and disclosure sequencing name outcomes/failure effects. Reverse reachability to `VOID` remains unresolved exactly as stated at lines 472, 474 and 567; BS-2v is unfilled at line 680 and implementation remains required at line 910. The document correctly keeps BS-6 and the first image byte blocked. Findings 1 and 2 mean V23 has not yet converted that honest unresolved state into a receiptable, converter-independent closure.

## Threshold audit

I read the neighbouring clauses around the document's operative thresholds and found no additional blocking value/phase/effect mismatch:

- galaxy-selection cuts operate in the pre-freeze population chain;
- `N_eq ≥ 100,000` is derived from the mask and failure is `INCONCLUSIVE-BY-POWER`;
- the confidence threshold remains deliberately undefined in refused BS-2a, pre-image, and therefore blocks BS-6;
- `a_LB_b < 0.85` is evaluated after BS-8f and before Stage C/unblinding, with `INCONCLUSIVE-BY-CALIBRATION` and halt;
- spread `≤ 0.03` versus `> 0.03` is evaluated after the calibration-floor complement and selects scalar versus profile, not PASS versus failure;
- Stage P/C use 1,000 trials, `x ≥ 962` (961 fails), and p `< 0.001`; Stage-C failure emits `INCONCLUSIVE-BY-POWER` before BS-L;
- post-unblinding numeric verdict regions use p `< 0.001`, p `> 0.05`, the 0.0408 amplitude, 3σ bands, and the `3.09·σ_ours(a_LB)` floor, with the complementary region `INCONCLUSIVE`;
- hand-check floors of at least 10 per non-empty joint cell and 30 per live inherited stratum fail rather than shrink.

## Standing-state check

The standing state is preserved: Findings 1, 2, 2b and 3 remain unresolved; BS-2a is refused/unfilled; Rows C2 and E cannot run; BS-6 and the first image byte remain blocked. An unfilled BS-2v does not bypass those blocks.

## Failed attacks / things that held

1. Digest substitution attack failed: the V23 runner pin matches the current subject bytes.
2. Predecessor drift attack failed: V22's banner pin and the complete V16→V23 successor-pin chain match recomputed hashes.
3. Identifier-keyed recount attack failed against the document: the binding tables really contain 15 and 8 rows, including `Unblinding receipt`.
4. Historical blame attack failed: the repaired V16→V17 and V21→V22 rows now state the actual diffs plainly.
5. Hidden execution attack failed: the text repeatedly and consistently says VOID conversion is unimplemented and blocks BS-6/first image byte.
6. Threshold-neighbour attack found no new value/phase/failure-effect contradiction beyond the BS-2v contract findings above.

## Testimony / unverified assertions

- I did not inspect `/Users/duhokim/NebulaMindData/` and performed no fetch.
- I did not re-run scientific code, fixtures, external-source checks, or real-geometry measurements; those historical/scientific claims remain Testimony in this pass.
- I did not treat prior referee verdicts as evidence for V23. They were read only where V23 itself reports them.
- The statement that the wrong 8→7 instruction came from the coordinator is chronology testimony; the V21→V22 byte change itself is independently verified.

## Evidence ledger and custody

Read content: the brief, pinned runner log, V23 whole document, and predecessor drafts V16–V22 for hash/diff checks. Computed SHA-256 for V16–V23. Performed an identifier-blind bounded Markdown-table recount and a V22→V23 neighbour diff. Wrote only this report in the assigned gates directory; did not modify the subject or predecessors.

**NOT CLEAR**