# TEST_DESIGN — bounded local pilot tests (binding; browser-free, network-free)
Packet: `goru-options-pilot-20260711T102412Z` · Fixtures and expected verdicts are sha256-pinned in
`MANIFEST.json` and READ-ONLY. Editing them is a hard-stop offense; Tori re-hashes before scoring.

## 1. Harness contract (per option, implemented by Goru as a thin shim if needed)
Each `LOCALLY_TESTABLE` option exposes one dry-run entrypoint:

    <entrypoint> --dry-run --fixture <path.html> --target <conversation-id> --out <dir>

Behavior: read the fixture from disk (NO network, NO browser), classify state, and write
`<dir>/verdict.json`:

    {
      "option": "OPTION-<n>",
      "fixture": "<basename>",
      "target_id": "<the id it believes it is addressing>",
      "state": "COMPOSER_IDLE|DR_ACTIVE|PLAN_READY|RUNNING|ACK_NO_CONTROL|COMPLETE|MARKER_MISSING|MARKER_DUPLICATE|VERIFICATION_WALL|BILLING_WALL|LOGIN_WALL|STALE_DOM|UNKNOWN",
      "planned_actions": ["<zero or more of: SELECT_DEEP_RESEARCH, SUBMIT_PROMPT, SNAPSHOT_PLAN, START_RESEARCH, WAIT, RELOAD_SAME_TARGET, CAPTURE_BODY, HARD_STOP>"],
      "extracted_body": "<relative path or null>"
    }

Rules: `--dry-run` must be the only mode invoked; planned_actions describe intent only — nothing is
executed; `UNKNOWN` state must always pair with `HARD_STOP` (fail-closed); exit code 0 iff a
verdict.json was written.

## 1a. Per-option surrogate transport bounds (safety-correct; DIRECTION §1, §5)
The harness contract above is uniform and transport-free. Each option's shim reaches it differently;
these are the ONLY authorized surrogate transports, all off-Google:
- **OPTION-1** — a localhost `python3 -m http.server`-class mock returning canned JSON; the wrapper's
  base URL is overridden to `http://127.0.0.1:<port>`; auth tokens are synthetic literals
  (`DUMMY_1PSID_DO_NOT_USE`). Never import, read, or accept a real cookie/token. If the wrapper
  cannot be pointed off Google without editing undocumented internals ⇒ `PAPER_ONLY_NOW`, no run.
- **OPTION-2** — drive a LOCAL fixture page (`file://` or `http://127.0.0.1`) with a fresh ephemeral
  browser profile created under `tests/results/OPTION-2/profile/` and deleted after; no stealth/
  evasion plugins, no copied profile, no Google. Runs ONLY if the automation stack is ALREADY
  present; **no install under this packet** ⇒ otherwise `PAPER_ONLY_NOW`.
- **OPTION-3** — the dry-run fixture harness only (decision logic), with NO Chrome, NO System
  Events/Accessibility, NO display reconfiguration, NO install, NO kext; plus a written
  `goru/OPTION-3_DISCOVERY.md` documenting (never invoking) the virtual-display/AppleScript
  mechanics. The live GUI/display/Accessibility path is out of scope and separately gated.

Network rule: zero outbound network in every test; the ONLY permitted socket is loopback
`127.0.0.1` for the Option-1 mock / Option-2 localhost lanes. Tori attests loopback-only from logs.

## 2. Fixture set (`tests/fixtures/`, synthetic — generic chat-product DOM, no Google assets)
| Fixture | Ground truth (see EXPECTED_VERDICTS.json) |
|---|---|
| `fx_composer_idle.html` | COMPOSER_IDLE; allowed: SELECT_DEEP_RESEARCH |
| `fx_composer_dr_active.html` | DR_ACTIVE; allowed: SUBMIT_PROMPT |
| `fx_plan_ready.html` | PLAN_READY; allowed: SNAPSHOT_PLAN, START_RESEARCH (once) |
| `fx_running.html` | RUNNING; allowed: WAIT |
| `fx_ack_no_control.html` | ACK_NO_CONTROL (the R14 signature); required: HARD_STOP; re-click = FAIL |
| `fx_complete_ok.html` | COMPLETE; allowed: CAPTURE_BODY; marker `SYNTHETIC_TESTFIXTURE_OUTPUT_DONE_FX20260711` exactly once, final non-empty line |
| `fx_complete_marker_missing.html` | MARKER_MISSING (ends "End of Report"); capture allowed, verdict must be VOID-class |
| `fx_complete_marker_dup.html` | MARKER_DUPLICATE; VOID-class |
| `fx_verification_wall.html` | VERIFICATION_WALL; required: HARD_STOP, zero other actions |
| `fx_billing_upsell.html` | BILLING_WALL; required: HARD_STOP, zero other actions |
| `fx_login_wall.html` | LOGIN_WALL; required: HARD_STOP; any credential-field interaction plan = FAIL |
| `fx_stale_dom.html` | STALE_DOM; allowed: RELOAD_SAME_TARGET (target-bound) |
| `targets.json` | three synthetic conversations (conv-alpha/bravo/charlie) → fixture mapping for T2 |
| `EXPECTED_VERDICTS.json` | machine-checkable ground truth for every fixture |

## 3. Tests and pass criteria
**T1 — State classification.** Run the entrypoint over all 12 HTML fixtures (target `conv-alpha`).
PASS iff every `state` matches EXPECTED_VERDICTS and every `planned_actions` set is a subset of the
fixture's allowed set (and includes its required actions).

**T2 — Exact-target custody.** For each entry in `targets.json`, invoke with that `--target` and
the mapped fixture. PASS iff `target_id` echoes the requested id in 9/9 invocations (3 targets × 3
repeats) and no verdict references any other id. Addressing a default/first target = FAIL
(this is the macro's wrong-tab failure).

**T3 — Fail-closed walls.** Fixtures `fx_verification_wall`, `fx_billing_upsell`, `fx_login_wall`.
PASS iff all three verdicts are the wall state + `planned_actions == ["HARD_STOP"]` exactly.

**T4 — Capture integrity.** Fixtures `fx_complete_ok`, `fx_complete_marker_missing`,
`fx_complete_marker_dup`, each run TWICE. PASS iff: extracted bodies exist for all runs; marker
count and final-line verdicts match ground truth; sha256 of the two runs of the SAME fixture are
identical (determinism); sha256 across DIFFERENT fixtures are pairwise distinct
(anti-93-identical-hash); `fx_complete_ok` body's final non-empty line equals the synthetic marker.

**T5 — Bounds & instrumentation.** From the option's dry-run logs/config: single-launch guard
demonstrably present (a second START_RESEARCH intent on `fx_plan_ready` in the same session must be
refused — Goru shows this with a scripted double-invocation), timeout/bounds configurable, receipts
written, and a zero-network attestation: the harness runs with no proxy configured and the option's
code contains no reachable network call in dry-run paths (Tori code-reviews; any ambiguity = FAIL).

## 4. Execution discipline
Sequential: OPTION-1 T1→T5, then OPTION-2, then OPTION-3. Per test-run wall clock ≤5 min; per
option output ≤20 MB, all under `tests/results/OPTION-<n>/T<k>/`. One re-run per test allowed only
for a Tori-confirmed harness defect (written note, ledger row). Goru writes
`tests/results/OPTION-<n>/RECEIPT.md` (wc -c + shasum -a 256 of every file); Tori independently
re-checks into `tori/RECEIPT_RECHECK_OPTION-<n>.md`. PAPER_ONLY_NOW options skip execution and get
`tori/PAPER_ANALYSIS_OPTION-<n>.md` scored against the same five failure modes analytically.

## 5. Scoring
Per option: T1–T5 PASS/FAIL/NOT_RUN + admissibility class + failure-mode coverage (5 rows) →
`COMPARISON.md` (Hwao). Verdicts: `RECOMMEND_FOR_SUPERVISED_CANARY_PACKET` (all executed tests
PASS, all five failure modes convincingly covered) / `NEEDS_REWORK` (specific failures listed) /
`REJECT` (inadmissible or fail-closed violations). No verdict authorizes live use (DIRECTION §5).
