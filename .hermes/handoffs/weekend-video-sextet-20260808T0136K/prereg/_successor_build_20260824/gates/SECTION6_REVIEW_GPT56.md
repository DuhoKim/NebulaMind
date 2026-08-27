# §6 REFEREE REPORT — GPT56

## Verdict

The draft finally states a universal access ban and makes table-authorized acts survive the void rule. The hand-check path is visible in one table. It is nevertheless not yet a closed or executable covenant: two live clauses forbid required operations, the receipt boundary classifies the same object both ways, and neither the acceptance producer nor the signed lock has a complete executable contract.

## Numbered findings

### 1. BLOCKER — the disclosure clause still forbids the BS-8f export that Stage C requires

**Clause / row at issue.** The opening Disclosure clause (§6 lines 18–22) forbids every real-χ-derived “summary” outside the sealed stores before BS-L. The scope then calls the BS-8f aggregates a permitted surface (lines 32–38); row G writes them and row H reads them before BS-L (lines 66–67). Part 3 C5 expressly calls BS-8f “the only permitted pre-lock χ-derived export.”

**Why it fails as a promise.** The later definition does not amend the unqualified opening prohibition. BS-8f is derived from committee labels and corresponding instrument outputs, is a summary, and must pass from calibration computation to Stage C at P4–P5. An operator can obey the Disclosure clause only by withholding it; an operator can run row H only by making the export the Disclosure clause forbids. Thus the committee can produce labels, but its required calibration result cannot reach Stage C without a textual breach.

**Smallest sufficient repair.** In the Disclosure clause, exempt exactly the permitted aggregate surface defined in §6.1 (and no other derivative), or require G and H to execute inside one sealed computation and make only BS-5f leave. Use the same choice consistently in the scope, rows G/H, and C5.

### 2. BLOCKER — “a process not in the table may not run” forbids the machinery that creates and audits the covenant

**Clause / row at issue.** The table preamble forbids any person/process not in the table and any act outside a row’s surface (lines 54–56); clause 2 broadens that to “A process not in the table may not run before the lock” (lines 89–94). Yet no row authorizes the BS-2k store/key/wrapper provisioner, the logging wrapper that must append every touch, image fetch/transport before row A receives release bytes, or the receipt-envelope verifier required by clause 3(e). Row K authorizes Hwao only to read χ-free artifacts and write slot receipts, not to provision stores, keys, escrow, or the wrapper.

**Why it fails as a promise.** The covenant’s own sealed stores and mandatory log cannot be created or operated without acts outside the table. The literal rule therefore makes BS-2k impossible and prevents reaching P1. This is not merely a missing convenience process: the omitted wrapper is the mechanism on which detectability rests.

**Smallest sufficient repair.** Scope the closed-world default to **touches of χ-bearing objects** rather than to every pre-lock process. Then add explicit rows for every process that touches a sealed store or predecessor archive, including the logging wrapper and any custody/provisioning operation that can touch stored bytes. χ-free transport, gates, and receipt verification may remain outside only if the narrowed default says so.

### 3. BLOCKER — the scope classifies execution receipts as both χ-bearing and non-χ-bearing

**Clause / row at issue.** The χ-bearing definition includes every per-object instrument “execution receipt” (lines 26–30), but the same paragraph says “Receipts, digests, logs and fixtures are not χ-bearing” (lines 36–38). Row C reads execution receipts and frozen confidence values; row K is permitted to read receipts and digests on the premise that they are χ-free.

**Why it fails as a promise.** The contradiction decides who may see a per-object instrument artifact before BS-L. Under the first sentence it must stay under a table exception in the main store; under the second, Hwao and external gates may read it. A receipt carrying confidence, status, or another per-object field can therefore cross the boundary while each side cites a different live sentence. The default-forbidden rule is not closed while its object classification is two-valued.

**Smallest sufficient repair.** Define receipt classes by schema. A canonical exported receipt/digest may be declared non-bearing only if its authenticated envelope exposes no per-object χ, sign, amplitude, confidence, label, agreement, or outcome-recovering field. Keep measurement/evidence payloads χ-bearing in the main store; export only the explicitly named non-bearing envelope/digest. Apply that definition in rows C, K, and the gate-witness sentence.

### 4. BLOCKER — row C has no named pre-BS-2f producer, while the current document and code place its check on the post-unblinding verdict path

**Clause / row at issue.** Row C requires an acceptance-ledger recompute at P2–P3 that writes the realised partition before BS-2f, but identifies it only as `run_production_verdict`’s future mandatory pre-verdict validator. Clause 2 admits that row C has no pinned symbol yet. Current §2.7 lines 315–322 says `run_production_verdict()` or a validator it calls performs the recomputation; current §5 lines 429–433 places that runner on the verdict path. The pinned v9 code’s `run_production_verdict()` (lines 1591–1605) checks only receipt count, sealed-mask type, and BS-5f envelope/mask fields; it has no acceptance-ledger evidence argument or recompute call. Part 2 does not require the corresponding §2.7 producer/timing edit.

**Why it fails as a promise.** BS-2f must exist before calibration and Stage C, hence before unblinding and before the verdict runner. A validator reachable only as part of the post-unblinding verdict call cannot produce BS-2f. Conversely, running `run_production_verdict()` at P2–P3 violates row M and would require real signs. Naming BS-2a as a future pin does not settle which callable produces the realised partition or when it is invoked.

**Smallest sufficient repair.** Require a separately named, BS-2a-pinned callable (for example `recompute_acceptance_ledger`) that consumes the enumerated evidence and produces/refuses the BS-2f partition at P2–P3. Require `run_production_verdict()` to re-invoke that same callable against the sealed ledger and compare the resulting mask digest. Add those exact producer/timing changes to Part 2’s §2.7 and §5 seams.

### 5. BLOCKER — BS-L names a “signature” but does not define a signable or verifiable lock artifact

**Clause / row at issue.** Clause 3(b) puts “Duho’s lock signature” inside the BS-L receipt; row L says Duho writes the receipt; clause 3(e) calls `receipt()` authenticated and requires consumer verification. In pinned v9, `receipt()` (lines 208–224) hashes a canonical body/envelope, returns only hashes plus environment, and neither signs nor retains authenticated field values for a consumer. The proposed code revision lists schema and consumer-envelope verification, but does not define the bytes Duho signs, the signature algorithm/key identity, the verifier symbol, or the exact guard that rejects an invalid signature.

**Why it fails as a promise.** A signature cannot simply sign an envelope that already contains that signature without a declared detached-signature construction. A hash-only receipt can prove deterministic serialization, not Duho’s authorization. As written, two implementations can both claim conformity while signing different payloads—or emit an unsigned hash object called a signed lock. BS-L is therefore recordable as a label but not executable and verifiable as the lock the covenant promises.

**Smallest sufficient repair.** Define BS-L as a detached signed artifact: canonicalize all non-signature fields, state exactly which digest Duho signs, identify the signing key/algorithm and roster binding, include the detached signature and signer identity in the outer schema, and pin a verifier called by both unblinding and `run_production_verdict()`. Failure of schema, digest binding, signature verification, BS-5f PASS, freeze completeness, or final-log verification must refuse unblinding.

## Checks that held

1. The access finding is closed at the level of the central rule: clause 1 bans decrypt/query/render/summarise/inspect for every person and process, and table-authorized access is the only exception.
2. The hand-check human path is substantially present: row E limits views to the allocated sample, isolates members from other roles, logs every view, and writes a sealed label set; row G is the sole per-object-to-aggregate consumer. Finding 1 is the remaining break between that aggregate and Stage C.
3. The chronology BS-5f → BS-L → unblinding → BS-7f/BS-V is acyclic, and BS-L is no longer in the class-P set it certifies.
4. BS-V is consistently verdict-only in the proposed conforming edits.
5. The existing `prereg_lint.py` returned “no inconsistencies found” on V15, but it cannot evaluate this unattached replacement or the semantic contradictions above; its checks cover slot existence/class, lock naming, list numbering, and repair-citation presence.

## Testimony

The following draft assertions were not treated as independently established facts in this review: that the redesign was historically outcome-blind; that no predecessor-store access occurred before this covenant; that raw-store access cannot bypass the future wrapper; and that the future BS-2k custody design, committee interface, schemas, signer, or consumer verifier will be adequate once written. The draft itself correctly leaves the first three as retrospective or physical-boundary risks. No real data or sealed store was accessed in this review.

**NOT CLEAR**