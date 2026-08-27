# §6 THIRD-PASS REFEREE REPORT — GPT56

## Verdict

The central access finding is closed at the normative level: §6.1 binds every person and process, makes the lifecycle table the sole pre-unblinding exception surface, and preserves a conforming table-authorized act from the void rule. The hand-check path can also operate without voiding the run. The replacement is nevertheless not executable end to end. Three claimed acceptances remain only names rather than receiptable mechanisms: the opening authorization still has no canonical body or one-use verifier contract; the continued access-log chain has no named later receipt for its purported final checkpoint; and the cutout-completion receipt is χ-bearing by the draft's own closed-world scope but has no lawful verification path into row D. The acceptance recompute also claims sign-blindness while reading receipts that the scope says carry signs and amplitudes. The archive checkpoints lack the transition rule the accepted finding required, and two outside-§6 seams remain absent from Part 2.

## Numbered findings

### 1. BLOCKER — the “canonical opening authorization” is still undefined and therefore not executable or replay-safe

**Clause / table row at issue.** Rows L and O (lines 104 and 107), clause 3(c)–(d) (lines 146–152), Part 2 item 6 (line 187), and Part 5 GPT56 item 4 (line 214).

**Why it fails as a promise.** The draft adds the adjective “canonical,” says row O verifies the authorization, and says replay voids the run. It never defines the canonical body, however: no field binds the BS-L digest, the identities of both stores, the declared destination, a one-use ceremony identifier, or the intended phase. It names no signature serialization, consumption record, replay-state store, or exact verifier behavior. Row O emits only an “unblinding log record,” and Part 2 asks for an “opening authorization verifier” without supplying the contract that verifier must implement. The same under-specified signatures identified in R2 therefore remain conforming implementations. Part 5’s statement that this finding was accepted is not a tested repair.

**Smallest sufficient repair.** Define the exact canonical opening-authorization body and serialization, binding at least BS-L’s digest, both store identities, the declared destination, a unique ceremony identifier, and phase P7; bind the signer to the BS-2k public key; name and pin a verifier that atomically refuses an already-consumed ceremony identifier; and carry the authorization, verification result, and consumption event in a named unblinding receipt/schema.

### 2. BLOCKER — the “genuinely final post-unblinding checkpoint” is not receipted in any named artifact

**Clause / table row at issue.** Row B (line 94), row O (line 107), clause 4 (line 155), and Part 5 CODEX item 3 (line 221).

**Why it fails as a promise.** Splitting the pre-unblinding lock checkpoint from later events correctly removes BS-L’s self-dependence. But the second half of the prescribed repair did not land. Row B says it emits a “final post-unblinding checkpoint,” and clause 4 says the chain continues to one; neither names the slot or artifact that carries and authenticates that checkpoint, its producer-of-record, its exact terminal event, or a verifier. Part 2 adds checkpoint fields only to BS-2f and BS-L (line 184), both pre-unblinding. The scope’s closed slot-receipt list likewise adds no later checkpoint slot. A mutable access-log head after unsealing is not a receipted final checkpoint, so BS-L → opening → unsealing is still not recordable end to end as promised.

**Smallest sufficient repair.** Name a later artifact—either a dedicated unblinding receipt or an explicit field in a suitably later slot—whose schema carries the terminal chain digest, the BS-L checkpoint it extends, and the exact last included event. Name its producer and verifier, add it to §7 and `SLOT_SCHEMA`, and make the verdict path require the authenticated receipt rather than an unbound “unblinding record.”

### 3. BLOCKER — the new cutout-completion receipt is χ-bearing by default, but row D has no lawful path to verify it

**Clause / table row at issue.** The closed scope rule (lines 43–60), rows C and D (lines 95–96), and Part 5 GPT56 item 6 / CODEX item 4 (lines 216 and 222).

**Why it fails as a promise.** Moving the cutout cross-check after production and making it row D’s authorization fixes the old BS-6 chronology. The new receipt is not in the exhaustive non-χ-bearing schema list, though, and it necessarily binds checksums or other identities of cutouts that the scope itself defines as χ-bearing. It is therefore χ-bearing by default and cannot be verified by an outside scheduler or receipt-envelope verifier. If it remains in the main store, row D’s exact read surface authorizes only cutouts, not the completion receipt; row B is only a conduit and is not assigned its verification. Merely placing the receipt in D’s “authorized by” column does not identify a lawful consumer. The accepted finding has been moved in time but not closed as an executable edge.

**Smallest sufficient repair.** Pin the cutout-completion schema and verifier at BS-9, state that the receipt remains in the main store, and add its authenticated in-store read/verification to row D’s exact surface (and to row E’s raw-evidence surface). Alternatively define a genuinely non-bearing completion attestation whose schema cannot carry or bind cutout payload bytes and add it explicitly to the closed list; do not export cutout digests while the current opaque-digest rule remains in force.

### 4. BLOCKER — row E cannot be sign-blind while reading the full execution receipts the scope says carry signs and amplitudes

**Clause / table row at issue.** Scope lines 33–36 and 55–60; rows D and E (lines 96–97); §2.7(3)–(5) in the current draft (current lines 311–336).

**Why it fails as a promise.** The scope expressly says every per-object execution receipt carries χ, sign, amplitude, and confidence. Row E then says it reads those execution receipts while “never” reading a sign or amplitude. Row B conveys sealed-store bytes “strictly as the conduit”; no pinned field projection or split receipt prevents E’s process from receiving the outcome fields. A code convention to ignore fields after reading the serialized receipt is not the sign-blind-by-construction boundary §2.7 requires, and row E’s void condition cannot make an already-visible field invisible. Because E controls the accepted partition after inference, this is outcome-adjacent access at exactly the selection point the acceptance design was created to close.

**Smallest sufficient repair.** Split D’s output into (a) a χ-bearing outcome object and (b) an authenticated acceptance-evidence record containing only the enumerated checksums/shapes, finite-output state, and frozen confidence quantity, with no sign or amplitude; make E read only (b). If a field-projection construction is chosen instead, pin the projection in BS-2a/BS-2k, have the mediator authenticate and return only the allowed fields without delivering the source bytes, and test that sign/amplitude fields are structurally unreachable by E.

### 5. BLOCKER — the archive seal-state checkpoints still have no expected transition/equality rule

**Clause / table row at issue.** Rows A and Q (lines 93 and 109), BS-L body clause 3(b) (lines 140–145), §6.2 (lines 163–166), Part 2 items 3 and 6 (lines 184 and 187), and Part 5 GPT56 item 2 (line 212).

**Why it fails as a promise.** The draft now names an actor and puts archive state into BS-2k, BS-2f, and the lock checkpoint, which repairs the prior absence of a producer and schema fields. It never states what relation must hold among the three states, what authenticated fields constitute “seal state,” or what exact condition makes the state “broken.” Three independently receipted arbitrary strings satisfy the current words. The prior finding’s required expected transition/equality rule was therefore omitted, while Part 5 declares the finding accepted. This does not cure the separately and honestly disclosed retrospective gap; it prevents even the prospective checkpoints from producing a determinate pass/fail.

**Smallest sufficient repair.** Define a canonical authenticated seal-state schema and stable archive identity; state the permitted transition relation from BS-2k → BS-2f → lock checkpoint (normally identity and intact-state equality, except for explicitly enumerated custody metadata transitions); require row Q and `verify_lock()` to fail on any mismatch, missing predecessor link, unrecognized transition, or unauthenticated state; and bind both earlier checkpoint digests into the later chain.

### 6. MAJOR — Part 2 leaves §7’s class-P count and DESIGN inventory false after the proposed slot migration

**Clause / table row at issue.** Part 2 items 1–2 (lines 182–183) versus current §7 lines 595–600.

**Why it fails as a promise.** The current table mechanically contains 20 rows: 14 class P and 6 class E. Applying the stated conforming edits—move BS-L from P to E and add BS-2k to P—produces 21 rows: 14 class P and 7 class E. Current §7 nevertheless says “One of twelve class-P slots is filled” and its “today’s count” of DESIGN slots omits both the already-labeled BS-2a and the proposed class-P DESIGN slot BS-2k. Part 2 does not instruct either sentence to change. This is not just typography: BS-L’s canonical freeze manifest promises every class-P receipt, so a contradictory declared count weakens the freeze-completeness check the new lock is supposed to make explicit.

**Smallest sufficient repair.** Add a Part 2 edit that regenerates §7’s class counts and DESIGN inventory from the actual rows after the move, explicitly includes BS-2a and BS-2k, and adds a lint assertion that the prose count equals the parsed table count.

### 7. MAJOR — Part 2 does not conform §5’s stated production guards to the new BS-L/unblinding requirements

**Clause / table row at issue.** Row P (line 108), clause 3(c)–(d) (lines 146–152), Part 2 items 4 and 6 (lines 185 and 187), versus current §5 lines 429–437 and 456–459.

**Why it fails as a promise.** Row P and clause 3 correctly require a verified BS-L and an unblinding record on the only verdict path. Current §5 defines that path by enumerating its guards and says it requires BS-5f bound to the mask before running; it names neither BS-L nor an authenticated unblinding receipt. Part 2 tells §5 to add the acceptance-ledger recompute, but does not tell it to add the new lock and unblinding guards. The code-side list mentions `verify_lock()`, yet an atomic candidate that applies Part 2 literally can still leave the document’s defining verdict section asserting the old guard surface.

**Smallest sufficient repair.** Add an explicit §5 conforming edit: `run_production_verdict()` must require and verify the canonical BS-L artifact, the one-use unblinding receipt, the exact accepted-mask binding, and the post-unblinding ledger recomputation before forming any statistic; name the corresponding new arguments/guards in §5 and in the pinned code revision.

## Checks that held

1. **Central access attack failed.** The table preamble and clauses 1–2 bind all people and processes before unblinding; there is no key-holder or powerful-role carve-out. Row R closes the remainder.
2. **Void-rule attack failed.** Clause 5 preserves an act performed inside a row’s exact surface after its authorization and with its emission. The mandatory committee view no longer voids the run.
3. **Committee-path attack failed.** Rows G → H → I now keep the χ-bearing label-set receipt in the committee store and expressly authorize I to read it there before emitting only BS-8f aggregates.
4. **Weak-mediation attack failed at the design level.** Clause 4 makes enforceable mediation a BS-2k fill condition and says inability to enforce it makes the slot unfillable. Whether that future boundary is real remains Testimony.
5. **BS-L self-dependence and freeze-binding attacks failed.** BS-L is class E, excludes itself from its preconditions, uses a detached signature, and binds the ordered class-P/gate/freeze manifest rather than re-resolving mutable filenames.
6. **Closed-world temporal-boundary attack failed.** The default is expressly pre-unblinding, and rows P and S name the verdict and disclosure paths afterward.
7. **Label-receipt-location attack failed.** The receipt is explicitly χ-bearing, remains in the committee store, and is in row I’s exact read surface.
8. **Old BS-6 timing attack failed.** Source-image checksums remain at BS-6; cutout completion is moved after production and before row D. Finding 3 concerns the new receipt’s custody/verification path, not its timing.
9. The current V15 lint ran clean and reported 20 rows (14 P, 6 E). It does not integrate this candidate or test any finding above. Independent row arithmetic gives the proposed table 21 rows (14 P, 7 E).
10. The live v9 reference hashes match §0’s pins. The existing symbols named by the draft (`calibration_bins`, `assign_bins`, `allocate_handcheck`, `accuracy_from_handcheck`, `stage_power`, `inject_signs`, `run_production_verdict`) exist; `recompute_acceptance_ledger` and `verify_lock` do not, consistent with the draft’s future-work disclosure.

## Testimony

Not independently verified: historical outcome-blindness of the redesign; any past or present archive access or seal state; enforceability of a future raw-store mediation boundary; committee members’ isolation or memory; existence, schemas, or behavior of the future mediator, cutout/instrument runners, committee interface, acceptance recompute, lock verifier, opening-authorization verifier, replay store, unsealing service, or integrated receipt code; and any future integrated lint or fixture result. I did not inspect any image, χ value, sealed-store payload, predecessor archive payload, key, credential, or `/Users/duhokim/NebulaMindData/`.

**NOT CLEAR**