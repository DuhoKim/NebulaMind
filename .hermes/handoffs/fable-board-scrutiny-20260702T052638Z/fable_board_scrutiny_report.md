# Fable 5 Board Scrutiny Report — Hermes / Lana / Goru

Task ID: `fable-board-scrutiny-20260702T052638Z`
Author: Fable 5 (outside reviewer, read-only inspection)
Written: 2026-07-02 (KST afternoon), repo `/Users/duhokim/NebulaMind/NebulaMind`, branch `feat/surveys-atlas-ia-p1-20260627`, HEAD `e5ceda8`

Evidence base: board files under `.hermes/board/`, the roadmap plan, the full 2026-07-01 → 2026-07-02 packet chain under `docs/paper_*` and `docs/paper_overnight_distillation_20260702T002532Z/`, the ingest preflight with its read-only public API snapshots, harvest tick summaries, and `git status`. No DB access, no writes except this report.

---

## 1. Executive verdict: partly right — correct direction, real discovery, but the loop has not been closed and the process is eating the mission

The redirect away from UI churn toward paper→claim→evidence→stance→contradiction→readiness→cited prose is the right mission, and the board did genuinely non-trivial work in the last ~15 hours (2026-07-01T12:26Z pilot → 2026-07-02T02:56Z preflight):

- It found **real, named errors in live content**, with source positions: the dark-energy page's `w ~ -0.85` DES claim (actual DES-SN5YR values: w = −0.80 +0.14/−0.16 SN-alone, −0.941 ± 0.026 combined, consistent with Λ within ~2σ, reconfirmed twice from arXiv:2401.02929); the GRB "energy as the mass of a small star" overreach; the White Dwarfs "1930s observational confirmation by Willem Luyten" story that no source supports; universal 0.01 R☉ radius and 0.5–1.2 M☉ wording presented as consensus; magnetic-WD merger-dominance claims.
- It built a defensible correction packet: 3 pages, 7 reader-facing sections, 54 verified citation anchors, an 18-row NO-GO ledger that survived four review layers (`docs/paper_overnight_distillation_20260702T002532Z/post_refinement_review_20260702T010238Z/`).
- Safety discipline was real, not claimed: read-only SQL, public API snapshots before proposing changes, zero mutations anywhere I checked.

Here is the problem. **As of the preflight snapshots (2026-07-02T02:56Z), the live wiki still serves every one of those refuted claims** — claim 1002 `w ~ -0.85` (labeled "debated"), claim 1184 "mass of a small star" (labeled **"accepted"**), claim 1007 Luyten (labeled **"accepted"**), claims 1008/1009/1016 unchanged. I verified this directly in `product_wiki_ingest_preflight_20260702T025609Z/readonly_public_snapshots/`. Fifteen hours of pipeline produced zero user-visible corrections, while the product actively tells readers things the board has proven wrong. The board's own preflight says exactly what is missing (`PRODUCT_EVIDENCE_IDS_RESOLVED: 0`, `CLAIM_MARKERS_RESOLVED: 0`, `FULL_PAGE_CONTENT_DIFF_PREPARED: false`) and then the campaign stopped one step short of the only step that matters.

Second problem, and it is strategic: the top-20 verification chain quietly demolished the corpus's headline numbers, and nobody said it plainly. Citation-snippet verification reviewed 240 candidate evidence snippets and accepted only ~20–31 (8–13%) as actually positioning the exact claim; 218 were "reviewed_not_sufficient_for_exact_claim." The corpus's "11,816 evidence rows, 88.8% support" is therefore mostly topical association, not claim-grounding — the uniform "50 support / 0 counter" rows on things like claim 1262 ("The Milky Way could be much younger than 13.6 Gyr", labeled accepted/ready_for_prose) are the tell. **True snippet-verified grounding today is roughly 10 claims out of 1,305, not 714 out of 1,305.** The mission is ~1% done, not ~55% done. That reframing should be stated on the board and should drive everything that follows.

Verdict in one sentence: right target, real findings, excessive ceremony, and a failure to ship — the board is currently a very good fact-checking machine wired to a printer that has never been turned on.

## 2. Biggest blind spots

1. **No shipped correction = the product is publishing known errors.** The gap between "we proved it wrong" and "the reader stops seeing it" is the entire value of the mission, and it is unclosed. Worse, wrong claims carry `accepted`/`consensus` trust labels in the live payloads, so the product is not merely stale, it is confidently wrong.
2. **Process ceremony scales faster than output.** ~258 `paper_*` artifact files (~12 MB) across ~15 sequential gated packets in ~15 hours, each minting its own bespoke approval phrase, marker, safety-ledger boilerplate, validation JSON, handoff, and cockpit update — to move 20 claims to "docs candidate." Each step re-reviews the previous step (review → refinement → post-refinement review → micro-cleanup v2 → preflight). At this unit cost, the remaining 1,035 needs-adjudication papers are years away. The gates were designed for safety; they have metastasized into the work itself.
3. **Approval-phrase inflation trains the operator to rubber-stamp.** Every summary ends with a new multi-sentence APPROVE phrase (I counted at least 10 distinct phrase families in 24 hours). When everything needs a unique paste, approvals stop being decisions. Three standing gate classes would do: read-only analysis, docs-only packet, per-packet mutation execute.
4. **The durable board is stale.** `.hermes/board/paper-prose-distillation-board.md` still shows every lane `[next]` and its cards unticked, last updated 2026-07-01T11:58Z — before the pilot even ran. The real work went ~15 packets past the board without the board being updated. A board that doesn't reflect state is decoration, and an outside reviewer (or Duho at a glance) cannot tell what's done.
5. **Evidence-table inflation was discovered but not escalated.** The 8–13% snippet acceptance rate is the single most important systemic finding of the campaign — it means "claims_with_evidence: 714" is not a trust metric — yet it appears only as counts inside a mid-chain summary JSON. It should have immediately changed the roadmap ("stop trusting stance counts; snippet-verify everything before prose") and been reported as a headline.
6. **Data hygiene defects noticed and dropped.** 526 of 1,305 claims carry trust_level `"0.5"` (a numeric string) mixed in with enum labels (`accepted`, `debated`, …). That's a schema defect in the product's trust surface, found on 2026-07-01, queued nowhere.
7. **Harvest ticks hit diminishing returns.** Six overnight ticks re-hammered the same 5–7 gap targets (DES numeric, Luyten history, WD radius/mass, magnetic WD, cluster observables), mostly re-confirming what earlier ticks had already established ("…RECONFIRMED", "…STILL_BLOCKED" statuses). Meanwhile 591 claims have zero evidence rows at all. Repetition without a stop rule is spend, not progress.
8. **"Read-only" runs write into production-served directories.** Each cron tick mirrors cockpit HTML/JSON into `frontend/public/agent-reports/` of **two** worktrees plus `HermesOps`, accumulating 15 backup files per tick, under approvals whose ledgers say "no production config changes." It's within the letter of the overnight approval, but it erodes the meaning of the read-only boundary and clutters a deploy-served path.
9. **The campaign is not version-controlled.** 201 dirty/untracked files; the entire distillation corpus lives outside git on a feature branch that also carries unrelated modified source (`backend/app/routers/pages.py`, `model_canary.py`, frontend edits). One careless `git clean -fd` erases the whole campaign. There is no committed, reviewable record of any of this.
10. **Goru is underemployed as a rubber stamp.** Goru's headline "issue" in the wiki-prose review was a heading-capitalization nit, and its source-lock mechanical check "checked only an early subset… superseded by Hermes." The mechanical lane should own deterministic validation scripts (ID resolution, anchor→row checks, NO-GO phrase grep, diff dry-runs) whose pass/fail gates the packet — not write prose memos.

## 3. What Fable would stop doing immediately

- **Stop opening new analysis/review layers.** No packet re-reviews, no "review of the refinement of the review." The current packet has passed four layers; a fifth adds cost, not confidence.
- **Stop the source-gap harvest ticks on the current 7 targets.** They are re-confirming settled positions. Re-enable harvesting only when a new tranche defines new gap targets.
- **Stop minting bespoke approval phrases per micro-step.** Collapse to the three-gate structure the preflight itself already implies (A1/A2 docs-only; A3 execute; A4 verify).
- **Stop cockpit mirroring on every tick** (or reduce to one root, one update per slice, no per-tick backups). It is boundary erosion plus file litter for negligible steering value.
- **Stop treating raw stance counts ("50 support rows") as readiness.** No claim goes to prose on counts alone anymore; snippet-verified positions only. Say this on the board.
- **Do not start any new campaign directory (galaxy_v2, page58, surveys, or a new paper tranche) until the current 3-page correction ships or Duho explicitly re-prioritizes.**

## 4. What Fable would do next — one slice: **ship the 3-page correction**

The next slice is exactly the thing the preflight declared missing, and nothing else: **the exact-diff publication packet for pages 5 (dark-energy), 19 (gamma-ray-bursts), 23 (white-dwarfs), ending in a single EXECUTE phrase for Duho.**

Concretely, the slice converts `reader_facing_cleanup_v2_*` (3 pages, 7 sections, 54 anchors, 18 NO-GO rows) into:

1. Resolved product IDs: every anchor mapped to an existing `evidence.id` (or an explicit INSERT row with full provenance), every section mapped to existing claim IDs with a per-claim decision — `update_text` / `relabel_trust` / `retire_and_replace` — covering at minimum claims 1002, 1184, 1007, 1008, 1009, 1016, 1273, 1277, 1278.
2. Whole-page before/after content diffs against the already-captured public snapshots, hash-pinned to the snapshot state.
3. A row-level backup file (read-only SELECT dump of affected rows) plus a restore script that is dry-run-validated against the backup before the packet is presented.
4. One packet-specific EXECUTE phrase and one ROLLBACK phrase, both minted inside the packet.

This is Approval A1+A2 from the preflight's own `required_approvals.jsonl`, fused into one slice. It is docs-only and read-only against the DB, so it is safe to run now; the only mutation remains behind Duho's paste of the EXECUTE phrase.

Why this and not "industrialize the pipeline" or "start tranche 2": because until one correction round-trips to the live page, the board has no proof its 15-hour pipeline produces anything a reader ever sees, and no unit-economics baseline to industrialize from. Ship first, then scale.

## 5. Step-by-step plan for the slice

**Timebox: 4 hours of lane time. One output directory:** `docs/paper_product_wiki_exact_diff_<UTC>/`. No other writes except one final board-status update.

- **Step 0 — Hermes:** freeze inputs. Record SHA-256 of the cleanup-v2 pages/sections/registry/NO-GO files and of the 9 public snapshots. Any later mismatch = stop.
- **Step 1 — Hermes (read-only DB):** snapshot `wiki_pages`, `page_versions`, `claims`, `evidence`, `page_citation_links`, `fact_sources` rows for page IDs 5/19/23 only (`BEGIN READ ONLY … ROLLBACK`), written as the backup JSONL + a `current_content_hash` per page. This is preflight approval A1.
- **Step 2 — Goru (deterministic scripts, not prose):** resolve all 54 anchors against the snapshot: for each, either an existing `evidence.id` (match on arxiv id + snippet position) or an `INSERT` candidate row with source URL, quoted snippet, and role. Resolve the 9 target claims to IDs with proposed action and new trust label. Output: `anchor_id_resolution.jsonl`, `claim_action_map.jsonl`, and a machine `validation.json` whose checks are: 54/54 anchors resolved or explicitly INSERT-flagged; 0 NO-GO phrases present in proposed content (grep the 18 ledger phrases); before-hashes match snapshots; proposed page content passes the same canonicalizer/contract checks the preflight ran.
- **Step 3 — Hermes:** author the whole-page diffs (current snapshot text → cleanup-v2 text placed under the target headings from `target_page_map.jsonl`), plus the guarded apply plan: per-page ordering (dark-energy first — smallest, crispest correction), API-or-SQL choice per write, `version_num` expectations (+1 per page), and the rollback script.
- **Step 4 — Lana (adversarial, one pass):** try to refute the packet: sample ≥10 anchors and check the quoted snippet actually supports the sentence it anchors; check each claim action against the adjudication decisions; check the diffs don't delete live content that was never adjudicated (sections outside the 7 must be byte-identical). Verdict: PASS / list of defects. One pass, no re-review cycle; defects go back to Step 2/3 once.
- **Step 5 — Hermes:** assemble the packet with the EXECUTE and ROLLBACK phrases and hand off to Duho. **Stop. No execution under this slice.**

**Expected artifacts (all in the one directory):** backup JSONL, anchor/claim resolution maps, per-page unified diffs, apply plan, rollback script + dry-run log, Goru `validation.json`, Lana verdict MD, packet MD with the two phrases, and a summary JSON.

**Verification (after Duho executes, as A4):** re-fetch the 3 public pages; assert `-0.85` and "mass of a small star" and the Luyten-confirmation sentence are gone; assert new DES numbers render; assert 54 anchors resolve in the public citations payload; assert `version_num` incremented exactly once per page; archive post-apply snapshots next to the pre-apply ones.

**Stop conditions:** any anchor unresolvable → mark BLOCKED, exclude that sentence, never invent IDs; live content hash drifted from snapshot → re-snapshot once, re-diff, and if it drifts again, stop and report; Lana finds a NO-GO leak → fix once or drop the section; 4-hour timebox reached → ship the packet with explicit gaps rather than extending.

## 6. Decision gates and approval phrases

Gate structure going forward (three classes, no new families):

- **G1 read-only analysis** — standing approval, no per-run phrases.
- **G2 docs-only packet** — standing approval per named slice.
- **G3 mutation execute** — always packet-specific, minted inside the packet, pasted by Duho only.

**The one phrase Duho needs to paste to start this slice (G2, covers preflight A1+A2):**

```text
APPROVE EXACT-DIFF PUBLICATION PACKET: Take a read-only DB snapshot of wiki_pages, page_versions, claims, evidence, page_citation_links, and fact_sources for page IDs 5, 19, 23 only; then author one docs-only exact-diff packet mapping the reader-facing cleanup v2 prose onto resolved product claim/evidence IDs, with whole-page before/after diffs, row-level backup, a dry-run-validated rollback script, and a single packet-specific EXECUTE phrase for my later approval. Write docs/JSONL/Markdown artifacts only, in one new directory. No DB writes, SQL mutations, migrations, deploy/restart, production config changes, OpenClaw relay, runtime source edits, secrets reads, destructive cleanup, or commit/push/merge. Timebox 4 hours; no new harvest ticks, no cockpit rewrites beyond one final status line, no new approval-phrase families.
```

Execution of the diff (G3) and any post-apply render/deploy checks (A4) remain separate pastes, exactly as the preflight designed. Separately — not part of this slice — Duho should decide whether to approve committing the distillation artifacts to a branch; right now the entire campaign is uncommitted working-tree state and one destructive git command from vanishing.

## 7. Risks, failure modes, and how to avoid artifact theater

- **Theater risk #1: the slice produces another beautiful packet and stalls again.** Countermeasure: the slice's definition of done includes the EXECUTE phrase in Duho's hands, and the board file gets a single line: `WAITING_ON_EXECUTE: <packet path>`. If the board writes any new analysis directory before that line clears, that is theater; call it.
- **Theater risk #2: validation by prose.** Goru writing "I checked and it looks right" is worthless; only script-emitted pass/fail counts gate the packet. Lana's review must name defects or say PASS — "PASS_WITH_LIMITATIONS" is banned in this slice; a limitation is either a defect (fix/drop) or a documented exclusion.
- **ID-resolution turns up mismatches** (likely, given the 8–13% snippet-acceptance finding): some anchors may have no existing evidence row. That's fine — INSERT plans with provenance are allowed — but if more than ~⅓ of anchors need inserts, pause and tell Duho, because it means publishing requires growing the evidence table, a bigger decision.
- **Concurrent drift:** the wiki is live and other lanes (surveys branch) touch `pages.py`. Hash-pin everything; apply must abort on hash mismatch, not merge.
- **Blast radius:** three pages, whole-page content replacement. The backup + tested restore script is the real safety net, not the ledger boilerplate. Do not execute without the dry-run-validated rollback in the packet.
- **Scale-up temptation:** after this ships, the next ask will be "do 100 papers." Don't — first compute unit economics from this slice (hours per shipped correction, % anchors resolvable, % snippets accepted) and fix the worst ratio before widening.

## 8. Smallest proof within 2–4 hours

One artifact: the exact-diff packet's summary table showing, for **claims 1002, 1184, and 1007**, four columns — live sentence (from snapshot), proposed sentence, resolved claim/evidence IDs, and NO-GO check result — plus a validated rollback dry-run log. That is reviewable by Duho in five minutes and proves the pipeline reaches the product's actual rows. If Duho then pastes EXECUTE, the visible proof lands minutes later: **the Dark Energy page stops saying `w ~ -0.85` and starts showing the real DES-SN5YR constraint with its citations.** One live corrected sentence is worth more than the 258 files produced so far.

## 9. Final recommended next command/brief for Hermes

Run this as the next board action, verbatim:

> **HERMES BRIEF — exact-diff publication packet (task `paper-exact-diff-<UTC>`):**
> Await Duho's paste of the APPROVE EXACT-DIFF PUBLICATION PACKET phrase (section 6 above). On approval: freeze input hashes; take the read-only DB snapshot for pages 5/19/23; dispatch Goru to run deterministic anchor→evidence-ID and claim→action resolution scripts with a machine validation.json; author whole-page diffs, backup, rollback script (dry-run it), and apply plan; dispatch Lana for one adversarial refutation pass (≥10 sampled anchors, NO-GO ledger sweep, out-of-scope-section byte-identity); fix defects once; assemble the packet with packet-specific EXECUTE and ROLLBACK phrases; update `.hermes/board/paper-prose-distillation-board.md` with actual lane states and the single line `WAITING_ON_EXECUTE: <packet path>`; stop. Timebox 4 hours. Forbidden: DB writes, migrations, deploy/restart, git writes, OpenClaw, new harvest ticks, new review layers, new approval-phrase families, more than one new output directory.
> Definition of done: Duho holds a reviewable diff for 3 pages and one EXECUTE phrase; nothing has mutated.

After the execute + render verification succeeds, the board's next planning conversation should be about industrializing (tranche 2 with the three-gate structure and scripted mechanical lane), informed by this slice's measured unit economics — not before.

---

**Bottom line:** direction right, discovery real, discipline real — but 15 hours, ~15 gates, and 258 files have not changed one word a reader sees, and the live wiki still asserts claims the board has disproven. Close the loop on three pages before anything else. The board's credibility for the whole paper-prose mission rides on turning one verified correction into visible, cited prose this week — everything else is preparation for a performance that hasn't opened yet.

FABLE_BOARD_SCRUTINY_DONE_20260702T052638Z
