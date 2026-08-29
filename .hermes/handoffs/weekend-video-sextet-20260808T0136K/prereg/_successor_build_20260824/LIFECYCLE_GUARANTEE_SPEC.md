**STATUS: SPEC — the access-log lifecycle's guarantee, stated as invariants before any further
construction. Written at the THREE-FAILURE THRESHOLD (V67 F1/F2, V68 F1/F2, V69 F1/F2 — one object,
three consecutive rounds, a new corner each time), under the rule this lane wrote after the citation
check failed the same way: the third failure means stop patching, because the corners keep appearing
when the purpose was never stated. The draft's lifecycle text is now DERIVED from this file; a
conflict between them is a defect in the draft.**

# WHAT THE ACCESS-LOG LIFECYCLE GUARANTEES — invariants by crash window and by reader

## 0. Objects and definitions

- **TOUCH** — bytes leaving a sealed store, or landing in one. Two kinds of leaving: **CONVEYANCE**
  (bytes to another row's process) and **RENDER** (display to a human through Row G's sealed
  interface). One kind of landing: **WRITE**.
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
| G2 | **No false event**: a touch event's outcome field is true of the store effect it records; **a refusal event truthfully records that a request was refused and NO store effect occurred** | every event |
| G3 | **One event per touch** — and **every event is either exactly one touch's event or a refusal's event; no event is both, and no event is neither** (V70's wording said "one touch per event", which contradicted refusal events outright — GPT56-V70 F1, CODEX-V70 F1, the round's first finding against this spec) | every touch kind |
| G4 | **No double decision**: one request never yields two events | every request |
| G5 | **Render = touch.** Every render is its own touch with its own committed event. **Row G's *"any unlogged view"* void clause is a consumer of G5, not an exception to N1** | Row G only |

## 2. The non-guarantees, with equal weight

| # | non-guarantee | why it cannot be otherwise |
|---|---|---|
| N1 | **Delivery is outside the custody claim** — the event records the store effect, never the requester's receipt or the human's perception | the requester and the human are external to any commit domain; three orderings failed trying to include them |
| N2 | **A request that dies before any commit is invisible** | making it visible needs a second event class, which changes what the log records — not authorised, REFERRED |
| N3 | **The log can over-report delivery, never under-report a touch** | the safe direction for a custody log, consequence of G1 + N1 |

## 3. The invariant table — crash window × reader

**Windows:** W1 = before any commit · W2 = at the commit (empty by atomicity — no partial state
exists) · W3 = after commit, before delivery · W4 = during delivery · W5 = after delivery.

| window | requester sees | verifier/auditor sees | Row B on recovery sees |
|---|---|---|---|
| W1 | nothing (no bytes ever left) | nothing — **N2**: indistinguishable from no request | no binding → request never happened; safe to re-process |
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
  is displayed and ends when the traversal position advances or the interface clears. Within a
  session, dwell and magnification of the already-rendered frame move no store bytes and are the
  SAME view — one commit, one event. **Displaying the object again after the session ends is a NEW
  view and requires a new render commit** (CODEX-V70 F2: without the session boundary, "magnification
  is no touch" and "any unlogged view voids" contradicted on cached frames). **If the principal means
  "view" per-glance rather than per-session, that is his reading to impose; the spec's definition is
  the session, stated so the word has one meaning.**
- **The committed buffer is GOVERNED, answering CODEX-V69 F2**: for **renders there is no buffer
  reuse** — each render re-conveys under its own commit; for **conveyance** the buffer is part of the
  committed touch, destroyed on delivery completion or request end, and **its existence, bounds and
  destruction are BS-2k design requirements with fixtures** — it is Row B's surface inside the
  transactional domain, not an ungoverned χ-bearing holding area.

**If the principal reads Row G's re-view practice differently — wanting re-views unlogged — that IS
the normative fork Blanc named, it weakens a void clause, and it is his. The spec's position is that
the covenant as written already contains G5.**

## 6. What this spec deliberately leaves open

- **N2 stands referred** (the durable pre-verdict state; needs a second event class).
- **The post-`BS-L` enumeration surface** is the enumeration mechanism's problem, not the
  lifecycle's; it is repaired in the draft where the enumeration lives.
- **Cross-run recurrence** stays a successor-preregistration duty.

**v9 untouched at `6a9abbbd`. Nothing here is evidence about the sky.**
