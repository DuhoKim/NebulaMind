FABLE_HARD_BURN_H4_WIKI_DRYRUN_20260711T035354Z

# Wiki/DB integration dry-run plan — P4 claim/evidence candidates (13/13)

**OFFLINE PLAN — NOTHING EXECUTED.** No DB connection was opened, no API called, no server started. Schema knowledge comes exclusively from read-only working-tree files (hashes in `H4_RECEIPT.md`). This plan makes the gated wiki/DB pass (rollup follow-up item 4) a mechanical execution; the gate approval itself is the publish decision.

Input basis: `p4-derived-claims/CLAIM_EVIDENCE_CANDIDATES.md` (13 candidates), pinned sha256 `1c8d9a7d28566a19a957cac754a7b8c6c5981a3ad445eb3d3f9daacbd49f8b39` — **recomputed, MATCH**. `wiki_schema.md` current working-tree sha256 `d1c04e1fcf1e9b412712d07407c42fccffcf12b5a2fc2eced59dba888594b5dd` — identical to the hash P4 recorded, so P4's shaping assumptions still hold.

---

## Part A — Preamble: ground truth, placeholder mapping, execution order

### A1. Real DB shape (from `backend/app/models/claim.py`, `backend/app/models/page.py`, `backend/app/models/external.py`)

Integration target is the **claims layer**, not page prose:

- `claims` (model `Claim`): `id` PK · `page_id` FK→`wiki_pages.id` (required) · `section` String(100), default `"Overview"` · `order_idx` int, default 0 · `connector` String(50) NULL · `text` Text (required) · `trust_level` String(20), default `"unverified"` · `claim_type` String(20), default `"established"` · `rewrite_status` String(30) NULL (visibility: `visible_claim_filter()` in `routers/claims.py` hides only `rewrite_status == "parent_replaced"`) · `debate_topic`/`debate_stance` NULL · `created_by_agent_id` FK NULL · `trust_score` float default 0.0 · timestamps server-side · human-override fields NULL.
- `evidence` (model `Evidence`): `id` PK · `claim_id` FK (required) · `title` Text (required) · `arxiv_id`/`doi`/`url`/`authors`/`year`/`summary`/`abstract`/`ads_bibcode`/`s2_paper_id`/`journal_ref` all nullable · `stance` String(20) default `"supports"` · `quality` float default 0.50 · `status` String(20) default `"active"` · `source_channel` String(40) default `"manual"` · `arxiv_verified`/`peer_reviewed` bool default false · jury fields (`relevance`,`entailment`,`rigor`,`confidence`, `consensus_*`) NULL at insert.
- `external_source_log` (model `ExternalSourceLog`): `source` String(20) · `external_id` String(100) · nullable FKs `page_id`/`claim_id`/`evidence_id` · `decision` String(40) · `notes` Text. **This existing table is the idempotency ledger for the pass** (§A5).
- `wiki_pages`: `slug` unique+indexed → page-id resolution key. `WikiPage.content` has a canonicalizer event guard — **not triggered by this pass** (we never set `content`).
- Trust recalc (`services/trust_calculation.py` + `config.py`): `TS = 0.45·E + 0.35·V + 0.10·T + 0.80·H`, `E = tanh((ΣQ_sup − ΣQ_chal)/1.5)`; buckets `accepted ≥ 0.30`, `challenged ≤ −0.30`, `consensus ≥ 0.75` (needs ≥3 supports); semantic caps from `debate_stance` on established claims: `"model_bounded"` caps accepted/consensus → `"reported"`, `"mixed_debated"` → `"debated"` (pinned by working-tree `backend/tests/test_trust_debate_stance_caps.py`).

### A2. P4 `wiki_shape` placeholder → real mechanism mapping

| P4 placeholder | Real mechanism at gate time |
|---|---|
| `page_id: OFFLINE_PLACEHOLDER` | `SELECT id FROM wiki_pages WHERE slug = :bare_slug` — bare slug = proposed slug minus `/wiki/` prefix (router `GET /api/pages/{slug}/claims` matches `WikiPage.slug == slug`, i.e. bare). Require exactly 1 row; verify `category = 'galaxy'`; else fail closed for that candidate. |
| `claim_id: OFFLINE_PLACEHOLDER` | DB-assigned at insert (`db.flush()` → `new_claim.id`), recorded in the gate-run receipt. |
| `evidence_ids: OFFLINE_PLACEHOLDER` | DB-assigned; this plan produces exactly **one** evidence row per candidate (one independent source — keeps `evidence_count` epistemically honest; multiple quoted spans fold into `summary`). |
| `page_version_fk: OFFLINE_PLACEHOLDER` | **No such column exists.** `claims` is page-scoped, not version-scoped; `page_versions` rows are only created by content edits, which this pass does not perform. Resolution: record `wiki_pages.updated_at` and `MAX(page_versions.version_num)` per target page in the gate-run receipt as the page-state snapshot. Flagged in §C1. |
| `publish_state: OFFLINE_PLACEHOLDER` | **No draft state exists for claims.** An inserted claim is immediately live in `GET /api/pages/{slug}/claims` (only `rewrite_status='parent_replaced'` is hidden). Publish state = composite: `claims.trust_level='unverified'` + `claims.rewrite_status=NULL` (visible) + `evidence.status='active'` + ledger `decision='inserted'`. See §A6. |
| `category: galaxy` | Verified against `wiki_pages.category` at gate time (all 4 target topics are `galaxy` per `wiki_schema.md` category table and are in the coverage map's COVERED list). |
| `proposed_section` | `claims.section` value; verify against the page's real section inventory at gate time (§A4 step G2). |
| `see_also: [...]` | **Not a claims-layer field** — page-content `## See Also` / `PageRelation` graph concern. Deferred to a separate content-editing pass; carried in this plan per candidate as deferred metadata. Flagged in §C2. |
| `references: [S1]/[S2]` | The candidate's single `evidence` row (title/authors/year/journal_ref per §A3). `DOI: OFFLINE_PLACEHOLDER` maps to `doi = NULL` — **the literal placeholder string must never be written into `evidence.doi`** (§C3). |

### A3. Shared payload templates (exact values; per-candidate overrides in Part B)

**T-CLAIM** — one `claims` row per candidate:

```yaml
page_id:        <resolved at gate, §A2>          # required FK
section:        <candidate proposed_section>     # String(100); ≤ 20 chars for all 13 → fits
order_idx:      <COUNT(claims WHERE page_id=:pid) at insert>  # append-at-end; matches autowiki
                # convention (autowiki/tasks.py:1450 `order_idx=len(claims)`,
                # deep_synthesis.py:207 count()); keep a running counter when inserting
                # several candidates into the same page in one gate run
connector:      NULL
text:           <candidate claim_text, byte-verbatim from CLAIM_EVIDENCE_CANDIDATES.md>
trust_level:    "unverified"                     # schema default; honest entry state
claim_type:     "established"                    # scoped single-stance statements, not pro/con debate pairs
rewrite_status: NULL                             # visible
debate_topic:   NULL
debate_stance:  "model_bounded"                  # semantic cap: display can never exceed "reported"
                # even if future votes/evidence push TS ≥ 0.30 — matches association-only,
                # proxy-bounded scope; pinned by test_trust_debate_stance_caps.py.
                # Fallback: if the deployed backend predates the cap logic, set NULL and
                # record "cap unavailable" in the gate receipt (preflight G0 checks this).
created_by_agent_id: NULL                        # matches autowiki convention; provenance via ledger
# trust_score/timestamps/human-override fields: leave to defaults (0.0 / server / NULL)
```

**T-EVID** — one `evidence` row per candidate:

```yaml
claim_id:       <flushed claim id>
arxiv_id:       NULL          # unpublished internal manuscript — no identifier fabrication
doi:            NULL          # NEVER write "OFFLINE_PLACEHOLDER"
url:            NULL          # repo file paths are not URLs; provenance lives in summary/journal_ref
title:          <S1|S2 full manuscript title, §A3.1>
authors:        "NebulaMind Research Autopilot"
year:           2026
summary:        <verbatim quoted evidence span(s) + snapshot line anchors + manifest ids
                 + custody run family; per candidate in Part B>
stance:         "supports"
quality:        0.50          # column default; deliberately NOT inflated for self-produced sources
journal_ref:    <"Offline cycle-5 candidate manuscript (unpublished); custody run <family>"> # ≤500 ✓
peer_reviewed:  false
arxiv_verified: false
status:         "active"
source_channel: "p4_offline_candidate"   # 20 chars ≤ String(40) ✓; free-form column (no enum
                                         # constraint found); queryable provenance tag for all rows
                                         # of this pass. Fallback "manual" if any consumer chokes.
added_by_agent_id: NULL
# abstract/ads_bibcode/s2_paper_id/intro_*/consensus_*/relevance/entailment/rigor/confidence: NULL
```

**T-LEDGER** — one `external_source_log` row per candidate (also for skips):

```yaml
source:      "p4_burn"                                   # 7 chars ≤ String(20) ✓
external_id: "<candidate_id>@20260711T010503Z"           # e.g. "P4-C01@20260711T010503Z", 23 ≤ 100 ✓
page_id:     <resolved page id>
claim_id:    <inserted claim id, or existing claim id on SKIP_DUPLICATE, or NULL on HOLD>
evidence_id: <inserted evidence id or NULL>
decision:    "inserted" | "skipped_duplicate" | "held_near_match"   # ≤ String(40) ✓
quality:     NULL
notes:       "H4 plan FABLE_HARD_BURN_H4_WIKI_DRYRUN_20260711T035354Z; candidates sha256 1c8d9a7d…b39"
```

**A3.1 Source titles** (shared): **S1** = "Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Pilot Matched-Control Study"; **S2** = "Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up". Custody families: S1 → `SDSS_AGN_SFR_PILOT_20260708T122000Z`; S2 → `SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z`.

### A4. Ordered execution steps for the gated pass

- **G0 — Preconditions (live).** Gate approval recorded. Snapshot backend `settings` trust constants (expect `TRUST_W_EVIDENCE=0.45, TRUST_ACCEPTED_MIN=0.30, TRUST_CHALLENGED_MAX=-0.30, TRUST_CONSENSUS_MIN=0.75/min 3 supports`). Confirm deployed code contains the `debate_stance` semantic-cap logic (run `backend/tests/test_trust_debate_stance_caps.py` against the deployed revision or verify `_apply_debate_stance_semantic_cap` present); if absent → per-claim fallback `debate_stance=NULL`, note in receipt. Take a table-scoped dump (`claims`, `evidence`, `external_source_log` rows for the 4 target pages) as the restore point. Pause the autowiki scheduler for the run window if operationally cheap; otherwise accept the benign race (no unique constraint on `(page_id, order_idx)`; a collision only affects display order).
- **G1 — Page-id resolution (live).** For bare slugs `active-galactic-nuclei`, `galaxy-clusters`, `galaxy-formation`, `interstellar-medium`: `SELECT id, title, category, updated_at FROM wiki_pages WHERE slug=:s`. Require exactly 1 row and `category='galaxy'`. Any miss → all candidates targeting that slug fail closed (report, don't guess an alternate page). Record `MAX(page_versions.version_num)` per page (page-state snapshot; replaces `page_version_fk`, §A2).
- **G2 — Section resolution (live).** Per page: `SELECT DISTINCT section FROM claims WHERE page_id=:pid` plus `## ` headers of `wiki_pages.content`. If the candidate's schema-named section exists (exact string), use it. If only a variant exists (live pages are known to deviate, e.g. deep_synthesis writes "Open Questions and Active Debates"), use the page's variant that contains the schema name as prefix/substring and record the mapping. If neither exists, use the schema name as-is (creates a new claims-panel group — legal per schema's required structure) and record it.
- **G3 — Idempotency sweep (live, read-only).** Classify each candidate per §A5 → `INSERT` / `SKIP_DUPLICATE` / `HOLD_NEAR_MATCH`. Snapshot per-page claim counts.
- **G4 — Inserts.** Page-grouped candidate order: AGN page C01→C02→C03→C04→C05→C07→C08→C11; galaxy-clusters C06→C09; galaxy-formation C10→C13; interstellar-medium C12. **One DB transaction per candidate**: re-run the §A5 checks inside the txn; insert T-CLAIM; `flush` → claim_id; insert T-EVID; `flush` → evidence_id; insert T-LEDGER(`decision='inserted'`); commit. Record `(candidate_id → page_id, claim_id, evidence_id, ledger_id, order_idx, section_used)` in the gate-run receipt as each txn commits.
- **G5 — Optional trust normalization.** Per inserted claim, call `recalculate_trust_v2(claim_id, db, trigger="p4_gated_integration")`. Predicted deterministic outcome for every candidate: `E = tanh(0.50/1.5) = 0.32152`, `V=0` (no votes; the Wikipedia cross-check bonus path reads `page.wiki_summary`, a column that does not exist on `WikiPage` → its `AttributeError` is swallowed → bonus never applies), `T=0` (year 2026), `H=0` → `TS = 0.45×0.32152 ≈ +0.1447` < 0.30 → level stays **`unverified`**; writes one `TrustAuditLog` row per claim (covered by rollback). No demotion webhook can fire (that needs `→challenged`, TS ≤ −0.30, impossible with a single supports row). Skipping G5 is also safe: claims sit at default `unverified`/0.0 until the next scheduled recalc.
- **G6 — Post-verify (live, read-only).** Per page: claim count = snapshot + inserts; each new claim returned by the `GET /api/pages/{slug}/claims` query shape in its `section_used` with `trust_level='unverified'`, `evidence_count=1`; ledger rows present for all 13 candidates (including skips/holds).
- **G7 — Receipt.** Persist the gate-run receipt (mapping table, pre/post counts, settings snapshot, section mappings, any fallbacks used) under the gated-run root. This receipt is the **primary idempotency input for any future re-run** (§A5 check 0).

**Requires live-DB confirmation (cannot be known offline):** the 4 page ids and exact live slugs; per-page section inventories; existing near-duplicate claims; prior P4 ledger rows; `order_idx` values; settings constants; deployed-code cap support; autowiki scheduler activity. Nothing in this plan pins an id.

### A5. Idempotency / duplicate-check design (applies per candidate; re-checked inside each insert txn)

0. **Prior-run receipt:** if a previous gate-run receipt maps this `candidate_id` to a claim id that still exists → `SKIP_DUPLICATE`.
1. **Ledger:** `SELECT * FROM external_source_log WHERE source='p4_burn' AND external_id=:eid`. Row with `decision='inserted'` and live `claim_id` → `SKIP_DUPLICATE`. Row with `decision='rolled_back'` → eligible for re-insert (note in receipt).
2. **Exact-text:** `SELECT id FROM claims WHERE page_id=:pid AND text=:claim_text` (claim_text is invariant-locked verbatim, so byte-equality is a stable natural key). Hit → `SKIP_DUPLICATE`, record existing claim id + backfill a ledger row so check 1 catches it next time.
3. **Numeral-anchor probe (near-duplicate guard):** `SELECT id, text FROM claims WHERE page_id=:pid AND text LIKE '%'||:a1||'%' AND text LIKE '%'||:a2||'%'` using the two candidate-distinctive anchors from Part B (chosen in §D2 so they cannot collide across the 13 candidates, including the C10/C13 `0.520` substring trap). Hit with *different* text → `HOLD_NEAR_MATCH`: do **not** insert; ledger `decision='held_near_match'`; escalate to human review (a prior variant integration or an organic claim with the same numerals must be adjudicated, not overwritten).
4. **Evidence dedup (when attaching to an existing claim on SKIP paths, if the gate chooses to backfill evidence):** `SELECT id FROM evidence WHERE claim_id=:cid AND title=:title AND stance='supports'` → skip if present.

### A6. Publish-state proposal

**Insert = publish (as unverified).** There is no claims draft state; the gate approval is the publication decision. Proposed state for all 13: visible immediately with the `unverified` badge; `debate_stance='model_bounded'` permanently caps display at `reported` (honest ceiling for association-only, proxy-bounded, self-sourced pilot results). Predicted steady state after any recalc: `unverified`, `trust_score ≈ +0.145`. Explicitly rejected alternative: hiding via `rewrite_status='parent_replaced'` abuses the rewrite pipeline's tombstone value and would strand invisible rows — **do not use**. Page prose (`wiki_pages.content`) is untouched: no `PageVersion`, no canonicalizer exposure, no attribution-note obligation (that applies to article prose; N/A at claims layer — §C4).

### A7. Rollback design (per candidate or whole run)

Inputs: the gate-run receipt's id mapping (authoritative); fallback discovery `SELECT claim_id, evidence_id FROM external_source_log WHERE source='p4_burn' AND decision='inserted'`. Per candidate, one transaction, FK-safe order:

- R1. Delete late-arriving dependents of our `evidence_id` (expected 0 rows each; count and report if >0): `evidence_votes`, `evidence_comments`, `jury_tasks` (FKs `evidence_id`/`claim_id`), `evidence_element_links` (`evidence_id`/`source_claim_id`/`target_claim_id`), `page_citation_links` (has `ondelete=CASCADE`, listed for completeness).
- R2. Delete the `evidence` row.
- R3. Delete `trust_audit_log` rows for the claim (exist iff G5 ran or a scheduled recalc fired).
- R4. `fact_sources.claim_id` is nullable and written by other generators — if any row references our claim, `UPDATE ... SET claim_id=NULL` (do not delete rows we didn't create). Check `claim_edit_proposals` for the claim (expected 0; if >0, HOLD — a human/agent has engaged with the claim and rollback needs adjudication).
- R5. Delete the `claims` row.
- R6. Keep the ledger row (it is the audit trail); `UPDATE external_source_log SET decision='rolled_back' WHERE id=:ledger_id`.
- R7. Verify page claim count returns to the G3 snapshot (minus other lanes' organic activity — compare against candidate-attributable ids only). Residual `order_idx` gaps are harmless (ordering only, no uniqueness constraint).

### A8. Schema-conformance statement (method)

Per payload, conformance is asserted against **both** schemas: (a) DB shape — every non-default column value listed in Part B fits its declared type/length (checklist §D1); required non-nullables (`claims.text`, `claims.page_id`, `evidence.title`, `evidence.claim_id`) are provided; no fabricated identifiers (`doi`/`arxiv_id`/`url` NULL). (b) Editorial `wiki_schema.md` — category `galaxy` ✓ for all four target pages; proposed sections ∈ required article structure (`Current Research` ×9, `Physical Properties` ×2, `Open Questions` ×2) ✓; reference format carries Author (Year) Title with venue note in `journal_ref` — DOI/arXiv absent because the sources are unpublished internal manuscripts (recorded deviation, §C3); ≥3 see_also links proposed per candidate but deferred (§C2). Each Part B entry ends with its per-candidate statement.

---

## Part B — Per-candidate integration specs (13/13)

Shared: claim payload = **T-CLAIM**, evidence payload = **T-EVID**, ledger = **T-LEDGER** with the overrides below. `claims.text` values below are byte-verbatim `claim_text` from the pinned candidates file (rendered symbols Δ ≥ ∈ ☉ − carried exactly; ASCII hyphens, `--` range dashes, `+/-`, and interval strings preserved character-for-character). Rollback for every candidate = §A7 with that candidate's recorded ids. Publish state for every candidate = §A6.

---

### P4-C01 — Flagship headline: matched-control catalog-sSFR offset
- **Target:** `/wiki/active-galactic-nuclei` → DB slug `active-galactic-nuclei`; `page_id` per §A2/G1.
- **Insert location:** section `Current Research` (G2-verified); `order_idx` = page claim count at insert (first AGN insert of the run).
- **Claim payload (T-CLAIM overrides):** `section="Current Research"`; `text=`
  > In a selection-aware SDSS DR17 matched-control pilot (RP-1), broad optical BPT-selected galaxies are associated with a lower catalog median sSFR proxy than star-forming controls matched in stellar mass and redshift only: the preferred custody-backed comparison yields 8,146 pairs and a median Δlog sSFR (target minus matched control) of -1.309 dex, with a bootstrap 95% confidence interval of [-1.334,-1.283] dex. This is a fiber-centered, morphology-uncontrolled association inside a non-volume-complete, sequentially capped 60,000-galaxy optical cache — not a causal feedback, physical-quenching, gas-depletion, or population-abundance measurement.
- **Evidence payload (T-EVID overrides):** `title=` S1; `journal_ref="Offline cycle-5 candidate manuscript (unpublished); custody run SDSS_AGN_SFR_PILOT_20260708T122000Z"`; `summary=` the three verbatim spans with anchors: (1) FLG snapshot line 13 (abstract): "Broad optical BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only; the preferred custody-backed comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex." [FLG-8146, FLG-MEDIAN-OFFSET, FLG-CI95, FLG-CI-LEVEL]; (2) FLG line 57 (Table 1 row, whole-row invariant FLG-ROW-057): `Broad optical BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\`; (3) FLG line 74 (conclusion): "Its provenance-retained result is the preferred 8,146-pair, -1.309 dex offset with bootstrap 95\% interval [-1.334,-1.283] dex." **CI upper bound must remain `-1.283` byte-exact (manifest known_rounding_anomaly; the re-rounded variant killed cycles 6/7).**
- **Ledger:** `external_id="P4-C01@20260711T010503Z"`.
- **Idempotency anchors (§A5.3):** `-1.309` AND `[-1.334,-1.283]`.
- **Conformance:** DB ✓ (section 16 chars ≤100; text Text; all identifiers NULL); editorial ✓ (galaxy / Current Research / S1 reference; see_also `[/wiki/galaxy-formation, /wiki/quasars, /wiki/stellar-evolution]` deferred §C2).

---

### P4-C02 — Flagship denominator census (BPT class counts)
- **Target:** `active-galactic-nuclei`; **section `Physical Properties`**; `order_idx` = running counter (C01+1).
- **Claim payload:** `section="Physical Properties"`; `text=`
  > The custody-backed analysis denominator of the RP-1 pilot contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects, within a fixed 60,000-galaxy SDSS DR17 optical-emission-line cache. These counts are conditional on the optical selection (strict four-line S/N cut, sequential specObjID cap) and are not population-complete.
- **Evidence:** `title=` S1; `journal_ref` as C01; `summary=` (1) FLG line 39: "The custody-backed analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects." [FLG-SF, FLG-COMP, FLG-8146, FLG-UNCLASS]; (2) FLG line 31: "The retained pilot analysis sample is a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}." [FLG-60000].
- **Ledger:** `external_id="P4-C02@20260711T010503Z"`.
- **Anchors:** `39,553` AND `12,234`.
- **Conformance:** DB ✓ (section 19 chars ≤100); editorial ✓ (Physical Properties hosts quantitative census data per schema; see_also deferred).

---

### P4-C03 — Flagship matching quality (coverage and separations)
- **Target:** `active-galactic-nuclei`; section `Current Research`; `order_idx` = counter.
- **Claim payload:** `section="Current Research"`; `text=`
  > RP-1's preferred matched comparison attains 100% target coverage (8,146 of 8,146 targets matched) using variance-normalized Euclidean nearest-neighbor matching in standardized (log M*, z) space with replacement and no mass–redshift caliper; the unrestricted match has median absolute separations of 0.0045 dex in log M* and 0.00021 in redshift. Matching is in stellar mass and redshift only, so the association still inherits any mismatch in structure or fiber coverage between the two populations.
- **Evidence:** `title=` S1; `journal_ref` as C01; `summary=` FLG line 39: "In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), and the unrestricted Euclidean match has median absolute separations of 0.0045 dex in $\log M_\star$ and 0.00021 in redshift, so the association still inherits any mismatch in structure or fiber coverage between the two populations." [FLG-COVERAGE-PCT, FLG-8146, FLG-SEP-LOGM, FLG-SEP-Z].
- **Ledger:** `external_id="P4-C03@20260711T010503Z"`.
- **Anchors:** `0.0045` AND `0.00021`.
- **Conformance:** DB ✓; editorial ✓ (note: claim text contains an en-dash in "mass–redshift" — carried verbatim; see_also deferred).

---

### P4-C04 — Flagship selection context (parent count and cache coverage)
- **Target:** `active-galactic-nuclei`; **section `Open Questions`**; `order_idx` = counter.
- **Claim payload:** `section="Open Questions"`; `text=`
  > RP-1's analysis sample is a fixed 60,000-galaxy subset of SDSS DR17 selected sequentially by specObjID. The strict public four-line S/N≥3 eligible parent count of 249,917 galaxies, and the corresponding 24.0% cache coverage, are selection-context diagnostics rather than custody-backed independent result rows. Because specObjID ordering follows SDSS targeting and plate/MJD bookkeeping, the subset is non-random and carries survey-plate and sky-coverage bias; it supports no absolute volume densities, luminosity functions, or population-normalized abundances.
- **Evidence:** `title=` S1; `journal_ref` as C01; `summary=` (1) FLG line 31: "The strict public four-line S/N$\geq3$ eligible parent count of 249,917 galaxies, and the corresponding 24.0\% cache coverage, are selection-context diagnostics rather than custody-backed independent result rows" [FLG-SNCUT, FLG-PARENT, FLG-COVERAGE]; (2) FLG line 31: "The retained pilot analysis sample is a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}." [FLG-60000].
- **Ledger:** `external_id="P4-C04@20260711T010503Z"`.
- **Anchors:** `249,917` AND `24.0` (the `%` sign stays out of the LIKE pattern — no escape hazard).
- **Conformance:** DB ✓ (section 14 chars); editorial ✓ (section-name note: live AGN page may carry the deep-synthesis variant "Open Questions and Active Debates" — G2 maps to the page's variant if that is what exists; see_also deferred).

---

### P4-C05 — Flagship aperture geometry (fiber-centered comparison)
- **Target:** `active-galactic-nuclei`; section `Physical Properties`; `order_idx` = counter.
- **Claim payload:** `section="Physical Properties"`; `text=`
  > Over the redshift interval 0.02<z<0.12, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so RP-1's catalog median sSFR proxy comparison is fiber-centered rather than global. Single-fiber measurements can miss extended star-forming disks; if broad optical BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a galaxy-wide star-formation comparison.
- **Evidence:** `title=` S1; `journal_ref` as C01; `summary=` (1) FLG line 32: "Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog median sSFR proxy comparison is fiber-centered rather than global." [FLG-ZRANGE, FLG-FIBER, FLG-KPC]; (2) FLG line 33 (no-numeral context): "If broad optical BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a galaxy-wide star-formation comparison."
- **Ledger:** `external_id="P4-C05@20260711T010503Z"`.
- **Anchors:** `1.2--6.5` AND `0.02<z<0.12` (claim text keeps the `--` range dash verbatim per P4 conventions).
- **Conformance:** DB ✓; editorial ✓ (see_also deferred).

---

### P4-C06 — Supplement environment baseline (10th-neighbor quartiles)
- **Target:** `/wiki/galaxy-clusters` → DB slug `galaxy-clusters`; section `Current Research`; `order_idx` = that page's claim count (first galaxy-clusters insert).
- **Claim payload:** `section="Current Research"`; `text=`
  > Within the fixed 60,000-galaxy SDSS emission-line denominator, a higher internally computed 10th-neighbor index is associated with a modestly higher low-sSFR emission-line fraction: 0.230 (3,456/15,000) in the high-index quartile versus 0.181 (2,710/15,000) in the low-index quartile, with a bootstrap high-minus-low interval of [0.041, 0.059]. A linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004, corresponding to an approximate 3.2 percentage-point increase in low-sSFR incidence at fixed mass and redshift. The 10th-neighbor index is a fiber-collision-biased projected-rank proxy (SDSS 55-arcsec collision limit), not a physical environmental or halo density estimate.
- **Evidence:** `title=` S2; `journal_ref="Offline cycle-5 candidate manuscript (unpublished); custody run SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z"`; `summary=` (1) SUP line 92: "The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004, corresponding to an approximate 3.2 percentage-point increase in low-sSFR incidence at fixed mass and redshift." [SUP-ENV-HI, SUP-ENV-HI-RATIO, SUP-ENV-LO, SUP-ENV-LO-RATIO, SUP-ENV-CI, SUP-ENV-COEF, SUP-ENV-PP, SUP-15000, SUP-NEIGHBOR-ORD, SUP-60000]; (2) SUP line 93: "The SDSS 55-arcsec fiber-collision limit systematically removes close spectroscopic neighbors in dense regions before any physical interpretation is attempted" [SUP-FCOLL]. `0.032 +/- 0.004` carried with `+/-` exactly.
- **Ledger:** `external_id="P4-C06@20260711T010503Z"`.
- **Anchors:** `0.230` AND `[0.041, 0.059]`.
- **Conformance:** DB ✓; editorial ✓ (see_also `[/wiki/active-galactic-nuclei, /wiki/galaxy-formation, /wiki/dark-matter]` deferred).

---

### P4-C07 — Supplement maintenance-heating denominator (massive subset)
- **Target:** `active-galactic-nuclei`; section `Current Research`; `order_idx` = counter (after C05).
- **Claim payload:** `section="Current Research"`; `text=`
  > In the atlas's massive subset (log M* ≥ 10.8), 9,298 SDSS emission-line galaxies include 5,695 low-sSFR objects by the pilot threshold; the broad optical BPT-selected fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This is an optical duty-cycle denominator for future X-ray and radio maintenance-heating follow-up, not a heating-to-cooling measurement.
- **Evidence:** `title=` S2; `journal_ref` as C06; `summary=` SUP line 103: "The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The broad optical BPT-selected fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects." [SUP-MASSCUT, SUP-MASSIVE-N, SUP-MASSIVE-LOWSSFR-N, SUP-BPT-FRAC-MASSIVE, SUP-BPT-FRAC-MASSIVE-LOWSSFR].
- **Ledger:** `external_id="P4-C07@20260711T010503Z"`.
- **Anchors:** `9,298` AND `0.607`.
- **Conformance:** DB ✓; editorial ✓ (see_also deferred).

---

### P4-C08 — Supplement high-excitation subset (resolved-kinematics denominator)
- **Target:** `active-galactic-nuclei`; section `Current Research`; `order_idx` = counter.
- **Claim payload:** `section="Current Research"`; `text=`
  > High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 SDSS emission-line galaxies (0.074). Their median log sSFR is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the subset defines a denominator for resolved-kinematics follow-up, not an escape or recycling result.
- **Evidence:** `title=` S2; `journal_ref` as C06; `summary=` SUP line 114: "High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator." [SUP-HIEXC-N, SUP-60000, SUP-HIEXC-FRAC, SUP-HIEXC-SSFR, SUP-FULL-SSFR].
- **Ledger:** `external_id="P4-C08@20260711T010503Z"`.
- **Anchors:** `4,440` AND `-11.53`.
- **Conformance:** DB ✓; editorial ✓ (see_also deferred).

---

### P4-C09 — Supplement radio-jet environment baseline (massive hosts, quartile contrast)
- **Target:** `galaxy-clusters`; section `Current Research`; `order_idx` = counter (after C06).
- **Claim payload:** `section="Current Research"`; `text=`
  > Among massive hosts in the atlas denominator, the high-index quartile has a broad optical BPT-selected fraction of 0.509, while the low-index quartile has 0.367; the bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency, and the neighbor ranking carries the same fiber-collision bias as the environment baseline.
- **Evidence:** `title=` S2; `journal_ref` as C06; `summary=` SUP line 125: "Among massive hosts, the high-index quartile has a broad optical BPT-selected fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]." [SUP-JET-HI, SUP-JET-LO, SUP-JET-CI].
- **Ledger:** `external_id="P4-C09@20260711T010503Z"`.
- **Anchors:** `0.509` AND `[0.112, 0.170]`.
- **Conformance:** DB ✓; editorial ✓ (see_also deferred).

---

### P4-C10 — Supplement stellar-mass selection diagnostic (incidence by mass bin)
- **Target:** `/wiki/galaxy-formation` → DB slug `galaxy-formation`; section `Current Research`; `order_idx` = that page's claim count.
- **Claim payload:** `section="Current Research"`; `text=`
  > In this optical-emission-line denominator, the first stellar-mass bin with low-sSFR fraction above 0.5 is log(M*/M☉) ∈ [11.0,12.5], and broad optical BPT-selected incidence peaks in the 11.0--12.5 bin at 0.520, within a selection-limited, SpecObjID-capped pilot sample. The peak is consistent with a selection-function bias (the S/N≥3 cut preferentially removes truly passive massive galaxies) and must not be read as a universal physical threshold or a physical transition mass for individual galaxies.
- **Evidence:** `title=` S2; `journal_ref` as C06; `summary=` (1) SUP line 136: "The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the broad optical BPT-selected incidence peaks in the 11.0--12.5 bin at 0.520 within this selection-limited, SpecObjID-capped pilot sample." [SUP-HALF, SUP-MASSBIN-INT, SUP-MASSBIN-DASH, SUP-BPT-PEAK]; (2) SUP line 136: "the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is concentrated in that mass bin." [SUP-SNCUT-B — spacing variant `S/N$\geq$3`, distinct manifest entry].
- **Ledger:** `external_id="P4-C10@20260711T010503Z"`.
- **Anchors:** `[11.0,12.5]` AND `11.0--12.5` — deliberately NOT `0.520`, which also occurs inside C13's `0.003-0.520` span on the same page (§D2).
- **Conformance:** DB ✓ (☉ and ∈ are multi-byte UTF-8, `Text` column — fine); editorial ✓ (see_also deferred).

---

### P4-C11 — Supplement tracer-threshold census (prevalence sensitivity)
- **Target:** `active-galactic-nuclei`; **section `Open Questions`**; `order_idx` = counter.
- **Claim payload:** `section="Open Questions"`; `text=`
  > Within the same 60,000-galaxy SDSS denominator, simple optical tracer definitions produce broad optical BPT-selected prevalence from 0.136 to 0.418 — a widest-to-narrowest prevalence ratio of 3.1 — before adding molecular, neutral, X-ray, or radio phases. This tracer sensitivity motivates a common-denominator multiphase census; it does not measure molecular or neutral outflow rates.
- **Evidence:** `title=` S2; `journal_ref` as C06; `summary=` SUP line 147: "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases." [SUP-60000, SUP-TRACER-LO, SUP-TRACER-HI, SUP-TRACER-RATIO].
- **Ledger:** `external_id="P4-C11@20260711T010503Z"`.
- **Anchors:** `0.136` AND `0.418`.
- **Conformance:** DB ✓; editorial ✓ (same G2 section-variant note as C04; see_also deferred).

---

### P4-C12 — Supplement gas-depletion denominator (CO/HI follow-up baseline)
- **Target:** `/wiki/interstellar-medium` → DB slug `interstellar-medium`; section `Current Research`; `order_idx` = that page's claim count.
- **Claim payload:** `section="Current Research"`; `text=`
  > The gas-depletion note's massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample; its broad optical BPT-selected fraction is 0.549, and the median H-alpha luminosity proxy is log L_Hα = 40.061 (erg/s catalog scale), which is 0.66 dex lower than in massive star-forming emission-line galaxies. The H-alpha value is an aperture-corrected, model-dependent catalog proxy, not a direct total cold-gas-mass measurement, and this denominator is note-specific — it should not be conflated with the log M* ≥ 10.8 maintenance-heating subset.
- **Evidence:** `title=` S2; `journal_ref` as C06; `summary=` (1) SUP line 158: "the massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample." / "Its broad optical BPT-selected fraction is 0.549, and the median H-alpha luminosity proxy is \(\log (L_{\mathrm{H}\alpha}/\mathrm{erg\,s^{-1}}) = 40.061\)." / "The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies." [SUP-GAS-N, SUP-GAS-BPT, SUP-GAS-LHA, SUP-GAS-DEX]; (2) SUP line 158: "This denominator is note-specific and should not be conflated with the \(\log M_\star \geq 10.8\) maintenance-heating subset summarized above." [SUP-MASSCUT, line-158 occurrence].
- **Ledger:** `external_id="P4-C12@20260711T010503Z"`.
- **Anchors:** `6,729` AND `40.061`.
- **Conformance:** DB ✓ (α is UTF-8 in Text — fine); editorial ✓ (see_also `[/wiki/active-galactic-nuclei, /wiki/galaxy-formation, /wiki/nebulae]` deferred). The `model_bounded` cap is especially apt here (explicitly proxy/model-scale-dependent value).

---

### P4-C13 — Supplement simulation target vector (forward-model spans)
- **Target:** `galaxy-formation`; section `Current Research`; `order_idx` = counter (after C10).
- **Claim payload:** `section="Current Research"`; `text=`
  > The atlas's simulation target vector comprises 15 mass-redshift cells with n ≥ 50, recording low-sSFR fraction, broad optical BPT-selected incidence, and median u−r colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729 and broad optical BPT-selected fractions span 0.003-0.520. This is an observed optical target vector for forward modelling, not a simulation comparison; simulations must be passed through the same optical S/N, fiber-aperture, and sequential cache-cap selection function before any comparison is valid.
- **Evidence:** `title=` S2; `journal_ref` as C06; `summary=` SUP line 169: "The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, broad optical BPT-selected incidence, and median \(u-r\) colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and broad optical BPT-selected fractions span 0.003-0.520." [SUP-CELLS, SUP-CELL-MIN, SUP-SPAN-QUENCH, SUP-SPAN-BPT]. **Integrity note carried into `summary`:** spans are anchored to the m3_p3 artifact result bullet, NOT re-derivable from Table 4 (that substitution was the cycle-6 integrity failure); carried verbatim.
- **Ledger:** `external_id="P4-C13@20260711T010503Z"`.
- **Anchors:** `0.005-0.729` AND `0.003-0.520`.
- **Scope flag:** the 15-row target-vector table itself (SUP-ROW-176…190 whole-row invariants, including the line-188 truncation anomaly) is **explicitly out of scope for the claims-layer pass** — it belongs to a future page-content pass and must be carried byte-identical as whole rows if ever integrated (§C5).
- **Conformance:** DB ✓ (− U+2212 in "u−r" carried verbatim in Text); editorial ✓ (see_also deferred).

---

## Part C — Flags: what cannot be mapped cleanly (and why)

All 13 candidates map to insertable claims-layer payloads — **none is blocked**. Five mapping gaps are structural and apply as noted:

- **C1. `page_version_fk` has no DB counterpart.** No column on `claims` references `page_versions`; claims attach to the page, not a version. Mitigation: page-state snapshot (`updated_at`, max `version_num`) recorded in the gate receipt (§A2). Affects all 13 equally.
- **C2. `see_also` is not a claims-layer field.** Page-content `## See Also` (and/or `PageRelation` graph rows) — editing page content triggers the canonicalizer and version machinery, deliberately excluded from this pass. All 13 candidates' ≥3 proposed links are carried above as deferred metadata for a follow-up content pass; that pass must verify each linked slug exists.
- **C3. Reference format deviation.** `wiki_schema.md` reference format expects "DOI or arXiv ID"; S1/S2 are unpublished internal manuscripts with neither. Mapping writes `doi=NULL`/`arxiv_id=NULL` (never the literal `OFFLINE_PLACEHOLDER`), carries venue status + custody run family in `journal_ref`, and relies on `source_channel='p4_offline_candidate'` for queryable provenance. Recorded, accepted deviation — preferable to fabricating identifiers.
- **C4. Attribution note is N/A at the claims layer.** The schema's *[Written from a {specialty} astronomy perspective by {model_name}]* note governs article prose. No prose is written in this pass; if the follow-up content pass runs, it must include the attribution line.
- **C5. Claims table has no candidate-provenance column.** Claim↔candidate linkage is only recoverable via (a) the gate receipt, (b) the ledger rows, (c) evidence `source_channel` + exact text. That is why §A5's ledger is mandatory, written in the same transaction as each insert.

Watch-item (not a blocker): `debate_stance='model_bounded'` overloads a debate-metadata column for status semantics — this is the codebase's own established mechanism (semantic caps + pinned tests), but G0 must confirm the deployed backend has it; fallback is `NULL` + receipt note (§A4 G0).

---

## Part D — Stretch: conformance checklist and dedup matrix

### D1. Field-by-field DB conformance (shared template, verified against model definitions)

| Field | Value (this plan) | Column constraint | OK |
|---|---|---|---|
| claims.page_id | gate-resolved int | FK wiki_pages.id, NOT NULL | ✓ |
| claims.section | "Current Research" (16) / "Physical Properties" (19) / "Open Questions" (14) | String(100) | ✓ |
| claims.order_idx | COUNT at insert | int | ✓ |
| claims.text | verbatim claim_text (all < 1,000 chars; UTF-8 Δ ≥ ∈ ☉ − α) | Text, NOT NULL | ✓ |
| claims.trust_level | "unverified" (10) | String(20) | ✓ |
| claims.claim_type | "established" (11) | String(20) | ✓ |
| claims.debate_stance | "model_bounded" (13) | String(20) | ✓ |
| claims.rewrite_status / connector / debate_topic / created_by_agent_id | NULL | nullable | ✓ |
| evidence.claim_id | flushed id | FK, NOT NULL | ✓ |
| evidence.title | S1 (122 chars) / S2 (78 chars) | Text, NOT NULL | ✓ |
| evidence.authors | "NebulaMind Research Autopilot" | Text NULL-ok | ✓ |
| evidence.year | 2026 | int | ✓ |
| evidence.summary | quoted spans + anchors | Text | ✓ |
| evidence.stance | "supports" (8) | String(20) | ✓ |
| evidence.quality | 0.50 (default) | float | ✓ |
| evidence.journal_ref | ≤ ~110 chars | String(500) | ✓ |
| evidence.source_channel | "p4_offline_candidate" (20) | String(40) | ✓ |
| evidence.doi / arxiv_id / url / ads_bibcode / s2_paper_id | NULL | nullable | ✓ |
| evidence.status | "active" | String(20) | ✓ |
| evidence.peer_reviewed / arxiv_verified | false | bool | ✓ |
| ledger.source | "p4_burn" (7) | String(20) | ✓ |
| ledger.external_id | 23 chars | String(100) | ✓ |
| ledger.decision | ≤ 17 chars | String(40) | ✓ |

Editorial (`wiki_schema.md`) conformance per candidate is stated inline in Part B; deviations are exactly C2–C4 above, identical for all 13.

### D2. Dedup matrix — shared numeral tokens across the 13 candidates (why each anchor pair is collision-free)

Grouped by target page (probes are page-scoped, so only same-page overlap matters):

| Page | Candidate | Distinctive anchor pair | Same-page token overlaps to avoid |
|---|---|---|---|
| AGN | C01 | `-1.309`, `[-1.334,-1.283]` | shares `8,146` with C02, C03; `60,000` with C02/C04/C08/C11; `DR17` with C02/C04 |
| AGN | C02 | `39,553`, `12,234` | shares `8,146`, `60,000`, `67` (too short/common — unused) |
| AGN | C03 | `0.0045`, `0.00021` | shares `8,146`, `100%` (unused) |
| AGN | C04 | `249,917`, `24.0` | shares `60,000`, `S/N≥3` (also in C10 text but different page) |
| AGN | C05 | `1.2--6.5`, `0.02<z<0.12` | shares `3` tokens too generic — unused |
| AGN | C07 | `9,298`, `0.607` | shares `10.8` with C12 (different page); `0.430` unique on page but `0.43` prefix risk — unused |
| AGN | C08 | `4,440`, `-11.53` | shares `60,000`; `0.074` unique but short — backup |
| AGN | C11 | `0.136`, `0.418` | shares `60,000`; `3.1` too short — unused |
| galaxy-clusters | C06 | `0.230`, `[0.041, 0.059]` | shares quartile phrasing with C09; no numeral overlap |
| galaxy-clusters | C09 | `0.509`, `[0.112, 0.170]` | none |
| galaxy-formation | C10 | `[11.0,12.5]`, `11.0--12.5` | **`0.520` collides with C13's `0.003-0.520` substring — deliberately not used** |
| galaxy-formation | C13 | `0.005-0.729`, `0.003-0.520` | `15`, `50` too short — unused |
| interstellar-medium | C12 | `6,729`, `40.061` | `10.8` shared with C07 (different page — safe) |

Anchor-pair uniqueness holds within every target page (both anchors must match, AND-ed), so §A5.3 cannot cross-fire between our own candidates; any hit on a *different* text is a genuine near-duplicate → HOLD.

**Cross-candidate claim dedup:** no two candidates share (page, text); the closest same-page pairs (C01/C02/C03 all quoting 8,146; C06/C09 both quartile contrasts) differ in every anchor pair and in claim text, so exact-text check §A5.2 cannot merge them.

---

*End of plan. Top-line marker `FABLE_HARD_BURN_H4_WIKI_DRYRUN_20260711T035354Z`; produced offline by lane H4 of `fable-weekly-hard-burn-20260711T035354Z`; nothing herein has touched the DB, API, or live wiki.*
