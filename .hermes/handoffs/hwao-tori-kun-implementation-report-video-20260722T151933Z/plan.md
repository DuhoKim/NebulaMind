# Hwao + Tori + Kun implementation report — video plan

Marker: `HWAO_TORI_KUN_IMPLEMENTATION_REPORT_VIDEO_PLAN_V2`

## Purpose and audience

Create a concise local-review implementation report for Duho and the NebulaMind team. The video explains how Kun's oversight report was converted into bounded implementation under Hwao's coordination, what Tori verified, what execution actually completed, and which release gates remain separate.

This V2 supersedes the earlier local `KUN_REPORT_TORI_PROGRESS_REVIEW_V1.mp4` only as a status report. V1 correctly said cleanup and status-map execution were still held at its freeze time; later receipts now prove those two bounded actions completed after explicit approval.

## Acceptance matrix

| Requirement | Contract |
|---|---|
| Duration | 100 seconds |
| Aspect / media | 1280×720, 16:9, H.264/AAC, 30 fps, fast-start |
| Audio | Clearly female narration only; `en-US-EmmaNeural`; no music |
| Captions | Burned-in narration plus external SRT, both derived from exact narration |
| Presenter | Approved synthetic Flow astronomer master portrait; silent opening and silent outro only |
| Lip-sync | Presenter is never visible while narration is audible; no false speaking animation |
| Visual style | Dark navy observatory, cyan/magenta accents, deterministic report cards and status maps |
| Required facts | Hwao preservation-first boundary; Tori Surveys custody chain; guarded deletion receipt; four-axis status/debate map PASS; private artifact boundary; remaining gates |
| Privacy | No secrets, `.env` contents, terminal logs, tokens, or private payloads on screen |
| Status honesty | Executed work, private review artifacts, and still-gated work must be visibly distinct |
| Publication | Local review artifact only; no upload, channel, website, cockpit, deploy, DB, Git, or visibility change |

## Source hierarchy

1. Frozen current receipts and generated outputs listed in `source_freeze.json`.
2. Fresh Hwao pane observation frozen in `HWAO_LIVE_ARTIFACT_FREEZE.md`.
3. Earlier Hwao wording guards only where they remain compatible with later authorized execution.
4. Older V1 video only as a validated renderer/presenter provenance source, never as current status truth.

The build compares every frozen source hash immediately before rendering and again before final mux. Any drift stops the build.

## Evidence/status matrix

| Claim | Current source | Status | Allowed wording | Forbidden implication |
|---|---|---|---|---|
| Preservation-first coordination | Hwao source-boundary verdict + Phase 4 ratification | Complete | Hwao preserved verified work and kept actions separately gated | Hwao authorized all remaining work |
| Surveys G3 review chain | G3 closure receipt | Unit closed, verified-PASS | two FAILs then unconditional PASS; Tori verified custody; Hwao closed | Surveys V2 landed on main |
| Guarded deletion | guarded deletion receipt | Executed after explicit approval | 18 quarantined debris files, 18 regenerable test DBs, and 2 primary caches removed; protected items retained | blanket cleanup or tracked deletion |
| Debate map | build receipt + map + validation | Docs-only built and PASS | 4 axes, 16/16 entries, 28 counterevidence items, 4 epistemic caps, 0 validation errors | map wired into product/trust scoring |
| Hwao artifact | fresh pane freeze | Private review artifact exists | captioned rendered-map capture exists; manual Share pending | public publication or live product proof |
| Remaining gates | G3 closure + G6 receipt | Held/closed separately | landing, wiring, prose, DB/runtime/publication remain separate gates | full release complete |

## Exact narration

### Scene 1 — Hwao coordination

"Hwao turned Kun's oversight into a preservation-first implementation plan. Completed evidence stayed intact, and each new action remained separately gated. That decision prevented a valid Claim Ledger contract from being rebuilt or silently overwritten."

### Scene 2 — Tori verification

"Tori tracked custody through the Surveys rework. Three fail-closed reviews recorded two failures before an unconditional pass across all ten acceptance items. Hwao closed the unit verified-PASS. The seven-file V2 remains frozen and uncommitted; landing it still needs separate approval."

### Scene 3 — guarded execution

"With explicit authorization, guarded deletion executed: eighteen quarantined debris files, eighteen regenerable test databases, and two primary pytest caches were removed. Eight protected caches and the secret-adjacent environment file stayed retained. No tracked file changed; the regeneration check passed four tests."

### Scene 4 — status/debate map

"Kun's docs-only implementation also built status and debate map version one from the frozen sixteen-entry claim ledger. Four axes preserve twenty-eight counterevidence items and four epistemic caps. The validator resolved every entry and returned PASS, with no database, Git, runtime, or publication action."

### Scene 5 — Hwao review artifact

"Hwao reviewed the implementation boundary and created a private, captioned capture of the rendered four-axis map: mechanism, prevalence, dominance debate, and simulation support. Manual sharing is still pending. The artifact reports the implementation; it does not prove that map wiring is live in the product."

### Scene 6 — release boundary

"This is real implementation progress, not a full release. Surveys landing, map wiring, reader-facing prose, database changes, runtime deployment, and public publication remain separate gates. The verified outputs are preserved; no additional action is implied by this report video."

## Scene table

| # | Duration | Audio | Dominant visual |
|---|---:|---|---|
| 0 | 3s | silence | Approved Flow astronomer portrait, title, V2 status |
| 1 | 13s | narration 1 | Hwao preservation-first decision path |
| 2 | 15s | narration 2 | Tori review chain: FAIL → FAIL → PASS → Hwao closed |
| 3 | 18s | narration 3 | Guarded deletion executed versus protected/retained |
| 4 | 16s | narration 4 | Four-axis map and exact validator metrics |
| 5 | 17s | narration 5 | Private artifact and manual-share boundary |
| 6 | 15s | narration 6 | Complete versus separately gated release actions |
| 7 | 3s | silence | Flow astronomer portrait; implementation verified, release gates retained |

Expected runtime: 100 seconds.

## Palette and typography

- Background: `#07101F`, `#0B1630`
- Cyan: `#35D9F2`
- Magenta: `#D95CFF`
- Success: `#4EE09A`
- Warning/held: `#F2C14E`
- Failure history: `#FF6B78`
- Body: `#EAF2FF`
- Muted: `#91A4C4`
- Typography: SF Mono

## Provenance and publication gate

Factual text/cards are rendered locally with Pillow and ffmpeg by a V2 adapter over the already-QA'd V1 renderer. Narration is Edge TTS `en-US-EmmaNeural`. The saved synthetic Flow astronomer master portrait is reused only during silence. No fresh generative video call is used.

The artifact remains local and review-only. Rendering does not authorize upload, publication, website integration, cockpit changes, runtime/deploy, DB changes, or Git writes.
