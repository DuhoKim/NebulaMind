# §6 SIXTH-PASS (R6b) REFEREE REPORT — GPT56

## Verdict

NOT CLEAR. R6b removes the checksum, and that is a real narrowing, but it does not close the C2 channel. A pixel-reading C2 still chooses three per-object bits, the order and timing of its mediated touches are exported by the access log, and the exact-parent stage-completion artifact has no closed schema at all. Authentication, independent recomputation, hermetic execution, and runtime attestation can prove which pinned program ran and that another program reproduces its answers; without closed predicate definitions and a side-effect/serialization contract, they do not prove that those answers are sign-independent. Clause 9 is not yet an executable oracle for that property. Separately, refusing reason (c) leaves the pre-lock mask able to include objects with no finite instrument output, even though calibration must consume those outputs and Stage C computes power on that mask. Row P defines a consequence only for the confidence cut, not for absent/non-finite outputs. Blocking findings: 1 and 2.

## Numbered findings

### 1. BLOCKER — the checksum channel is narrowed, not closed; C2 retains value, ordering, timing, missingness, and completion-artifact channels

**Row / clause / sentence at issue.** Closed-list item (v), lines 18–26; access-log schema at line 21; rows B–E, lines 37–41; clause 9, line 80; Part 5 items 2–4, lines 119–121.

**Why it fails.** Removing expected/actual cutout digests fixes the literal checksum oracle. It does not make a process that reads every cutout incapable of encoding morphology-derived sign.

First, the output schema is not actually closed. Item (v) says the projection contains “only narrowly enumerated authenticated predicate bits” but introduces the fields with “e.g.” The draft never gives the exact field set, exact Boolean derivation for `parent_attempt_present`, `byte_integrity_pass`, or `canonical_shape_pass`, or a fixed source/serialization for the parent/attempt witness. “Every legal value is mechanically fixed” fixes the range to bits; it does not fix which pixel states map to each bit. A hostile pinned C2 can make `canonical_shape_pass` equal an inferred sign bit, or select which nominal integrity bit fails, and a separately pinned verifier can faithfully recompute the same malicious predicate. Authentication and reproducibility preserve that channel; they do not establish sign-independence.

Second, the table exports a channel outside the row values. Row B logs every C2 touch with timestamp, object identity, operation and success/refusal. C2 is not required to read or publish in canonical parent order, on a fixed schedule, or atomically after complete verification. It can therefore encode inferred signs in access order, delays, refusal placement, or whether/when it reaches stage completion. The exact-parent rule prevents a selectively missing projection from becoming a smaller accepted mask if it is enforced; it does not prevent outcome-conditioned run abort or an outcome-coded log sequence.

Third, the “authenticated C2 exact-parent stage-completion artifact” is neither included in closed-list item (v) nor assigned a closed schema. The draft does not state its exact fields, canonical body, parent-manifest binding, duplicate/extra rejection, serialization, single-issuance rule, or whether partial projections become observable before it is verified. Under line 26 it is χ-bearing by default, yet rows B and D rely on it as a pre-lock authorization object. Its unspecified contents and issuance behavior are themselves writable and missingness channels.

Finally, the proposed enforcement is still a promise rather than a gate oracle. A hermetic allowlist and runtime attestation constrain ambient capabilities and identify bytes; they do not stop those allowed bytes from implementing handedness logic over the pixels they must read. Clause 9 says adversarial encodings “must fail” but does not define the invariant to compare, the exact transformed pairs, which legitimate predicate changes are allowed, or whether “fail” means producer refusal, fixture rejection, or gate failure. The subject's Part 2 line 97 explicitly places implementation of the worker, mediator block, and fixtures in the next atomic revision, and the current pinned `ref/successor_ref_v9.py` contains none of the named R6b C2 symbols.

**Smallest sufficient repair.** Replace “e.g.” with one exact projection schema and freeze, for every bit, a closed-form derivation from a named immutable parent witness and mediated bytes. The independent verifier must implement an independently pinned specification rather than merely duplicate C2's mapping. Give the stage-completion artifact an exact canonical schema and require set equality—not count equality—against the immutable parent set, rejecting missing, duplicate and extra rows. Make projection publication atomic and canonically ordered after closure; prevent C2-chosen timestamps/order/refusal details from entering the externally visible non-χ log surface before the lock. Define clause 9's producer-level metamorphic oracle and expected result for every transformation, plus negative implementations that encode through each bit, ordering, timing, omission, duplicate, extra-parent, and completion field and are proven to make the gate fail. Until those bytes and fixtures pass fresh BS-2a gates, call the route narrowed, not closed.

### 2. BLOCKER — refusing reason (c) relocates the defect into calibration, Stage C, and the verdict path

**Row / clause / sentence at issue.** Row E, line 41; rows F–J, lines 42–46; Row P, line 52; Part 2 items 2–3, lines 93–94; Part 3 C1, line 103; residual risk R3, line 112; current V15 §2.7 lines 302–345 and §4 lines 421–425.

**Why it fails.** R6b honestly stops asking a pre-inference writer to report a future instrument fact. That is a valid refusal of the impossible writer assignment, but the downstream contract is not repaired.

Row E now constructs BS-2f from cutout predicates only. Therefore an object can be `ACCEPTED` even when Row D produces no usable measurement or a non-finite one. That object then enters Row F's calibration bins and hand-check allocation. Row I must read “the corresponding instrument outputs” to form BS-8f, but the draft gives no rule for an allocated object whose output is absent/non-finite: no replacement, no sealed halt, no finite-subset calibration contract, and no authorization for changing the allocation. Thus the pipeline may be unable to produce BS-8f before unblinding.

Even if calibration happens to avoid every unusable object, Row J runs Stage C on the entire BS-2f accepted-position mask. Current §4 defines BS-5f power on exactly that sealed mask. A mask containing rows that cannot enter the scientific statistic inflates the sample and can PASS a power test for a population that will never be analysed.

The promised post-unblinding consequence does not cover this. Row P says only that it “applies confidence-based exclusion” and triggers mask/calibration/power recomputation “if this exclusion removes any object.” Neither Row P nor Part 2 defines how absent/non-finite outputs are detected, whether they are excluded, their precedence relative to confidence, or whether their removal triggers the same recomputation and refusal. A non-finite confidence is not guaranteed to compare below a threshold, and an absent receipt has no confidence to compare. Part 2's phrase “deferring any non-finite instrument outputs to post-unblinding handling” names a destination but supplies no handling rule. This is exactly the refusal silently relocated into the estimator chain.

**Smallest sufficient repair.** Choose one honest route and bind it end to end. Either (a) add the sealed, independently supervised presence/finiteness transaction previously declined, so BS-2f contains only objects with one committed finite output before calibration and Stage C; or (b) remove reason (c) from pre-lock acceptance but define an exact post-unblinding absent/non-finite rule in Row P, apply it before any statistic, and trigger the same deterministic final-mask, calibration-applicability, and Stage-C recomputation/refusal for every removal, not only confidence removals. Route (b) must also solve the pre-unblinding BS-8f problem: the allocation/calibration protocol must either be defined over a provably usable sealed subset without exporting per-object outcomes, or fail the run before BS-8f. BS-5f may not certify a mask containing rows the verdict cannot use.

## Checks that held / failed attacks

1. **Literal checksum attack failed.** No expected or actual cutout digest appears on the R6b acceptance projection; the draft repeatedly keeps cutout digests inside the sealed boundary. Finding 1 concerns the remaining bit/log/completion channels.
2. **Exact-parent intent is materially stronger.** Row E requires exactly one verified projection per parent and rows B/D make C2 completion a prerequisite. If supplied with a canonical set-equality schema and enforced atomically, this can close selective omission and duplicate rows from the realised partition. The current completion artifact is underspecified, so I do not credit implementation-level closure.
3. **Future-execution-status attack failed.** C2 no longer claims to report Row D's completion or finiteness. The draft explicitly refuses reason (c) pre-lock rather than renaming a cutout fact as an instrument fact. Finding 2 concerns the unbound downstream consequence of that refusal.
4. **Universal-ban restoration held.** Clause 1 has the substantive R5 body and binds every person/process to access, not merely disclosure.
5. **Committee G→H→I restoration held.** Rows G, H and I still define view → sole ingestion → aggregate computation, and restored clause 5 says an authorized in-surface act does not void the run. The example changed, but the general rule still covers committee completion.
6. **BS-5f → BS-L → unblinding restoration held.** Restored clause 3 and rows J/N/O/P retain the named sequence, verify-lock refusal, and the gate on the verdict path.
7. **Clauses 3, 4, 5, 6, 7 and 8 were restored substantively from R5.** Mechanical R6→R6b diff shows only the requested clause-body restoration, the Part 5 typo fix, headings/status, and the added restoration item. The disclosed §6.2/§6.3 placeholders remain an assembly gap and are not a finding here.
8. **BS-2a refusal is honest and does not make §6 unreviewable.** R6b says REFUSED/UNFILLED in Row C2 and clause 2 and blocks BS-6. That is the correct present execution state. It does not excuse an incomplete successor contract, and no run may rely on C2 until findings 1–2 and the handedness-amplitude constraint pass fresh gates.

## Testimony

I did not inspect any image, cutout, χ value, sealed-store payload, predecessor-archive content, key, credential, access log, runtime attestation, live process, committee conduct, or `/Users/duhokim/NebulaMindData/`. I did not fetch anything. I did not verify historical archive access, present store mediation, hermeticity, side-channel resistance, or any future C2/Row B/Row P implementation. Statements about how a hostile C2 could encode information and how the proposed mechanisms would behave are contract analysis, not observations of running code. R6b itself places implementation in a future atomic revision.

## Evidence ledger

- Recomputed `SECTION6_DRAFT_AGY_R6B.md` sha256 as `f9743e836ff791906c94726991a7db43f04ef1a82baaaf4b9e0bea60c2c3d566`, matching the referee brief.
- Read `BRIEF_SECTION6_REVIEW_R6B.md`, `BRIEF_DRAFT_SECTION6_R6B.md`, `SECTION6_DRAFT_AGY_R6B.md`, `SECTION6_DRAFT_AGY_R6.md`, `SECTION6_DRAFT_AGY_R5.md`, both R5 referee reports, and `BS2A_REVIEW_GPT56.md`.
- Read current `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` §2.7, §4 and §5 around the acceptance, Stage-C, complete-sample and verdict contracts.
- Mechanically diffed R6→R6b and R5→R6b. R6b's subject hash and R6/R5 comparison hashes were recomputed locally.
- Searched the current pinned `../ref/successor_ref_v9.py` for the R6b C2/integrity/completion/attestation symbols; none were present. This agrees with Part 2's own future-implementation disclosure.
- No data fetch, data-directory read, image read, χ computation, sealed-store operation, preregistration edit, code mutation, or report other than this file occurred.

Blocking findings are 1 (channel narrowed, not closed) and 2 (reason (c) relocated into an undefined calibration/power/verdict path).

**NOT CLEAR**