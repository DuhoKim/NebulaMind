# CODEX referee report — proposed replacement §6, second pass

## Verdict

**NOT CLEAR.** The central access finding is closed: clause 1 bans access universally, the table is the sole exception surface, and clause 5 preserves conforming table-authorized acts. The revision also repairs the first draft's receipt-column, lock-schema, mediator, and committee-write-path defects. Five new lifecycle breaks remain, however. Two required artifacts have no closed producer/consumer path, the access-log checkpoint closes before events the table requires it to log, row C places a post-BS-6 artifact at BS-6, and the custody acceptance rule expressly permits a design in which a raw-store read is undetectable.

## Numbered findings

### 1. BLOCKING — the label-set receipt is χ-bearing under the scope rule, but its location and only permitted reader are absent from the table

**Clause / table row at issue.** §6.1 scope lines 47–61; rows G–I, especially row H; the hand-check trace lines 114–117. The closed non-χ-bearing list says an authenticated schema may not carry a digest of an outcome-bearing payload and expressly makes any opaque digest of χ-bearing bytes χ-bearing by default. The label-set receipt is not one of the listed `SLOT_SCHEMA` receipts and row H defines it “over the sealed label-set digest.” Row H simultaneously says it “emits nothing outside” the committee store. Row I is authorized by the completed label-set receipt but its touch surface names only the sealed labels and corresponding instrument outputs, not that χ-bearing receipt.

**Why it fails as a promise.** The repair correctly makes row H the sole label writer, but it leaves the receipt that closes the write in no lawful place. If row H exports the receipt, it exports a χ-bearing digest that the scope forbids. If it keeps the receipt in the committee store, row I must read and authenticate it there, but row I's exact surface does not authorize that read. Treating the digest as non-χ-bearing would reopen the object-naming carve-out repaired from round 1. The end-to-end committee trace therefore still cannot reach BS-8f under one reading of the table and scope.

**Smallest sufficient repair.** State that the label-set receipt is χ-bearing and remains in the committee sealed store; add that receipt to row H's in-store write and to row I's exact in-store read/verification surface. Keep its digest off every exported pre-lock receipt. If an external completion signal is needed, define a separate authenticated non-bearing attestation whose schema cannot carry or bind the label payload, and list that schema explicitly in the scope.

### 2. BLOCKING — the acceptance ledger has readers and component writers but no producer for the ledger record §2.7 requires

**Clause / table row at issue.** The sealed-store paragraph lines 63–73; rows C–E; current §2.7(4), lines 315–322; Part 2 item 4. Row C writes cutouts and checksum records. Row D writes instrument outputs and execution receipts. Row E begins by reading “the acceptance ledger's per-object evidence,” including terminal status/reason material it may refuse, and then writes the realised partition. No row creates or appends the acceptance ledger, joins the expected and actual checksums/shapes, writes the finite-output flags, or supplies the provisional terminal status and reason that row E is said to check.

**Why it fails as a promise.** BS-2f cannot be produced from an artifact that no authorized actor constructs. Allowing an unnamed process to assemble the ledger violates the table's closed-world rule; treating C or D as the implicit ledger writer exceeds both rows' stated write surfaces. This is outcome-adjacent custody, not clerical plumbing: whoever assembles statuses, reasons, joins, and missing-receipt evidence can move objects between accepted and excluded unless the construction is pinned and recomputed.

**Smallest sufficient repair.** Choose one closed construction. Prefer making the BS-2a-pinned `recompute_acceptance_ledger` consume the raw C/D records plus the independently fixed parent/attempt list, compute every status and reason itself, and atomically write both the append-only evidence ledger and realised partition; remove any dependence on operator-supplied statuses. Alternatively add a separately named, BS-2a-pinned ledger-ingestion row with exact append schema and make row E recompute from it. Conform §2.7 and the BS-2f producer text to the same choice.

### 3. BLOCKING — BS-L is called the access log's final checkpoint before required BS-L/unblinding events, creating both a chronology break and a lock-time self-dependence

**Clause / table row at issue.** Row B; rows L, N, and O; clause 3(b)–(c); clause 4. Row B operates “to the final checkpoint.” Clause 4 says the final checkpoint is receipted at BS-L. Yet row L requires the opening to be a logged event, row O requires every unsealing step to be logged after BS-L, and row N says the BS-L ceremony writes BS-L “and its log entries.” Clause 3(b) places the final running digest “at lock time” inside the body Duho signs.

**Why it fails as a promise.** If BS-L is truly the final checkpoint, row B has stopped before rows L/O generate the mandatory opening and unsealing events. If those events extend the chain, BS-L was not final and cannot prove the complete log. Row N adds a tighter cycle: a BS-L log event appended after the signed body changes the checkpoint the body calls final, while including that event before the artifact exists requires logging an event for an object not yet emitted. The sequence is therefore not recordable exactly as promised even though BS-L no longer certifies the class-P set containing itself.

**Smallest sufficient repair.** Split the concepts. Freeze a **pre-unblinding lock checkpoint** immediately before canonicalizing/signing BS-L; do not call it final and do not require it to include BS-L's own issuance event. Continue the same chain through BS-L issuance, opening, unsealing, BS-7f, and BS-V, and receipt a genuinely final post-unblinding checkpoint in a named later artifact. State which event closes each segment and make `verify_lock()` verify the BS-2f → lock-checkpoint extension without self-inclusion.

### 4. BLOCKING — row C says a post-BS-6 cutout artifact is cross-checked at BS-6

**Clause / table row at issue.** Row C; current §2.5 lines 206–211; the phase line. BS-6 authorizes the first image byte. Row C runs only after BS-6 and then produces per-cutout checksum records, but its emission says those records are “the §2.5 producer checksum list” and are “cross-checked at BS-6.” Current §2.5's producer checksum list is part of image transport under BS-6, before cutout production.

**Why it fails as a promise.** A receipt cannot cross-check records that do not exist yet. The row also conflates two different custody surfaces: the source-image producer checksum list available at transport approval and the per-cutout expected/actual checksums later consumed by acceptance. Under the literal table, conforming row C cannot emit the stated receipt; under an informal reading, an operator must choose which checksum list BS-6 and the acceptance ledger bind.

**Smallest sufficient repair.** Keep the source-image producer checksum list in BS-6. Give row C's per-cutout checksum/shape records a distinct schema and post-production checkpoint, append them to the acceptance evidence under finding 2's named producer, and bind/cross-check them at BS-2f (or another named post-C receipt), never at BS-6. Conform the scope's “producer checksum list” term so it names only the pre-image transport artifact.

### 5. BLOCKING — the text permits a BS-2k design in which the access violation that matters is undetectable

**Clause / table row at issue.** Clause 4 lines 202–215; row B; residual risks R1 and R7. Clause 4 first requires BS-2k to provision the stores so every access flows through row B, but then permits a technical boundary below which access outside the wrapper is physically possible and requires only that the risk be stated. R1 says a key holder with raw storage access can read without an event and “nothing shows it.” R7 expressly says a weak custody design honestly receipted at BS-2k satisfies the letter.

**Why it fails as a promise.** Requirement 7 is detectability, not disclosure of nondetection. A successful wrapper log plus an unlogged raw read is neither an absent log nor a gap in its chain; BS-L can verify every carried event while the prohibited access remains invisible. Because the draft says that a weak design still conforms, the table's “only path” claim is not an acceptance criterion on BS-2k. This leaves exactly the key-holder access event the covenant exists to prevent forbidden but undetectable.

**Smallest sufficient repair.** Make enforceable mediation a BS-2k gate condition, not a residual-risk disclosure: during the sealed phase, no holder or run host may possess a raw-store read path outside the pinned mediator; the gate must identify and test that boundary, and inability to enforce it makes BS-2k unfillable. State the unavoidable boundary precisely (for example, the named infrastructure administrator or hardware trust boundary), but do not let a design with an ordinary holder bypass satisfy the slot merely by naming the risk.

## Checks that held

1. Clause 1 closes the original access-versus-disclosure finding at the normative level: every person and process is bound, and no key-holder or powerful-role carve-out remains.
2. Clause 5 makes a within-surface, properly authorized table act non-voiding; the committee's mandated view is no longer prohibited merely because it is pre-lock access.
3. The authorization/emission column split removes the first draft's distributed self-precondition for C–J.
4. BS-L is class E in the proposed conforming edits, BS-V remains verdict-only, and the canonical detached-signature construction avoids putting the signature inside its own signed body.
5. Rows G and H now define one human-entry-to-storage path with row H as sole writer and no intermediate persistence. Finding 1 concerns the receipt after that write, not a revival of the prior dual-writer defect.
6. The acceptance recompute is now assigned a pre-BS-2f callable and the verdict path is required to re-invoke it; finding 2 concerns the still-unnamed construction of the evidence ledger it consumes.
7. The archive is not silently treated as mediated: §6.2 consistently chooses prospective seal-state checkpoints and says no row reads it.

## Mechanical check

I ran `python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py <current V15 draft> --gates <gates>`. It reported 20 §7 rows (14 class P, 6 class E) and “no inconsistencies found.” There is no integrated candidate containing Part 1 plus Part 2's conforming edits, so the required integrated lint cannot yet be run. The present linter does not test label-receipt information flow, ledger producers, log-checkpoint chronology, checksum timing, or enforceable mediation; its clean result does not resolve findings 1–5.

## Testimony

I did not inspect any image, χ value, sealed store, archive payload, key, credential, access log, or `/Users/duhokim/NebulaMindData/`. I did not establish whether a real mediator, raw-store exclusion boundary, committee interface, label-set receipt, ledger assembler, signer, or unsealing service exists outside the reviewed files. Assertions that the redesign was historically outcome-blind, that no predecessor access occurred, and that the future BS-2k design can make every access mediated remain unverified testimony. I reviewed `SECTION6_DRAFT_KIMI_R2.md`, the current V15 text, the two first-pass referee reports, the R2 drafting/review briefs, `tools/prereg_lint.py`, and the relevant `successor_ref_v9.py` schema/receipt/verdict-runner regions; I modified only this report.

**NOT CLEAR**