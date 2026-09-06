# R3C2 — two-seat gate on V29 (`37ba5891…`), reconciled BY TOPIC (2026-09-07 02:33 KST)

Reports: `R3C2_GATE_V29_codex_20260907.md` (PREREG_UNSOUND; written 02:05, wrapper absent at the 02:18:01 check), `R3C2_GATE_V29_kimi_20260907.md`
(PREREG_SOUND_WITH_REPAIRS; written 02:25, count 0 observed 02:28:09). Access lines verified. Blind intact. C5 YES, no masked stage, both.

| topic | codex | kimi | disposition in V30 `57de1252d5f9d459…` |
|---|---|---|---|
| duplicate input ids shadow a fabricated copy; explicit claim ids unbound | F1 | — | tool: uniqueness + key agreement at the seal, sealed-identity binding at compare; text; controls + probes |
| a hybrid of both declared branches accepted | F2 | — | tool: complete-branch matching only; text; control + probe |
| manifest line column vs its stated convention (character-level ambiguity) | — | N1 | convention stated at the character level, column recomputed, manifest re-pinned, partition regenerated |
| duplicated comment line in the seat tool | — | N2 | removed |
| the manifest column header says the column is "consumed by no tool", but the partition tool sums it and writes `nonblank_lines` (no integrity predicate depends on it) | C1 (cosmetic) | — | ACCEPTED (added 2026-09-07 02:39 KST on Blanc's 02:39 order — the row was missing; the finding was not seen, not declined). Not applied in V30: the header lives in the pinned manifest whose digest is in the master's §2, and the master was a C0 input when the omission was found. Applied in the next version (with the V30 gate's repairs): header → "informational, summed and reported by the partition tool, not used as an integrity predicate", manifest re-pinned, partition regenerated. |

Kit: 174 controls, 61 deletion probes, PASS; both pin sheets verify; packet built from V30. C0 and the gate run on V30 next.

**Sweep (2026-09-07 02:39 KST, Blanc 02:39):** every finding label in both V29 reports checked programmatically against this table — codex F1, F2, C1; kimi N1, N2 — one row was missing (codex C1, above); none other. Cause: the lane's label grep matched the form `COSMETIC C1` but not codex's `**C1 — COSMETIC`; the programmatic sweep is now part of every reconciliation.
