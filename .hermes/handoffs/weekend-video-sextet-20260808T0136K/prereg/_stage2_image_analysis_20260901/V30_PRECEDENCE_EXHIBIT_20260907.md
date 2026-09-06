# V30 — PRECEDENCE EXHIBIT (Blanc 03:20: one order, one resolver, exhibited pairwise) — 2026-09-07 03:33 KST

Executed: `_optionA_dev/track10/exhibit_precedence_pairs.py` (SHA-256 d44bc2860e167842b6e561221dfc678d22d552b39d4f5f36ef575368ec8f65f8) on provenance_designs_v10. Deterministic.

PRECEDENCE ORDER (top wins): LOCAL-TERMINAL > FORGED > NOT-EARLIEST > EXPIRED > DERIVED-TERMINAL > RETRY-UNAVAILABLE > RETRY-INCOMPLETE > ACCEPT

| class A (contributed first / second) | class B | winner, A first | winner, B first | same? | winner is the higher class? |
|---|---|---|---|---|---|
| LOCAL-TERMINAL | FORGED | LOCAL-TERMINAL | LOCAL-TERMINAL | yes | yes |
| LOCAL-TERMINAL | NOT-EARLIEST | LOCAL-TERMINAL | LOCAL-TERMINAL | yes | yes |
| LOCAL-TERMINAL | EXPIRED | LOCAL-TERMINAL | LOCAL-TERMINAL | yes | yes |
| LOCAL-TERMINAL | DERIVED-TERMINAL | LOCAL-TERMINAL | LOCAL-TERMINAL | yes | yes |
| LOCAL-TERMINAL | RETRY-UNAVAILABLE | LOCAL-TERMINAL | LOCAL-TERMINAL | yes | yes |
| LOCAL-TERMINAL | RETRY-INCOMPLETE | LOCAL-TERMINAL | LOCAL-TERMINAL | yes | yes |
| FORGED | NOT-EARLIEST | FORGED | FORGED | yes | yes |
| FORGED | EXPIRED | FORGED | FORGED | yes | yes |
| FORGED | DERIVED-TERMINAL | FORGED | FORGED | yes | yes |
| FORGED | RETRY-UNAVAILABLE | FORGED | FORGED | yes | yes |
| FORGED | RETRY-INCOMPLETE | FORGED | FORGED | yes | yes |
| NOT-EARLIEST | EXPIRED | NOT-EARLIEST | NOT-EARLIEST | yes | yes |
| NOT-EARLIEST | DERIVED-TERMINAL | NOT-EARLIEST | NOT-EARLIEST | yes | yes |
| NOT-EARLIEST | RETRY-UNAVAILABLE | NOT-EARLIEST | NOT-EARLIEST | yes | yes |
| NOT-EARLIEST | RETRY-INCOMPLETE | NOT-EARLIEST | NOT-EARLIEST | yes | yes |
| EXPIRED | DERIVED-TERMINAL | EXPIRED | EXPIRED | yes | yes |
| EXPIRED | RETRY-UNAVAILABLE | EXPIRED | EXPIRED | yes | yes |
| EXPIRED | RETRY-INCOMPLETE | EXPIRED | EXPIRED | yes | yes |
| DERIVED-TERMINAL | RETRY-UNAVAILABLE | DERIVED-TERMINAL | DERIVED-TERMINAL | yes | yes |
| DERIVED-TERMINAL | RETRY-INCOMPLETE | DERIVED-TERMINAL | DERIVED-TERMINAL | yes | yes |
| RETRY-UNAVAILABLE | RETRY-INCOMPLETE | RETRY-UNAVAILABLE | RETRY-UNAVAILABLE | yes | yes |

pairs exhibited: 21; every pair same winner in both orders and the higher class: True

Within one class the FIXED stage sequence decides (contribution index), never list or retrieval order:
  [X, Y] → X-first-in-sequence;  [Y, X] → X-first-in-sequence

COMPLETE-PATH PAIRS executed by the tests (run_configurations_v14.composed_resolver; labelled fixtures):
  LOCAL-TERMINAL (approval wrong repository) vs RETRY-UNAVAILABLE (seed re-derivation RETRY) → EVENT-INCONSISTENT  [track 10, codex V29-1]
  FORGED (approval same-id contradiction) vs RETRY-UNAVAILABLE (seed re-derivation RETRY) → EVENT-FORGED  [track 10, codex V29-1]
  RETRY-UNAVAILABLE alone (seed re-derivation RETRY, genuine approval) → REDERIVE-RETRY  [track 10, control]
  LOCAL-TERMINAL (open event wrong repository) vs RETRY-UNAVAILABLE (ls-remote down) → HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT  [track 10, codex V29-2]
  FORGED (open event same-id contradiction) vs RETRY-UNAVAILABLE (ls-remote down) → HISTORY-CONTINUATION: OPEN-EVENT-FORGED  [track 10, codex V29-2]
  RETRY-UNAVAILABLE alone (ls-remote down, genuine open event) → HISTORY-CONTINUATION: RETRY-REMOTE-UNAVAILABLE  [track 10, control]
  LOCAL-TERMINAL (open event wrong repository) vs RETRY-UNAVAILABLE (approval feed HTTP 503) → HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT  [track 10, codex V29-2]
  FORGED (approval same-id) vs RETRY-UNAVAILABLE (undetermined delivery) → EVENT-FORGED  [track 9, codex V28-1]
  LOCAL-TERMINAL (approval wrong repository) vs RETRY-UNAVAILABLE (undetermined delivery; feed healthy / 503) → EVENT-INCONSISTENT  [track 9, codex V28-1]
  FORGED (open same-id) vs RETRY-UNAVAILABLE (undetermined open delivery) → HISTORY-CONTINUATION: OPEN-EVENT-FORGED  [track 9, codex V28-2]
  LOCAL-TERMINAL (open wrong repository) vs RETRY-UNAVAILABLE (undetermined open delivery) → HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT  [track 9, codex V28-2]
  RETRY-UNAVAILABLE alone (undetermined, nothing contradicts) → RETRY-EVENTS-UNAVAILABLE / RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE  [tracks 8/9, controls]
  FORGED vs RETRY-UNAVAILABLE, standalone helper (same-id contradiction, undeterminable head) → FORGED  [track 8, codex V27-1]
  LOCAL-TERMINAL vs RETRY-UNAVAILABLE, standalone helper (wrong repository, HTTP 503) → INCONSISTENT-INPUT  [track 8, codex V27-1]
