# Ultra usage scrutiny + same-format Galaxy Evolution wiki output gate

Marker: ULTRA_USAGE_AND_WIKI_FORMAT_ROLE_TABLE_PACKET_20260707

User direction:
- Scrutinize how to use Ultra usage.
- The resulting Galaxy Evolution wiki page for each method should use the same format as the current page on NebulaMind.
- Do not let any lane turn this into solo execution. Use the role table.

Role table for this packet:
- Hwao / Fable: coordinator and planner. Divide the work and sequence one role-table packet at a time.
- Lana: high-reasoning science/design/review pressure. Judge whether Ultra/Antigravity output improves the method or introduces overclaim/prose drift.
- Goru: mechanical validation. Count headings, claim markers, citations, source markers, safety locks, quota snapshots, and format conformance.
- Kun: reproducibility / implementation check. Verify another agent can rebuild the same method result from the artifacts, without hidden web/app state.
- Tori / Hermes: relay, recorder, receipt verifier, bounded tool executor. Not captain.

Immediate team protocol:
1. Pause solo next-step behavior.
2. ACK with: `ACK ULTRA FORMAT GATE: Hwao coordinates; Ultra is supervised second-opinion capacity only; each method wiki output must match the current NebulaMind Galaxy Evolution page format.`
3. Hwao must issue a role-split packet before any method continues.
4. If a role partner or required evidence is missing, say `ROLE_TABLE_BLOCKER` and stop.

Ultra / Antigravity usage scrutiny rule:
- Treat Ultra/Antigravity/Gemini capacity as an artifact factory or supervised second-opinion lane, not as permission for autonomous rewriting.
- Default use: one bounded, marker-bearing review packet on a specific contested method artifact, then stop.
- Do not use Ultra just because quota exists. Use it only when Lana/Hwao name the exact question that needs a second opinion.
- Goru must record visible non-secret quota before/after if Ultra/Antigravity is used.
- Kun must verify the output can be reconciled against local repo/source facts and method artifacts.
- Tori records a receipt and rejects outputs that cannot be traced to local artifacts.
- Hard stops: no API key, GCP project, Vertex, billing, payment, credits purchase, account changes, OAuth-code/token handling, browser automation, cron, DB, SQL, publish, deploy, restart, git, or route/config mutation without separate explicit approval.
- `/usage (quota)` in agy/Antigravity is safe for read-only quota visibility. `/credits` is payment/credit-adjacent and must not be opened or used unless the user explicitly approves that exact step.

Current NebulaMind Galaxy Evolution page format contract:
- Canonical current page: `https://nebulamind.net/wiki/galaxy-evolution`
- Canonical API source: `https://nebulamind.net/api/pages/galaxy-evolution`
- Page id/slug observed: page 57 / `galaxy-evolution`
- Version observed: 1710
- Content style: Markdown article rendered by `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`, not a standalone method-card dashboard.
- Required article title: `# Galaxy Evolution`
- Required opening note shape: a blockquote explaining that highlighted claim chips mark statements with provenance and are used sparingly; the page remains a narrative synthesis first.
- Current H2 section skeleton to match unless Hwao explicitly records a reason for one method-level exception:
  1. `Overview: Galaxy Evolution as a Regulated Baryon Cycle`
  2. `Dark Matter Halos & Structure Formation`
  3. `Gas Supply, Star Formation & Feedback`
  4. `AGN Feedback & Quenching`
  5. `Environment, Morphology & Structural Growth`
  6. `Chemical Enrichment & Cosmic Timing`
  7. `High-Redshift & Reionization Frontier`
  8. `Observational Evidence & Surveys`
  9. `Synthesis & Open Tensions`
- Required renderer behavior to preserve:
  - Same NebulaMind article rhythm: title/header/provenance, evidence-view controls, article prose, optional open debates/questions, contributors/edit history when available, and TOC sidebar.
  - Same marker grammar for claim chips: `<!--claim:ID-->prose<!--/claim:ID-->`.
  - Same citation marker grammar where used: `<!--cite:EVIDENCE_ID-->`.
  - Claims must be sparse and meaningful; do not flood every sentence with chips.
  - No `hero_facts` unless separately requested.
  - Sources/history/source page relationship must remain compatible with the current wiki renderer.

Method output gate:
- Existing method `wiki-page.html` files are allowed as static workspaces, but they are not enough as final method wiki outputs if they use custom method-card layout instead of the live NebulaMind article format.
- Each method must produce a same-format draft artifact whose core content is a Markdown article matching the live page format contract above.
- Each method must include a format-conformance receipt with:
  - page title check;
  - opening blockquote check;
  - H2 heading count and exact heading list;
  - claim marker count and IDs;
  - citation marker count and evidence IDs;
  - source/fact-source compatibility note;
  - no live DB/wiki/page_versions publish;
  - no product trust recompute;
  - no cross-method overwrite;
  - no Ultra/Gemini/Antigravity use unless a separate Hwao role packet authorizes exactly one supervised review.

What each method should do next, after ACK only:
- Hwao: create a role-table packet for each method that assigns Lana/Goru/Kun/Tori responsibilities for same-format conversion/review.
- Lana: review whether the method-specific prose preserves scientific caution and does not overclaim.
- Goru: run mechanical format counts against the current page skeleton and method draft.
- Kun: reproduce the draft from source artifacts and verify it can be rebuilt without hidden UI state.
- Tori: record receipts and verify files; do not write/publish the live wiki.

Safety state:
- `NO ACTIVE EXECUTION PHRASE`
- This packet authorizes relay, analysis, and docs/static receipts only.
- It does not authorize live wiki publish, page_versions insertion, SQL, DB writes, deploy/restart, trust recompute, git commit/push/merge, cloud/API/billing/account actions, or payment/credits actions.
