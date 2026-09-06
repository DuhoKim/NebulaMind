# R3C2 — two-seat gate on V33 (`70a02733…`), reconciled BY TOPIC (2026-09-07 05:38 KST)

Reports: `R3C2_GATE_V33_codex_20260907.md` (PREREG_UNSOUND, two findings; PRIOR_FINDINGS_CLOSED=YES; written 05:13, wrapper absent at 05:26:04), `R3C2_GATE_V33_kimi_20260907.md`
(**PREREG_SOUND**, no findings; PRIOR_FINDINGS_CLOSED=YES; written 05:33, pid gone at 05:37:03). Access lines verified. Blind intact. C5 YES, no masked stage, both.
The V32 seat-order finding is CLOSED by both seats; both V33 findings sit inside the SPI pattern (serialisation at the enforcement point; a fixture of the exhibition) — no new predicate was added anywhere.

| topic | codex | kimi | disposition in V34 `6e18bc39bbe35fa0…` |
|---|---|---|---|
| merge wrote unsorted keys: structurally equal seat records in different member order → different merged bytes and sealed_ledger_sha256, same verdict | F1 | — | REPAIRED at the single enforcement point: merge serialises with sorted keys (recursive); §3 sentence replaced by codex's exact text; member-order construction added; fail-first against pinned V33 byte copies (FAIL on that row only) |
| exhibition's 'hybrid direction 1' was a complete parent-only alternative, not a hybrid; true hybrid absent | F2 | — | REPAIRED (lane fixture defect, disclosed): row relabelled and kept; true hybrid + reciprocal added, both must FAIL with the 'neither complete declared branch' diagnostic in both orders; every construction asserts expected PASS/FAIL; fixture writer no longer normalises; sealed_ledger_sha256 retained in the artefact compare; failure lines in emitted order |

Kit: 185 controls, 63 deletion probes, PASS (no pre-existing assertion conflicted); both pin sheets verify; packet built from V34. Brief slip (Q7 'gate on V33') disclosed in the run log. C0 and the gate run on V34 next.

**Sweep (2026-09-07 05:38 KST):** every finding label in both reports checked programmatically against the rows — missing: none (kimi reported no findings).
