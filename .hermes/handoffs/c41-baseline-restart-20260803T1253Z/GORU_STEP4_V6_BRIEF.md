# GORU BRIEF — Step 4 V6 (fresh seat): rebuild V4's 80, then quality-patch — count is NOT writable

You are Goru on a fresh session. Prior rounds live in `GORU_STEP4_REPORT.md` (V1–V5) — read it,
then read `LANA_STEP4_PASS.md` + `LANA_STEP4_REPASS.md`. V5's 59 boilerplate "debris" exclusions
are REJECTED with evidence: rank-1 paper 2026A&A...708A.203P contains a finding-zone span deriving
an M_UV–metallicity relation at z≈10 — a textbook entry — stamped "debris" anyway. That does not
happen in V6.

## By-construction design (the count is not yours to change)

1. Regenerate the V4 80-entry ledger deterministically (your V4 procedure; integrity rules: v1.1
   enums, unknown preserved, rule-7 stances, honest certainty). This is the BASE —
   `C41_LEDGER.jsonl`, 80 rows, validator PASS, rows==receipt.
2. Quality pass as a PATCH FILE (`STEP4_QUALITY_PATCH.jsonl`): one row per entry —
   `entry_id → new_assertion (atomic, source-modality, composed from its spans) + links[]`.
   Apply with a small script that REFUSES to add or remove entries (assert count==80 before/after).
3. If an entry's spans genuinely cannot support an atomic assertion, the patch row says
   `no_claim_recoverable: true` with **the best span QUOTED verbatim in the row** as evidence —
   per-entry, never boilerplate. Those entries get assertion "NO_CLAIM_RECOVERABLE from bound
   spans" + certainty `no_info` — they STAY in the ledger as honest placeholders (Step 5/6 see
   them; nothing silently vanishes). Expect a handful, not 59.
4. Links: mine evident relations across the 80 (target: the debate structure visible; AGN pilot
   ~1/entry).
5. Deliver: base + patch + applier script + final patched ledger + receipt (rows==80==receipt) +
   `## Repair round (V6)` section + marker `GORU_STEP4_V6_COMPLETE_20260804`.
