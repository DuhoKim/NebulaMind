# Goru Pre-Implementation Review

**Role**: Mechanical Verifier
**Focus**: Exact paths, markers, JSON/HTML parseability, machine-checkable schema conditions, and cockpit state validation.

### 1. Does the primitive and step sequence have any blocker before implementation?
No hard blockers, but a mechanical automation gap exists. Steps 7 and 8 require me (Goru) to mechanically check wording tiers and sentence bindings, but the Baseline does not specify the exact JSON schema for those artifacts. Without strict schemas, I cannot write automated gate scripts to parse them reliably. 

### 2. What exact wording or structural change would you make to The Baseline? 
**Problem (Step 7)**: 
```markdown
Required artifact:
- `RUN_DIR/artifacts/wording_contract_check.json`
```
**Replacement**: 
```markdown
Required artifact:
- `RUN_DIR/artifacts/wording_contract_check.json` (Must strictly map `sentence_id` to `max_allowed_tier` and `actual_tier` for mechanical validation).
```

**Problem (Step 8)**: 
```markdown
Required artifacts:
- `RUN_DIR/reports/PROSE_PREVIEW.md`
- `RUN_DIR/artifacts/prose_sentence_bindings.jsonl`
```
**Replacement**: 
```markdown
Required artifacts:
- `RUN_DIR/reports/PROSE_PREVIEW.md`
- `RUN_DIR/artifacts/prose_sentence_bindings.jsonl` (Must strictly contain `sentence_id`, `text`, and `bound_entry_ids` array).
```

### 3. Is any required artifact/schema/pass condition missing for a non-expert to follow it step by step?
Yes. The exact expected keys for `prose_sentence_bindings.jsonl` and `wording_contract_check.json` must be formally declared (as patched above) so that non-experts and automated validators know exactly what data structure to emit. Furthermore, Step 4’s `claim_status_ledger.jsonl` schema is present and well-formed, but Step 5's `claim_source_stance_matrix.jsonl` is missing its explicit schema block.

### 4. Does the cockpit visually communicate the current state and next gate clearly enough?
Yes. The cockpit HTML at `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/live-steering-cockpit.html` successfully parses. It contains the valid `THE_BASELINE_PREIMPLEMENTATION_QUARTET_REVIEW_RUNNING_20260703T0810Z` marker, explicit progress bar graphics showing steps 2 through 5 as "Pending", and a clearly bound read-only hold phrase. The graphical communication is mechanically intact.

### 5. Final verdict
**PASS_WITH_PATCHES**

GORU_BASELINE_PREIMPLEMENTATION_REVIEW_DONE_20260703T0810Z
