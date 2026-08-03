# Goru M2 brief — same-format conformance ledger

Packet: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z.md`
Marker to include: `HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z`

Your role: Method2 Goru mechanical conformance only.

Inputs:
- Content: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md`
- Preview: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`
- Canonical reference: `/Users/duhokim/NebulaMind/NebulaMind/frontend/src/app/wiki/[slug]/WikiPageClient.tsx`

Output ledger:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/SAME_FORMAT_CONFORMANCE_LEDGER_20260707T064500Z.md`

Task:
- Mechanical pass/fail only: H2 count/order, claim markers open==close + expected ID set, numeric cite count, cite-unmatched count, TOC-heading parity, boilerplate scan after stripping HTML comments, shell grid/rail/header/provenance/static controls/preview-only links/method-label-in-chrome checks.
- Expected M2: 9 H2s, claim IDs {2942,2943,2944,2945,2946,2947}, 0 numeric cites, cite-unmatched markers allowed and expected for unresolved local 28xxx source IDs.
- No content edits, no shell edits, no DB/API/live/publish/git/deploy/cockpit/cloud.
- Stop after writing the one ledger file.
