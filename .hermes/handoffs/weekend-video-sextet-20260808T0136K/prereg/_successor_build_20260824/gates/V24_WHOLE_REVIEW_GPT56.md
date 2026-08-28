# V24 WHOLE-DOCUMENT REVIEW — GPT56

Verdict: **NOT CLEAR.** The dispatched V24 bytes match the supplied SHA-256, the §7 binding tables independently close at 15 Class-P and 8 Class-E rows, and the count emitter survives an adversarial in-memory row insertion. The new §10 mechanism does not close: V24 omits its own V23→V24 transition, the checker reports that omission, embedding the current draft's whole-file result digest creates an unresolved self-reference, and the replacement deleted the finding→change mapping that §6.3 still requires. BS-2v is now honestly labelled UNRESOLVED, but its current coverage test is not yet converter-independent and its receipt contract is not exact enough for a gate to reject a non-conforming receipt using only this document.

## Subject identity — verified before substantive review

I recomputed SHA-256 over the exact current bytes of `../PREREG_SUCCESSOR_DRAFT_V24_20260827.md` and compared the resulting 64-hex value with the digest supplied in `BRIEF_V24_WHOLE_REVIEW.md` lines 3–5:

- computed current V24: `6d722dc51316a2dbc3f3cf07a7dec8c8c5776df16388b43177681899cb32f977`
- brief pin: `6d722dc51316a2dbc3f3cf07a7dec8c8c5776df16388b43177681899cb32f977`
- comparison: **MATCH — exact 64-hex digest equality**

I also recomputed V23 as `134433199c85ea4566eab7aae146455518d92d314893b3cba7a6a413163454b7` and compared it with V24 lines 3–4: **MATCH**. I recomputed all V1–V24 whole-file hashes; every 16-hex endpoint printed in the 22 written §10 rows agrees with the corresponding current draft bytes.

## Numbered findings

### 1. HIGH / BLOCKING — §10 lines 802–831 and `tools/prereg_trace.py` lines 106–171: the generated trace is stale, its check is non-conforming, and its current-draft result digest is self-referential

**Why it fails.**

1. V24's written table contains 22 rows and stops at V22→V23 (line 829). An independent rebuild from all 24 immutable drafts yields 23 transitions. The omitted row is:

   `| V23 → V24 | 134433199c85ea45 | 6d722dc51316a2db | §10 (+26/−87), (preamble) (+3/−3), §7 (+2/−2), §11 (+1/−1) | no row-count change |`

2. Running the supplied checker on V24 returns exit 1: `MISSING: no written row for V23 → V24; 23 computed transition(s); 1 problem(s)`.
3. This is not repaired by blindly rerunning and pasting the output. The row's `result sha256` is the hash of the whole V24 file. Inserting that hash into V24 changes V24's bytes and therefore changes the hash being inserted. The current design has no canonical exclusion/normalisation rule for §10 and no external post-freeze trace artifact, so it asks the file to contain its own whole-file digest.
4. The `--check` implementation does not do what its interface claims. Lines 161–169 check only that a transition string occurs somewhere in the whole document and that either endpoint digest occurs somewhere. It never compares the written section statistics, row-count transition, both endpoint digests, or exact rendered row with the computation. I altered one section statistic and one row-count field in memory; the current check predicate reported zero problems.

**Independent comparison.** I separately parsed V1–V24, recomputed SHA-256, used an independent line diff and heading attribution, and recounted the two §7 tables. All 22 common written rows were byte-equal to the independent reconstruction; only V23→V24 was absent. Thus the historical rows are accurate as observations, but the current trace is incomplete and the mechanism cannot maintain the stated whole-file result digest in-band as designed.

**Smallest sufficient repair.** Choose one non-self-referential contract and state it exactly: either (a) §10 in Vn covers only transitions through V(n−1), while V(n−1)→Vn is emitted in an external immutable gate artifact after Vn freezes; or (b) define and test a canonical digest that excludes/normalises the generated §10 block. Then make `--check` extract the exact §10 generated block and byte-compare every rendered field, with an explicit expected coverage range. Do not use a whole-file Vn digest inside Vn without a defined exclusion rule.

### 2. HIGH / BLOCKING — §6.3 lines 597–599 versus §10 lines 802–831: replacing prose with the computed table broke the document's binding finding→change obligation

**Why it fails.** Section 6.3 still requires that “every gated revision … changes one thing per finding,” that “the §10 trace maps finding → change,” and that any untraceable change be listed separately with its hypothesis. V24 line 804 claims this mapping is “expressed as finding IDs referenced from the referee reports.” The table contains no finding ID, no referee-report reference, no change identity, and no hypothesis. It reports only the six largest changed sections and aggregate added/removed line counts. A changed section is neither a finding nor a change mapping, and truncating to six sections can omit changed regions.

The previous prose was fallible, but deleting it did not repeal the normative §6.3 dependency. The replacement therefore makes line 804 false and leaves every transition without the mapping the current document requires. This is precisely the dependency break the brief asked reviewers to test.

**Smallest sufficient repair.** Keep the mechanically computed observation table, but add a separate mechanically validated mapping whose keys are immutable referee report digest + finding ID and whose values identify the bounded patch/change or explicitly mark an untraced hypothesis. Alternatively amend §6.3 through a gated revision to require only the observation trace. Do not claim finding IDs are present when none appear.

### 3. HIGH / BLOCKING — §7 line 680, §7.1 lines 705–763, and §11 line 849: BS-2v coverage is not finally independent of the converter; V24 correctly admits it is unresolved

**Why it fails.** V24 improves the future design: line 680 requires converter-emitted IDs and fixture-exercised IDs to be compared with the contents behind a preregistration-pinned §7.1 digest that the converter cannot author. That would be the right three-party structure if the external normative bytes and digest were actually frozen.

They are not. No literal `registry_digest` value appears in §7.1, §7, or §11. Line 680 explicitly says the registry “cannot be pinned before the converter exists” and marks BS-2v UNRESOLVED. Section 11 line 849 then reintroduces conflicting ownership by saying the converter “must define a canonical closed antecedent registry,” even while a later sentence says the gate compares against the pinned §7.1 digest. A converter-defined registry is not the preregistration-owned authority.

The claim that the registry cannot be pinned before the converter exists is also unexplained by the mechanism: the 53-row §7.1 table exists now and can be canonically serialized and hashed without converter bytes. I independently counted **53 rows, 53 unique IDs, zero duplicate IDs, and 53 `VOID` failure effects**; under the simple raw-table UTF-8 serialization including terminal newline its SHA-256 is `c52c7f713f483ce1b39fb45ccffd7e2c1301bf43ec187738bdbc7fa57174929c`, demonstrating that converter-independent pinning is mechanically possible once the canonical serialization is chosen. That example digest is evidence, not a proposed normative pin; the document must define its own serialization and pin.

**Judgment requested by the brief:** the current BS-2v coverage test is **not finally independent of the converter**. The proposed future comparison can become independent, and V24 is honest about the present unresolved state. Because BS-2v remains unfilled, BS-6 and the first image byte remain blocked rather than being silently authorised.

**Smallest sufficient repair.** Define the canonical §7.1 serialization in the preregistration, insert its literal digest before converter implementation, state that the converter only consumes that authority, delete “the converter must define” from §11, and require three separately authenticated ordered vectors: normative, emitted branches, and exercised fixtures. Check uniqueness before set/order comparison and reject any metadata mismatch as well as missing/extra/non-VOID rows.

### 4. HIGH / BLOCKING — §6.1 lines 503–511, §7 line 680, and §11 lines 839, 849: the authenticated BS-2v receipt is still not rejectable from the written schema alone

**Why it fails.** Section 6.1 makes non-χ-bearing eligibility conditional on conformity to a pinned `SLOT_SCHEMA`. Section 11's explicit `SLOT_SCHEMA` work item at line 839 names BS-L, BS-2k, deferred BS-2a, and BS-2f/BS-L changes; it still does not require an exact `SLOT_SCHEMA['BS-2v']` entry. Line 849 lists useful minimum concepts — registry digest, converter digest, ordered normative IDs, exercised IDs, uniqueness/count closure, metadata, classification — but “including” is open-ended and is not an exact schema.

Using only the written text, a gate still lacks: a schema ID/version; canonical field names, types, ordering and serialization; an authentication envelope and verifier; a fixture implementation/battery digest; a separately authenticated ordered converter-emitted ID vector (distinct from “ordered normative IDs”); duplicate evidence for each vector before set conversion; separately named normative-vs-emitted and normative-vs-exercised results; and a terminal PASS/REFUSE field whose authentication and recomputation are required. “All authenticated” does not define how a verifier authenticates decoded fields.

Consequently V24 lines 23–24 overstate that the receipt-schema blocker is closed at document-contract level. The implementation is safely marked unresolved, but a gate cannot yet reject every non-conforming receipt using only the current contract.

**Smallest sufficient repair.** Add an exact, closed BS-2v slot schema and canonical serialization to the preregistration/next atomic code inventory; bind its literal schema digest; name the verifier and require it to recompute every decoded field and both independent comparisons from pinned inputs; pin the fixture battery and converter implementation; and define one fail-closed terminal result. Replace “including” with an exhaustive field contract.

### 5. MEDIUM / BLOCKING TO A CLEAN DOCUMENT — preamble lines 5 and 23–25 contradict the document's live unresolved status

**Why it fails.** Line 5 says “VOID reachability [is] repaired here,” while §5 line 472, §5 line 474, Clause 10 line 567, §7 line 680, and §11 line 849 all say the category/converter is not executable or unresolved. Lines 23–25 similarly claim the GPT56 schema blocker is closed at document-contract level, contradicted by Finding 4. These are live V24 banner claims, not historical quotation, and a reader encounters them before the later caveats.

**Smallest sufficient repair.** Replace line 5 with the exact current state (“VOID antecedents are textually enumerated; reverse reachability and BS-2v remain unresolved”) and narrow lines 23–25 to the actual V24 delta (“required receipt concepts were added; exact slot schema and implementation remain unresolved”).

## Independent §7 count and emitter audit

- Structurally bounded recount: **15 Class-P rows** and **8 Class-E rows**.
- The Class-E table includes `Unblinding receipt`; 22 of the total 23 rows carry a `BS-` identifier.
- `python3 tools/prereg_lint.py …V24… --gates …/gates` reports `23 (15 class P, 8 class E)` and no inconsistency.
- `python3 tools/prereg_counts.py …V24…` reports 15/8 and says the prose already matches.
- Independent adversarial in-memory test: after inserting a synthetic sixteenth Class-P table row without editing the prose, `count_rows()` returned 16/8, `prereg_counts.rewrite()` changed “fifteen” to “sixteen,” and a second run was byte-idempotent with zero changes.

**Judgment:** the §7 current count is correct and the emitter is operational for the exercised structural change. Unlike the §10 design, it has no whole-file self-digest cycle.

## Clause 10 and threshold-neighbour audit across §§0–11

### Forward termination

The pre-existing non-VOID branches retain stated effects and phases. I read the neighbours of each operative threshold family:

- population cuts (`z < 0.15`, ellipticity `< 0.1836734693877551`, `dered_mag_r < 17.7`, `shape_r > 1.5`) act in the pre-freeze selection chain;
- retained `N_eq ≥ 100,000` is geometry-derived; the production runner's failure effect is `INCONCLUSIVE-BY-POWER` before a numeric verdict;
- the confidence threshold remains deliberately undefined in refused BS-2a before any image byte; this blocks BS-6, while any later low-confidence removal maps to `INCONCLUSIVE-BY-CALIBRATION`;
- any `a_LB_b < 0.85` is evaluated at P5 after BS-8f and before Stage C/BS-L/unblinding, with immediate `INCONCLUSIVE-BY-CALIBRATION` and halt;
- only on that complement does spread `≤ 0.03` select scalar and `> 0.03` select profile; spread failure is not a run failure;
- Stage P/C use 1,000 trials and `x ≥ 962` (961 fails), with one-sided p `< 0.001`; Stage-C failure at P5 emits `INCONCLUSIVE-BY-POWER` before BS-L;
- production numeric regions are post-unblinding: p `< 0.001` plus sign/amplitude/floor conditions yields REPRODUCED, p `> 0.05` plus the strict amplitude bound yields REJECTED, and the complement is INCONCLUSIVE;
- the `3.09·σ_ours(a_LB)` detection floor is evaluated for REPRODUCED; below it cannot be named REPRODUCED;
- hand-check floors `≥10` per non-empty joint cell and `≥30` per live inherited stratum fail rather than shrink.

The V23→V24 diff changes none of those threshold values, phases, or failure effects. No new threshold-neighbour contradiction was found.

### Reverse reachability

Reverse reachability still stops at `VOID`: §5 and Clause 10 say it is not executable, BS-2v is unresolved, and no pinned converter currently maps all 53 normative antecedents. This is an honest fail-closed status. Findings 3–4 show why the proposed gate is not yet a converter-independent, receipt-rejecting closure. BS-6 and the first image byte therefore remain blocked.

## Failed attacks / checks that held

1. Digest substitution attack failed: V24 matches the brief's full SHA-256, and V23 matches V24's predecessor pin.
2. Historical trace-row attack failed for all 22 common rows: independent diff/count reconstruction matched each written row byte-for-byte.
3. Binding-table boundary and non-BS first-cell attacks failed: the count is 15/8, including `Unblinding receipt`.
4. Count-emitter drift attack failed: a synthetic row insertion was detected, rewritten correctly, and idempotent on rerun.
5. Registry duplicate/effect attack failed at the textual level: 53 rows, 53 unique IDs, all with `VOID` effect; lifecycle Rows A–S plus C2 and the five outside-row antecedents have textual registry coverage.
6. Hidden execution-authority attack failed: V24 repeatedly keeps BS-2a refused, Rows C2/E unable to run, BS-2v unresolved, and BS-6/first image byte blocked.
7. Threshold-neighbour attack found no V24-introduced change in a value, phase, or failure effect.

## Testimony / unverified assertions and limits

- I did not read `/Users/duhokim/NebulaMindData/` and performed no fetch.
- I did not re-run the scientific selection, Stage-P measurement, closure fixtures, external citation checks, or χ-bearing work. Their reported measurements, authorization chronology, source verification, prior referee times/verdicts, and real-geometry claims remain **Testimony** in this bounded document-contract review.
- I treated prior V23 referee reports as allegations/context and re-derived the V1–V24 digest/trace facts and §7/§7.1 counts from current bytes.
- I did not modify the subject or any predecessor. The only intended write is this report in the assigned gates directory.
- The repository had extensive pre-existing modified/untracked state before this review; no claim is made that the repository as a whole is clean.

## Evidence ledger

Content read: `gates/BRIEF_V24_WHOLE_REVIEW.md`; V24 whole document; V23→V24 diff; `tools/prereg_trace.py`; `tools/prereg_counts.py`; relevant `tools/prereg_lint.py`; `gates/GENERATED_TRACE.md`; `gates/run_replacements.py`; `gates/run_replacements2.py`; prior `V23_WHOLE_REVIEW_GPT56.md` and `V23_WHOLE_REVIEW_CODEX.md`. Programmatic byte reads: all V1–V24 drafts for full SHA-256, independent transition diff, and §7 row-count reconstruction.

Executed checks: `shasum -a 256` over V24 and V1–V24; V23→V24 `git diff --no-index`; prereg linter; prereg count emitter in report mode; prereg trace generator and `--check`; independent Python reconstruction of all transition rows; independent structural recount of §7 and §7.1; in-memory adversarial count-emitter mutation/idempotence test; in-memory corruption test against the trace check predicate; pre-write read-only `git status`.

**NOT CLEAR**