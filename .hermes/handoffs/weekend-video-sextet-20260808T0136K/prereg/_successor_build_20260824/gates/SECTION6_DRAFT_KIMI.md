# §6 DRAFT — KIMI SEAT, 2026-08-27

Status: DRAFT FOR REFEREE. Written under `BRIEF_DRAFT_SECTION6.md`. Referees: GPT56 and
CODEX. Principal reviews before anything enters the document. This file modifies nothing;
`../PREREG_SUCCESSOR_DRAFT_V14_20260827.md` is untouched. Part 1 is the complete replacement
§6, written to drop in. Part 2 lists the conforming edits outside §6 that dropping it in
requires. Part 3 states every choice the brief's requirements did not force, with its
alternative. Part 4 names the residual risks this draft itself carries. Part 5 maps the
brief's seven requirements to where they land, and says where I read a requirement as
unforceable as literally stated.

---

# PART 1 — THE REPLACEMENT §6

## §6 Conduct

- **Disclosure.** Nothing derived from any real χ value — value, sign, summary, label, or
  count of signs — is published, spoken, or written outside the sealed stores defined in
  §6.1 before the primary lock; after unblinding, disclosure waits for BS-V (§7). The
  predecessor's §4/condition-2 breach is why this clause exists. What binds *access* is
  §6.1, and §6.1 is the normative object of this section.

### §6.1 The blinding covenant — one lifecycle table, and the table is normative

**Scope — what is χ-bearing.** A *χ-bearing object* is: any cutout produced for this run;
any per-object instrument output (χ value, sign, amplitude, confidence, execution receipt);
any per-object hand-check label or per-object human–instrument agreement; any derivative of
these that is not on the permitted aggregate surface below; and **the predecessor's sealed
archive of 208,405 χ measurements** (§6.2), which is outcome knowledge on overlapping sky
and is covered by every clause of this covenant exactly as this run's store is. The
*permitted aggregate surface* — χ-derived but defined as not χ-bearing — is exactly: the
BS-2f mask fields (brickid, objid, position, acceptance flag, calibration-bin label,
boundaries, digests — never a χ sign), and the BS-8f aggregate record (â, σ_a, a_LB, the
per-bin {â_b, σ_ab, a_LB_b}, ε̂, and the full Cov_a — aggregates over the hand-check sample,
never a per-object value). Receipts, digests, logs and fixtures are not χ-bearing. Anything
not listed here is χ-bearing if a reasonable reader could extract outcome information from
it; doubt resolves toward χ-bearing.

**The two sealed stores.** The *main sealed store* holds cutouts, instrument outputs and the
acceptance ledger. The *committee sealed store* holds the hand-check labels. Both are
provisioned at **BS-2k** (custody design: store identities, key generation/split/escrow,
the key-holder roster, the logging wrapper, and the access-log schema) — a class-P DESIGN
slot, so both stores, all keys and the roster exist before the freeze, hence before any
image byte. Gates and referees are external witnesses: their inputs are receipts, digests
and fixtures only, and no gate input is χ-bearing.

**The phase line.** P0 freeze (every class-P slot receipted, gates passed, Duho's freeze
signature) → P1 BS-6, first image byte → P2 cutout production and instrument inference →
P3 BS-2f → P4 BS-8f → P5 BS-5f → P6 BS-L, **the primary lock** → P7 unblinding →
P8 BS-7f and BS-V → P9 disclosure. BS-5f blocks BS-L; BS-L blocks unblinding; BS-V follows
unblinding and is the verdict receipt, never the lock.

**THE TABLE.** Each row is one permitted actor or process. **Any person or process not in
this table, and any act outside a row's stated surface, is forbidden by default** — that is
what makes completeness checkable by reading one column.

| # | actor / process — identity | may touch (read → write) | when | under which receipt | what voids the run |
|---|---|---|---|---|---|
| A | **Cutout producer** — the BS-9 production runner; symbol and digest pinned at BS-9 (future work; may not run until BS-9 is filled) | reads release image bytes → writes cutouts into the main sealed store; never reads any sealed object | P1–P2, after BS-6 | BS-6 + the producer checksum list (§2.5) | any cutout or derivative outside the store; any human view of a cutout outside row E's interface |
| B | **Instrument runner** — the BS-9 gated runner executing BS-3's pinned instrument identity (weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry) | reads cutouts in the store → writes per-object χ, confidence and execution receipts into the store only | P2, after row A, before BS-2f | the per-object measurement receipts (one per parent object; completeness is what `require_complete_sample()` later checks) | any χ-derived value emitted outside the store |
| C | **Acceptance-ledger recompute** — `run_production_verdict`'s mandatory pre-verdict validator; validator code pinned at BS-2a (DESIGN) | reads ledger evidence only — expected/actual cutout checksums and shapes, execution receipts, finite-output flags, frozen confidence values; **never a χ sign, amplitude, or axis-relative position** (§2.7(3): sign-blind by construction) → writes the realised partition | P2–P3, after complete inference, before BS-2f | BS-2f | reading any χ sign or amplitude; any exclusion reason outside §2.7(2)(a)–(d); any status, reason or evidence the recompute disagrees with |
| D | **Calibration-bin sealing** — `calibration_bins()`, `assign_bins()`, `allocate_handcheck()` (pinned symbols) | reads positions and acceptance flags only (χ-free) → writes sealed boundaries, bin labels, and the hand-check allocation | allocation plan pinned pre-freeze at BS-8p; boundaries sealed and labels assigned at P3, at BS-2f | BS-8p (plan); BS-2f (sealed boundaries) | any χ-bearing input to bin construction |
| E | **Hand-check committee** — members named at BS-8p; **no member holds any other role in this study**, and no member fills, adjudicates or locks any slot other than co-signing their own label-set receipt | views χ-bearing cutouts **of the allocated sample only**, through the BS-8p sealed interface → writes labels into the committee sealed store only | after BS-8p and after the sample's cutouts exist; complete before BS-8f | the label-set receipt (schema pinned at BS-8p); every view logged | a member holding any other role; any label, tally, description or impression exported by a member outside the sealed interface; any view of an object outside the allocated sample; any unlogged view |
| F | **Label-ingestion writer** — the interface pinned at BS-8p | reads the committee's labels → writes them into the committee sealed store; emits nothing outside it | with row E | the label-set receipt | any write path outside the pinned interface |
| G | **Calibration computation** — `accuracy_from_handcheck()` (pinned symbol) | reads the committee label set and the corresponding instrument outputs, inside the stores → writes **only** the BS-8f aggregate fields | P4, after the label-set receipt, before BS-8f | BS-8f | any per-object label, sign or agreement leaving the stores; any field beyond the BS-8f schema |
| H | **Stage-C runner** — `stage_power` with `inject_signs` (pinned symbols; frozen generator, addresses, pass rule) | reads the sealed BS-2f mask (χ-free) and the BS-8f aggregates; injects synthetic signs only — **never reads a real χ** → writes the Stage-C receipt | P5, after BS-2f and BS-8f, before BS-L | BS-5f | reading any real χ; continuing the run after a Stage-C FAIL (INCONCLUSIVE-BY-POWER halts the run; no real-sky statistic is formed) |
| I | **Key holders** — roster designated at BS-2k before the freeze; roster digest bound into BS-L | touch nothing before the lock; custody exists for the lock ceremony and later audit only — **holding a key is custody, never licence** | — | BS-2k (designation); BS-L (binding) | any pre-lock read by any holder, authorised or not |
| J | **Duho** | signs the freeze; designates holders at BS-2k; signs BS-L reading its digest fields only; opens the lock by signature after BS-L exists, the opening recorded in the log | P0, P6, P7 | the freeze signature; BS-L | any pre-lock access to a χ-bearing object; opening the lock before BS-L exists |
| K | **Hwao** — producer of record for the slots | reads receipts, digests and χ-free artifacts → writes the slot receipts §7 assigns | throughout | the slots' receipts | any pre-lock access to a χ-bearing object |
| L | **The lock ceremony** — producer: Duho | reads the digests BS-L binds → writes the BS-L receipt and its log entries | P6, after BS-5f, before unblinding | BS-L | a BS-L receipt missing any schema field; a lock with no log |
| M | **Verdict path** — `run_production_verdict()` (pinned symbol) | **post-unblinding only**: reads the real χ vector joined to the accepted mask → writes the permutation record and the verdict | P8, after unblinding | BS-7f, then BS-V | any execution before unblinding — see clause 3(d) |
| N | **Every other person and every other process** | nothing χ-bearing before unblinding; the default is forbidden | — | — | any access |

Synthetic exploration (`explore_verdict()` on a `FixtureMask`) touches no sealed object and
is unrestricted; the §3 type boundary — production entry points call `require_sealed()` and
refuse a fixture by type, and the reverse — is what makes this sentence true.

**Clauses.**

1. **The ban is universal and binds access, not merely disclosure.** No person and no
   process may decrypt, query, render, summarise or inspect any χ-bearing object or
   derivative before unblinding, except within a table row's stated surface. The ban names
   no roles because it has none: it binds Duho, Hwao, every key holder, every committee
   member outside row E's surface, and every process alike. No authorisation other than the
   table's exists; claimed authority is no defence for access outside it, and there is no
   logged-and-therefore-permitted read.

2. **The exceptions are the table's rows, or they do not exist.** A process not in the
   table may not run before the lock. Each automation row is identified by the pinned code
   symbol that implements it; where the implementation is future work (rows A, B, C, F),
   the row names the class-P or gated slot — BS-9, BS-2a, BS-8p — whose receipt pins the
   symbol and digest, and **the process may not run before that pin exists**. A row run
   under a symbol or digest that disagrees with its pin is access outside the table.

3. **The primary lock (BS-L) is executable and receiptable.**
   (a) *Class and preconditions.* BS-L is a **class-E** slot. Its preconditions are: the
   freeze is in force (every class-P slot receipted — §7's class-P set, which does not and
   cannot include BS-L — gates passed, Duho's freeze signature), and BS-5f's Stage-C
   receipt exists. BS-L certifies no set containing itself.
   (b) *Schema.* The BS-L receipt names exactly: the roster digest (from BS-2k), the
   accepted-mask digest (BS-2f), the calibration-record digest (BS-8f), the Stage-C receipt
   digest (BS-5f), the decision-input digests (the §0 code digest and the frozen decision
   constants it carries), the access-log digest, the environment record, and Duho's lock
   signature. This field set enters the pinned `SLOT_SCHEMA` at the next code revision
   (already forced by the Stage-P blocker); until then no conforming BS-L receipt can be
   emitted and this clause forbids what the code cannot yet produce.
   (c) *Sequence and producers.* The sequence BS-5f → BS-L → unblinding → BS-V is recorded
   through named producers: Hwao produces BS-5f via row H; **Duho produces and signs BS-L**
   and performs the logged unblinding; Hwao produces BS-7f and BS-V via row M. BS-V is the
   verdict receipt only; it carries no lock field, seals nothing, and is never the lock.
   (d) *The gate on the only verdict path.* The production runner must require a BS-L
   receipt bound to the mask digest exactly as it requires BS-5f's; that guard enters at
   the same code revision as (b). Until the code carries it, row M's void stands in prose:
   conduct text forbids what the code cannot yet refuse, and §0's code-precedence rule does
   not reach this section.
   (e) *Receipt authenticity.* A receipt is evidence only as produced by the pinned
   `receipt()` and verified against its pinned schema; a control field asserted outside the
   authenticated envelope is not evidence of anything. The consumer-side verification this
   requires is part of the same code revision.

4. **Access is logged or it did not happen.** An append-only access log covers both sealed
   stores and the predecessor archive; every decryption, query, render and read against
   them — successful or refused — appends an entry at the time of the touch. Its digest is
   receipted at BS-2f and again at BS-L. **The absence of the log, any gap in it, or a
   missing receipt of its digest is itself a failure: a lock with no log is a lock that
   failed.** The checkable sentence is: **no χ-derived artifact exists outside the sealed
   stores before the primary lock.** Completeness: BS-2k's design must provision the stores
   so that every access flows through the logging wrapper, must state the technical
   boundary below which access outside the wrapper is physically possible, and must name
   who holds the risk below that boundary. What the log records is visible; what bypasses
   the wrapper is the residual risk BS-2k is required to state, not allowed to hide.

5. **The void rule.** Any pre-lock access outside the table voids the run — authorised or
   not, disclosed or not, and whether or not the accessor believed it harmless. Access
   inside a table row, within its stated surface and under its stated receipt, is the run
   proceeding as designed and does not void it. The committee's mandated view (row E) and
   the named processes' mandated touches (rows A–D, F–H) are inside the table; this clause
   and clause 1 are written to be jointly satisfiable, and a reading under which the table
   authorizes an act that this clause voids is a defect in this text, not a discretion
   available to any operator.

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
The archive is retained as historical record; it is a χ-bearing store under §6.1's table,
log and void rule exactly as this run's store is, and it is not an input. Reuse would
require a new text, a new gate and a new signature, because the reuse contract and its
blinding safeguards do not exist here.

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

The four-round failure mode named in the brief is clauses contradicting each other across
650 lines. This replacement is written so §6 needs no arbitration, but five seams outside
§6 must be conformed in the same revision or the contradiction returns:

1. **§7 class-P table.** Remove the BS-L row (BS-L becomes class E). Add **BS-2k** (class
   P, DESIGN; producer Hwao, holders designated by Duho; content: sealed-store identities,
   key generation/split/escrow, key-holder roster, logging wrapper, access-log schema;
   blocks BS-6). Regenerate the classification sentence from the table: fourteen class-P
   slots, one filled (BS-2m); DESIGN slots are BS-2a, BS-2k, BS-5p, BS-8p and BS-9.
2. **§7 class-E table.** Add the BS-L row (producer Duho; content per §6.1 clause 3(b);
   blocked by BS-5f and the freeze; blocks unblinding). BS-V's content becomes "verdict"
   only — strike "+ primary lock". BS-8f's producer becomes "Hwao, from the hand-check
   committee's sealed label set" (the committee co-signs the label-set receipt, not the
   slot). BS-8p's content gains: the committee declaration — members, their sealed store,
   the sealed interface, the label schema and the label-set receipt schema.
3. **§7 BS-2f row and the pinned `SLOT_SCHEMA`** (next code revision): the access-log
   digest field joins BS-2f's schema.
4. **§10.** Strike "the BS-V primary lock" from the disclosed-open list; record this §6
   replacement in the repair trace. The V12/V13/V14 correction blockquotes inside the old
   §6.1 are retired with it — §10 is the trace's home.
5. **§5 guard list.** Add that `run_production_verdict()` requires a BS-L receipt bound to
   the mask digest exactly as it requires BS-5f's — flagged as riding the next code
   revision, which the Stage-P blocker already forces. Code-side items in the same
   revision, listed for completeness, not claimed as text repairs: `SLOT_SCHEMA` entries
   for BS-L and BS-2k; consumer-side envelope verification and rejection of post-envelope
   control fields (GPT56-V14 3).

Already-owed repairs this draft does not touch and does not claim: §2.7's closing sentence
must agree with the table on BS-2f's class (KIMI-V14 F8); the (d)-threshold's single home
(KIMI-V14 F3); the dead fixture citations (F5); the z\* misquote in text and pinned
docstring (F6); the v7-subject disclosure (F7); F9–F12; the open Stage-P blocker.

---

# PART 3 — CHOICES THE REQUIREMENTS DID NOT FORCE, AND THE ALTERNATIVE TO EACH

- **C1 — Custody provisioning became a slot (BS-2k), class P, DESIGN.** The brief required
  an enumerated roster, a working log and a declared committee store; nothing named who
  builds any of it or when, and my round-4 answer-8 finding was that the covenant's entire
  subject matter came into existence off-stage. Alternatives: fold roster and log schema
  into BS-2a (rejected — dilutes acceptance design's gate and still names no store or key
  provenance); leave provisioning implicit (the V14 status quo; rejected). BS-2k being
  class P puts store, keys, roster and wrapper in existence before the freeze, which makes
  "roster named before any image byte" a consequence rather than a promise.
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
- **C4 — The log digest is receipted at both BS-2f and BS-L.** V14's sentence named both;
  KIMI-V14 F2(d) showed BS-2f's schema cannot hold it and offered either home.
  Alternative: receipt at BS-L alone (rejected — loses the mid-execution receipt point;
  the schema field rides an already-forced code revision, so the cost is one field).
- **C5 — The BS-8f aggregate record is defined as the only permitted pre-lock χ-derived
  export.** Stage C needs a_LB and the decision bands evaluate at â before unblinding, so
  some aggregate surface must exist. Alternative: forbid even aggregates and move Stage
  C's calibration input inside a sealed computation (rejected — restructures §4/§5
  machinery four rounds have already closed, for a leak surface I judge sign-free; see
  R5).
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
  rely on cross-section prose consistency (the failure mode the brief cites as the reason
  this draft exists).
- **C8 — The V12/V13/V14 repair blockquotes are not carried into the replacement.** §10
  holds the trace. Alternative: carry them (rejected — the covenant must read as law, not
  as its own history; two of those blockquotes claimed repairs that did not land).
- **C9 — Rows D and H are in the table although their read surfaces are χ-free.** The
  default-forbidden rule makes the table the complete pre-lock process set, not only the
  χ-touching subset; completeness is the property the brief asked to be checkable.
  Alternative: list only χ-touching processes (rejected — "a process not on this list may
  not run before the lock" would then forbid the bin-sealing and Stage-C computations the
  run requires).
- **C10 — The surviving non-blinding §6 bullets are carried unchanged into §6.3.**
  Alternative: re-home them to §5/§10 (rejected — reorganizing other sections is outside a
  §6 replacement's scope, and silent loss of a carried clause is exactly the defect class
  under repair).

---

# PART 4 — RESIDUAL RISKS THIS DRAFT CARRIES

Named as plainly as I named the principal's, per the brief.

- **R1 — Detection stops at the wrapper's physics.** The covenant detects looks that flow
  through the logging path. A key holder with raw storage access reads without an entry
  and nothing shows it. Clause 4 forces BS-2k to state that boundary and name the risk
  holder; below the boundary the covenant is attestation, not detection. This was
  KIMI-V12 F3's tail and KIMI-V14 Q5's answer; this draft does not close it and no prose
  can.
- **R2 — The retrospective window is open.** The redesign predates this covenant. Clause 6
  states what is checkable and stops; whether anyone read predecessor χ before the geometry
  artifacts were fixed is established by nothing here. CODEX-V14 6 stands open against this
  draft exactly as it stood against V14; its remedy is the principal's decision (C6).
- **R3 — Executability rides the next code revision.** BS-L and BS-2k schemas, BS-2f's log
  field, the BS-L guard on the verdict path, and consumer-side envelope verification do
  not exist in the pinned v9 bytes. Until that revision lands and is gated, §6 forbids in
  prose what the code cannot yet refuse — the same posture the document already takes for
  Stage P, with the same weakness: conduct prose has no arbiter, and clause 3(d) says so
  rather than hiding it.
- **R4 — The committee is a designed human hole.** N named people see χ-bearing cutouts
  before the lock because BS-8f cannot exist otherwise. The draft binds their roles,
  sample, interface, logging and exports; it cannot bind memory, and collusion or leakage
  through a channel outside the interface is undetectable by anything in this text. The
  mitigation is procedural; the residual is real.
- **R5 — The aggregate export is a judgment call, and I am the one who made it.** C5
  declares the BS-8f per-bin aggregates sign-free with respect to the tested question. If a
  referee shows an information path from {â_b, σ_ab, a_LB_b, ε̂, Cov_a} to the answer, the
  repair is a redesign of Stage C's pre-unblinding power check, not a rewording of §6.
- **R6 — The default-forbidden rule has no emergency lane.** A future pre-lock process — a
  retry worker, a transport-resume tool, a monitoring job — is forbidden until added by
  gated amendment. That is the point of the table. It is also a pressure toward
  improvisation at the first production failure, and this draft offers no answer to that
  pressure beyond the void rule.
- **R7 — BS-2k delegates the hard part.** Key generation, split, escrow, destruction and
  wrapper enforcement are a DESIGN slot: this draft requires them to exist and be gated;
  it does not design them. A weak custody design honestly receipted at BS-2k satisfies the
  letter of this text.
- **R8 — The rest of the document's debt stands.** F3, F5–F12 and the open Stage-P blocker
  are untouched by this draft (Part 2 lists the seams it does conform). A §6 that passes
  its referee round does not make the document freezeable, and nothing in this draft
  should be quoted as claiming otherwise.
- **R9 — One seat drafted this against its own four reports.** The brief inverted the
  roles because the principal's repair rate in this prose had fallen below their
  defect-introduction rate. Nothing about my seat exempts me from the same arithmetic. The
  table form is the mitigation — completeness and consistency are checkable column-wise
  rather than by cross-referencing paragraphs — not the cure. The cure is the two referee
  seats reading this as a fresh subject.

---

# PART 5 — THE BRIEF'S SEVEN REQUIREMENTS, WHERE EACH LANDS, AND ONE REFINEMENT

1. **Ban access, not merely disclosure** → §6.1 clause 1 plus the default-forbidden rule
   under the table; disclosure remains a separate, kept clause at §6's head. Implemented.
2. **The ban must not be role-scoped** → clause 1 binds every person and process by name
   class (Duho, Hwao, key holders, committee outside row E, all processes); rows I–N make
   the universality concrete; "holding a key is custody, never licence". Implemented.
3. **The exceptions must exist and must not be voided by the ban** → table rows A–H
   enumerate them, including the calibration computation (row G) and the label-ingestion
   writer (row F) that CODEX-V14 4 and KIMI-V14 F4(ii) found omitted; clause 5 states that
   access inside a row does not void and that a contrary reading is a text defect, not an
   operator discretion. Implemented.
4. **The lock must be executable and receiptable** → clause 3: BS-L is class E and
   certifies no set containing itself (GPT56-V14 2 / CODEX-V14 1); its schema is named
   field-by-field; BS-V is verdict-only; the sequence BS-5f → BS-L → unblinding → BS-V has
   a named producer at every step; the receipt-authenticity requirement (GPT56-V14 3) is
   stated at text level with its code repair flagged. Implemented at text level; its code
   half is flagged, not claimed (R3).
5. **The automation set must be complete and each member identified by the pinned code
   symbol** → clause 2 and the table's identity column. **Refinement, stated rather than
   silently complied with:** for rows A, B, C and F the implementing symbol is future
   BS-9/BS-2a/BS-8p work, so a pin quotable today does not exist; the draft names the slot
   whose receipt pins the symbol and digest and forbids the process to run before that pin
   exists — the repair KIMI-V14 F4 prescribed ("where the implementation is future
   BS-3/BS-9 work, say so instead of claiming a pin"). If the requirement intends every
   symbol pinned in today's bytes, it is unsatisfiable until the BS-3/BS-9 work lands, and
   I flag that rather than fabricate pins.
6. **Every actor is enumerated** → rows E–G name the committee, its members' source of
   authority (BS-8p), its sealed store, its isolation (no other role; labels and a co-signed
   label-set receipt only), and where its χ-derived labels live (the committee sealed
   store; only the BS-8f aggregates leave, via row G). Rows I–N cover holders, Duho, Hwao,
   the lock ceremony, the verdict path, and the default. Implemented.
7. **Violation must be detectable** → clause 4: append-only log over both stores and the
   predecessor archive, digest receipted at BS-2f and again at BS-L, absence or gap itself
   a failure, the checkable sentence, and the honest completeness boundary (R1).
   Implemented.

No requirement was judged wrong. The refinement under (5) is the only place this draft
departs from the brief's literal wording, and it departs toward the finding the brief cites
for that requirement, not away from it.

— KIMI, 2026-08-27. Draft; not in force; referees are GPT56 and CODEX.
