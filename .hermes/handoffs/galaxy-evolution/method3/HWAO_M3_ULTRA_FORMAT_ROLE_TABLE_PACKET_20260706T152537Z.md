# Method3 role-table packet — Ultra usage scrutiny + same-format wiki output gate

Marker: GALAXY_EVOLUTION_METHOD3_ULTRA_FORMAT_ROLE_TABLE_20260706T152537Z
Parent packet: ULTRA_USAGE_AND_WIKI_FORMAT_ROLE_TABLE_PACKET_20260707 (mastermind root)
Issued by: Hwao-DMW — coordinator/planner (coordination only; no method substance in this packet)
Execution state: NO ACTIVE EXECUTION PHRASE

ACKs already on record:
- `ACK ROLE TABLE TEAMWORK: no solo execution; Hwao coordinates, Lana reasons/reviews, Goru mechanically verifies, Kun checks reproducibility, Tori relays/records/verifies.`
- `ACK ULTRA FORMAT GATE: Hwao coordinates; Ultra is supervised second-opinion capacity only; each method wiki output must match the current NebulaMind Galaxy Evolution page format.`

## Method3 state this packet builds on

- P0 receipts complete (packet `GALAXY_EVOLUTION_METHOD3_P0_START_20260706T140842Z`).
- P1 docs-only sentence plan (S01–S12, 7 debate axes) adopted as **plan of record** by Hwao review
  `reviews/HWAO_P1_SENTENCE_PLAN_REVIEW_20260706T150253Z.md` (verdict PASS).
- Lana/Goru/Kun/Tori P1 reviews were recommended but not yet written. This packet folds those
  P1 review duties into the new gate deliverables so each lane writes exactly one report.

## Gate requirements (from user direction + mastermind packet)

1. **Ultra scrutiny:** Ultra/Gemini/Antigravity is supervised second-opinion capacity only.
   Default for Method3 is ZERO Ultra use. This packet does NOT authorize any Ultra use.
2. **Format gate:** the final Method3 Galaxy Evolution wiki output must be a Markdown article
   matching the current live NebulaMind page format contract (mastermind packet, "format contract"
   section): title `# Galaxy Evolution`; opening blockquote about sparse claim chips; the exact
   9-H2 skeleton (Overview: Regulated Baryon Cycle / Dark Matter Halos & Structure Formation /
   Gas Supply, Star Formation & Feedback / AGN Feedback & Quenching / Environment, Morphology &
   Structural Growth / Chemical Enrichment & Cosmic Timing / High-Redshift & Reionization
   Frontier / Observational Evidence & Surveys / Synthesis & Open Tensions); claim chip grammar
   `<!--claim:ID-->prose<!--/claim:ID-->`; citation grammar `<!--cite:EVIDENCE_ID-->`; chips
   sparse; no `hero_facts`. The existing `wiki-page.html` method-card workspace remains allowed
   as a workspace but is NOT the final method output.

## Lane assignments (each lane writes exactly ONE report under this method root)

### Lana — high-reasoning science/design review
Report: `reviews/LANA_M3_P1_FORMAT_ULTRA_MEMO_<UTC>.md`
1. P1 duty (carried over): review the S01–S12 sentence plan for semantic accuracy, reader
   clarity, and overclaim risk; note verdict per sentence or per group.
2. Section mapping judgment: propose how the S01–S12 spine distributes across the 9 live-page
   H2 sections (which sentences seed which sections; where the spine under-covers a section,
   e.g. halos/chemical enrichment/high-z, mark it COVERAGE_GAP for Hwao sequencing — do not
   silently invent content).
3. Ultra scrutiny: state whether any exact, bounded Method3 question would benefit from ONE
   supervised Ultra second opinion (e.g. adjudicating a contested overclaim call). "Quota
   exists" is not a reason. If none, record `ULTRA_NOT_NEEDED` with one line of reasoning.
   Do not invoke Ultra yourself.

### Goru — mechanical validation
Report: `reviews/GORU_M3_P1_FORMAT_CHECKLIST_<UTC>.md`
1. P1 duty (carried over): verify all 7 debate axes appear in the plan md+json, counts match
   (7 axes / 12 sentences), and hard-stop/no-write markers are present in the P1 artifacts.
2. Instantiate the Method3 format-conformance checklist from the mastermind contract as
   measurable checks: title string; blockquote presence; H2 count == 9 and exact ordered list;
   claim marker count + IDs; cite marker count + evidence IDs; sparse-chip bound (record the
   current live page's chip count as the reference bound if visible in local sources);
   `hero_facts` absent; renderer-compatibility notes. Output = a checklist other lanes can run
   verbatim against any future Method3 draft.
3. Source rule: derive reference facts from LOCAL repo artifacts only (e.g. `wiki_schema.md`,
   `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`, existing docs snapshots). No DB queries,
   no network fetch. If the live page snapshot (page 57 / version 1710) is required and no
   local snapshot exists, record `ROLE_TABLE_BLOCKER: live-page snapshot needed` instead of
   fetching solo — Tori fetches read-only only after Hwao/user approval.

### Kun — reproducibility / implementation check
Report: `reviews/KUN_M3_P1_REPRO_CHECK_<UTC>.md`
1. P1 duty (carried over): confirm another agent could rebuild the S01–S12 plan from the named
   source files (debate-map refresh run `hwao_debate_map_refresh_20260706T002104Z`, baseline
   step6 status_debate_map, method briefs) with no hidden state.
2. Format-gate duty: confirm the format contract itself is rebuildable from named local sources
   (list exact file paths + fields), and define the rebuild recipe another agent would follow to
   regenerate the future same-format Method3 article draft from {P1 plan, Lana section mapping,
   Goru checklist}. Flag any step that would require hidden web/app state.
3. Note the carried source caveat: `status_debate_map.json` status is
   `FINAL_DRAFT_PATCHED_AFTER_GORU_BLOCKER_PENDING_RECHECK`; the citation-binding gate must
   resolve it or bind against the refreshed debate map as primary.

### Tori — relay, recorder, receipt verifier (not captain)
Report: `receipts/TORI_M3_FORMAT_GATE_RECEIPT_<UTC>.md`
1. Verify the three lane reports exist under this method root, carry this packet's marker, and
   each contains a hard-stop acknowledgement; record a receipt listing file paths + markers.
2. Maintain the safety ledger for this gate: confirm zero Ultra/Gemini/Antigravity use, zero
   DB/SQL/publish/deploy/restart/git/cloud/billing actions by any lane.
3. Bounded tool execution (e.g. a read-only live-page snapshot GET) ONLY if Hwao/user issues an
   explicit later instruction naming the exact command; otherwise record requests as blockers.

## Sequencing

1. Goru (checklist) and Lana (memo) may run in parallel — neither depends on the other.
2. Kun runs after Goru+Lana reports exist (his recipe references both).
3. Tori receipts last.
4. Hwao then writes the gate verdict and, if clean, opens P2: docs-only same-format prose
   draft — a Markdown article in the Method3 public workspace following the 9-H2 skeleton and
   Lana's mapping, WITHOUT claim/cite markers (P2 checks title/blockquote/H2 conformance only).
   Claim-chip + citation binding stays a later P3 gate, per the P1 plan-of-record rule.
   No lane starts P2 work under this packet.

## Ultra doctrine for Method3 (binding until superseded)

- No lane may invoke Ultra/Gemini/Antigravity under this packet. Zero-use is the default outcome.
- A future use requires ALL of: Lana names the exact bounded question → Hwao issues a separate
  single-use authorization packet → Goru records visible non-secret quota before/after
  (`/usage` only; `/credits` is forbidden) → Kun reconciles the output against local artifacts →
  Tori records the receipt and rejects untraceable output. Output is advisory only and never
  lands in a deliverable without lane review.

## Hard stops (all lanes)

No live wiki publish or page_versions update; no DB write, SQL apply/rollback, or migration;
no trust recompute; no backend/API/service restart; no deploy; no git commit/push/merge; no
cloud/API/GCP/billing/account/payment/credits actions; no browser automation; no cron; no
OAuth/token handling; no cross-method writes; no shared-parent/alias edits; no solo
Ultra/Gemini/Antigravity use. Writes only inside the Method3 handoff root and Method3 public
workspace. If a role partner or required evidence is missing: say `ROLE_TABLE_BLOCKER` and stop.

## Stop condition for this gate

Gate is complete when the three lane reports + Tori receipt exist (or explicit
`ROLE_TABLE_BLOCKER` entries are recorded) under this method root, and Hwao has written the
gate verdict. Hwao stops now, after ACKing this packet's path.
