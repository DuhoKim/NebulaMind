# V6 BUILD LIST — from the converged V5 refusals (both gates, 8 blockers each, 1:1 overlap)

Hwao, 2026-08-25 00:30 KST. The design layer survived round 4 (V5): byte-exact fixture
reproduction on an independent run, all five selector counterexamples pass, 8 of 18 V4
findings fully closed, axis/quotations/partition/CP/void/BS-9 all held. Every remaining
blocker is a missing IMPLEMENTATION with a gate-stated acceptance test. Build these, then V6.

| # | build item | defined by gate findings | acceptance test (from the gates) |
|---|---|---|---|
| 1 | `canonical_mask()` typed constructor: validates lengths, unique (brickid,objid), flags, s∈{−1,+1}, bin labels, finite pinned c bytes; sorts internally; binds mask digest + input-kind tag; ONLY input Stage C / real record accepts | gpt56 F3, codex F5 | banned inputs (bare vector, parent positions, non-sign labels, reversed rows) all fail closed |
| 2 | Per-bin Stage C: `inject_trial` accepts scalar OR validated per-bin a via mask bin labels | gpt56 F1, codex F1 | spread-trigger boundary fixture executes both paths |
| 3 | `build_plan()` orchestrator: separate n_raw/n_ret; ledger on raw, ALL thresholds on retained; prefix scan; L_min_plan/L_plan; S_final; re-pass; emits full receipt | gpt56 F2 | gpt56's 7-brick raw/retained fixture selects [1,3] not [1,2]; 17-raw/16-retained boundary fixture |
| 4 | Calibration producer suite: tertile boundaries, 3×9 integer allocation (rounding/remainder/budget/tie rules), HC corrected-accuracy estimator, full Cov_a incl. shared-error term, a_LB producer, path adjudicator | gpt56 F4, codex F8 | Cov_a reconstructed from synthetic cell counts + shared-error inputs, not consumed ad hoc |
| 5 | Receipt schemas: domain-separated, shape-delimited canonical payloads for every slot + environment envelope (python/numpy/BLAS build/arch/threads); receipt writers record env | gpt56 F5, codex F2/F4 | cross-environment refusal test; every §7 slot has a code symbol |
| 6 | Environment FREEZE (not record): pinned python/numpy/BLAS build; production asserts; docstring/BLAS contradiction resolved (scalar quad form or pinned BLAS) | codex F4, gpt56 F5 | mismatched env refuses to run |
| 7 | Vectorized/chunked power kernel with PROVED equality to the nested reference on fixtures; production benchmark; resource/checkpoint bounds; n_perm_power decision (9,999 with rederived CP integer, or equal-cost alternative) — any change gated, never silent | gpt56 F8, codex F5 | small-case exact equality vs nested loop; measured production-scale runtime in receipt |
| 8 | `decide()`: assembles Â_L path choice, sigmas, floor, §5 regions, halts; class-E verdict + primary-lock receipt; blind-double STOP receipt slots | gpt56 F7 | fixture battery over every §5 region incl. boundary p values |
| 9 | Sigma fail-closed: non-finite/зero-q inputs raise | codex F6 | non-finite fixture raises |
| 10 | BS-2c closure rewording + validator: table.keys == manifest.keys exactly (post-materialization), grouped-sum == ungrouped total; validator in code | gpt56 F5, codex F7 | toy fixtures incl. missing-brick and extra-brick refusals |
| 11 | Blind-double protocol honesty: publish a complete normative spec generated per function (op order stated) sufficient to reimplement without reading bodies, OR rename to clean-reimplementation review; explicit P/E blind-double receipt slots incl. Stage P/C, calibration, real record, verdict | gpt56 F6, codex F3 | second implementation reproduces fixtures from spec alone |
| 12 | §7 slot table rebuilt machine-checkable: named accountable producer, inputs-available-at-time, schema/digest, code symbol, blocks, failure consequence — per slot | gpt56 F7 | gate walk finds no unnamed producer, no orphan obligation |

| 13 | Academic-gates fields (adopted 2026-08-25 from harness-workshop via Blanc): §1 carries the bibcode/DOI for Longo 2011 (2011PhLB..699..224L / doi:10.1016/j.physletb.2011.04.008 — verify at freeze) and the release data papers; frame named explicitly (ICRS) wherever coordinates appear; BS-1b/BS-2c archive every query VERBATIM as a runnable script (no NL/MCP output enters a receipt unreconstructed) | external practice, EXTERNAL_PRACTICE_ADOPTIONS_20260825.md §1 | gate finds no uncited claim source, no unarchived query, no unnamed frame |

Seat plan (platoon): items 1–3, 8–10 = Hwao (core semantics); 4 = Hwao spec + gpt2 blind
implementation; 5–6 = gpt1; 7 = Hwao kernel + gpt2 independent equality check; 11 = spec
autogen Hwao, second implementation gpt2 (fresh session, spec-only); 12–13 = Hwao. Then V6 →
both gates → freeze candidate → Duho.

Revision discipline (adopted, same source §2): every V6 change must appear in the §9
finding→change trace; any change NOT traceable to a gate finding is listed separately with
its hypothesis stated. (The v8 double-edit refutation in the custody saga was this rule
violated; V2–V5 stayed honest here via the trace tables — now it is explicit policy.)
