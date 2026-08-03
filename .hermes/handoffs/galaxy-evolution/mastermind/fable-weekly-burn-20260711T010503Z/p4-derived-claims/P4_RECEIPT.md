# P4 receipt — derived claim/evidence candidates from the clean cycle-5 package

status: COMPLETE

- t_ack: 2026-07-11T02:22:04Z (T0_lane)
- t_end: 2026-07-11T02:33:00Z (well inside hard cap T0_lane + 30 min = 02:52:04Z; clock < 03:50:00Z absolute stop)
- tmux pane id: %187
- brief: `HWAO_FABLE_BURN_P4_BRIEF_20260711T010503Z` (late-start guard PASS: ACK 02:22:04Z < 03:15:00Z)

## Artifact table (write dir `p4-derived-claims/`)

| File | Bytes | sha256 |
|---|---|---|
| `P4_ACK.md` | 410 | `cda7b641d2bc14da8a51b76e7a4dfe7d913fd97d6319a672a0e96d2d20ddc147` |
| `CLAIM_EVIDENCE_CANDIDATES.md` | 33940 | `1c8d9a7d28566a19a957cac754a7b8c6c5981a3ad445eb3d3f9daacbd49f8b39` |
| `sources-snapshot/rp1_flagship_polished.tex` | 23917 | `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384` |
| `sources-snapshot/supplementary_denominator_atlas.tex` | 37532 | `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71` |
| `P4_RECEIPT.md` | (this file — not self-hashed) | — |
| `FABLE_BURN_P4_DONE_20260711T010503Z` | 0 (empty marker) | — |

## Source table (verified 2026-07-11T02:22–02:23Z, before any extraction)

| Source (absolute path) | Observed sha256 | Expected | Verdict |
|---|---|---|---|
| `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` | `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384` | same | PASS |
| `.../candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` | `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71` | same | PASS |
| `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants/INVARIANT_MANIFEST.json` | `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717` | same | PASS |
| `.../p1-rp1-invariants/INTRODUCTION_LITERATURE_REFERENCE.md` | `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` | same | PASS |
| `/Users/duhokim/NebulaMind/NebulaMind/wiki_schema.md` (formatting reference only; no pinned hash per brief §3) | `d1c04e1fcf1e9b412712d07407c42fccffcf12b5a2fc2eced59dba888594b5dd` | n/a — recorded as observed | RECORDED |

Both tex snapshots hash-identical to the live cycle-5 originals; all line references taken from the snapshots. Live runner tree was read-only-touched (two `cp` reads + `shasum`); nothing written there.

## Candidates: 13

- P4-C01 — flagship FLG:13/57/74 (headline 8,146-pair matched offset, CI)
- P4-C02 — flagship FLG:39/31 (denominator census)
- P4-C03 — flagship FLG:39 (matching coverage/separations)
- P4-C04 — flagship FLG:31 (parent count / cache coverage selection context)
- P4-C05 — flagship FLG:32/33/25 (fiber-centered aperture geometry)
- P4-C06 — supplement SUP:92/93 (environment 10th-neighbor baseline)
- P4-C07 — supplement SUP:103 (maintenance-heating massive subset)
- P4-C08 — supplement SUP:114 (high-excitation subset)
- P4-C09 — supplement SUP:125 (radio-jet environment quartiles)
- P4-C10 — supplement SUP:136 (mass-bin incidence diagnostic)
- P4-C11 — supplement SUP:147 (tracer-threshold census)
- P4-C12 — supplement SUP:158 (gas-depletion denominator)
- P4-C13 — supplement SUP:169 (simulation target-vector spans)

Flagship headline covered first per brief §4; all eight supplement atlas entries covered. The 15 target-vector table rows (SUP-ROW-176…190) are carried as a unit inside P4-C13 with the whole-row invariance rule rather than expanded into separate candidates (integrity-safe form given the line-188 truncation anomaly).

## Numerals check summary

Every numeral in claim_text/evidence maps to a manifest entry id; **zero unmatched**. Scripted audit at 02:31:19Z against the snapshots reproduced the manifest `occurrences_expected` for every string used, e.g. flagship: `[-1.334,-1.283]`=4, `-1.309`=6, `8,146`=9, `60,000`=11, `249,917`=1, `24.0\%`=1, `39,553`=1, `12,234`=1, `0.0045`=1, `0.00021`=1, `1.2--6.5`=2, `0.02<z<0.12`=2; supplement: all 28 checked strings at expected counts. Corruption signatures absent everywhere (snapshots and `CLAIM_EVIDENCE_CANDIDATES.md`): re-rounded CI upper bound = 0 hits, `2.831` = 0, cycle-6 spans `0.001-0.856`/`0.001-0.610` = 0. Canonical FLG-CI95 string carried verbatim (rounding anomaly respected, never re-derived); FLG-ROW-057 table row carried as one byte-identical string. Manifest entry ids used per candidate are listed inline in the deliverable. Exceptions: none.

## Deviations and resolved ambiguities

- Deviations from the brief: **none**. No conflicts between disk state and the brief were observed.
- Ambiguity 1 — numeral scope in a staging file: the manifest's verbatim rule is applied to claim_text and quoted evidence spans; staging metadata (candidate ids, line anchors, timestamps, artifact hashes, marker strings) is documented as outside manuscript prose. Stated in the deliverable's Conventions section.
- Ambiguity 2 — LaTeX vs plain rendering: evidence quotes are byte-verbatim LaTeX; claim_text may render markup (`95\%`→95%, `S/N$\geq3$`→S/N≥3) with digits identical. Stated in Conventions.
- Ambiguity 3 — `wiki_schema.md` defines article structure, not a claim/evidence table; candidates are shaped as claim+evidence blocks carrying schema-conformant fields (category `galaxy`, `/wiki/` slugs, target sections, ≥3 see_also links, schema-format reference lines) with `OFFLINE_PLACEHOLDER` for all DB-resident fields (page_id, claim_id, evidence_ids, page_version_fk, publish_state).

## Follow-up queue

- GATED — needs separate Duho approval: integrator/wiki handoff of the 13 candidates (any DB/API/page_versions write, publish-state change, or placement into a runner `candidates/` tree).
- GATED — needs separate Duho approval: network verification pass (ADS/arXiv) of external-literature values before any quantitative prior-work comparison is added to these candidates, plus registration of any such value as a manifest `external_reference` entry (per P1 reference block §3, EXT-1…EXT-4 slots).
- GATED — needs separate Duho approval: registering wiki-page targets/slugs against the live DB (slugs proposed here were chosen from `wiki_schema.md` coverage list offline; real page ids/fks must come from a gated integrator pass).

## Coordination-file checks

| When (UTC) | Check | Result |
|---|---|---|
| 02:22:04Z (ACK) | burn root listing for `GLOBAL_STOP_20260711T010503Z.md` / `HOLD_5H_20260711T010503Z.md` | neither present |
| 02:31:19Z (mid-run) | same | neither present |
| 02:32:16Z (pre-receipt) | same | neither present |

FABLE_BURN_P4_DONE_20260711T010503Z
