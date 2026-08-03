# Fable Grand Design — one canonical Galaxy Evolution page

Lane: outside strategist / adversarial reviewer (Fable 5)
Task: GALAXY_CANONICAL_GRAND_DESIGN_20260702 — advisory only, read-only, no mutation attempted.
Evidence read: baseline_compare.md/.json, both page content exports, both claims JSONL files (721 + 8 rows), version-history notes inside the baseline JSON.

## 0. What the baseline actually says (the asymmetry that decides everything)

| | Page 57 (V1) | Page 58 (V2 pilot) |
|---|---|---|
| slug | `galaxy-evolution` (clean, canonical-shaped) | `galaxy-evolution-v2` (workbench-shaped) |
| version history | 1,708 versions, forensic source_notes, proven backup/revert practice (v1704 bad apply → forward-revert v1705) | 7 versions, all June pilot |
| claims | 721 rows — but **526 are trust `"0.5"` with zero evidence** (the junk/bulk layer); only 22 are surfaced as markers in current prose | 8 rows — all calibrated (`debated`/`consensus`), 8–40 evidence rows each, all surfaced |
| evidence rows attached | 223 (supports 98, neutral 82, mismatch 29, challenges 12, refutes 2) | 138 (supports 35, **none 102**, challenges 1) |
| citation links / fact sources | 8 / 3 | 0 / 0 |
| prose (current) | v1708 "max-papers apply" — 8-section synthesis, reader-facing voice, 22 inline claim markers woven into sentences | 9-section synthesis, good skeleton, but **drafting-spec voice leaks into reader text** ("This page should avoid pretending…", "The main editorial improvement is to stop presenting 'debates' as separate article furniture") |
| claim marker syntax | `<!--claim:NNNN-->` | `<!-- claim:NNNN-->` (leading space — parser/tooling trap) |

Two more facts that matter: claim ID ranges do not collide (V1 tops out at 2926, V2 is 2929–2936), and neither page has `url_count` entries, so external-link breakage risk is low. Also note V1's prose is *not* the ancient page — it was itself rewritten on 2026-06-21; the "old vs new" framing is misleading. The real difference is **where the assets live**, not which prose is modern.

## 1. Which page should be canonical? — Page 57, slug `galaxy-evolution`. Not close.

**Choose V1/page 57 as the canonical identity and absorb V2's assets into it.**

Defense:

- **Data gravity.** Page 57 owns the claim/evidence/debate graph (721 claims, 223 stanced evidence rows, votes, citation links, fact sources) and a 1,708-version forensic history that has already survived a bad apply and a forward-revert. Re-homing 8 V2 claims into page 57 is a ~8-row repoint with evidence following by claim_id; moving 721 claims the other way (or to a new entity) is a mass migration with hundreds of failure points and zero benefit.
- **Slug semantics.** `galaxy-evolution` is what a reader, a search engine, and every internal surface expects. `galaxy-evolution-v2` is a lab bench; promoting a `-v2` slug to canonical either strands the clean slug or forces a rename anyway — so you'd pay the migration and still end up doing V1-side work.
- **Version-history continuity.** Canonical identity should keep the audit trail. Page 57's history *is* the institutional memory of this page (including the hero_facts clearing, the FIX4 seed, the distill repairs). Starting a new entity orphans that.
- **What V2 actually contributes is portable.** Its genuinely valuable assets are: (a) the 8 calibrated claims with deep evidence, (b) the "Synthesis: What Regulates Galaxy Evolution?" closer, (c) the surveys-framed-by-what-uncertainty-they-reduce section, (d) the editorial rule "absorb debates into topical sections, don't quarantine them," and (e) the reader-note header about claim chips. All five move easily into page 57. Nothing about them requires V2's page row to survive as canonical.

**Reject "new entity"** explicitly: a third page doubles the migration (both old pages must map into it), breaks the slug or requires a swap-rename dance, resets version history, and its only theoretical benefit — a "clean start" — is already delivered by page 57's v1708 rewrite plus a content update. New-entity is the highest-risk, lowest-benefit option on the table.

## 2. Clean end-state model

- **Identity:** one publishable page: id 57, slug `galaxy-evolution`, title "Galaxy Evolution". Its content is the merged prose (V1 spine + V2's five portable assets), with claim markers normalized to one syntax (`<!--claim:NNNN-->`) *in the new version only* — never by rewriting historical versions.
- **Claims:** V2 claims 2929–2936 re-homed to page 57 (page_id repoint preferred over copy — preserves claim IDs, evidence rows, votes, and debate links untouched). They join V1's 22 surfaced claims in matching sections. The 699 unsurfaced V1 claims remain attached to page 57 as backlog data, unrendered, explicitly out of scope for this merge.
- **Page 58:** retired workbench, not deleted. Title stays honest ("… V2 Pilot — Archived"), content replaced by a short banner + pointer to canonical + a note of what was absorbed and when. Keep its 7-version history intact as the pilot's record. Its claims table ends empty (claims moved, not copied) with the move recorded in source_notes on both pages' new versions.
- **Redirect/alias:** end state is `galaxy-evolution-v2` → 301/router-level redirect to `galaxy-evolution`. This needs a source-level check (does `backend/app/routers/pages.py` support aliases/redirects today?). If not supported, interim state = archived banner page (safe, zero source edits), and the redirect ships later as a separate, small, source-edit-gated change. Do not block the content merge on router work.
- **Workbench pattern going forward:** no more sibling `-v2` page rows for pilots. Pilots live as draft `page_versions` or docs-only preview packets (the exact-diff pattern), and if a sandbox page row is ever truly needed it must carry a non-canonical banner and a decision-by date from birth. The V1/V2 confusion this task exists to fix is the direct product of piloting via a second live page row.
- **Future editing workflow:** all content changes to page 57 go through the now-proven loop: docs-only exact-diff packet → Goru machine validation → Lana adversarial pass → Duho EXECUTE → apply → render verification → snapshot archive.

## 3. Phases and approval gates

- **Phase 0 — Baseline (done).** This quartet directory is the frozen read-only baseline; its SHA-256 hashes pin both pages.
- **Phase 1 — Canonical merge preview packet (docs-only, next).** One directory containing: (a) a **spine map table** — every canonical H2, which V1/V2 section feeds it, which claims anchor in it; (b) the **merged prose draft** with all 30 claim markers placed and V2's drafting-spec voice stripped; (c) the **claim re-homing table** (2929–2936: page_id repoint + section assignment + marker position); (d) the **page 58 retirement draft** (banner text, retitle); (e) explicit exclusions (everything in section 4 below). *Gate: Duho approves the merged draft direction — a content-taste decision only he can make.*
- **Phase 2 — Exact-diff packet (docs-only).** Reuse the pages-5/19/23 machinery verbatim: read-only DB snapshot of both pages' rows (wiki_pages, page_versions, claims, evidence, page_citation_links, fact_sources), whole-page before/after diffs for both pages, row-level backup, dry-run-validated rollback script, Goru validation JSON (marker parse check, claim-count reconciliation 22+8, byte-identity of untouched fields, NO-junk-claim-leak check), one Lana adversarial pass, one EXECUTE phrase. *Gate: Goru PASS + Lana PASS + Duho pastes EXECUTE.*
- **Phase 3 — Apply + verify.** Guarded apply (page 57 content + claim repoints first, page 58 banner second), then render probes: both slugs return 200, all 30 chips resolve on canonical, zero orphan markers, version_num +1 on each page, post-apply snapshots archived beside pre-apply. *Gate: verification report; any failed probe → rollback, no partial state.*
- **Phase 4 — Redirect/retirement completion (separately gated).** Only after Phase 3 settles: router alias/redirect for `galaxy-evolution-v2`, de-index if applicable. This is a **source-edit risk class**, so it gets its own small approval and its own verify. *Gate: separate approval phrase; never bundled into the DB EXECUTE.*
- **Phase 5 — Backlog campaign (out of scope here).** The 526 zero-evidence `"0.5"` claims and the 377-claim "Open Questions & Frontier Debates" dump-section are a claim-triage campaign for the paper-distillation pipeline, not part of canonicalization. Naming this explicitly prevents the merge from swelling into a rewrite of 721 claims.

Sequencing caution: Phase 1 can be prepared now in parallel with the running pages-5/19/23 exact-diff work (both are docs-only), but **do not present Duho two EXECUTE phrases in the same window**. Queue the galaxy EXECUTE behind the 3-page correction so operator attention on mutations stays undivided.

## 4. What must NOT be merged automatically

1. **Trust labels.** No auto-normalization of V1's 526 `"0.5"` values into real labels, and no silent laundering of them onto canonical rendered surfaces. They stay backlog until adjudicated.
2. **Claim text.** The merge moves and places claims; it does not rewrite them. Claim rewording is the adjudication pipeline's job, with source positions.
3. **Evidence stance rows.** V2 carries 102 stance-`none` rows and V1 carries `mismatch`/`refutes` rows from a different era's semantics; bulk stance rewriting during a page merge would corrupt two different provenance vocabularies at once.
4. **Section assignment by string-matching.** V1 claim sections ("Physical Mechanisms", "Open Questions & Frontier Debates") don't correspond to either prose spine. Only the 30 surfaced claims get human-reviewed placements; nothing else is remapped.
5. **Version histories.** Never squash, rewrite, or migrate page_versions between pages. Page 58's history stays on page 58.
6. **Deletions.** No page row, claim row, or evidence row is deleted anywhere in this plan. Retirement = banner + emptied claim attachment via repoint, all reversible from backup.
7. **Marker-format history rewrites.** Normalize marker syntax in the new canonical version only; historical versions keep their bytes.
8. **The hero_facts surface.** It was deliberately cleared on page 57 (v1703) and is terminated framing; nothing from V2 may resurrect it as a side effect.

## 5. Single next move Hermes should recommend to Duho

**Commission Phase 1: the docs-only Canonical Merge Preview Packet for page 57.** One directory, one timebox (≤3 hours of lane time), Goru building the mechanical spine/claim tables from this baseline, Lana adversarially checking the merged draft for V2 meta-voice leaks, junk-claim leakage, and marker integrity, Hermes assembling and updating the cockpit. Deliverable Duho can judge in five minutes: the spine map, the merged draft, the 8-claim re-homing table, and the page 58 retirement banner — with the Phase 2 exact-diff approval phrase attached, and the galaxy EXECUTE explicitly queued behind the pages-5/19/23 correction.

Suggested approval phrase for Hermes to offer:

```text
APPROVE GALAXY CANONICAL MERGE PREVIEW PACKET: Build a docs-only preview packet that merges Galaxy Evolution V1 (page 57) and V2 (page 58) into one canonical draft on slug galaxy-evolution: spine map, merged prose draft with normalized claim markers, claim re-homing table for claims 2929-2936, page 58 retirement banner draft, and explicit exclusion list. Write docs/JSONL/Markdown artifacts in one new directory only. No DB writes, SQL mutations, migrations, deploy/restart, git writes, runtime source edits, secrets, OpenClaw, or deletes. Timebox 3 hours; galaxy execution remains queued behind the pages-5/19/23 exact-diff EXECUTE.
```

One-line verdict: **canonical is page 57 with V2 absorbed as assets, page 58 retired behind a banner then a redirect — the merge is a placement exercise for 30 good claims, not a rewrite of 721.**

FABLE_GALAXY_CANONICAL_DESIGN_DONE_20260702
