# HWAO_GORU_FIXTURE_ADJUDICATION — supersession approved with verification guardrails

Ref: `HWAO_GORU_FIXTURE_ESCALATION.md`, `fixtures/GORU_FIXTURE_REVIEW_BLOCKED.md` · Direction-only; Hwao edits no implementation files; no live/network/browser/git/DB/deploy/dashboard action authorized here.

## Adjudication

Tori's rejection is **upheld**. All four defects contradict values already established twice independently (HWAO_ROOT_CAUSE.md §1 chip census; TORI_ROOT_CAUSE_CORRECTED.md) from the same sealed HTML: the S2 Citation-cell chip arrays are `[27,28,10,11,15,20,30,30]`, not empty; S5 is **four** GAP lines with attribution GAP1→chip 30, GAP2→token, GAP3→chip 36, GAP4→token (no "GAP5" exists); the ledger is 46 **paired** chip+anchor events yielding 37 unique indices with 0 inconsistencies; and the corrupted-mapping fixture must actually demonstrate a same-index→two-URLs inconsistency or T2 cannot be authored RED. Goru's helper parser reproduced the exact chip blind spot this packet exists to repair. No sealed input changed, so this is a lane-output defect, not a data dispute.

**Supersession is APPROVED**: Tori may replace the invalid Goru-derived facts with a packet-local deterministic fixture generator/test adapter parsing the real sealed HTML byte-copy, using the locally present parse5 (read-only use from `frontend/node_modules`; no install, no network). Goru is **advisory/blocked for this fixture family** until Hwao re-tasks it; Goru's other standing work is unaffected.

## Binding guardrails on the supersession

1. **Generator:** packet-local (e.g. `fixtures/gen_expected_dom_facts.mjs`), deterministic (no clock/random), input = the hash-checked sealed-HTML byte-copy (`78ed129c…2bbc`). Record parse5 path, version, and sha256 in the receipt.
2. **Acceptance gate — regenerated facts must equal the independently published values**, explicitly including the four corrected points above plus the standing census (108 chips; S1 40 / S2 8 / S3 3 / S4 9 / S5 2 / ledger 46; 46 anchors all in-ledger; 0 `<td>` anchors; heading order; li+p twins; 12 orphan indices {2,5,8,9,13,16,18,23,24,29,31,33}). **Any mismatch vs the published values ⇒ STOP and escalate** — do not silently trust either the generator or the prior reports.
3. **Independent verification preserved despite the lane change:** Kun re-runs the generator (twice, byte-identical) and diffs its output against the published values, countersigning in the fixture manifest; Lana's sign-off scope now explicitly includes fixture-facts review. Tori may not self-certify facts it generated.
4. **Custody:** the invalid Goru pass-2 files and its done marker are preserved untouched (do not delete or rewrite); the manifest records them as SUPERSEDED with a pointer to this adjudication. New receipt: `fixtures/TORI_FIXTURE_SUPERSEDE_RECEIPT.md` with generator hash, parse5 pin, and a fact-diff table (Goru-invalid vs regenerated vs published), plus Kun's countersign.
5. **Corrupted fixture requirement:** derived from the real HTML with a minimal injected conflict (one index mapped to two different URLs); a generator self-test must assert the inconsistency is present and detectable.
6. Then **proceed with T0–T15 exactly per `HWAO_IMPLEMENTATION_DIRECTION.md`** — all file boundaries, GREEN criteria, and stop conditions unchanged; the RED receipt must note this supersession.

HWAO_GORU_FIXTURE_SUPERSEDE_APPROVED_20260713T010203Z
