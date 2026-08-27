# §6 DRAFT — AGY SEAT, FIFTH PASS (R5), 2026-08-27

Status: DRAFT FOR REFEREE. Written under `BRIEF_DRAFT_SECTION6_R5.md`, revising
`SECTION6_DRAFT_AGY_R4.md` against the two fourth-pass referee reports —
`SECTION6_REVIEW_R4_GPT56.md` and `SECTION6_REVIEW_R4_CODEX.md`.
This file modifies nothing; `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` is untouched. Part 1
is the complete replacement §6, written to drop in. Part 2 lists the conforming edits
outside §6 that dropping it in requires. Part 3 states every choice the findings did not
force, with its alternative. Part 4 names the residual risks this draft itself carries, including the explicit diagnosis of our prior failure modes.
Part 5 maps the brief's six findings to REPAIR or REFUSE.

---

# PART 1 — THE REPLACEMENT §6

## §6 Conduct

- **Disclosure.** Nothing derived from any real χ value — value, sign, summary, label, or
  count of signs — is published, spoken, or written outside the sealed stores defined in
  §6.1 before the primary lock, **with exactly one exception: the permitted aggregate
  surface defined in §6.1's scope paragraph, which leaves the sealed stores only as the
  BS-2f, BS-8f, and BS-5f receipts, on the paths the table names, and is the only pre-lock
  χ-derived export this text allows.** After unblinding, disclosure waits for BS-V (§7).
  The predecessor's §4/condition-2 breach is why this clause exists. What binds *access* is
  §6.1, and §6.1 is the normative object of this section.

### §6.1 The blinding covenant — one lifecycle table, and the table is normative

**Scope — what is χ-bearing.** A *χ-bearing object* is: any cutout produced for this run;
any per-object instrument output — a χ value, sign, amplitude, confidence value, **and
every per-object execution measurement receipt, which carries those fields**; any per-object hand-check
label or per-object human–instrument agreement; any derivative of these that is not on the
permitted aggregate surface below; and **the predecessor's sealed archive of 208,405 χ
measurements** (§6.2) — outcome knowledge on overlapping sky, governed by §6.2's seal-state
rule and enforceable mediation. The *permitted aggregate surface* — χ-derived but defined as not χ-bearing — is
exactly: the BS-2f mask fields (brickid, objid, position, acceptance flag, calibration-bin
label, boundaries, digests — never a χ sign), the BS-8f aggregate record (â, σ_a, a_LB,
the per-bin {â_b, σ_ab, a_LB_b}, ε̂, and the full Cov_a — aggregates over the hand-check
sample, never a per-object value), and **the BS-5f Stage-C receipt (PASS/FAIL and the permitted Stage-C scalar output, never a per-object calibration label)**. 

**Non-χ-bearing receipt and log classes — a closed list, defined by schema, and the list is exhaustive.** 
An artifact is non-χ-bearing only if it conforms to one of these authenticated schemas, none of which can carry a per-object
outcome value or a digest of a payload containing one: 
(i) a slot receipt under the pinned `SLOT_SCHEMA` as conformed by this revision's code items — namely
BS-1, BS-1b, BS-2a, BS-2c, BS-2k, BS-2m, BS-2o, BS-3, BS-4, BS-5p, BS-2s, BS-6, BS-7p,
BS-8p, BS-9, BS-2f, BS-8f, BS-5f, and BS-L (BS-7f and BS-V are explicitly post-unblinding χ-bearing receipts and are removed from this list); 
(ii) the access log under its BS-2k event schema (timestamp, actor, table
row, operation, object identity, success/refusal, refusal reason, running chain digest —
identities and flags, never payload bytes); 
(iii) the producer checksum list (§2.5), exclusively for source images; 
(iv) fixtures and their transcripts, synthetic by construction; 
(v) the authenticated **acceptance-evidence projection** containing only attempt identity, expected/actual checksum, shape, and execution completion/non-finite status. **Confidence is explicitly excluded from this projection and deferred to post-unblinding.**

**Everything else is χ-bearing by default**: any artifact not on this list and not on the permitted surface; every
per-object execution measurement receipt wherever it sits; the cutout-completion receipt; **any opaque digest of χ-bearing bytes** — a
digest whose preimage's schema is not on this list or the permitted surface, the acceptance
ledger's measurement digest among them, because such a digest is a verification oracle for a guessed
outcome; **the label-set receipt**, which is χ-bearing and remains in the committee store; **BS-7f and BS-V receipts**;
and any schema that permits outcome payloads. Doubt resolves toward χ-bearing.

**The sealed stores.** The *main sealed store* holds cutouts, instrument outputs, the cutout-completion receipt, and the
acceptance ledger. The *committee sealed store* holds the hand-check labels and the label-set receipt. A third
χ-bearing store — the predecessor archive — is governed by §6.2's seal-state rule and Row B's enforceable mediation. All three stores are provisioned at
**BS-2k** (custody design: the three store identities, key generation/split/escrow, Duho's
signing public key, the key-holder roster, the mediator symbol and its access-log event
schema, the unsealing construction, and the archive's identity, existing holder roster and
receipted seal state) — a class-P DESIGN slot, so all stores, all keys, the roster, the
mediator and the archive's receipted seal state exist before the freeze, hence before any
image byte. Gates and referees are external witnesses: their inputs are the closed list of
non-χ-bearing receipt classes and fixtures only, and no gate input is χ-bearing.

**The phase line.** P0 freeze (BS-2k and every other class-P slot receipted, gates passed,
Duho's freeze signature) → P1 BS-6, first image byte → P2 cutout production, integrity projection, and instrument
inference → P3 BS-2f → P4 BS-8f → P5 BS-5f → P6 BS-L, **the primary lock** → P7 unblinding
→ P8 BS-7f and BS-V → P9 disclosure. BS-5f blocks BS-L; BS-L blocks unblinding; BS-V follows
unblinding and is the verdict receipt, never the lock.

**THE TABLE.** Each row is one permitted actor or process. **Any pre-unblinding touch of a χ-bearing
object by any person or process not in this table, or outside a row's stated surface, is
forbidden by default** — that is what makes completeness checkable by reading one column.
Processes that never touch a χ-bearing object — release-image transport under BS-6, gates
and referees reading the closed receipt classes, receipt-envelope verification, scheduling
— are outside this default precisely because the default governs χ-bearing touches and
nothing else; this sentence is what says so. Two receipt columns are named separately
because they are two different things: an act is permitted once its **authorized by**
condition exists, and it is made auditable by the **emission** it produces. No row's
authorization is its own emission. Post-unblinding, rows P and S govern the verdict and disclosure paths.

| # | actor / process — identity | may touch (read → write) | when | authorized by (must exist first) | emits (receipt this act produces) | what voids the run |
|---|---|---|---|---|---|---|
| A | **Custody provisioner** — producer: Hwao builds, Duho designates the holders; the BS-2k custody design and the tooling it names | creates the two new stores' containers and brings the predecessor archive under the mediator; generates, splits and escrows the keys; generates Duho's signing keypair and binds its public half; installs the mediator (row B); records the predecessor archive's identity, its existing holder roster and its seal state by non-content metadata operation → writes the BS-2k design artifacts. **Never reads a χ value**: none exists yet for this run, and the archive's contents it never opens — it records seal state, not contents | P0, before the freeze, hence before any image byte | — (a freeze prerequisite; no slot precedes it) | BS-2k | any read of archive contents; any key share retained outside the escrow the design declares; any store, key or wrapper existing outside the receipt; failure to enforce mediation as a gate condition |
| B | **Store mediator / log writer** — the logging wrapper whose symbol and digest BS-2k pins (future work; may not mediate before that pin exists) | the only path by which any row's stated read or write reaches **any of the three** sealed stores' bytes; conveys bytes strictly as the conduit of another row's stated surface → appends exactly one event per touch, success or refusal, under the BS-2k event schema. A request that matches no extant row's actor, surface and window is refused, and the refusal is logged | from BS-2k's completion through unblinding | BS-2k | the access-log chain; its running checkpoint digest receipted at BS-2f, the pre-unblinding lock checkpoint receipted at BS-L, and the final post-unblinding checkpoint (carried in the unblinding receipt) | any byte delivered outside the requesting row's stated surface; any unlogged touch; any retained copy; a refusal left unlogged |
| C | **Cutout producer** — the BS-9 production runner; symbol and digest pinned at BS-9 | reads release image bytes → writes cutouts into the main sealed store, via row B; never reads any sealed object | P1–P2, after BS-6 | BS-6 (transport approval) and BS-9 (runner pin) | **the χ-bearing cutout-completion receipt, appended to the main store** | any cutout or derivative outside the store; any human view of a cutout outside row G's interface |
| C2 | **Cutout integrity verifier** — `verify_cutout_integrity` symbol and digest pinned at BS-2a | reads **only** cutouts via row B and fixed parent lists. Computes and writes the separate authenticated **acceptance-evidence projection** containing only attempt identity, expected/actual checksum, shape, and execution completion/non-finite status. **Never invokes the classifier** and has no access to instrument output. | P2, after row C, before row D | BS-2a (design), the cutout-completion receipt | the acceptance-evidence projections, one per parent object, in the store | executing the classifier; emitting any field outside the schema |
| D | **Instrument runner** — the BS-9 gated runner executing BS-3's pinned instrument identity | reads cutouts and the cutout-completion receipt (authenticating it against the pinned verifier) → writes per-object χ-bearing measurement receipts (χ, sign, amplitude, confidence) into the store only | P2, after row C2, before BS-2f | BS-3 (instrument identity), BS-9 (runner pin), and the cutout-completion receipt | the per-object measurement receipts in the store | any χ-derived value emitted outside the store |
| E | **Acceptance-ledger recompute** — the callable `recompute_acceptance_ledger` whose symbol and digest BS-2a's receipt must pin | reads **only the separate authenticated acceptance-evidence projections** in the main store (expected/actual cutout checksums, shapes, statuses) and fixed parent lists — and **computes the structural §2.7(2) predicates from it**. Does not read the cutout-completion receipt. → atomically writes both the append-only evidence ledger and the realised partition | P2–P3, after complete inference, before BS-2f | BS-2a (the frozen acceptance design), and exactly one verified acceptance-evidence projection per parent object | the realised-partition record, bound by BS-2f | reading any field outside the evidence schema; allowing operator-supplied statuses |
| F | **Calibration-bin sealing** — `calibration_bins()`, `assign_bins()`, `allocate_handcheck()` (pinned symbols) | reads the accepted partition's positions and acceptance flags only (χ-free) → writes sealed boundaries, bin labels, and the hand-check allocation | allocation plan pinned pre-freeze at BS-8p; boundaries sealed and labels assigned at P3, with the partition, at BS-2f | BS-8p (plan) and the realised partition | the sealed boundary and allocation record, bound by BS-2f | any χ-bearing input to bin construction |
| G | **Hand-check committee** — members named at BS-8p; **no member holds any other role in this study**, and no member fills, adjudicates or locks any slot other than co-signing the label-set receipt | views χ-bearing cutouts **of the allocated sample only**, rendered through the BS-8p sealed interface's view half (symbol pinned at BS-8p) → each label leaves the member only through that same interface to row H; a member's hands never write the committee store, and **no intermediate persistence or export exists between entry and row H's write** | after BS-8p and after the sample's cutouts exist; complete before BS-8f | BS-8p (the declaration), the sealed allocation, and the sample's cutouts existing | the member co-signatures carried by the label-set receipt | a member holding any other role; any label, tally, description or impression exported by a member outside the sealed interface; any view of an object outside the allocated sample; any unlogged view; any label path other than entry → row H |
| H | **Label-ingestion writer — the committee store's only writer** — the BS-8p sealed interface's ingestion half (symbol and digest pinned at BS-8p) | receives labels from row G through the interface → writes them, as one label set, into the committee sealed store, and writes the **χ-bearing label-set receipt** into the committee sealed store; emits nothing outside it | with row G, completing before BS-8f | BS-8p | **the χ-bearing label-set receipt, over the sealed label-set digest, the view-log range, the allocation digest, and the member co-signatures, which stays in the store** | any write path outside the pinned interface; any intermediate persistence between entry and write; any field beyond the pinned label schema; exporting the receipt's digest |
| I | **Calibration computation** — the BS-8p-pinned per-bin reducer feeding `accuracy_from_handcheck()` | reads the sealed label set, the corresponding instrument outputs, AND the **χ-bearing label-set receipt**, inside the stores → writes **only** the BS-8f aggregate fields (the permitted aggregate surface) | P4, after the label-set receipt, before BS-8f | the completed label-set receipt in the store | BS-8f | any per-object label, sign or agreement leaving the stores; any field beyond the BS-8f schema |
| J | **Stage-C runner** — `stage_power` with `inject_signs` (pinned symbols) | reads the sealed BS-2f mask (χ-free) and the BS-8f aggregates; injects synthetic signs only — **never reads a real χ** → writes the Stage-C receipt | P5, after BS-2f and BS-8f, before BS-L | BS-2f and BS-8f | BS-5f | reading any real χ; continuing the run after a Stage-C FAIL |
| K | **Key holders** — roster designated at BS-2k before the freeze; roster digest bound into BS-L | touch nothing before the lock; custody exists for the lock ceremony and later audit only — **holding a key is custody, never licence** | — | BS-2k (designation) | none (the roster digest is bound by BS-L) | any **pre-unblinding** read by any holder, authorised or not |
| L | **Duho** | signs the freeze; designates holders at BS-2k; signs BS-L's canonical lock digest (clause 3(b)) reading its digest fields only; creates the **canonical opening authorization** (clause 6); opens the lock by signature after BS-L exists and verifies, the opening a logged event | P0, P6, P7 | for the freeze: every class-P slot receipted and the gates passed; for BS-L: clause 3(a)'s preconditions | the freeze signature; the BS-L detached signature; the opening authorization | any **pre-unblinding** access to a χ-bearing object; opening the lock before a verified BS-L exists; signing anything but the canonical lock digest |
| M | **Hwao** — producer of record for the slots | reads the closed list of non-χ-bearing receipt classes (scope) → writes the slot receipts §7 assigns | throughout | §7's producer-of-record assignments | the slots' receipts | any **pre-unblinding** access to a χ-bearing object — a per-object execution receipt among them |
| N | **The lock ceremony** — producer: Duho | reads the digests BS-L binds → writes the BS-L artifact | P6, after BS-5f, before unblinding | clause 3(a)'s preconditions | BS-L | a BS-L artifact missing any schema field; a lock with no log; a signature over anything but the canonical body digest |
| O | **Unsealing service** — the unsealing callable whose symbol BS-2k pins (future work) | reconstructs key use for this ceremony only and decrypts both sealed stores into the declared post-unblinding working location; every step a logged event. Requires and verifies the canonical opening authorization, ensuring its unique ceremony identifier has not been consumed | P7 only; runs exactly once | a passing `verify_lock()` and Duho's **canonical opening authorization** | the **unblinding receipt**, carrying the authorization digest, verification result, consumed ceremony identifier, the ordered terminal events for unsealing, the complete extending chain segment, and the genuinely final access-log checkpoint | any invocation before a verified BS-L; any replay of the opening authorization; any decrypted byte outside the declared working location |
| P | **Verdict path** — `run_production_verdict()` (pinned symbol; guard extended per clause 3(d)) | **post-unblinding only**: reads the real χ vector joined to the accepted mask; first re-invokes `recompute_acceptance_ledger` against the sealed ledger and refuses on a mask-digest disagreement with BS-2f. **Applies confidence-based exclusion threshold**. Requires a verified BS-L bound to that mask digest exactly as it requires BS-5f's → writes the permutation record and the verdict | P8, after unblinding | the unblinding receipt (verified by pinned `verify_unblinding_receipt()`) and a verified BS-L | BS-7f, then BS-V | any execution before unblinding; any verdict produced outside this symbol |
| Q | **Archive seal-state checker** — `verify_archive_seal` (pinned symbol at BS-2k) | reads archive metadata (not contents) by non-content metadata operation | P3, P6 | BS-2k | the archive seal-state receipt at BS-2f and pre-unblinding lock checkpoint | any read of archive contents |
| R | **Every other person and every other process** | nothing χ-bearing pre-unblinding; the default is forbidden | pre-unblinding | — | — | any pre-unblinding access |
| S | **Disclosure and Publication** | **post-unblinding only**: exports the result after the verdict receipt exists | P9 | BS-V | the published result | any export before BS-V |

The hand-check path, end to end: **BS-8p authorization and allocation → individually logged
views through the sealed interface (row G) → labels written only through that interface,
the sole writer (row H) → the χ-bearing label-set receipt remaining in the store →
BS-8f aggregation reading that receipt (row I) → Stage C (row J).**

Synthetic exploration (`explore_verdict()` on a `FixtureMask`) touches no sealed object and
is unrestricted.

**Clauses.**

1. **The ban is universal and binds access, not merely disclosure.** No person and no
   process may decrypt, query, render, summarise or inspect any χ-bearing object or
   derivative before unblinding, except within a table row's stated surface. The ban names
   no roles because it has none: it binds Duho, Hwao, every key holder, every committee
   member outside row G's surface, and every process alike.

2. **The exceptions are the table's rows, or they do not exist.** No process that touches a
   χ-bearing object may run before the lock unless a row names it. Each automation row is
   identified by the pinned code symbol that implements it. The symbols that exist in the
   pinned v9 bytes today are exactly: rows F, I, J, P, and the receipt envelope.
   Every other automation symbol is future work, and its row names the class-P slot whose
   receipt pins the symbol and digest — BS-2k (rows B, O, Q), BS-9 (rows C, D), BS-2a (rows C2, E),
   BS-8p (rows G, H) — and **the process may not run before that pin exists**.

3. **The primary lock (BS-L) is executable and receiptable.**
   (a) *Class and preconditions.* BS-L is a **class-E** slot. Its preconditions are: the
   freeze is in force, and BS-5f's Stage-C receipt exists. BS-L certifies no set containing itself.
   (b) *The lock artifact — a detached signature over a canonical body.* BS-L's canonical
   body names exactly, in canonical order: the roster digest, the
   accepted-mask digest, the calibration-record digest, the Stage-C receipt
   digest, the decision-input digests, **the ordered manifest of every class-P slot receipt, gate reports, and Duho's freeze signature**, the **pre-unblinding lock checkpoint** together with the chain segment demonstrating it extends BS-2f's, the **archive seal-state receipt**, the environment record, and Duho's signer identity.
   The canonical body's digest is what Duho signs. The detached signature and the signer identity are carried in the
   outer artifact, outside the signed body.
   (c) *Sequence, producers and verification.* The sequence BS-5f → BS-L → unblinding →
   BS-7f → BS-V is recorded through named producers. The pinned verifier `verify_lock()` checks schema
   completeness, every digest binding, BS-5f's PASS, the manifest of freeze completeness (verifying those bound bytes rather than re-resolving filenames), the lock checkpoint's extension of BS-2f, and the archive seal-state transition (Clause 7). **Failure refuses unblinding and refuses
   the verdict path.**
   (d) *The gate on the only verdict path.* The production runner must require a verified BS-L. **These mechanisms
   are run guards and digest serializations, which §0's enumeration assigns to the pinned code**. This §6 replacement and every Part 2 seam
   are **one atomic candidate revision**.
   (e) *Receipt authenticity.* Canonical receipts must carry and authenticate their decoded fields.

4. **Access is logged and mediated.** An append-only log covers all three sealed stores. Enforceable mediation is a **BS-2k gate condition**: no holder or run host may possess a raw-store read path outside the pinned mediator; the gate must identify and test that boundary, and inability to enforce it makes BS-2k unfillable. A **pre-unblinding lock checkpoint** is taken immediately before canonicalizing BS-L; the chain continues through issuance, opening, and unsealing to a **genuinely final post-unblinding checkpoint**, carried in the unblinding receipt.

5. **The void rule.** Any pre-unblinding touch of a χ-bearing object outside the table voids the
   run. Access inside a table row, within its stated surface, after its stated
   authorization exists and producing its stated emission, does not void it (e.g. BS-L issuance and opening).

6. **Opening authorization.** The canonical opening-authorization body and signature envelope binds exactly: the BS-L digest, both store identities, the declared post-unblinding destination, a unique one-use ceremony identifier, phase P7, Duho's signer identity (bound to the BS-2k public key), and the schema/version. Row O's pinned verifier authenticates those exact fields and atomically refuses an already-consumed ceremony identifier.

7. **Archive seal-state transition.** The canonical authenticated seal-state schema binds archive identity, seal identifier/version, holder-roster digest, checkpoint predecessor digest, and monotonic event/epoch data. The permitted transition relation from BS-2k → BS-2f → lock checkpoint is identity and intact-state equality. BS-2f compares against BS-2k; BS-L compares against BS-2f. `verify_lock()` refuses any nonconforming transition.

8. **What is checkable about the redesign's blindness.** The retrospective-custody question is **open** and is named here rather than claimed closed; its resolution is a freeze-level decision for the principal.

### §6.2 The predecessor's sealed measurements

The declined study's 208,405 sealed χ measurements are archived. **No predecessor χ
measurement enters this run's analysis.** The archive is retained as historical record; **no row in §6.1's table reads it.** Its governance is seal-state and enforceable mediation: BS-2k records the archive's identity, roster, and a receipted seal state via non-content metadata operation (Row A), and the archive is explicitly brought under Row B's mediator. Any attempted read of the archive's contents will be blocked by the mediator and logged, or if unlogged, break the access log's chain. That seal state is re-receipted at BS-2f and at the pre-unblinding lock checkpoint (Row Q), subject to the transition equality rule in Clause 7. A broken seal state is a custody failure.

### §6.3 General conduct clauses (carried unchanged)

- **No strata in the estimator.**
- **Calibration.**
- **Void rule for changes.**
- **One change per iteration.**
- **No claim stronger than its check.**
- **Custody.**
- **Blind double, honestly scoped.**

---

# PART 2 — CONFORMING EDITS OUTSIDE §6 THAT THIS REPLACEMENT REQUIRES

1. **§7 class-P table.** Remove BS-L. Add **BS-2k** (class P, DESIGN; blocks BS-6).
2. **§7 class-E table.** Add BS-L row (producer Duho; content per §6.1 clause 3(b)). Keep BS-V verdict only. BS-8f producer Hwao.
3. **§7 counts and DESIGN inventory.** Update §7's text to state "One of fourteen class-P slots is filled", updating the parsed count from 12 to 14. **Replace** the current DESIGN inventory with a list that includes BS-2a and BS-2k, and strictly excludes BS-2f (which is value-only). Add a lint assertion that the prose count equals the parsed table count and that the DESIGN inventory matches the VALUE/DESIGN classification. Add the unblinding receipt as a named post-unblinding artifact.
4. **§7 BS-2f row and pinned `SLOT_SCHEMA`**: The access-log checkpoint field and archive seal-state digest join BS-2f's schema. BS-L schema gets the manifest, lock checkpoint, and archive seal-state. Add unblinding receipt schema.
5. **§2.7(4) and §5:** `verify_cutout_integrity` executes pre-inference and computes the separate acceptance-evidence projection. `recompute_acceptance_ledger` computes statuses and reasons from these projections, atomically writing the evidence ledger and realised partition. Confidence threshold exclusion is dropped from pre-lock and moved to post-unblinding. Modify `run_production_verdict()` to require and verify the canonical BS-L artifact, the one-use unblinding receipt, the exact accepted-mask binding, and the post-unblinding ledger recomputation before forming any statistic. Post-unblinding, it applies the confidence rule exclusion. Name the corresponding new arguments/guards in §5.
6. **§10.** Record this §6 replacement.
7. **Code-side items in the same atomic revision**: `SLOT_SCHEMA` updates, `verify_lock()`, `verify_cutout_integrity`, `verify_unblinding_receipt()`, `verify_archive_seal()`, `recompute_acceptance_ledger`, enforceable mediation gate checks, opening authorization verifier.
8. **§2.5:** "Producer checksum list" applies exclusively to source image transport at BS-6.

---

# PART 3 — CHOICES THE FINDINGS DID NOT FORCE, AND THE ALTERNATIVE TO EACH

- **C1 — Changing the writer of the acceptance-evidence projection to a pre-inference integrity verifier.** Alternative: Write the projection from the outcome-aware instrument process, but constrain its output fields. Rejected because, as the principal advised, a projection written by a process that has seen the sign can always encode it. The integrity check (shape, checksum, completion) is a property of the image bytes and is computable without invoking the classifier. We separated this into Row C2, achieving outcome-blindness by construction.
- **C2 — Dropping confidence-based exclusion before unblinding.** Alternative: Keep confidence-based exclusion pre-lock and attempt to prove the confidence function cannot encode the sign. Rejected because proving that information flow is much harder than simply deferring the check. The cost is that we do not know until post-unblinding if too many objects fall below the confidence threshold, potentially wasting a run if the sample size becomes insufficient. We accept this cost for structural integrity.
- **C3 — Deriving cutout completeness from the fixed parent list and projections in Row E, rather than reading the completion receipt.** Alternative: Create an in-store verifier for the completion receipt in Row E. Rejected because the parent list is fixed, and enforcing exactly one authenticated projection per parent is sufficient and avoids giving Row E any additional complex receipts.
- **C4 — Archive seal-state checker as a separate row (Row Q).** Alternative: assign it to Row M (Hwao). Rejected because it's a gate inspector task (metadata only) rather than slot receipt writing. We assigned it the pinned symbol `verify_archive_seal`.

---

# PART 4 — RESIDUAL RISKS AND DIAGNOSIS OF FAILURE MODES

- **D1 — The Characteristic Defect: Renaming as Refusal.** In R3 and R4, this drafting process exhibited a repeated failure mode: renaming a finding without structurally addressing it. When told the acceptance projection was not sign-blind, we renamed it "outcome-free" but left it generated by an outcome-aware process containing confidence derived from the classifier. We declared a property instead of building a constraint. This draft explicitly acknowledges this failure mode. We have now addressed it by *changing the writer* and moving the confidence check post-unblinding, ensuring the property holds structurally.
- **R1 — The retrospective window is open.** The archive's seal-state receipts are prospective only. Whether anyone read predecessor χ before the geometry artifacts were fixed is established by nothing here. CODEX-V14 6 stands open against this draft.
- **R2 — Executability rides the next code revision.** Many required schemas and checks (BS-L manifest, enforceable mediation gates, opening authorization, evidence projection, integrity verifier) do not exist yet. Clause 3(d) makes the replacement an atomic candidate revision condition.
- **R3 — The committee is a designed human hole.** The draft binds their roles and interface, but cannot bind memory.

---

# PART 5 — THE FINDINGS, WHERE EACH LANDS

1. **The acceptance-evidence projection is declared outcome-free, not made outcome-free (GPT56 1 / CODEX 1).** REPAIR. We adopted the principal's design principle. We created a new Row C2 (`verify_cutout_integrity`) that reads cutouts pre-inference and computes the acceptance-evidence projection (checksums, shape, execution status). It never invokes the classifier, making the projection outcome-free by construction. We dropped confidence-based exclusion before unblinding, moving it to post-unblinding in `run_production_verdict()`.
2. **Predecessor-archive access is forbidden but not prospectively detectable or mediated (CODEX 2).** REPAIR. We brought the predecessor archive under the pinned mediator (Row B) and the append-only access log at BS-2k. We removed every raw holder/read path, and bound that log's checkpoints into BS-2f and BS-L. Any read attempt is now mediated and logged.
3. **The table's automation inventory omits its own automated archive checker (CODEX 3 / GPT56 4).** REPAIR. We gave Row Q the named checker symbol `verify_archive_seal`, pinned its digest in BS-2k, added it to clause 2's future-work enumeration, and added it to Part 2's atomic code revision list.
4. **Row E has no lawful path to consume its χ-bearing cutout-completion authorization, and the receipt has no verifier (CODEX 4 / GPT56 2).** REPAIR. We defined the cutout-completion receipt's schema and pinned its verifier at BS-9. Row D authenticates and verifies it before inference. We removed the cutout-completion receipt entirely from Row E's authorization; instead, Row E derives completeness by verifying exactly one authenticated acceptance-evidence projection per parent against the independently fixed parent list.
5. **The unblinding receipt names a final checkpoint but does not make finality verifiable (GPT56 3).** REPAIR. We defined the canonical authenticated schema for the unblinding receipt, binding the BS-L checkpoint digest, the complete extending chain segment, the terminal events for unsealing, and the final access-log checkpoint. We pinned `verify_unblinding_receipt()` and require Row P to call it, enforcing finality structurally.
6. **The closed non-χ-bearing list classifies outcome receipts as non-outcome artifacts (GPT56 5).** REPAIR. We removed BS-7f and BS-V from the closed non-χ-bearing list. We explicitly classified them as post-unblinding χ-bearing receipts in the scope and authorized them only through Rows P and S after the unblinding receipt exists.
7. **Part 2 preserves a false §7 DESIGN inventory (GPT56 6).** REPAIR. We updated Part 2 to explicitly *replace* the DESIGN inventory, strictly excluding the value-only BS-2f and including BS-2a and BS-2k. We also added a lint assertion to check that the DESIGN inventory matches the value/design classification.
