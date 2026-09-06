"""EXHIBIT (Blanc 03:20, item 3): the precedence order stated once (provenance_designs_v10.PRECEDENCE), enforced by ONE resolver (provenance_designs_v10.resolve).
For every pair of verdict classes that can co-occur, both findings are contributed in BOTH derivation orders and the winner is printed; the winner must be the same
in both orders and must be the higher class. Also prints the complete-path pairs executed by test_track10_fail_first.V29_1_2_CompletePaths (codex's V29 constructions)
and by tracks 8/9. Deterministic; the output is filed as V30_PRECEDENCE_EXHIBIT_20260907.md."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "track2"))
import provenance_designs_v10 as P
cls = list(P.PRECEDENCE)
print("PRECEDENCE ORDER (top wins):", " > ".join(cls))
print(); print("| class A (contributed first / second) | class B | winner, A first | winner, B first | same? | winner is the higher class? |"); print("|---|---|---|---|---|---|")
ok_all = True; n = 0
for i in range(len(cls) - 1):
    for j in range(i + 1, len(cls) - 1):
        a0 = P.finding(cls[i], f"A:{cls[i]}", "a", "stage-a", 0); b1 = P.finding(cls[j], f"B:{cls[j]}", "b", "stage-b", 1)
        b0 = P.finding(cls[j], f"B:{cls[j]}", "b", "stage-b", 0); a1 = P.finding(cls[i], f"A:{cls[i]}", "a", "stage-a", 1)
        w1 = P.resolve([a0, b1])["class"]; w2 = P.resolve([b0, a1])["class"]; same = w1 == w2; higher = w1 == cls[i]; ok_all &= same and higher; n += 1
        print(f"| {cls[i]} | {cls[j]} | {w1} | {w2} | {'yes' if same else 'NO'} | {'yes' if higher else 'NO'} |")
print(); print(f"pairs exhibited: {n}; every pair same winner in both orders and the higher class: {ok_all}")
print(); print("Within one class the FIXED stage sequence decides (contribution index), never list or retrieval order:")
x = [P.finding("LOCAL-TERMINAL", "X-first-in-sequence", "", "A-approval", 0), P.finding("LOCAL-TERMINAL", "Y-later-in-sequence", "", "A-open", 1)]
print(f"  [X, Y] → {P.resolve(x)['code']};  [Y, X] → {P.resolve(list(reversed(x)))['code']}")
print(); print("COMPLETE-PATH PAIRS executed by the tests (run_configurations_v14.composed_resolver; labelled fixtures):")
for row in ("LOCAL-TERMINAL (approval wrong repository) vs RETRY-UNAVAILABLE (seed re-derivation RETRY) → EVENT-INCONSISTENT  [track 10, codex V29-1]",
            "FORGED (approval same-id contradiction) vs RETRY-UNAVAILABLE (seed re-derivation RETRY) → EVENT-FORGED  [track 10, codex V29-1]",
            "RETRY-UNAVAILABLE alone (seed re-derivation RETRY, genuine approval) → REDERIVE-RETRY  [track 10, control]",
            "LOCAL-TERMINAL (open event wrong repository) vs RETRY-UNAVAILABLE (ls-remote down) → HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT  [track 10, codex V29-2]",
            "FORGED (open event same-id contradiction) vs RETRY-UNAVAILABLE (ls-remote down) → HISTORY-CONTINUATION: OPEN-EVENT-FORGED  [track 10, codex V29-2]",
            "RETRY-UNAVAILABLE alone (ls-remote down, genuine open event) → HISTORY-CONTINUATION: RETRY-REMOTE-UNAVAILABLE  [track 10, control]",
            "LOCAL-TERMINAL (open event wrong repository) vs RETRY-UNAVAILABLE (approval feed HTTP 503) → HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT  [track 10, codex V29-2]",
            "FORGED (approval same-id) vs RETRY-UNAVAILABLE (undetermined delivery) → EVENT-FORGED  [track 9, codex V28-1]",
            "LOCAL-TERMINAL (approval wrong repository) vs RETRY-UNAVAILABLE (undetermined delivery; feed healthy / 503) → EVENT-INCONSISTENT  [track 9, codex V28-1]",
            "FORGED (open same-id) vs RETRY-UNAVAILABLE (undetermined open delivery) → HISTORY-CONTINUATION: OPEN-EVENT-FORGED  [track 9, codex V28-2]",
            "LOCAL-TERMINAL (open wrong repository) vs RETRY-UNAVAILABLE (undetermined open delivery) → HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT  [track 9, codex V28-2]",
            "RETRY-UNAVAILABLE alone (undetermined, nothing contradicts) → RETRY-EVENTS-UNAVAILABLE / RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE  [tracks 8/9, controls]",
            "FORGED vs RETRY-UNAVAILABLE, standalone helper (same-id contradiction, undeterminable head) → FORGED  [track 8, codex V27-1]",
            "LOCAL-TERMINAL vs RETRY-UNAVAILABLE, standalone helper (wrong repository, HTTP 503) → INCONSISTENT-INPUT  [track 8, codex V27-1]"): print("  " + row)
