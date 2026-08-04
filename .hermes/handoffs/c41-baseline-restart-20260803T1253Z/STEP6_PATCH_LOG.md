# STEP6 PATCH LOG — Kun red-team patches applied

Lane: `c41-baseline-restart-20260803T1253Z` · Author: Lana · 2026-08-04 14:39 KST
Source of patch list: `KUN_STEP6_REDTEAM.md` (F1–F4; "Patches requested (pre-Step-7)" section).
Nothing applied beyond that list.

| patch | file | one-line diff |
|---|---|---|
| F1 (retitle A7, bearing-primary) | C41_STATUS_DEBATE_MAP_V1.md | A7 title "AGN boundary: stellar or AGN power in the tested objects?" → "Budget attribution: is the ionizing/excitation power in the tested objects stellar?" (summary-table row + section heading). |
| F1 (one-line boundary note) | C41_STATUS_DEBATE_MAP_V1.md | Added one sentence to the A7 boundary paragraph stating this seam IS the A7↔A6 boundary the condensation report's ±1 judgment band (fold-A7-into-A6) refers to, not the forbidden AGN-nature axis. |
| F2 (missing A5 Status line) | C41_STATUS_DEBATE_MAP_V1.md | Added `**Status:** \`emerging_sample_limited\` (all members); one-sided-plus-open, declared.` to A5, after the dispersion paragraph, matching the other six axes' template position. |
| F3 (ledger re-land) | C41_LEDGER.jsonl — NOT TOUCHED | Deferred: Kun marks F3 "applier lane, not Lana" — re-landing `VERIFICATION_STATUS_PATCH.jsonl` per-row is the v8 applier's action; this lane's report-don't-fix discipline holds and the map's disclosure already binds to the pinned Kun artifacts. No edit made. |
| F4 (R2 components-count nit) | C41_CONDENSATION_REPORT.md | R2 phrasing "the undirected link graph has 6 components" → "has 2 nontrivial components plus 4 isolates (6 components total when isolates are counted as components)"; same graph, arithmetic unchanged. |

Titles/labels only were changed for F1; no entry placements, trace rows, machine checks, counts,
shas, or status enums were altered by any patch. The 81-row trace and coverage table are
byte-identical to the Kun-re-executed state.

LANA_STEP6_PATCHED_20260804
