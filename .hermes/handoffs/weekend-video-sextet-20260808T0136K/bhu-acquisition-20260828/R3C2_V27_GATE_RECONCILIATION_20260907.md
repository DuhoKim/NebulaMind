# R3C2 — two-seat gate on V27 (`12daf4f5…`), reconciled BY TOPIC (2026-09-07 00:46 KST)

Reports: `R3C2_GATE_V27_codex_20260907.md` (PREREG_UNSOUND; written 00:26, wrapper absent at the 00:36:46 check; LEAK=NONE), `R3C2_GATE_V27_kimi_20260907.md`
(PREREG_SOUND_WITH_REPAIRS; written 00:39, count 0 observed 00:42:33). Access lines verified. C5 YES, no masked stage, both. Prior V26 findings: closed by both except one PARTLY (codex: audit completeness) and one cosmetic (kimi: docstrings).

| topic | codex | kimi | disposition in V28 `c9a43610be7451aa…` |
|---|---|---|---|
| audit accepts incomplete reconstructions; ignores evidence; borrows missing dependencies from the sealed side | F1 | — | tool: schema validated at the re-derivation seal; every field/evidence/edge compared; roots from the auditor's own graph only; text; controls + probes |
| a declared alternative accepted per input, then rejected by root comparison | F2 | — | tool + §3 text: like-with-like under the matching branch; control |
| STANDARD with ORIG_SILENT / missing coordinates skips the value-line check; BLOCKED evidence not bound to the claiming file | F3 | — | tool + text; controls + probes |
| ordinary PRINTED cannot cite evidence on a different line from its value | F4 | — | tool + text; controls + probe |
| historical parenthesis names the wrong old token | C1 | F1 | text |
| delivered lane/batch tool docstrings still "STAGED, UNADOPTED" | C2 | F2 (V26 N1) | docstrings |

Kit: 156 controls, 54 deletion probes, PASS; both pin sheets verify; packet built from V28. C0 and the gate run on V28 next.
