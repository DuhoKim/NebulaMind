# CLI_BRIEF — Fresh Goru / Gemini CLI (Antigravity) lane: cycle-9 blocker, debate-map, repair-priority analysis
Lane ID: `GORU_PILOT_CLI_20260711T050514Z` · Issued by Hwao under `pilot-gemini-resume-20260711T050514Z` · Effort: **MAX** (deep reasoning; quota headroom is the point — Antigravity at 1% of 5h window, 7% weekly)

## 0. ACK first
Per the quintet role-table protocol, write `cli/GORU_CLI_ACK.md` with the exact Goru ACK phrase from the role-table packet (`QUINTET_ROLE_TABLE_TEAMWORK_CORRECTION_20260707.md`) before substantive work. No solo-lane deviation: scope changes go back to Hwao/Duho, not improvised.

## 1. Mode and write area (binding)
- **STRICT READ-ONLY** on every input. You write ONLY under:
  `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/pilot-gemini-resume-20260711T050514Z/cli/`
- Temp/intermediate files: `cli/_tmp_*` inside that dir. Never TMPDIR, /tmp, or scratchpad.
- **Prohibited:** any write to candidates, journal/runner dirs, SPRINT_STATUS, the live REQ file, or any path outside `cli/`; any signal/restart of runner PID 45665; tmux send-keys to any pane; network beyond the Gemini API itself; reading `.env`/secret files.
- Quota cap: stop and write a partial receipt if you approach **40% of the 5h Antigravity window**. Log window % before/after in the receipt.

## 2. Inputs (read-only; resolve, then pin exact paths in your receipt)
1. **Cycle-9 (current, rejected):** locate SPRINT_STATUS for the 48h research-journal pilot under `.hermes/handoffs/galaxy-evolution/` / the mastermind area, resolve from it the cycle-9 draft + audit output (the audit that builds but rejects). Record resolved absolute paths + how you found them.
2. **Cycle-5 (last clean):** same resolution; this is your passing baseline for diffing.
3. **Hard-burn analyses** under `.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z/`:
   - `h3-runner-integration-packet/` (runner integration)
   - `h6-p1-invariant-rca-audit/` (invariant root-cause analysis — directly relevant to the two missing invariants)
   - `h7-p2-ledger-debate-audit/` (ledger/debate audit — directly relevant to the debate-map)
   - `HARD_BURN_ROLLUP.md` for orientation.
4. Known cycle-9 rejection set (from Duho, 20260711T050514Z): missing invariants **`249,917`** and **`24.0`**; failing gates **prior-work comparison, length, equations, tables, operator-prose, warnings**.

If any input cannot be located read-only, say so in the artifact's §D and receipt — do not guess paths into existence and do not widen your search into write operations.

## 3. Task — one substantial offline artifact
Write `cli/GORU_CYCLE9_BLOCKER_DEBATE_REPAIR_ANALYSIS.md` with these sections:

**A. Blocker inventory.** One entry per rejection item (both invariants + all six gates). For each: what the audit expects, what cycle-9 actually contains (quote + line refs), root-cause hypothesis (cross-reference H6 for the invariants; compare against how cycle-5 satisfied the same gate), and the concrete repair. For `249,917` and `24.0`: identify what these values are, every location the audit expects them, and whether the failure is omission, formatting/precision drift, or upstream data drift.

**B. Debate-map.** Reconstruct the cycle-9 discussion-phase state: positions/claims on the table, agreements vs unresolved disagreements, and which unresolved items causally block which gates (especially prior-work comparison and operator-prose). Cross-check against H7's ledger/debate audit; flag contradictions between the live discussion state and H7.

**C. Repair-priority ranking.** Ordered repair list for the next writer slot (~05:48Z, or the following slot if missed). Per repair: gate(s) fixed, effort (S/M/L), risk of regressing clean-cycle-5 properties, exact insertion target (section/heading/line anchor in the cycle-9 draft), and dependency order. Advisory only — you draft targets, you do not apply anything.

**D. Open questions / unresolved inputs.** Anything you could not verify read-only.

## 4. Receipt + marker (orchestrator watches for these)
- `cli/GORU_CLI_RECEIPT.md`: UTC start/end, model/tool used, every file read (absolute path; sha256 where cheap), Antigravity window %/weekly % before and after, safety attestation ("no writes outside cli/, runner untouched, no candidate/runner/SPRINT_STATUS writes").
- Completion marker file (empty or one-line): `cli/GORU_PILOT_CLI_DONE_20260711T050514Z` — write it **last**, after artifact + receipt.
- Deliver fast: artifact + receipt + marker are the outputs; do not burn the window on exploratory tangents beyond §2's inputs.
