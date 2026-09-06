# R3C2 — two-seat gate on V28 (`c9a43610…`), reconciled BY TOPIC (2026-09-07 01:45 KST)

Reports: `R3C2_GATE_V28_codex_20260907.md` (PREREG_UNSOUND; written 01:12, wrapper absent at the 01:22:27 check), `R3C2_GATE_V28_kimi_20260907.md`
(PREREG_SOUND_WITH_REPAIRS; written 01:37, count 0 observed 01:40:41). Access lines verified. Blind intact. C5 YES, no masked stage, both.

| topic | codex | kimi | disposition in V29 `37ba58918ec6f6b0…` |
|---|---|---|---|
| off-sample closure records not compared | F1 | — | tool: every record in each selected claim's closure compared; text; controls + probe |
| declared alternatives only for a local origin change (parent-only, inherited fail) | F2 | — | tool: branch matching over the whole closure, one matched graph; text; controls |
| STANDARD value line outside the claiming file bypasses the import rule | F3 | — | tool + §2 text; control + probe |
| docstring / usage remnants | C2 | N4 | seat tool labels, manifest docstring, usage synopsis |
| builder "bytes" are character counts | — | N1 | builder prints bytes |
| manifest line column (9 rows differ under splitlines) | — | N2 | convention stated (newline-delimited), manifest re-pinned, partition regenerated |
| kit README stale | — | N3 | updated |
| merge silent on value/status/coordinate disagreement | — | N5 | merge fails in the open; text; control + probe |

Kit: 165 controls, 57 deletion probes, PASS; both pin sheets verify; packet built from V29. C0 and the gate run on V29 next.
