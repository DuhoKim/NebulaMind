# Pre-implementation Quartet discussion synthesis — The Baseline

Marker: `THE_BASELINE_PREIMPLEMENTATION_REVIEW_PATCHED_20260703T0824Z`

## Verdict

All review lanes returned `PASS_WITH_PATCHES`. None rejected the primitive or step order. The shared concern was schema ambiguity before implementation.

## What each lane said

- Fable: doctrine is sound; no claim-rescue loophole; add proportionality, abstract-only support rule, quantified countercase quota, stance mapping, missing-critics test, and cockpit next-gate clarity.
- Lana: pipeline is sound; canonicalize `certainty_level`, `epistemic_type`, field names, certainty derivation, stance location, and enum registry before implementation.
- Goru: mechanics pass but validators need exact schemas for `claim_source_stance_matrix.jsonl`, `wording_contract_check.json`, and `prose_sentence_bindings.jsonl`.

## Accepted amendments applied

1. Added pre-implementation review consensus and proportionality rule.
2. Added canonical enum registry.
3. Declared Baseline field names canonical over lane variants.
4. Rewrote Step 4 ledger schema with `source_access`, `source_bibcodes` derived index, span-level stance/rationale, `as_of`, and `verification_note`.
5. Added deterministic certainty derivation.
6. Added Step 5 stance matrix schema.
7. Rewrote Step 7 wording contract as `(certainty_level, epistemic_type, source_access)`.
8. Added `wording_contract_check.json` schema.
9. Added `prose_sentence_bindings.jsonl` schema.
10. Added countercase quota and missing-critics test.
11. Added ledger-to-production stance mapping requirement.
12. Updated cockpit to show review patched and 9-stage progress/next gate.

## Implementation gate

Do not implement Claim Ledger Contract v1 until the user approves the docs-only gate. Recommended short phrase remains:

```text
claim ledger contract
```

## Safety ledger

DB writes 0 · SQL 0 · migrations 0 · deploy/restart 0 · git writes 0 · product publish/prose 0 · Claim Ledger implementation 0 · secrets 0.

THE_BASELINE_PREIMPLEMENTATION_REVIEW_PATCHED_20260703T0824Z
