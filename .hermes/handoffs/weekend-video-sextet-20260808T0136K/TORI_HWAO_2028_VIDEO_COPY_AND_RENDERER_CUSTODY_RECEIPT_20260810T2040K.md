# Tori custody receipt — 20:28 private cockpit copies and disclosed renderer actions

- Marker: `TORI_HWAO_2028_VIDEO_COPY_AND_RENDERER_CUSTODY_RECEIPT_20260810T2040K`
- Verified at: `2026-08-10T20:40:11+0900 KST`
- Video-copy authority disclosed by Hwao: Duho, verbatim `publish both to the cockpit`
- Video-copy verdict: `PASS_EXACT_BYTE_PRIVATE_COCKPIT_COPY_SELECTION`
- Renderer/code-action authority status: `DISCLOSED_BUT_SEPARATE_AUTHORITY_NOT_SHOWN`
- User-acceptance label: **not asserted**

## 1. Exact regate selection

### MZR anchor

Regate:

`reviews/TORI_MZR_ANCHOR_LITERATURE_BEAT_EXACT_HASH_REGATE_20260810T1754K.json`

Regate SHA-256:

`c2d9f1fcd9e36d44a0841fc56bf1a8366bc0347c24e988d596dd0c07b1f50c7d`

The regate binds exactly:

- candidate directory: `integrator/canaries/mzr-anchor-literature-beat-motion-fix-20260810T1705K`
- video: `mzr-anchor-literature-beat-canary-20260810T1705K.mp4`
- SHA-256: `47f71fc40e1f81f7e4374e7e867c07cc64f8595ad553137403bff7d52dbec547`
- duration: `239.348000s`

Copied destination:

`/Users/duhokim/HermesOps/cockpit/videos/c41-highz-mzr-calibration-anchored-narrated-20260810T2028.mp4`

Independent result:

- source/destination SHA-256 equal: yes
- source/destination size equal: `13,186,479` bytes
- source/destination duration equal: `239.348000s`

### Brightend

Regate:

`reviews/TORI_BRIGHTEND_LITERATURE_BEAT_EXACT_HASH_REGATE_20260810T1804K.json`

Regate SHA-256:

`a77e1cf66f42067d766a2c6cf8a8a95b554ee14a0eae88db7524f40177349cd0`

The regate binds exactly:

- candidate directory: `integrator/canaries/brightend-literature-beat-typography-fix-20260810T1748K`
- video: `brightend-literature-beat-canary-20260810T1748K.mp4`
- SHA-256: `6483525852a5fafbb41d82e4c9fba0dc7e98b4f8b7599007e2af0a379ef49dd7`
- duration: `273.782000s`

Copied destination:

`/Users/duhokim/HermesOps/cockpit/videos/c41-brightend-uvlf-archival-gap-narrated-20260810T2028.mp4`

Independent result:

- source/destination SHA-256 equal: yes
- source/destination size equal: `14,802,732` bytes
- source/destination duration equal: `273.782000s`

**Selection confirmation:** Hwao selected the correct Brightend candidate. The Tori regate binds `1748K / 648352...`, not the lexically older or same-byte siblings.

All three Brightend candidates remain present:

1. `1640K`: `49f1fe3dcf3fed69d0269c24fefddb67c45f6d558e34727d4b7ee5b823abc05d`, `14,764,748` bytes, `273.782000s`;
2. `qa-fix 1732K`: same `49f1fe3d...` bytes, `14,764,748` bytes, `273.782000s`;
3. `typography-fix 1748K`: `648352...`, `14,802,732` bytes, `273.782000s`.

## 2. Cockpit delta and private served bytes

Both destination mtimes are `2026-08-10 20:28:24 KST`.

Current cockpit MP4 count: `38`.

Both regates independently froze the prior cockpit manifest at `36` MP4s. The two 20:28 destinations are the only MP4s newer than the prior 16:27 copy. This supports the disclosed exact `+2` delta; no contrary file-level evidence was found.

Direct private served verification:

1. `https://duho-macstudio.taila27502.ts.net/cockpit/videos/c41-highz-mzr-calibration-anchored-narrated-20260810T2028.mp4`
   - HTTP 200
   - `content-type: video/mp4`
   - content length `13,186,479`
   - streamed SHA-256 `47f71fc40e1f81f7e4374e7e867c07cc64f8595ad553137403bff7d52dbec547`
2. `https://duho-macstudio.taila27502.ts.net/cockpit/videos/c41-brightend-uvlf-archival-gap-narrated-20260810T2028.mp4`
   - HTTP 200
   - `content-type: video/mp4`
   - content length `14,802,732`
   - streamed SHA-256 `6483525852a5fafbb41d82e4c9fba0dc7e98b4f8b7599007e2af0a379ef49dd7`

Publication registry:

- path: `/Users/duhokim/HermesOps/cockpit/videos/published.json`
- SHA-256: `41de05345ad354c28df3caea530b51d8fa126692ecac7423039fb6d93ff76979`
- current entries contain only the spin-parity publication record; neither 20:28 destination appears.

This proves no registry publication for the two files. Tori did not query YouTube/account APIs, so the stronger claim of no external upload remains Hwao's disclosed side-effect statement rather than an independently queried account fact.

Both regates retain:

- `video_reportable_now: false`;
- upload/public/Git gates closed;
- acceptance effect `NONE`;
- provisional and non-reportable pending Duho watch.

The fresh private-copy authority changes only the narrow cockpit-copy gate for the two named exact hashes. It does not alter those scientific/acceptance fields.

## 3. Correction to the reported title defect

Confirmed: there is no card-title defect in this finding. The card schema uses `name`, and the stale-visibility test preserved all card names. A probe for a nonexistent `title` key was a test-reading error, not a renderer defect.

## 4. Renderer/headline/idle-seat custody

### Current recovery state

Current tmux topology:

- session: `ge-renderer`
- pane shell PID: `42638`, started `2026-08-10 20:25:26 KST`
- renderer child PID: `42959`, started `2026-08-10 20:25:29 KST`
- command: `python3 tools/render_ge_autopilot_dashboard_v2.py --watch --interval 20`
- pane health: alive; renderer emits scheduled `health: watching` records

The current topology does use a persistent shell with the renderer as a child, so Ctrl-C no longer inherently destroys the tmux session.

The disclosed exact first outage interval (`20:16:50–20:20:56`) cannot be reconstructed from the current recreated tmux session alone. Current process evidence proves the final shell/renderer instance started at `20:25:26/20:25:29 KST`, consistent with the disclosed second session recreation.

### Classification-aware headline hunk

Backups/source:

- pre-headline backup SHA-256: `a3855b4dd9ced190dbe8f5af3733b0fb229c222679c046322680d4994c571d28`
- pre-idle backup SHA-256: `506bed43dc836268c304aeff1d57755788c4155c798ef03a1ecd795cb17087bc`
- current renderer SHA-256: `05b8382d123634d461d94727584389521320a5eeec3b575b3cd460fd3a89e1c1`
- selectable patch SHA-256: `e8c6364174fb32c80d3f9f337e40e83270349e269764d7cce52169f027875828`

`pre-headline → pre-idle` is exactly the source hunk from Tori's selectable patch. `git apply --reverse --check` passes against current source/test state, independently confirming the hunk is present. The new focused headline test file exists.

Live private output now shows the intended semantic split:

- Claude: `1%`, `FRESH LIVE METER`;
- Gemini app: `1%`, `FRESH LIVE METER`;
- Moonshot: `$33.30`, `FRESH LIVE METER`;
- Antigravity: `Stale`, `STALE HISTORICAL OBSERVATION`;
- Codex: `Stale`, `STALE HISTORICAL OBSERVATION`.

However, the applied hunk is **not a fully green integrated change**:

- focused headline behavior passes;
- wallet/Decision 2 integration run: `7 passed, 1 failed`;
- failing assertion: `test_per_card_freshness_is_bound_without_applying_headline_fallback` still requires `big is None`, while the applied hunk now correctly emits `10%`.

This is a stale test expectation in Tori's earlier wallet test, and it is a defect in the selectable packet Tori authored: the patch added its new test but did not update the prior assertion that explicitly encoded the unapplied state. It must be treated as a finding, not worked around. Tori made no source/test correction in this custody pass.

### Idle/seated seat fields

`pre-idle → current` adds only:

- capture of `interactive_sessions` from `crew_live()`;
- `seated_seats`;
- `idle_seats`;
- `seat_state_note`.

Current private output:

- `seated_seats`: `Goru, Kun, Lana, Tori, Yui`;
- `live_seats`: `Tori`;
- `idle_seats`: `Goru, Kun, Lana, Yui`;
- note says five seat sessions are present, one working, four idle.

The fields are live and distinguish present-idle from absent.

### Authority separation

The only exact authority supplied in this disclosure is Duho's `publish both to the cockpit`, which covers the two named media copies.

It does **not**, by itself, authorize:

- applying the headline source/test hunk;
- applying the idle-seat source change;
- renderer restarts/activation.

Moreover, the headline packet on disk said `Apply authority: NOT GRANTED` and required a separate later decision. No separate Duho authority for these renderer/code actions is supplied in this message.

Therefore this receipt records the headline/idle/restart actions as `DISCLOSED_BUT_SEPARATE_AUTHORITY_NOT_SHOWN`. It does not call them approved, accepted, or cleared. No rollback is performed without a fresh direction.

## 5. Tori safety ledger

This custody pass performed only read-only file/process/status/HTTP verification, local focused tests, and this handoff receipt.

Tori performed:

- cockpit/video copies: 0
- source/test edits: 0
- renderer/monitor restarts: 0
- provider/account/browser calls: 0
- public frontend/Baseline writes: 0
- registry/YouTube writes: 0
- Git commit/push/merge: 0
- cron/config/secret actions: 0
- deletion/rollback: 0
- user-acceptance assertions: 0
