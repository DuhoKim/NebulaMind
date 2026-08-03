# HWAO_RESEARCH_PLAN — true simultaneous web operation on the Mac Studio (research only)

Packet: `studio-simultaneous-web-research-20260714T011414Z` · Hwao coordinates only. Research-only boundaries of `USER_DIRECTION.md` bind every lane verbatim: no browser driving (and never Chrome during Flow work), no installs, no browser/profile creation, no code/service/account/login/permission-dialog changes, no live experiments; read-only local inspection allowed; web research via non-GUI `web_search`/`web_extract` of official sources only; never expose cookies, tokens, profile contents, browsing history, or unrelated tabs. End state: `HWAO_FINAL_RECOMMENDATION.md` (a recommendation + permission-gated implementation plan) and `TORI_VERIFIED_SYNTHESIS.md` — no implementation.

## 0. Shared protocol (all lanes)

- **ACK** per role table in `<lane>/ACK.md` before work. Write areas: `lana/`, `goru/`, `kun/`, `tori/` + shared `evidence/` (Tori-owned); temp as `<lane>/_tmp_*`.
- **Evidence standard:** every external claim carries source URL + access date + a ≤50-word quote + product/version; official domains only (developer.chrome.com, chromium.org / chromium source docs, playwright.dev, developer.apple.com, the cua-driver official repo/docs, support.google.com / policies.google.com). Every local claim carries file path + line ref (or command + output excerpt). Unknown = say UNKNOWN; never infer product behavior from memory when a doc can be cited.
- **Local read-only rules:** process lists, command-line flags, `ls`/`stat` of paths, LaunchAgent listings, and driver-script source reading are allowed. Profile internals are NOT: no reads of Cookies/History/Login Data/Preferences contents — existence and mtime of lock files only. If a step would require launching, installing, logging in, or clicking anything: STOP and record.
- **Question map:** Q1/Q4 → Tori · Q2/Q5/Q6 → Lana · Q3 → Lana (policy) + Goru (local surfaces) · Q7 → Kun.
- **Sequence:** P1 Goru + Tori in parallel → P2 Lana + Kun (consume P1 outputs) → P3 Hwao `HWAO_FINAL_RECOMMENDATION.md`, then Tori `TORI_VERIFIED_SYNTHESIS.md` (verifies every recommendation claim against lane evidence). Lane completion markers: `<LANE>_SIMWEB_DONE_20260714T011414Z`.

## 1. GORU brief — local collision inventory (P1; read-only local; no network)

**Mission:** enumerate every concrete mechanism by which two agents on this Studio can currently interfere through web automation, and list candidate mechanical isolation controls that exist locally today (no installs).

Deliver `goru/GORU_COLLISION_INVENTORY.md`:
1. **Flow/Veo driver dissection:** locate the current driver script(s) (start under `/Users/duhokim/HermesOps/scripts/` and any LaunchAgents referencing Flow/Veo); quote with line refs each offending operation named in the direction — front-window/active-tab targeting, `activate`, close-all-Chrome-windows, global clipboard use, global System Events keystrokes — plus any others found (delays/focus assumptions, hardcoded coordinates).
2. **Chrome instance/profile facts:** running Chrome process tree with full command-line flags (`ps`); profile directory paths in use; existence/mtime (NOT contents) of `SingletonLock`/`SingletonSocket`/`SingletonCookie` in each `user-data-dir`; window/tab count only if obtainable without driving Chrome (else UNKNOWN).
3. **Automation-stack census:** every cua-driver/Hermes/computer-use process and LaunchAgent; which OS-global resources each local automation consumer touches — keyboard (System Events), clipboard, focus/frontmost, screen recording, downloads directory, notification space — as a **collision matrix** (resource × consumer × exclusive/shared × evidence ref).
4. **Bridge-loss dossier:** collate the two documented process-local bridge losses (R1 `TORI_COMPUTER_USE_DIAGNOSTIC.md`/fresh-process receipts; R2 `TORI_R2_BROWSER_BRIDGE_BLOCKER.md`) — symptoms (`list_apps`=0, `0x0` capture, doctor GREEN), timing, process lineage — as reproduction input for Kun.
5. **Local isolation candidates (inventory only, no launches):** other installed browsers/bundles (`ls /Applications`), additional macOS user accounts, displays/Spaces, existing separate `user-data-dir`s — each tagged with which collision-matrix rows it would eliminate.
Prohibited: launching/driving anything, profile-content reads, network. Cap: standing 40% Antigravity window. Stop on any credential-bearing output — redact path-only and note.

## 2. TORI brief — official-doc evidence (P1; non-GUI web research only)

**Mission:** establish what Chrome, CDP, Playwright, macOS, cua-driver, and Google account policy OFFICIALLY support for concurrent automation. No Chrome driving; `web_search`/`web_extract` only; store raw extracts under `evidence/` with per-file URL+date+sha256.

Deliver `TORI_EVIDENCE_NOTES.md` (packet root, per direction) answering with citations:
1. **Chrome/Chromium:** multi-instance semantics of `--user-data-dir` (one running instance per user-data-dir; second launch on same dir delegates to the singleton); current remote-debugging constraints — notably the 2024+ change requiring a **non-default** `--user-data-dir` for `--remote-debugging-port`/`--remote-debugging-pipe`; `DevToolsActivePort` discovery; whether two Chrome instances with distinct user-data-dirs run truly independently (processes, locks, updates).
2. **CDP/Playwright:** CDP multi-client attach rules; Playwright browser **contexts** as isolation units (cookies/storage per context) vs persistent contexts (one per user-data-dir); `connectOverCDP` capabilities/limits; official guidance on concurrent contexts vs concurrent browsers; what Playwright says about attaching to a user's signed-in profile.
3. **macOS:** System Events keystrokes/clipboard = system-global (cite); AXUIElement per-app/per-window addressing (durable element/window identity vs frontmost); per-process Accessibility + Screen Recording permission model (does a new helper process inherit or re-prompt); anything official on multiple simultaneous AX clients.
4. **cua-driver:** official target-addressing model (app/window/element; is there durable tab/window identity?), documented multi-session/multi-process support, any documented bridge-loss/session-invalidation behavior or issue reports in the official repo.
5. **Google account concurrency:** official statements on multiple simultaneous sessions per account, automation-related "unusual traffic"/challenge triggers, and any Flow/Veo or Gemini usage-surface statements about concurrent use/quota sharing.
Each item ends VERIFIED (cited) / PARTIAL / UNKNOWN — no filling gaps by inference. Hard stops: any page requiring login → skip and record; no forums/blogs as primary evidence (may be noted as leads only).

## 3. LANA brief — architecture & safety (P2; consumes Goru + Tori outputs; local-only, no network)

**Mission:** decide the isolation architecture and the safety policy; specify — at contract level, zero implementation — what replaces the current colliding automation.

Deliver `lana/LANA_ARCHITECTURE_SAFETY.md`:
1. **Isolation-boundary decision matrix (Q2):** tab / window / profile / separate browser bundle / Playwright context / separate OS user / VM — scored per interference axis from Goru's collision matrix (input focus, keystrokes, clipboard, profile singleton, session/auth sharing, quota coupling, downloads, permission dialogs, CAPTCHA/challenge blast radius, crash/update blast radius), each score citing Goru/Tori evidence. Name the **minimum sufficient boundary** for (a) two read-only agents, (b) one driving + one reading, (c) two driving agents, with explicit reasoning.
2. **Broker/lease architecture (Q5):** a browser-broker design where every automation action requires a valid lease on an exact target — lease scopes ({browser-bundle, user-data-dir, window-id, tab/target-id} plus global-resource leases for {keyboard, clipboard, focus, downloads-dir}), single-writer exclusivity, TTL + heartbeat + revocation, **fail-closed on lease loss** (the R1/R2 bridge-loss lesson: a client that cannot re-verify its target identity must stop, never fall back to frontmost), an audit journal, and a no-lease-no-action invariant compatible with cua-driver's addressing model as Tori documents it.
3. **Authenticated-session & shared-state policy (Q3):** same-Google-account concurrency (recommendation expected: process/profile parallelism allowed, **account-level serialization of authenticated *submissions***, one authenticated surface active per account at a time unless Tori's evidence shows official support otherwise); quota coupling; downloads segregation per profile; clipboard = leased global resource (or banned in favor of direct input APIs per Tori's macOS findings); focus discipline (no `activate` outside a focus lease); permission-prompt/CAPTCHA/account-challenge = global hard-stop event that freezes ALL leases on that account, not just the triggering agent.
4. **Replacement contract for the Flow driver (Q6):** for each offending operation Goru quotes, the exact-target replacement requirement (close-all → close leased window-id only; front-tab targeting → durable tab/target-id addressing; global keystrokes → element-addressed input under keyboard lease; global clipboard → per-target injection or leased clipboard with save/restore), stated as testable contract clauses for a future gated implementation.
5. **FAIL_CLOSED_IMPACT register:** any place the proposed architecture relaxes a current de-facto safety property, flagged for Hwao.

## 4. KUN brief — reproducibility & canary design (P2; consumes Goru + Tori + Lana draft; design-only)

**Mission:** design (not run) the staged proof of non-interference and the bridge-loss reproduction protocol.

Deliver `kun/KUN_CANARY_DESIGN.md`:
1. **Canary ladder C0–C4**, each with preconditions, exact observables, deterministic pass/fail assertions, abort + rollback gate, and evidence-capture set: **C0** dual-process bridge soak (two idle Hermes processes hold computer-use bridges ≥N min; assert zero `list_apps`=0 / `0x0` events — directly targets the R1/R2 failure) · **C1** dual read-only capture, different apps · **C2** dual read-only capture, same browser different windows/instances (per Lana's chosen boundary) · **C3** one driving agent under lease + one observing agent (invariants: observer's target URL/window-id/hash unchanged; frontmost app unchanged for non-focus-lease holder; clipboard hash unchanged; window count unchanged) · **C4** dual authenticated-surface dry-run, zero submissions (compose-only), account-challenge watch. Every canary 3× repeatable with byte-comparable receipts; any single invariant breach = ladder STOP.
2. **Bridge-loss reproduction/diagnosis protocol:** exact logging to finally localize process-local bridge loss (MCP session lifecycle, driver logs, PID lineage, timing correlation with other automation), designed from Goru's dossier.
3. **Rollback/no-go gates (Q7):** per-rung entry approval, what artifact set constitutes rung-PASS, and the rule that live authenticated use is reachable only after C0–C4 receipts + a fresh user gate.

## 5. Completion

All four lane reports + `TORI_EVIDENCE_NOTES.md` complete with markers → Hwao writes `HWAO_FINAL_RECOMMENDATION.md` (chosen boundary, broker/lease architecture, replacement contract, canary ladder, permission-gated implementation plan — implementation itself explicitly NOT authorized by this packet) → Tori writes `TORI_VERIFIED_SYNTHESIS.md` cross-checking every recommendation claim against lane evidence, flagging any unsupported claim. Stop conditions (all lanes): any action requiring install/launch/login/driving; any credential/cookie/token exposure risk; any ambiguity between "inspect" and "operate" — stop and escalate to Hwao.

HWAO_SIMULTANEOUS_WEB_PLAN_DONE
