# V24 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** V24's §7 count is correct and the old V22→V23 false completion claim has been removed, but the document is not clear. BS-2v is still not independent: no registry digest is pinned, §7 says the converter cannot author the registry while §11 still says it must define it, and the claimed authenticated receipt remains an open-ended requirement rather than an exact `SLOT_SCHEMA` contract a gate can validate. The generated §10 replacement also fails its own current-draft check, cannot embed the current whole-document digest without self-reference, silently omits changed sections in ten historical transitions, and no longer supplies the finding→change map that §6.3 requires. Clause 10 additionally has a pre-existing Row-L signing contradiction and inaccurate registry phases. The standing blocks remain effective: `VOID` is unresolved, BS-2a is refused, Rows C2/E cannot run, and BS-6/the first image byte remain blocked.

## Digest-first comparison

I computed SHA-256 over the current bytes of `../PREREG_SUCCESSOR_DRAFT_V24_20260827.md` and compared all 64 hex digits directly with the digest supplied in the review instruction and `BRIEF_V24_WHOLE_REVIEW.md` lines 3–5:

- computed V24: `6d722dc51316a2dbc3f3cf07a7dec8c8c5776df16388b43177681899cb32f977`
- instructed/brief digest: `6d722dc51316a2dbc3f3cf07a7dec8c8c5776df16388b43177681899cb32f977`
- comparison: **MATCH**

I also computed V23 as `134433199c85ea4566eab7aae146455518d92d314893b3cba7a6a413163454b7` and compared it with V24 lines 3–4: **MATCH**. I computed V1–V24 live and compared the 16-hex endpoints printed in every existing §10 row with those draft bytes. All 22 written rows have the correct endpoint prefixes.

## Independent machine-surface checks

### §7 count

I independently bounded each count to its immediate Markdown table, treated the first cell as opaque, and stopped at the first non-table line:

- Class P: **15** rows.
- Class E: **8** rows.
- The eighth Class-E row is `Unblinding receipt`, so only 22 of the 23 total rows carry a `BS-` identifier.

`tools/prereg_counts.py` independently reported 15/8 and “prose already matches the table”; `tools/prereg_lint.py` also reported 15/8 and no inconsistency. V24 line 672 is correct.

### §10 trace

I compared the written §10 table against every V1–V24 draft, not merely against the generator's self-report.

- There are **24 drafts and 23 adjacent transitions**.
- V24 §10 contains **22** transition rows, ending at V22→V23.
- Every existing row is byte-equal to the corresponding row currently rendered by `tools/prereg_trace.py`.
- The generator renders one additional row, V23→V24, with endpoints `134433199c85ea45` and `6d722dc51316a2db`; that row is absent.
- The generator's own `--check V24` exits 1: `MISSING: no written row for V23 → V24`.
- For V23→V24, I independently reproduced the generator's SequenceMatcher attribution: §10 +26/−87, preamble +3/−3, §7 +2/−2, §11 +1/−1, no row-count change. Those sums are 125 changed lines under that algorithm. A standard `git diff --numstat` aligns the same bytes as +35/−96, showing that “line counts by diff” is algorithm-defined rather than a unique byte fact.

## Numbered findings

### 1. HIGH / BLOCKING — §6.1 Row L and Clauses 3/6, lines 533, 548–559 — the required signing path voids itself

**Why it fails.** Row L requires Duho to emit three distinct signed objects: the freeze signature, the BS-L detached signature over the canonical lock-body digest, and the canonical opening authorization. Clause 6 explicitly defines the opening authorization as a signed body/envelope. But Row L's unqualified void condition is “signing anything but the canonical lock digest.” Read literally, signing the required freeze or opening-authorization body voids the run. The registry then labels `VOID-6.1L-WRONG-SIGNATURE` as P7 (line 749), although the canonical BS-L-body signature occurs at P6 and the freeze signature at P0. This leaves no clean lifecycle path through the acts the same row requires.

**Smallest sufficient repair.** Scope the Row-L condition to each act: at P0 authenticate only the canonical freeze body; at P6 sign only the canonical BS-L body digest; at P7 authenticate only the canonical opening-authorization body. Give each failure a separate stable antecedent ID and its real phase, or state one exact phase-indexed rule that distinguishes the three bodies.

### 2. HIGH / BLOCKING — §7/§7.1/§11, lines 680, 705–763, 849 — BS-2v coverage is still not converter-independent

**Why it fails.** V24 describes the right architecture at line 680: compare converter-emitted and exercised fixture IDs against preregistration-owned registry contents that the converter cannot author. But it does not instantiate that architecture:

1. No literal `registry_digest` value is pinned anywhere in the preregistration.
2. Line 680 marks the gate unresolved and says the registry cannot be pinned before the converter exists. The opposite ordering is required for independence, and the 53-row registry already exists in the current document, so its canonical bytes can be defined and digested now.
3. Section 11 line 849 still says the converter “must define a canonical closed antecedent registry,” directly contradicting line 680's statement that the converter does not author it.

Thus this is not finally an independent coverage test. It is an honest unresolved design plus contradictory ownership language, not an executable three-way comparison.

**Smallest sufficient repair.** Define the registry's canonical serialization over the current §7.1 table, pin its literal digest in this preregistration before converter implementation exists, delete converter authorship from §11, and require separate ordered/unique comparisons `converter IDs == pinned registry IDs` and `fixture IDs == pinned registry IDs`, including exact metadata equality.

### 3. HIGH / BLOCKING — §6.1 and §11, lines 503–511, 680, 839, 849 — a gate still cannot reject a non-conforming BS-2v receipt using only the written contract

**Why it fails.** Section 11 line 849 now lists the requested concepts—registry digest, converter implementation digest, ordered normative IDs, exercised IDs, uniqueness/count closure, per-ID metadata, result classification—but calls them fields “including” those items. It still does not:

- require an exact `SLOT_SCHEMA['BS-2v']` entry (line 839's explicit slot-schema work names BS-L, BS-2k and deferred BS-2a, not BS-2v);
- close the field set or define schema/version, field types, canonical serialization, authentication envelope, or verifier;
- require the converter-emitted ordered ID vector as an authenticated receipt field separate from the normative and exercised vectors;
- identify/authenticate the fixture battery or its digest;
- state which decoded fields the gate recomputes rather than trusts.

Under §6.1's closed-list rule, a generic promise that a future receipt will be canonical is not the pinned schema conformance needed to classify that receipt as non-χ-bearing. Different incompatible receipts could satisfy the prose list.

**Smallest sufficient repair.** Add an exact, closed `SLOT_SCHEMA['BS-2v']` contract and named verifier. Include schema/version, canonical registry bytes+digest, converter implementation/protocol digest, fixture battery digest, three ordered ID vectors (normative/emitted/exercised), duplicate evidence for each, exact per-ID metadata and conversion result, both independently recomputed equality results, count closure, authentication envelope, and terminal PASS/REFUSE state; bind those schema/verifier bytes in the pre-BS-6 pin.

### 4. HIGH / BLOCKING — §6.3 and §10, lines 597–599, 802–831 — replacing prose removed the required finding→change custody map

**Why it fails.** Section 6.3 still requires every gated revision to change one thing per finding and says “the §10 trace maps finding → change; any change not traceable to a finding is listed separately with its hypothesis.” The replacement table contains no finding ID, report identity, hypothesis, or mapping column. Section 10 line 804 and the generated footer claim finding IDs are referenced from referee reports, but no such IDs or report references appear in the table. The table now answers “which lines differed,” not “which finding authorized each change.” This is exactly a dependency on the removed prose, and it is broken.

**Smallest sufficient repair.** Keep computed byte observations, but add a non-characterising mapping keyed only by immutable referee-report digest + finding ID to the changed-region IDs, plus a separately enumerated unrequested-change/hypothesis list. Alternatively move that mapping to a pinned sidecar and amend §6.3 to name it rather than §10.

### 5. HIGH / BLOCKING — §10 and `tools/prereg_trace.py`, lines 802–831 and tool lines 106–171 — the current transition is missing and the whole-document result digest is self-referential

**Why it fails.** The generator sees 23 transitions, while the embedded table has 22 and its own check fails on V23→V24. Simply pasting the missing generated row cannot repair this: the row embeds V24's current whole-document digest, so inserting it changes V24's digest and §10 line counts. In an in-memory test, inserting the generated `6d722dc51316a2db` row changed the full digest to `c692b8c6653319e9…`; replacing the embedded digest with that new value changed the actual prefix again to `baf447825369d730`. This is structural self-reference, not a stale paste alone.

The checker is also weaker than its docstring: tool lines 161–169 search the whole document for a transition phrase and accept a row if either endpoint prefix appears anywhere. They do not compare the written row's section counts or §7 counts with the generated row.

**Smallest sufficient repair.** Do not embed a current whole-document result hash inside the bytes it hashes. Put the current transition in an external gate receipt/sidecar that pins V24, or define and pin a canonical digest that excludes a precisely delimited generated region. Then make `--check` extract §10 only and compare every expected row/field exactly, with no missing or extra transitions.

### 6. MEDIUM / MATERIAL ACCURACY — §10 and `tools/prereg_trace.py`, lines 806–831 and tool lines 111–114 — “sections changed” silently means only the six largest sections

**Why it fails.** The table header says “sections changed,” and the footer says sections and line counts are computed, but `sorted(... )[:6]` discards every changed section after the largest six without an ellipsis or count. Independent reconstruction found omitted changed sections in **10 of the 22 written transitions**. Examples:

- V1→V2 omits §4, §9 and §8.
- V5→V6 omits eleven sections, including §10, §0, §§2.1/2.3/2.4/2.2/2.5.
- V15→V16 omits §7, §11, §5, §6, §10 and §2.5.
- V16→V17 omits §2.6, §6.1 and §7.

Those rows are not complete observations of what changed. The generator path and algorithm are also referenced without a digest; live hashes during this review were `c2123fa4…` for `prereg_trace.py`, `2909be88…` for `prereg_counts.py`, and `9d1a9cf…` for `prereg_lint.py`.

**Smallest sufficient repair.** Emit all changed sections, or label the column “six largest changed sections” and append an explicit omitted-section count/list. Pin the generator/checker bytes or bind them in the gate receipt, and state the exact diff algorithm if line attribution is contractual.

### 7. MEDIUM / CLAUSE-10 METADATA — §7.1 and §6.1, lines 709–763 versus 533–540 — several registry phases describe the permitted row phase, not the phase of the forbidden antecedent

**Why it fails.** The registry closes numerically—53 unique IDs, comprising 48 semicolon-delimited lifecycle-row antecedents plus five from §5/§2.7/§6.3—but at least three phase fields are not exact:

- `VOID-6.1L-WRONG-SIGNATURE` is labelled P7 (line 749), while the BS-L canonical-body signature is P6 and the freeze signature is P0.
- `VOID-6.1P-EARLY-EXECUTION` is labelled P8 (line 757), while its source is “any execution before unblinding” (line 537), i.e. before the allowed P8 path.
- `VOID-6.1S-EARLY-EXPORT` is labelled P9 (line 763), while its source is “any export before BS-V” (line 540); BS-V is produced at P8, so the forbidden branch is pre-P9.

A converter consuming these exact metadata rows would authenticate false phase information even if every ID converted to `VOID`.

**Smallest sufficient repair.** Define “Phase” as trigger phase/window, not the allowed row phase, and correct every timing violation accordingly (`pre-unblinding`, `pre-BS-V`, P0/P6/P7 act-specific signing, etc.). Gate exact source/phase/effect equality, not IDs alone.

## Clause 10 and threshold sweep, both directions

Forward non-VOID termination remains substantially explicit. I read neighboring text for each operative threshold family:

- §2.1: the 2026-09-05 release choice is resolved at BS-1; absent DR11 photo-z selects Branch B, while selecting A voids current §0 pins and requires a new preregistration.
- §2.2–§2.3: the eight galaxy predicates (`1`, `0`, non-PSF, `flux_r > 0`, `0 ≤ z < 0.15`, ellipticity `< 0.183673…`, `r < 17.7`, `shape_r > 1.5`) act in pre-freeze parent selection; predicate failure excludes the row. Exact enumeration applies at ≤16 positive-count bricks; retention is `floor(0.8572n)`; `N_eq ≥ 100,000` is pre-statistic and failure yields `INCONCLUSIVE-BY-POWER` in the runner.
- §2.7: the confidence value remains deliberately unset in refused BS-2a and therefore blocks BS-6. Once frozen, Row P applies it at P8; below-threshold removal yields `INCONCLUSIVE-BY-CALIBRATION`; choosing/moving it after real inference is `VOID`.
- §3/§4: `a_LB_b < 0.85` is evaluated after BS-8f and before Stage C/statistics and halts `INCONCLUSIVE-BY-CALIBRATION`; only its complement reaches the spread split, where `≤0.03` selects scalar and `>0.03` selects profile, not failure. Stage P/C use p `<0.001`, 1,000 trials, 95% CP lower bound `≥0.95`, equivalently `x≥962` with 961 failing. Stage-C failure at P5 emits `INCONCLUSIVE-BY-POWER` before BS-L. The self-verification 10× boundary requires independent retest and one unconfirmed success fails closed.
- §5: after unblinding, REPRODUCED uses p `<0.001`, correct sign, the 0.0408 three-sigma band and evaluated 3.09σ floor; REJECTED uses p `>0.05` and strict amplitude bound `<0.0408`; equality/gaps fall to numeric `INCONCLUSIVE`.
- §6.3: hand-check floors are ≥10 per non-empty joint cell and ≥30 per live inherited stratum; infeasibility fails rather than shrinking.

I found no new numerical value/boundary/failure-effect mismatch beyond the carried-open dual Stage-P definition and refused confidence design, both honestly blocking. Reverse reachability still fails at `VOID`, as V24 admits at lines 472, 474, 567 and 680. Findings 1–3 and 7 show that even the proposed registry/converter path is not yet exact. BS-6 and the first image byte therefore remain blocked.

## V22→V23 claim and computed-table dependency result

The old V22→V23 prose claim that V23 completed BS-2v independence and added authenticated §11 schema fields is gone. The replacement V22→V23 row accurately reports only byte-level observations: §7.1 +59/−0, §10 +11/−3, preamble +3/−3, §7 +2/−1, §6.1 +1/−1, and no slot-row-count change. That specific false completion claim is repaired by deletion.

However, replacing all prose with the computed table broke the §6.3 finding→change dependency (Finding 4), omitted the current revision (Finding 5), and silently truncated historical section inventories (Finding 6). Thus the replacement did break mechanisms that depended on the former prose.

## Failed attacks / checks that held

1. Subject substitution failed: V24's full SHA-256 matches the instructed digest exactly; V24's V23 predecessor pin also matches live V23.
2. Historical endpoint-drift attack failed for the 22 written trace rows: every printed 16-hex endpoint matches the current immutable draft bytes.
3. Existing-row generation mismatch failed: all 22 embedded transition rows exactly equal the current generator's corresponding rows.
4. §7 boundary/identifier attack failed: the immediate tables contain 15 Class-P and 8 Class-E rows, including the phrase-led `Unblinding receipt`; both count and lint tools agree.
5. Registry omission/duplication attack failed at the ID-count level: 53 rows, 53 unique IDs, closing against 48 table antecedents plus five external antecedents.
6. V22→V23 false-completion attack failed: that semantic claim has been removed rather than carried forward.
7. Hidden execution authorization failed: the draft repeatedly and consistently keeps BS-2a refused, Rows C2/E non-runnable, `VOID` non-executable, and BS-6/first image byte blocked.
8. Threshold-neighbor sweep found no additional numeric threshold defect beyond the explicitly carried-open designs and the Clause-10 phase/signing findings above.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/` and performed no fetch.
- I did not run scientific measurements, reference fixtures, or external-source verification. Geometry, source anchors, historical authorization chronology, and earlier scientific receipt claims remain Testimony here.
- Prior V23 referee reports were read to identify the named prior blockers, but none of their conclusions was accepted without rechecking the current drafts and tools. I did not read the sibling V24 referee report.
- “These counts were emitted” is not historically provable from current bytes alone; I verified that the current tool computes 15/8 and would make no change.

## Evidence ledger and custody

Read content: `BRIEF_V24_WHOLE_REVIEW.md`; V24 whole document; V23 whole-review reports; `tools/prereg_trace.py`, `tools/prereg_counts.py`, and `tools/prereg_lint.py`. Read draft V1–V24 bytes programmatically for hashes, adjacent diffs, table counts, and §10 row comparisons. Ran SHA-256 over V1–V24 and the three tools; direct V23→V24 diff/numstat; independent immediate-table recount; independent transition/section reconstruction; registry ID/metadata/count closure; both generators in read-only mode; trace `--check`; prereg linter; and an in-memory self-reference test. No data fetch occurred and no subject/predecessor/tool file was modified. The only file written by this seat is this report; the sibling `V24_WHOLE_REVIEW_GPT56.md` was already untracked before this write and was not opened or changed.

**NOT CLEAR**