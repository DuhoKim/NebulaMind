# P4 brief — derived claim/evidence candidates from the clean cycle-5 package (offline, wiki-shaped)

Marker: `HWAO_FABLE_BURN_P4_BRIEF_20260711T010503Z`
Issued: 2026-07-11 ≈02:19Z by Hwao (coordinator). Clock check at issue: `2026-07-11T02:17:47Z`. Relayed by Tori, file handoff only.
Lane: **one single fresh Lana Fable pane** (not a reused P1/P2/P3 pane). Supervision: Tori (meter, stop/hold files, custody), Hwao (receipt review).
Authorization chain: Duho `approve fable burn 20260711T010503Z` → `HWAO_FABLE_BURN_EXECUTION_ACCEPTED_20260711T010503Z` → condition packet `TORI_FABLE_BURN_P4_CONDITION_MET_20260711T021637Z` → this brief.

Condition verified by Hwao at 02:17:47Z: P1/P2/P3 done markers present and all three receipts `status: COMPLETE` with correct final markers; Fable weekly 9% (< 60%); Fable 5-hour 27%; clock < 03:15Z; no `GLOBAL_STOP_20260711T010503Z.md` or `HOLD_5H_20260711T010503Z.md` at the burn root.

This brief is self-contained. If anything on disk conflicts with it, the safety boundaries in §7 win; note the conflict in your receipt.

## 1. Mission

The cycle-5 package is RP-1's last integrity-clean manuscript state (flagship + supplement), and P1 has just produced a 105-entry numeric-invariant manifest plus an invariant-safe reference block from it. Your packet extracts **candidate claim/evidence pairs** from that clean package into **offline, wiki-shaped candidates** following the repo's `wiki_schema.md` conventions — each pair carrying exact source line references, numerals verbatim per the manifest, and the association-only wording contract. These are staging assets for a later, separately-gated wiki/integrator pass. **Offline candidates only: nothing you write is published, and you never touch the DB, API, wiki, or the runner's `candidates/` tree.**

This is the plan's sanctioned stretch packet. It has a **30-minute hard cap** — quality over count; stop clean.

## 2. Write scope (your ONLY writable directory)

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p4-derived-claims/`

Create it (`mkdir -p`) as your first action. Everything else on this machine is read-only to you.

## 3. Sources (read-only — these and nothing else)

Evidence sources (the only permitted claim/evidence basis):

1. Clean cycle-5 package (LIVE runner-owned tree — read-only; snapshot before use):
   - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex`
     expected sha256: `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384`
   - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`
     expected sha256: `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71`
2. P1 outputs (sibling packet dir — you may READ exactly these two files, write nothing there):
   - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants/INVARIANT_MANIFEST.json`
     expected sha256: `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717`
   - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p1-rp1-invariants/INTRODUCTION_LITERATURE_REFERENCE.md`
     expected sha256: `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d`

Formatting reference (conventions only, not an evidence source):

3. `/Users/duhokim/NebulaMind/NebulaMind/wiki_schema.md` — follow its claim/evidence conventions for shaping the candidates. It is a working-tree file with no pinned hash; record the hash you observed in your receipt. Where the schema implies DB-resident fields (ids, foreign keys, publish state), use explicit `OFFLINE_PLACEHOLDER` values — never real DB values.

**Snapshot and verify first.** Copy the two tex files into `p4-derived-claims/sources-snapshot/`, `shasum -a 256` all four evidence sources, and compare against the expected hashes above (they come from the P1/P2 receipts, cross-corroborated). **Any mismatch → stop immediately with receipt status `BLOCKED`** (it would mean the clean package or P1 outputs changed under you — that is for Hwao, not you, to resolve). Work only from your snapshots for line references.

No other evidence inputs: not the cycle-6/7 packages, not the Gemini materials, not P2/P3 outputs, not the wider repo, not your own memory of the literature. A claim you cannot anchor to a cycle-5 line (or a manifest entry) does not become a candidate.

## 4. Deliverables (exact filenames, in your write dir)

1. **`CLAIM_EVIDENCE_CANDIDATES.md`** — top line marker `FABLE_BURN_P4_CLAIM_EVIDENCE_CANDIDATES_20260711T010503Z`, then a header stating plainly: *offline candidates — not published, not integrated; every numeral verbatim from cycle 5 per `INVARIANT_MANIFEST.json`; association-only wording contract applies.* Then the candidate pairs, each with:
   - `candidate_id` (`P4-C01`, `P4-C02`, …);
   - `claim_text` — association-only wording: no "establishes"/"demonstrates"/"proves"/causal phrasing; carry RP-1's scope caveats (association-only, morphology-uncontrolled, fiber-centered) wherever the claim would otherwise overread;
   - `evidence` — one or more entries, each with source file (cycle-5 package-relative path), exact line number(s) in your snapshot, the verbatim quoted span, and the matching `INVARIANT_MANIFEST.json` entry id(s) for every numeral;
   - `numerals_check` — confirmation that each numeral in the claim/evidence matches the manifest `exact_string` character-for-character (cycles 6/7 died on exactly this — re-typed numbers);
   - `caveats` and `verification: LOCAL_ONLY`;
   - wiki-shaped structure per `wiki_schema.md` conventions, with `OFFLINE_PLACEHOLDER` for DB-resident fields.
   As many complete, high-quality pairs as the 30-minute cap allows — a finished pair beats two half-pairs; cover the flagship's headline results before supplement detail.
2. **`P4_RECEIPT.md`** — see §8.
3. On full completion only: empty marker file named exactly `FABLE_BURN_P4_DONE_20260711T010503Z`.

## 5. First action (ACK)

`mkdir -p` your write dir, then write `P4_ACK.md` containing: the line `FABLE_BURN_P4_ACK_20260711T010503Z`, your ACK timestamp UTC (this is your T0_lane), your tmux pane id, and the brief marker you received (`HWAO_FABLE_BURN_P4_BRIEF_20260711T010503Z`).

**Late-start guard:** if your ACK time is ≥ `2026-07-11T03:15:00Z`, do not start work — write `P4_RECEIPT.md` with status `BLOCKED` (P4 latest-start condition expired), final line `FABLE_BURN_P4_PARTIAL_20260711T010503Z`, and stop.

## 6. Timeline and stop conditions

- **Hard cap: T0_lane + 30 min.** No target/overrun split — at the cap, stop where you are and write the receipt (status `PARTIAL` if the done set is incomplete).
- Absolute stops, whichever comes first:
  1. `GLOBAL_STOP_20260711T010503Z.md` exists at the burn root (`fable-weekly-burn-20260711T010503Z/`);
  2. your clock ≥ **2026-07-11T03:50:00Z**;
  3. the 30-minute hard cap.
- Poll the burn root for `GLOBAL_STOP_20260711T010503Z.md` and `HOLD_5H_20260711T010503Z.md` at ACK, at least once mid-run (~15 min), and before writing the receipt.
- `HOLD_5H` present → finish only the candidate pair in progress, write receipt with status `HELD_5H`, stop.
- Any stop before completion → receipt status `PARTIAL` (or `HELD_5H`/`BLOCKED`), final line `FABLE_BURN_P4_PARTIAL_20260711T010503Z`, and NO done marker file.
- Done early → stop immediately. There is nothing after P4; do not invent work.

## 7. Safety boundaries (absolute — crossing any of these ends the packet)

1. **Write scope:** create/modify files ONLY inside `p4-derived-claims/`. Everything else — the burn root, `briefs/`, `METER_LOG.md`, the `p1`/`p2`/`p3` dirs, the sprint tree, the repo (including `wiki_schema.md`, `frontend/`, `backend/`) — is read-only to you.
2. **Runner isolation:** the sprint tree `ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/` is live and runner-owned: never write there, never write into any `candidates/` tree, never promote anything, never touch/signal/patch/kill PID 45665 or any other process. If cycle-8 material appears, ignore it.
3. **No network:** no browser or browser automation, no WebFetch/WebSearch, no curl/wget or package installs, no ADS/arXiv/VizieR/SDSS lookups, no MCP network tools. External-literature enrichment of these candidates is a later, separately-gated pass.
4. **No product/state mutation:** no DB/SQL, no API calls (incl. `/api/pages`, page_versions), no live wiki publication of any candidate, no deploy/restart, no service changes. Your output is files in your write dir — nothing else changes state.
5. **No git:** no add/commit/push/branch/tag/stash — not even for your own artifacts.
6. **No scheduling/daemons:** no cron, launchd, background jobs, or new monitors.
7. **No credentials/billing/cloud:** no OAuth/API-key/credential access, no reading `.env*` or secret files, no billing/account/`/credits` actions, no gcloud/GCP/cloud CLIs.
8. **No pane interference:** no tmux send-keys of any free text to any pane; do not interact with other panes; the unsent composer text in `ge-mastermind:0.0` must not be disturbed. You communicate only via files in your own write dir.
9. **Fail closed:** if a step seems to require crossing any line above, don't — record the conflict in the receipt and continue with what is allowed, or stop with status `BLOCKED`.

Allowed tooling: local read-only text processing (`grep -n`, `diff`, `awk`, `wc`, `shasum -a 256`, etc.) plus file writes inside your write dir.

## 8. Receipt spec (`P4_RECEIPT.md`)

- `status:` COMPLETE | PARTIAL | HELD_5H | BLOCKED
- `t_ack` / `t_end` (UTC), pane id
- Artifact table: filename, byte size, sha256
- Source table: all four evidence sources + `wiki_schema.md`, absolute path, observed sha256, and PASS/FAIL against the expected hashes in §3
- Candidate count and a one-line list of candidate ids with their flagship/supplement anchor
- Numerals check summary: every numeral used ↔ manifest entry id, zero unmatched (or the exceptions listed)
- Deviations from this brief (should be none) and any ambiguity you resolved, with the choice made
- Follow-up queue, each line labeled `GATED — needs separate Duho approval` (at minimum: integrator/wiki handoff of the candidates; any network verification the pairs would benefit from)
- Coordination-file checks performed (timestamps, result)
- Final line: exactly `FABLE_BURN_P4_DONE_20260711T010503Z` (complete) or `FABLE_BURN_P4_PARTIAL_20260711T010503Z` (anything less)

`HWAO_FABLE_BURN_P4_BRIEF_20260711T010503Z`
