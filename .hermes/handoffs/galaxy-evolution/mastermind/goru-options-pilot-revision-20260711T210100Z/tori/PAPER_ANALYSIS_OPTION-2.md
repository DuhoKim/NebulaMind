# OPTION-2 paper-only analysis

Packet: `goru-options-pilot-20260711T102412Z`
Class: `PAPER_ONLY_NOW`
Live status: `INADMISSIBLE-LIVE => REJECT-for-live`

## Why it was not executed

The declared surrogate uses Python Playwright. The module is installed, but its configured executable is an existing `Google Chrome for Testing` binary. DIRECTION §0 prohibits Chrome launch under this packet. Goru also certified that the surrogate uses no headless browser. No browser process, profile, localhost server, or Option-2 shim was therefore created or run.

## T1–T5

| Test | Verdict | Reason |
|---|---|---|
| T1 — state classification | NOT_RUN | Requires the prohibited browser launch in the declared design. |
| T2 — exact-target custody | NOT_RUN | DOM target-binding claims exist only in `goru/OPTIONS_DECLARATION.md`; no executable evidence. |
| T3 — fail-closed walls | NOT_RUN | Wall-selector behavior is declared but untested. |
| T4 — capture integrity | NOT_RUN | No capture runs; no determinism or pairwise-hash evidence. |
| T5 — bounds/instrumentation | NOT_RUN | No shim, single-launch guard, timeout, receipt, or network attestation was executed. |

## Five old-macro failure modes

1. **Deep Research not selected.** The old macro opens `https://gemini.google.com/app` and immediately pastes/submits (`ruthless_weekend_burn.py:168-173`) without checking Pro or Deep Research. The Option-2 declaration proposes explicit DOM assertions, which could address this in principle, but provides no implementation evidence.
2. **Start Research not activated.** The old macro only presses Enter (`ruthless_weekend_burn.py:171-173`) and never verifies a plan or active server state. The proposed transition check is conceptually relevant but untested.
3. **Wrong-target capture.** The old macro creates tabs through `window 1` and invokes a generic capture script without persisting an exact tab identity (`ruthless_weekend_burn.py:168-177`). The proposed target-container binding is the right design direction but untested.
4. **No gates.** The old loop has no quota, marker, verification, billing, or login checks (`ruthless_weekend_burn.py:147-183`). Proposed wall selectors could fail closed, but no T3 evidence exists.
5. **Identical captures.** The old macro does not compare output hashes or require target-specific markers before accepting a capture (`ruthless_weekend_burn.py:175-178`). The proposed unique-marker/hash check is conceptually relevant but untested.

## Policy and technical result

A local browser surrogate would not test copied-profile behavior, stealth/evasion, Google authentication, anti-bot survival, or Gemini Deep Research. Those defining live mechanisms are prohibited and remain unsafe regardless of any fixture result.

Final verdict: `REJECT_LIVE__SURROGATE_NOT_RUN`

This analysis authorizes no browser or live service use.
