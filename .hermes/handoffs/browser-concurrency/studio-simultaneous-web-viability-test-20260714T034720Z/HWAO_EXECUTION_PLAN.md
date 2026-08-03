# HWAO_EXECUTION_PLAN — Flow + Deep Research viability test (C0–C3 staged execution)

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z` · Run captain: Hwao (sole coordinator). Authority: `USER_DIRECTION.md` (sha256 `822aa87f…de96`) — start-now for the local ladder; held gates listed there remain held and are re-listed in §6. Source of truth: `ledger/RUN_LEDGER.jsonl` (append-only, hash-chained, broker-epoch-ordered; verify with `broker/ledger.py <path> verify`).

## 1. Roles (per user role decision, binding)

Hwao — captain: rung entry/exit decisions, adjudication, ledger authority. **Tori** — Deep-Research-side correspondent + receipt verifier. **Yui** — Flow-side correspondent + *non-interference witness*: read-only confirmation before/after every rung that the user's active Flow window and default Chrome profile were untouched. **Goru / Garu / WonE** — helpers in the Hwao-scoped lanes of §3 only. Correspondents and helpers are never automatic browser writers; every write requires my designation in the ledger *plus* a broker lease. The deterministic broker (`broker/broker.py`, tests 13/13 green) owns target, account-submission, clipboard, focus, and the machine-wide desktop-control leases; all cua/AX/pointer/keyboard writes serialize under desktop-control; only DOM/CDP writers over the separate sandbox profiles may overlap.

## 2. Sandbox (already created; empty by construction)

`sandbox/profiles/writerA`, `sandbox/profiles/writerB` — dedicated **non-default** user-data directories, created empty; **no credential, cookie, token, or profile-content copying ever** (held gate). `sandbox/downloads/writerA`, `sandbox/downloads/writerB` — per-writer download dirs. All canary browser instances launch ONLY on these profiles, windowless/headless or minimized, and never touch the default Chrome instance or the user's Flow window.

## 3. Staged execution C0 → C3 (three comparable passes per rung; Kun's patched design governs invariants/receipts)

Standing user approval for C0–C3 exists in `USER_DIRECTION.md`; each rung still needs my recorded `rung_entry` ledger entry, granted only after Tori's receipt verification of the prior rung.

- **C0 — dual-bridge soak** (no browser at all): Goru and Garu each hold an idle computer-use bridge for N=20 min (Hwao-set, recorded in MANIFEST), sampling `list_apps` count and capture dimensions on a fixed cadence; WonE assembles `BRIDGE_TELEMETRY.jsonl` + receipts. Pass: zero `list_apps=0`, zero `0x0`, heartbeats continuous, desktop-control timeline EMPTY, 3× byte-comparable.
- **C1 — dual read-only capture, different non-browser apps:** Goru observes app/window A, Garu app/window B (read leases only); WonE runs assertions. Pass: stable fingerprints, no cross-target reads, frontmost/clipboard/window-count unchanged, no bridge-loss signature.
- **C2 — dual read-only capture, sandbox browser targets:** WonE launches two sandbox instances (writerA/writerB profiles, `--no-first-run`, no startup window where possible, CDP on ephemeral ports via `DevToolsActivePort`) under target leases; Goru/Garu hold read leases on distinct targets. No navigation beyond about:blank/local file, no keyboard/clipboard/focus/desktop leases. Pass per Kun C2.A1–A8.
- **C3 — DOM/CDP parallel action + broker-serialized cua action:** Goru (writerA) and Garu (writerB) perform deterministic non-submitting DOM/CDP actions on their own leased targets — allowed to overlap (the parallel path). WonE performs the single scripted cua/AX action on a sandbox window ONLY while holding the exclusive desktop-control lease; a deliberately queued second cua request must be denied/queued (broker proof). Yui witnesses Flow-window/default-Chrome untouched throughout. Pass per Kun C3.A1–A10 incl. `DOM_CDP_TIMELINE` / `DESKTOP_CONTROL_TIMELINE` overlap report.
- **C4 — PREPARE ONLY:** author the C4 compose-only run sheet and freeze-drill checklist; **stop before** any sign-in, security/permission prompt, CAPTCHA/challenge, submit-like action, or quota-bearing action. Execution of C4 with fresh authentication is a held gate.

Receipts per rung land in `receipts/c<N>/pass<K>/` (MANIFEST, LEASE_JOURNAL, TARGET_SNAPSHOTS, GLOBAL_RESOURCES, BRIDGE_TELEMETRY, DESKTOP_CONTROL_TIMELINE, DOM_CDP_TIMELINE, ASSERTIONS) and are hash-logged to the run ledger; Tori verifies; Yui countersigns non-interference.

## 4. Ledger and split-brain rules

One ledger, `ledger/RUN_LEDGER.jsonl`; every grant/action/receipt/decision is an entry; broker epochs order all claims. Correspondents write observations to the ledger only — never re-scope lanes, never coordinate peer-to-peer on state. Any cross-side or receipt disagreement is STOP-class: freeze via broker, adjudication by Hwao, entry recorded. Scope changes relayed through a correspondent bind only after my confirming ledger entry.

## 5. Emergency stop

Anyone — Yui, Tori, any helper, Hwao, or the user — may declare STOP at any moment. Effect: `broker.freeze()` (all live leases on both sides revoked instantly, no final action), ledger `emergency_stop` entry, all lanes halt, artifacts preserved read-only. **Resume requires a fresh user gate from Duho — no one else may reset the broker.** Automatic freeze triggers: any invariant breach; any `list_apps=0`/`0x0`; any permission/security prompt, CAPTCHA, challenge, or sign-in surface; any evidence the default Chrome or Flow window was touched; any unleased desktop write; receipt non-comparability; correspondent disagreement.

## 6. Held gates (unchanged, re-affirmed)

Credential/cookie/token/secret copying or exposure · Google sign-in/account changes · handling any permission/security prompt · C4 execution if fresh authentication is needed · any Flow or Deep Research submission · any AI-credit/quota spend · Phase IV live overlap canary · DB writes, deploy/restart, git, publication, billing, cron, unrelated browser actions. Passing C0–C3 proves local mechanical viability only; it cannot prove same-account Flow+DR active-job overlap (that is Phase IV, separately gated).

## 7. Sequence from now

1. Tori relays the five briefs in `briefs/`; Yui/Goru/Garu/WonE write ACKs to `briefs/acks/` (protocol ACK before any participation — user direction §2).
2. Tori writes the ACK-verification receipt; I record `rung_entry C0` in the ledger.
3. C0 ×3 → Tori verify + Yui countersign → `rung_entry C1` → … → C3 ×3.
4. C4 prepare-only artifacts; then full-ladder review (Hwao + Tori) → viability report to Duho with the Phase-IV gate question.
