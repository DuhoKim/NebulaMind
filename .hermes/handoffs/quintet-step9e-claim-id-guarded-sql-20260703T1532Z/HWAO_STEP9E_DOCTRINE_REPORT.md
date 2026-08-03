# Hwao/Fable Doctrine Report — Step 9E claim-ID resolution and guarded SQL packet

Task: HWAO STEP 9E adversarial doctrine review · Status: COMPLETE — read-only; no SQL executed; apply/rollback scripts parsed as text only; no DB/API/product/git mutation.
Verified directly: approval packet, all 5 new claim rows, all 35 evidence rows (field discipline + a full 9D→9E stance join), Peng reuse decision, apply SQL (tables touched, guards, temp-table technique), rollback SQL (keying + guards), citation-link plan.

## Verdict: `PASS_WITH_PATCHES` — three patches, all documentation/acknowledgment; no SQL semantics change required.

## What passes, and passes well

- **My three Step 9D patches are implemented — one beyond spec.** The normalization-tolerant duplicate guard is in the apply SQL as a four-way check (exact bibcode array; arXiv IDs normalized by stripping `oai:arxiv.org:` prefixes and `v\d+$` suffixes with case fold; URL patterns; normalized-title match) that RAISEs on any hit. Provenance conventions: all 35 rows carry provenance JSONB with packet id/derivation keys, a dedicated `source_channel`, `verified_at: null`, and zero inherited per-claim metrics.
- **Doctrine holds (Task 1):** all 35 evidence rows target the five NEW derived claims; no existing claim receives new evidence; claim 2929 is explicitly not edited ("split/supplemented… visible/trust recompute belongs to a later gate"); the new claims carry honest initial trust (`debated`/`reported`, no consensus). No evidence-hunting, no rescue, no prose-first violation.
- **Task 4 — no product publish/content update implied:** the SQL inserts into `claims`, `evidence`, `page_citation_links`, plus two `ON COMMIT DROP` temp tables mapping keys→generated IDs (clean technique, no schema change). `wiki_pages`/`page_versions` appear **only inside RAISE guards** (content-hash and latest-version pins). One ordering note: the page-hash pin means this packet must execute *before* any Step 9 content apply, or be re-pinned — state the ordering explicitly.
- **Rollback honesty:** symmetric, keyed on `provenance->>'packet_id'` for evidence and links (via join) and exact claim texts for the five claims, with count guards (0 or 35 / 0 or 5) and its own rollback phrase. Not executed, correctly.
- **Peng/anti-row-17 (Task 5):** reuse of existing evidence 6651 + existing page-57 link 36734, no insert, no update, a guard requirement in the SQL, core sentences restricted to P9S008/P9S009 (the dominance/alternatives axis — exactly the 9D compatibility gate), and loose sentence uses explicitly excluded from execution binding. No hidden rescue: Peng supports the *alternatives* claim, which is the correct polarity.
- **Task 3 — phrase prematurity:** the future execution phrase exists inside the packet conditioned on "after Quintet review and your explicit decision" — the established minting pattern. Recommendation stands: the **cockpit must not display it** until all Quintet lane reports land (dead/premature-phrase rule); the packet text itself is acceptable.

## Finding 1 — the 16 stance mappings are semantically right but undocumented (Patch 1)

Joining 9D design to 9E rows: all 16 non-plain-supports design stances (9 `supports_with_scope_qualifier`, 6 `qualifies`, 1 `contradicts_or_qualifies`) landed as `supports`, with no per-row mapping note. On inspection this is **correct-by-construction, not laundering**: the five claim texts absorbed the qualifier/debate content (claim 733 itself says "detection rates remaining tracer- and sample-dependent"; claim 735 *is* the reservoir caution; claim 734 lists SF-driven outflows among alternatives). A source that qualified the old broad story genuinely supports the new scoped claim — stance complexity migrated into claim wording, which is the derived-claim architecture working. **But an auditor cannot see that from the rows**: 16 silent design→production flattenings are indistinguishable from the stance-laundering pattern this campaign exists to catch. Patch 1: add a per-row `stance_mapping_note` to those 16 rows' provenance (one sentence each: design stance X → supports because the target claim text absorbs the qualifier, quoting the absorbing fragment) plus one packet-level paragraph; re-pin checksums. No stance value changes.

## Finding 2 — execution creates a publicly visible intermediate state (Patch 2)

If executed, this packet changes **two public surfaces before any prose exists**: the claims endpoint will list five new (unsurfaced) claims on page 57, and the citations surface gains 35 new page-citation links with no corresponding content markers until the separate Step 9 content apply. The packet says the claims stay unsurfaced, but it does not name the *visible* intermediate state. Per the campaign's own lesson (visible side effects are decided, not discovered): add an explicit "intermediate visible state" section and give the operator the choice — accept the staged state (links+claims first, prose later) or move the 35 link inserts into the content-apply packet. Either answer is fine; the silence is not.

## Finding 3 — two one-line assertions (Patch 3)

(a) `source_channel` value is 35 characters — have the validator assert the column accepts it (the `String(40)` trigger incident is the standing precedent for silent length traps). (b) `peer_reviewed: true` on all 35 — defensible (all sources carry journal bibcodes), but record the basis in provenance ("peer_reviewed set from journal bibcode presence") so it reads as evidence, not assumption.

## Task answers

1. Overclaiming/evidence-hunting/prose-first: none — derived-claims-only targeting verified at row level. 2. Evidence rows as prose completion or Step 10 unlock: no — explicitly deferred, Step 10 locked; Finding 2 adds the missing visibility acknowledgment. 3. Phrase premature for public display: in-packet minting is fine; cockpit display waits for Quintet completion. 4. No publish/content-update/deploy implied: verified in SQL text (guards-only references to page tables) with one execution-ordering note. 5. Peng stance semantics: clean — reuse restricted to the compatible axis, loose uses excluded, no rescue.

## Safety ledger (this review)

SQL executed 0 · DB writes 0 · API mutations 0 · migrations 0 · deploy/restart 0 · product publish 0 · git 0 · files written 1 (this report).

HWAO_STEP9E_DOCTRINE_DONE
