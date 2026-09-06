# R3C2 — two-seat gate on V30 (`57de1252…`), reconciled BY TOPIC (2026-09-07 03:22 KST)

Reports: `R3C2_GATE_V30_codex_20260907.md` (PREREG_UNSOUND; written 02:56, wrapper absent at the 03:03:19 check), `R3C2_GATE_V30_kimi_20260907.md`
(PREREG_SOUND_WITH_REPAIRS; written 03:14, count 0 observed 03:17:38). Access lines verified. Blind intact. C5 YES, no masked stage, both.

| topic | codex | kimi | disposition in V31 `7c661ac0c6157bff…` |
|---|---|---|---|
| full-record branch predicate not authoritative: the REVERSE hybrid (alt origin + alt evidence, primary parents) got a false PASS | F2 | — | tool: unconditional record-level MISMATCH before any diagnostic; §3 text; controls (both hybrid directions); the earlier probes now assert the diagnostic disappears while the verdict holds — the guard the lane had removed at 02:31 for probes is restored (Blanc 03:03) |
| identity conflict fails globally but is not carried into dependent MISMATCH rows | F1 | — | tool: per-input identity conflict included in the record's diffs and propagated; §3 text; control; its probe asserts the per-record path holds when the global line is deleted |
| manifest header 'consumed by no tool' (deferred from V29) | C1 | C1 | manifest header reworded; manifest re-pinned; partition regenerated |

Kit: 176 controls, 61 deletion probes, PASS; both pin sheets verify; packet built from V31. C0 and the gate run on V31 next.

**Sweep (2026-09-07 03:22 KST):** every finding label in both reports checked programmatically against the rows — missing: none.
