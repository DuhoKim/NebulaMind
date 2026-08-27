# §6 SEVENTH-PASS (R7) REFEREE REPORT — GPT56

## Verdict

NOT CLEAR. R7 honestly leaves the BS-2a mechanism unresolved, preserves the previously credited protections, and makes a substantive repair to the reason-(c) path: Row I fails closed for an unusable allocated output, while Row P forbids silent inner-join loss and extends recomputation to absence, non-finiteness, and confidence removals. But the new prose does not yet close the gate contract it claims to close. The post-unblinding terminal states are described rather than defined, and no canonical post-unblinding artifact binds the final parent accounting, final mask, calibration-applicability result, and re-evaluated Stage-C result. More decisively, R7 says BS-5f may not certify a mask containing unusable rows, even though current V15 §4 defines BS-5f on the pre-attrition BS-2f mask and R7 deliberately permits that mask to contain such rows. If Row P removes one, current V15 §5 requires a BS-5f receipt bound to the exact verdict mask, but R7 neither produces a replacement receipt nor defines a distinct post-unblinding adequacy receipt/guard. Blocking findings: 1–2.

## Numbered findings

### 1. BLOCKER — Row P names terminal-state categories but does not define a gate-evaluable final-accounting contract

**Row / clause at issue.** Row P (R7 line 52); Part 2 item 3 (line 102); Part 5 item 5 (line 129).

**Why it fails.** The exact-parent join, precedence, no-silent-loss rule, and no-retry rule are real improvements. They tell a gate which conditions must be noticed and in what order. They do not define the promised “explicit deterministic terminal states”: there are no exact state names or enum, no canonical per-parent record, no rule rejecting duplicates/extras, no closure identity for the independently fixed attempt set, no producer/receipt for the post-unblinding partition, and no binding from that partition to the recomputed final-mask digest. “Under a pinned protocol” likewise does not identify the protocol, pinning slot/artifact, inputs, outputs, or verifier. A gate could determine that an accepted object is absent or non-finite, but it could not decide whether a purported final accounting and recomputation receipt conforms, because the bytes and closure rule to validate are absent.

This is not BS-2a work. It is the Row-P/post-unblinding contract that this pass was specifically authorized to repair. Deferring the C2 schemas is honest; deferring the final-state and recomputation schema while calling Defect 4 repaired is not sufficient.

**Smallest sufficient repair.** In Row P and the conforming §5 edit, enumerate the exact post-unblinding states (at minimum usable, absent, non-finite, confidence-excluded), define their precedence and one-row-per-parent set-equality closure against the immutable attempt set, and name a canonical authenticated post-unblinding adequacy artifact. That artifact must bind the parent-set digest, old BS-2f mask digest, complete terminal-state partition, final-mask digest, calibration-applicability decision, Stage-C inputs/result, protocol/code digest, and verifier result; missing, duplicate, extra, non-finite, or off-enum fields must refuse the verdict before any statistic.

### 2. BLOCKER — the BS-5f rule is temporally false and leaves the exact-mask receipt seam unresolved

**Row / clause at issue.** Row J (R7 line 46); Row P (line 52); Part 2 items 2–3 (lines 101–102); residual risk R3 (line 119); Part 5 item 5 (line 129); current V15 §4 lines 421–425 and §5 lines 429–434.

**Why it fails.** Current V15 §4 says Stage C/BS-5f runs before unblinding on the sealed BS-2f accepted-position mask. R7 intentionally permits that mask to include an object whose output will later be classified absent or non-finite. Therefore the categorical Row-J sentence “BS-5f may not certify a mask containing rows the verdict cannot use” is not the rule actually implemented by this route: BS-5f can and, in the motivating case, does certify the pre-attrition mask. Row P can only discover and repair the mismatch later.

The later recomputation does not repair the receipt seam as written. Current V15 §5 requires `run_production_verdict()` to hold a BS-5f receipt bound to the exact mask digest. Once Row P removes an object and computes a new final-mask digest, the locked BS-5f receipt is bound to the old mask. R7 says to recompute Stage-C power, but does not say that this creates any authenticated artifact, what slot/name it has, or how §5's exact-mask guard is changed. Issuing a new BS-5f after unblinding would also contradict BS-5f's defined pre-unblinding class-E role. Moreover, Part 5's claim that an unusable row cannot be certified “without triggering refusal” is false when the final-mask recomputation still passes the locked adequacy condition: Row P then proceeds rather than refuses.

**Smallest sufficient repair.** State the temporal truth: BS-5f certifies only the locked pre-attrition BS-2f mask and is insufficient for a changed final mask. On any post-unblinding removal, require a separately named post-unblinding adequacy receipt bound to the final-mask digest and the original BS-5f/BS-L digests; require §5's verdict guard to verify both receipts and exact final-mask binding; refuse before forming a statistic if calibration applicability or re-run Stage C fails. Do not call the later artifact BS-5f. Replace the false “may not certify” and “without triggering refusal” claims with this supersession/revalidation rule.

### 3. MINOR — Part 5 understates the already-credited reason-(c) refusal while honestly leaving the BS-2a mechanism unresolved

**Row / clause at issue.** Part 5 items 1–4 (R7 lines 125–128); Clause 2 and Row C2.

**Why it fails.** The disposition is not evasive for the actual BS-2a defects: byte-exact schemas, canonical serialization, independent verification, attestation, mediator transitions, and fixture oracles genuinely remain for a replacement BS-2a artifact, and R7 no longer presents a future-work list as a repair receipt. However, item 1 labels the “impossibility” itself UNRESOLVED even though both R6b referees already credited the specific future-execution-status repair: C2 no longer claims to report Row D completion/finiteness, reason (c) is refused pre-lock, and Rows C2/E remain blocked. What is unresolved is the replacement BS-2a integrity mechanism, not whether the impossible pre-inference execution-fact assignment was refused.

**Smallest sufficient repair.** Split the disposition: mark the impossible future-execution-status assignment **RESOLVED BY REFUSAL** (with the pipeline blocked), and separately mark the replacement BS-2a mechanism and its channel-closure requirements **UNRESOLVED**. This is an accuracy repair, not permission to execute.

## Checks that held / failed attacks

1. **Subject identity held.** The recomputed R7 sha256 is `ecccedde495a88377497057a4334c676f651f559fc0a7b2635a78dca8a990f30`, exactly matching the brief.
2. **Mechanical R6b→R7 scope held.** The normative clause bodies 1–9 are byte-equivalent after whitespace normalization; their average normalized length is unchanged. The table still contains exactly 20 unique rows: A, B, C, C2, D–S. Outside headings, disposition text, and the reconstitution of §6.2/§6.3, the normative table changes are confined to Rows I, J, and P.
3. **§6.2 reconstitution held.** Its normalized text is identical to R5.
4. **§6.3 reconstitution held.** The seven substantive bullets are identical to R5. The only normalized difference is removal of the R5 heading parenthetical “(carried unchanged),” which adds no rule.
5. **Universal-ban regression attack failed.** Clause 1 is unchanged from R6b and retains the substantive R5 access ban.
6. **Committee-path regression attack failed.** Rows G and H are unchanged. Row I retains G→H→I completion and adds a fail-closed condition; it does not create an alternate label path.
7. **Lock-chain regression attack failed.** Clause 3 and Rows N/O/P preserve BS-5f → BS-L → unblinding → BS-7f → BS-V and verified-lock refusal.
8. **Row-I leakage attack did not find a handedness disclosure in the prose.** A halt before BS-8f reveals only the aggregate fact that at least one allocated object lacked a usable finite output; it exports no sign, value, object identity, count, or direction. That completeness fact can be outcome-adjacent, but fail-closed handling is the safer trade than silently calibrating a changed subset. The alternative finite-subset calibration was not available under this pass without defining a sealed subset/reallocation mechanism—effectively the pre-lock supervisor route the principal ruled out.
9. **BS-2a candor held.** Clause 2, Row C2, Part 2, residual risk R1, and Part 5 all say BS-2a is REFUSED/UNFILLED, Rows C2/E cannot run, BS-6 is blocked, and the pipeline cannot reach the first image byte.

## Testimony

I did not inspect `/Users/duhokim/NebulaMindData/`, fetch any data, read any image/cutout/χ value, inspect a sealed-store payload, key, credential, live access log, runtime attestation, or committee record, or execute the scientific pipeline. I did not verify any future BS-2a or Row-P implementation. Claims about gate behavior are contract analysis of the named draft and current V15 text, not observations of a running mechanism.

## Evidence ledger

- Read `BRIEF_SECTION6_REVIEW_R7.md`, `SECTION6_DRAFT_AGY_R7.md`, `SECTION6_DRAFT_AGY_R6B.md`, `SECTION6_DRAFT_AGY_R5.md`, `SECTION6_REVIEW_R6B_GPT56.md`, and `SECTION6_REVIEW_R6B_CODEX.md`.
- Read current `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` §2.7, §4 Stage C, and §5 verdict/run-guard text.
- Recomputed sha256 for R7, R6b, and R5; mechanically diffed R6b→R7; enumerated the table rows; extracted and whitespace-normalized clauses 1–9 and R5/R7 §6.2–§6.3.
- No data fetch, data-directory read, image read, χ computation, sealed-store operation, preregistration edit, code mutation, or write other than this referee report occurred.

**NOT CLEAR**