# R3C2 — two-seat gate on V31 (`7c661ac0…`), reconciled BY TOPIC (2026-09-07 04:07 KST)

Reports: `R3C2_GATE_V31_codex_20260907.md` (PREREG_UNSOUND; PRIOR_FINDINGS_CLOSED=YES; written 03:49, wrapper absent at the 03:53:01 check), `R3C2_GATE_V31_kimi_20260907.md`
(**PREREG_SOUND**, no findings; PRIOR_FINDINGS_CLOSED=YES; written 03:59, count 0 observed 04:02:33). Access lines verified. Blind intact. C5 YES, no masked stage, both.

| topic | codex | kimi | disposition in V32 `849483185cfbac11…` |
|---|---|---|---|
| merge dropped the alternative branch's origin_search; a supported ORIG_SILENT alternative failed and the verdict depended on seat order | F1 | — | lane tool preserves origin_search_alt; compare checks the matched branch's search; controls in both seat orders + probe |
| JSON key order in origin_search changed an audit result (string display compared) | F2 | — | structural comparison; control with reordered keys |
| kit README overstates the deletion-probe contract | C1 | — | README states the contract as it is (kill, or guard-retained diagnostic absence) |

Kit: 182 controls, 63 deletion probes, PASS; both pin sheets verify; packet built from V32. C0 and the gate run on V32 next.

**Sweep (2026-09-07 04:07 KST):** every finding label in both reports checked programmatically against the rows — missing: none (kimi reported no findings).
