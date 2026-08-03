# Decomposed Galaxy Research Pipeline Implementation Plan

> **For Hermes:** Hwao coordinates this plan. Use subagent-driven-development task-by-task only after Duho approves implementation. Tori remains relay, receipt verifier, and bounded executor; Goru remains LOCAL-ONLY unless separately directed.

**Goal:** Replace one-shot, report-writing Deep Research prompts with narrow per-simulation evidence packets and deterministic local assembly, so the final report is rendered only from individually validated atomic records.

**Architecture:** First calibrate the current validator against the sealed C1r rendered HTML/structured capture to separate true model defects from DOM-association defects and unrealistic contract rules. Then build a dependency-free Python pipeline under `tools/galaxy_research_pipeline/` that generates one machine-readable research brief per simulation, validates each returned unit independently, and deterministically assembles only passing units into the global report. Browser research remains a later, separately armed gate; this plan's first implementation wave is offline-only.

**Tech Stack:** Python 3.11 standard library, pytest, JSON/JSONL artifacts, existing rendered-DOM fixtures and validator artifacts. No DB, production app, deployment, browser automation, network requests, or new dependencies in the offline wave.

---

## Binding safety and scope

- The terminal C1r packet remains immutable: `.hermes/handoffs/galaxy-evolution/mastermind/gemini-dr-revised-canary-20260712T045317Z/`.
- Use its sealed artifacts read-only:
  - `runs/c1r/body.md` (`8a130c5a...`)
  - `runs/c1r/rendered_body.html` (`78ed129c...`)
  - `runs/c1r/structured_capture.json` (`2d10e34a...`)
  - `runs/c1r/validator_result.json` (`34f525a5...`)
- Do not modify or reuse `tools/gemini_deep_research_driver.py`; it selects the first Gemini tab, activates Chrome, uses global clipboard/System Events, and has obsolete completion/report selectors.
- No live Gemini run is authorized by this plan. A future live pilot requires a new packet, fresh quota/custody gates, exact-target browser ownership, and separate Duho approval.
- The assembler must never invent, paraphrase into stronger claims, fill blanks, infer absence, or repair failed evidence records. It emits a blocked report instead.
- No commit, push, DB write, deploy, restart, cron, or public cockpit update without a separate instruction.

## Proposed artifact model

Each simulation unit is a standalone JSON document with these top-level fields:

- `schema`: `NM_SIMULATION_EVIDENCE_UNIT_V1`
- `unit_id`, `simulation`, `aliases`, `research_request_id`
- `sources`: canonical source records keyed by stable local `source_id`
- `calibration_targets`: atomic records, one claim per record
- `feedback_parameters`: atomic records, one claim per record
- `emergent_properties`: atomic records, one claim per record
- `validations`: one observation comparison per record
- `double_counting_warnings`: one attributed warning per record
- `observable_statuses`: exactly the five requested feedback-relevant observables
- `gaps`: cited gaps or explicit unverified-absence records
- `manual_review`: reviewer, status, notes

Each atomic claim record carries:

- exact source-backed text or exact allowed empty token
- `source_ids` local references
- quantitative values split into value/unit/uncertainty fields
- `uncertainty_status`
- validation `comparability` token when applicable
- fraction/incidence `tracer`, `selection`, `denominator`, and `redshift`
- `claim_scope` and `source_quote`

The deterministic renderer repeats resolved citations into every required output cell. Research workers do not hand-author the final Markdown table.

---

### Task 1: Calibrate the sealed C1r failures before changing the contract

**Objective:** Classify every one of the 54 deterministic failures as `MODEL_DEFECT`, `RENDERED_DOM_ASSOCIATION_DEFECT`, `VALIDATOR_DEFECT`, or `CONTRACT_UNREALISTIC`, with direct evidence.

**Files:**
- Create: `tools/galaxy_research_pipeline/c1r_forensics.py`
- Create: `tools/tests/test_galaxy_research_c1r_forensics.py`
- Create at run time: `.hermes/handoffs/galaxy-evolution/mastermind/gemini-dr-decomposed-design-<UTC>/offline/c1r_failure_classification.json`
- Read only: terminal C1r `body.md`, `rendered_body.html`, `structured_capture.json`, and `validator_result.json`

**Steps:**
1. Write failing tests that load miniature table fixtures where citations appear as nested anchors, sibling source chips, and detached footnote/source containers.
2. Run: `python3.11 -m pytest tools/tests/test_galaxy_research_c1r_forensics.py -q`
   - Expected: FAIL because the forensic classifier does not exist.
3. Implement a read-only classifier that joins each validator `source_ref` to structured block, rendered HTML element, nested links, sibling citation controls, and source-chip identifiers.
4. For C2/C4, distinguish genuinely empty/uncited cells from citations visually associated by Gemini but omitted by the current extractor.
5. For C6, distinguish scientific fraction/incidence claims from method/parameter text that merely contains those words.
6. For C7, compare canonical URL sets after normalizing `http/https`, abstract/full-article variants, arXiv versions, fragments, and trailing punctuation; preserve true orphan ledger rows as defects.
7. Emit one classification row per original finding plus aggregate counts and unresolved items.
8. Run the focused tests again; expected PASS.
9. Run against the sealed C1r artifacts and manually inspect every unresolved row.
10. Gate: no contract or validator change until classification has zero unresolved rows and Hwao records a review receipt.

**Verification:**
- Original artifact hashes remain unchanged.
- Classification contains exactly 54 deterministic input failures.
- Every classification includes source refs and rendered evidence; no title-only or text-snippet-only attribution.

---

### Task 2: Define the machine-readable unit schema and fail-closed validator

**Objective:** Create a strict Python schema validator for one simulation's atomic evidence packet.

**Files:**
- Create: `tools/galaxy_research_pipeline/__init__.py`
- Create: `tools/galaxy_research_pipeline/schema.py`
- Create: `tools/galaxy_research_pipeline/unit_validator.py`
- Create: `tools/galaxy_research_pipeline/specs/unit_v1.json`
- Create: `tools/tests/test_galaxy_research_unit_validator.py`

**Steps:**
1. Write fixtures for one fully valid unit and failures for missing source IDs, empty claim fields, unresolved source references, missing uncertainties, missing comparability tokens, incomplete fraction qualifiers, duplicate records, malformed URLs, missing observable rows, and unsupported status tokens.
2. Run focused tests and confirm RED.
3. Implement standard-library validation functions returning structured findings, never booleans alone.
4. Require exactly one of:
   - source-backed atomic claim; or
   - the field's exact allowed empty/not-reported token.
5. Require all `source_ids` to resolve inside the same unit's source registry.
6. Require `manual_review.status == PASS` before a unit can be assembly-eligible.
7. Run tests and confirm GREEN.

**Verification command:**
`python3.11 -m pytest tools/tests/test_galaxy_research_unit_validator.py -q`

---

### Task 3: Generate narrow per-simulation research briefs

**Objective:** Produce deterministic prompts/manifests for eight independent units without launching a browser.

**Files:**
- Create: `tools/galaxy_research_pipeline/briefs.py`
- Create: `tools/galaxy_research_pipeline/templates/unit_prompt.md`
- Create: `tools/galaxy_research_pipeline/specs/simulations_v1.json`
- Create: `tools/tests/test_galaxy_research_briefs.py`

**Initial units:**
- IllustrisTNG
- EAGLE
- SIMBA
- FIRE/FIRE-2
- ROMULUS
- ASTRID
- FLAMINGO
- BAHAMAS

**Steps:**
1. Write tests pinning stable unit IDs, simulation aliases, exact output schema, source-quote requirement, and the prohibition on global synthesis.
2. Implement deterministic brief generation from `simulations_v1.json`.
3. Each brief asks only for one simulation and outputs JSON records, not Markdown tables or a global narrative.
4. Split broad categories into atomic records; no cell may contain several independently sourced claims.
5. Include a per-unit source registry so citations are specified once by the researcher and repeated locally only by the renderer.
6. Emit `brief.md`, `unit_manifest.json`, and `expected_output_schema.json` under a caller-supplied offline packet directory.
7. Verify byte-stable output across repeated generation.

**Verification command:**
`python3.11 -m pytest tools/tests/test_galaxy_research_briefs.py -q`

---

### Task 4: Build deterministic normalization without changing claim meaning

**Objective:** Normalize identifiers and representation while preserving original claim text and provenance.

**Files:**
- Create: `tools/galaxy_research_pipeline/normalize.py`
- Create: `tools/tests/test_galaxy_research_normalize.py`

**Steps:**
1. Write RED tests for arXiv version normalization, DOI case, URL fragments, MNRAS abstract/full-article variants, duplicate sources, Unicode spaces, and stable source IDs.
2. Implement normalization that stores both `original_url` and `canonical_url`.
3. Never rewrite claim text, source quotes, uncertainties, or comparability decisions.
4. Treat questionable equivalence as `AMBIGUOUS_CANONICALIZATION`, not a merge.
5. Confirm GREEN.

**Verification command:**
`python3.11 -m pytest tools/tests/test_galaxy_research_normalize.py -q`

---

### Task 5: Build the deterministic global assembler

**Objective:** Render the global report only from assembly-eligible unit records, with stable ordering and per-cell citations.

**Files:**
- Create: `tools/galaxy_research_pipeline/assemble.py`
- Create: `tools/galaxy_research_pipeline/render.py`
- Create: `tools/tests/test_galaxy_research_assemble.py`

**Steps:**
1. Write RED tests for stable simulation ordering, blocked units, duplicate sources, citation repetition in every claim-bearing cell, exact empty tokens, section order, comparability tokens, qualifiers, Links ledger bijection, and final marker placement.
2. Implement `assemble_units(units)` to validate all units before rendering.
3. If any unit fails or lacks manual PASS, emit only `assembly_blocked.json`; do not emit `report.md`.
4. Render calibration, validation, warnings, observable map, gaps, and Links ledger from typed records.
5. Resolve local `source_ids` and repeat rendered citations into each required output cell mechanically.
6. Build the Links ledger from actual rendered references, not from a separately generated list.
7. Place the final marker exactly once after all content.
8. Confirm GREEN.

**Verification command:**
`python3.11 -m pytest tools/tests/test_galaxy_research_assemble.py -q`

---

### Task 6: Replace the monolithic validator with layered validation

**Objective:** Separate representation validation, unit semantics, assembly invariants, and final rendered-contract checks.

**Files:**
- Create: `tools/galaxy_research_pipeline/report_validator.py`
- Create: `tools/tests/test_galaxy_research_report_validator.py`
- Read/reference only initially: revised C1r `validator/validator.py` and `validator/structured_capture.js`

**Layers:**
1. `unit_validator`: atomic evidence and provenance.
2. `assembler`: typed construction and citation placement.
3. `report_validator`: final section/order/token/marker/link checks.
4. `manual_review`: scientific meaning, source fidelity, and selection comparability.

**Steps:**
1. Port only rules confirmed valid by Task 1's forensic classification.
2. Add DOM fixtures that reproduce Gemini table/source-chip markup.
3. Remove keyword heuristics proven to over-trigger; replace them with typed record checks before rendering.
4. Keep final rendered checks for order, blank cells, banned register, URL bijection, and marker only.
5. Run old failed C1 and C1r fixtures as regression failures.
6. Run a clean assembled fixture as deterministic PASS.

**Verification command:**
`python3.11 -m pytest tools/tests/test_galaxy_research_report_validator.py -q`

---

### Task 7: Add an offline CLI and immutable receipt bundle

**Objective:** Provide one operator command for generation, validation, assembly, and receipt creation without browser access.

**Files:**
- Create: `tools/galaxy_research_pipeline/cli.py`
- Create: `tools/galaxy_research_pipeline/receipts.py`
- Create: `tools/tests/test_galaxy_research_cli.py`

**Commands:**
- `generate-briefs --out <packet>`
- `validate-unit --unit <unit.json> --out <receipt.json>`
- `assemble --units <dir> --out <assembly-dir>`
- `validate-report --body <report.md> --structured <capture.json> --out <receipt.json>`

**Steps:**
1. Write RED CLI tests using `tmp_path`.
2. Require exclusive-create outputs and refuse overwrite.
3. Hash every input/output and write an immutable manifest.
4. Record blocked units separately; never silently omit them.
5. Ensure all commands are offline and dependency-free.
6. Confirm GREEN.

**Verification command:**
`python3.11 -m pytest tools/tests/test_galaxy_research_cli.py -q`

---

### Task 8: Run a fully offline end-to-end fixture pilot

**Objective:** Prove the pipeline with synthetic/curated fixtures before any model or browser work.

**Files:**
- Create: `tools/tests/fixtures/galaxy_research/`
- Create: `tools/tests/test_galaxy_research_end_to_end.py`
- Create at run time: `.hermes/handoffs/galaxy-evolution/mastermind/gemini-dr-decomposed-design-<UTC>/offline/e2e/`

**Steps:**
1. Build eight small clean units with known citations and one blocked unit variant.
2. Confirm all-clean units generate a stable report and a passing receipt.
3. Confirm one blocked unit prevents report creation.
4. Confirm each final claim-bearing cell contains its resolved citation.
5. Confirm the Links ledger is generated bijectively from rendered references.
6. Confirm report bytes and hashes are stable across two runs.
7. Run the whole tools test subset.

**Verification commands:**
- `python3.11 -m pytest tools/tests/test_galaxy_research_*.py -q`
- `python3.11 -m compileall -q tools/galaxy_research_pipeline`

---

### Task 9: Prepare—but do not arm—a one-simulation live pilot packet

**Objective:** After all offline gates pass, prepare a fresh packet for one simulation only, without launching Gemini.

**Files:**
- Create later: `.hermes/handoffs/galaxy-evolution/mastermind/gemini-dr-unit-pilot-<UTC>/`
- Pin: brief, unit schema, validators, assembly code, fixtures, and receipts by SHA-256.

**Pilot choice:** Start with one simulation whose method and validation literature are well defined; Hwao chooses only after the forensic review. Do not default automatically.

**Required separate gates:**
- explicit Duho approval for the live pilot
- fresh quota below the packet threshold
- exact-target browser custody
- Pro + Deep Research verified
- one prompt submission and one human Start
- no follow-up/retry
- capture unit JSON plus rendered response
- unit validator PASS plus manual semantic PASS
- exact-ID cleanup after custody

**Stop condition:** A failed unit pilot closes the packet. It does not trigger another simulation, prompt repair, or retry.

---

## Acceptance criteria for the future design

The offline design is implementation-ready only when:

1. C1r forensic classification covers all 54 deterministic failures with zero unresolved rows.
2. Unit schema and validator tests pass.
3. Brief generation is byte-stable and produces exactly eight independent units.
4. A failed or unreviewed unit prevents assembly.
5. The assembler mechanically places citations and never synthesizes missing content.
6. Links ledger is generated from rendered references and is bijective.
7. Layered validator passes the clean fixture and fails both historical failed reports for the correct reasons.
8. End-to-end offline output is byte-stable across repeated runs.
9. No production, DB, browser, network, deploy, git, cron, or cockpit action occurs.
10. A future live pilot remains separately permission-gated.

## Risks and tradeoffs

- **Validator false positives:** Task 1 must resolve DOM/source-chip association before using historical counts to redesign the contract.
- **Contract practicality:** Repeating full citations in every cell is machine-renderable even if unreasonable for model-authored prose; move repetition to the renderer rather than weakening provenance.
- **Cross-unit inconsistency:** Units may use conflicting definitions or selections. Preserve them as separate records and require manual comparability review; do not reconcile automatically.
- **Source verification:** URL/metadata verification is a separate gated network step. Offline records remain `QUARANTINED_PENDING_LOCAL_CHECK` until verified.
- **Model JSON drift:** Unit validator fails closed. Do not add permissive repair that changes meaning.
- **Operational complexity:** Eight small runs cost more coordination than one large run, but each failure is isolated and reviewable.

## Handoff

Hwao should first commission Task 1 as a fresh offline-only post-mortem lane. Only after the 54 findings are classified should Hwao finalize the unit contract and dispatch implementation tasks. No live Gemini work is part of this approval.
