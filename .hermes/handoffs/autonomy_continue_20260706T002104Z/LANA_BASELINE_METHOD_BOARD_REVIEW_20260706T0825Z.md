# Lana review — Baseline method board (semantic / methodology)

Marker to report: `LANA_BASELINE_METHOD_BOARD_REVIEW_20260706T0825Z`
Type: read-only advisory. No DB/API/network, no packet execution, no SQL, no trust/prose/wiki/product mutation, no git/deploy/restart, no public cockpit change, no approval phrases.
Question in scope: which **two** alternative methods should stand beside the current method (`Packet-gated claim-layer reconciliation`) on a permanent public method board, what to name them, where names could mislead, and what each public method homepage must explain.

---

## TL;DR recommendation

- **Keep the current method** as the center: `Packet-gated claim-layer reconciliation`.
- **Seat exactly these two peers beside it:**
  1. **Source-first evidence adjudication** — the *upstream* alternative (anchor: papers → evidence).
  2. **Debate-map-first narrative rebuild** — the *downstream* alternative (anchor: debate map → prose).
- **Do not seat** `evaluation-first readiness gate` or `display hygiene first` as peers. They are real and useful, but they are **cross-cutting overlays**, not rival ways to produce the baseline. Presenting them as peers would mislead the user (see §3–§4).
- **Better framing (recommended):** present the board as **one anchor axis** — *sources → claims (current) → prose* — with the two overlays drawn as bands that cross all three, not as extra columns. This is the single change that makes the board honest and comparable.

The three peers are not mutually exclusive; the homepages should say so explicitly. The choice the board is really making is **"where do we anchor the remaining Galaxy Evolution baseline work,"** not "which one is correct."

---

## 1. The comparison axis (the "better framing" the brief invites)

The stated goal pipeline is: **papers → claim/status ledger → debate map → prose → product/wiki completion.**

Every candidate is really a choice of *which stage drives the work and in which direction*:

| Anchor stage | Direction | Method | Unit of work |
|---|---|---|---|
| papers → evidence | bottom-up | **Source-first evidence adjudication** (peer) | the paper / evidence-stance adjudication |
| claim/status ledger | ledger-centric | **Packet-gated claim-layer reconciliation** (current) | the claim/evidence row |
| debate map → prose | top-down | **Debate-map-first narrative rebuild** (peer) | the section narrative / debate node |

Two things cut **across** all three rows and must not be drawn as their own columns:

- **Evaluation-first readiness gate** — a *quality/completeness gate* applied between stages (coverage, contradiction, trust-consistency checks). It governs *when a stage may advance*, regardless of which anchor you chose.
- **Display hygiene first** — a *sequencing tactic* that pulls the product/wiki-render safety work (P4-style: invalid trust levels, visible-vs-audit mismatches, render guards) to the front. It protects the reader surface but does not itself move papers→claims→prose forward.

Framing the board this way gives the user a clean spatial decision (upstream / ledger / downstream) plus two honestly-labeled overlays, instead of five flat options that overlap and blur into each other.

---

## 2. The two recommended peer alternatives

### 2.1 Source-first evidence adjudication  *(upstream peer)*

**Definition (concise, homepage-ready):** Build the baseline bottom-up from the paper corpus. Adjudicate each source's claims and stances first (supports / refutes / neutral, with provenance), and let the verified evidence set determine which claims and statuses may exist — narrative is written only after the evidence layer is settled.

**Why it earns a seat:** It is the strongest *scientific-integrity* alternative and the natural upstream counterweight to the current ledger-centric method. It attacks the overclaim class we are already cleaning up (the AGN-feedback cluster: broad "heats/expels the gas reservoirs" 2298/2299 and the hidden duplicate 2924) **at its root** — a claim can never outrun its sources because sources are adjudicated first. It also strengthens the thing reviewers trust most: per-claim provenance to arXiv ids.

**Honest limits (must appear on its homepage):** bottom-up convergence is slower; it can over-index on individual papers and under-serve the *debate shape*; it needs an explicit step to lift adjudicated evidence into a coherent debate map or it stalls at a pile of well-grounded but unsynthesized rows.

### 2.2 Debate-map-first narrative rebuild  *(downstream peer)*

**Definition (concise, homepage-ready):** Build the debate map and section narrative top-down first, then require every prose assertion to bind to a ledger claim + evidence row before it is published — rebuilding, splitting, or renaming claims so the ledger matches the debate structure the narrative needs. Prose that cannot bind to sufficient evidence is demoted to an open question, not published as a claim.

**Why it earns a seat:** It is the strongest *reader-coherence* alternative and the natural downstream counterweight. It catches narrative gaps and mis-scoped claims that a row-by-row ledger pass misses (e.g., that 2572's plain-correlation wording did not match its `refutes` primacy evidence, or that 2298/2924 are near-duplicate heating statements the narrative only needs once).

**Honest limits (must appear on its homepage — this is the high-risk method):** "prose-first" invites prose to lead evidence, which is exactly the failure mode the P1 cleanup exists to fix. It is only safe with a **hard binding rule**: every published sentence maps to a claim+evidence row and obeys *modality ≤ certainty* (a "can/in some systems" claim may not be rendered as a universal one), and caution successors (2945 `debated`, 2946 `reported`) cap what the prose above them may assert. Without that rule, this method manufactures overclaims faster than any other.

---

## 3. Why the other two candidates are overlays, not peers

**Evaluation-first readiness gate → cross-cutting governance overlay.** This is a *content-quality gate*, not a content-production method. If the user "chose" it as a peer, they would select a gate and still have no method that actually produces claims or prose. It also overlaps conceptually with the current method's packet-gating, so seating both as peers implies two competing gates when they govern different things (see §4). Recommend: present it as an overlay that any of the three peers runs *through* — define readiness criteria (source coverage, zero unbound prose sentences, no visible-vs-audit trust contradictions, no un-adjudicated contradictions) and let it gate stage-to-stage promotion.

**Display hygiene first → sequencing tactic / phase.** This is P4-remedy-B elevated to a slogan: protect the public render (invalid `"0.5"` trust levels, `consensus`-vs-`unverified` badge mismatches like 2298) before deeper work. It is worth doing early, but it *hides rather than repairs* underlying ledger state and advances zero scientific completeness. Seating it as a peer would imply cosmetic display fixes constitute baseline progress. Recommend: present it as an optional fast-path phase ("display-safety first, then anchor"), explicitly labeled as not baseline-completing.

---

## 4. Naming risk flags (where names could mislead the user)

1. **`Packet-gated claim-layer reconciliation` (current) — mixes a safety property into the method name.** "Packet-gated" describes the *mutation-safety mechanism*; "reconciliation" describes the *content locus*. Two risks: (a) a reader may over-read "reconciliation" as "the baseline is finished," when it only settles the **claim ledger** and can leave prose/display trailing; (b) naming one method by its safety gate makes it look as if the other methods are *not* gated. **Fix:** name all three peers by content-anchor, and state on every homepage that packet-gating (exact-diff, per-packet approval phrase, pre/post verification, rollback) is a **shared** safety property of all three, not a distinguishing feature.

2. **`Source-first` — could read as "primary-sources-only" or "re-ingest every paper from scratch."** It means *adjudication order* (evidence before narrative), not a data re-import or a ban on synthesis. Definition must say so, or the user may expect a far heavier/expensive scope than intended.

3. **`Prose-first` / `debate-map-to-prose rebuild` — highest-risk name.** It can be heard as "write the story and the claims will follow," which licenses exactly the universal-overclaim pattern (broad AGN heating/expulsion) the current cleanup is undoing. **Fix:** prefer **"Debate-map-first narrative rebuild,"** and make the modality ≤ certainty binding rule part of the *definition*, not a footnote.

4. **`Evaluation-first readiness gate` — sounds like a production method but is a gate.** A user could pick it and end up with criteria but no content engine. It also collides semantically with packet-gating. **Fix:** label it a **quality/readiness gate** and explicitly contrast it with the **safety gate** (packet-gating): the readiness gate asks "is this stage *complete and consistent* enough to advance?"; the safety gate asks "is this *mutation* exact, reversible, and approved?" Different gates, both needed, neither a peer method.

5. **`Display hygiene first` — "hygiene/first" implies progress.** Could mislead the user into treating a clean-looking public page as a completed baseline. **Fix:** name it a **display-safety phase** and state that it defers, not resolves, ledger/prose work.

---

## 5. What the permanent public method homepages must explain

Recommend a **shared homepage template** so the three peers are honestly comparable, plus per-method specifics. Each method homepage must cover:

1. **One-line definition + a "you are here" marker on the pipeline** (papers → ledger → debate map → prose → product/wiki), showing which stage the method anchors on and in which direction it drives.
2. **What drives the work (unit of work) and the order of operations** — the concrete step sequence a contributor follows.
3. **What it optimizes for, and what it explicitly does *not* guarantee.** Current: claim-layer correctness + reversibility; does **not** by itself guarantee prose/display currency. Source-first: evidential grounding; does not by itself produce a debate narrative. Debate-map-first: reader coherence; does not by itself guarantee each sentence is evidence-bounded until the binding rule runs.
4. **Failure modes and the guardrail that mitigates each** — e.g. debate-map-first → overclaim → *modality ≤ certainty* binding + caution-successor caps; source-first → slow convergence / unsynthesized pile → mandatory lift-to-debate-map step; claim-layer → prose/display lag → paired downstream pass.
5. **Shared safety & reversibility posture** — packet-gating shown as common to all: exact-diff row-level changes, a fresh per-packet approval phrase minted at write time (never pre-authorized), pre/post read-only verification, guarded rollback. Presented as a floor all methods stand on.
6. **Trust/status semantics** — how trust levels/scores and *science statuses* (`debated`, `reported`, `model_bounded`) are handled, and the rule that any recompute is **status-aware** and never flattens a deliberate caution state into `accepted` merely because a numeric score crosses a threshold. State that trust recompute is staged (currently gated behind the P4 consistency work), so visible trust may be intentionally stale after a text change.
7. **A concrete definition of "baseline complete" under this method** — the exit criteria for each pipeline stage, so the user can tell *actually done* from *looks done*: every claim bound to evidence + arXiv provenance; every published prose sentence bound to a claim; no visible-vs-audit trust contradictions; no un-adjudicated contradictions in the debate map; product/wiki surface matches the ledger.
8. **One worked end-to-end example on real material** — run the AGN-feedback / central-quenching cluster (2298 / 2299 / 2924 / 2572, with caution successors 2945 / 2946 and the separate 2573) through the method, start to finish. This is what makes an abstract method legible and comparable; each homepage should walk the *same* cluster so readers can diff the methods directly.
9. **Decision guidance: when to prefer this method, and how it composes with the others** — state plainly that the three are sequenceable (e.g. source-first to ground the corpus → claim-layer reconcile to gate writes → debate-map-first to finish the narrative), and that the two overlays (readiness gate, display-safety phase) apply throughout.
10. **Provenance / audit surface** — every claim → evidence → arXiv id; every prose sentence → claim; visible packet/version markers; a link to the method's own change history.

A short **board-level index page** should sit above the three, carrying the §1 axis diagram, the two overlays, and the naming-risk clarifications from §4 so a first-time reader is not misled by the individual method names.

---

## 6. What the board actually needs to decide

1. Ratify the two peers: **Source-first evidence adjudication** and **Debate-map-first narrative rebuild** (vs. a different pair).
2. Ratify the reframing: overlays (readiness gate, display-safety) drawn as cross-cutting bands, **not** peer columns.
3. Ratify final names, incorporating the §4 fixes (especially renaming "prose-first" → "debate-map-first" and de-emphasizing "packet-gated" as a distinguisher).
4. Approve the homepage template (§5) as the required shape for all three permanent pages.
5. Confirm the homepages describe methods only and mint/quote **no** execution or apply approval phrases (public method pages are documentation, not gates).

None of the above authorizes any write; each is a documentation/authoring decision for a later, separately-scoped build.

---

## Safety ledger (this review)

| Action | Count / state |
|---|---|
| DB / API / network checks run | 0 |
| Packets executed | 0 |
| SQL authored or executed | 0 |
| Trust recompute | 0 |
| Prose / wiki / page_versions publish | 0 |
| Product / source code change | 0 |
| Git / deploy / restart | 0 |
| Public cockpit / report mutation | 0 |
| Execute/apply approval phrase minted or quoted | 0 |
| Files written | 1 (this advisory report) |
| Inputs | brief read-only; recommendations are advisory only |

This is advisory only. Method names, framing, and homepage contents are proposals for the board; nothing here changes any claim, page, trust value, or service.

LANA_BASELINE_METHOD_BOARD_REVIEW_20260706T0825Z
