# V13 pre-render exact-hash three-seat gate

Status: ACTIVE_PRE_RENDER_GATE — ANY HOLD BLOCKS
Coordinator/owner: Yui

## Exact frozen packet

Review only these current bytes:

- `STORYBOARD_DRAFT_V13.json` — SHA-256 `4df53ed7d5f0e38dfe54570f7761bb9e6affe4dd3a686e66f3da852074fad817`
- `V13_VISUAL_TEXT_CONTRACT.json` — SHA-256 `c7557b98853655355a5ce96daf27e1d385c561db5657309dfa3bbc696e551361`
- `NARRATION_DRAFT_V12.md` (reused unchanged as V13 narration) — SHA-256 `178ffe4ada125668c8ff84bc156adee7820954591f9781adb7101aac562d80da`
- `V13_CONTRACT_REPAIR_RECEIPT.json` — SHA-256 `2ae7114a45f5dd9a5aeecc45719a2c2ab25d5637df049b6f3fcc6dd30228d339`
- `V13_REPAIR_A_EXACT_AUTHORITY.md` — SHA-256 `35e5fa1e90f8d4e5544b3aab4172e6a894b3c5a5df31d9e954a741991484056b`

The previously generated V13 storyboard hash `8ee969eaff4ea0eb4dc8c06934c4109185767e061be8d19b00afac9fddb10097` is INVALID and must not receive a verdict.

## Authorized delta only

V13 is V12 plus exactly two contract repairs and administrative version/status labels. No narration, card, picture, design, timing, per-card keep list, or script byte changes are authorized.

Repair A exact value in `render_contract.card_05_no_terminus_prohibition`:

`no 95.4% endpoint, arrow, tick, bracket, marker, whisker, shaded boundary, axis-aligned glyph, or scaled terminus`

All nine terms are mandatory. `scaled terminus` must remain literal.

Repair B exact value in `V13_VISUAL_TEXT_CONTRACT.json.rules.conditionally_permitted_roles[0]`:

`{"role": "illustration_tag", "text": "ILLUSTRATION", "permitted_when": "QA judges a generated asset could be read as an observation"}`

This is conditional permission, not a requirement to show the tag when the condition is false.

## Common checks required of every seat

1. Independently recompute all five hashes above. Stop with HOLD if any differ.
2. Confirm Repair A is exact and complete, including literal `scaled terminus`.
3. Confirm Repair B is exact, singular, and does not broaden the closed world.
4. Confirm V13 storyboard equals V12 after removing only `version`, `status`, and Repair A.
5. Confirm V13 text contract equals V12 after removing only `status` and Repair B.
6. Confirm all 11 card records, metaphor kit, per-card viewer-text keep lists, narration payloads, planned timing, and 402-second total are unchanged.
7. Confirm target 142 WPM, allowed band 135–150, mandatory embedded subtitle stream, exact SRT, and exact VTT remain in the render contract.
8. Confirm no viewer-facing/heard crew or personal names and no generated quantitative/observation claim path was introduced.
9. Do not inherit a V12 verdict. Give a fresh verdict bound to all five current hashes.

## Seat-specific review

### Lana

Judge semantic/claim-boundary fidelity of both repairs and whether the nine-term enumeration now satisfies your V12 HOLD condition without semantic drift. Confirm that conditional `ILLUSTRATION` permission creates a usable safety path without weakening the closed-world rule.

Write only: `LANA_GATE_V13.md` in this directory.
End with exactly one standalone marker:
- `LANA_V13_EXACT_HASH_PASS`
- `LANA_V13_HOLD`

### Goru

Mechanically reproduce the exact structural delta and term inventory. Count the nine Repair A terms, prove `scaled terminus` exists, prove Repair B is exactly one object, and independently confirm all frozen hashes and unchanged structures.

Write only: `GORU_GATE_V13.md` in this directory.
End with exactly one standalone marker:
- `GORU_V13_EXACT_HASH_PASS`
- `GORU_V13_HOLD`

### Kun

Judge implementation/reproducibility of the contract change. Confirm render-from-gated-bytes is feasible, Repair A/B are machine-assertable, no unreviewed source delta exists, and the caption/subtitle and decoded-audio WPM gates remain enforceable.

Write only: `KUN_GATE_V13.md` in this directory.
End with exactly one standalone marker:
- `KUN_V13_EXACT_HASH_PASS`
- `KUN_V13_HOLD`

## Scope and stop rule

Allowed: read the frozen packet, V12 comparison files, V8 supporting receipts/spec, and local test/source-builder evidence; recompute hashes; write only your own gate receipt.

Forbidden: edit any source/contract/authority/build/render file; render audio/video; generate media; upload; mutate YouTube; change cockpit; git write; DB write; deploy/restart; browse external sources.

Any HOLD blocks render. A PASS on any hash other than the five listed above is stale and unusable.
