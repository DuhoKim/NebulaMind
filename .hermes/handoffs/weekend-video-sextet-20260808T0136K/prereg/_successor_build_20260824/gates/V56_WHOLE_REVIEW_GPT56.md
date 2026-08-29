# V56 whole-document review — GPT56

## Verdict

**NOT CLEAR.** The dispatched V56 bytes matched the required SHA-256 before the first draft read. The new refusal-vocabulary repair does not establish the closure it claims: its checker ignores the row-table surface from which the vocabulary is purportedly derived; the eight codes omit an expected refusal created by the draft's own missing-cutout path; and one of the eight codes violates the stated “never describe the object” principle. Separately, §5 still disagrees with the regenerated raise-site ledger, and the ledger misclassifies a supplied-argument guard under §5's own caller boundary.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §6.1 lines 581–582; `tools/refusal_vocabulary_check.py` lines 70–85

The derivation fingerprint does not bind the row surfaces on which the derivation expressly rests. Section 6.1 says the vocabulary stops being closed when the table gains or changes “a row, a surface or a precondition,” and says the checker fails when the table moves away from the pin. The checker instead hashes only row ID, phase, `authorized by`, and `what voids the run` (`keep = [cols[1]] + ... (4, 5, 7)`). It deliberately omits column 3, `may touch (read → write)`, which is the stated surface.

I mutated Row B's surface in memory from “the only path by which any row's stated read or write reaches any of the three sealed stores' bytes” to “DELIVERS EVERY SEALED OBJECT TO EVERY REQUESTER.” The original and mutated drafts both produced fingerprint `1d0b3e48ac5a435441662d3a9137fbf6b07e603e8b78205931fad386b72682bd`; `check(mutated_text)` returned no problems. Thus a surface can change maximally while the claimed derivation check stays green. The passing checker and its self-test do not support line 582's claim.

### F2 — HIGH / REPAIR-REQUIRED — §2.7 lines 342–355; §6.1 lines 577–581, Row B line 598, Row C2 line 600

The eight-code set is not closed over refusals the closed table itself requires. Consider Row C2 at P2, with BS-2a and the cutout-completion receipt verified, requesting through Row B the cutout for a parent identity that is inside the permitted set. If that target cutout is absent, corrupt, or unreadable, Row B cannot deliver bytes and must append a refusal event. This is not hypothetical residue: §2.7 expressly makes a missing or byte-integrity-failed cutout an ordinary pre-lock exclusion, and Row C2 exists to emit `parent_attempt_present` and `byte_integrity_pass` for exactly that path.

None of the eight codes applies: the requester and surface are authorized; preconditions and phase are satisfied; the lock state and one-use ceremony are irrelevant; the identity is in the permitted set; and this is a read, not a nonconforming write. The reason is the state of the target object, which the stated principle forbids the reason from describing. Therefore the table itself generates a legitimate refusal outside the set. With no catch-all, the refusal cannot be logged under the required schema and Row B's “refusal left unlogged” condition voids the run. The claim that an outside refusal necessarily means the table changed is false.

### F3 — MEDIUM / REPAIR-REQUIRED — §6.1 lines 578–579

The set fails its own principle even before a ninth code is proposed. Line 578 says a refusal reason may describe request and authorization state but “may never describe the OBJECT,” and claims none of the codes refers to an object. `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` does exactly that: combined with the separately logged object identity, it states a property of that object—non-membership in the permitted set. It therefore adds a per-object membership bit beyond the identity field. This is a code-shaped counterexample already inside the closed set, not merely a stylistic ninth-code proposal. Either the principle must be narrowed honestly (for example, to forbid outcome/object-content properties rather than every object property) or this code needs a derivation that does not contradict the test.

### F4 — MEDIUM / REPAIR-REQUIRED — §5 line 524; `ref/RAISE_SITE_CLASSIFICATION.md` lines 9–16

The current draft and regenerated ledger still disagree on the supposedly reconciled inventory. Section 5 states `CALLER 20 · INTEGRITY 61 · NUMERICAL 22 · ... = 112`, then immediately says “The numerical class is 21.” The referenced ledger actually has `CALLER 21`, `INTEGRITY 61`, `NUMERICAL 21`, and 3 each for NUMERICAL-PLANNING, TYPED-OUTCOME, and WRAPPER, totaling 112. I independently parsed all 112 table rows and reproduced those ledger counts, and independently counted 112 AST `Raise` nodes in the pinned source. The stale 20/22 partition remains an affirmative current-state claim and contradicts both the next sentence and the referenced artifact.

### F5 — MEDIUM / REPAIR-REQUIRED — §5 line 496; `ref/RAISE_SITE_CLASSIFICATION.md` lines 97–99; pinned reference lines 1199–1209

The caller-error boundary is applied wrongly to `inject_signs` line 1209. The function receives `a` as a supplied argument, expands it to `a_obj`, and raises when that supplied accuracy is non-finite or outside `(0.5, 1]`. The adjacent shape guard at line 1206 is correctly classified CALLER, but the range guard at line 1209 is classified NUMERICAL. Under §5's explicit test—“a caller error if it tests a property of an argument as supplied”—both are caller errors. In the preregistered paths, Stage P supplies the frozen 0.85 and Stage C is required to halt on a lower-bound failure before invocation, so an out-of-range `a` is not an admissible-data numerical outcome. This site also shows that the ledger's current 21/21 split is not validated merely because it sums to 112.

## Failed attacks / repairs that held

- Subject custody held before review: SHA-256 was exactly `c0743b40698e75b69451fd317adafae94d4f80d011b988dcb2e992496040d122`.
- The §0 pins held: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- Withdrawal completeness held: no draft or ledger site is currently classified `UNREACHABLE-BY-CONSTRUCTION`; the term remains only as the ruled status, its withdrawn history, and its falsification rule.
- Counts held at 16 class P / 8 class E; `prereg_counts.py` matched the prose.
- The revision trace held when invoked with the draft directory and `--check`: 55 computed transitions, 0 problems.
- The VOID registry self-test held: 54 antecedents, six controls, 0 failures; misconduct conditions remain `Any` while numerical non-finite/degenerate conditions remain post-unblinding.
- The lint exited 0 with exactly 96 legacy-citation advisories and 0 blocking findings. Per the brief, I did not report those advisories.
- The Stage-P citation repair held: V56 now cites GPT56-V11 F4 and CODEX-V11 4 and expressly removes KIMI rather than repeating the V42 miscitation.
- The V43 rerun deletion held: no discretionary study-run retry, seed schedule, attempt log, cap, verifier, or added rerun slot was revived; Row P still says “No discretionary retry.”
- BS-3g remains honestly DESIGN/UNFILLED and blocked on the preregistered gain-to-sign mapping. Its §11 schema/producer/verifier item is still only named, so the edge is not yet receiptable, but the draft does not falsely claim that it is.
- Row L's named-object exemption does not catch the BS-L detached signature: that signature is over the canonical lock digest. I did not re-report the expressly referred freeze-signature-definition or P7-phase residues.

## Evidence ledger and scope

Read in content: the V56 brief; the full V56 draft; `ref/RAISE_SITE_CLASSIFICATION.md`; the relevant `successor_ref_v9.py` functions; and `tools/refusal_vocabulary_check.py`. Executed: subject and §0 SHA-256 checks; independent AST/table raise counts; refusal checker and self-test; an in-memory Row-B-surface mutation; prereg counts; revision-trace check; VOID-registry self-test; and prereg lint. No draft, reference, tool, or other project file was modified. The only write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V56
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 581–582; tools/refusal_vocabulary_check.py lines 70–85 | The derivation checker ignores the row-table surface, so a maximal surface change leaves the pinned fingerprint and checker result unchanged.
F2 | HIGH | REPAIR-REQUIRED | §2.7 lines 342–355; §6.1 lines 577–581, Row B line 598, Row C2 line 600 | An authorized read of a permitted but missing or unreadable cutout requires a Row-B refusal that none of the eight closed codes can log.
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 578–579 | REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET violates the stated principle by encoding a property of the logged object identity.
F4 | MEDIUM | REPAIR-REQUIRED | §5 line 524; ref/RAISE_SITE_CLASSIFICATION.md lines 9–16 | The draft still states CALLER 20 / NUMERICAL 22 while the next sentence and live 112-row ledger say 21 / 21.
F5 | MEDIUM | REPAIR-REQUIRED | §5 line 496; raise ledger lines 97–99; pinned reference lines 1199–1209 | inject_signs' supplied-accuracy range guard is classified NUMERICAL even though §5's own boundary makes it a CALLER error.
<!-- END FINDINGS-BLOCK -->