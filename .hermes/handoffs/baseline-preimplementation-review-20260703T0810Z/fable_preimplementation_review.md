# Fable Pre-implementation Review — The Baseline

Task: THE_BASELINE_PREIMPLEMENTATION_QUARTET_REVIEW_20260703T0810Z · Lane: Fable (outside doctrine/adversarial reviewer) · Status: COMPLETE — review only; no files edited except this report.
Read: the canonical Baseline (full), Lana and Goru co-author reports, the integration report (in context), and the rebuilt cockpit source (3,687 bytes).

## Verdict: `PASS_WITH_PATCHES`

No blocker. The primitive is right, the step sequence is executable, the claim-rescue loopholes I hunted for are closed at multiple layers (Step 0 stop-if bans rescue objectives, Step 5 bans topical attachment, the tripwire list names `rescue search` and `score chasing`), and there is no prose-first regression — prose cannot begin before Step 8 and cannot ship with orphan sentences. The seven patches below are wording/spec tightenings that a non-expert implementer would otherwise trip over. Apply them and build the ledger contract; do not iterate the Baseline further before contact with real data.

## Q1 — Blockers before implementation: NONE

The papers → ledger → map → prose → derived-artifacts sequence is sound, each step has owner + artifacts + pass + stop conditions, and Step 10 correctly quarantines all mutation behind the existing exact-diff discipline. The one systemic risk is ritual mass, addressed by Patch 5 rather than by blocking.

## Q2 — Exact wording/structural patches (quoted problem → replacement)

**Patch 1 — define `modality` vs `certainty_level`; they are currently conflated.**
Problem (Step 4 schema): `"modality": "may_or_can",` alongside `"certainty_level": "emerging_sample_limited"` — and the invariant "Prose modality may never exceed evidence certainty." A non-expert cannot tell what the entry's own `modality` field is for, versus the certainty tier that caps prose.
Replacement — insert after the Step 4 schema block:
> **`modality` vs `certainty_level`, once and clearly:** `modality` is the strength of the assertion *as written* ("can expel" is modal; "expels" is declarative). `certainty_level` is the strength of its *support*. They are independent: an entry may assert "can expel" (modal) with `established` certainty. The wording contract binds prose to **min(assertion modality, certainty tier cap)** — a sentence may never be more declarative than the assertion, nor stronger than the certainty tier allows.

**Patch 2 — abstract-only evidence has no rendering tier; Step 2 and Step 7 currently disagree.**
Problem: Step 2 stop-if says abstract-only must not back "strong prevalence or mechanism claims" (implying weak use is allowed), while Lana's ladder note says "No-info / single abstract → Not renderable" and Step 7's table has no `abstract_only` row at all.
Replacement — add one row to the Step 7 table:
> | `abstract_only` support | "reported / can (as reported)" — only when the abstract itself states the finding (astronomy abstracts often carry quantified results, e.g. the 46% figure); flagged `abstract_only` in the binding | sole support for prevalence-general, dominance, or "established" wording |

**Patch 3 — quantify the countercase quota; "not empty" is gameable with one token paper.**
Problem (Step 1 pass condition): "Countercase/alternative cell is not empty." and (Step 6): "Countercase quota is met or the section is blocked." — the quota is never defined anywhere.
Replacement (Step 1 pass condition):
> - Countercase/alternative cell contains **≥2 independent sources per named debate axis**, or a recorded attestation "no countercases found after targeted search: `<queries used>`" signed by Lana. Token compliance (one stale countercase for the whole section) fails this gate.

**Patch 4 — the ledger stance vocabulary does not map to the production stance vocabulary.**
Problem (Step 5): ledger stances are `supports / qualifies / contradicts / mixed / no_info`, but the production `evidence.stance` enum is `supports / challenges / neutral / none / mismatch / refutes`, and Step 10 derives production rows from the ledger. Undefined mapping = a silent translation layer someone will improvise later.
Replacement — add to Step 10 requirements:
> 8. The Claim Ledger Contract v1 must include the **ledger↔production stance mapping table** (e.g., `qualifies` → `neutral`+qualifier note; `contradicts` → `challenges`/`refutes` per strength; `mixed` → split links). No derived evidence row may carry a stance that did not pass through this table.

**Patch 5 — anti-ritual clause: one packet, consolidated artifacts, scoped contract.**
Problem: Steps 0–9 require ~20 artifacts; nothing says whether each step needs its own approval. Left ambiguous, this reproduces the packet-per-micro-step ceremony the board already suffered once.
Replacement — insert before Step 0:
> **Proportionality rule:** Steps 0–9 execute inside **one approved docs-only run** (the phrase covers the whole pipeline through prose preview); only Step 10 ever needs its own approval phrase. For a single-section run, artifacts may be consolidated into fewer files provided every pass condition remains individually checkable. The first ledger build is scoped small by design: the schema plus the 8 AGN seed entries and the 2299 trio (~12 entries, each seed carrying its paper IDs) — completeness comes from later runs, not from the first one.

**Patch 6 — add the missing-critics test to Step 6.**
Problem (Step 6 stop-if): the false-consensus guard covers the biased denominator but not absent critics.
Replacement — add to Step 6 pass conditions:
> - The map answers, in writing: "who would disagree with each `established`/`widely_supported` status, and are they in the corpus?" An unanswered critics question blocks those two labels (downgrade to `emerging` or fix the corpus).

**Patch 7 — declare the Step 4 schema canonical over lane variants.**
Problem: Goru's co-author report specifies variant field names (`claim_statement`, `source_bibcodes`, `dominance_side`) that differ from the Baseline's Step 4 schema (`assertion`, `evidence_spans[]`, `links`). Two readable specs = future drift.
Replacement — add under the Step 4 schema:
> This schema is canonical. Variant field names in lane reports are superseded; Contract v1 may **extend** it (e.g., Goru's `dominance_side` as an optional axis tag) but may not rename existing fields.

## Q3 — Missing pieces for a non-expert

The step-by-step is genuinely followable — owners, artifacts, pass and stop conditions per step is the right shape. The gaps a non-expert would actually hit are exactly Patches 1–4 (what is modality vs certainty; what to do with abstract-only rows; how many countercases; how ledger stances become DB stances). Nothing else is missing for the docs-only phases; Step 10 correctly inherits the already-proven mutation runbook.

## Q4 — Cockpit clarity: structure right, one content gap

The rebuilt cockpit is exactly the overhaul shape — 3,687 bytes (from 41KB), calm sections, **zero** live approve/execute phrases, hold phrase only. Two gaps against the Baseline's own "Graphical progress model" section: (a) the cockpit never mentions the ledger (grep count 0) and does not display the 9-stage pipeline chain with stage 4 "claim ledger — next required" highlighted; (b) the recommended next approval (`claim ledger contract`) is not visible, so an operator reading only the cockpit knows the state is HOLD but not what the single next decision is. Patch for Hermes: render the 9-stage chain (one line, current stage highlighted) plus one "Recommended next:" line carrying the short phrase — keeping the dead-phrase rule (it is a *recommended* phrase for the operator to paste, clearly labeled, the only actionable item on the page).

## Q5 — Final verdict

`PASS_WITH_PATCHES` — apply Patches 1–7 (all small, none structural), patch the cockpit per Q4, then proceed directly to **Claim Ledger Contract v1 + the ~12-entry AGN worked example**. The doctrine is ready for contact with real data; further pre-implementation polishing would itself become the ritual the Baseline warns against.

## Safety ledger

Review only · DB writes 0 · SQL 0 · migrations 0 · Baseline/board/cockpit edits 0 · prose 0 · ledger implementation 0 · git 0 · secrets 0 · files written 1 (this report).

FABLE_BASELINE_PREIMPLEMENTATION_REVIEW_DONE_20260703T0810Z
