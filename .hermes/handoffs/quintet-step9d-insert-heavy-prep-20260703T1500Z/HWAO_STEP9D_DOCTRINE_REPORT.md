# Hwao/Fable Doctrine Report — Step 9D insert-heavy exact-diff preparation

Task: HWAO STEP 9D adversarial doctrine review · Status: COMPLETE — read-only except this report; no SQL executed or created; no DB/API/product/git mutation.
Verified directly: approval packet, all 35 use-matrix rows (field-level distributions), all 25 candidate entities, claim skeletons, Peng reuse decision, GO/NO-GO (raw rows), summary/validation, full-directory phrase scan.

## Verdict: `PASS_WITH_PATCHES` — three patches, all landing as Step 9E requirements; the packet itself may complete as PREPARED_ONLY.

## Task 1 — Adversarial findings

- **Evidence-ID laundering: NONE — and the design is doctrinally elegant.** All **35** claim-use rows target the five **new skeleton claims** derived from the Step 9 prose; **zero** rows attach sources to existing numeric claim IDs. No old claim is being rescued by new evidence. Better still: the five countercase papers land as *supports* for the dominance/alternatives and reservoir-caution claims — the debate map has converted contradiction into first-class supported content, which is exactly what "derived claims from the prose" is supposed to produce (stance design: 19 supports, 9 supports-with-scope-qualifier, 6 qualifies, 1 contradicts-or-qualifies; targets: dominance 13, outflows 7, heating 6, reservoir 6, synthesis 3).
- **Rollback dishonesty: NONE.** The rollback artifact is explicitly design-only (order named, no SQL), the backup design *requires* a fresh backup in the future execution packet rather than pretending the read-only snapshot is one, and the GO/NO-GO row states it plainly. Honest on all three surfaces.
- **Hidden execution phrase: NONE.** Full-directory scan finds no execute/apply/run phrase; `insert_sql_status` on all 35 rows reads "NOT_AUTHORED_AS_EXECUTABLE_SQL_IN_STEP9D_PREP"; the only forward phrase is the 9E preparation approval (below).
- **Step 10 creep: NONE.** Dedicated NO-GO row ("Step 9D prep does not complete the Galaxy Evolution wiki page or unlock Step 10"); six NO-GOs total, all held.
- **Duplicate-row hazards: one real residual (Patch 1).** The existence check reports "insert-candidate **exact-key** existing rows: 0" — exact-key only, with no normalization mention in summary or validation. The 9C finding stands: this DB provably contains variant identifier formats (`v\d+` suffixes, `oai:arXiv.org:` prefixes), so exact-key zero can be a false negative that later mints duplicates. Separately, the **Peng anti-row-17 rule is implemented exactly as required** (prefer reuse of 6651; no new Peng row without explicit operator override) — and its stance/proposition gate ("dominance-alternative or strangulation qualifier ONLY") correctly prevents reuse from becoming a stance mismatch.

## Task 2 — Should the packet complete despite 35 cross-claim citation review refs?

**Yes.** The 35 refs are declared, counted, and fenced as an explicit NO-GO row for Step 9E ("product evidence rows are claim-scoped" — the review exists precisely because each paper-use must be judged per target claim). A preparation packet completing with declared-and-gated unresolved items is the correct gate pattern this campaign has used since the first preflight; hiding them would be the defect, and they are not hidden. Completion as `PREPARED_ONLY` with those NO-GOs standing is approved from this lane.

## Task 3 — Is the next approval phrase safe and non-executing?

**Yes.** The 9E phrase authorizes claim-ID resolution and *authoring* of an execution-ready backup/diff/rollback SQL packet, dispatches Quintet review, and "stop[s] before execution," with the full hard-stop list enumerated (no DB writes, SQL mutations, API mutations, migrations, deploy/restart, product publish, git). This matches the established write-packet pattern: SQL may exist at 9E, phrase-gated and unexecuted, with execution requiring its own later operator paste. No ambiguity found.

## Task 4 — Core doctrine preserved?

**Decisively.** The flow here is papers → ledger → map → prose → **derived claims** (five skeletons matching the prose's five paragraphs) → evidence attachments designed against those derived claims. The skeletons encode the 9B dispositions structurally — "DO_NOT_REUSE_2924_AS_FLAT_CONSENSUS_HEATING," 2915 preservation as an *option* with drift check and no new insert, 2917 rebind gated on the 2557/2572 duplicate consolidation (the backlog remembered, not rediscovered). Nothing in this packet hunts evidence to rescue an old sentence; every attachment serves a claim derived from the reviewed prose.

## The three patches (all as Step 9E requirements; add one line each to 9D's design docs now)

1. **Normalization-tolerant existence guard at 9E.** Note in 9D's summary that the duplicate check was exact-key only; require 9E's guarded SQL preconditions to re-check existence with normalized identifiers (strip `v\d+$`, strip `oai:arXiv.org:` prefixes, case/whitespace fold) per source before any insert — a false-negative here is how row-duplication happens despite the anti-row-17 rule.
2. **Insert-row template inherits the sourcefill-v2 provenance conventions, by name.** The 25 entity rows carry no provenance fields yet (acceptable at design level), but 9E's evidence-insert template must mandate: in-band `provenance` JSONB (packet id, derivation reason, human-gold status), a real `source_channel`, honest `verified_at` semantics (null unless position-verified), and no inherited per-claim metrics. These lessons were paid for once (the 2299 source-fill block); make them structural, not remembered.
3. **Design stances resolve through the Contract v1 ledger↔production stance-mapping table, per row.** `supports_with_scope_qualifier` (9 rows) and `contradicts_or_qualifies` (1 row) are design placeholders, not production enums; 9E must map each through the contract's table (e.g., qualifier → `neutral` + qualifier note, never silently flattened to `supports`), with no bulk defaulting.

## Safety ledger (this review)

DB writes 0 · SQL executed/created 0 · API mutations 0 · migrations 0 · deploy/restart 0 · product publish 0 · git 0 · files written 1 (this report).

HWAO_STEP9D_DOCTRINE_DONE
