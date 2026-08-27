# V16 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

V16 is **NOT CLEAR**. The pinned bytes match, the R15 Part-1 §6 body landed byte-for-byte, BS-2f is correctly class E, and most named conforming edits are present. But the whole-document seam exposes two blocking contradictions: §2.7 still retains the deleted reason-(d) confidence contract and gives its threshold to a different slot than §7, and §4 was not conformed to Row J's mandatory pre-Stage-C calibration halt even though §10 says that edit was applied. These defects fail Clause 10 forward termination because a later operator can choose which stated threshold owner and which stated Stage-C entry contract governs.

## Subject identity — verified before opening

- Required SHA-256: `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`.
- Independently computed SHA-256 for `../PREREG_SUCCESSOR_DRAFT_V16_20260827.md`: `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`.
- Result: **MATCH**. The bytes reviewed are the pinned bytes.

## Numbered findings

1. **HIGH / BLOCKING — §2.7's conforming edit is only partial: deleted reason (d) remains live and its confidence threshold has two owners.**

   - **Section and lines:** §2.7 lines 335–372, especially 335–338, 358–363, 365–372; §7 lines 642 and 649.
   - **Applied evidence:** V16 correctly narrows the pre-lock exclusion list to reasons (a)–(b) at lines 335–338 and defers confidence handling post-unblinding. But lines 358–363 still say “Reason (d) is the outcome-adjacent one,” and lines 371–372 still say “The thresholds in (d) are pinned ... in BS-3.” There is no reason (d) left in the enumerated list. Meanwhile §7 line 642 assigns “the numeric confidence threshold and the named authority that sets it” to the refused BS-2a DESIGN slot, while line 649 describes BS-3 as the instrument identity (`τ = 4.4006456017494235`).
   - **Why it fails:** This is not harmless historical quotation. All three passages are live normative §2.7/§7 text. A literal operator can treat BS-3's `τ` as the confidence exclusion threshold under §2.7(7), or wait for BS-2a to set a numeric confidence threshold under §2.7(6)/§7. That changes the post-unblinding `EXCLUDED-BY-CONFIDENCE` branch and therefore whether the run emits `INCONCLUSIVE-BY-CALIBRATION`. Clause 10 fails in the forward direction because the branch's meaning depends on a later choice of threshold owner. It also defeats the fold's claim that the conforming edit was checked “as applied.”
   - **Smallest sufficient repair:** Delete the stale reason-(d) and “thresholds in (d)” language. State one closed post-unblinding confidence predicate, with exactly one owner. If the predicate/value remains part of refused BS-2a, say so consistently and make BS-3's `τ` merely an instrument-identity constant unless a fresh gated design explicitly equates the two. Keep BS-6 blocked until that single contract exists.

2. **HIGH / BLOCKING — §4 was not conformed to Row J's mandatory calibration gate, while §10 falsely says the §4 edit was applied.**

   - **Section and lines:** §4 lines 412–452, especially 448–452; §6 Row J line 526; §10 line 736.
   - **Applied evidence:** Row J requires evaluating `a_LB_b < 0.85` after BS-8f and **before running Stage C**; failure emits `INCONCLUSIVE-BY-CALIBRATION` and halts. §4's complete Stage-C definition instead starts directly with the sealed BS-2f mask and measured lower bounds, and names only Stage-C FAIL → `INCONCLUSIVE-BY-POWER`. It never states the pre-Stage-C calibration admission branch or its failure effect. A mechanical V15→V16 comparison shows no change anywhere in §4, despite R15 Part 2 item 3 naming §4 and V16 §10 line 736 asserting that conforming edits were applied to §4.
   - **Why it fails:** §4 is the document's statistical Stage-C contract; Row J is the conduct/lifecycle contract. As applied, a reader can follow §4 directly into Stage C with a low `a_LB_b`, while Row J requires an earlier calibration halt. The same threshold therefore has the right value in Row J but an omitted phase and failure effect in §4—the exact whole-document defect this gate asks to detect. Clause 10 fails forward because the low-bound branch has two stated continuations, and §10 overstates the fold's repair state.
   - **Smallest sufficient repair:** Add the Row-J admission gate to §4 before the Stage-C definition: any bin `< 0.85` → immediate pre-unblinding `INCONCLUSIVE-BY-CALIBRATION`; only all bins `>= 0.85` may run Stage C. Then make §10's repair trace point to the actual applied text rather than claiming an edit that did not land.

3. **MEDIUM — the fold record conflates fold initiation with the final V16 byte state and therefore overstates its chronology.**

   - **Section and lines:** banner lines 3–22; fold record lines 581–586; §11 line 748.
   - **Evidence:** The banner says the R15 verdicts “landed during the fold” and records CODEX at 21:52:33 and GPT56 at 21:53:46. It also says the GPT56 blocker was closed “by this edit,” which is visibly present in §11 line 748. The fold record nevertheless says the artifact was folded “before R15 referee verdicts existed” and that the round “had not returned when the fold was performed.” Filesystem evidence is consistent with the reports' recorded times (`SECTION6_REVIEW_R15_CODEX.md` mtime 21:52:33 KST; GPT56 21:53:46 KST), while the reviewed V16 bytes have mtime 22:47:17 KST and necessarily contain the post-verdict blocker repair.
   - **Why it fails:** The principal's 21:48 instruction and an initial replacement action may both predate the verdicts, but the final pinned V16 bytes do not. The record currently uses “folded/performed” for both the initial operation and the later post-verdict revision. That is not an accurate custody chronology for the artifact now under review.
   - **Smallest sufficient repair:** Distinguish (a) fold instructed/initiated at 21:48 before verdicts, (b) verdicts landing during assembly, and (c) final V16 bytes written after applying the GPT56 schema-inventory repair. Do not describe the final pinned bytes as having been performed before the verdicts existed.

4. **MEDIUM — the document overclaims class-P completion immediately after saying BS-5p is unfillable.**

   - **Section and lines:** §2.6 lines 269–317, especially 277–289, 307–311, and 317; §7 line 636.
   - **Evidence:** Lines 277–289 and 307–311 repeatedly and correctly say the exact Stage-P route is not in the §0 code, BS-5p cannot be filled, and the measured harness is not definitional. Line 317 then says, without qualification, “These fill the class-P inputs that six gate rounds said could not be closed by writing alone.” §7 line 636 correctly says only one of fourteen class-P slots is filled, BS-2m.
   - **Why it fails:** The sentence makes the draft read more finished than its actual gate state. At minimum, Stage-P's measured result does not fill BS-5p; the document itself says so three times. This is precisely the overclaim check in the brief, and it sits adjacent to the disclosed blocker where a reader is most likely to infer closure.
   - **Smallest sufficient repair:** Replace line 317 with a narrow statement that these are measured candidate values/evidence only; they do not fill BS-5p or any other unreceipted class-P slot. Preserve §7's one-of-fourteen count.

5. **MEDIUM — the scalar/profile decision threshold is operational but absent from the prose threshold/branch contract.**

   - **Section and lines:** §0 lines 69–102; §3 lines 386–395; §5 lines 464–476; pinned `ref/successor_ref_v9.py` lines 1492–1496.
   - **Evidence:** §3 names a scalar path and a profile fallback, and §5 emits the path taken, but V16 never states the branch predicate. The pinned code defines it as `max_b |a_b - a_hat| <= 0.03` → `SCALAR`, otherwise `PROFILE`. A whole-document search finds no `0.03` or equivalent predicate in V16.
   - **Why it fails:** §0 says prose states thresholds, and Clause 10 applies to every branch in the document. The code pin prevents executable discretion today, so this is not the same severity as Findings 1–2; nevertheless the prose's named two-path contract and results field cannot be audited bidirectionally from V16 itself. A reader cannot derive which stated path is reachable from which calibration record without opening implementation bytes.
   - **Smallest sufficient repair:** State the `0.03` predicate, phase (after BS-8f, before any real statistic), equality side (scalar), and effect (profile selection, not run failure) in §3 or §5, tied explicitly to `adjudicate_path()`.

## Applied conforming-edit audit

- **§2.5 producer-checksum narrowing — HOLDS.** Lines 237–240 limit the producer checksum list to source-image transport at BS-6.
- **§2.7 exclusions — DOES NOT HOLD AS A WHOLE.** Reasons (a)–(b), deferral, and no post-attrition Stage-C rerun landed, but stale live reason-(d)/BS-3 language remains (Finding 1).
- **§4 Stage-C conformance — DOES NOT HOLD.** No V15→V16 edit landed in §4; the Row-J calibration phase/effect is absent (Finding 2).
- **§5 guard surface — HOLDS at document-contract level.** Lines 456–473 require canonical BS-L, one-use unblinding receipt, final-mask/ledger verification, and refusal before a statistic on an inconclusive adequacy result. Implementation remains unresolved.
- **§7 count and DESIGN inventory — HOLDS with an explicit artifact distinction.** I parsed 14 class-P slot rows. The class-E table contains seven `BS-*` slots plus the separately named unblinding-receipt artifact; “7 class-E slots” is therefore correct. BS-2a and BS-2k are the only DESIGN slots named in the inventory; BS-2f is value-only and is correctly in class E.
- **§10 repair trace — DOES NOT HOLD.** It claims an applied §4 conforming edit that the mechanical diff disproves and does not distinguish the later §11 blocker-closing edit.
- **§11 code-side inventory — PRESENT, NOT IMPLEMENTED.** The unblinding-receipt item now enumerates the required semantic field set and requires future schema bytes to be pinned and authenticated. This closes GPT56's inventory omission at document-contract level, not at byte/implementation level. The wording “exact ... including at minimum” should be resolved into a closed canonical schema when BS-L/unblinding implementation is delivered; current V16 honestly marks that work unresolved.

## Clause 10 — entire-document audit in both directions

### Forward: branch to exactly one outcome

- **Holds:** release A/B selection and date fallback; selection exact/production boundary; manifest pass/refusal checks; verdict p-value boundaries; Row-I allocated-output halt; Row-J trial-count, 962-success and self-verification partitions; Row-O one-use/replay partition; Row-P ordered record-state partition; zero-versus-any post-unblinding removal; disclosure after BS-V.
- **Fails:** the confidence-exclusion branch has two live threshold owners (§2.7 BS-3 versus §7 BS-2a), and the low-calibration branch has two document surfaces (§4 direct Stage-C entry versus Row-J pre-Stage-C halt). These are Findings 1–2.
- **Carried blocker, honestly disclosed:** Stage P remains dual-valued between the pinned shared-null code and the preferred exact-per-trial route. V16 explicitly blocks BS-5p rather than hiding this; it is not credited as resolved.

### Reverse: every stated outcome has a reachable witness

- `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, and numeric `INCONCLUSIVE` have closed p/sign/band/floor predicates, including equality in the residual region.
- Pre-lock `INCONCLUSIVE-BY-CALIBRATION` is witnessed by any `a_LB_b < 0.85`; `INCONCLUSIVE-BY-POWER` by fewer than 962 successes or either self-verification failure after protocol admission.
- Row-P missing/duplicate/orphan/malformed outcomes and absence/non-finite/confidence exclusions each have a corresponding ordered record state; any exclusion reaches post-unblinding `INCONCLUSIVE-BY-CALIBRATION`.
- `VOID` is witnessed by table-listed forbidden acts and protocol/digest deviation.
- The successful path is structurally named but presently unreachable in execution because BS-2a is refused, BS-6 is blocked, and the required code/schema work does not exist. That blockage is declared, not an orphan hidden by the document.
- The scalar/profile result paths have executable witnesses in the pinned code, but the `0.03` reverse mapping is absent from the prose (Finding 5).

## Threshold sweep — value, phase, failure effect

- **Calibration floor `0.85`:** source value and Row-J phase/effect are correct; §4 omits them (Finding 2). Equality is PASS.
- **Stage-C protocol `1,000`; success cut `962`:** correct values, P5/pre-BS-L phase, count deviation → VOID, clean `<962` → `INCONCLUSIVE-BY-POWER`, clean `>=962` → PASS.
- **Self-verification:** any `refuted` or `nonconservative` → pre-lock `INCONCLUSIVE-BY-POWER`; correct.
- **Post-unblinding attrition:** one or more removals → `INCONCLUSIVE-BY-CALIBRATION`; zero proceeds; correct and no Stage-C rerun.
- **Confidence threshold:** value/owner is not single-valued between live §2.7 and §7 text; post-unblinding effect is exclusion then calibration inconclusiveness (Finding 1).
- **Scalar/profile spread `0.03`:** value, phase and equality effect exist only in pinned code, not prose (Finding 5).
- **Production permutations `100,000`; reproduction p `<0.001`; rejection p `>0.05`; detection multiplier `3.09`; amplitude `0.0408`:** prose and pinned v9 agree, including strict/equality boundaries.
- **Planning thresholds:** retention `0.8572`, `N_eq >=100,000`, exact mode `<=16`, and margin `1.2` agree with pinned v9.
- **Catalog cuts and release date:** the stated values and branch effects are single-valued in V16.

## Fold-record verification

- R15 source SHA-256 recomputed as `d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a`: **MATCH**.
- Extracted V16 §6 through §6.3 is byte-identical to R15 Part 1: **MATCH** (both extracted bodies SHA-256 `7472acd61f0661f13102bdeb6c165f214777a716ade08f8a8b66f4a0b05d368f`).
- R15 report times match their file mtimes: CODEX 21:52:33 KST and GPT56 21:53:46 KST.
- The recorded R15 verdicts and their substantive dispositions match the report files.
- The GPT56 unblinding-schema omission is now listed in §11 and remains explicitly unimplemented.
- Fold chronology needs the initiation/final-byte distinction in Finding 3.

## Failed attacks

- I tried to reproduce the linter's claimed live class-P BS-2f assertion. It does not exist in the operative §7 table: BS-2f is class E and value-only. The occurrence in the fold record is explicitly a quotation of V15's stale state. The brief's false-positive explanation holds on independent inspection.
- I tried to recover the broad producer-checksum scope; §2.5 now limits it to source-image transport at BS-6.
- I tried to bypass BS-L/unblinding/final-mask adequacy through the live §5 prose; the new guard sentence closes that document-level route.
- I recomputed §7 counts and DESIGN classification; the seven `BS-*` class-E slots, fourteen class-P slots, BS-2a/BS-2k DESIGN inventory, and class-E BS-2f disposition hold.
- I tested the principal Row-J boundaries: `a_LB_b == 0.85` passes, 962/1,000 passes subject to self-verification, 961 fails, and a nonstandard trial count is a protocol deviation. V16 Row J and pinned v9 agree.
- I tried to turn post-unblinding attrition into a Stage-C rerun; §2.7, §5, Row J and Row P consistently forbid it.

## Testimony

- The 21:48 Duho instruction is stated in the edit brief and V16 banner; I found no independent timestamped instruction artifact in the reviewed directory. I therefore treat the authority/time itself as Testimony while independently verifying the later report times and current file state.
- Future `verify_lock()`, `verify_unblinding_receipt()`, canonical slot/unblinding schemas, Row-J guard, mediator, C2 worker, acceptance recomputation, replay verifier and negative fixtures do not exist in pinned v9. Their behavior is requirement/Testimony, not executed protection.
- BS-2a's three-seat refusal and Findings 1, 2, 2b and 3 are carried state assertions. I did not re-adjudicate the external BS-2a reports.
- The predecessor archive count, real-geometry counts, Stage-P measurements, source citation and historical authorization statements were not independently re-derived from prohibited data or network sources in this gate.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, inspect secrets, or touch χ-bearing material.

## Evidence ledger and custody

Content read:

- `BRIEF_V16_WHOLE_REVIEW.md`
- `../PREREG_SUCCESSOR_DRAFT_V16_20260827.md` in full
- `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` through whole-file mechanical comparison and targeted source passages
- `SECTION6_DRAFT_AGY_R15.md`
- `SECTION6_REVIEW_R15_CODEX.md`
- `SECTION6_REVIEW_R15_GPT56.md`
- `BRIEF_FOLD_V16.md`
- `BRIEF_V16_FOLD_BANNER.md`
- `BRIEF_V16_CLOSE_BLOCKER.md`
- `SECTION6_REVIEW_R12_GPT56.md`
- `SECTION6_REVIEW_R13_GPT56.md`
- `SECTION6_REVIEW_R13_CODEX.md`
- `SECTION6_REVIEW_R14_CODEX.md`
- `SECTION6_REVIEW_R14_GPT56.md`
- `../ref/successor_ref_v9.py` constants, Stage-C partition, calibration path and production-decision regions

Independent checks run:

- SHA-256 of V16 before opening; SHA-256 of V15, R15 §6, v9 reference code, closure worker and fixture transcript.
- Exact R15-Part-1 ↔ V16-§6 byte comparison.
- Whole-file V15→V16 opcode/diff audit; this found no §4 edit.
- Programmatic §7 class-P/class-E row counts and DESIGN classification inspection.
- Full Row-P extraction; whole-document branch/outcome and threshold-token sweep.
- Direct source checks of `N_TRIALS`, `CP_PASS_X`, `A_FLOOR`, retention, exact-mode, N_eq, decision thresholds, `adjudicate_path()`, Stage-C fail-closed returns, and production verdict logic.
- File timestamp/stat checks for R15 reports and V16 chronology.

No source, draft-under-review, code, gate, or data artifact was modified. The only write by this seat is this required report.

**NOT CLEAR**