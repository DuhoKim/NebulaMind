# §6 DRAFT — KIMI SEAT, SECOND PASS (R2), 2026-08-27

Status: DRAFT FOR REFEREE. Written under `BRIEF_DRAFT_SECTION6_R2.md`, revising
`SECTION6_DRAFT_KIMI.md` against the two referee reports on it —
`SECTION6_REVIEW_GPT56.md` (five blockers) and `SECTION6_REVIEW_CODEX.md` (four blockers,
one major) — read in full, not from the brief's summary. Referees: GPT56 and CODEX. The
principal reviews before anything enters the document. I do not referee my own text; Part 4
names this draft's own residual risks and Part 5 maps every finding to where it landed.
This file modifies nothing; `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` is untouched. Part 1
is the complete replacement §6, written to drop in. Part 2 lists the conforming edits
outside §6 that dropping it in requires. Part 3 states every choice the findings did not
force, with its alternative. Part 4 names the residual risks this draft itself carries.
Part 5 maps the brief's seven requirements and all ten findings to where they land, and
says what I verified before accepting each.

The first draft's closure is kept where the referees confirmed it: the ban binds access,
universally, with the table as the only exception, and a table-authorized act does not void
the run. No repair below trades that away; Part 5 says so finding by finding.

---

# PART 1 — THE REPLACEMENT §6

## §6 Conduct

- **Disclosure.** Nothing derived from any real χ value — value, sign, summary, label, or
  count of signs — is published, spoken, or written outside the sealed stores defined in
  §6.1 before the primary lock, **with exactly one exception: the permitted aggregate
  surface defined in §6.1's scope paragraph, which leaves the sealed stores only as the
  BS-2f and BS-8f receipts, on the paths the table names, and is the only pre-lock
  χ-derived export this text allows.** After unblinding, disclosure waits for BS-V (§7).
  The predecessor's §4/condition-2 breach is why this clause exists. What binds *access* is
  §6.1, and §6.1 is the normative object of this section.

### §6.1 The blinding covenant — one lifecycle table, and the table is normative

**Scope — what is χ-bearing.** A *χ-bearing object* is: any cutout produced for this run;
any per-object instrument output — a χ value, sign, amplitude, confidence value, **and
every per-object execution receipt, which carries those fields**; any per-object hand-check
label or per-object human–instrument agreement; any derivative of these that is not on the
permitted aggregate surface below; and **the predecessor's sealed archive of 208,405 χ
measurements** (§6.2) — outcome knowledge on overlapping sky, governed by §6.2's seal-state
rule. The *permitted aggregate surface* — χ-derived but defined as not χ-bearing — is
exactly: the BS-2f mask fields (brickid, objid, position, acceptance flag, calibration-bin
label, boundaries, digests — never a χ sign), and the BS-8f aggregate record (â, σ_a, a_LB,
the per-bin {â_b, σ_ab, a_LB_b}, ε̂, and the full Cov_a — aggregates over the hand-check
sample, never a per-object value). **Non-χ-bearing receipt and log classes — a closed list,
defined by schema, and the list is exhaustive.** An artifact is non-χ-bearing only if it
conforms to one of these authenticated schemas, none of which can carry a per-object
outcome value or a digest of a payload containing one: (i) a slot receipt under the pinned
`SLOT_SCHEMA` as conformed by this revision's code items — the v9 schema does not yet carry
BS-2a, BS-2k or BS-L, and until it does no receipt of those slots can exist at all — namely
BS-1, BS-1b, BS-2a, BS-2c, BS-2k, BS-2m, BS-2o, BS-3, BS-4, BS-5p, BS-2s, BS-6, BS-7p,
BS-8p, BS-9, BS-2f, BS-8f, BS-5f, BS-L, and BS-7f/BS-V, which exist only
post-unblinding; (ii) the access log under its BS-2k event schema (timestamp, actor, table
row, operation, object identity, success/refusal, refusal reason, running chain digest —
identities and flags, never payload bytes); (iii) the producer checksum list (§2.5); (iv)
fixtures and their transcripts, synthetic by construction. **Everything else is χ-bearing
by default**: any artifact not on this list and not on the permitted surface; every
per-object execution receipt wherever it sits; **any opaque digest of χ-bearing bytes** — a
digest whose preimage's schema is not on this list or the permitted surface, the acceptance
ledger's digest among them, because such a digest is a verification oracle for a guessed
outcome; and any schema that permits outcome payloads. Doubt resolves toward χ-bearing.

**The sealed stores.** The *main sealed store* holds cutouts, instrument outputs and the
acceptance ledger. The *committee sealed store* holds the hand-check labels. A third
χ-bearing store — the predecessor archive — is governed by §6.2's seal-state rule, not by
any row of the table, because no row ever reads it. Both new stores are provisioned at
**BS-2k** (custody design: the two store identities, key generation/split/escrow, Duho's
signing public key, the key-holder roster, the mediator symbol and its access-log event
schema, the unsealing construction, and the archive's identity, existing holder roster and
receipted seal state) — a class-P DESIGN slot, so both stores, all keys, the roster, the
mediator and the archive's receipted seal state exist before the freeze, hence before any
image byte. Gates and referees are external witnesses: their inputs are the closed list of
non-χ-bearing receipt classes and fixtures only, and no gate input is χ-bearing.

**The phase line.** P0 freeze (BS-2k and every other class-P slot receipted, gates passed,
Duho's freeze signature) → P1 BS-6, first image byte → P2 cutout production and instrument
inference → P3 BS-2f → P4 BS-8f → P5 BS-5f → P6 BS-L, **the primary lock** → P7 unblinding
→ P8 BS-7f and BS-V → P9 disclosure. BS-5f blocks BS-L; BS-L blocks unblinding; BS-V follows
unblinding and is the verdict receipt, never the lock.

**THE TABLE.** Each row is one permitted actor or process. **Any touch of a χ-bearing
object by any person or process not in this table, or outside a row's stated surface, is
forbidden by default** — that is what makes completeness checkable by reading one column.
Processes that never touch a χ-bearing object — release-image transport under BS-6, gates
and referees reading the closed receipt classes, receipt-envelope verification, scheduling
— are outside this default precisely because the default governs χ-bearing touches and
nothing else; this sentence is what says so. Two receipt columns are named separately
because they are two different things: an act is permitted once its **authorized by**
condition exists, and it is made auditable by the **emission** it produces. No row's
authorization is its own emission. (Row letters differ from this draft's first version: the
provisioner, mediator and unsealing rows are new, and the first draft's rows C, E, G, H, L,
M and N are E, G, I, J, N, P and Q here.)

| # | actor / process — identity | may touch (read → write) | when | authorized by (must exist first) | emits (receipt this act produces) | what voids the run |
|---|---|---|---|---|---|---|
| A | **Custody provisioner** — producer: Hwao builds, Duho designates the holders; the BS-2k custody design and the tooling it names | creates the two new stores' containers; generates, splits and escrows the keys; generates Duho's signing keypair and binds its public half; installs the mediator (row B); records the predecessor archive's identity, its existing holder roster and its seal state → writes the BS-2k design artifacts. **Never reads a χ value**: none exists yet for this run, and the archive's contents it never opens — it records seal state, not contents | P0, before the freeze, hence before any image byte | — (a freeze prerequisite; no slot precedes it) | BS-2k | any read of archive contents; any key share retained outside the escrow the design declares; any store, key or wrapper existing outside the receipt |
| B | **Store mediator / log writer** — the logging wrapper whose symbol and digest BS-2k pins (future work; may not mediate before that pin exists) | the only path by which any row's stated read or write reaches a sealed store's bytes; conveys bytes strictly as the conduit of another row's stated surface → appends exactly one event per touch, success or refusal, under the BS-2k event schema (timestamp, actor, row, operation, object identity, success/refusal, refusal reason, running chain digest). A request that matches no extant row's actor, surface and window is refused, and the refusal is logged | from BS-2k's completion to the final checkpoint | BS-2k | the access-log chain; its running checkpoint digest receipted at BS-2f, and again at BS-L as the final checkpoint (clause 3) | any byte delivered outside the requesting row's stated surface; any unlogged touch; any retained copy; a refusal left unlogged |
| C | **Cutout producer** — the BS-9 production runner; symbol and digest pinned at BS-9 (future work; may not run until BS-9 is filled) | reads release image bytes → writes cutouts into the main sealed store, via row B; never reads any sealed object | P1–P2, after BS-6 | BS-6 (transport approval) and BS-9 (runner pin) | the per-cutout checksum records of §2.5's producer checksum list, bound into the acceptance ledger and cross-checked at BS-6 | any cutout or derivative outside the store; any human view of a cutout outside row G's interface |
| D | **Instrument runner** — the BS-9 gated runner executing BS-3's pinned instrument identity (weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry) | reads cutouts in the store → writes per-object χ, confidence and per-object execution receipts into the store only — all χ-bearing, and they stay there | P2, after row C, before BS-2f | BS-3 (instrument identity), BS-9 (runner pin), and row C's complete cutouts | the per-object measurement receipts, one per parent object, in the store (completeness is what `require_complete_sample()` later checks) | any χ-derived value emitted outside the store |
| E | **Acceptance-ledger recompute** — the callable `recompute_acceptance_ledger` whose symbol and digest BS-2a's receipt must pin (future work: the symbol does not exist in the pinned v9 bytes; naming it here binds BS-2a, and the process may not run before that pin exists) | reads the acceptance ledger's per-object evidence in the main store — expected/actual cutout checksums and shapes, per-object execution receipts, finite-output flags, frozen confidence values: χ-bearing evidence, and this row is its only pre-lock reader — and **recomputes every §2.7(2)(a)–(d) predicate from it**; never a χ sign, amplitude, or axis-relative position beyond what the evidence schema carries (§2.7(3): sign-blind by construction) → writes the realised partition; refuses any status, reason or evidence the recompute disagrees with | P2–P3, after complete inference (every parent object has a measurement receipt), before BS-2f | BS-2a (the frozen acceptance design) and the complete set of per-object measurement receipts | the realised-partition record, bound by BS-2f | reading any field outside the evidence schema — a χ sign or amplitude above all; any exclusion reason outside §2.7(2)(a)–(d); any status, reason or evidence the recompute disagrees with |
| F | **Calibration-bin sealing** — `calibration_bins()`, `assign_bins()`, `allocate_handcheck()` (pinned symbols) | reads the accepted partition's positions and acceptance flags only (χ-free) → writes sealed boundaries, bin labels, and the hand-check allocation | allocation plan pinned pre-freeze at BS-8p; boundaries sealed and labels assigned at P3, with the partition, at BS-2f | BS-8p (plan) and the realised partition | the sealed boundary and allocation record, bound by BS-2f | any χ-bearing input to bin construction |
| G | **Hand-check committee** — members named at BS-8p; **no member holds any other role in this study**, and no member fills, adjudicates or locks any slot other than co-signing the label-set receipt | views χ-bearing cutouts **of the allocated sample only**, rendered through the BS-8p sealed interface's view half (symbol pinned at BS-8p) → each label leaves the member only through that same interface to row H; a member's hands never write the committee store, and **no intermediate persistence or export exists between entry and row H's write** | after BS-8p and after the sample's cutouts exist; complete before BS-8f | BS-8p (the declaration: members, store, interface, label schema, label-set receipt schema), the sealed allocation, and the sample's cutouts existing | the member co-signatures carried by the label-set receipt | a member holding any other role; any label, tally, description or impression exported by a member outside the sealed interface; any view of an object outside the allocated sample; any unlogged view; any label path other than entry → row H |
| H | **Label-ingestion writer — the committee store's only writer** — the BS-8p sealed interface's ingestion half (symbol and digest pinned at BS-8p; future work; may not run before that pin exists) | receives labels from row G through the interface → writes them, as one label set, into the committee sealed store; emits nothing outside it | with row G, completing before BS-8f | BS-8p | **the label-set receipt, over the sealed label-set digest, the view-log range, the allocation digest, and the member co-signatures** | any write path outside the pinned interface; any intermediate persistence between entry and write; any field beyond the pinned label schema |
| I | **Calibration computation** — the BS-8p-pinned per-bin reducer (joining labels to instrument signs inside the stores) feeding `accuracy_from_handcheck()` (pinned symbol, which consumes only the per-bin counts) | reads the sealed label set and the corresponding instrument outputs, inside the stores → writes **only** the BS-8f aggregate fields (the permitted aggregate surface) | P4, after the label-set receipt, before BS-8f | the completed label-set receipt | BS-8f | any per-object label, sign or agreement leaving the stores; any field beyond the BS-8f schema |
| J | **Stage-C runner** — `stage_power` with `inject_signs` (pinned symbols; frozen generator, addresses, pass rule) | reads the sealed BS-2f mask (χ-free) and the BS-8f aggregates; injects synthetic signs only — **never reads a real χ** → writes the Stage-C receipt | P5, after BS-2f and BS-8f, before BS-L | BS-2f and BS-8f | BS-5f | reading any real χ; continuing the run after a Stage-C FAIL (INCONCLUSIVE-BY-POWER halts the run; no real-sky statistic is formed) |
| K | **Key holders** — roster designated at BS-2k before the freeze; roster digest bound into BS-L | touch nothing before the lock; custody exists for the lock ceremony and later audit only — **holding a key is custody, never licence** | — | BS-2k (designation) | none (the roster digest is bound by BS-L) | any pre-lock read by any holder, authorised or not |
| L | **Duho** | signs the freeze; designates holders at BS-2k; signs BS-L's canonical lock digest (clause 3(b)) reading its digest fields only; opens the lock by signature after BS-L exists and verifies, the opening a logged event | P0, P6, P7 | for the freeze: every class-P slot receipted and the gates passed; for BS-L: clause 3(a)'s preconditions | the freeze signature; the BS-L detached signature; with row O, the unblinding log record | any pre-lock access to a χ-bearing object; opening the lock before a verified BS-L exists; signing anything but the canonical lock digest |
| M | **Hwao** — producer of record for the slots | reads the closed list of non-χ-bearing receipt classes (scope) → writes the slot receipts §7 assigns | throughout | §7's producer-of-record assignments | the slots' receipts | any pre-lock access to a χ-bearing object — a per-object execution receipt among them |
| N | **The lock ceremony** — producer: Duho | reads the digests BS-L binds → writes the BS-L artifact and its log entries | P6, after BS-5f, before unblinding | clause 3(a)'s preconditions | BS-L | a BS-L artifact missing any schema field; a lock with no log; a signature over anything but the canonical body digest |
| O | **Unsealing service** — the unsealing callable whose symbol BS-2k pins (future work; may not run before that pin exists) | reconstructs key use for this ceremony only and decrypts both sealed stores into the declared post-unblinding working location; every step a logged event | P7 only; runs exactly once | a passing `verify_lock()` and Duho's opening signature | the unblinding log record | any invocation before a verified BS-L; any key-share reconstruction outside the ceremony; any decrypted byte outside the declared working location |
| P | **Verdict path** — `run_production_verdict()` (pinned symbol; guard extended per clause 3(d)) | **post-unblinding only**: reads the real χ vector joined to the accepted mask; first re-invokes `recompute_acceptance_ledger` against the sealed ledger and refuses on a mask-digest disagreement with BS-2f; requires a verified BS-L bound to that mask digest exactly as it requires BS-5f's → writes the permutation record and the verdict | P8, after unblinding | the unblinding record and a verified BS-L | BS-7f, then BS-V | any execution before unblinding; any verdict produced outside this symbol |
| Q | **Every other person and every other process** | nothing χ-bearing before unblinding; the default is forbidden | — | — | — | any access |

The hand-check path, end to end: **BS-8p authorization and allocation → individually logged
views through the sealed interface (row G) → labels written only through that interface,
the sole writer (row H) → the completed label-set receipt, co-signed by the committee →
BS-8f aggregation (row I) → Stage C (row J).**

Synthetic exploration (`explore_verdict()` on a `FixtureMask`) touches no sealed object and
is unrestricted; the §3 type boundary — production entry points call `require_sealed()` and
refuse a fixture by type, and the reverse — is what makes this sentence true.

**Clauses.**

1. **The ban is universal and binds access, not merely disclosure.** No person and no
   process may decrypt, query, render, summarise or inspect any χ-bearing object or
   derivative before unblinding, except within a table row's stated surface. The ban names
   no roles because it has none: it binds Duho, Hwao, every key holder, every committee
   member outside row G's surface, and every process alike. No authorisation other than the
   table's exists; claimed authority is no defence for access outside it, and there is no
   logged-and-therefore-permitted read.

2. **The exceptions are the table's rows, or they do not exist.** No process that touches a
   χ-bearing object may run before the lock unless a row names it. Each automation row is
   identified by the pinned code symbol that implements it. The symbols that exist in the
   pinned v9 bytes today are exactly: rows F (`calibration_bins()`, `assign_bins()`,
   `allocate_handcheck()`), I (`accuracy_from_handcheck()`), J (`stage_power` with
   `inject_signs`), P (`run_production_verdict()`), and the receipt envelope (`receipt()`).
   Every other automation symbol is future work, and its row names the class-P slot whose
   receipt pins the symbol and digest — BS-2k (rows B, O), BS-9 (rows C, D), BS-2a (row E),
   BS-8p (rows G, H, I's reducer) — and **the process may not run before that pin exists**.
   A row run under a symbol or digest that disagrees with its pin is access outside the
   table.

3. **The primary lock (BS-L) is executable and receiptable.**
   (a) *Class and preconditions.* BS-L is a **class-E** slot. Its preconditions are: the
   freeze is in force (every class-P slot receipted — §7's class-P set, which does not and
   cannot include BS-L — gates passed, Duho's freeze signature), and BS-5f's Stage-C
   receipt exists. BS-L certifies no set containing itself.
   (b) *The lock artifact — a detached signature over a canonical body.* BS-L's canonical
   body names exactly, in canonical order: the roster digest (from BS-2k), the
   accepted-mask digest (BS-2f), the calibration-record digest (BS-8f), the Stage-C receipt
   digest (BS-5f), the decision-input digests (the §0 code digest and the frozen decision
   constants it carries), the access-log final checkpoint (the running chain digest at lock
   time) **together with the chain segment demonstrating that the final checkpoint extends
   the checkpoint receipted at BS-2f**, the environment record, and Duho's signer identity.
   The canonical body's digest — computed exactly as `receipt()` computes an envelope
   digest — is what Duho signs. The detached signature (Ed25519, under Duho's personal
   signing key generated and bound at BS-2k) and the signer identity are carried in the
   outer artifact, outside the signed body, so no signature is ever over a body containing
   itself. This field set and construction enter the pinned `SLOT_SCHEMA` and code at the
   next code revision (already forced by the Stage-P blocker); until then no conforming
   BS-L artifact can be emitted and this clause forbids what the code cannot yet produce.
   (c) *Sequence, producers and verification.* The sequence BS-5f → BS-L → unblinding →
   BS-7f → BS-V is recorded through named producers: Hwao produces BS-5f via row J; **Duho
   produces and signs BS-L** (row N) and performs the logged unblinding (rows L, O); Hwao
   produces BS-7f and BS-V via row P. The pinned verifier — `verify_lock()`, entering at
   the same revision — is called by both the unblinding ceremony and
   `run_production_verdict()`; it recomputes the canonical body and its digest, verifies
   the detached signature against Duho's BS-2k-bound public key, and checks schema
   completeness, every digest binding (roster = BS-2k's, mask = BS-2f's, calibration =
   BS-8f's, Stage-C = BS-5f's, decision inputs = §0's pinned code), BS-5f's PASS, freeze
   completeness, and the final-log checkpoint's extension of the BS-2f checkpoint by
   replaying the carried segment. **Failure of any of these refuses unblinding and refuses
   the verdict path.** BS-V is the verdict receipt only; it carries no lock field, seals
   nothing, and is never the lock.
   (d) *The gate on the only verdict path — and §0's reach, stated correctly.* The
   production runner must require a verified BS-L bound to the mask digest exactly as it
   requires BS-5f's; that guard enters at the same code revision as (b). **These mechanisms
   — the BS-L schema, receipt-envelope verification, and this guard — are run guards and
   digest serializations, which §0's own enumeration assigns to the pinned code; §0's
   code-precedence rule reaches them, and the first draft's sentence saying it does not
   reach this section was wrong.** Consequently this §6 replacement and every Part 2 seam
   are **one atomic candidate revision**: no freeze and no execution is conforming until
   the newly pinned and gated code implements the BS-2k, BS-L and BS-2f schemas,
   authenticated receipt-field consumption, and the BS-L guard on the only production
   verdict path — validated by `prereg_lint.py` on the integrated candidate and by a new
   end-to-end refusal fixture walking BS-2f + BS-8f → BS-5f → BS-L → unblinding → BS-7f →
   BS-V with tamper tests at every edge. Until that revision lands and is gated, row P's
   void stands in prose: conduct text forbids what the code cannot yet refuse — the same
   disclosed posture the document already takes for Stage P, with the same weakness, named
   here rather than hidden.
   (e) *Receipt authenticity.* A receipt is evidence only as produced by the pinned
   `receipt()` and verified against its pinned schema; the revision must make canonical
   receipts carry and authenticate their decoded fields, or make every consumer decode and
   verify the canonical body — a control field asserted outside the authenticated envelope
   is not evidence of anything. (The pinned v9 `run_production_verdict()` reads exactly
   such post-envelope fields from the BS-5f receipt; the defect is named here, not
   reproduced.) The consumer-side verification this requires is part of the same code
   revision.

4. **Access is logged or it did not happen.** An append-only log, written only by row B
   from BS-2k's completion, covers both new sealed stores; every mediation — successful or
   refused — appends one event at the time of the touch under the BS-2k event schema, each
   event chained to the last by the running digest. The chain digest is receipted at BS-2f
   and again, as the final checkpoint with its extending segment, at BS-L. **The absence of
   the log, any gap or broken link in it, or a missing checkpoint receipt is itself a
   failure: a lock with no log is a lock that failed.** The checkable sentence is
   unchanged: **no χ-derived artifact exists outside the sealed stores before the primary
   lock.** The predecessor archive is not behind this log; its detection rule is §6.2's
   seal-state checkpoints. Completeness: BS-2k's design must provision the stores so that
   every access flows through row B, must state the technical boundary below which access
   outside the wrapper is physically possible, and must name who holds the risk below that
   boundary. What the log records is visible; what bypasses the wrapper is the residual
   risk BS-2k is required to state, not allowed to hide.

5. **The void rule.** Any pre-lock touch of a χ-bearing object outside the table voids the
   run — authorised or not, disclosed or not, and whether or not the accessor believed it
   harmless. Access inside a table row, within its stated surface, after its stated
   authorization exists and producing its stated emission, is the run proceeding as
   designed and does not void it. The committee's mandated views (row G) and the named
   processes' mandated touches (rows A–J) are inside the table; this clause and clause 1
   are written to be jointly satisfiable, and a reading under which the table authorizes an
   act that this clause voids is a defect in this text, not a discretion available to any
   operator.

6. **What is checkable about the redesign's blindness.** The successor footprint was chosen
   from geometry alone. What is checkable is that the redesign record
   (`real/REAL_GEOMETRY_RESULT_20260825.md`, the selection artifacts and their digests)
   carries no outcome-derived quantity — inspected, and re-inspectable; if any is ever
   found in the redesign path, the redesign was not blind and this text's licence fails
   with it. That the redesign was in fact blind rests on evidence this prospective covenant
   cannot produce: the geometry choice predates it, and no log this section creates reaches
   backward. The retrospective-custody question is **open** (referee finding CODEX-V14 6)
   and is named here rather than claimed closed; its resolution is a freeze-level decision
   for the principal, not something this section asserts.

### §6.2 The predecessor's sealed measurements

The declined study's 208,405 sealed χ measurements are archived. **No predecessor χ
measurement enters this run's analysis. Every χ this study uses is measured fresh under
this text**, from images fetched under this text, through the instrument this text pins.
The archive is retained as historical record; **no row in §6.1's table reads it, at any
phase, for any purpose, and it is not an input.** Its governance is seal-state, not use:
BS-2k records the archive's store identity, its existing holder roster, and a receipted
seal state — the technical state that makes it inaccessible to this run's hosts, and the
logging boundary that would catch an attempt — and that seal state is re-receipted at
BS-2f and at BS-L. A broken seal state at any checkpoint is a custody failure of the run.
Reuse would require a new text, a new gate and a new signature, because the reuse contract
and its blinding safeguards do not exist here.

### §6.3 General conduct clauses (carried unchanged)

- **No strata in the estimator.** The centred slope needs no tertiles; the one-shot strata
  hazard is retired by design.
- **Calibration.** Bin-construction algorithm and the 3 × 9 joint allocation with V3-pred's
  nine HC strata are frozen in code (`calibration_bins()`, `assign_bins()`,
  `allocate_handcheck()` — proportional, largest remainder, explicit tie rule, and BOTH
  inherited floors enforced: ≥ 10 per non-empty joint cell **and ≥ 30 real labels per live
  inherited HC stratum**). Infeasible floors FAIL rather than shrink. `calibration_bins()`
  states and IMPLEMENTS one tie rule and refuses degenerate bins. Numeric boundaries are
  instantiated and sealed at **BS-2f** from positions and flags only. **BS-8f** reports â,
  σ_a, a_LB, per-bin â_b, σ_ab, a_LB_b, ε̂ and the full Cov_a via
  `accuracy_from_handcheck()`, which implements **the inherited HC-1H estimator**
  `a = (raw − ε)/(1 − 2ε)` with the shared-ε derivative propagated. **Admissibility
  (`adjudicate_path()`):** `max_b |â_b − â| ≤ 0.03` AND every `a_LB_b ≥ 0.85` → scalar
  path; spread failure only → profile path; any `a_LB_b < 0.85` →
  **INCONCLUSIVE-BY-CALIBRATION, pre-unblinding halt.** V3-pred's HC-1H measurement and
  validity rules (committee, sealed keys, HC-5, HC-6) are carried by quotation at freeze.
- **Void rule for changes.** Any post-first-real-χ change to ANY binding rule, parameter,
  algorithm, slot schema, randomness/serialization contract, reference-code byte, or
  decision threshold in this preregistration voids the run; only the mechanical filling of
  predeclared class-E values by their frozen producers is exempt. Post-read amendments
  cannot cure a void.
- **One change per iteration:** every gated revision of this text changes one thing per
  finding, and the §10 trace maps finding → change; any change not traceable to a finding
  is listed separately with its hypothesis stated.
- **No claim stronger than its check.** Gate-state sentences never exceed the cited
  artifact's first line.
- **Custody.** Receipts with digests; deliverables sha-pinned at gate dispatch by the
  gate's own report (an external witness) and committed to git; self-referential hash
  chains are not custody; describe-vs-compute discipline throughout.
- **Blind double, honestly scoped:** because §0 makes the code bodies normative, the second
  product is a **clean-room reimplementation from this constitution plus a published
  per-function normative specification**, gated against the reference on the fixture
  battery. Where the spec is insufficient to reproduce a digest, that is a **spec defect to
  be repaired**, not an agreement failure. Divergence in any integer, sequence, or verdict
  is a STOP recorded as a finding — never reconciled by editing either implementation
  toward the other.

---

# PART 2 — CONFORMING EDITS OUTSIDE §6 THAT THIS REPLACEMENT REQUIRES

The four-round failure mode named in the first brief is clauses contradicting each other
across 650 lines. This replacement is written so §6 needs no arbitration, but these seams
outside §6 must be conformed **in the same revision** or the contradiction returns — and
clause 3(d) now makes that atomicity a stated condition, not a hope: the §6 replacement,
these text seams, and the code items below are one candidate revision, and no freeze or
execution is conforming until all of it lands and is gated.

1. **§7 class-P table.** Remove the BS-L row (BS-L becomes class E). Add **BS-2k** (class
   P, DESIGN; producer Hwao, holders designated by Duho; content: the two new stores'
   identities, key generation/split/escrow, Duho's signing public key, the key-holder
   roster, the mediator symbol and access-log event schema, the unsealing construction, and
   the predecessor archive's identity, existing holder roster and seal-state receipt;
   blocks BS-6). Regenerate the classification sentence from the table: with BS-L removed
   and BS-2k added, **fourteen class-P slots, one filled (BS-2m); the DESIGN slots are
   BS-2a, BS-2k, BS-5p, BS-8p and BS-9**; BS-2f stays explicitly class-E and value-only.
2. **§7 class-E table.** Add the BS-L row (producer Duho; content per §6.1 clause 3(b),
   including the detached signature and signer identity; blocked by BS-5f and the freeze;
   blocks unblinding). Keep BS-V's content as "verdict" only (V15 already reads "verdict
   only — NOT the lock"). BS-8f's producer becomes "Hwao, from the hand-check committee's
   sealed label set" (the committee co-signs the label-set receipt, not the slot). BS-8p's
   content gains the committee declaration — members, the committee sealed store, the
   sole-writer sealed interface (view half and ingestion half), the label schema, the
   label-set receipt schema, and the per-bin reducer.
3. **§7 BS-2f row and the pinned `SLOT_SCHEMA`** (next code revision): the access-log
   checkpoint field joins BS-2f's schema.
4. **§2.7(4) and §5 — producer and timing of the acceptance recompute.** §2.7(4) names
   `recompute_acceptance_ledger` — pinned at BS-2a — as the callable that recomputes every
   predicate from the ledger evidence and produces or refuses the realised partition at
   P2–P3, replacing the "`run_production_verdict()` — or a mandatory pre-verdict validator
   it calls" formulation (which places the check on the post-unblinding path, where BS-2f
   cannot come from). §5's runner description gains two sentences: it re-invokes that same
   callable against the sealed ledger after unblinding and refuses on a mask-digest
   disagreement with BS-2f; and it requires a verified BS-L bound to the mask digest
   exactly as it requires BS-5f's. Both ride the next code revision, which the Stage-P
   blocker already forces.
5. **§10.** Record this §6 replacement in the repair trace; retire the V12/V13/V14
   correction blockquotes with the old §6.1 — §10 is the trace's home. Update the
   disclosed-open list: "the BS-L primary lock" becomes the atomic code revision this
   replacement requires (BS-2k/BS-L/BS-2f schemas, authenticated receipt fields,
   `verify_lock()`, the BS-L guard, the end-to-end fixture), open until gated.
6. **Code-side items in the same atomic revision** — listed for completeness, not claimed
   as text repairs: `SLOT_SCHEMA` entries for BS-L (body fields plus detached signature and
   signer identity), BS-2k, and the BS-2f checkpoint field; receipts that carry and
   authenticate their decoded fields, or consumers that decode and verify the canonical
   body, with post-envelope control fields rejected (GPT56-V14 3); `verify_lock()`;
   `recompute_acceptance_ledger`; the end-to-end refusal fixture BS-2f + BS-8f → BS-5f →
   BS-L → unblinding → BS-7f → BS-V with tamper tests at every edge; and a
   `prereg_lint.py` run on the integrated candidate. These are integration-time
   requirements stated here, not work this draft claims to have done — there is no
   integrated candidate to lint yet.

Already-owed repairs this draft does not touch and does not claim: §2.7's closing sentence
must agree with the table on BS-2f's class (KIMI-V14 F8); the (d)-threshold's single home
(KIMI-V14 F3); the dead fixture citations (F5); the z\* misquote in text and pinned
docstring (F6); the v7-subject disclosure (F7); F9–F12; the open Stage-P blocker.

---

# PART 3 — CHOICES THE FINDINGS DID NOT FORCE, AND THE ALTERNATIVE TO EACH

- **C1 — Custody provisioning became a slot (BS-2k), class P, DESIGN.** The first brief
  required an enumerated roster, a working log and a declared committee store; nothing
  named who builds any of it or when, and my round-4 answer-8 finding was that the
  covenant's entire subject matter came into existence off-stage. Alternatives: fold roster
  and log schema into BS-2a (rejected — dilutes acceptance design's gate and still names no
  store or key provenance); leave provisioning implicit (the V14 status quo; rejected).
  BS-2k being class P puts store, keys, roster and wrapper in existence before the freeze,
  which makes "roster named before any image byte" a consequence rather than a promise. In
  this revision BS-2k additionally carries the archive's seal-state receipt, Duho's signing
  public key, the mediator symbol and the unsealing construction (findings GPT56-2/5,
  CODEX-3) — same slot, more content; the alternative of scattering them across BS-2a and
  BS-8p was rejected because custody is one design and should be gated once.
- **C2 — BS-L moved to class E, preconditions = freeze-in-force + BS-5f.** This is
  GPT56-V14 2's and CODEX-V14 1's prescribed repair; the requirement forced the substance
  (no self-certifying set), not the class. Alternative: keep BS-L class P with an
  "except itself" clause (rejected — it stays blocked by a post-inference receipt while
  claiming to be a freeze prerequisite, the timing contradiction both seats named).
- **C3 — The committee labels and co-signs only its label-set receipt; Hwao alone produces
  BS-8f.** Alternative: restate the isolation bar so the committee may co-fill BS-8f
  (rejected — the one group that sees χ before unblinding would co-produce the record that
  sets the decision bands; KIMI-V14 F4(iii) option 1 and GPT56-V14 5's repair both point
  the way taken).
- **C4 — The log is receipted as chain checkpoints at BS-2f and at BS-L, and BS-L's
  checkpoint must demonstrably extend BS-2f's.** V14's sentence named both; KIMI-V14 F2(d)
  showed BS-2f's schema cannot hold it and offered either home; CODEX-3 requires the
  extension to be demonstrated, not merely renamed. Alternative: receipt at BS-L alone
  (rejected — loses the mid-execution checkpoint; the schema field and the segment ride an
  already-forced code revision).
- **C5 — The Disclosure clause now exempts exactly the permitted aggregate surface, and the
  same choice is stated in the scope, rows I/J, and here.** This is GPT56-1's first
  prescribed repair, taken. Alternative: its second — run the calibration computation and
  Stage C inside one sealed computation and let only BS-5f leave (rejected — restructures
  §4/§5 machinery four rounds have already closed, for a leak surface I judge sign-free;
  see R5). The finding was that the first draft's opening clause forbade what its scope
  permitted; the repair is that the clause, the scope, the rows and this choice now say one
  thing.
- **C6 — §6.1(6) states the checkable sentence and names the retrospective question open.**
  Alternatives: keep V14's "establishes" verb (rejected — violates this document's own
  "no claim stronger than its check"; KIMI-V14 F11 / GPT56-V12 F4); write a class-P
  retrospective-custody receipt into this draft (declined — whether predecessor-store logs
  or participant attestations exist is a fact I cannot verify from this seat, and under
  CODEX-V14 6's own formulation an unlogged interval voids reuse of the redesign. A
  drafting seat should not enact a study-ending consequence on an unverified premise; the
  principal holds both the fact and the decision. Named in §6.1 clause 6 and R2, not
  silently dropped).
- **C7 — A §6-internal precedence sentence (clause 5's final sentence) declares the table
  and the void jointly satisfiable and any contrary reading a text defect.** Alternative:
  rely on cross-section prose consistency (the failure mode the first brief cites as the
  reason this draft exists).
- **C8 — The V12/V13/V14 repair blockquotes are not carried into the replacement.** §10
  holds the trace. Alternative: carry them (rejected — the covenant must read as law, not
  as its own history; two of those blockquotes claimed repairs that did not land).
- **C9 — Rows F and J are in the table although their read surfaces are χ-free, and rows A,
  B and O are in the table because the store machinery must be inside the closed world** —
  the provisioner predates any χ, the mediator touches sealed bytes only as another row's
  conduit, and the unsealing service runs only after the lock, but all three can touch the
  sealed stores' machinery and GPT56-2/CODEX-3 found them missing. The default-forbidden
  rule makes the table the complete pre-lock set of processes that touch χ-bearing objects
  or the sealed stores' machinery; completeness is the property the brief asked to be
  checkable. Alternative: list only χ-touching processes (rejected — the bin-sealing and
  Stage-C computations would then be forbidden by the default, and the store machinery
  would exist off-table).
- **C10 — The surviving non-blinding §6 bullets are carried unchanged into §6.3.**
  Alternative: re-home them to §5/§10 (rejected — reorganizing other sections is outside a
  §6 replacement's scope, and silent loss of a carried clause is exactly the defect class
  under repair).
- **C11 — The closed-world default is scoped to touches of χ-bearing objects, not to every
  pre-lock process.** This is GPT56-2's prescribed repair, and it reconciles the brief's
  constraint ("the table is the normative object; anything not in it is forbidden by
  default") with the blocker: under an all-process reading, "anything" forbids the
  covenant's own machinery, so the constraint's "anything" must read as "any χ-bearing
  touch" — and the table plus clause 1 keep the default universal over exactly that.
  Alternative: keep the all-process default and add rows for every support process
  (rejected — the support set is uncompletable: transport, schedulers, gates, verifiers;
  the covenant's object is outcome knowledge, not process hygiene). χ-free processes remain
  outside only because the table preamble's sentence says so, as the finding required.
- **C12 — Non-χ-bearing is defined by a closed list of authenticated schemas; the
  categorical "receipts, digests, logs and fixtures are not χ-bearing" is deleted.** This
  is CODEX-1's prescribed repair. Alternative: declare per-object execution receipts
  non-χ-bearing so Hwao and gates can audit them live (rejected — it recreates an access
  carve-out through object naming instead of role naming; Hwao's audit needs are served by
  checkpoint digests pre-lock and by the recompute's re-invocation post-unblinding).
- **C13 — `recompute_acceptance_ledger` is named as the BS-2a-pinned callable, with the
  post-unblinding re-invocation required of the verdict path.** This is GPT56-4's
  prescribed repair. Alternative: leave the callable's name to BS-2a (rejected — the
  finding was that no producer was named and the only named home sat on the post-unblinding
  path; the name is a requirement binding BS-2a's receipt, not a claim the symbol exists
  today — the same discipline as the requirement-5 refinement in Part 5).
- **C14 — The BS-L signature is detached Ed25519 over the canonical body digest, under
  Duho's personal key bound at BS-2k, with `verify_lock()` the pinned verifier.** This is
  GPT56-5's prescribed construction. Alternative: leave algorithm and key identity to the
  future BS-2k design (rejected — the finding was that "signature" named nothing signable
  or verifiable; the construction must be in the text. Substituting a different scheme
  afterward is a gated amendment, exactly as for any frozen constant).
- **C15 — The archive is governed by receipted seal state, not by binding it behind the
  mediator.** CODEX-3 offered both; I take its second option. Alternative: extend BS-2k to
  bind the archive behind the same wrapper (declined — from this seat I cannot verify that
  an enforceable wrapper can be attached to a store no row may read, and no row needs to
  read it. A seal-state receipt is checkable at every checkpoint; a wrapper-attachment
  claim is not. If the principal knows the archive can be wrapped, BS-2k's gate is where
  that evidence belongs, and the table needs no change — the archive still has no reader
  row).
- **C16 — The receipt column is split into "authorized by" and "emits".** This is CODEX-2's
  prescribed repair. Alternative: keep one column and define "under" to mean "authorized
  by" (rejected — the emission half then sinks back into prose, and the finding was the
  conflation, not the word).

---

# PART 4 — RESIDUAL RISKS THIS DRAFT CARRIES

Named as plainly as I named the principal's, per the brief.

- **R1 — Detection stops at the wrapper's physics.** The covenant detects looks that flow
  through the mediator. A key holder with raw storage access reads without an event and
  nothing shows it. Clause 4 forces BS-2k to state that boundary and name the risk holder;
  below the boundary the covenant is attestation, not detection. This was KIMI-V12 F3's
  tail and KIMI-V14 Q5's answer; this draft does not close it and no prose can.
- **R2 — The retrospective window is open.** The redesign predates this covenant. Clause 6
  states what is checkable and stops; whether anyone read predecessor χ before the geometry
  artifacts were fixed is established by nothing here, and the archive's seal-state
  receipts are prospective only — they bind the archive from BS-2k forward, not before.
  CODEX-V14 6 stands open against this draft exactly as it stood against V14; its remedy
  is the principal's decision (C6).
- **R3 — Executability rides the next code revision, and this revision says so as a
  condition, not a hope.** BS-L and BS-2k schemas, BS-2f's checkpoint field, the BS-L guard
  on the verdict path, authenticated receipt-field consumption, `verify_lock()`,
  `recompute_acceptance_ledger`, and the end-to-end fixture do not exist in the pinned v9
  bytes. Clause 3(d) makes the §6 replacement, the Part 2 seams and that code one atomic
  candidate revision — which closes the "prose defect, code wins" failure CODEX-4 named,
  but only by refusing to let any of it be conforming alone. Until the revision lands and
  is gated, conduct prose has no arbiter, and the table now binds more future symbols than
  the first draft did (BS-2k's mediator and unsealing, BS-2a's callable, BS-9's runners,
  BS-8p's interface and reducer); every one is a place the future work can drift from this
  text. The mitigation is the refusal-to-fabricate discipline: each such process is
  forbidden before its pin exists.
- **R4 — The committee is a designed human hole.** N named people see χ-bearing cutouts
  before the lock because BS-8f cannot exist otherwise. The draft binds their roles,
  sample, interface, logging and exports; it cannot bind memory, and collusion or leakage
  through a channel outside the interface is undetectable by anything in this text. The
  mitigation is procedural; the residual is real.
- **R5 — The aggregate export is a judgment call, and I am the one who made it.** C5
  declares the BS-8f per-bin aggregates sign-free with respect to the tested question. If a
  referee shows an information path from {â_b, σ_ab, a_LB_b, ε̂, Cov_a} to the answer, the
  repair is a redesign of Stage C's pre-unblinding power check, not a rewording of §6.
- **R6 — The default-forbidden rule still has no emergency lane for χ-bearing touches.** A
  future pre-lock process that must touch a sealed store — a retry worker re-entering the
  store, a recovery tool — is forbidden until added by gated amendment. The narrowed
  default (C11) relieves the pressure for χ-free support work, which no longer needs the
  table's leave to exist; it relieves nothing for χ-bearing touches, and that is the point.
  It is also a pressure toward improvisation at the first production failure, and this
  draft offers no answer to that pressure beyond the void rule.
- **R7 — BS-2k delegates the hard part, and this revision loads more onto it.** Key
  generation, split, escrow, destruction, wrapper enforcement, the signing keypair, the
  unsealing construction, and the archive's seal state are a DESIGN slot: this draft
  requires them to exist and be gated; it does not design them. A weak custody design
  honestly receipted at BS-2k satisfies the letter of this text.
- **R8 — The rest of the document's debt stands.** F3, F5–F12 and the open Stage-P blocker
  are untouched by this draft (Part 2 lists the seams it does conform). A §6 that passes
  its referee round does not make the document freezeable, and nothing in this draft should
  be quoted as claiming otherwise.
- **R9 — One seat drafted this against its own four reports and its own first draft.** The
  brief inverted the roles because the principal's repair rate in this prose had fallen
  below their defect-introduction rate. Nothing about my seat exempts me from the same
  arithmetic — the first draft's nine blockers are the arithmetic. The table form is the
  mitigation — completeness and consistency are checkable column-wise rather than by
  cross-referencing paragraphs — not the cure. The cure is the two referee seats reading
  this as a fresh subject.

---

# PART 5 — THE REQUIREMENTS AND THE FINDINGS, WHERE EACH LANDS

## The first brief's seven requirements

1. **Ban access, not merely disclosure** → §6.1 clause 1 plus the default-forbidden rule in
   the table preamble; disclosure remains a separate, kept clause at §6's head.
   Implemented.
2. **The ban must not be role-scoped** → clause 1 binds every person and process by name
   class (Duho, Hwao, key holders, committee outside row G, all processes); rows K–Q make
   the universality concrete; "holding a key is custody, never licence". Implemented.
3. **The exceptions must exist and must not be voided by the ban** → table rows A–J
   enumerate them, including the calibration computation (row I) and the label-ingestion
   writer (row H) that CODEX-V14 4 and KIMI-V14 F4(ii) found omitted, and now also the
   custody machinery (rows A, B, O); clause 5 states that access inside a row does not void
   and that a contrary reading is a text defect, not an operator discretion. Implemented.
4. **The lock must be executable and receiptable** → clause 3: BS-L is class E and
   certifies no set containing itself (GPT56-V14 2 / CODEX-V14 1); its artifact is a
   canonical body with a detached signature, named field-by-field; BS-V is verdict-only;
   the sequence BS-5f → BS-L → unblinding → BS-7f → BS-V has a named producer at every
   step; the receipt-authenticity requirement (GPT56-V14 3) is stated at text level with
   its code repair flagged. Implemented at text level; its code half is an atomicity
   condition, not a claim (R3).
5. **The automation set must be complete and each member identified by the pinned code
   symbol** → clause 2 and the table's identity column. **Refinement, stated rather than
   silently complied with (unchanged from the first draft, and the brief's R2 text records
   the principal accepting it):** for rows B, C, D, E, H and O — and the BS-8p interface
   that row G's views run through — the implementing symbol is
   future BS-2k/BS-9/BS-2a/BS-8p work, so a pin quotable today does not exist; the draft
   names the slot whose receipt pins the symbol and digest and forbids the process to run
   before that pin exists — the repair KIMI-V14 F4 prescribed ("where the implementation is
   future BS-3/BS-9 work, say so instead of claiming a pin"). Clause 2 now also names the
   symbols that DO exist in the pinned v9 bytes, so the two sets cannot be conflated. If
   the requirement intends every symbol pinned in today's bytes, it is unsatisfiable until
   the BS-2k/BS-9/BS-2a/BS-8p work lands, and I flag that rather than fabricate pins.
6. **Every actor is enumerated** → rows G–I name the committee, its members' source of
   authority (BS-8p), its sealed store, its isolation (no other role; labels and a
   co-signed label-set receipt only), and where its χ-derived labels live (the committee
   sealed store; only the BS-8f aggregates leave, via row I). Rows K–Q cover holders, Duho,
   Hwao, the lock ceremony, the unsealing service, the verdict path, and the default.
   Implemented.
7. **Violation must be detectable, not merely forbidden** → clause 4: append-only chained
   log over both new stores, checkpoints receipted at BS-2f and BS-L with the extension
   demonstrated, absence or gap itself a failure, the checkable sentence, and the honest
   completeness boundary (R1); the archive by seal-state checkpoints (§6.2). Implemented.

No requirement was judged wrong. The refinement under (5) remains the only place this draft
departs from the first brief's literal wording, and it departs toward the finding the brief
cites for that requirement, not away from it.

## The nine blockers and the major, disposition of each

I verified each finding against the pinned v9 bytes and V15 before accepting it. All ten
are accepted. None of the prescribed repairs required refusal on the brief's two protected
grounds — none reintroduces role-scoping (the ban and the default stay universal over
χ-bearing touches) and none makes an authorised act void the run (clause 5's
jointly-satisfiable sentence is intact, and the two-column repair strengthens it by
removing the reading under which a row's own emission was its missing precondition).

1. **GPT56-1 (Disclosure forbids the BS-8f export) — accepted.** The Disclosure clause now
   exempts exactly the permitted aggregate surface and names its only export paths; the
   same choice is stated in the scope, rows I/J (the first draft's G/H), and C5, as the
   repair demanded.
2. **GPT56-2 (the default forbids the covenant's own machinery) — accepted.** The default
   is scoped to χ-bearing touches (table preamble, clause 2); rows A (provisioner), B
   (mediator) and O (unsealing) were added; χ-free transport, gates and receipt
   verification remain outside only because the preamble's sentence says so (C11).
3. **GPT56-3 (execution receipts classified both ways) — accepted.** Same defect as
   CODEX-1; repaired there. Row E's surface now lists the evidence fields as the χ-bearing
   material that row alone may read; row M's surface is the closed list.
4. **GPT56-4 (row C had no named pre-BS-2f producer) — accepted.** Row E names
   `recompute_acceptance_ledger`, pinned at BS-2a, running at P2–P3; the verdict path
   re-invokes it post-unblinding and refuses on a mask-digest disagreement; Part 2 item 4
   carries the §2.7(4) and §5 seams. Verified first: v9 `run_production_verdict()` (lines
   1591–1605) has no evidence argument and no recompute call, and §2.7(4)'s "or a validator
   it calls" does place the check on the post-unblinding path.
5. **GPT56-5 (BS-L's "signature" named nothing signable) — accepted.** Clause 3(b)/(c)
   defines the canonical body, the detached Ed25519 signature over its digest, the
   BS-2k-bound key, the signer identity in the outer artifact, and `verify_lock()` called
   by both unblinding and the verdict path, with the full refusal list. Verified first:
   v9 `receipt()` (lines 208–224) returns hashes only — no signature, no retained field
   values.
6. **CODEX-1 (categorical receipt/log exemption recreates a carve-out by object naming) —
   accepted.** The categorical sentence is deleted; the scope now defines non-χ-bearing by
   a closed list of authenticated schemas and states the χ-bearing-by-default rule for
   anything unlisted, any opaque digest of χ-bearing bytes, and any schema permitting
   outcome payloads; rows D, E, M and the gate-witness sentence are reconciled to it (C12).
7. **CODEX-2 ("under which receipt" self-dependent) — accepted.** The column is split into
   "authorized by" and "emits"; the preamble states the act/audit rule and that no row's
   authorization is its own emission; the hand-check path is stated in the finding's own
   order (C16).
8. **CODEX-3 (detection machinery missing; archive not operationally covered) — accepted,
   taking the finding's second option for the archive.** Rows B and O name the mediator and
   the unsealing service with inputs, outputs, event schema, refusal behavior and emitted
   checkpoints; BS-2k binds all three stores — the two new ones by provisioning, the
   archive by identity, holder roster and receipted seal state (C15 records why not the
   first option); BS-L binds the final checkpoint together with the segment demonstrating
   it extends BS-2f's (clause 3(b)).
9. **CODEX-4 (clause 3(d) wrongly denied §0's reach) — accepted.** The non-reach sentence
   is struck. Clause 3(d) now states that §0's enumeration (run guards, digest
   serializations — V15 lines 40–73, re-read for this revision) reaches the BS-L schema,
   envelope verification and the guard, and makes the whole replacement plus Part 2 plus
   the code items one atomic candidate revision, with `prereg_lint.py` and the end-to-end
   refusal fixture as integration-time validation. Verified first: §0 does enumerate "the
   run guards, and all digest serializations".
10. **CODEX-major (rows E and F did not define one closed label path) — accepted.** One
    write path: row G submits labels only through the BS-8p interface; row H is the
    committee store's sole writer; intermediate persistence is forbidden on both rows; row
    H emits the completed label-set receipt over the sealed label-set digest, the view-log
    range, the allocation digest and the member co-signatures.

— KIMI, 2026-08-27. Second-pass draft; not in force; referees are GPT56 and CODEX.
