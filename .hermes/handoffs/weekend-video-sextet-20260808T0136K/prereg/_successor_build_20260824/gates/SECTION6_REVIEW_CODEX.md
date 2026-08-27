# CODEX referee report — proposed replacement §6

## Findings

1. **BLOCKING — the scope definition both classifies execution receipts as χ-bearing and exempts all receipts, logs, and digests from χ-bearing status.**

   **Clause / row at issue.** §6.1 “Scope — what is χ-bearing,” lines 26–38. Lines 27–28 expressly include a per-object instrument “execution receipt” among χ-bearing outputs. Lines 36–37 then say without qualification that “Receipts, digests, logs and fixtures are not χ-bearing.” Row B writes per-object execution receipts; row C reads execution receipts; row K allows Hwao to read receipts.

   **Why it fails as a promise.** The two classifications cannot both govern the same execution receipt. Under the broader exemption, a process can place a real χ value, sign, per-object agreement, or an outcome-revealing digest into something called a receipt or log and move it onto the nominally χ-free surface. Under the earlier sentence, row C’s receipt reads are χ-bearing exceptions and must remain inside their exact surface. Which reading wins determines whether Hwao can receive outcome information before unblinding. This recreates an access carve-out through object naming rather than role naming.

   **Smallest sufficient repair.** Delete the categorical exemption. Define as non-χ-bearing only a closed list of authenticated receipt/log schemas whose fields and digested payloads are proven unable to encode or bind an outcome-bearing value. State that an unlisted receipt, an opaque digest of χ-bearing bytes, and any receipt whose schema permits outcome payloads are χ-bearing by default. Reconcile rows B, C, K, and the access-log schema to that definition.

2. **BLOCKING — the lifecycle’s “under which receipt” condition is self-dependent for the mandatory exceptions.**

   **Clause / rows at issue.** The table’s receipt column and clause 5’s statement that an exception is valid only “under its stated receipt.” Row C is under BS-2f although it produces the realised partition receipted by BS-2f; row E is under the label-set receipt although committee views precede completion of that label set; row G is under BS-8f although it computes the fields BS-8f records; row H is under BS-5f although it produces the Stage-C result; row L is under BS-L although it produces BS-L. Row B similarly names per-object measurement receipts that its own run emits.

   **Why it fails as a promise.** Read literally as a precondition, none of those actors may perform the access needed to create its receipt. Read instead as “receipted afterward,” the column does not state what pre-existing receipt authorizes the access, despite the table being the normative, executable lifecycle. The committee trace therefore still requires an operator to choose a meaning: it must view cutouts before its label-set receipt exists, but clause 5 says the view survives only if it occurs under that receipt. This is the same self-dependence defect the BS-L repair was intended to remove, distributed across the exception rows.

   **Smallest sufficient repair.** Split the column into two explicit columns: **pre-existing authorization / pinned identity** and **receipt emitted by this act**. For every row, name both. State that an act is permitted after the former exists and is made auditable by the latter; do not use “under” for both meanings. The hand-check path should read, in order, BS-8p authorization and allocation → individually logged views → labels written only through the pinned interface → completed label-set receipt co-signed by the committee → BS-8f aggregation.

3. **BLOCKING — the table omits the process that is supposed to make violations detectable, and it does not operationally cover the predecessor archive.**

   **Clause / rows at issue.** §6.1’s “two sealed stores” paragraph; rows I and N; clauses 2 and 4; BS-2k as described in §6.1 and Part 2. Clause 4 requires a logging wrapper over both new stores and the predecessor archive. The normative table has no row for the wrapper/log writer, the sealed-store service, or the key/unsealing service. Row N either forbids such a process from touching χ-bearing material or admits it only as an unnamed catch-all, contrary to clause 2’s pinned-identity rule. BS-2k provisions “both stores,” their keys and roster, while the predecessor archive is a third χ-bearing store governed “exactly” by the covenant but is not included in that provisioning description.

   **Why it fails as a promise.** The append-only log is the only detection mechanism in the draft. If its writer and mediation boundary are outside the closed table, strict compliance forbids the mechanism; if row N silently authorizes it, the supposedly complete automation set is neither enumerated nor symbol-pinned. The archive has the same gap prospectively: clause 4 promises every archive read is logged, but no row or BS-2k field binds its existing store identity, holders, access path, or wrapper. Calling the archive covered does not connect it to the mechanism that makes coverage detectable.

   **Smallest sufficient repair.** Add explicit lifecycle rows for the pinned store-access mediator/log writer and any key/unsealing service, with exact inputs, outputs, event schema, refusal behavior, and emitted checkpoint receipts. Extend BS-2k to bind all three stores, including the predecessor archive’s identity, existing holder roster, and enforceable logging boundary, or state that the archive is technically inaccessible throughout this run and receipt that state. Make BS-L bind a final log checkpoint that demonstrably extends the BS-2f checkpoint rather than merely naming another digest.

4. **BLOCKING — clause 3(d) incorrectly says §0’s code-precedence rule does not reach the missing lock guard and receipt machinery.**

   **Clause / external seam at issue.** §6.1 clause 3(b)–(e), especially line 115; current document §0 lines 40–73; current §5 lines 427–459; pinned `ref/successor_ref_v9.py` `SLOT_SCHEMA` and `run_production_verdict()`.

   **Why it fails as a promise.** §0 expressly makes run guards and digest serializations operational mechanisms defined by pinned code, with code winning over conflicting prose. BS-L’s schema, envelope verification, and the guard that blocks the only verdict path are exactly run-guard and digest-serialization mechanisms. The pinned v9 bytes have no BS-L or BS-2k schema, BS-2f has no access-log field, and `run_production_verdict()` requires BS-5f but not BS-L. Part 2 and R3 disclose the needed future revision, but clause 3(d)’s statement that §0 does not reach this section is false under §0’s subject-matter rule. Replacing §6 before the conforming code/text revision would leave the prose-defect/code-precedence failure live.

   **Smallest sufficient repair.** Strike the non-reach sentence. State that this replacement and all Part 2 seams are one atomic candidate revision and that no freeze or execution is conforming until the newly pinned and gated code implements BS-2k/BS-L/BS-2f schemas, authenticated-field consumption, and a BS-L guard on the only production verdict path. Then run `prereg_lint.py` on the integrated candidate and add an end-to-end refusal fixture for BS-5f → BS-L → unblinding → BS-7f/BS-V.

5. **MAJOR — rows E and F do not define one closed label path.**

   **Rows at issue.** Row E says the committee “writes labels into the committee sealed store only.” Row F then says the label-ingestion writer “reads the committee’s labels” and writes them into that same store. Both cite the same label-set receipt.

   **Why it fails as a promise.** If row E already writes the store, row F is redundant and its input location is undefined. If row F is the only writer, row E’s allowed write surface is false and the transient path from human entry to row F is unnamed. That ambiguity matters because raw labels are χ-bearing and the draft’s central promise is that every χ-bearing touch and transfer is visible in one table. It also leaves unclear which process emits the label-set receipt and exactly what the committee co-signs.

   **Smallest sufficient repair.** Make row E submit labels only through row F’s pinned sealed interface; make row F the sole storage writer; prohibit any intermediate persistence or export; and state that row F emits the completed label-set receipt over the sealed label-set digest, view-log range, allocation digest, and member co-signatures. Alternatively delete row F and identify row E’s interface as the sole pinned writer, but retain only one write path.

## Mechanical check

I ran `python3 tools/prereg_lint.py <current V15 draft> --gates <gates>` against the current document. It reported 20 §7 rows (14 class P, 6 class E) and no inconsistency. The script does not evaluate the proposed replacement plus Part 2 edits, receipt-information flow, table self-dependence, logging-process completeness, or §0’s reach, so that clean result does not resolve findings 1–5.

## Testimony

I did not inspect any image, χ value, sealed store, access log, key, credential, or `/Users/duhokim/NebulaMindData/`. I did not establish whether an enforceable wrapper for the predecessor archive or either proposed store exists outside the reviewed files. Finding 3 is that this draft does not enumerate and bind those mechanisms, not testimony that no external implementation exists.

**NOT CLEAR**