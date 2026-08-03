# COMPARISON — Goru three-options pilot (closure)
Packet: `goru-options-pilot-20260711T102412Z` · Compiled by Hwao 2026-07-11 · Coordinator role only
(no execution). Source of record: `tori/TORI_FINAL_COMPARISON_HANDOFF.md`
(sha256 `a4fe7f908b9b193b7574c006740151c70da91c1b7a29ca341651c02ce06434a4`, verified) and the
countersigned `WAVE_LEDGER.md`. Companion: `DECISION_MATRIX.md`.

## NON-EQUIVALENCE (verbatim, binding — DIRECTION §6)
> A surrogate/mock/benign-local PASS demonstrates only that an option's transport-free decision
> logic (state handling, target custody, fail-closed behavior, capture integrity, bounds) is sound
> against synthetic fixtures. It is NOT evidence that the option can obtain a Gemini Web Deep
> Research result, NOT a measure of anti-bot survival, NOT a Gemini success, and NOT authorization
> for any live Google/Gemini use. For OPTIONS 1 and 2 the live transport is banned under current
> policy, so no surrogate result can move them past REJECT-for-live. For OPTION-3, a benign PASS may
> only justify a SEPARATE, Duho-gated packet for its GUI/display/Accessibility mechanics — never a
> direct live run.

## 1. Bottom line
| Option | Mechanism | Live status (policy) | Surrogate class | Executed result | **Binding verdict** |
|---|---|---|---|---|---|
| OPTION-1 | gemini-webapi/bard-api RPC + `__Secure-1PSID/1PSIDTS` | INADMISSIBLE-LIVE | MOCK_ONLY | T1/T2/T3/T5 PASS, T4 FAIL † | **`REJECT_LIVE__SURROGATE_FAIL`** |
| OPTION-2 | stealth Playwright/Puppeteer + copied Chrome profile | INADMISSIBLE-LIVE | PAPER_ONLY_NOW | T1–T5 NOT_RUN | **`REJECT_LIVE__SURROGATE_NOT_RUN`** |
| OPTION-3 | virtual/dummy display + AppleScript/System Events | SEPARATELY-GATED-LIVE | SURROGATE_TESTABLE | T1/T2/T3/T5 PASS, T4 FAIL † | **`NEEDS_REWORK`** |

† T4 FAIL for both executed options is a pinned test-oracle contradiction authored into this packet,
not a defect in the options — see §4. **No option is authorized for live use. No separately gated
next step is authorized by this packet.**

## 2. Per-option detail
**OPTION-1 — `REJECT_LIVE__SURROGATE_FAIL`.** The live transport (undocumented Google RPC driven by
`__Secure-1PSID/1PSIDTS`) is banned, so it is rejected for live regardless of any surrogate outcome.
Its MOCK_ONLY surrogate (a loopback `127.0.0.1` canned-response server with the synthetic literal
`DUMMY_1PSID_DO_NOT_USE`, no real cookie/secret, no Google host) ran browserless and passed state
classification (T1), exact-target custody (T2), fail-closed walls (T3), and bounds/instrumentation
(T5). The first run was a logged harness defect (missing T5 session-state parent dir; preserved
immutably under `tests/results/OPTION-1_ATTEMPT1_HARNESS_DEFECT/`, note `b0378e16…`); exactly one
corrected rerun followed. T4 FAILed only on the §4 oracle contradiction. Receipt `ff665b7e…`
(22,146 B, loopback-only), Tori recheck `a960395…` = VALID.

**OPTION-2 — `REJECT_LIVE__SURROGATE_NOT_RUN`.** The live transport (a cloned live Chrome profile
plus stealth/anti-bot evasion) is banned. Even the surrogate was correctly refused execution: the
installed Playwright's configured Chromium resolves to a real `Google Chrome for Testing` binary, so
launching it would breach the packet-wide no-Chrome rule (DIRECTION §0) and contradict Goru's own
`no headless/stealth: YES` self-certification. Tori confirmed no Option-2 shim, runner, result
directory, browser/Chrome process, server, profile, marker, delegation, or network action ever
existed. Assessment is static only: analysis `9174d32c…`, dispatch `514aaa67…`. T1–T5 = NOT_RUN.

**OPTION-3 — `NEEDS_REWORK`.** The live form (virtual display + Accessibility/System Events + Chrome
+ Google) is separately gated and was not exercised. Its benign browserless lane (a `bs4` fixture
parser + dry-run state machine; no network, browser, System Events, Accessibility, display reconfig,
install, or kext) passed T1/T2/T3/T5 and FAILed T4 only on the §4 oracle contradiction. Because the
binding eligibility rule (DIRECTION §7) requires **every executed test to pass**, one FAIL — even a
spurious one — makes it ineligible for a separately gated next step under this packet. Receipt
`2923f8ac…` (24,320 B), Tori recheck `af9d1162…` = VALID, discovery doc `aac84ca7…` (documentation
only; no live display/Accessibility inspection).

## 3. Failure-mode coverage (the five weekend-macro defects)
Both executed options demonstrably close macro failure modes 1–3 (Pro+Deep-Research selection via
T1, Start-research-once/active-state via T1, wrong-target capture via T2's 9/9 exact-target echo).
Mode 4 (gates) is partially shown: the verification/billing/login **walls** are handled fail-closed
(T3 PASS), but the **marker-gate** portion was scored under the defective T4 oracle. Mode 5 (the
93-identical-hash pathology) was exercised under T4; the hash determinism/distinctness behavior was
not the cause of the T4 FAIL. Option 2, unexecuted, is assessed for all five only on paper.

## 4. Shared T4 root cause (packet-authoring defect)
Pinned fixture `fx_complete_marker_dup.html` (sha256 `3a00e029…`) ends with the marker → final
non-empty line = marker (true), marker count = 2. Pinned oracle `EXPECTED_VERDICTS.json`
(sha256 `863b0f18…`) demands count = 2 **and** `marker_is_final_nonblank_line: false` for that same
fixture — a self-contradiction. Both shims reported the fixture truthfully and were failed by the
inconsistent expectation. Both pins are byte-unchanged (verified at closure); nothing was mutated to
"rescue" a result. Remediation is a **new, explicitly Duho-approved packet revision** that fixes the
oracle (or the fixture) and re-pins by sha256, after which T4 can be re-run for the two executed
lanes. Only that revision could move Option 3 off `NEEDS_REWORK`; even then, per NON-EQUIVALENCE, the
ceiling is a separately gated design step, never live use.

## 5. Recommendation to Duho
1. **Options 1 and 2: closed, rejected for live** on policy grounds that no test can change.
2. **Option 3: the only candidate with a forward path**, but it needs a small packet revision to fix
   my T4 oracle bug before its benign logic can be judged clean. That is a local, browser-free fix.
3. **No live automation of Gemini Web is on the table from this pilot.** The verification hard stop
   is still uncleared and untouched by this packet; any future live step remains behind a separate,
   Duho-gated packet with the joint-recovery arming/custody gates as its floor.

## 6. Safety attestation (this closure)
No live, browser, network, Google/Gemini, System Events, Accessibility, display, install, or kext
action was taken to compile this comparison. No database, deploy/restart, git, cron, cloud, billing,
account, credential, public-cockpit, or publication write was made. All outputs are advisory and stay
under this packet root; every external ID/link from any lane remains quarantined; the 93 weekend-macro
outputs remain invalid/audit-only. Dashboard/cockpit status is addressed separately in the closure
report — the `WAVE_LEDGER` is an internal custody log, not the public cockpit.
