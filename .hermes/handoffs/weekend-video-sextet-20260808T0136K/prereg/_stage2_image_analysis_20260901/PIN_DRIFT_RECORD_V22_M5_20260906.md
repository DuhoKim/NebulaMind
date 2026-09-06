# PIN DRIFT RECORD — V22 pins edited in place after the V22 review (codex V23 M5; Blanc's order 22:58 KST) — 2026-09-06 23:00 KST

Blanc's requirements: (1) do NOT retro-edit the V22 pins; record old vs new digests and what changed; (2) adopt an immutability rule; (3) say whether any V22 VERDICT depended on the edited bytes.

## 1. The four files: digest as pinned at V22, digest now, what changed

| file | V22 pin (what the V22 reviewers read) | now (V23 pin) | in the V22 sandbox digest list? | what changed (git diff eb72e8dda..HEAD) |
|---|---|---|---|---|
| `corpus_identity/history_v2.py` | `ce3d8c1cee3f9734…` | `374d468a8a57f9f3…` | yes | two stages added to STAGES (builder-control-refusal, builder-args-refusal) for codex V22 D; nothing else (1 file changed, 1 insertion(+), 1 deletion(-)) |
| `track1/test_track1_fail_first.py` | `f2772a6cbe3081df…` | `34cf9c3528e12211…` | yes | test_C4c uses a TEMP argparse sidecar instead of the in-tree one (codex V22 side-effect note); no assertion changed (1 file changed, 6 insertions(+), 3 deletions(-)) |
| `track1/coherent_attacks.py` | `1a00000e501b34c8…` | `06dc9a54c0648cae…` | yes | imports switched v6→v7, v2→v3, v22→v23; rows 9c–9k rebuilt on validate_continuation_v3 (open events, publish_entry), row 10d added (codex V22 attack A); header text (1 file changed, 39 insertions(+), 24 deletions(-)) |
| `track2/test_track2_fail_first.py` | `fb784f792981d13c…` | `a65599e2cf68136a…` | yes | module docstring only — the run-1 claim corrected to MISSING-INTERFACE (codex V22); no test changed (1 file changed, 3 insertions(+), 2 deletions(-)) |

Full digests: see the archived copies' README (`_optionA_dev/_archive_v22_pins/README.md`) for the V22 values and `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V23_20260906.md` for the V23 values. The V22 rule text is NOT edited: its pins still name the bytes the V22 reviewers read; those bytes are restored under `_optionA_dev/_archive_v22_pins/` (hash-verified) and are no longer at their original paths.

## 2. Did any V22 VERDICT depend on the edited bytes?

NO. The V22 reviewers read the sandbox built at 21:36 KST from commit eb72e8dda; that sandbox's digest list (`_tmp_v22_gate_COPIED_DIGESTS.txt`, committed) carries the V22-pinned digests of all four files (column 4 above), and the edits were made afterwards (22:0x–22:1x KST, for V23). Both V22 verdicts (AGY_SELRULE_V22_SEATA.md, CODEX_SELRULE_V22_SEATB.md) were therefore rendered on the V22 bytes — the pins in the V22 text describe exactly what they examined. What the drift means instead: for those four paths the V22 verdicts are about code that is now SUPERSEDED at that path (by the V23 successors), and a reader who opens the path today does not see what V22's reviewers saw — hence the restoration under distinct archived names. The V22 verdicts are hereby LABELLED: 'rendered on the V22-pinned bytes of history_v2.py / test_track1_fail_first.py / coherent_attacks.py / test_track2_fail_first.py, which are superseded at their paths since V23; archived copies at _optionA_dev/_archive_v22_pins/.'

## 3. The other two drifts today, for the pattern Blanc named
- The README against its pin sheet, and the decision brief's stale reconciliation digest (Tori's lane, codex 22:00 note) — recorded there. This lane's M5 is the third. Common cause: a file treated as 'staged/draft' was edited after a digest of it had been stated to a reviewer.

## 4. The rule adopted (also in PIN_IMMUTABILITY_RULE_20260906.md, the lane state, and memory)
Once a file's digest has been stated to a dispatched review — in a rule text, a brief, a pin sheet or a sandbox digest list — that file is IMMUTABLE at that path until the review's verdicts are filed; any change goes to a NEW filename (successor), and the review's digest list is the authority on what was read. After the verdicts are filed, the pinned bytes stay retained at their path or under an archived name; a later candidate re-pins its successors. Test files and inspection scripts are pinned files like any module.
