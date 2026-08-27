# SECTION 6 REVIEW R14 — CODEX

## Verdict

R14 closes the narrow R13 calibration-carrier finding at the document-contract level: it chooses route (b), requires a pinned `verify_lock()` to resolve the BS-L-bound BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`, pins the implementation/schema digest, and requires the negative low-bound fixture. Route (b) is preferable to route (a): it leaves BS-5f as a Stage-C receipt and makes the independent verifier, rather than a producer-authored PASS field, establish calibration admissibility. The section is nevertheless not clear because Part 2 still does not satisfy its own completeness claim: several outside-§6 conforming edits required by Part 1 are absent, including a previously identified §7 count/DESIGN-inventory correction whose falsity can be reproduced directly from current V15.

## Digest verification — performed before opening the subject

- Required SHA-256: `d151824355006d9e97f17f465d4321d19f3b478f239d5432fc85d0997245d5e9`.
- Independently computed before opening `SECTION6_DRAFT_AGY_R14.md`: `d151824355006d9e97f17f465d4321d19f3b478f239d5432fc85d0997245d5e9`.
- Result: **MATCH**. The bytes reviewed are the pinned bytes.

## Numbered findings

1. **BLOCKING — Part 2 lines 101–114 / §7 seam / Clause 3 and Rows B, N, O, P: the claimed complete outside-§6 edit list remains incomplete.**

   **Evidence.** Part 1 requires more outside work than Part 2 names:

   - **§7 count and DESIGN inventory.** Current V15 §7 lines 595–600 says “One of twelve class-P slots is filled” and lists BS-2f, BS-5p, BS-8p and BS-9 as DESIGN slots. I independently parsed the current tables: they contain **14 class-P and 6 class-E rows**. Applying R14 Part 2 items 5–6 removes class-P BS-L, adds class-P BS-2k, and adds class-E BS-L, yielding **14 class-P and 7 class-E rows**. The prose would still say twelve; it would also omit DESIGN slots BS-2a and BS-2k and retain BS-2f despite V15 lines 341–342 and 624 calling BS-2f value-only. Part 2 has no count/inventory replacement or lint edit. This exact seam had been stated explicitly in `SECTION6_DRAFT_AGY_R5.md` Part 2 line 187 but is absent from R14.
   - **Canonical receipt/schema seams.** Part 1 line 21 says its closed non-χ-bearing list uses the pinned `SLOT_SCHEMA` “as conformed by this revision's code items”; Rows B/N/O and Clauses 3–7 require authenticated BS-2f checkpoint fields, a canonical BS-L artifact, an unblinding receipt/final checkpoint, archive-transition fields, and their verifiers. The pinned v9 `SLOT_SCHEMA` at lines 185–205 has no BS-2a, BS-2k or BS-L entry, and its BS-2f schema has only `(brickid, objid, c, accept_flag, bin, boundaries, mask_digest)`. A code search found no `verify_lock()`, BS-L, BS-2k, unblinding-receipt, adequacy-receipt, stage-completion, or acceptance-evidence implementation. R14 item 7 now adds the Row-J guard and route-(b) `verify_lock()` requirement, but it still does not list the actual SLOT_SCHEMA additions and the BS-2f/BS-L/unblinding schema conformances Part 1 requires.
   - **§5 guard seam.** Current V15 §5 lines 429–434 enumerates the production guards and requires only a mask-bound BS-5f before the verdict calculation. R14 Part 2 item 3 adds verification of the post-unblinding adequacy receipt and final-mask binding, but does not explicitly conform §5 and the pinned production symbol to require and verify the canonical BS-L artifact and one-use unblinding receipt that Row P and Clause 3 make mandatory. A literal application therefore leaves §5's declared guard surface incomplete.
   - **Other literal outside seams.** Part 1 line 23 narrows §2.5's producer checksum list to source images; Clause 10 and current V15 §6.3/§10 require the replacement to enter the repair trace. Part 2 contains neither the §2.5 conformance nor the §10 trace edit. Its code list also omits named Part-1 mechanisms such as `verify_unblinding_receipt`, `verify_archive_seal`, the opening-authorization/replay verifier, `recompute_acceptance_ledger`, enforceable-mediation gate checks, and the general `SLOT_SCHEMA` update. These were explicit in R5 Part 2 lines 188–192 and have disappeared from the asserted-complete list.

   **Why it fails.** The defect is not that the unresolved code has not yet been written; the brief expressly permits implementation to remain unresolved. The defect is that Part 2 claims to enumerate every conforming edit needed by the atomic candidate but still omits required edits. Applying Part 2 literally leaves false §7 arithmetic/classification, an old §5 guard declaration, and missing schema/verifier work beneath normative Part-1 receipts. Thus R14 repairs the three R13-created omissions but does not make the broader completeness claim true.

   **Smallest sufficient repair.** Restore the missing outside-edit entries without changing the accepted branch partition, phases, values, rows, or clauses: (a) regenerate §7's class count and replace its DESIGN inventory, with lint against parsed rows/classifications; (b) enumerate the required SLOT_SCHEMA/receipt changes for BS-2f, BS-2k, BS-L and the unblinding/adequacy artifacts; (c) conform §5 and its pinned production guard to canonical BS-L, one-use unblinding, adequacy and exact-final-mask verification; (d) list the remaining named verifier/mediation/recompute implementations; and (e) add the §2.5 and §10 conforming edits. Keep all implementation work honestly UNRESOLVED until it exists.

## Part 2 completeness walk

| Part-1 dependency outside §6 | R14 Part 2 status |
|---|---|
| BS-2a REFUSED/UNFILLED; BS-6 blocked | Present — item 1 |
| Remove pre-lock reason (c); move non-finite/confidence handling post-unblinding; no post-attrition Stage-C rerun | Present — item 2 |
| §5 adequacy/final-mask refusal guard | Partial — item 3 omits explicit canonical BS-L and one-use unblinding guards |
| Row-P exact-parent closure and ordered adequacy consequence | Present — item 4 |
| Move BS-L P→E and add class-P BS-2k | Present — items 5–6 |
| Recompute §7 count and replace DESIGN inventory; lint both | **Absent** |
| Conform pinned receipt schemas for BS-2f checkpoints, BS-2k, BS-L and unblinding/adequacy artifacts | **Absent / not enumerated by the route-specific digest sentence** |
| Row-B hard block and C2 hermetic worker/fixtures | Present — item 7 bullets 1–2 |
| Row-J low-bound guard | Present — item 7 bullet 3 |
| Route-(b) `verify_lock()`, implementation/schema digest pin, negative low-bound fixture | Present — item 7 bullets 4–5 |
| Remaining named Part-1 verifiers, replay guard, recompute and mediation implementation | **Absent** |
| §2.5 source-image-only checksum scope | **Absent** |
| §10 repair-trace entry | **Absent** |

Accordingly, Part 2's completeness claim does **not** hold.

## Route (b) adjudication

The route taken is unambiguously **(b)** (status line 3, Part 2 line 113, and Part 3 C3 line 122). Its required dependency is checkable in principle:

1. BS-L binds the calibration-record digest.
2. `verify_lock()` resolves the corresponding authenticated BS-8f bytes.
3. The verifier independently computes `all(a_LB_b >= 0.85)`.
4. Low-bound BS-8f must fail the negative fixture and cannot yield a passing lock.
5. Only a passing lock can authorize unblinding and Row P.

This closes rather than merely relocates the narrow R13 finding, provided the named future implementation and schema are eventually delivered and gated. Route (a) is not better: adding a producer-authored BS-5f calibration bit/minimum would enlarge the Stage-C receipt and still require the lock verifier to authenticate its source. Route (b) checks the authoritative BS-8f record directly. Row J's and Clause 3(c)'s phrases that BS-5f “binds” or carries “BS-5f's complementary calibration PASS” should be read as a sequencing prerequisite, not as a new BS-5f field; the operative route-(b) carrier is BS-L's BS-8f digest plus verifier recomputation.

## Clause 10 — both directions over the whole table

### Forward: every branch terminates in one stated consequence

- **Row I:** any allocated missing/non-finite instrument output halts before BS-8f; the usable-finite complement emits BS-8f.
- **Row J calibration:** any per-bin `a_LB_b < 0.85` emits `INCONCLUSIVE-BY-CALIBRATION` and halts pre-unblinding; the exact complement is all bins `>= 0.85`.
- **Row J protocol:** trial-count or frozen implementation/protocol deviation is checked before Stage C/BS-5f and terminates `VOID` through the row's void rule.
- **Row J Stage C:** with calibration and protocol admitted, `< 962` successes, `refuted`, or `nonconservative` emits `INCONCLUSIVE-BY-POWER`; `>= 962` with neither fail-closed flag is the sole PASS route to BS-5f.
- **Row O:** one authorized P7 invocation emits the unblinding receipt; pre-lock invocation, replay, or out-of-destination decryption is void.
- **Row P accounting:** the ordered eight-state precedence assigns missing, duplicate, orphan and malformed records one unconditional `INCONCLUSIVE-BY-*` refusal each; absence, non-finiteness and low confidence are removals; accepted-finite is the complement. Any one removal then emits `INCONCLUSIVE-BY-CALIBRATION`, with no Stage-C rerun. Zero removal binds the already verified pre-unblinding calibration and Stage-C PASS.
- **Clause 8:** unresolved retrospective custody at freeze refuses the run; resolution is required before freeze.
- **Other rows:** each normal authorized act has its named emission, and each forbidden-surface branch has one void consequence. I found no new double outcome or deferred post-data judgement in Part 1.

The forward partition holds. Finding 1 is an outside-edit completeness failure, not a new overlap in the accepted Part-1 partition.

### Reverse: every stated outcome has a reachable, authenticated witness in the document contract

- Pre-lock `INCONCLUSIVE-BY-CALIBRATION` is witnessed by authenticated BS-8f with any low bin; route (b) now supplies the lock-verifier dependency and negative fixture requirement.
- `INCONCLUSIVE-BY-POWER` is witnessed by `< 962` successes or either fail-closed self-verification flag after the protocol checks.
- `VOID` is witnessed by protocol/count/digest deviation and the table's stated forbidden acts.
- Row P's four accounting refusals and three exclusion states each have the corresponding exact-parent record state; any exclusion witnesses the post-unblinding calibration-applicability refusal.
- The successful path requires BS-8f calibration PASS independently recomputed by `verify_lock()`, BS-5f Stage-C PASS, BS-L, one-use unblinding, zero-removal exact-parent closure, BS-7f, BS-V and then disclosure.

No outcome is orphaned in the prose contract. The current implementation cannot yet authenticate these future witnesses; that is correctly marked unresolved, and Finding 1 requires the full implementation/schema work to be listed rather than silently implied.

## Threshold sweep — value, phase, failure effect

1. **Calibration lower bound:** threshold `0.85`; evaluated from BS-8f at Row J/P5 before Stage C, BS-5f, BS-L and unblinding; any bin `< 0.85` emits `INCONCLUSIVE-BY-CALIBRATION`, all bins `>= 0.85` continues. This matches V15 lines 566–567 and `A_FLOOR = 0.85` / `adjudicate_path()` at code lines 81 and 1492–1496.
2. **Stage-C trial count:** exactly `1_000`; checked before Stage-C execution/BS-5f; mismatch is protocol deviation and `VOID`. Code lines 77 and 1277 match.
3. **Stage-C success threshold:** `< 962` FAIL and `>= 962` PASS out of 1,000; evaluated P5 before BS-L; FAIL emits `INCONCLUSIVE-BY-POWER`. Code lines 78 and 1277 match.
4. **Stage-C self-verification:** any `refuted` or `nonconservative` result at P5 is fail-closed and emits `INCONCLUSIVE-BY-POWER`; neither is required for PASS. Code lines 1275–1277 match.
5. **Post-unblinding attrition:** one or more removals at Row P/P8 emits `INCONCLUSIVE-BY-CALIBRATION`; zero removals is the complement; no Stage-C rerun occurs.
6. **Confidence exclusion:** the numeric threshold belongs to the REFUSED/UNFILLED BS-2a design and must exist before BS-6. If eventually filled, application is post-unblinding: below threshold → `EXCLUDED-BY-CONFIDENCE` → at least one removal → `INCONCLUSIVE-BY-CALIBRATION`. No executable run can defer choosing the value because BS-2a blocks the first image byte.
7. **Exact-parent cardinality:** zero, more than one, extra and malformed records are evaluated post-unblinding with the four fixed `INCONCLUSIVE-BY-*` effects; exactly one structurally valid record continues through the remaining precedence states.
8. **Allocated-sample finiteness and opening cardinality:** any allocated unusable output halts before BS-8f; Row O permits exactly one P7 opening and treats replay as void.

I found no conflicting threshold value, phase, or failure effect.

## Failed attacks

- I tried to recreate R13's missing authenticated calibration-PASS witness. R14's route-(b) requirement defeats it at the document level by making BS-L's BS-8f binding and independent verifier recomputation mandatory and by requiring a low-bound negative fixture.
- I tried to route a calibration or Stage-C FAIL into Row P. BS-L requires the passing pre-unblinding path, so Row P correctly contains no dead post-unblinding re-evaluation branch.
- I tried to produce two consequences for Row P's missing/duplicate/extra/malformed states. They are absent from the void column and retain one ordered unconditional refusal each.
- I tried the value/phase/effect boundaries at equality: `a_LB_b == 0.85` passes the calibration floor, `successes == 962` passes Stage C, and the trial count must equal 1,000. The draft and code agree.
- The attack that landed was the broader completeness walk: the three new R14 bullets are present, but older required outside seams have dropped out of the list.

## Testimony

- The future Row-J guard, `verify_lock()`, BS-L/unblinding/adequacy schemas, mediator, C2 worker, replay store and negative fixture do not exist in the pinned implementation and were not executed. Their described future behavior is Testimony until implemented and gated.
- BS-2a REFUSED/UNFILLED, Rows C2/E blocked, and the first image byte blocked are draft/brief state assertions. I did not independently adjudicate the external BS-2a gate reports.
- I did not verify the predecessor count of 208,405 or any archive seal state. I did not read `/Users/duhokim/NebulaMindData/`, touch χ-bearing inputs, inspect secrets, or perform a network fetch.

## Evidence ledger

Content read:

- `BRIEF_SECTION6_REVIEW_R14.md`
- `BRIEF_DRAFT_SECTION6_R14.md`
- `SECTION6_DRAFT_AGY_R14.md`
- `SECTION6_DRAFT_AGY_R13.md` through the R13→R14 unified diff
- `SECTION6_REVIEW_R13_CODEX.md`
- `SECTION6_REVIEW_R3_GPT56.md`
- `SECTION6_DRAFT_AGY_R5.md` Part 2 and relevant repair map
- `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` relevant §2.5, §2.7, Stage C, §5, calibration/void-rule, §7 and §10 passages
- `../ref/successor_ref_v9.py` constants, `SLOT_SCHEMA`, Stage-C return partition, and calibration adjudicator

Checks run:

- `shasum -a 256 SECTION6_DRAFT_AGY_R14.md`
- R13→R14 unified diff
- Full Row-P extraction and whole-table parse (20 lifecycle rows)
- Whole-document branch/outcome/threshold token counts
- Independent current-V15 §7 row parse (14 class P, 6 class E) and post-edit arithmetic (14 class P, 7 class E)
- Searches for `verify_lock`, BS-L/BS-2k schemas, unblinding/adequacy receipts, stage completion, acceptance evidence, producer-checksum scope and prior completeness findings

No source, preregistration, code, draft-under-review, or data artifact was modified. The only write was this required referee report.

**NOT CLEAR**