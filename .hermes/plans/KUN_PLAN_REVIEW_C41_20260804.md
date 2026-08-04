# KUN ADVERSARIAL REVIEW — C41 restart plan

Plan under review: `.hermes/plans/2026-08-04_0040-c41-jwst-highz-baseline-restart.md` (Hwao, draft 2026-08-04 ~00:40 KST)
Reviewer: Kun on Hermes via Nous Portal route `moonshotai/kimi-k3`
Date: 2026-08-04 ~01:40-02:20 KST
Stance: adversarial per mandate. FINDINGS ONLY. Every checkable claim was checked against the repo/engine state I independently audited on 2026-08-03.

**Overall assessment: SOUND STRUCTURE, FOUR MATERIAL DEFECTS.** The ordering doctrine (map picks the study), the non-circularity contract in study shape #1, and the gate phrases are genuinely good. But the plan (a) assigns work to a lane ("Yui (Hermes)") that cannot execute it as written, (b) cites a "corrected crew map" that does not exist as an artifact anywhere I can find, (c) sells a 4-day schedule whose Step-2/3 throughput has no pilot precedent — the only completed Baseline run processed 26 papers with humans driving every stage — and (d) mis-describes the ranking it relies on ("v2 … promoted tonight", "controversy×tractability") in ways that are half-true and need correction before Duho anchors decisions on them.

---

## FINDING 1 (HIGH) — "Yui (Hermes)" is assigned Step 2, but Yui is a Flow/Studio lane, not a Hermes lane, and the plan's own non-goals say no new automation

Evidence: My own persistent crew-map knowledge plus the repo's canonical roster (`memory/platoon-roster.md`) contain no "Yui (Hermes)" seat; in the 2026-08-03 session context, Yui owns Flow on Mac Studio (user profile: "Tori=DR/Pro; Yui+user=Flow/Studio"). The plan's lane table lists "Tori (Hermes)" for Step 1 and "Yui (Hermes)" for Step 2 — but Tori is the Hermes seat. A "Yui (Hermes)" seat is asserted nowhere except this plan. Step 2 as specified (fulltext + source-strength labels over 120–180 papers using `tools/nm_fulltext_layer.py`) is a compute+API job requiring ADS token access and Ollama embeddings on a host; `nm_fulltext_layer.py` hardcodes `_ROOT = "/Users/duhokim/NebulaMind/NebulaMind"` and reads `backend/.env` for `NM_ADS_API_KEY` — it runs where the repo and token live. If the intent is "Yui drives it from Studio," the plan must say how (the file paths and .env are host-local). As written, the assignment is unexecutable or mis-attributed.

## FINDING 2 (HIGH) — The "corrected crew map" the plan invokes twice ("per the corrected crew map", "No Codex lanes (engine retired/unassigned)") does not exist as an inspectable artifact

Evidence: I searched the repo (`.hermes`, `docs`, `memory/`) for any crew-map document. Closest artifacts: `memory/platoon-roster.md` (v3, 2026-06-11 — predates every recent correction; it has no Hwao/Tori/Yui/Lana/Goru seats at all) and `.hermes/agents/kun-codex-lane-protocol.md` whose RETIRED banner (2026-08-03/04) is the ONLY place the "Codex engine retired, Goru on Antigravity/Gemini, Kun on Kimi K3" correction is written down. There is no single corrected crew map. The plan's crew claims are consistent with my session knowledge (Codex engine retirement is TRUE per the banner), but a plan that gates morning decisions should cite the banner file, not an absent "map". The gap also makes Finding 1 unresolvable by reference — nothing to check "Yui (Hermes)" against.

## FINDING 3 (HIGH) — Schedule realism: Steps 2–5 for 120–180 papers in 2 days has no precedent; the only completed Baseline pilot did 26 papers, and its stages were human-driven, not mechanical-throughput

Evidence: The contract-v1 AGN run (preserved at `docs/claim_ledger_contract_v1_agn_20260703T0830Z`, backup `~/HermesOps/backups/claim-ledger-contract-v1-20260721T114246Z`, receipt `PHASE0_PRESERVATION_RECEIPT.md`) processed: **16 ledger entries / 45 spans / 26 sources**. That is the ENTIRE completed corpus of Baseline-primitive execution, and it took from 2026-07-03 (contract complete marker) to 2026-07-21 (preservation receipt) with four lanes engaged. The plan's "assumes Goru mechanical runs at the span stage behave like the AGN pilot" misreads the pilot: there was no mechanical Goru span-extraction throughput in it — the spans were produced in lane review sessions. 120–180 papers is a **5–7× scale-up** over the only data point, with a new extractor (Goru/Antigravity) doing the bulk. The honesty note ("scope shrinks before quality does") partially covers this, but the Day-2/Day-3 grid presents 2 days as the plan, not as the upper bound. Realistic: Day 2–3 gets through 40–80 papers; the plan should pre-commit the shrink trigger ("if <N papers ledgered by end of Day 3, cut scope to the top-K contested-measurement papers and proceed") rather than discover it.

## FINDING 4 (MEDIUM) — Ranking mislabeling: "controversy×tractability ranking (v2)" conflates three different scores; the 0.957 cited is the citation-activity score, not the controversy score — but the #1 claim survives anyway

Evidence (all verified against promoted artifacts):
- Live `frontiersData.ts` (sha b3b0f6d5…, promoted 2026-08-03): C41 = size 1317, yearMedian 2021, recentFrac 0.426, citeMedian 46.0, nDebates 146, `score: 0.957`, `scoreV1: 0.374`, tractable 1. Plan's figures all match EXACTLY.
- `frontier_map_v3_reranked.json`: C41 `frontier_score_cite: 0.957`, `score_v1: 0.37407`, `delta_papers: 21` (matches "1,317+21" in Step 1).
- The ranking the LAB displays (and the rerank receipt's top-14 list) is by `frontier_score_cite` (citation activity). `score_v1` is the controversy×tractability composite (sat(activity) × tractable × (0.6·tension_norm + 0.4·growth_norm) per `rank_frontiers_v3.py`). There is no "v2 ranking" in the promoted pipeline — `nm_dispersion_v2.py` exists and its output `dispersion_v2.json` exists, but the promoted frontiersData derives from the v3-rank/v1-score machinery; "v2" appears to refer to the dispersion work, which feeds `strict_tension` only partially (rerank path keeps constants frozen).
- The good news for the plan: C41 is #1 under BOTH metrics — #1 by `frontier_score_cite` (0.957) AND #1 by `scoreV1` (0.374, next core is C40 at 0.143) AND #1 in `FRONTIER_RANK_MOVEMENT` (previousRank 1 → currentRank 1). And under the hand-reviewed core-scope filter (`frontierScope.ts`, merged via #129), C41 is also the top core cluster. So the plan's central empirical claim — "C41 is the #1 frontier" — is TRUE under every ranking interpretation on the box. But the sentence describing WHY should be fixed before the morning review, because Duho will ask "which ranking?" and the plan as written gives a muddled answer.

## FINDING 5 (MEDIUM) — nDebates=146: the plan's honesty note is correct and should go further — the number is `round(strict_tension × size)` where strict_tension is a title/abstract LEXICON hit rate, not a debate count

Evidence: `gen_frontiers_data.py:70` — `"nDebates": int(round(c["strict_tension"]*c["size"]))`; `rank_frontiers_v3.py:130` — `strict_tension = strict_hit / n` where hits come from STRICT_TERMS (`tension/discrepan/contradict/inconsisten/cannot explain`) mined from titles+abstracts with the physics-quantity-tension strip fix. 0.11086 × 1317 = 146. So "146 debates" ≈ "146 papers in C41 whose title/abstract fires a disagreement lexeme." The plan's note ("lexicon-derived count, not 146 real controversies") is accurate; my addition: the condensation target "~8–15 live axes" is plausible but has no derivation — Step 6 should report the condensation explicitly (146 lexicon hits → K merged axes, with the merge rule receipted), not just land in range.

## FINDING 6 (MEDIUM) — Study shape #1's non-circularity contract is good but incomplete: it guards data-vs-model contact, not selection-vs-result contact

The shape's stated defense: "data side never touches the models; model side never fits our data." Real and necessary. But the dominant circularity risk in bright-end-UV-LF work is subtler: **the catalogs (JADES/CEERS/COSMOS-Web) are the same public catalogs the model papers themselves use for normalization/validation**, and the same JWST photometry feeds both the LF estimate and some of the claimed tensions. A published-prediction-vs-public-catalog comparison can still be circular at the level of shared reduction pipelines, shared photometric-redshift codes (EAZY/BEAGLE assumptions), and shared completeness corrections. The fix is cheap and belongs in the Step-1 corpus protocol: require the LF assembly to state, per catalog, which reduction/photo-z/completeness chain it inherits, and prefer model predictions whose papers do NOT calibrate on those same chains (or declare the overlap as a scope limit in the ledger). The plan's fallback honesty (shape #1 → #3 if completeness fails) is genuinely good practice — keep it, extend it to this class.

## FINDING 7 (MEDIUM) — Step-1 "no cherry-picking clause" is aspirational; the enforceable mechanism is not named

The corpus protocol is where motivated selection would enter (this is exactly the doctrine's "evidence-hunting forbidden" rule applied upstream). The plan says "selection rules … no cherry-picking clause" and "frozen selection list w/ shas" — good — but the refutation loop is "Kun refutes" with no stated refutation CRITERIA. Suggest the Step-1 gate include three mechanical checks I can run cheaply: (a) selection rule expressed as an executable filter over the C41 member list (which exists: cluster assignments in the engine's labels) BEFORE anyone reads titles; (b) the excluded-paper list published with reasons-per-class, not just the included list; (c) a decoy test — I inject K papers designed to tempt motivated exclusion (e.g., a paper contradicting the expected map outcome); the protocol must retain them or name a rule-based reason. Without (a)-(c), "no cherry-picking" is a promise, not a control.

## FINDING 8 (LOW-MEDIUM) — Gate structure is mostly strong; two gaps

Good: verbatim gate phrases per step, Duho-freezes-Step-0, findings-only until Step 6, artifacts in a lane dir, git capture only via the proven PR path at approved boundaries. Gaps:
(a) **Track-B gate is under-specified relative to Track-A.** "the final pick waits for the map + Duho's gate" — but no gate PHRASE is defined for the Track-B pick, and Week-2 work (measurement execution) has no stage gates at all in this document. If the measurement starts Day 5+, its gate phrases should exist now (the morning review is exactly when Duho's attention is available). Suggest: `APPROVE C41 TRACK-B SHAPE <n> — <name>` and `APPROVE C41 TRACK-B MEASUREMENT START`.
(b) The plan says "no DB/live/wiki/git writes inside the stages" — but Step 2's `nm_fulltext_layer.py` writes to `fulltext_cache/` under the engine dir, and Step 6 receipts will write files. Clarify "writes" = product/DB/git surfaces; engine-dir and lane-dir artifact writes are obviously necessary. Minor wording, but this crew runs on precise gates.

## FINDING 9 (LOW) — Verified TRUE claims (for the record, so the morning review knows what it can rely on)

- C41 stats quoted: all exact matches to promoted data (Finding 4).
- "1,317+21": engine reranked JSON `delta_papers: 21` for C41. TRUE.
- Newest-member name-drops: "A Massive Galaxy at the Edge of Feedback-Free Efficiency" (arXiv 2607.29589) and the Azahar papers (2607.15344, 2607.15357) are real, in the delta store, assigned to cluster 41. TRUE.
- Tools named: `nm_external_data.py` (tracked, #127; VizieR TAP raw-HTTP + retry/backoff + cache — verified content), `nm_fulltext_layer.py` (exists, UNTRACKED — see Finding 10), `nm_paper_history.py` (tracked; does exactly what the plan says — append-only human-direction log). TRUE with one tracking caveat.
- "claim-ledger contract v1 exists and was validated on the 26-paper AGN pilot": TRUE — contract + 16-entry ledger + 26-source scope checks preserved at `docs/claim_ledger_contract_v1_agn_20260703T0830Z` with sha manifest and PASS validation receipt (16 entries/45 spans/26 sources/0 errors). The plan can lean on this; it's real.
- "No Codex lanes (engine retired/unassigned)": TRUE per the retired banner in `.hermes/agents/kun-codex-lane-protocol.md` (and consistent with my session knowledge that Duho retired the Codex engine 2026-08-03).
- R7 framing ("Baseline stalled at status/debate-map-next since 2026-07-03; this advances the real stage"): consistent with the board (still dated 2026-07-21, stage table unchanged) and with my audit.

## FINDING 10 (LOW) — `nm_fulltext_layer.py` is untracked; Step 2 would run production-adjacent research tooling that exists in no commit

Same class as my closed R5 finding (the frontier scheduler was untracked until #130). If Step 2 executes, its primary tool should be committed first (trivial PR via the proven path) — otherwise the Step-2 receipts will cite code git cannot reproduce. Note: the file also hardcodes repo-absolute `_ROOT` paths, which intersects Finding 1's lane/host question.

## FINDING 11 (LOW) — DR throttle ("at most 2 DR runs, spaced") is consistent with the crew's standing DR-as-reference doctrine, but the feedback links are dead

All six `[[...]]` Obsidian-style references in the plan (`[[feedback_autopilot_publishable_bar]]`, `[[feedback_frontier_not_lowhanging]]`, `[[feedback_dr_as_reference_not_lane_replacement]]`, `[[reference_dr_account_throttle_gentle_pace]]`, `[[reference_metallicity_calibration_scale]]`, `[[feedback_auto_record_human_paper_history]]`) resolve NOWHERE in the repo (grep across .hermes/docs finds only the plan itself; the old Obsidian vault at `~/Documents/Obsidian Vault (old)/` is retired per the crew's communication protocol). The claims behind them are consistent with session knowledge (autopilot rejections, DR-as-reference, the Te-vs-strong-line ~0.24 dex trap), but the morning review should not treat the links as checkable citations. Either inline the one-line substance of each (the plan already does for the metallicity trap) or point them at wherever these notes now live.

## FINDING 12 (LOW) — Track-B shape #3's claim "ties into the v2 dispersion machinery that already promotes f_esc as contested" is accurate

Verified: `nm_dispersion_v2.py` has an `fesc` quantity definition (LyC escape fraction, fraction-range validation, percent-fix at line ~545), and `dispersion_v2.json` exists in the engine dir. No defect; noted so the morning review knows this one checks out.

---

## Recommendations to fold in before the morning gate (ranked)

1. Reassign or re-specify Step 2: either "Tori (Hermes)" executes it on the repo host, or spell out Yui's Studio execution path; commit `nm_fulltext_layer.py` first (Findings 1, 10).
2. Cite the actual crew-correction artifact (the retired banner) instead of the absent "corrected crew map"; better: write the one-paragraph corrected crew map into the plan header (Finding 2).
3. Add the shrink trigger to the Day-2/3 schedule as a pre-committed rule with numbers (Finding 3).
4. Fix the ranking sentence: "C41 is #1 under both the citation-activity ranking shown on the Lab (score 0.957) and the controversy×tractability composite (scoreV1 0.374), before and after the 2026-08-03 rerank" (Finding 4).
5. Add the Step-6 condensation report requirement (146→K axes with merge rule) (Finding 5).
6. Extend shape #1's non-circularity contract with the shared-pipeline/completeness overlap declaration (Finding 6).
7. Convert the no-cherry-picking clause into the three mechanical checks (executable filter, published exclusions-by-class, decoy test) (Finding 7).
8. Define Track-B gate phrases now (Finding 8a); clarify the writes carve-out (Finding 8b).
9. Inline or re-point the dead `[[...]]` references (Finding 11).

## Evidence ledger (commands/reads, all read-only)

- Read plan in full (119 lines).
- C41 data: regex/python extraction from `frontend/src/app/lab/frontiersData.ts` (C41 block, FRONTIER_RANK_MOVEMENT "41", all-57 scoreV1 parse + core/all rankings); `.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718/frontier_map_v3_reranked.json` (C41 record; top-5 by frontier_score_cite; rank_movements).
- nDebates provenance: `gen_frontiers_data.py:70`, `rank_frontiers_v3.py:23-27,130` (STRICT_TERMS lexicon, string-tension strip, strict_hit/n).
- Delta membership: `delta/new_papers.jsonl` scan → 2607.29589 (Feedback-Free), 2607.15344/2607.15357 (Azahar) → cluster 41.
- Tools: reads of `tools/nm_external_data.py` (TAP/retry/cache lines), `tools/nm_fulltext_layer.py` (full header; `_ROOT`/.env/ADS token mechanics; 280 lines; untracked per `git ls-files`), `tools/nm_paper_history.py` (docstring).
- Contract v1: `docs/claim_ledger_contract_v1_agn_20260703T0830Z` + `~/HermesOps/backups/claim-ledger-contract-v1-20260721T114246Z` (both exist, full structure); `PHASE0_PRESERVATION_RECEIPT.md` (PASS, 16/45/26 counts); sha manifest (36 rows) — note: the phase0 copy in the handoffs dir is manifest+receipt ONLY (artifacts live in docs/ + backup), which is fine but worth knowing.
- Crew: `memory/platoon-roster.md` (v3 roster, no crew seats); `.hermes/agents/kun-codex-lane-protocol.md` (RETIRED banner — the actual crew-correction text); `.hermes/agents/subnav-watcher-governance.md` (exists — closes my earlier R3 residue; read while in the directory); searches for "crew map" document: none found.
- Dispersion: `tools/nm_dispersion_v2.py` (fesc quantity def), `dispersion_v2.json` exists.
- Roadmap cross-read: `.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md` (step vocabulary, AGN seed entries §, line 592 "26 already full-text-checked AGN papers").
- Board state: `paper-prose-distillation-board.md` header/stage table (Updated 2026-07-21; claim-ledger complete; status/debate map next).
- `[[...]]` reference resolution: grep across `.hermes`, `docs` — no targets; `~/Documents/Obsidian Vault (old)/.obsidian` exists (retired vault).
- No writes except this report. No `.env*` opened (nm_fulltext_layer's token-reading code was read, not executed).

## Uncertainties

- Whether "Yui (Hermes)" reflects a post-my-knowledge seat change Duho made verbally tonight; if so, Finding 1 downgrades to "document it." Flagged as inference either way.
- The actual throughput of Goru/Antigravity on mechanical span extraction has no prior data point; Finding 3's 40–80 estimate is my inference from the 26-paper pilot's human-driven pace, not a measurement.
- I did not verify JADES/CEERS/COSMOS-Web VizieR table availability (the plan correctly defers this to Step 1 with a fallback; no network queries beyond localhost/nebulamind probes were in scope tonight).
- The 146→8–15 condensation plausibility: untestable until Step 6; Finding 5 asks for the merge-rule receipt rather than prejudging the number.

---

KUN_C41_PLAN_REVIEW_COMPLETE_20260804
