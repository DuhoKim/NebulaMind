# Tori Phase 1 dispatch — OPTION-3 benign browserless lane

Packet: `goru-options-pilot-20260711T102412Z`
UTC: `2026-07-11T11:35:18Z`
Official surrogate class: `SURROGATE_TESTABLE`
Live status: `SEPARATELY-GATED-LIVE`
Official verdict marker: `ADMISSIBILITY_VERDICT_20260711T104119Z` (zero bytes)

## Binding scope

Execute Option 3 only, after writing the implementation and receiving Tori's explicit pre-execution approval. This dispatch authorizes a browserless dry-run parser over the pinned synthetic fixtures and a documentation-only discovery note. It authorizes no GUI/display/Accessibility mechanism and no live service.

Read and obey `DIRECTION.md`, `TEST_DESIGN.md`, `MANIFEST.json`, `tests/fixtures/EXPECTED_VERDICTS.json`, `tests/fixtures/targets.json`, and `goru/OPTIONS_DECLARATION.md`.

## Absolute prohibitions

- No Google or Gemini access
- No browser, Chrome, Chrome for Testing, Chromium, Playwright, WebDriver, or headless process
- No System Events, AppleScript execution, Accessibility control, UI scripting, display inspection/reconfiguration, virtual-display activation, or kext
- No network or sockets, including localhost
- No cookies, tokens, credentials, browser profiles, or environment secrets
- No installs or package-manager commands
- No execution or modification of `ruthless_weekend_burn.py` or derivatives
- No fixture, expected-verdict, target, generator, manifest, or prior-result edits
- No delegated/background/self agent
- No files outside this packet root

## Phase 1A — implement, but do not run

Create only:

1. `goru/option3_shim.py`
2. `goru/test_runner_option3.py`
3. `goru/OPTION-3_DISCOVERY.md`

The shim must implement exactly:

`python3 goru/option3_shim.py --dry-run --fixture <path.html> --target <conversation-id> --out <dir>`

Requirements:

- `--dry-run` is mandatory and is the only mode.
- Read only a canonical path strictly inside `tests/fixtures/`, limited to the 12 pinned HTML fixture basenames.
- Parse locally with BeautifulSoup; no network-capable imports or calls.
- Emit the exact `verdict.json` schema in `TEST_DESIGN.md`.
- `UNKNOWN` and all wall states fail closed with `planned_actions == ["HARD_STOP"]` where required.
- Echo the exact requested synthetic target ID; never choose a default target.
- Persist a target-bound single-start session record only under the current test's output tree; create its parent directory before access.
- Extract report text deterministically without modifying semantic content.

The runner must implement T1–T5 exactly as specified, with:

- all subprocesses bounded at 300 seconds or less;
- per-test elapsed duration;
- total output bound of 20 MB that actively fails T5 if exceeded;
- a machine-readable summary for T5;
- no proxy/network assumptions required because the code must contain no reachable network path;
- `tests/results/OPTION-3/RECEIPT.md` listing SHA-256 and byte size for every result and the three Goru-authored files;
- ledger rows only after the run completes.

Important pinned-ground-truth rule: `fx_complete_marker_dup.html` visibly ends with the synthetic marker, while pinned `EXPECTED_VERDICTS.json` says `marker_is_final_nonblank_line=false`. Do not edit, normalize, reinterpret, or work around either pinned file. If the extracted body truth conflicts with that expected flag, record T4 `FAIL`, identify the exact mismatch, continue to T5, and do not request a rerun; this is not a harness defect.

`goru/OPTION-3_DISCOVERY.md` is documentation only. It may describe hypothetical virtual-display/AppleScript mechanics, prerequisites, failure modes, security risks, explicit Duho approval gates, and a future packet outline. It must repeatedly label those mechanics `NOT_INVOKED` and must not inspect or change live display, Accessibility, System Events, or GUI state. Include an explicit statement that a benign surrogate PASS would not authorize live use.

After creating the three files, stop. Do not execute any Python or shell command. Tell Tori the paths and ask for pre-execution review.

## Phase 1B — only after Tori approval

Tori may authorize exactly one invocation of `goru/test_runner_option3.py`. Execute only that exact command after approval. If it aborts, do not edit or rerun until Tori adjudicates whether it is the single allowed harness-defect rerun.

At completion, report:

- T1–T5 PASS/FAIL
- exact T4 mismatch if present
- receipt path, SHA-256, receipt bytes, and total output bytes
- discovery-note path and SHA-256
- exact text: `GORU_OPTION3_PHASE1_DONE__NO_LIVE_AUTHORIZATION`

Do not create a packet completion marker; Hwao owns final comparison and packet closure.

## Non-equivalence

A local result tests only transport-free decision logic against synthetic fixtures. It is not a Gemini result, not evidence of GUI/display/Accessibility reliability, and not permission for any live use. Only a fully passing benign lane plus complete discovery documentation could make Option 3 eligible for a separately Duho-gated future packet.
