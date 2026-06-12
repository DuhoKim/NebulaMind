# Galaxy Evolution v2 — Revised: Evidence-Driven Debates, No Pre-Authored D1–D10

**Author:** Kun
**Date:** 2026-05-11
**Status:** REVISES `~/.openclaw/workspace/설계_GalaxyEvolution_Research_v1.md` v3 (LOCKED 2026-05-08); supersedes §A.v3.3 (debate-to-section mapping) and §A.v3.5 (synthesis prompt)
**Scope:** Galaxy-evolution wiki page. Removes the 10 hand-authored debate claims (D1–D10, DB ids 1487–1496); replaces with evidence-driven debate detection driven by the stance jury.
**Triggered by:** Papa's 2026-05-11 directive — "the pre-authored debate claims approach is wrong... debate claims should NOT be manually designed... [they should] emerge organically from the evidence process."
**Audience:** Tori (implementer), HwaO (coordinator), Papa.

This redesign is the natural extension of the dissolution principle Papa locked across three rounds on 2026-05-08 (no compass cards → no labeled "research agenda" → no separate debates section → debates as woven prose). The next round, locked here, removes the last piece of artifice: even the *existence* of the debates is no longer hand-curated. The trust system surfaces them.

---

## 1. What the prior design got wrong

`설계_GalaxyEvolution_Research_v1.md` v3 §A.v3.3 hand-authored a mapping of 10 debate propositions (D1 mass-quenching separability, D2 z>10 mass budget, …, D10 ram-pressure vs strangulation) onto specific topical sections, and §A.v3.5 instructed Rakon to weave each one into prose with HTML-comment markers `<!-- claim:NNNN --> ... <!-- /claim:NNNN -->`.

That was the wrong unit of authorship. The model:

1. **Pre-decided which questions are debated.** A real research debate is one where the literature actually disagrees in the evidence — not one Kun thinks ought to be debated. Some of D1–D10 may have converged in the literature already; some genuinely-contested topics may not be in D1–D10. The static list locks in our 2026-05 view of the field.
2. **Created an artificial "debate-shaped" claim layer.** D1–D10 were inserted as `claim_type='debate'` rows (ids 1487–1496) with no evidence yet attached. The trust system's normal job — detecting conflict via the stance jury — was bypassed.
3. **Required updates whenever the field moved.** When Williams+2024 published a JWST UV-LF result that arguably resolves D2, the curated list would need a manual edit. The evidence pool already encodes that resolution; we just weren't reading from it.

Papa's framing: **debate emerges from the evidence, not from the curator.**

---

## 2. The replacement principle

A claim is debated **if and only if** the trust system determines so. Concretely:

> A claim is `trust_level='debated'` when it has at least one supporting evidence row AND at least one challenging evidence row, both with `quality ≥ EVIDENCE_DEBATE_QUALITY_FLOOR` (default 0.40), and the stance jury has run on both.

The synthesis layer reads this signal at synthesis time. Page renderers (and the Wiki Page Layout v1 woven-prose model) treat `trust_level='debated'` claims as the source-of-truth for which paragraphs deserve the inline debate framing.

This signal already exists. The stance jury (`drain_stance_jury_backlog`, hourly per `worker.py:41`) is the system that produces it. The mistake in the prior design was layering a parallel hand-curated track instead of using it.

### 2.1 The "debated" predicate (live SQL)

```sql
-- A claim is debated iff it has both ≥1 supporting and ≥1 challenging evidence
-- of quality ≥ floor, with stance jury settled.
SELECT c.id
  FROM claims c
  WHERE c.page_id = :page_id
    AND EXISTS (
      SELECT 1 FROM evidence e
       WHERE e.claim_id = c.id
         AND e.stance = 'supports'
         AND e.quality >= 0.40
         AND e.stance_jury_run_at IS NOT NULL
    )
    AND EXISTS (
      SELECT 1 FROM evidence e
       WHERE e.claim_id = c.id
         AND e.stance = 'challenges'
         AND e.quality >= 0.40
         AND e.stance_jury_run_at IS NOT NULL
    );
```

The `claims.trust_level` column is updated by `recalculate_trust_v2` (or its successor) whenever evidence is added or stance changes. Synthesis can either read `trust_level='debated'` directly (cheaper) or run the predicate query above (more authoritative; tolerant to trust-recalc lag).

**Recommendation:** synthesis queries `trust_level='debated'` from the column. The trust-recalc pipeline already runs after every evidence insert/stance update, so the column is the right cache.

---

## 3. What happens to D1–D10 (claim ids 1487–1496)

Three options; recommendation: **option B**.

| Option | Treatment | Pros | Cons |
|---|---|---|---|
| A — Delete | `DELETE FROM claims WHERE id BETWEEN 1487 AND 1496` | Cleanest; no residue | Loses the claim *propositions* themselves, which are scientifically real. We'd be re-creating equivalents soon enough. |
| **B — Convert to `established`** ✅ | `UPDATE claims SET claim_type='established', trust_level='unverified' WHERE id BETWEEN 1487 AND 1496` | Keeps the falsifiable propositions as regular claims. Stance jury runs on them as evidence accumulates. Some will organically become `trust_level='debated'`; others will settle to `accepted` or `consensus`. The system reaches the right answer on its own. | Requires re-evaluation. Some may have evidence already attached — need to verify those rows are still appropriate as established claims (not as debate framings). |
| C — Keep `claim_type='debate'` but only render the ones with real conflict | Filter by §2.1 predicate at synthesis time | Lightest migration | Leaves a hybrid system (some hand-authored, some evidence-driven). Confuses future contributors. |

**Locked: option B.** Convert D1–D10 to established claims. Strip them of the artificial "debate" status; let the trust system decide. The text of each proposition (e.g. "Mass-quenching is separable from environment-quenching at fixed M* and z") is a fine *claim* — it just shouldn't be presupposed as debated.

`debate_topic` and `debate_stance` columns can be nulled too:

```sql
UPDATE claims
   SET claim_type   = 'established',
       trust_level  = 'unverified',
       debate_topic = NULL,
       debate_stance = NULL,
       updated_at   = NOW()
 WHERE id BETWEEN 1487 AND 1496;
```

Then trigger `recalculate_trust_v2(page_id=57)` (galaxy-evolution) to re-classify based on whatever evidence is currently attached. Some of the 10 will likely move to `accepted` or `consensus`; others stay `unverified` until evidence arrives.

### 3.1 What about the 8 stale debate rows (ids 1479–1486) that were already deleted in the v3 design?

The v3 design (`설계_GalaxyEvolution_Research_v1.md` §A.v3.3) instructed Tori to delete claims 1479–1486 as "stale debate rows from a prior pass." That deletion still applies — those rows had outdated framing AND were also hand-authored. Don't restore them.

### 3.2 Beyond galaxy-evolution: what about the 160 debate-typed claims across 26 other pages?

Live audit (Mac Studio, 2026-05-09) showed 160 `claim_type='debate'` rows distributed across 26 pages. The same critique applies — most of those are leftovers from prior renovation passes. They need an audit:

- For each, check whether ≥1 support + ≥1 challenge evidence is already attached.
- If yes: the claim is genuinely debated — keep `claim_type='debate'`.
- If no: convert to `claim_type='established'` (option B above).

This is a separate cleanup task (§7 below). Not blocking on galaxy-evolution v2 ship.

---

## 4. Synthesis-time integration (replaces §A.v3.5 of the research doc)

### 4.1 The synthesis prompt no longer carries a hand-curated debate list

Each per-section Rakon prompt previously included a `DEBATES ASSIGNED TO THIS SECTION` block listing claim ids and supports/challenges anchor papers. That block is **removed**. Replaced with a query the synthesis pipeline runs against the DB at section-build time:

```python
def collect_debated_claims_for_section(db, page_id, section_name):
    """Returns claims on this section that are organically debated.

    A claim qualifies if:
      - it lives in this section (claims.section == section_name)
      - claim_type is currently 'established' or 'debate'
      - trust_level is 'debated'
      - it has ≥1 supports + ≥1 challenges with quality >= floor
        and stance_jury_run_at IS NOT NULL on both

    Returns [(claim_id, claim_text, [(arxiv_id, year, stance, quality), ...]), ...]
    sorted by trust_score asc (most contested first).
    """
    ...
```

The result feeds Rakon's per-section prompt as context. If the query returns zero rows for a section, the prompt has no debate block — Rakon writes purely-established prose for that section. **A section with no organic debates is correct, not a failure.**

### 4.2 Updated per-section prompt template

Replacing §A.v3.5 of the research doc:

```
You are writing one section of a graduate-research-grade astronomy wiki page
on galaxy evolution. Audience: PhD astronomers and postdocs. Tone: rigorous,
citation-rich, no pop-science framing. Voice: Nature Reviews / Annual Reviews
article — established science and contested ground appear in the same prose
flow, not in separate containers.

Section: {section_name}
Target length: {min}–{max} chars
Page: galaxy-evolution
Existing prose (reference only, you may ignore): {existing_text}
Required content beats: {section_beats}
Available high-quality evidence (use these citations): {top_15_evidence_rows}
Required established-claim count for this section: {n}

CONTESTED CLAIMS for this section (queried from the trust system at synthesis time):
{for each row in collect_debated_claims_for_section(db, page_id, section_name):}
- claim:{id} — {text}
  Supports ({n_supports}): {supports_list as Author+Year (arXiv:ID)}
  Challenges ({n_challenges}): {challenges_list as Author+Year (arXiv:ID)}

For each contested claim above (if any), weave it into the topical prose:
- State the contested proposition naturally in the topical narrative.
- Cite at least one supporting and one challenging paper inline as
  Author+Year (arXiv:ID). The supports/challenges lists above ARE the
  citations to use; do not invent new ones.
- Use phrasing like "remains debated", "competing interpretations",
  "while X argues … Y finds …". No D-numbering visible to reader.
- Wrap the contested paragraph in HTML comments
   <!-- claim:{id} -->
   {paragraph text}
   <!-- /claim:{id} -->
  on lines of their own, immediately before and after the paragraph.

If CONTESTED CLAIMS is empty for this section, write established-only prose.

(Banned phrases unchanged from v3 §A.v3.5: "scientists have discovered",
 "groundbreaking", "unlocks the secrets of", "biodiversity", "revolutionized",
 "fundamentally altering", "unprecedented", "providing insights".
 Other constraints unchanged.)
```

The structural change is small (one block replaced) but the semantics shift entirely: the curator no longer chooses which debates to present.

### 4.3 What if no claim on a page is debated yet?

Possible at v1 ship. Galaxy-evolution currently has many `claim_type='debate'` rows (per the audit) but most lack the support+challenge evidence pairs the new predicate requires. Reality on day-one: the page may render with **zero** woven-debate paragraphs, or with only 2–3.

That's correct. The page reads as Wikipedia-tradition prose — established science only — until evidence accumulates. As biblio mining and arxiv ingest add stance-jury-graded evidence, organic debates surface and on the *next* synthesis, those paragraphs get the contested framing.

This solves the v3 acceptance criterion "All 10 debates appear as woven prose" — that criterion is replaced by **"All claims that the trust system marks `trust_level='debated'` appear as woven prose"**, which is naturally satisfied (could be 0, could be 30, depends on the evidence at synthesis time).

---

## 5. Handling the just-finished Rakon synthesis (Mac Pro DONE 00:28 KST May 11)

Per the live roster, Rakon completed Galaxy Evolution synthesis at 00:28 KST May 11 — using the (now-superseded) v3 prompt with D1–D10 baked in. The output PageVersion likely contains:

- 8 topical sections per the v3 spine (correct, no change)
- HTML-comment markers `<!-- claim:1487 -->` … `<!-- /claim:1496 -->` wrapping 10 debate paragraphs (the artifact this redesign removes)
- Inline citations for the supports/challenges of each D1–D10 (still useful — the cited papers are real)

Three options for this output:

| Option | Treatment | Effort | Recommendation |
|---|---|---|---|
| **R1 — Strip markers, keep prose** ✅ | After §3 DB migration converts 1487–1496 to `established`, strip the `<!-- claim:NNNN -->` wrapper from prose around those ids only (10 markers). Keep the paragraph text. The prose stops being flagged as "debated"; the trust system will re-flag the genuinely-contested ones once stance jury catches up. | 0.25d Tori | Best — preserves Rakon's work, accepts the redesign. |
| R2 — Re-synthesize | Re-run all 8 sections through Rakon's next warm window with the §4.2 prompt. | full Rakon warm-window slot + 1d Tori | Wasteful. The prose is fine; the framing is what changed. |
| R3 — Promote as-is | Ship the v3 prose with the D1–D10 markers and migrate D1–D10 to `established` later. | trivial | Bad — leaves 10 stale markers pointing at established claims. Frontend would render them inert (since the wrapper span sets `id="claim-NNNN"` but the trust-system tooltip would say "established"), but the visual highlight from Wiki Page Layout v1 would still trigger. UI lies. |

**Locked: R1.** Strip the 10 markers in a one-shot post-processing pass before promoting to `WikiPage.content`. Pseudocode:

```python
def strip_artificial_debate_markers(content: str, claim_ids_to_strip: list[int]) -> str:
    """Remove <!-- claim:NNNN --> ... <!-- /claim:NNNN --> wrappers for the
    specified claim ids only. Keep the inner prose.
    """
    for cid in claim_ids_to_strip:
        pattern = re.compile(
            rf"<!--\s*claim:{cid}\s*-->([\s\S]*?)<!--\s*/claim:{cid}\s*-->",
            re.MULTILINE
        )
        content = pattern.sub(lambda m: m.group(1).strip(), content)
    return content
```

Apply to the new PageVersion's content with `claim_ids_to_strip = [1487, 1488, ..., 1496]` before approving. Other markers (if Rakon produced any beyond D1–D10 — unlikely but possible) stay intact.

---

## 6. Updated acceptance criteria (replaces §A.v3.6)

For galaxy-evolution v2 ship, the page is acceptable when:

- [ ] Content length 12,000–15,000 chars (unchanged)
- [ ] **Exactly 8** h2 content sections per `설계_WikiPageLayout_v1.md` §1.2 (unchanged)
- [ ] No standalone "Open Questions / Active Debates" h2 (unchanged from v3)
- [ ] No standalone "Recent Advances / Research Frontiers" h2 (unchanged from v3)
- [ ] 25–35 total claims (unchanged; counts established + organically-debated together)
- [ ] **Every `<!-- claim:NNNN -->` marker in `PageVersion.content` corresponds to a claim where `trust_level='debated'` AND ≥1 support + ≥1 challenge evidence with quality ≥ 0.40 exist.** (REPLACES v3 "exactly 10 debate markers"; verified by SQL join.)
- [ ] D1–D10 (claim ids 1487–1496) have `claim_type='established'` and have been re-classified by `recalculate_trust_v2`
- [ ] No claim has `claim_type='debate'` without backing evidence pair (verified by `SELECT … WHERE claim_type='debate' AND NOT EXISTS (predicate from §2.1)` returning empty)
- [ ] All 5 §A.5 highlights cited with arXiv IDs (unchanged)
- [ ] References ≥ 20 (unchanged)
- [ ] No URLs / dataset links in body (unchanged)
- [ ] No banned pop-science phrases (unchanged)
- [ ] No D-numbering visible to readers (unchanged)
- [ ] Provenance chip exactly `🤖 Synthesized by 671B model` (unchanged)
- [ ] Independent reader test: a senior researcher recognizes contested ground from prose alone (unchanged)
- [ ] **NEW:** if the page renders zero contested paragraphs at v2 ship, that is acceptable — the prose is Wikipedia-tradition established narrative; debates surface as the trust system catches up.

---

## 7. Tori implementation handoff

Sequenced to land in one session:

1. **DB migration (0.25d Tori).** Run §3 SQL to flip claim ids 1487–1496 to `claim_type='established'`. Verify with `SELECT id, claim_type, trust_level FROM claims WHERE id BETWEEN 1487 AND 1496`.
2. **Trigger trust recalculation (5 min).** Call `recalculate_trust_v2.delay(page_id=57)`. Wait for hourly stance-jury drain (`crontab(minute=0)`) to settle stances on attached evidence.
3. **Strip artificial markers (0.1d Tori).** Apply §5 R1 `strip_artificial_debate_markers` to the new PageVersion's content (the one Rakon produced at 00:28 KST May 11). Save as a new PageVersion with editor_agent_id of the post-processor.
4. **Walk §6 acceptance scorecard (Kun, 1.5h).** Verify the SQL predicate is empty for `claim_type='debate' WITHOUT backing pair`. Spot-check that any remaining `<!-- claim:NNNN -->` markers in the page correspond to genuinely-debated claims.
5. **Promote to live (0.1d Tori).** `UPDATE wiki_pages SET content = (latest accepted PageVersion.content) WHERE slug='galaxy-evolution'`. Trigger `update_coverage_map_daily`.
6. **Cross-page audit task (deferred, 0.5d Tori, later).** For all 26 pages with `claim_type='debate'` rows that lack the §2.1 predicate, run the same conversion — flip to `established`, recalc trust. Run after galaxy-evolution v2 ships and stabilizes.

Total for galaxy-evolution v2 ship: **~0.5d Tori + 1.5h Kun.** No Rakon time required (re-using the existing synthesis output).

---

## 8. Platoon Assignment

| Step | Volume | Owner | Model | Why |
|---|---:|---|---|---|
| §3 DB migration (UPDATE 10 rows) | 1 invocation | **Tori** | claude-sonnet-4-6 | Pure SQL; Tori writes and verifies. No LLM platoon member needed. |
| §3 `recalculate_trust_v2.delay(page_id=57)` | 1 invocation | — | (no model — internal trust math) | Pure Python computation over evidence rows. |
| Hourly stance-jury drain on attached evidence (settles supports/challenges + sets `stance_jury_run_at`) | up to ~50 evidence rows on page 57 | **Buddle** | `deepseek-r1:32b` (Mac Pro) | Existing stance-jury model per roster; already running `drain_stance_jury_backlog` continuously. The §3 trust-recalc piggybacks on Buddle's existing queue. |
| §5 `strip_artificial_debate_markers` post-processor | 1 invocation | **Tori** | claude-sonnet-4-6 | String regex; Tori writes the migration script + invokes. No platoon LLM. |
| §6 acceptance review | 1 invocation | **Kun** | claude-opus-4-7 | Spot-checks; SQL predicate verification; voice review. Self-assigned. |
| §7.6 cross-page audit (deferred) | 160 claims | **Tori** | claude-sonnet-4-6 | Scripted SQL; verify-and-flip pattern. No LLM step. |
| Future per-section synthesis re-runs (when evidence adds debates organically) | per page renovation | **Rakon** | `deepseek-r1:671b` (Mac Pro warm window) | Same as v3 §A.v3.5, just with the §4.2 prompt update. Scheduled-warm only; not real-time. |

Notably: this redesign needs **zero LLM work for the immediate galaxy-evolution v2 ship**. The Rakon synthesis is already done; we're post-processing its output and migrating DB. Buddle's existing stance-jury work is the only ongoing platoon load, and that's pre-scheduled.

**Escalation paths:** none for v2 ship. Future per-section re-runs use the same Rakon escalation as v3 (warm-window batch).

## 9. Roster check (2026-05-11 00:31 KST snapshot)

Read against `~/.openclaw/workspace/memory/platoon-roster.md`.

| Member | Roster status | Roster job | This doc's ask | Verdict |
|---|---|---|---|---|
| Rakon | ✅ DONE — standby | Galaxy Evolution synthesis complete | None for this v2 ship; future per-section re-runs only | **Compatible.** |
| Buddle | 🔄 ACTIVE | Stance jury drain | Stance settling on page 57 evidence — already in Buddle's normal queue | **Compatible.** No additional load; the existing hourly `drain_stance_jury_backlog` task picks it up. |
| Tori | 🔄 ACTIVE | Tasks 14 & 15 (evidence linking + stance jury on 5 pages) | DB migration (~0.25d), marker strip (~0.1d), promotion (~0.1d) | **Compatible-but-tight.** Tori is actively working. The asks here total ~0.5d and are SQL/regex tasks Tori can interleave. If Tori is saturated when this ships, defer cross-page audit (§7.6) — that's already deferred. |
| Mima, Blanc, Nutty, Tera, Takji, Groq, Gemini | various | various | None | **Not used.** |

**Net:** all assignments compatible. The redesign is deliberately light on platoon load — the heavy synthesis is already done, and the cleanup work is mostly SQL.

---

## 10. Open questions for Papa

1. **Cross-page audit timing (§7.6).** Run the 26-page audit immediately after galaxy-evolution v2 ships, OR wait until the evidence-driven debate detection has been live and observed for a week? Recommendation: wait one week. Galaxy-evolution v2 is the proof-of-concept; let it stabilize before sweeping the rest.
2. **Re-classification of D1–D10 evidence.** Some of D1–D10 may already have evidence rows attached from biblio mining (the audit found 160 debate-typed claims and 11k+ evidence rows). When converting those 10 to `established`, the existing evidence stays attached — if the stance jury has already run on it, recalculate_trust_v2 will immediately re-classify some as `debated` organically. **This is the desired outcome.** Recommendation: proceed without preview — the system reaching the right answer on its own is exactly the point.
3. **Acceptance threshold tuning.** `EVIDENCE_DEBATE_QUALITY_FLOOR = 0.40` matches the existing `EVIDENCE_MIN_QUALITY_FOR_ACCEPTED`. Should the debate floor be higher (e.g. 0.50) so we don't surface debates from low-quality conflicts? Recommendation: keep at 0.40 for v1 (consistent with existing trust system); raise only if signal noise becomes a problem.

---

## 11. References

- Prior design (now superseded): `~/.openclaw/workspace/설계_GalaxyEvolution_Research_v1.md` v3 §A.v3.3 + §A.v3.5
- Layout (unchanged): `~/.openclaw/agents/kun/workspace/설계_WikiPageLayout_v1.md` (LOCKED 2026-05-08)
- Rejection of prior PageVersion: `~/.openclaw/agents/kun/workspace/리뷰_GalaxyEvolution_PV2597_v1.md`
- Code: `backend/app/agent_loop/tasks.py:drain_stance_jury_backlog`, `recalculate_trust_v2`
- Trust mechanics: `~/.openclaw/agents/kun/workspace/설계_신뢰도_메커니즘_v1.md` (Phase 1)
- Live roster: `~/.openclaw/workspace/memory/platoon-roster.md` (read at 2026-05-11 00:31 KST snapshot)
- Live audit (Mac Studio prod, 2026-05-09): 160 `claim_type='debate'` rows across 26 pages, 11,346 evidence rows total

— 🔬 Kun
