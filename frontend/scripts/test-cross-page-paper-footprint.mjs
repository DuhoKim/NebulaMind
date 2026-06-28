import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/sources/crossPagePaperFootprint.ts");
const sourcesClientPath = path.join(repoRoot, "src/app/wiki/[slug]/sources/WikiSourcesClient.tsx");
const fixtureSourcesPagePath = path.join(repoRoot, "src/app/wiki/source-trace-browser-fixture/sources/page.tsx");
const packagePath = path.join(repoRoot, "package.json");
const aggregatePath = path.join(repoRoot, "scripts/test-wiki-ux-smoke.mjs");
const backendPagesPath = path.resolve(repoRoot, "../backend/app/routers/pages.py");

assert.ok(fs.existsSync(helperPath), "Cross-page paper footprint helper should live beside the wiki sources client.");

const helperSource = fs.readFileSync(helperPath, "utf8");
const compiled = ts.transpileModule(helperSource, {
  compilerOptions: {
    module: ts.ModuleKind.CommonJS,
    target: ts.ScriptTarget.ES2019,
    strict: true,
  },
  fileName: helperPath,
});
const module = { exports: {} };
vm.runInNewContext(compiled.outputText, { module, exports: module.exports, require }, { filename: helperPath });

const { buildCrossPagePaperFootprintDeck, normalizePaperFootprintTone } = module.exports;
assert.equal(typeof buildCrossPagePaperFootprintDeck, "function");
assert.equal(typeof normalizePaperFootprintTone, "function");
assert.equal(normalizePaperFootprintTone("contradicting"), "counter");
assert.equal(normalizePaperFootprintTone("supporting"), "support");
assert.equal(normalizePaperFootprintTone("unclear"), "neutral");

const deck = buildCrossPagePaperFootprintDeck([
  {
    schema_version: "cross_page_paper_footprint.v1",
    paper: { arxiv_id: "2606.990101", title: "Cross-page fixture", author_year_key: "Fixture2026" },
    page_count: 2,
    claim_count: 3,
    evidence_count: 3,
    tone_counts: { support: 2, counter: 1, neutral: 0 },
    trust_counts: { accepted: 1, challenged: 1, debated: 1 },
    scope: { label: "wiki-wide paper footprint", caveat: "Across indexed wiki evidence rows; not a final verdict." },
    pages: [
      {
        slug: "dust-obscured-galaxies",
        title: "Dust-obscured Galaxies",
        claim_count: 1,
        evidence_count: 1,
        counter_count: 1,
        support_count: 0,
        neutral_count: 0,
        claims: [
          { claim_id: 7201, claim_text: "Dust changes counts.", section: "Dust", trust_level: "challenged", stance: "contradicting", tone: "counter", href: "/wiki/dust-obscured-galaxies#claim-7201", votes_agree: 0, votes_disagree: 2 },
        ],
      },
      {
        slug: "early-galaxies",
        title: "Early Galaxies",
        claim_count: 2,
        evidence_count: 2,
        counter_count: 0,
        support_count: 2,
        neutral_count: 0,
        claims: [
          { claim_id: 7101, claim_text: "Massive galaxies assembled early.", section: "Assembly", trust_level: "debated", stance: "supporting", tone: "support", href: "/wiki/early-galaxies#claim-7101", votes_agree: 1, votes_disagree: 0 },
          { claim_id: 7102, claim_text: "Minor mergers add halos.", section: "Assembly", trust_level: "accepted", stance: "supporting", tone: "support", href: "/wiki/early-galaxies#claim-7102", votes_agree: 0, votes_disagree: 0 },
        ],
      },
    ],
  },
  null,
]);

assert.equal(deck.hasCrossPageFootprint, true);
assert.equal(deck.paperCount, 1);
assert.equal(deck.pageCount, 2);
assert.equal(deck.claimCount, 3);
assert.equal(deck.counterCount, 1);
assert.equal(deck.scopeCaveat, "Across indexed wiki evidence rows; not a final verdict.");
assert.equal(deck.items[0].paperLabel, "Fixture2026");
assert.equal(deck.items[0].impactLabel, "2 pages · 3 claims · 1 countering");
assert.equal(deck.items[0].pages[0].slug, "dust-obscured-galaxies", "papers with countering pages should surface first.");

const emptyDeck = buildCrossPagePaperFootprintDeck([]);
assert.equal(emptyDeck.hasCrossPageFootprint, false);
assert.equal(emptyDeck.summary, "No cross-page paper footprint is available for this page yet.");

const futureSchemaDeck = buildCrossPagePaperFootprintDeck([
  { schema_version: "cross_page_paper_footprint.v2", paper: { arxiv_id: "9999.00001", title: "Future schema" }, pages: [] },
]);
assert.equal(futureSchemaDeck.hasCrossPageFootprint, false, "Unknown footprint schema versions should be skipped, not rendered or crashed.");

const fallbackDeck = buildCrossPagePaperFootprintDeck([
  { schema_version: "cross_page_paper_footprint.v1", paper: { arxiv_id: "2606.00042" }, page_count: 1, claim_count: 1, tone_counts: {}, pages: [] },
]);
assert.equal(fallbackDeck.items[0].paperLabel, "2606.00042", "Paper label fallback should prefer arXiv ID before generic copy.");

const clientSource = fs.readFileSync(sourcesClientPath, "utf8");
assert.match(clientSource, /buildCrossPagePaperFootprintDeck/, "Sources page should derive a cross-page paper footprint deck.");
assert.match(clientSource, /\/api\/pages\/paper-footprint\?/, "Sources page should use the read-only paper footprint endpoint.");
assert.match(clientSource, /data-testid="cross-page-paper-footprint"/, "Sources page should expose a stable cross-page footprint section.");
assert.match(clientSource, /data-testid="cross-page-paper-card"/, "Sources page should render stable cross-page paper cards.");
assert.match(clientSource, /data-testid="cross-page-paper-page-link"/, "Cross-page cards should link to affected wiki pages.");
assert.match(clientSource, /data-testid="cross-page-paper-claim-row"/, "Cross-page cards should list affected claims.");
assert.match(clientSource, /wiki-wide paper footprint/i, "Sources page should use explicit cross-page product copy.");
assert.match(clientSource, /not a final verdict/i, "Sources page should avoid truth adjudication copy.");
assert.match(clientSource, /Across indexed wiki evidence rows/i, "Sources page should explain indexed-data scope.");
assert.match(clientSource, /testOnlyFixtureData/, "Sources client should support deterministic no-auth fixture data for browser/route smoke coverage.");
assert.match(clientSource, /footprintError/, "Sources client should track footprint fetch failures separately from empty results.");
assert.match(clientSource, /Couldn't load wiki-wide paper footprint\. Retry\./, "Sources client should render an explicit retryable footprint error.");
assert.match(clientSource, /data-testid="cross-page-paper-footprint-retry"/, "Sources client should expose a stable retry affordance.");
assert.match(clientSource, /aria-label=\{`\$\{page\.title\} —/, "Cross-page page links should include impact counts in their accessible name.");

const fixtureSourcesSource = fs.readFileSync(fixtureSourcesPagePath, "utf8");
assert.match(fixtureSourcesSource, /source-trace-browser-fixture/, "Static source fixture should target the deterministic source-trace slug.");
assert.match(fixtureSourcesSource, /cross_page_paper_footprint\.v1/, "Static source fixture should include a cross-page footprint payload.");
assert.match(fixtureSourcesSource, /data|testOnlyFixtureData|WikiSourcesClient/, "Static source fixture should render through WikiSourcesClient.");
assert.match(fixtureSourcesSource, /not a final verdict/, "Static source fixture should preserve truth-framing copy.");

const backendPagesSource = fs.readFileSync(backendPagesPath, "utf8");
assert.match(backendPagesSource, /@router\.get\("\/paper-footprint"/, "Backend should expose a read-only paper footprint endpoint before slug routes.");
assert.match(backendPagesSource, /cross_page_paper_footprint\.v1/, "Backend endpoint should version its response contract.");
assert.match(backendPagesSource, /not a final verdict/, "Backend scope caveat should avoid truth adjudication.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:cross-page-paper-footprint"], "node scripts/test-cross-page-paper-footprint.mjs");

const aggregateSource = fs.readFileSync(aggregatePath, "utf8");
assert.match(aggregateSource, /test:cross-page-paper-footprint/, "Wiki UX aggregate smoke should include the cross-page footprint probe.");
assert.match(aggregateSource, /cross_page_paper_footprint_ok/, "Wiki UX aggregate smoke should expect the cross-page footprint marker.");

console.log("cross_page_paper_footprint_ok");
