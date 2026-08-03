# Lana — pre-implementation review of *The Baseline*

Task: `THE_BASELINE_PREIMPLEMENTATION_QUARTET_REVIEW_20260703T0810Z` · Lane: Lana (methods/pipeline reviewer) · Review/discussion only.
Written: 2026-07-03, repo `/Users/duhokim/NebulaMind/NebulaMind`. **No edits to Baseline/cockpit/board/DB/source/git. No Claim Ledger implementation. One report written.**

## Verdict: **PASS_WITH_PATCHES**

The primitive, the 0→10 step sequence, and the method bindings are sound and implementable — the pipeline logic is right and the gates are in the correct order. **But the Claim Ledger Contract v1 cannot yet be built *without ambiguity***, because the schema/enum vocabulary is not canonical: the same fields carry different value-sets across Steps 4/6/7, and the integrated Step-4 schema does not match Goru's own co-author schema. Building now would yield three subtly incompatible ledgers (Baseline text vs Goru's validator vs implementer). The patches below make it unambiguous; none require redesign.

## 1. Blockers before implementation

**No blocker in the primitive or step sequence** — those pass. The blocker is a **schema-canonicalization gap** in Step 4 + Steps 6/7, four concrete instances:

- **B1 — `certainty_level` has three different enums.** Step 6 defines `established | widely_supported | emerging_sample_limited | actively_debated | contradicted_or_model_dependent | no_info`. Step 7's wording table adds two values not in that enum — `single_case` and `simulation_model`. Step 4's schema shows `certainty_level: "emerging_sample_limited"` but never declares the allowed set. → A non-expert cannot mechanically map a ledger entry to a wording tier.
- **B2 — `epistemic_type` enum differs between the Baseline and Goru.** Baseline Step 2 uses `review | observational_sample | single case | simulation | theory | method`. Goru's co-author schema uses `simulation_model | observational_sample | review_status`. Same field, three spellings (`review` vs `review_status`, `simulation` vs `simulation_model`).
- **B3 — Step-4 ledger fields do not match Goru's ledger fields.** Baseline: `assertion`, `evidence_spans[]`. Goru: `claim_statement`, `source_bibcodes[]`. If Goru's mechanical validator keys on `claim_statement`/`source_bibcodes` and the implementer builds `assertion`/`evidence_spans`, the Contract v1 fails validation on field names alone.
- **B4 — no certainty-derivation rule.** Step 4 lists `certainty_dimensions` *and* a `certainty_level`, but no rule maps dimensions → level. Two implementers will assign different levels from identical dimensions → non-reproducible, and the whole "modality ≤ certainty" guarantee rests on a hand-assigned value.

These are the same class of issue (uncanonical vocabulary), and together they block "implementable without ambiguity." They are cheap to fix.

## 2. Exact wording/structural changes (quote → replacement)

**Patch A — one canonical `certainty_level` enum, and make the wording contract a function of TWO axes.**
> Problem (Step 7 table rows): `single_case` and `simulation_model` appear as "Ledger certainty" values, but Step 6's `certainty_level` enum does not contain them.

Replacement — keep `certainty_level` to the **six** Step-6 values and add a second keying axis `epistemic_type`, because "it's a simulation" and "it's a single case" are *epistemic types*, not certainty levels:

> **Wording contract is a function of `(certainty_level, epistemic_type)`.** `certainty_level ∈ {established, widely_supported, emerging_sample_limited, actively_debated, contradicted_or_model_dependent, no_info}`. Independently, if `epistemic_type = simulation` the sentence must use "in simulations / in this model" regardless of certainty; if `epistemic_type = single_case` the sentence must use "shows this can occur" and may not use "common/typical." A `single_case` observation is normally `certainty_level = emerging_sample_limited` with `certainty_dimensions.consistency = single_source`; a simulation is normally `model_dependence = high`.

**Patch B — add the certainty-derivation rule (Step 4).**
> Problem: `certainty_dimensions` and `certainty_level` coexist with no mapping.

Replacement (insert after the schema): 
> **Deriving `certainty_level` from dimensions (GRADE-style, deterministic):** start from `epistemic_type` (review/multi-sample observational → up to `established`; single observational sample → `emerging_sample_limited`; simulation/theory → cap at `contradicted_or_model_dependent`/`widely_supported` with `model_dependence` noted). Then **downgrade** one tier for each of: `consistency = mixed|single_source`, `directness = indirect|model_only`, `precision = qualitative|unclear`. If sources disagree in stance, level is `actively_debated`. `certainty_level` is a pure function of the dimensions; it is never hand-picked.

**Patch C — reconcile Step-4 fields with Goru's schema; declare one canonical field set.**
> Problem: Baseline `assertion`/`evidence_spans` vs Goru `claim_statement`/`source_bibcodes`.

Replacement: pick canonical names once (recommend the Baseline's richer `assertion` + `evidence_spans`, and add `source_bibcodes` as a derived convenience index), and state: *"Field names in this schema are canonical; Goru's validator and all implementers key on exactly these names. `source_bibcodes` = the deduplicated list of `evidence_spans[].paper_id`."* This aligns Goru's mechanical gate with the built artifact.

**Patch D — define the three undefined enums and move `stance` to the link level.**
> Problem: `modality` (`"may_or_can"`), `links[].type` (`"specializes"`), and entry-level `stance` (`"supports"`) are shown by example only; and Step 5 assigns stance per claim-source *link* with a different 5-value enum, while the Step-4 entry carries a single `stance`.

Replacement:
> `modality ∈ {is_are_does, commonly_probably, may_or_can, shows_can_occur, mixed_debated, in_model_only}` and must itself be ≤ the `certainty_level` cap. `links[].type ∈ {specializes, generalizes, contradicts, depends_on, same_axis}`. **`stance` lives on each evidence span/link, not on the entry** — `evidence_spans[].stance ∈ {supports, qualifies, contradicts, mixed, no_info}` (matching Step 5). The entry-level stance, if kept, is *derived* (e.g., `contradicts` if any span contradicts). This is required because one atomic entry can have spans from different papers with different stances.

*(Minor, non-blocking: add `as_of` (ISO date) and `verification_note` fields to the ledger for the living-review cadence the plan claims and to record why an entry is `blocked`.)*

## 3. Missing artifacts/schema/pass-conditions for a non-expert

- **A canonical enum registry.** After Patches A–D, add one short block — `RUN_DIR/artifacts/ledger_enums.md` (or an appendix) listing every enum: `certainty_level`, `epistemic_type`, `rhetorical_zone`, `modality`, `stance`, `links.type`, `verification_status`. Without it, Steps 3–7 each re-spell values. This is the single most useful addition for "a non-expert can follow it."
- **A worked full ledger row for 2299.** The AGN seeds (lines 431–436) name the mechanism/prevalence/dominance split but show no *complete* ledger JSON for even one of them. Add one fully-populated example row (all fields, real spans from the 26 papers, `links` between the three) as the copy-me template. Contract v1 is far less ambiguous with one gold example than with a schema alone.
- **The certainty-derivation worked example.** Show 2299-prevalence resolving to `emerging_sample_limited` via the Patch-B rule (46% subset → `precision=quantified`, `consistency=single_source` → downgrade), so implementers see the function applied.
- **Stance-matrix vs embedded-spans authority.** State that `claim_source_stance_matrix.jsonl` (Step 5) is the normalized link table and the ledger's `evidence_spans` reference it by `span_id` (no duplicated stance/rationale), to prevent drift between Steps 4 and 5.

## 4. Cockpit clarity

The served cockpit clearly communicates the **review meta-state** (pills `REVIEW RUNNING` / `IMPLEMENTATION HELD`, the 5-step review-progress grid, hold phrase). That part is good.

**Gap:** it does *not* render the **pipeline state + next gate** that the Baseline itself mandates ("Graphical progress model for cockpit," the 9-stage chain with stage 4 = "next required"). An operator sees "a review is running" but not "we are at stage 4 of 9; the next gate is *build the claim ledger*." Recommendation (patch-level, not a blocker): add the 9-stage chain `[1 corpus]→…→[9 exact-diff]` with the current stage highlighted and the next gate labeled, so both the review state and the pipeline position are visible on one screen. Keep the amber/held framing until patches land.

## 5. Final verdict

**PASS_WITH_PATCHES.** Approve proceeding to Claim Ledger Contract v1 **after** Patches A–D (canonical `certainty_level` two-axis wording; certainty-derivation rule; field-name reconciliation with Goru; enum definitions + stance-on-link) and the enum registry + one fully-worked 2299 ledger row are added. The step sequence and method bindings need no change. With those patches, a non-expert can build Contract v1 unambiguously and Goru's mechanical validator will agree with the built artifact.

## Safety ledger

- DB writes: 0 · SQL: 0 · migrations: 0 · deploy/restart: 0 · git: 0 · secrets: 0 · product publish/prose: 0 · Baseline/cockpit/board edits: 0 · Claim Ledger implementation: 0
- Reads: Baseline plan, Goru co-author report, served cockpit HTML (read-only).
- Files written by Lana: 1 (this report)

LANA_BASELINE_PREIMPLEMENTATION_REVIEW_DONE_20260703T0810Z
