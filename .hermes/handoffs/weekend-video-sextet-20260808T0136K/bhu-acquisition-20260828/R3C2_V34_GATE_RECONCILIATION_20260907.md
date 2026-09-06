# R3C2 — two-seat gate on V34 (`6e18bc39…`), reconciled BY TOPIC (2026-09-07 06:30 KST)

Reports: `R3C2_GATE_V34_codex_20260907.md` (PREREG_UNSOUND, F1 + C1; PRIOR_FINDINGS_CLOSED=YES; written 06:00, wrapper absent at 06:10:12), `R3C2_GATE_V34_kimi_20260907.md`
(**PREREG_SOUND**, no findings; PRIOR_FINDINGS_CLOSED=YES; written 06:21, pid gone at 06:24:57). Access lines verified. Blind intact. C5 YES, no masked stage, both.
Both V33 findings CLOSED by both seats. Seat-permutation equality held on every construction codex built; F1 is a new class (graph composition), repaired at merge without any downstream seat-order selection.

| topic | codex | kimi | disposition in V35 `b2e2073c49936328…` |
|---|---|---|---|
| per-input canonical mixing composes a primary graph no seat supplied (two acyclic seat graphs → cyclic mixed view): compute exits 1 instead of the DISPUTED pair; audit's diagnostic root computation on the mixed view adds a false mismatch when the auditor equals complete A or B (permutation equality held) | F1 | — | REPAIRED with codex's exact §3 sentences: merge preserves both complete seat graphs (provenance_graphs, seat-blind order, equal once); compute classifies from those graphs, refuses a mixed ledger without graphs; audit's unmatched-view roots are diagnostic only, matched-graph cycles still fail; exhibition builds the mixed-cycle fixture deterministically, requires audit PASS + compute 0 + DISPUTED in both orders, compute output joins every compared outcome; fail-first vs pinned V34 byte copies (audit [1,1], compute [1,1] on the two cycle rows only) |
| exhibition docstring described the old comparison | C1 | — | REPAIRED with codex's exact docstring |

Kit: 186 controls, 63 deletion probes, PASS. Two pre-existing controls conflicted and are disclosed in §10.30: a hand-composed mixed ledger fixture (now merge-built, assertions unchanged) and the V33 fail-first control's "only" clause (now names the exact failure set at V33). C0 and the gate run on V35 next.

**Sweep (2026-09-07 06:30 KST):** every finding label in both reports checked programmatically against the rows — missing: none (kimi reported no findings).
