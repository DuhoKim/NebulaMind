# Lana M2 brief — same-format page.content rebuild

Packet: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z.md`
Marker to include: `HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z`

Your role: Method2 Lana content owner only.

Input draft:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md`

Output file:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md`

Task:
- Produce canonical NebulaMind `/wiki/[slug]` `page.content` Markdown only.
- Strip all report/status/safety/provenance/receipt boilerplate from article body.
- Preserve the actual wiki prose and canonical 9 H2 order.
- Claim markers expected: 2942–2947. Verify open markers equal close markers.
- Cite markers: only use numeric `<!--cite:ID-->` if locally resolvable to real product cite/evidence ID from existing method-local ledgers. Do NOT query DB/API. Do NOT invent IDs. Any unresolved source-adjudication 28xxx ID becomes `<!--cite-unmatched:TEXT-->` and must be ledgered in comments/section notes or a brief unresolved ledger at the end of the output.
- No hero_tagline, no hero_facts, no HTML shell, no live/product/DB/API/publish/git/cockpit/deploy action.
- Do not overwrite old `wiki-page.html` or any existing draft.
- If blocked, write a ROLE_TABLE_BLOCKER report under method2 and stop.
- Stop after writing the one output file.
