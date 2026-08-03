# DECISION_MATRIX — Goru three-options pilot (COMPILED 2026-07-11 by Hwao)
Packet: `goru-options-pilot-20260711T102412Z`. Filled from countersigned Tori+Goru results
(handoff `tori/TORI_FINAL_COMPARISON_HANDOFF.md` sha256
`a4fe7f908b9b193b7574c006740151c70da91c1b7a29ca341651c02ce06434a4`, verified). Closed verdicts are
binding; FAIL is not reinterpreted as PASS.

## Non-equivalence clause (verbatim, binding — copied from DIRECTION §6)
> A surrogate/mock/benign-local PASS demonstrates only that an option's transport-free decision
> logic (state handling, target custody, fail-closed behavior, capture integrity, bounds) is sound
> against synthetic fixtures. It is NOT evidence that the option can obtain a Gemini Web Deep
> Research result, NOT a measure of anti-bot survival, NOT a Gemini success, and NOT authorization
> for any live Google/Gemini use. For OPTIONS 1 and 2 the live transport is banned under current
> policy, so no surrogate result can move them past REJECT-for-live. For OPTION-3, a benign PASS may
> only justify a SEPARATE, Duho-gated packet for its GUI/display/Accessibility mechanics — never a
> direct live run.

## A. Policy/admissibility matrix (fixed by DIRECTION §1; independent of test outcomes)
| Dimension | OPTION-1 gemini-webapi/bard-api RPC | OPTION-2 stealth Playwright + copied profile | OPTION-3 virtual display + System Events |
|---|---|---|---|
| Defining live transport | `__Secure-1PSID/1PSIDTS` + undocumented RPC | cloned profile + stealth vs anti-bot | display reconfig + Accessibility/System Events + Chrome |
| Cookie/secret access required (live) | YES → **banned** | YES (profile tokens) → **banned** | NO (but Chrome/Google → gated) |
| Profile read/copy (live) | NO | YES → **banned** | NO |
| Stealth/evasion (live) | partial (RPC bypass) | YES → **banned** | NO |
| Undocumented Google endpoint (live) | YES → **banned** | NO (real UI) | NO (real UI) |
| Install / kext / display reconfig (live) | NO | browser install possible | YES (virtual display) → **gated** |
| Accessibility/System Events (live) | NO | NO | YES → **gated** |
| **LIVE STATUS (current policy)** | **INADMISSIBLE-LIVE → REJECT-for-live** | **INADMISSIBLE-LIVE → REJECT-for-live** | **SEPARATELY-GATED-LIVE (not tested here)** |

## B. Surrogate feasibility & results matrix (COMPILED)
| Dimension | OPTION-1 | OPTION-2 | OPTION-3 |
|---|---|---|---|
| Surrogate lane | localhost mock HTTP (stdlib), synthetic tokens | localhost static page, fresh ephemeral profile, no stealth (only if stack already installed) | dry-run fixture harness (no Google/Chrome/SysEvents/display/install) + discovery doc |
| Surrogate class (Phase 0) | MOCK_ONLY | PAPER_ONLY_NOW | SURROGATE_TESTABLE |
| T1 state classification | PASS | NOT_RUN | PASS |
| T2 exact-target custody | PASS | NOT_RUN | PASS |
| T3 fail-closed walls | PASS | NOT_RUN | PASS |
| T4 capture integrity (anti-93-hash) | FAIL † | NOT_RUN | FAIL † |
| T5 bounds & instrumentation | PASS | NOT_RUN | PASS |
| Receipts reconciled (Tori) | VALID (recheck `a960395…`; receipt `ff665b7e…`, 22,146 B, loopback-only) | N/A no results (analysis `9174d32c…`, dispatch `514aaa67…`) | VALID (recheck `af9d1162…`; receipt `2923f8ac…`, 24,320 B) |

† **T4 FAIL is a pinned-oracle defect, not an option defect** — see §E. Both executed shims
deterministically and correctly extracted the dup-marker body (count 2, final line = marker).

## C. Five macro-failure-mode coverage (COMPILED)
| Failure mode | OPTION-1 | OPTION-2 | OPTION-3 |
|---|---|---|---|
| 1. Pro+Deep Research never selected | COVERED (T1 PASS) | NOT_RUN (paper analysis only) | COVERED (T1 PASS) |
| 2. Start research never clicked | COVERED (T1 PASS: PLAN_READY→START once, RUNNING→WAIT, ACK_NO_CONTROL→HARD_STOP, no re-click) | NOT_RUN (paper) | COVERED (T1 PASS) |
| 3. Wrong-tab / wrong-target capture | COVERED (T2 PASS, 9/9 exact-target echo) | NOT_RUN (paper) | COVERED (T2 PASS) |
| 4. No quota/marker/verification gates | PARTIAL — walls COVERED (T3 PASS: verification/billing/login→HARD_STOP); marker-gate blocked by the §E oracle defect | NOT_RUN (paper) | PARTIAL — walls COVERED (T3 PASS); marker-gate blocked by the §E oracle defect |
| 5. 93 identical-hash captures | exercised under T4 (overall FAIL); hash determinism/distinctness was NOT the failure cause | NOT_RUN (paper) | exercised under T4 (overall FAIL); hash determinism/distinctness was NOT the failure cause |

## D. Final verdicts (closed vocabulary; binding — from Tori handoff, not reinterpreted)
| Option | Verdict | Justification (evidence refs) | What it authorizes |
|---|---|---|---|
| OPTION-1 | `REJECT_LIVE__SURROGATE_FAIL` | Live INADMISSIBLE by policy (§A); surrogate T1/T2/T3/T5 PASS, T4 FAIL on the §E pinned-oracle defect. Receipt `ff665b7e…`, recheck `a960395…`. One logged harness-defect abort (`b0378e16…`) then one corrected rerun. | **Nothing live.** |
| OPTION-2 | `REJECT_LIVE__SURROGATE_NOT_RUN` | Live INADMISSIBLE by policy (§A); PAPER_ONLY_NOW (installed Playwright's Chromium resolves to real Google Chrome for Testing → launch would breach §0 no-Chrome). T1–T5 NOT_RUN; analysis `9174d32c…`, dispatch `514aaa67…`. No shim/runner/browser/profile/network existed. | **Nothing live.** |
| OPTION-3 | `NEEDS_REWORK` | Live SEPARATELY-GATED (§A). Benign browserless lane T1/T2/T3/T5 PASS, T4 FAIL on the §E pinned-oracle defect. Binding rule (DIRECTION §7) requires EVERY executed test to pass for eligibility, so **not** eligible. Receipt `2923f8ac…`, recheck `af9d1162…`, discovery `aac84ca7…`. | **Nothing live; NOT eligible for a separately gated next step under this packet.** |

## E. Root cause of the shared T4 FAIL (packet-authoring defect, remediation path)
The pinned fixture `tests/fixtures/fx_complete_marker_dup.html` (sha256 `3a00e029…`, unchanged) has
body lines: `marker` / `Section 2.` / `marker` — so marker **count = 2** and the **final non-empty
line IS the marker (true)**. The pinned oracle `tests/fixtures/EXPECTED_VERDICTS.json`
(sha256 `863b0f18…`, unchanged) asserts for that fixture `marker_count: 2` **and**
`marker_is_final_nonblank_line: false`. Those two pins contradict each other: a body ending in the
marker cannot have final-line = false. Both executed shims (Options 1 and 3) reported the fixture
truthfully and were therefore scored FAIL by an internally inconsistent expectation. This is a
defect in the pilot's own test oracle (Hwao-authored), **not** evidence that either option mishandles
duplicate markers or capture integrity.
- **No retrospective mutation.** Per Tori and DIRECTION, no pinned file was edited and no further
  rerun is authorized under this packet; results stand as adjudicated.
- **Remediation (requires a NEW explicitly Duho-approved packet revision):** correct the oracle so
  the dup-marker fixture's `marker_is_final_nonblank_line` matches the fixture (true), OR rebuild the
  fixture so the marker is not the final line; re-pin both by sha256; then re-run T4 for the two
  executed lanes. Only that revision could change Option-3's `NEEDS_REWORK` toward eligibility — and
  even a clean re-run authorizes at most a separately gated step, never live use (see NON-EQUIVALENCE).

**Reading guide for Duho.** Section A is policy and does not move with test results — Options 1 and
2 are rejected for live use because their transport is banned, full stop. Options 1 and 3 both showed
sound *non-transport* logic (state handling, exact-target custody, fail-closed walls, bounds); their
only failure is the §E oracle bug, which is mine to fix in a revision, not a defect in their code.
Option 2 was never executed and stands rejected for live on policy alone. The single forward path
this packet can surface is: fix the §E oracle in an approved revision, re-run Option 3's benign lane,
and — only if it then fully passes — consider a SEPARATE Duho-gated packet for its GUI/display
mechanics. Nothing here is a green light to automate Gemini.
