# V59 whole-document referee — CODEX

## Verdict

**NOT CLEAR.** The dispatched subject matched the required SHA-256 before the first read. The V57 withdrawal does not actually remove the suspended eight-code vocabulary from the operative access-log contract; V59's new universal `receipt_strict()` binding cannot be satisfied by several receipt producers the document itself names; and the nine-field BS-3g schema does not bind the data or perturbations from which its quantities and invariance outcome are computed. The draft also misidentifies the corrected refusal-checker bytes and still disagrees with its live raise-site ledger.

## Findings

### F1 — HIGH — the suspended eight-code refusal set remains the operative access-log schema

**At issue:** §6.1 lines 577–585.

Line 577 still states without qualification that the access log's refusal-reason field "carries exactly one code from the closed set below and nothing else." Lines 579–580 then define the eight codes and the no-catch-all consequence as present rules. Line 581 says the derivation is withdrawn and the set suspended; line 582 says nothing may be read as carrying the no-catch-all decision forward. But line 584, after that withdrawal, again states that "Every refusal is therefore one of" the eight categories and that the set "is DERIVED" and must be regenerated/re-pinned when the table changes.

Those are opposite operative instructions, not merely history versus a replacement rule. Row B still must log every refusal, but there is no replacement refusal field schema while the old exact-eight schema remains stated as exact. An implementation can follow line 577 and enforce the suspended set, or follow lines 581–582 and refuse to treat that set/no-catch-all rule as in force. The missing/unreadable-cutout counterexample therefore still reaches the old unloggable-refusal/VOID branch under one equally literal reading. Suspension requires demoting the exact-eight/no-catch-all clauses themselves to explicitly non-normative history and making BS-2k unfillable until a replacement event schema is derived and gated.

### F2 — HIGH — the new universal strict-constructor binding is impossible for named non-slot receipt producers

**At issue:** §11 lines 982–986 against §6.1 Rows B, C, C2, H, O, P and Q (lines 601–617) and §11 lines 976–977.

V59 does not merely require every **slot-receipt** producer to avoid direct `v9.receipt()` calls. It says: "Every producer named in §6.1 and §7 must construct receipts through [receipt_strict()] and through nothing else," and says any producer that cannot be routed through it is a STOP. `receipt_strict()` is defined to refuse every name absent from pinned `SLOT_SCHEMA`.

Several §6.1 producers intentionally emit receipts/artifacts that are not slots in that schema: Row B's access-log chain/checkpoints, Row C's χ-bearing cutout-completion receipt, Row C2's evidence projections and stage-completion artifact, Row H's χ-bearing label-set receipt, Row O's unblinding receipt, Row P's post-unblinding adequacy receipt, and Row Q's archive seal-state receipt. Section 11 separately requires canonical schemas/verifiers for the unblinding and archive artifacts; it does not place all these producers in `SLOT_SCHEMA`. The four deliberately deferred slot entries do not cure these non-slot producers.

Therefore at least Rows C, H, O, P and Q cannot obey the new "through it and through nothing else" rule as written. This meets V59's own STOP condition and is the brief's named path back to the principal/unfreeze question. The repair must bind every producer of a `SLOT_SCHEMA` envelope to the strict constructor while separately pinning constructors/verifiers for non-slot receipts, and must prohibit direct `v9.receipt()` use at the actual slot-producing call sites. A universal producer rule is not a stronger version of that binding; it is an unsatisfiable one.

### F3 — HIGH — BS-3g's nine fields do not bind the inputs or perturbation set, so a clean receipt can certify the wrong run

**At issue:** §7 BS-3g line 765; §11 lines 987–1019; `ref/gain_gradient_estimator.py` lines 70–75; `ref/gain_gradient_kernel.py` lines 62–69.

The BS-3g row says the slot binds the statistic, sample, positional stratification, uncertainty, bound, acceptance rule and failure consequence. Its exact nine-field schema binds three code-file digests, a mapping identifier, three scalar numbers, an outcome token and a perturbation count. It binds no BS-2f/BS-8f receipt or mask digest, no `a_hat`/`cov_a`/`c_bar` input digest, no catalogue/input artifact digest, no counterfactual-runner digest, and no ordered perturbation manifest or its digest.

That omission is load-bearing. The actual estimator API is `estimate_gamma(a_hat, cov_a, c_bar)`: code identity does not identify those run-time inputs. The kernel loads catalogue files by path; its code digest does not identify the bytes used by a future runner. And `n_perturbations` proves only a count, not which perturbations were evaluated. A producer can evaluate a favourable subset of the allowed perturbations, report the same count, and emit `HELD`; or replay valid `gamma_hat`/`sigma_gamma` values computed from a different mask/calibration input. The proposed verifier's instruction to recompute "from the files on disk" repeats mutable-path lookup rather than authenticating the inputs of the emitted receipt.

This also defeats the claimed per-object-field proof indirectly: `mapping_id` has no pinned lexical/registry schema and names a mapping whose output is explicitly a counterfactual sign vector; line 1016's claim that no object identifier or per-object quantity could occupy it "without violating its stated type" is not established by the words "stable identifier." Exact field-set enforcement blocks an extra key, but it does not make an under-specified allowed key safe.

BS-3g needs authenticated input identities/digests, the counterfactual implementation digest, and an ordered complete perturbation manifest (or a digest resolving to pinned bytes), plus a closed typed mapping registry. Without them the verifier cannot establish that the reported invariance outcome belongs to the preregistered sample and complete perturbation set, so the `blocks BS-6` edge is still not receiptable.

### F4 — MEDIUM — the draft's corrected refusal-checker digest does not match the referenced file

**At issue:** §6.1 line 585; `tools/refusal_vocabulary_check.py` on disk.

Line 585 identifies `fd6d6d7e…` as the corrected tool digest. Independent hashing of the referenced repository file produced:

`c2ccebbcb4730944ce1ff15ca27984feef17b39529f89656c9432b2e83c80b4c  tools/refusal_vocabulary_check.py`

No lane-local file exists at the draft's relative `tools/` path; the referenced repository tool is the file that implements the documented R05 behavior. The actual tool does fail V59 with exactly R05 and its self-test passes, so the designed suspended-state behavior holds, but the byte-identity claim does not. Replace the asserted digest with the actual full digest or identify and pin the intended bytes unambiguously.

### F5 — MEDIUM — §5 and the live raise-site ledger still disagree on the numerical inventory

**At issue:** §5 line 524; `ref/RAISE_SITE_CLASSIFICATION.md` lines 9–16 and its table.

The live ledger summary is `CALLER 23 / INTEGRITY 60 / NUMERICAL 20 / NUMERICAL-PLANNING 3 / TYPED-OUTCOME 3 / WRAPPER 3 = 112`. Section 5 nevertheless states "The numerical class is 21" and then says it is 18 if three flagged checks move. The ledger's own line 16 is also stale: it says soft reclassifications drop numerical "from 22 to 18," while the table marks only two rows soft and starts from 20, which would produce 18.

This is not a harmless copied total after the draft says to consult the live ledger: the sentence immediately after that instruction asserts a conflicting current total, and the ledger contradicts its own table. The exception-to-outcome implementation inventory cannot be audited against three simultaneous baselines (21, 20, and 22). Regenerate every summary from the classified rows and leave `NUMERICAL-PLANNING`'s referred normative status untouched.

## Failed attacks / repairs that held

1. **Subject and frozen pins held.** Before reading the draft, SHA-256 was exactly `9257411511b39de6c32b8b5b52a2f4ad45dec287a9150332dadafdd6253c6105`. The pinned reference and worker recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` and `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
2. **The unknown-slot exploit reproduces, and known-slot extra-field refusal holds.** Pinned v9 has 18 schema entries and lacks BS-3g, BS-2a, BS-2k, BS-L and BS-2v. `receipt(slot, {'per_object_chi': b'+1'})` accepted all five. Adding that field to a conforming BS-6 field set raised `RuntimeError`; the both-directions check works for a slot actually present in `SLOT_SCHEMA`.
3. **The intended R05 state holds.** `tools/refusal_vocabulary_check.py V59` exited 1 with exactly R05, and `--self-test` reported seven controls, zero failures. I did not report R05 itself as a defect.
4. **Withdrawal from the raise ledger holds.** No table row is classified `UNREACHABLE-BY-CONSTRUCTION`; the draft's falsification clause routes a future wrongly promoted guard to `INCONCLUSIVE-BY-NUMERICAL-FAILURE` and corrects the record.
5. **The V43 same-run rerun deletion holds.** Remaining "rerun" language concerns future Stage-P/design work, historical explanation, or explicit no-rerun rules. No discretionary retry, attempt log, attempt cap or seed schedule for a terminated study run has returned.
6. **Row-L named-object breadth held within the assigned lens.** The freeze signature and opening authorization are the two exceptions; the BS-L detached signature is over the canonical lock digest and is not caught by "anything but" that digest. I did not re-derive the parked P7-only phase or canonical-body residue.
7. **VOID misconduct scope held.** Forbidden acts, protocol deviation and digest deviation remain phase `Any`; only numerical non-finite/degenerate antecedents are post-unblinding.
8. **Counts, trace, VOID name coverage and lint held at their stated scope.** `prereg_counts.py` returned 16 class P / 8 class E; `prereg_trace.py` returned 58 transitions / 0 problems; `void_registry.py` returned 54 antecedents and its six-control self-test passed; `prereg_lint.py` exited 0 with 96 legacy advisories and 0 blocking findings. Per the brief, the legacy advisories are not findings.
9. **The V42/KIMI correction is now honest.** V59 no longer claims KIMI-V11 F7 supports the dual-valued Stage-P statement; it says KIMI F13 argued the opposite and F7 is a v7-subject disclosure finding. Reading the KIMI report confirms that account.
10. **Class inventory held at 16/8.** I found no operative 15/8 assumption; the historical V36→V37 row correctly records the change.

## Evidence ledger and custody

Read in content: `BRIEF_V59_REVIEW.md` first; the exact V59 draft after its digest matched; `ref/RAISE_SITE_CLASSIFICATION.md`; the `SLOT_SCHEMA`/`receipt()` region of pinned `ref/successor_ref_v9.py`; `tools/refusal_vocabulary_check.py`; `ANSWER_RECEIPT_UNKNOWN_SLOT_AND_V9.md`; the BS-3g kernel, estimator and verifier; the gain-control design references needed to inspect the receipt inputs; and the V11 KIMI report. Executed: SHA-256 checks; unknown-slot and known-slot-extra receipt probes; refusal checker and self-test; class-count checker; trace checker; VOID checker/self-test; lint; and targeted searches for suspension, rerun, unreachable and producer-binding clauses. No draft, reference, checker, ledger or source file was modified. The only write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V59
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 577–585 | The suspended eight-code/no-catch-all set remains the operative access-log schema and is reasserted after its own withdrawal.
F2 | HIGH | REPAIR-REQUIRED | §11 lines 982–986; §6.1 Rows B/C/C2/H/O/P/Q | The universal receipt_strict binding cannot be satisfied by named producers of non-SLOT_SCHEMA receipts, triggering V59's own STOP condition.
F3 | HIGH | REPAIR-REQUIRED | §7 line 765; §11 lines 987–1019 | BS-3g binds neither its data inputs nor its perturbation manifest, so a valid-looking receipt can certify a different sample or favourable subset.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 line 585 | The asserted corrected refusal-checker digest fd6d6d7e… does not match the referenced file's c2ccebbc… SHA-256.
F5 | MEDIUM | REPAIR-REQUIRED | §5 line 524; raise ledger lines 9–16 | The draft says numerical 21 while the live table says 20, and the ledger's own soft-count sentence still starts from 22.
<!-- END FINDINGS-BLOCK -->