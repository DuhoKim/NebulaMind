# Hwao correction brief — method wiki pages are wrong-format

User correction:
- “I don’t see much of wiki contents on each method’s pages.”
- “I mentioned that the wiki page should have same format as NebulaMind page format, but current ones are not.”

Tori verification result:
- The user is right. The current method outputs under `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/.../wiki-page.html` are static standalone report-style HTML pages, not NebulaMind `/wiki/[slug]` format pages.
- Stop treating the previous director comparison as sufficient. The existing Goru/Kun/Lana comparison receipts are useful only as evidence of the wrong-format artifacts, not as approval to continue evaluating them as final pages.

Canonical NebulaMind wiki page format evidence:
- `frontend/src/app/wiki/[slug]/page.tsx` fetches canonical page data from `/api/pages/{slug}` and renders `<WikiPageClient />`.
- `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` uses the NebulaMind wiki layout:
  - article grid: content column plus sticky TOC rail (`TOCSidebar`), lines around 903–917.
  - Galaxy method links shown above the real Galaxy Evolution page only when `slug === "galaxy-evolution"`, line around 919.
  - History and Sources buttons: `/wiki/{slug}/history`, `/wiki/{slug}/sources`, lines around 944–953.
  - optional hero section from `page.hero_tagline`, lines around 956–1010.
  - provenance chip after hero/fallback header, lines around 1017–1033.
  - trust summary panel, line around 1035.
  - evidence/reader controls: Reader/Evidence toggle, Reduce highlights, citation chip toggle, research questions toggle, lines around 1044–1121.
  - prose is Markdown rendered through `ReactMarkdown`, lines around 1123–1199.
  - claim markers use `<!--claim:ID-->...<!--/claim:ID-->`, parsed into inline trust badges/evidence panels, lines around 141–172 and 1156–1195.
  - citation markers use `<!--cite:ID-->` and `<!--cite-unmatched:...-->`, parsed into citation chips, lines around 148–155 and 1165–1173.
  - TOC is from Markdown headings in page.content, `extractHeadings`, lines around 175–190.

Current method output evidence:
- Method1 static page: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html`
  - 29,063 bytes, about 2,577 words, report/static HTML.
  - Has `Galaxy Evolution — Method 1 wiki page` and provenance/status sections.
- Method2 static page: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html`
  - 28,665 bytes, about 2,570 words, report/static HTML.
- Method3 static page: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html`
  - 18,383 bytes, about 2,327 words, static HTML.
- Landing pages are mostly method workspace/status pages; they link to `wiki-page.html`, but the linked page is still a static HTML approximation, not canonical NebulaMind wiki route/data format.

Required correction:
- Issue a new Hwao same-format rebuild packet.
- The target is not “make the static report HTML prettier.”
- The target is a NebulaMind wiki-format preview for each method: same data/shape/readability as `/wiki/galaxy-evolution` page content, preserving the method-local separation.

Preferred no-apply output scope unless the user separately approves DB/product writes:
1. For each method, generate a same-format Markdown content artifact that could be used as `page.content` for a NebulaMind wiki page:
   - same section/headings style as the canonical page,
   - no report/status boilerplate in the article body,
   - uses NebulaMind marker grammar (`<!--claim:...-->`, `<!--cite:...-->`, `<!--cite-unmatched:...-->`) where IDs are real and verified; if product evidence IDs are unresolved, mark them `cite-unmatched` and ledger them rather than inventing IDs,
   - no hero_facts unless explicitly approved,
   - no broad/unsupported evidence-hunting.
2. For each method, generate a static preview shell only if it mimics the canonical `/wiki/[slug]` layout closely enough for side-by-side review:
   - NebulaMind article grid,
   - title/header/optional tagline,
   - contents rail,
   - Reader/Evidence controls visual state if static,
   - sources/history links either disabled or clearly preview-only,
   - method label outside the article prose, not replacing the wiki content.
3. Produce a method-local conformance ledger comparing each rebuilt method page against the canonical `WikiPageClient` surface.
4. Preserve old wrong-format pages as historical artifacts; do not overwrite them without a backup/manifest.
5. No DB writes, no `/api/pages` update, no page_versions publish, no live wiki publish, no deploy/restart, no git commit/push/merge, no cockpit update, no shared-method overwrite.

Role split request:
- Hwao should produce a lane-split packet with exact deliverables for Method1/2/3 same-format rebuilds.
- Use method-local teams for the actual rebuild work; standalone Goru/Antigravity may help with mechanical conformance checks only.
- Required final Hwao verdict should be about same-format conformance, not about subjective page preference.

Output requested from Hwao:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z.md`

Safety state:
- Docs/static preview only.
- No product/DB/live publish gate is approved.
- User correction supersedes previous comparison-only direction.
