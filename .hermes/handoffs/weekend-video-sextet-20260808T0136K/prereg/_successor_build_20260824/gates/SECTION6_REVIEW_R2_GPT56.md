# §6 SECOND-PASS REFEREE REPORT — GPT56

## Verdict

The central access finding is closed: the ban now binds every person and process, and an act inside a table row no longer voids the run. The committee path is also traceable through label ingestion and aggregation. The replacement is nevertheless not yet a closed, executable lifecycle covenant. Its claimed detection boundary expressly admits undetectable raw access; the archive checkpoints have neither schema fields nor a producer; BS-L does not bind the freeze whose completeness it claims to verify; the normative table accidentally continues its closed-world prohibition after unblinding; and two ceremony/production edges remain unreceiptable.

## Numbered findings

### 1. BLOCKER — the draft promises detectable access while expressly permitting a BS-2k design with an undetectable raw-access path

**Clause / row at issue.** Row B says it is “the only path” to either new store and clause 4 says BS-2k “must provision the stores so that every access flows through row B” (§6.1 lines 97, 202–215). But R1 concedes that “A key holder with raw storage access reads without an event and nothing shows it” (lines 465–469), and R7 says “A weak custody design honestly receipted at BS-2k satisfies the letter” (lines 504–508).

**Why it fails as a promise.** These are not merely physical-world caveats around an otherwise detectable violation. They authorize a class-P design whose declared architecture contains a pre-lock read path that emits no event, leaves the log chain complete, and therefore survives every BS-2f/BS-L checkpoint. The log proves completeness only over calls that voluntarily enter the wrapper. That does not satisfy the brief’s requirement that violation be detectable, and it contradicts the live “every access flows through row B” promise.

**Smallest sufficient repair.** Make BS-2k fail unless it demonstrates one of two closed constructions: (a) the χ-bearing bytes are cryptographically inaccessible except through the mediator until the receipted unsealing ceremony, with no holder possessing a usable raw-store key; or (b) every lower-level read path has an independent, immutable audit/seal mechanism whose checkpoint is bound into BS-L. Delete R7’s statement that a weak design can satisfy the text. If neither construction is available, narrow the claim honestly: the covenant forbids all access but detects only mediated access, and requirement 7 remains open rather than “Implemented.”

### 2. BLOCKER — the predecessor archive’s promised BS-2f and BS-L seal-state checkpoints have no receiptable path

**Clause / row at issue.** §6.2 requires the archive’s seal state to be “re-receipted at BS-2f and at BS-L” and makes a broken checkpoint a custody failure (lines 238–250). No table row performs either later seal-state inspection or names its producer. More decisively, clause 3(b)’s exact BS-L canonical body contains no archive identity or seal-state digest (lines 150–161), and Part 2 adds only the access-log checkpoint to BS-2f’s schema (lines 318–319). The proposed BS-L §7 row likewise says only “content per §6.1 clause 3(b)” (lines 310–312).

**Why it fails as a promise.** A producer cannot place the archive checkpoint into either exact slot schema without creating an extra field that the pinned `SLOT_SCHEMA` must reject. A conforming BS-L therefore cannot evidence the §6.2 checkpoint, while an artifact that does carry it cannot conform to clause 3(b)’s exact body. The archive is consequently declared operationally covered but is not covered by either promised receipt.

**Smallest sufficient repair.** Name the actor/process and non-content metadata operation that obtains each seal state; add the archive identity plus seal-state receipt/digest to the BS-2f schema, BS-L canonical body, §7 rows, and `verify_lock()` checks; and state the expected transition/equality rule between BS-2k, BS-2f, and BS-L. Alternatively remove the checkpoint claim and keep the archive explicitly outside this run’s detectable custody boundary.

### 3. BLOCKER — BS-L does not bind the freeze whose completeness it certifies

**Clause / row at issue.** Clause 3(a) makes “every class-P slot receipted — gates passed, Duho’s freeze signature” a BS-L precondition (lines 145–149), and `verify_lock()` is said to check freeze completeness (lines 164–175). Yet the exact signed body binds roster, BS-2f, BS-8f, BS-5f, decision inputs, access-log segment, environment, and signer identity only (lines 150–161). It does not contain the ordered class-P receipt manifest/digests, gate-report digests, or Duho’s freeze signature/digest.

**Why it fails as a promise.** `verify_lock()` can check the omitted items only by consulting mutable external paths at verification time. The detached signature then proves the listed execution digests but not that the freeze set was complete or that the gates and freeze signature being consulted later are the ones that authorized this run. BS-L avoids self-dependence, but it does not receipt the full predicate it claims to lock.

**Smallest sufficient repair.** Add to the canonical signed body an ordered manifest (or one canonical manifest digest) of every class-P slot receipt, the required gate reports, and Duho’s freeze signature, with slot identities and code/schema pins. Require `verify_lock()` to verify those bound bytes rather than re-resolving mutable filenames. The manifest must exclude BS-L by construction.

### 4. BLOCKER — the unblinding authorization is an undefined, replayable “opening signature”

**Clause / row at issue.** Row L says Duho “opens the lock by signature,” and row O is authorized by a passing `verify_lock()` plus “Duho’s opening signature” (lines 107, 110). Clause 3 defines the detached signature on BS-L in detail but nowhere defines a second opening statement, its canonical bytes, what lock/destination/ceremony it binds, its verifier, or its receipt schema. Row O emits only an unblinding log record.

**Why it fails as a promise.** A signature over an unspecified message is not an executable authorization. An implementation may reuse the BS-L signature, sign a bare word such as `OPEN`, or replay an opening from another lock or destination and still claim conformity. This leaves the BS-L → unblinding edge—the edge the brief specifically requires to be recordable—dependent on an unpinned convention.

**Smallest sufficient repair.** Define a canonical opening-authorization body binding at least the BS-L digest, both store identities, declared post-unblinding destination, one-use ceremony identifier, and intended phase; sign it with the BS-2k-bound key; pin and name the verifier; and carry the authorization plus verification result in the unblinding receipt. Row O must refuse replay, mismatch, or an already-consumed ceremony identifier.

### 5. MAJOR — the normative closed-world table has no post-unblinding/disclosure boundary

**Clause / row at issue.** The table preamble says **any** χ-bearing touch by a person/process not in the table, or outside a row’s surface, is forbidden by default (lines 81–87), without a pre-lock or pre-unblinding qualifier. Row Q says every other person/process may touch “nothing χ-bearing before unblinding” but supplies no post-unblinding window or authorization (line 112). Clause 1 is pre-unblinding, while the phase line and Disclosure clause require P8 verdict production and P9 disclosure (lines 27–31, 75–80). Only rows O and P name post-unblinding χ access; no row authorizes the disclosure actor or publication process.

**Why it fails as a promise.** Because the table is expressly normative, its broader unqualified default survives the narrower temporal language in clause 1 and row Q. After BS-V, a person or publication process touching the real result is still outside every stated row surface. The document therefore promises disclosure at P9 while its normative object forbids the touches needed to perform it.

**Smallest sufficient repair.** Either scope the table’s closed-world default explicitly to pre-unblinding χ-bearing touches and state the separate post-unblinding/BS-V disclosure rule, or add complete post-unblinding analysis and disclosure rows with actors, surfaces, receipts, and windows. Do not rely on row Q’s implication; give it an explicit post-unblinding rule.

### 6. MAJOR — cutout completion is “cross-checked at BS-6” before the cutouts exist, leaving row D’s start condition unreceipted

**Clause / row at issue.** The phase line places BS-6 at P1 before cutout production and inference at P2 (lines 75–79). Row C runs after BS-6, produces the per-cutout checksum records, and says they are “cross-checked at BS-6” (line 98). Row D may start only after “row C’s complete cutouts,” but names no emitted completion receipt as authorization (line 99). Current §2.5 likewise makes BS-6 the approval under which the first image bytes are fetched, so BS-6 cannot already attest to the later producer outputs.

**Why it fails as a promise.** A receipt that precedes the first image byte cannot cross-check checksums of cutouts produced afterward. Without a later completion/checkpoint artifact, “row C’s complete cutouts” is an operator assertion, not a receiptable precondition, and D can begin against a partial store while every named slot still exists.

**Smallest sufficient repair.** Keep BS-6 as transport authorization only. Name a post-production cutout-completion receipt (or a precisely identified field/checkpoint in an existing execution receipt) that closes the parent/manifest/checksum accounting after row C; make that receipt an explicit row-D authorization; and move the checksum cross-check to that point.

## Checks that held

1. **Access attack failed.** Clause 1 bans decrypt/query/render/summarise/inspect universally; it has no role-scoped holder exception. Table-authorized touches are the only exceptions.
2. **Void-rule attack failed.** Clause 5 expressly preserves an act performed inside a row’s surface after its authorization and with its required emission. The committee’s mandated views do not void the run.
3. **Committee-path attack failed.** Rows G → H → I give the allocated views, sole ingestion writer, sealed label-set receipt with member co-signatures, and per-bin reducer. No second label persistence path is stated.
4. **BS-L self-dependence attack failed.** BS-L is class E, its precondition set is the class-P set plus BS-5f, and the signed body is detached rather than self-containing. BS-V remains verdict-only.
5. **Acceptance-timing attack failed.** Row E now names a separately pinned `recompute_acceptance_ledger` at P2–P3, and Part 2 requires §2.7 and §5 to use the same callable before BS-2f and again after unblinding.
6. **Receipt-class contradiction from R1 failed.** Per-object execution receipts remain χ-bearing; exported slot receipts are schema-closed; opaque digests of χ-bearing payloads are χ-bearing by default.
7. The existing lint was run on the current V15 text and returned 20 slot rows (14 class P, 6 class E) and “no inconsistencies found.” It cannot lint this unattached replacement or the semantic defects above; the draft correctly does not claim an integrated lint pass.

## Testimony

Not independently verified: historical outcome-blindness of the redesign; the predecessor archive’s past or present seal state; absence of raw-store access; adequacy of any future BS-2k key/escrow/mediator design; existence or behavior of future symbols (`recompute_acceptance_ledger`, `verify_lock()`, mediator, unsealing service, committee interface/reducer, BS-9 runners); and any future integrated code/lint/fixture result. No real data, archive contents, sealed store, or secret material was accessed.

**NOT CLEAR**