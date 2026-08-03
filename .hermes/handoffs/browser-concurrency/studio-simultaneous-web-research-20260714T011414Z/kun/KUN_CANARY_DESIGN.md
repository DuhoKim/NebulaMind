# KUN_CANARY_DESIGN — staged non-interference proof and bridge-loss diagnosis

Packet: `studio-simultaneous-web-research-20260714T011414Z` · Lane: Kun P2 · Research-only design. This document authorizes no launch, browser/profile creation, install, code change, service restart, account action, login, permission-dialog interaction, or live experiment.

Inputs consumed:
- `USER_DIRECTION.md`: observed collision problem and research-only boundaries.
- `HWAO_RESEARCH_PLAN.md` §4: Kun deliverable requirements.
- `goru/GORU_COLLISION_INVENTORY.md`: Flow collision points, OS-global resource matrix, R1/R2 bridge-loss symptoms.
- `TORI_EVIDENCE_NOTES.md` §§4.1-4.5 and `evidence/20_cua_driver_shared_desktop_contract.md`: Cua Driver 0.7.1 verifies target routing, but multiple MCP clients share screen, keyboard, pointer, accessibility tree, and recording machinery; two clicks contend; browser-tab writes should use DOM/CDP.
- `lana/LANA_ARCHITECTURE_SAFETY.md`: corrected minimum boundary, broker/lease contract, desktop-control lease, DOM/CDP-only parallel-write path, Flow replacement clauses, fail-closed policy.

## 0. Global canary rules

All canaries C0-C4 are future, permission-gated designs only.

**Repeatability rule.** Each rung must run exactly 3 independent repeats before promotion. A rung passes only when all 3 repeats produce byte-comparable receipts after normalizing the planned volatile fields: monotonic timestamps, PIDs, lease IDs, and absolute temp paths. All non-normalized receipt fields must match byte-for-byte across repeats.

**Stop rule.** Any single invariant breach, bridge-loss signature, unexpected native permission prompt, CAPTCHA/account challenge, target-identity ambiguity, unleased global-resource mutation, non-comparable receipt, or missing artifact stops the ladder. Later rungs remain unauthorized until Hwao reviews the failure package and the user gives a fresh gate for a revised design.

**Fail-closed rule.** A client that cannot re-verify its target identity must stop, release its lease, and emit a bridge-loss event. It must never fall back to frontmost app/window/tab.

**Parallel-write rule.** The only permitted parallel-write path is browser-native DOM/CDP action against separate browser processes/profiles and exact CDP target ids. cua/AX/pointer/keyboard actions are not independent parallel channels: every such write must hold the single machine-wide `desktop-control` lease, and no two such writes may overlap in time.

**Rollback baseline.** Every rung starts from an approved recorded baseline of target fingerprints, window counts, frontmost app, clipboard hash, download directory hashes, and active lease registry state. Rollback means no further automation, revoke all leases for the rung, preserve artifacts read-only, and verify the baseline resources are unchanged or explicitly accounted for by the rung's expected no-op/compose-only design.

**Evidence standard.** Each repeat produces a receipt bundle:
- `MANIFEST.json`: rung, repeat index, planned boundary, agent roles, normalized volatile-field list, artifact hashes.
- `LEASE_JOURNAL.jsonl`: grants, heartbeats, target re-verifications, actions, revocations, releases, bridge-loss events.
- `TARGET_SNAPSHOTS.jsonl`: target fingerprints before/during/after, including bundle id, user-data-dir label, native window id, CDP target id where applicable, URL/origin hash, and content hash when allowed.
- `GLOBAL_RESOURCES.jsonl`: frontmost app, clipboard hash only, window count, downloads directory hash, permission/challenge watch state.
- `BRIDGE_TELEMETRY.jsonl`: MCP session lifecycle, cua-driver session id, PID lineage, list/capture dimensions, driver health markers, and cua shared-desktop state labels.
- `DESKTOP_CONTROL_TIMELINE.jsonl`: every planned or denied cua/AX/pointer/keyboard write, its `desktop-control` lease id, start/end monotonic timestamps, holder pid, target fingerprint, and overlap check result.
- `DOM_CDP_TIMELINE.jsonl`: every browser-native DOM/CDP action, profile/process label, CDP target id, start/end monotonic timestamps, and proof that no desktop-control lease was required or touched.
- `ASSERTIONS.json`: deterministic assertion names with pass/fail and exact observed value.

## 1. Canary Ladder C0-C4

### C0 — Dual-process bridge soak

Purpose: directly target the R1/R2 process-local bridge-loss failure where capture returns `0x0` and `list_apps` returns zero while doctor remains green.

Preconditions:
- Explicit rung-entry user approval exists for C0.
- Two idle Hermes/computer-use processes are assigned as observers only.
- No browser driving, no target mutation, no keyboard/clipboard/focus/desktop-control lease, and no account surface.
- Bridge telemetry collection is configured before the soak starts.

Procedure design:
- Start two independent idle observer processes and hold their computer-use bridges for `N` minutes, where `N` is selected by Hwao before execution and recorded in `MANIFEST.json`.
- At a fixed cadence, each process performs only non-mutating bridge health checks: application enumeration and zero-interaction capture metadata collection.
- No observed app is activated, clicked, typed into, closed, navigated, or otherwise mutated.

Deterministic assertions:
- `C0.A1`: every scheduled `list_apps` sample from both processes has application count `> 0`.
- `C0.A2`: every scheduled capture metadata sample from both processes has width `> 0` and height `> 0`.
- `C0.A3`: no sample contains the R1/R2 signature: `list_apps=0` or capture dimensions `0x0`.
- `C0.A4`: both bridge sessions maintain continuous heartbeat coverage for the full `N` minutes.
- `C0.A5`: no keyboard, clipboard, focus, desktop-control, browser, profile, account, or download resource is leased or mutated.
- `C0.A6`: all 3 repeat receipt bundles are byte-comparable after approved normalization.

Abort gate:
- Abort immediately on any `list_apps=0`, `0x0` capture, missed heartbeat beyond the declared tolerance, process crash, or unplanned global-resource mutation.

Rollback gate:
- Revoke observer leases, preserve both process logs, verify no browser/profile/account/download state was touched, and mark the ladder stopped until the bridge-loss diagnosis protocol in §2 is reviewed.

Evidence capture:
- Full `BRIDGE_TELEMETRY.jsonl` with per-process session lifecycle, PID/PPID, sample cadence, dimensions, app-count values, and health markers.
- `LEASE_JOURNAL.jsonl` proving no write/global leases.
- Empty `DESKTOP_CONTROL_TIMELINE.jsonl` proving no cua/AX/pointer/keyboard write was attempted during the dual-bridge read-only soak.
- `ASSERTIONS.json` for C0.A1-C0.A6.

### C1 — Dual read-only capture, different apps

Purpose: prove two read-only agents can observe different non-browser apps without AX/session interference before any same-browser test.

Preconditions:
- C0 has passed 3x with byte-comparable receipts.
- Explicit rung-entry user approval exists for C1.
- Two stable non-browser app/window targets are selected and fingerprinted without mutation.
- Agents hold read-only leases on different app/window targets; no keyboard/clipboard/focus/desktop-control leases.

Procedure design:
- Observer A captures metadata and allowed content hash for app/window target A.
- Observer B captures metadata and allowed content hash for app/window target B.
- Both observers run concurrently for the declared duration and cadence.

Deterministic assertions:
- `C1.A1`: target A fingerprint remains stable for observer A across the repeat.
- `C1.A2`: target B fingerprint remains stable for observer B across the repeat.
- `C1.A3`: observer A never records observer B's target as its leased target, and observer B never records observer A's target as its leased target.
- `C1.A4`: all captures have dimensions `> 0`; no `list_apps=0` event occurs.
- `C1.A5`: frontmost app hash, clipboard hash, and window count are unchanged from baseline.
- `C1.A6`: no write/global-resource lease is granted.
- `C1.A7`: `DESKTOP_CONTROL_TIMELINE.jsonl` contains no cua/AX/pointer/keyboard writes.
- `C1.A8`: all 3 repeat receipt bundles are byte-comparable after approved normalization.

Abort gate:
- Abort on target swap, ambiguous target identity, any `0x0` capture, `list_apps=0`, frontmost/clipboard/window-count change, or non-comparable receipt.

Rollback gate:
- Revoke read leases, preserve evidence, verify both target fingerprints return to baseline, and keep C2 unauthorized until C1 evidence is reviewed.

Evidence capture:
- Per-observer target snapshots, capture metadata, bridge telemetry, global-resource hashes, and assertion results.

### C2 — Dual read-only capture, same browser at Lana's chosen boundary

Purpose: prove read-only observation of browser targets is stable at the boundary Lana selected before any driving occurs.

Preconditions:
- C1 has passed 3x with byte-comparable receipts.
- Explicit rung-entry user approval exists for C2.
- Browser targets are already available under the approved boundary; this design does not create profiles, launch browsers, log in, or navigate.
- Per Lana, read-only agents may use window/target-scoped read addressing inside one shared instance only if C0/C1 were green; if Hwao chooses the conservative path, C2 uses separate existing process/profile targets instead.
- No keyboard, clipboard, focus, navigation, close, submit, or download action is permitted.
- No desktop-control lease is permitted; C2 remains read-only even if the capture mechanism uses cua/AX/recording machinery.

Procedure design:
- Observer A holds a read lease on browser target A: native window id plus CDP target id where available.
- Observer B holds a read lease on browser target B at the selected boundary.
- Both observers capture target metadata and allowed hashes at the declared cadence.

Deterministic assertions:
- `C2.A1`: each observer's leased browser target id remains constant unless the design declares a read-only expected rotation; no undeclared rotation is allowed.
- `C2.A2`: URL/origin hash for each target remains unchanged.
- `C2.A3`: content hash for each target remains unchanged when the page is declared static; if dynamic content is unavoidable, only the declared dynamic fields are normalized.
- `C2.A4`: window count is unchanged.
- `C2.A5`: frontmost app and clipboard hash are unchanged.
- `C2.A6`: no close, activate, navigate, keyboard, clipboard, download, login, or account action appears in the lease journal.
- `C2.A7`: no `list_apps=0` or `0x0` capture occurs.
- `C2.A8`: `DESKTOP_CONTROL_TIMELINE.jsonl` contains no cua/AX/pointer/keyboard writes; browser observation may use read-only capture only.
- `C2.A9`: all 3 repeat receipt bundles are byte-comparable after approved normalization.

Abort gate:
- Abort on target-id drift, URL/origin hash change, window-count change, unleased global-resource mutation, account/challenge prompt, bridge-loss signature, or non-comparable receipts.

Rollback gate:
- Revoke read leases, preserve artifacts, verify target fingerprints and global-resource hashes match baseline, and keep C3 unauthorized pending review.

Evidence capture:
- Browser target fingerprints, CDP target ids if available, native window ids, URL/origin hashes, content hashes, bridge telemetry, global-resource hashes, and assertion results.

### C3 — DOM/CDP parallel action plus broker-serialized cua action

Purpose: distinguish the only parallel-write path from the serialized desktop path. Browser-native DOM/CDP writes over separate profiles may overlap with read-only observation and with another DOM/CDP action. cua/AX/pointer/keyboard writes must serialize under the single machine-wide desktop-control lease and must not overlap with any other cua/AX/pointer/keyboard write.

Preconditions:
- C2 has passed 3x with byte-comparable receipts.
- Explicit rung-entry user approval exists for C3.
- DOM/CDP writer target and observer target are assigned at Lana's minimum boundary for one driving plus one reading: separate process/profile with distinct non-default `user-data-dir`, or a stricter boundary chosen by Hwao.
- Any second DOM/CDP writer, if included in the approved C3 repeat, also uses a separate browser process/profile and exact CDP target id.
- Any cua/AX/pointer/keyboard writer has a single write lease on its exact target plus the exclusive `desktop-control` lease; the observer has only a read lease.
- Clipboard use is banned unless a clipboard lease fallback is explicitly approved for the rung; no authenticated submission is allowed.

Procedure design:
- Phase C3-DOM: one or two writers perform deterministic, non-submitting browser-native DOM/CDP actions against only their leased CDP targets in separate profiles. These actions are allowed to overlap in time because they do not use cua/AX/pointer/keyboard desktop machinery.
- Phase C3-CUA: any cua/AX/pointer/keyboard action is deliberately brokered through the `desktop-control` lease. A second cua/AX/pointer/keyboard action request, if present in the design, must be denied or queued until the first lease is released.
- Observer continuously samples its own target fingerprint, URL/window id/content hash, bridge health, and whether a desktop-control lease is live.
- Global resources are sampled before, during, and after the writer action.

Deterministic assertions:
- `C3.A1`: observer target URL/origin hash is unchanged.
- `C3.A2`: observer native window id and CDP target id are unchanged.
- `C3.A3`: observer content hash is unchanged except for predeclared dynamic fields.
- `C3.A4`: frontmost app is unchanged for every process that does not hold a focus lease.
- `C3.A5`: clipboard hash is unchanged; if a clipboard fallback was approved, the final hash equals the baseline hash and intermediate clipboard ownership is fully journaled.
- `C3.A6`: global window count is unchanged unless the writer action declares an expected delta on the writer's leased window only.
- `C3.A7`: every DOM/CDP write is recorded in `DOM_CDP_TIMELINE.jsonl` with a separate profile/process label and exact CDP target id; no DOM/CDP write acquires or requires the `desktop-control` lease.
- `C3.A8`: overlapping write intervals are permitted only when every overlapping write is browser-native DOM/CDP over separate profiles. The overlap report must show zero overlapping cua/AX/pointer/keyboard writes.
- `C3.A9`: every cua/AX/pointer/keyboard write is recorded in `DESKTOP_CONTROL_TIMELINE.jsonl` with a live `desktop-control` lease id covering the full start/end interval.
- `C3.A10`: for every pair of cua/AX/pointer/keyboard writes, intervals are non-overlapping: `end_i <= start_j` or `end_j <= start_i`. Any denied/queued second request must be journaled as denied/queued before execution, not executed concurrently.
- `C3.A11`: no action in the journal references front window, active tab, close-all, global System Events keystrokes, unleased desktop-control, or unleased downloads.
- `C3.A12`: writer target re-verification succeeds before every writer action, whether DOM/CDP or cua.
- `C3.A13`: no `list_apps=0`, `0x0` capture, target ambiguity, permission prompt, CAPTCHA, or account challenge occurs.
- `C3.A14`: all 3 repeat receipt bundles are byte-comparable after approved normalization.

Abort gate:
- Abort on any observer target mutation, frontmost change without focus lease, clipboard hash drift, unexpected window-count change, unleased action, target re-verification failure, bridge-loss signature, account/challenge prompt, non-comparable receipt, DOM/CDP write without exact CDP target/profile proof, cua/AX/pointer/keyboard write without desktop-control lease, or any overlapping cua/AX/pointer/keyboard write intervals.

Rollback gate:
- Revoke writer, observer, DOM/CDP, and desktop-control leases; stop further actions; preserve audit journal, desktop-control timeline, DOM/CDP timeline, and target snapshots; verify observer/global resources match baseline; require Hwao review before any C4 approval.

Evidence capture:
- Broker audit journal, `DOM_CDP_TIMELINE.jsonl`, `DESKTOP_CONTROL_TIMELINE.jsonl`, overlap report proving zero overlapping cua/AX/pointer/keyboard writes, before/during/after target snapshots for writer and observer, frontmost/clipboard/window/download hashes, bridge telemetry, and C3 assertion results.

### C4 — Dual authenticated-surface dry-run, zero submissions

Purpose: prove two authenticated surfaces can be present in isolated browser/process/profile targets without submissions, quota changes, or challenge escalation before any live authenticated use is considered.

Preconditions:
- C3 has passed 3x with byte-comparable receipts.
- Explicit rung-entry user approval exists for C4.
- Authenticated surfaces already exist in approved isolated targets; this design does not log in, create profiles, solve challenges, change accounts, or submit work.
- Account-submission lease is not granted. Compose-only leases are granted with a hard zero-submit invariant.
- Same-account plus shared-egress freeze policy from Lana is active.

Procedure design:
- Agent A opens or observes an already-authenticated compose surface in target A and performs only deterministic compose-only, reversible local field preparation allowed by the rung.
- Agent B does the same in target B.
- Both agents watch for quota indicators, submit buttons/state, account prompts, CAPTCHA, permission prompts, and challenge banners without interacting with them.

Deterministic assertions:
- `C4.A1`: zero submit/send/generate/research/finalize actions occur in the lease journal.
- `C4.A2`: account-submission lease is never granted.
- `C4.A3`: each authenticated target's URL/origin hash and window/target ids remain bound to the original lease.
- `C4.A4`: no quota/credit counter change is observed in any allowed surface hash or metadata field.
- `C4.A5`: no CAPTCHA, unusual-traffic, account challenge, permission prompt, or login prompt appears; if one appears, it is recorded only as a freeze event and not interacted with.
- `C4.A6`: clipboard hash, frontmost app, and unrelated window count remain unchanged.
- `C4.A7`: no downloads are created outside the lease-owned download directories; compose-only dry-run creates no final artifacts unless explicitly declared.
- `C4.A8`: no `list_apps=0`, `0x0` capture, or target re-verification failure occurs.
- `C4.A9`: any compose-only write uses browser-native DOM/CDP over separate profiles; any cua/AX/pointer/keyboard write is prohibited unless explicitly reclassified as a serialized desktop-control action by Hwao before the rung.
- `C4.A10`: all 3 repeat receipt bundles are byte-comparable after approved normalization.

Abort gate:
- Abort and freeze all same-account plus shared-egress leases on any account/challenge/prompt event, any submit-like action, quota indicator change, target ambiguity, bridge-loss signature, global-resource mutation, unapproved cua/AX/pointer/keyboard write, overlapping desktop-control interval, or non-comparable receipt.

Rollback gate:
- Revoke all target and compose-only leases, preserve challenge/prompt evidence without interacting, verify no account-submission lease existed, verify no quota-affecting action is journaled, and require a fresh user gate before any live authenticated use.

Evidence capture:
- Authenticated target fingerprints, zero-submit lease journal, `DOM_CDP_TIMELINE.jsonl`, `DESKTOP_CONTROL_TIMELINE.jsonl` if any serialized desktop action is explicitly approved, prompt/challenge watch records, quota/credit metadata hashes where allowed, global-resource hashes, bridge telemetry, and assertion results.

## 2. Bridge-loss reproduction and diagnosis protocol

Goal: localize the process-local bridge loss documented by Goru and Tori: `list_apps=0` and `0x0` capture while `computer-use doctor` remains green. This protocol is still design-only and may run only after explicit approval.

Required logging channels:
- **MCP session lifecycle:** session creation time, session id, transport endpoint label, reconnects, disconnects, errors, close codes, heartbeat send/receive times, and owning agent id.
- **cua-driver session lifecycle:** driver app/binary identity, driver version, session id, per-session config ownership, bridge connection open/close events, and any multi-session warnings.
- **Shared-desktop lifecycle:** desktop-control lease grant/deny/queue/release events, holder pid, monotonic start/end timestamps, and whether the action touched cua, AX, pointer, keyboard, or recording machinery.
- **PID lineage:** agent PID/PPID, driver PID/PPID, gateway PID/PPID, process start time, process exit status, and parent changes.
- **Capture/list telemetry:** every `list_apps` count, capture dimensions, target app/window id requested, target app/window id returned, duration, timeout, and error code.
- **Health correlation:** doctor status snapshots before and after failure, Accessibility/Screen Recording permission status labels, CPU/memory pressure labels, and concurrent automation activity labels.
- **Broker correlation:** lease id, epoch, holder pid, target fingerprint, action type, re-verification result, and revocation state at the exact sample before and after failure.
- **Timebase:** monotonic timestamp and wall-clock timestamp for every record, plus a run-start synchronization marker emitted by both processes.

Diagnosis matrix:
- If one process reports `list_apps=0` or `0x0` while the other stays healthy, classify as process-local bridge loss.
- If both processes fail in the same sampling interval, classify as shared driver/session/system failure until proven otherwise.
- If doctor remains green while one or both sessions fail, classify as application/session-layer bridge loss rather than permission/system absence.
- If target re-verification fails before capture/list failure, classify as target-lifecycle loss, not bridge loss.
- If a missed heartbeat precedes the first bad sample, classify as transport/session instability.
- If a concurrent lease revocation or broker epoch change precedes the bad sample, classify as expected fail-closed behavior unless bridge telemetry also shows `list_apps=0` or `0x0`.
- If two cua/AX/pointer/keyboard write intervals overlap, classify as broker serialization failure, not as acceptable cua concurrency.
- If two browser-native DOM/CDP write intervals overlap across separate profiles and no desktop-control lease is touched, classify as intended parallel browser-write behavior unless target or global-resource assertions fail.

Deterministic failure package:
- First bad sample plus five samples before and after from every logging channel.
- PID lineage snapshot for all involved processes.
- Lease registry snapshot with stale/revoked/live state.
- Assertion file naming the first violated invariant.
- A minimal timeline sorted by monotonic time, with no cookies, tokens, browsing history, profile contents, unrelated tabs, or credential-bearing data.

No-go diagnosis outcomes:
- Any unexplained `list_apps=0` or `0x0` event blocks C1-C4.
- Any bridge failure that can be masked by falling back to frontmost/active-tab blocks all writer rungs until fail-closed enforcement is proven.
- Any evidence that two long-lived sessions increase bridge-loss rate blocks shared-login-session concurrency and escalates the boundary decision back to Hwao/Lana.
- Any overlapping cua/AX/pointer/keyboard write blocks C4 and live use until the desktop-control lease is corrected and C3 is rerun.
- Any claim of parallel writes that is not browser-native DOM/CDP over separate profiles is a no-go.

## 3. Rollback and no-go gates

Per-rung entry approval:
- C0 requires explicit approval after Hwao accepts this design.
- C1 requires C0 PASS artifacts and explicit approval.
- C2 requires C1 PASS artifacts and explicit approval.
- C3 requires C2 PASS artifacts and explicit approval.
- C4 requires C3 PASS artifacts and explicit approval.
- Live authenticated use is not reachable from this packet. It requires C0-C4 PASS artifacts and a fresh user gate after Hwao/Tori review.

Rung-PASS artifact set:
- Three complete receipt bundles for the rung.
- One normalized byte-comparison report proving the 3 repeats match under the declared normalization rules.
- One assertion summary showing every invariant passed.
- One bridge-loss summary showing zero `list_apps=0`, zero `0x0`, zero target re-verification failures, or an explicitly expected and reviewed fail-closed event.
- For C3 and any later rung with writes: one DOM/CDP-vs-desktop-control report proving that all overlapping writes were DOM/CDP over separate profiles and that all cua/AX/pointer/keyboard writes were serialized under one desktop-control lease.
- One rollback verification showing resources returned to baseline or only approved expected no-op/compose-only state.

No-go conditions:
- Any single invariant breach in any repeat.
- Any missing evidence artifact.
- Any account/challenge/permission prompt in C0-C3; in C4 it is captured only as a freeze event and remains a no-go for live use.
- Any quota/credit-affecting action or submission in C4.
- Any use of close-all, front-window/active-tab fallback, global System Events keystrokes, unleased clipboard mutation, shared download sink, or unleased focus.
- Any cua/AX/pointer/keyboard write without the exclusive desktop-control lease.
- Any overlapping cua/AX/pointer/keyboard writes, including two clicks that contend for the shared desktop.
- Any assertion that cua-driver multi-client support provides independent parallel desktop control.
- Any parallel-write path other than browser-native DOM/CDP over separate browser profiles.
- Any inability to explain a bridge-loss signature from the required logs.

Fresh-user-gate rule:
- Passing C0-C4 proves only that the designed non-interference canaries produced acceptable receipts. It does not authorize live authenticated Flow, Gemini, Deep Research, or any other account-affecting workflow.
- After C4 passes, Hwao and Tori must review the full artifact set and present a recommendation. Only then may the user grant a fresh, explicit live-use gate for a separately scoped implementation or operation.
- Without that fresh user gate, all authenticated live use, submissions, profile creation, login, browser launch, service change, code change, and account-affecting actions remain prohibited.

KUN_SIMWEB_DONE_20260714T011414Z
