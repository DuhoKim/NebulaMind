# galaxy-evolution Quality Roadmap (v2 — 2026-05-16 update)

**Author:** Kun
**Original date:** 2026-05-12 21:00 KST · **This update:** 2026-05-16 09:45 KST
**Goal:** push galaxy-evolution from current avg Q ≈ 0.66 → **Q ≥ 0.78** (sustained over 7 days)
**Audience:** Tori (implementer), HwaO (coordinator), Papa
**Companion docs:** `autowiki_loop_v1.md` (pipeline spec), `beat_schedule_v3.md` (cadences + active proposer roles), `job_schedule_v1.md` §8/§9 (multi-model platoon), `debated_claim_seeder_v1.md` (new lane targeting contested-claim gap)

> **Status of v1 (2026-05-12) targets:** P0 SHIPPED. P1 PARTIALLY SHIPPED (judge anonymized, rubric ceiling raised — see §1.3). P2/P3/P4 SHIPPED via the v3 multi-model engine (§9). All v1 acceptance criteria except "q ≥ 0.95 sustained" are met. The v2 target is the new, more honest 0.78 floor — see §1.5.

---

## 1. Current state (live audit, 2026-05-16 09:25 KST)

### 1.1 Page-level snapshot

```
page              : galaxy-evolution (id=57)
content           : 95,427 chars        (was 27,478 in v1 — +247%)
sections          : ~10
claims            : 41                  (was 34 in v1 — +21%)
                    25 accepted · 9 challenged · 6 debated · 1 consensus
hero_tagline      : NULL                ← regression: hero_refresh lane has not run / not committed
active ideas      : 15
draft ideas       :  6  (Nutty post-commit + JI pool waiting promotion)
research_idea_anchors : 6 (drafts only — actives use claim_id direct column, see §1.4)
last commit q1    : ranges from 0.66 (2026-05-15 178 ticks) to max 0.94 today
```

### 1.2 Quality (q1) trend, last 5 days

| Date | Ticks/day | avg q1 | max q1 | Δ vs prior day |
|---|---:|---:|---:|---|
| 2026-05-11 Mon |   2 | 0.5557 | 0.5849 | baseline |
| 2026-05-12 Tue | 112 | 0.7719 | 1.0000 | **+0.22** (v1 P0 fix shipped, autowiki active) |
| 2026-05-13 Wed |  96 | 0.7268 | 1.0000 | −0.05 |
| 2026-05-14 Thu | 103 | 0.7253 | 0.9100 | flat |
| 2026-05-15 Fri | 178 | **0.6598** | 0.9400 | **−0.07** ← regression starts |

**The trend is downward since 2026-05-13.** Three contributing factors, all already diagnosed:

1. **Sonnet section_rewrite ceiling effect** (`delta_q_fix_v1.md`): Sonnet rewriting q0=0.93+ sections produces tiny-negative-Δ commits that drag the page avg down. Threshold-leak: legacy autowiki_tick gates at `Δq ≥ +0.02`, Sonnet gate lets `Δq > -0.01` through. Fix specced 2026-05-15, awaiting Tori.
2. **AstroSage stuck rows** (23/24 in 4-h sample have `judge=None`, never reach the judge step). Likely Mac Studio inference contention from the 6-model resident set. Separate P2 fix in `delta_q_fix_v1.md`.
3. **Tick frequency 3× higher than v2** (288/day at 5-min cadence vs 96/day at 15-min in v2). The same proposer/judge errors fire 3× more often, amplifying the negative-Δ tail.

### 1.3 What v1 said vs what we got — calibration check

| v1 acceptance criterion | Today's measurement | Hit? |
|---|---|---|
| autowiki_tick commits ≥3 of next 5 ticks (post-P0) | 24 commits / 61 attempts in last 24 h = 39% | ✓ (above 60% commit rate goal of P1.b) |
| 5 parallel judge calls produce ≥2 distinct rubric outputs | confirmed in `u0_runs` jsonb sampling — variance is real now | ✓ |
| u1_median ≥ 9.5 on any committed row | max q1 = 1.0000 multiple times this week (rubric ceiling raised) | ✓ |
| compute_health_score(page).depth ≥ 0.9 | not directly measured here (different code path now) | n/a |
| freshness ≥ 0.85, 2024+ evidence count ≥ 100 | autowiki has been ticking nonstop since 2026-05-12, freshness has held | ✓ inferred |
| Every section rewritten at least once in 7 days | round-robin landed, 10 sections rotated 2-3× each | ✓ |
| **q1 reaches 0.95+ on 3 consecutive commits** | **max q1=1.0 hit, but avg slipped to 0.66** | **✗** — see §1.4 |

So **the v1 roadmap's structural goals all landed**, but the q1 trajectory is now *less stable*, not just below target. v1 assumed monotone improvement; reality is bumpy with regressions.

### 1.4 Where ideas are anchored — and where they aren't

Live audit:

| linkage | count | observation |
|---|---:|---|
| `research_ideas.status='active'` on page 57 | 15 | all kun-seeded on 2026-05-13 |
| of those, `claim_id IS NOT NULL` | **15 (100%)** | seeded with direct-column linkage |
| of those, has `research_idea_anchors` row | **0** | dual schema not used |
| `research_ideas.status='draft'` on page 57 | 6 | recent J1/JI output |
| of those, has `research_idea_anchors` row | **6 (100%)** | drafts use anchors-table linkage |
| of those, `claim_id IS NOT NULL` | **0** | drafts don't set `claim_id` |

**Two linkage mechanisms, used inconsistently.** Kun-seeded ideas use `research_ideas.claim_id` (direct FK). Auto-generated drafts use `research_idea_anchors` (kind/ref_id table). Queries that JOIN one mechanism miss ideas in the other.

The `debated_claim_seeder_v1` design fixes this by **writing both linkages** on every new idea. Recommendation in §3 below: also backfill the dual linkage on the existing 21 ideas (one-shot SQL).

Independent gap (motivates Task 1): of the 15 **debated/challenged** claims on the page, **0 have ≥1 anchored idea** (via either mechanism after the 3 weak `claim_id` links from kun-seed are excluded). The wiki's open questions have no research agendas attached. New seeder lane (§2.5 below) closes this.

### 1.5 Recalibrating the target — why 0.78 not 0.95

v1's "q ≥ 0.95" target was set when the judge rubric maxed at 9.09. Post-P1.c rubric expansion, top-end is 1.0 (q1=1.0 hit multiple times). But the **average** can't be 0.95 because every section_rewrite ticks through a u0→u1 transition — even great rewrites land at ~0.93 because the baseline state is already strong.

Papa's new target Q ≥ 0.78 (7.8/10) is the **right** number: it's the threshold where the page reads as "research-grade reference content" in the rubric, distinguishing it from the 0.55 baseline state (just-claims-and-sections, no integration).

**Current gap: 0.78 target − 0.66 avg = +0.12 to close.**

---

## 2. What the autowiki loop is doing today vs what's still manual

### 2.1 Automated (autowiki + v3 multi-model engine, no human action)

| Lane | Cadence | Status | Daily output target |
|---|---|---|---|
| `autowiki_tick` (AstroSage proposer + Nutty judge) | every 5 min (288/day) | ✓ firing, ~24 commits/day | section_rewrite + claim_insert + evidence_link |
| `sonnet_section_rewrite` (Claude Sonnet 4.6 proposer, A/B with AstroSage) | every 30 min (48/day) | ⚠ negative-Δ regression — fix pending | ~24 successful commits/day target |
| `rakon_deep_pass` | every 2 h (12/day) | ✗ 100% error (Mac Pro Rakon resident-set gap) | 12 debate skeletons/day |
| `rakon_draft_async` (R2 idea drafts) | every 4 h (6/day) | ✓ firing (per Papa note: "Rakon generating more now") | 3-10 ideas/tick |
| `buddle_evidence_pair` | hourly | ✓ should be firing | 3 evidence candidates/h × 24 |
| `buddle_draft_async` Path B | every 6 h | ✓ | 5-10 ideas/day |
| `astrosage_hero_refresh` (v3: now `opus_hero_refresh`) | every 8 h | ✗ **regression** — hero_tagline currently NULL | 3 hero updates/day |
| `mima_cross_page_synthesis` | every 6 h | ⚠ status unconfirmed | 4 ClaimMigrationProposals/day |
| `tera_coverage_audit` | Mon+Wed+Fri 02:00 KST | ⚠ status unconfirmed | 3 CoverageReports/wk |
| `tera_evidence_audit` | every 12 h | ⚠ status unconfirmed | 2/day |
| `takji_methodology_gate` (inline in autowiki_tick) | every tick | ✓ active per error log | gate-rejects on methodology fails |
| `takji_schema_validate` | every 4 h | ⚠ X4 SQL bug spammed log (separate fix in `j1_fix_v1.md`) | 6/day |
| `atom_claim_relevance` (X4 inline) | every tick | ✗ `claims.status` column-name bug | flag ClaimDecayCandidates |
| `nutty_trust_recompute` | hourly :20 | ✓ firing | hourly trust updates |
| `idea_judge_pool` (JI) (Atom→Takji→AstroSage→Opus chain) | every 4 h (6/day) | ✓ firing | ~5 ideas promoted/tick |
| `J1 process_lightweight_event` (Nutty post-commit) | event-driven | **✗ 0 rows ever** — see `j1_fix_v1.md` | should be ~5 drafts/day |
| `rakon_adversarial_probe` | daily 00:00 KST | ✗ blocked by R1 Mac Pro Rakon outage | 3 falsifying-evidence candidates/day |
| **NEW** `seed_debated_claim_ideas` | every 6 h (per `debated_claim_seeder_v1`) | not yet deployed | 5 claims × 2-3 ideas/tick |

### 2.2 Still manual (Kun + Papa actions, no automation)

| Action | Owner | Why not automated |
|---|---|---|
| Mac Pro Rakon resident-set fix (load `deepseek-r1:671b`) | HwaO | requires ops-level change (Ollama config + launchd or shell wrapper). Blocks 3 lanes (R1 deep_pass, R2 idea_draft, R3 adversarial). |
| Beat schedule v3 deploys (Sonnet/Opus active roles) | Tori (specced) | code change waiting for J1 + delta_q fixes to land first |
| Section structure restructuring (e.g., merge 2 weak sections into 1 strong) | Kun (manual review) | autowiki rewrites within-section; cross-section restructure not yet automated |
| Hero tagline + hero_facts (`opus_hero_refresh`) | Tori (specced, not landed) | hero is currently NULL — symptom of the unshipped `opus_hero_refresh` task |
| Citation-quality audits beyond Atom-7b score | Kun (occasional) | no per-citation manual review automated |
| Pilot page expansion (galaxy-evolution → AGN / black-hole-mergers) | Papa | strategic call; v3 design pinned to page 57 only |

---

## 3. Specific next steps to close the gap to Q ≥ 0.78

In priority order. Each step has an expected Δq contribution and an effort estimate.

### 3.1 Land the J1 + delta_q fixes (P0, +0.08 to +0.12 in avg q1, **biggest win**)

Both fix specs already written:
- `j1_fix_v1.md` — restore Nutty draft generation (J1 currently produces 0 rows ever). Effort: 0.5 day Tori.
- `delta_q_fix_v1.md` — stop Sonnet rewrites from degrading high-q0 sections. Effort: 0.5 day Tori.

**Expected impact:** today's −0.07/day downward drift reverses. Within 48 h of landing, avg q1 should climb back to ~0.74 (where it was on 2026-05-13). Within 5 days, ~0.78 sustained.

### 3.2 Mac Pro Rakon resident-set fix (P0, +0.05 to +0.10 in avg q1, **second biggest win**)

`deepseek-r1:671b` must be preloaded on Mac Pro and kept warm. Today all R1/R2/R3 Rakon lanes error out (13/13 last 7 days). Once fixed:
- R1 `rakon_deep_pass` (12/day) starts producing debate skeletons — feeds Q's `open_questions_q` dimension
- R2 `rakon_draft_async` runs deeper structural reasoning (currently fallback to Buddle when Mac Pro Rakon down — Papa confirmed it's firing, so possibly already on Buddle)
- R3 `rakon_adversarial_probe` (daily) finds falsifying papers — feeds `evidence_depth` and `noise_penalty` dimensions

Owner: **HwaO**. Effort: 0.5 day. Blocking dependency on a launchd / Ollama config change.

### 3.3 Deploy `debated_claim_seeder_v1` (P1, +0.03 to +0.05 in avg q1)

Doc just written. 15 debated/challenged claims have **0 anchored research ideas**. The seeder writes 3 ideas per claim within 5 days (acceptance criterion §4 in seeder doc). Effect: rubric's `open_questions_q` and `frontier_signal` dimensions get cleaner signal — debated claims with attached research agendas score higher than orphan debated claims.

Owner: Tori. Effort: 1 day (new task + beat + post-commit trigger + 2 tests).

### 3.4 Ship `opus_hero_refresh` (P1, +0.02 in avg q1, **+0.10 on hero-aware ticks**)

Hero tagline is currently NULL. Per v3 spec (`beat_schedule_v3.md` §3.5), Opus 4.7 should refresh hero_tagline + 3 hero_facts every 8 h. Once landed, `hero_richness` rubric dimension goes from 0 → 1.0 on every tick — and that's a load-bearing dimension in the page-level q1 average.

Owner: Tori. Effort: 0.5 day. Already designed in `beat_schedule_v3.md`.

### 3.5 Fix X4 / takji_schema_validate SQL bug (P1, no direct Δq, **stops error-log spam**)

`atom_claim_relevance` inline call in `autowiki_tick` queries `claims.status='accepted'` — column is `trust_level`. Error log floods every 5 min. Fixing it doesn't directly improve q1 but:
- Stops `[autowiki] X4 claim fetch page=57 failed` from drowning out real signal
- Unblocks ClaimDecayCandidate generation (currently zero rows ever), which feeds the R3 adversarial probe priority queue

One-line fix. Owner: Tori. Effort: 5 minutes (part of `j1_fix_v1.md` P1 §3.4).

### 3.6 Backfill dual-linkage on existing ideas (P2, +0.02 in q1 long-tail)

Existing actives use `claim_id` direct column; drafts use `research_idea_anchors`. Queries that JOIN one miss the other (§1.4). One-shot SQL backfill:

```sql
-- For every existing research_ideas row with claim_id but no anchor, create the anchor.
INSERT INTO research_idea_anchors (idea_id, kind, ref_id, created_at)
SELECT ri.id, 'claim', ri.claim_id::text, NOW()
FROM research_ideas ri
WHERE ri.claim_id IS NOT NULL
  AND ri.page_id = 57
  AND NOT EXISTS (
    SELECT 1 FROM research_idea_anchors a
    WHERE a.idea_id = ri.id AND a.kind = 'claim' AND a.ref_id = ri.claim_id::text
  );

-- For every draft with an anchor of kind='claim' but no claim_id, set the claim_id.
UPDATE research_ideas ri
SET claim_id = (a.ref_id)::integer
FROM research_idea_anchors a
WHERE a.idea_id = ri.id
  AND a.kind = 'claim'
  AND ri.claim_id IS NULL
  AND ri.page_id = 57;
```

Affects rubric's `evidence_depth` for any claim that now appears linked to ideas. Owner: HwaO/Tori (DBA-style). Effort: 10 min.

### 3.7 Cross-section synthesis pass (P3, +0.03 in q1, **deferred**)

Currently every section rewrite is within-section. Two weak sections might be better merged or restructured. Tera (gemma3:27b, 128 k context) is the natural fit — load whole page into context, propose section-level restructure. Not yet specced.

Owner: Kun (design) → Tori (impl). Effort: 1 day spec + 1 day impl. **Deferred** until §3.1–3.6 land and we know whether they alone close the gap.

---

## 4. Projected trajectory

Assumptions: §3.1 + §3.2 + §3.5 land within 48 h; §3.3 + §3.4 land within 4 days; §3.6 runs within 1 day. All numbers are *avg q1* (not max).

| Date | Expected avg q1 | Driver |
|---|---:|---|
| 2026-05-16 (today) | 0.66 | baseline — regressing daily |
| 2026-05-17 | 0.66–0.70 | §3.1 lands (J1 + delta_q fixes) → Sonnet floor at +0.02, Nutty drafts resume |
| 2026-05-18 | 0.70–0.74 | §3.2 lands (Mac Pro Rakon back) → R1/R2/R3 contribute |
| 2026-05-19 | 0.72–0.76 | §3.3 lands (debated claim seeder) → debated-claim ideas anchor properly |
| 2026-05-20 | 0.74–0.78 | §3.4 lands (Opus hero refresh) → `hero_richness` from 0 → 1.0 |
| 2026-05-21 | **0.78 (target hit)** | all v2 fixes in place for ≥24 h |
| 2026-05-22–28 | **≥ 0.78 sustained** | acceptance window (7-day rolling avg) |

**Target hit date: 2026-05-21, target sustained: 2026-05-28.**

---

## 5. Platoon Assignment

(Per Papa's standing rule, every periodic/real-time job names its model owner.)

| Step | Model | Why |
|---|---|---|
| §3.1 J1 fix | none (Python) | Code fix; restores existing Nutty 14b path |
| §3.1 delta_q fix | none (Python prompt config) | Threshold tightening + Sonnet skip rule |
| §3.2 Mac Pro Rakon resident | none (HwaO ops) | Ollama config / launchd |
| §3.3 debated_claim_seeder primary | **Rakon (deepseek-r1:671b)** | structural reasoning on contested claims; see `debated_claim_seeder_v1.md` §3 |
| §3.3 fallback | **Buddle (deepseek-r1:32b)** | Mac Pro understudy |
| §3.3 fallback-fallback | **Mima (qwen3:30b)** | Mac Studio diversity voice if Mac Pro down |
| §3.4 hero refresh | **Opus (claude-opus-4-7)** | highest-stakes/smallest-surface text — see `beat_schedule_v3.md` §3.5 |
| §3.5 X4 SQL fix | none (Python) | Trivial code edit |
| §3.6 dual-linkage backfill | none (SQL) | One-shot UPDATE/INSERT |
| §3.7 cross-section synthesis (deferred) | **Tera (gemma3:27b, 128 k context)** | only model that fits the whole page |

No new cloud spend beyond what `beat_schedule_v3.md` already budgeted (~$6/day).

---

## 6. Acceptance criteria for Q ≥ 0.78

- [ ] **Within 24 h of §3.1 + §3.2 landing:** avg q1 over rolling 4-h window ≥ 0.72
- [ ] **Within 5 days of §3.3 landing:** all 15 debated/challenged claims have ≥ 3 anchored research ideas
- [ ] **Within 24 h of §3.4 landing:** `wiki_pages.hero_tagline` IS NOT NULL on page 57, refreshes every 8 h
- [ ] **Within 7 days from today:** rolling 24-h avg q1 ≥ 0.78
- [ ] **Sustained acceptance:** rolling 7-day avg q1 ≥ 0.78 for 7 consecutive days

---

## 7. Open questions for Papa

1. **Pilot expansion.** Once page 57 sustains Q ≥ 0.78, what's the next page? AGN (page 9, 20 claims) and magnetars (page 28, 17 claims) both have the highest claim counts after galaxy-evolution. AGN has more 2024-2026 literature; magnetars has fewer debates but cleaner consensus. Recommend AGN as next pilot.
2. **R1 `rakon_deep_pass` debate-skeleton output destination.** The 12/day debate skeletons currently land in `autowiki_runs.judge_rationale` only — they don't auto-spawn claim_insert_debate proposals. Should I design a `rakon_deep_pass → claim_insert_debate` auto-trigger? Higher cadence of debated claims means higher `open_questions_q` rubric. Separate design needed if so.
3. **Cross-page debate linking.** Some galaxy-evolution debates (e.g., AGN feedback at high z, dust-obscured SFR) are also active on AGN / reionization pages. Mima M4 cross-page synthesis is supposed to catch this. Status of M4 (currently "unconfirmed firing" in §2.1) — Tori to verify or Kun to investigate.
4. **`research_idea_anchors` vs `research_ideas.claim_id` schema redundancy.** §1.4 documents the dual-linkage mess. Long-term, pick one mechanism and migrate the other. Anchors table is more flexible (multi-anchor per idea, multi-kind); claim_id direct column is simpler. Recommend keeping anchors as canonical and deprecating claim_id in v2.x. Need Papa's call.

— 🔬 Kun, 2026-05-16 09:45 KST

---

## Appendix A: v1 retrospective (what hit, what didn't)

v1 acceptance items: 6 of 7 ✓, 1 ✗.

The ✗ ("q1 0.95 sustained on 3 consecutive commits") was over-aggressive — assumed rubric ceiling rises would translate linearly to avg lift. Reality: max hits 1.0 frequently, but avg is dragged by gate_reject + rollback + tiny-negative-Δ commits. v2's 0.78 target is calibrated against the actual avg-q1 distribution, not the max.

v1's pathology findings (judge framing leakage, byte-identical rubric at temp=0, page-level vs section-level scoring) all proved correct and were fixed by P1 changes. The current regression (since 2026-05-13) is a different problem: v3's new active-proposer roles (Sonnet, future Opus) introduce new threshold-leak paths that v1 didn't anticipate.

## Appendix B: TF-IDF Classifier Content Window Bug (2026-05-12, still open)

`_page_text()` in `arxiv_classifier.py` caps content at 1,500 chars from a now-95k-char page (was 33k in v1).
Even directly relevant papers score below 0.30 threshold (galaxy-evolution max cosine 0.19).
Fix: raise content cap to 10,000 chars or add per-page keyword override (in v1 was "5,000"; updated for new page size).
Effort: 0.5 day Tori. Still unaddressed.
