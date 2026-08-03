# Kun report + Tori progress — evidence-bounded video plan

Marker: `KUN_TORI_PROGRESS_VIDEO_PLAN_V1`

## Purpose and audience

Create a concise local-review status video for Duho and the NebulaMind team explaining:

1. what Kun's oversight report concluded;
2. which corrective phases are complete;
3. what Tori actually verified;
4. which execution gates remain held or closed.

This is a status update, not a claim that the full corrective plan is finished.

## Acceptance matrix

| Requirement | Contract |
|---|---|
| Duration | Approximately 85–90 seconds |
| Aspect / media | 1280×720, 16:9, H.264/AAC, 30 fps, fast-start |
| Audio | Clearly female narration only; `en-US-EmmaNeural`; no music |
| Captions | Burned-in captions plus external SRT, both derived from the exact narration |
| Presenter | Approved synthetic Flow astronomer master portrait; silent opening and silent outro only |
| Lip-sync | No presenter is visible while narration is audible; therefore no false speaking animation |
| Visual style | Dark navy observatory, cyan/magenta accents, exact deterministic cards and status maps |
| Required facts | Contract correction; Phase 0/1 counts; piecemeal decision; 20/20 intent preservation; Surveys review chain; Kun Phase 4 PASS; held gates |
| Privacy | No secrets, credentials, `.env` contents, personal data, internal terminal logs, or private tokens on screen |
| Status honesty | Completed phases and held/closed gates must be visibly distinct |
| Publication | Local review artifact only; no upload, channel, website, cockpit, deploy, DB, Git, or visibility change |

## Source hierarchy

1. Frozen current reports and receipts listed in `source_freeze.json`.
2. Hwao source-boundary verdict `HWAO_SOURCE_BOUNDARY_VERDICT.md`.
3. The current Kun live-lane marker `KUN_PHASE4_CORRECTED_SCOPE_VERIFIED_20260722`.
4. Older clips only as presenter identity provenance, never as status truth.

Immediately before final rendering, the build must compare every frozen source hash with `source_freeze.json` and stop on drift.

## Evidence/status matrix

| Claim | Source | Status | Allowed wording | Forbidden implication |
|---|---|---|---|---|
| Contract v1 was already valid | canonical plan + Phase 0 receipt | Complete | `already COMPLETE / PASS`; rebuilding rejected | Kun asked to rebuild and it was rebuilt |
| 36-file preservation | Phase 0 receipt | Complete | 36/36 files and digests/mtimes matched | committed or published |
| 380-entry classification | Phase 1 report | Complete, read-only | 222 keep, 130 archive, 18 candidates, 10 unknown; zero moves/deletes | cleanup executed |
| Rework piecemeal | Phase 2/3 decisions | Decision complete | per-unit fates decided | all units landed on main |
| Four dirty-intent patches | Phase 3 decision | Complete | 20/20 modified tracked paths preserved | code merged or deployed |
| Surveys G3 review chain | closure receipt | Unit closed, worktree frozen | two FAILs, then unconditional PASS; Hwao closed on stronger evidence; Tori verified custody | Tori solely authored the unit; V2 merged |
| Latest Kun Phase 4 check | live Kun marker + Phase 4 ratification | PASS on corrected scope | 18 test DB files; 10 caches = 2 ordinary-future-scope + 8 held; safety zero | cleanup approved or started |
| Remaining gates | Phase 3/4 ledgers | Held/closed | future explicit gates remain | full Kun plan complete |

## Wording guards from Hwao

- The video names only the 18 **test database files**; it does not show the separate 18 G4a ordinary quarantine candidates.
- Phase 4 wording is `cleanup scope defined`, never `cleanup approved` or `cleanup started`.
- Volatile branch-behind counts are omitted.
- Tori is credited with custody and receipt verification; Hwao is credited with the Surveys closure ruling.

## Exact narration

### Scene 1 — report correction

“Kun’s oversight report rated the project healthy, with risks. One correction changed the plan: Claim Ledger Contract version one had already passed. The team would preserve and reconcile finished work, not rebuild it.”

### Scene 2 — preservation

“Phase zero preserved the contract: thirty-six files, sixteen ledger entries, forty-five evidence spans, forty-five stance rows, and twenty-six unique bibcodes. Source and backup digests and modification times matched, with zero validation errors.”

### Scene 3 — classification

“Phase one classified all three hundred eighty worktree entries before touching anything: two hundred twenty-two keep-commit, one hundred thirty archive, eighteen deletion candidates, and ten unknown. Nothing moved or deleted.”

### Scene 4 — piecemeal decision

“Phases Two and Three chose rework piecemeal. Surveys would be rebuilt on current main; the wiki fix re-applied; the backend runner held for a product decision; superseded Lab front-end commits abandoned. Four intent patches preserved all twenty modified files.”

### Scene 5 — Tori progress

“Tori’s role was custody and receipt verification. In the Surveys unit, three independent fail-closed reviews produced two honest failures, then one unconditional pass across all ten acceptance items. Hwao closed the unit on that stronger evidence. The passing V2 stays frozen and uncommitted.”

### Scene 6 — latest Kun check and boundary

“Kun’s latest check passed the corrected Phase Four scope: eighteen test database files, and ten cache directories split into two in ordinary future scope and eight held. Safety counters stayed at zero. Cleanup scope is defined, but cleanup, Git landing, database work, status-map work, runtime, and publication remain gated.”

## Scene table

| # | Duration | Audio | Dominant visual |
|---|---:|---|---|
| 0 | 3.0s | silence | Approved astronomer portrait; title and review date |
| 1 | 11.5s | narration 1 | `HEALTHY WITH RISKS` → material correction → preservation-first |
| 2 | 13.0s | narration 2 | Contract preservation count grid and 36/36 match path |
| 3 | 12.0s | narration 3 | Exact proportional 380-entry classification bar; zero actions |
| 4 | 14.0s | narration 4 | Per-unit fate map and four-patch / 20-of-20 preservation card |
| 5 | 15.0s | narration 5 | Three-review timeline: FAIL → FAIL → PASS → Hwao closure |
| 6 | 17.0s | narration 6 | Kun PASS counts + completed versus held/closed boundary |
| 7 | 2.5s | silence | Approved portrait; `Progress is real. Gates still matter.` |

Expected runtime: 88.0 seconds.

## Palette and typography

- Background: `#07101F`, `#0B1630`
- Cyan: `#35D9F2`
- Magenta: `#D95CFF`
- Success: `#4EE09A`
- Warning/held: `#F2C14E`
- Failure history: `#FF6B78`
- Body: `#EAF2FF`
- Muted: `#91A4C4`
- Typography: SF Mono for headings, counts, statuses, and captions

## Publication gate

The artifact remains local and review-only. Rendering does not authorize upload, publication, website integration, cockpit changes, or any external mutation.
