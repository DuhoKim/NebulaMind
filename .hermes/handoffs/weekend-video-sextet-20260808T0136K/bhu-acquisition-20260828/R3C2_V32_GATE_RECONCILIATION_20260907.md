# R3C2 — two-seat gate on V32 (`84948318…`), reconciled BY TOPIC (2026-09-07 04:45 KST)

Reports: `R3C2_GATE_V32_codex_20260907.md` (PREREG_UNSOUND, one finding; PRIOR_FINDINGS_CLOSED=YES; written 04:29, wrapper absent at the 04:35:27 check), `R3C2_GATE_V32_kimi_20260907.md`
(**PREREG_SOUND**, no findings; PRIOR_FINDINGS_CLOSED=YES; written 04:40, count 0 observed 04:42:50). Access lines verified. Blind intact. C5 YES, no masked stage, both.

| topic | codex | kimi | disposition in V33 `70a02733917c4626…` |
|---|---|---|---|
| seat-order dependence, SECOND instance: equal origin labels, different complete searches — merge kept seat A's search; identical auditor record fails A/B, passes B/A | F1 | — | repaired as ONE PATTERN (Blanc 04:37): SEAT-PERMUTATION INVARIANCE stated once and named in §3; single enforcement point = merge (seat-blind canonical primary + complete-branch preservation whenever anything provenance-bearing differs); exhibition of the property over every reviewer construction under both seat orders, whole-outcome equality asserted; fail-first against pinned V32 byte copies (FAIL) and delivered tools (PASS) |

**Blanc's question (04:37):** V31's both-seat-order controls DID pass while V32 F1 was live — they asserted PASS for one fixture whose seats carried different origin labels, so the alternative was always created; they asserted the verdict, not whole-outcome equality, and had no equal-label/different-search case, which is exactly the case merge's `origin != origin` predicate excluded.

Kit: 184 controls, 63 deletion probes, PASS (no pre-existing assertion conflicted); both pin sheets verify; packet built from V33. C0 and the gate run on V33 next.

**Sweep (2026-09-07 04:45 KST):** every finding label in both reports checked programmatically against the rows — missing: none (kimi reported no findings).
