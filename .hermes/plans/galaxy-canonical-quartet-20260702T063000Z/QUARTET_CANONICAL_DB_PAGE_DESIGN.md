# Quartet canonical DB/page design — Galaxy Evolution

Marker: `GALAXY_CANONICAL_QUARTET_DESIGN_COMPLETE_20260702`

Created UTC: `2026-07-02T06:38:37Z`

Mode: read-only design. This is about how to change the DB/page safely, but it does not execute that change.

## One-line verdict

**Make page 57 / `galaxy-evolution` the single canonical page; absorb V2 as assets; retire page 58 as a workbench after an approved exact-diff publish.**

## Safety / verification

- DB/page content publish executed: 0
- Apply SQL generated: false
- Deploy/restart: 0
- Git commit/push/merge: 0
- Runtime source edits: 0
- Page content hashes unchanged vs Quartet baseline: `{'57': True, '58': True}`
- Note: page 57 `updated_at` metadata drift was already observed; current content hash/version/counts are stable.

## Quartet consensus

- Hermes: page 57 is the data/provenance backbone; V2 is editorial workbench.
- Lana: V1 has the better public article; V2 has the better outline and devices. Merge additively onto V1.
- Goru: the spines do not align one-to-one; marker syntax differs; strict V1 marker parser sees zero V2 chips.
- Fable: page 57 wins by data gravity, slug semantics, and version-history continuity; no third entity.

## Current inventory

| Item | Page 57 / V1 | Page 58 / V2 |
|---|---:|---:|
| Slug | `galaxy-evolution` | `galaxy-evolution-v2` |
| Latest version | 1708 | 7 |
| Claims | 721 | 8 |
| Evidence rows | 223 | 138 |
| Evidence votes | 683 | 8 |
| Page citation links | 8 | 0 |
| Fact sources | 3 | 0 |
| Body claim markers, permissive scan | 22 | 8 |
| Body claim markers, strict V1-style scan (Goru) | 22 | 0 |

V2 marker trap: V2 uses `<!-- claim:NNNN-->` with a leading space, while V1 uses `<!--claim:NNNN-->`. The preview must normalize new canonical markers to V1 syntax.

## Canonical section spine

1. **Overview: Galaxy Evolution as a Regulated Baryon Cycle** — V1 thesis + V2 reader orientation
2. **Dark Matter Halos & Structure Formation** — V1 halo/baryon efficiency + V2 high-z/JWST caveat
3. **Gas Supply, Star Formation & Feedback** — V1 gas cycle + V2 depletion/regulation distinctions
4. **AGN Feedback & Quenching** — V1 maintenance-feedback prose + V2 mode/phase conditionality
5. **Environment, Morphology & Structural Growth** — V1 ram pressure/S0/mergers + V2 satellites/cosmic web
6. **Chemical Enrichment & Cosmic Timing** — V1-only asset; preserve
7. **High-Redshift & Reionization Frontier** — V1 reionization claims, slimmed; massive-galaxy tension moved to §2
8. **Observational Evidence & Surveys** — V2 graft; organize by uncertainty reduced, not mission list
9. **Synthesis & Open Tensions** — V2 closer + V1 honest gaps

## Intended DB/page change classes

- **content_publish**
  - target: `wiki_pages id=57`
  - expected change: replace content with approved merged canonical markdown; keep slug/title canonical
  - requires: publish preflight + explicit APPROVE PUBLISH
- **version_insert**
  - target: `page_versions page_id=57`
  - expected change: insert new version row with merged content/source_note
  - requires: same publish preflight
- **claim_rehome_optional**
  - target: `claims ids 2929-2936 currently page_id=58`
  - expected change: if preview accepts them, update page_id to 57 and canonical section/order placements; preserve evidence/votes by claim_id
  - requires: row-level backup/exact diff/rollback; explicit inclusion in publish packet
- **retirement_banner_optional**
  - target: `wiki_pages id=58 and page_versions page_id=58`
  - expected change: replace V2 content with archived/superseded banner pointing to canonical page; retitle if desired
  - requires: same or separate exact-diff packet; no delete
- **redirect_later**
  - target: `runtime/router/source for galaxy-evolution-v2`
  - expected change: 301/alias to galaxy-evolution if supported
  - requires: separate source/runtime approval, tests, deploy/restart gate
- **claim_backlog_noop**
  - target: `remaining V1 claim graph, especially 526 zero-evidence trust 0.5 and 377 open-question bucket`
  - expected change: no automatic rewrite/remap in canonical merge
  - requires: separate triage campaign

## What the next preview packet must produce

- spine map
- merged prose draft
- normalized claim-marker map
- V1 surfaced-chip preservation map
- V2 claims 2929-2936 re-homing table
- page 58 retirement banner draft
- explicit exclusion/no-auto-merge list
- rendered review HTML if static serving allows
- manifest with hashes

## Hard no-auto-merge list

- No blind replacement of page 57 with V2 prose
- No automatic trust-label normalization
- No evidence stance rewrites
- No deletion of page 58 or histories
- No hero_facts resurrection
- No marker-history rewrites
- No new evidence rows just because prose lacks citations
- No two simultaneous EXECUTE phrases for different mutation packets

## Next recommended approval

```text
APPROVE GALAXY CANONICAL MERGE PREVIEW PACKET: Build a docs-only preview packet that merges Galaxy Evolution V1 (page 57) and V2 (page 58) into one canonical draft on slug galaxy-evolution: spine map, merged prose draft with normalized claim markers, claim re-homing table for claims 2929-2936, page 58 retirement banner draft, and explicit exclusion list. Write docs/JSONL/Markdown artifacts in one new directory only. No DB writes, SQL mutations, migrations, deploy/restart, git writes, runtime source edits, secrets, OpenClaw, or deletes. Timebox 3 hours; galaxy execution remains queued behind the pages-5/19/23 exact-diff EXECUTE.
```

## Source lane reports

- hermes: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/hermes_synthesis.md`
- lana: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/lana_structure_report.md`
- goru_md: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/goru_mechanical_map.md`
- goru_json: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/goru_mechanical_map.json`
- fable: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/fable_grand_design.md`

GALAXY_CANONICAL_QUARTET_DESIGN_COMPLETE_20260702
