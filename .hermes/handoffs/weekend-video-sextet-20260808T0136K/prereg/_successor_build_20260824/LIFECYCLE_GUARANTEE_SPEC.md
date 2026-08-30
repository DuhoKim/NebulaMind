**STATUS: SPEC — the access-log lifecycle's guarantee, stated as invariants before any further
construction. Written at the THREE-FAILURE THRESHOLD (V67 F1/F2, V68 F1/F2, V69 F1/F2 — one object,
three consecutive rounds, a new corner each time), under the rule this lane wrote after the citation
check failed the same way: the third failure means stop patching, because the corners keep appearing
when the purpose was never stated. The draft's lifecycle text is now DERIVED from this file; a
conflict between them is a defect in the draft.**

# WHAT THE ACCESS-LOG LIFECYCLE GUARANTEES — invariants by crash window and by reader

## 0. Objects and definitions

- **TOUCH** — bytes leaving a sealed store, or landing in one. Two kinds of leaving: **CONVEYANCE**
  (bytes to another row's process) and **RENDER** (bytes to Row G's sealed interface for display —
  **the render's store effect is the conveyance-to-interface, a DISTINCT kind with its own
  store-qualified operation token, one event of one kind**; the human's perception is never an
  event, and the display itself is bounded by G6's session, not logged as a second touch —
  GPT56-V81 F3: wording that made a render event "assert conveyance" read as one event serving two
  kinds). One kind of landing: **WRITE**.
- **TOUCH COMMIT** — one atomic commit in the BS-2k transactional domain:
  `{store effect, its one event carrying the effect's true outcome, Row B's identifier binding}`.
- **REFUSAL COMMIT** — the same commit with no store effect: `{event, binding}`.
- **DELIVERY** — what happens to already-conveyed bytes after their commit (a row's process consuming
  them; a human perceiving a rendered frame). **Delivery is not a touch.**
- **READERS** — the four parties who consult the record: the **requester** (external), the
  **enumeration/BS-L verifiers** (read chain + checkpoint materials at gates), the **post-hoc
  auditor** (reads everything after the run), and **Row B itself on recovery** (reads its own
  committed bindings, never the chain — recomputing custody from the file being recovered is the
  hash-chains-launder-tampering shape).

## 1. The guarantees

| # | invariant | holds for |
|---|---|---|
| G1 | **No unlogged touch**: no bytes leave or land in a sealed store without a committed event | every touch kind |
| G2 | **No false event**: a touch event's outcome field is true of the store effect it records; **a refusal event truthfully records that a request was refused and NO store effect occurred — AND its reason token is true of the refusal: a request with no completed permission verdict may carry only `REFUSED-UNCLASSIFIED`, and any specific code asserts its condition was actually established** (GPT56-V71 F2: without this, a false specific code bypasses the catch-all enumeration entirely) — **and an ARRIVAL event is under this invariant too: it truthfully records RECEIPT — its identifying facts are those of one real request, appended before any processing of that request (extended over the arrival class, GPT56-V88 F1)** | every event |
| G3 | **One TOUCH event per touch** — and **the event classes PARTITION: every committed event is exactly one of an ARRIVAL event (§1c), one touch's event, or one refusal's event — no event is two of these and no event is none** (re-derived over the arrival class — GPT56-V88 F1: the pre-arrival form said every event is a touch's or a refusal's and no event is neither, which forbade the class the same sitting authorised; V70's lesson — an event partition must name ALL its classes, GPT56-V70 F1, CODEX-V70 F1 — applied to three) | every event |
| G4 | **No double decision**: one request never yields two DECISION events — a touch commit or a refusal commit — and, since the WRITE-AHEAD ARRIVAL RECEIPT was authorised as its own event class (principal ruling, 2026-08-30 10:46), a completed request carries exactly ONE arrival event and ONE decision event; this invariant counts decisions only. The pre-arrival form said two EVENTS bare, which condemned the arrival receipt the same sitting authorised — swept as a set with GPT56/CODEX-V87 F1. | every request |
| G6 | **A view is the display session of one render commit**: it ends at the first of position advance, interface clear, or any interruption of continuous display — visibility loss, blanking, occlusion, navigation away; duration alone does not multiply views, nothing displayed after an interruption is the same view, and commit↔session ownership is one-to-one — each render commit opens at most one session and every session is opened by exactly one commit | Row G only |
| G5 | **Render = touch.** Every render is its own touch with its own committed event. **Row G's *"any unlogged view"* void clause is a consumer of G5, not an exception to N1** | Row G only |

## 1b. Operations that are in NO cell because they are FORBIDDEN, not unmodelled

**Delete, truncate, and custody-relevant metadata mutation of a sealed object are not touch kinds —
they are forbidden operations** (GPT56-V71 F7 asked which cell they land in; the answer is none, on
purpose, and here is the purpose). No row's stated surface includes destroying or mutating a sealed
object, so **via Row B such a request is a REFUSAL COMMIT (`REFUSED-ROW-NOT-AUTHORISED` or
`REFUSED-OUTSIDE-STATED-SURFACE`)**, fully covered by the refusal invariants; **outside Row B it is a
bypass of the mediator — `VOID-5-FORBIDDEN-ACT` / digest deviation**, which the covenant already
claims at phase Any. **The commit domain does not model operations whose occurrence voids the run; it
refuses the request or the run dies.** An unmodelled-but-possible operation would be a spec hole; a
forbidden one is a wall.

## 1c. The ARRIVAL RECEIPT — the second event class, authorised by ruling (2026-08-30 10:46)

**Every request's ARRIVAL is durably logged BEFORE any processing begins** — a write-ahead event
carrying the request's identifying facts (row, operation, object identity, timestamp — and the AUTHENTICATED CLOCK PAIR `boot_epoch` + `monotonic_reading`, the durable start the §3b deadline is measured from), appended by
Row B on receipt. **This is a second event class, and it changes what the access log records: the
principal authorised exactly that.** What it buys: **no real request can vanish** — a request that
dies anywhere after arrival has its arrival event, so the crash-before-commit case is no longer
invisible; the pre-verdict death that N2 spent eleven revisions naming as a residue is now a logged
arrival with no terminal event, which recovery and the auditor can SEE and the deadline machinery
can close. An arrival event is not a touch and satisfies no touch invariant; a touch without a
preceding arrival is refused by the verifier as malformed history. **One ARRIVAL per request, appended exactly once at receipt by the single serialised writer; recovery resumes from the logged arrival and never re-appends it — a second arrival for one request is malformed history, refused the same way (GPT56-V88 F4's duplicate branch).** **THE RECEIPT TRANSITION (GPT56-V89 F2, CODEX-V89 F5 — "before any processing" needs a boundary, or a half-arrived request sits on an undefined side of it): a request EXISTS exactly when (1) its complete framed unit — length-prefixed and digest-closed under the BS-2k wire schema — has been fully read and decoded, and (2) its ARRIVAL event's framed unit is durably committed. Frame decode is part of RECEIPT, not processing; "processing" begins at authorisation. A truncated, malformed or partial frame is BY DEFINITION not a request — wire noise outside the lifecycle, in the only sense the log can speak — and a crash mid-arrival-append fails the event's digest closure and is no arrival. The no-vanish guarantee is scoped to completely framed, schema-decodable requests, and this sentence is that scoping.**

## 2. The non-guarantees, with equal weight

| # | non-guarantee | why it cannot be otherwise |
|---|---|---|
| N1 | **Delivery is outside the custody claim** — the event records the store effect, never the requester's receipt or the human's perception | the requester and the human are external to any commit domain; three orderings failed trying to include them |
| N2 | **RETIRED BY RULING (2026-08-30 10:46): the WRITE-AHEAD ARRIVAL RECEIPT makes every real request durably visible** — arrival is logged BEFORE any processing, as a second event class the principal explicitly authorised, so no request can vanish and the lifecycle promise becomes true instead of narrowed. Kept in the table as the record of what was a non-guarantee for eleven revisions | the second event class it needed WAS authorised (principal ruling, 2026-08-30 10:46) — this cell carried the impossibility for eleven revisions; the authorisation dissolved it, and the cell now records that resolution (GPT56-V88 F3, CODEX-V88 F2: the sweep retired the body and left this cell still refusing) |
| N3 | **The log can over-report delivery, never under-report a touch** | the safe direction for a custody log, consequence of G1 + N1 |

## 3. The invariant table — crash window × reader

**Windows (re-cut at V91 — the arrival class created a window the table did not have, GPT56-V90 F4):** W0 = before the arrival commit (the pre-arrival wire; §1c's receipt transition is the boundary) · W1 = after the arrival commit, before the decision commit (the PENDING span, §3b) · W2 = at a commit (empty by atomicity — no partial state exists, arrival and decision commits alike) · W3 = after the decision commit, before delivery · W4 = during delivery · W5 = after delivery.

| window | requester sees | verifier/auditor sees | Row B on recovery sees |
|---|---|---|---|
| W0 | nothing (no bytes ever left) | nothing — a request that dies before its arrival commit never entered the log's world (§1c scopes the guarantee to completely framed, receipted requests) | nothing — no arrival, no work item |
| W1 | nothing (no bytes ever left) | **the ARRIVAL event (§1c)** — visible with no terminal event: the named PENDING state (§3b), which the deadline machinery closes; its invariant is exactly-one-terminal's existence half | the arrival is the work item; recovery resumes it to ONE decision, no second arrival |
| W2 | — | — | — (atomic: no such window) |
| W3 | nothing yet | a TRUE event: the effect happened | binding present → never re-decide; **conveyance**: may re-deliver from the committed buffer, no new event; **render**: NO re-render without a NEW touch commit (G5) |
| W4 | partial bytes / partial frame | same true event | same as W3 |
| W5 | the bytes / the frame | same true event | nothing to do |

**Reading the table is the completeness argument: every corner the three failed rounds found lives in
one cell.** V67's under-logged read = W1 mislabelled as safe for a resolve-first ordering — killed by
making the effect part of the commit. V68's outcome-change-after-event = a claimed W3→W5 transition
that could alter the terminal fact — killed by deleting the `TRANSFER` state: **after W2 there is no
state whose failure changes what the log claims.** V69's unsatisfiable Row G rule = classing renders
as N1-delivery — killed by G5.

## 3b. The deadline — lifecycle semantics, so it lives HERE (GPT56-V81 F2, CODEX-V81 F4: the
deadline was added to the draft and absent from this spec, invisible to the derivation checker — the
single-home rule violated by the repair that extended the lifecycle)

**Every request carries a deadline.** Its value is a BS-2k design constant; its clock is the
**monotonic** clock (wall-clock manipulation does not extend it); it is **fixed at request receipt
and never resets** — no state transition, retry-internal step or partial progress renews it. A live
request past its deadline **is** a processing failure under a live Row B and receives the
`REFUSED-UNCLASSIFIED` refusal commit. A request that is neither terminal nor within deadline is a
state this spec does not admit. **The admitted nonterminal state has a NAME — `PENDING`: arrival committed, no decision event, deadline unexpired (named for the existence half of exactly-one-terminal, GPT56-V88 F4, CODEX-V88 F3). A past-deadline zero-terminal arrival is NOT PENDING and not admitted — it is the state whose absence §6.1's five verifier gates check, and finding one refuses the gate as a custody failure; the last gate refuses any zero-terminal arrival at all — the run does not end over an open request.** **THE AUTHENTICATED CLOCK BASIS (GPT56-V89 F1, CODEX-V89 F2 — a verifier cannot read the monotonic clock it is asked to enforce): the ARRIVAL event carries `(boot_epoch, monotonic_reading)` — Row B's own monotonic reading at append, authenticated with the event — and every checkpoint's materials carry a CLOCK RECORD `(boot_epoch, monotonic_reading)` of their production. Overdue is COMPUTED FROM THOSE BYTES ONLY: an arrival is overdue at a gate iff the gate checkpoint's epoch exceeds the arrival's — a restart happened after it; readings do not compare across epochs, so the conservative closure is the deadline refusal at the first later-epoch pass — or the epochs are equal and the checkpoint reading minus the arrival reading exceeds the BS-2k deadline constant. The wall-clock ISO timestamp is human-facing and NEVER the comparison basis; no verifier reads a clock at verification time.** **THE SEMANTICS THE SIGNATURES DO NOT CARRY (CODEX-V90 F1, GPT56-V90 F2 — a signature proves authorship, not monotonicity): `boot_epoch` is a BS-2k-provisioned RESTART COUNTER — incremented exactly once at every Row B start, committed in the transactional domain BEFORE any event of the new epoch, never reused and never decreased; it is a sequence number and owes nothing to any clock. Monotonicity is an INVARIANT OVER THE SIGNED EVENT ORDER, checkable by any verifier from the chain bytes alone: (a) epochs are non-decreasing along chain order; (b) within one epoch, `monotonic_reading` is non-decreasing along chain order; (c) an event's epoch equals the counter value committed for the epoch it was appended in. A violation of any of the three is MALFORMED HISTORY and refuses the CHAIN, not the request — regression and reuse are thereby detectable from bytes, which is the origin-outside-the-author pattern: the chain order, not Row B's say-so, is what the comparison rests on. Bounds, stated where the fields live: `boot_epoch` is a decimal integer in [0, 10^6]; `monotonic_reading` is a decimal integer nanosecond count in [0, 2^63 − 1] (GPT56-V90 F3: both were called bounded with no bound stated).** **And the COMMIT itself is bounded (CODEX-V82 F7: a live Row B
stalled INSIDE the atomic commit could not append the deadline refusal, leaving a past-deadline
nonterminal request): the transactional domain aborts any commit that neither completes nor
aborts within its own BS-2k commit bound — transactional semantics make abort always available —
and the aborted request then receives the deadline refusal. A stalled commit resolves to
abort-then-refusal, never to a wait — **within what the platform serves: where the STORAGE ITSELF
never returns (GPT56/CODEX-V83 F5: an fsync that hangs forever), no domain can conjure liveness,
and that terminal case is the platform failing — the same shape as the RETIRED N2's old residue, kept as a comparison only — the run ends by operator
observation, not by lifecycle rule, and the lifecycle is TOTAL over the states the platform
serves, which is the honest quantifier.**

## 4. The states, derived — this list REPLACES every previous statement of the state machine

`RECEIVED` → `PENDING-AUTHORISATION` → (writes only: `PENDING-SURFACE-CHECK`) → **one commit**
(refusal or touch) → (conveyance only: delivery, outside the custody claim).

**There is no `TRANSFER` state.** V69 deleted it in one paragraph and left it declared in another —
a deletion that did not delete, the incomplete-retraction shape this corpus knows best. **The draft's
state declaration now points here, so the fact has one home and cannot drift against itself.**

## 5. The Row G analysis — why GPT56-V69 F2's fork DISSOLVES, and what it costs

**The asserted fork:** delivery cannot be inside the atomic domain, AND Row G voids any unlogged view
— so unlogged re-views (V69's carve-out) make the two rules unsatisfiable together.

**The dissolution: the covenant had already decided, and V69's carve-out was written over it.** Row
G's cell voids *"any unlogged view"* — views were **always** logged events. The N1 carve-out is
correct for **conveyance** (a machine re-consuming already-conveyed bytes) and was **over-broad** in
covering renders. Under **G5**: every render is a fresh touch commit — logged, satisfying Row G —
while what remains outside the claim is the human's **perception** of a rendered frame, which no log
can capture and Row G's clause never claimed. **Both rules hold simultaneously. No normative choice
is needed, because no rule changed: G5 restates what Row G's void clause already required.**

**The costs, stated so the dissolution is not mistaken for free:**
- **The V65 schedule sentence is recut**: *"re-viewing the current object is unrestricted"* remains
  true in **schedule** terms (a re-render is not a request for a different object and never violates
  the traversal) and is **corrected in custody terms: every re-render is a logged touch.** **A VIEW is the display session of ONE render commit** — it begins when the committed conveyance
  is displayed and ends at the FIRST of: the traversal position advancing, the interface clearing,
  or **ANY interruption of continuous display — visibility loss, blanking, occlusion, navigation
  away** (CODEX-V71 F2: a visibility-loss-and-restore redisplay fired neither named ender and kept
  one commit alive across views). **A session is one continuous uninterrupted display**; duration
  alone does not multiply views — one long look is one view — but **nothing displayed after an
  interruption is the same view** (GPT56-V71 F3: an operator could otherwise hold a session open
  indefinitely across repeated redisplays under one event). Within a
  session, dwell and magnification of the already-rendered frame move no store bytes and are the
  SAME view — one commit, one event. **Displaying the object again after the session ends is a NEW
  view and requires a new render commit** (CODEX-V70 F2: without the session boundary, "magnification
  is no touch" and "any unlogged view voids" contradicted on cached frames). **If the principal means
  "view" per-glance rather than per-session, that is his reading to impose; the spec's definition is
  the session, stated so the word has one meaning.**
  **BUFFER LIFETIME AND CACHE, because G5 and G6 composed into two contradictions in one round.**
  A render buffer lives **from its touch commit until its VIEW SESSION ends — or, if no session
  ever opens (a crash between commit and first frame), until its REQUEST ends — then must be
  destroyed** (GPT56-V77 F6: a commit that opened no session left the buffer with no named
  destruction trigger; the request boundary is the trigger every commit already has) — V74 said it dies "with its commit", which made delivering after the commit from a
  dead buffer an impossibility (CODEX-V74 F2); a buffer outliving the SESSION would be a cache.
  And **the sealed interface renders EXCLUSIVELY from Row B conveyances and holds NO redisplayable
  surface beyond the live session — compositor, framebuffer or otherwise** (GPT56-V74 F3: occlusion
  ends the session under G6, and a compositor restore would create the new view with no new commit;
  the interface must re-request instead, which is a new touch). **A BS-2k interface design
  requirement with fixtures: occlude-and-restore must produce a second committed render event or no
  image.**
- **The committed buffer is GOVERNED, answering CODEX-V69 F2**: for **renders there is no buffer
  reuse** — each render re-conveys under its own commit; for **conveyance** the buffer is part of the
  committed touch, destroyed on delivery completion or request end, and **its existence, bounds and
  destruction are BS-2k design requirements with fixtures** — it is Row B's surface inside the
  transactional domain, not an ungoverned χ-bearing holding area.

**If the principal reads Row G's re-view practice differently — wanting re-views unlogged — that IS
the normative fork Blanc named, it weakens a void clause, and it is his. The spec's position is that
the covenant as written already contains G5.**

## 6. What this spec deliberately leaves open

- **N2 is RETIRED** — the arrival receipt (§1c) is the second event class, authorised 2026-08-30; nothing here is referred any more.
- **The post-`BS-L` enumeration surface** is the enumeration mechanism's problem, not the
  lifecycle's; it is repaired in the draft where the enumeration lives.
- **Cross-run recurrence** stays a successor-preregistration duty.

**v9 untouched at `6a9abbbd`. Nothing here is evidence about the sky.**
