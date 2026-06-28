import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/paperClaimFlightDeck.ts");
const clientPath = path.join(repoRoot, "src/app/wiki/[slug]/WikiPageClient.tsx");
const packagePath = path.join(repoRoot, "package.json");
const aggregatePath = path.join(repoRoot, "scripts/test-wiki-ux-smoke.mjs");

assert.ok(fs.existsSync(helperPath), "Paper-to-claim flight deck helper should live next to wiki page helpers.");

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

const {
  buildPaperClaimFlightDeck,
  extractPaperClaimEdges,
} = module.exports;

assert.equal(typeof buildPaperClaimFlightDeck, "function");
assert.equal(typeof extractPaperClaimEdges, "function");

const content = `# Fixture page

<!--claim:501-->Massive galaxies assembled early<!--cite:101,102-->.<!--/claim:501-->

<!--claim:502-->Minor mergers add stellar halos<!--cite:204-->.<!--/claim:502-->

<!--claim:503-->Dust-obscured systems complicate counts<!--cite:102-->.<!--/claim:503-->

A page-level citation outside a claim should not be treated as claim evidence<!--cite:999-->.
`;

const edges = extractPaperClaimEdges(content);
assert.equal(
  JSON.stringify(edges.map((edge) => [edge.evidenceId, edge.claimId])),
  JSON.stringify([[101, 501], [102, 501], [204, 502], [102, 503]]),
  "Paper-to-claim edge extraction should preserve claim-scoped citation links and ignore page-only citations.",
);

const deck = buildPaperClaimFlightDeck(
  content,
  [
    {
      evidence_id: 101,
      author_year_key: "JWST2024",
      title: "JWST support synthesis",
      authors: ["A. Lens", "B. Halo"],
      year: 2024,
      arxiv_id: "2401.00101",
      url: "https://example.org/jwst-support",
      summary: "Supportive paper linked to one claim.",
    },
    {
      evidence_id: 102,
      author_year_key: "Dust2025",
      title: "Dust-obscured counter survey",
      authors: ["C. Dust", "D. Survey", "E. Model"],
      year: 2025,
      doi: "10.1234/dust.counter",
      url: "https://example.org/dust-counter",
      summary: "Counter-pressure paper linked to two claims.",
    },
    {
      evidence_id: 204,
      author_year_key: "Halo2022",
      title: "Halo assembly support sample",
      authors: "Halo Collaboration",
      year: 2022,
      url: null,
      summary: null,
    },
    {
      evidence_id: 999,
      author_year_key: "PageOnly2020",
      title: "Page-level source without claim edge",
      authors: [],
      year: 2020,
      url: "https://example.org/page-only",
    },
  ],
  {
    sections: [
      {
        title: "Early assembly",
        claims: [
          { id: 501, text: "Massive galaxies assembled early.", trust_level: "challenged", evidence_count: 4, con_count: 2 },
          { id: 502, text: "Minor mergers add stellar halos.", trust_level: "accepted", evidence_count: 3, con_count: 0 },
          { id: 503, text: "Dust-obscured systems complicate counts.", trust_level: "debated", evidence_count: 2, con_count: 1 },
        ],
      },
    ],
  },
  [501, 502, 503],
  "galaxy-evolution-v2",
);

assert.equal(deck.totalPapers, 4);
assert.equal(deck.linkedPapers, 3);
assert.equal(deck.unmappedPapers, 1);
assert.equal(deck.linkedClaims, 3);
assert.equal(deck.hasFlightDeck, true);
assert.equal(deck.headline, "3 papers linked to 3 visible claims");
assert.match(deck.summary, /paper-to-claim navigation/i);
assert.match(deck.summary, /not a final verdict/i);
assert.equal(deck.items[0].evidenceId, 102);
assert.equal(deck.items[0].paperLabel, "Dust2025");
assert.equal(deck.items[0].title, "Dust-obscured counter survey");
assert.equal(deck.items[0].byline, "C. Dust, D. Survey et al. · 2025");
assert.equal(deck.items[0].locator, "DOI:10.1234/dust.counter");
assert.equal(deck.items[0].claimCount, 2);
assert.equal(deck.items[0].counterPressureClaims, 2);
assert.equal(deck.items[0].rankLabel, "2 claim links · 2 with counter pressure");
assert.equal(deck.items[0].sourceIndexHref, "/wiki/galaxy-evolution-v2/sources");
assert.equal(deck.items[0].externalHref, "https://example.org/dust-counter");
assert.equal(
  JSON.stringify(deck.items[0].claimLinks.map((link) => [link.claimId, link.trustLevel, link.href, link.sectionLabel])),
  JSON.stringify([
    [501, "challenged", "#claim-501", "Early assembly"],
    [503, "debated", "#claim-503", "Early assembly"],
  ]),
);
assert.equal(deck.items[0].claimLinks[0].claimText, "Massive galaxies assembled early.");
assert.equal(deck.items[1].evidenceId, 101, "single challenged-claim paper should outrank neutral support-only paper.");
assert.equal(deck.items[2].evidenceId, 204);
assert.equal(deck.items[2].locator, "External source link unavailable");
assert.equal(deck.items[2].summary, "No abstract or summary has been published for this source yet.");

const emptyDeck = buildPaperClaimFlightDeck("No claim-scoped citations", [], { sections: [] }, [], "");
assert.equal(emptyDeck.hasFlightDeck, false);
assert.equal(emptyDeck.headline, "No paper-to-claim links mapped yet");
assert.equal(emptyDeck.summary, "Claim-scoped paper links will appear here once citations are mapped to visible claims.");

const clientSource = fs.readFileSync(clientPath, "utf8");
assert.match(clientSource, /from "\.\/paperClaimFlightDeck"/, "WikiPageClient should use the paper-to-claim flight deck helper.");
assert.match(clientSource, /buildPaperClaimFlightDeck\(/, "WikiPageClient should derive the flight deck from page content, citations, and claims.");
assert.match(clientSource, /data-testid="paper-claim-flight-deck"/, "Wiki page should expose a stable paper-to-claim flight deck section.");
assert.match(clientSource, /data-testid="paper-claim-flight-card"/, "Flight deck should render paper cards with stable markers.");
assert.match(clientSource, /data-testid="paper-claim-flight-claim-link"/, "Flight deck paper cards should link back to visible claim anchors.");
assert.match(clientSource, /data-testid="paper-claim-open-paper"/, "Flight deck should preserve external paper links when present.");
assert.match(clientSource, /data-testid="paper-claim-source-index-link"/, "Flight deck should link to the source index for the page.");
assert.match(clientSource, /Paper-to-claim flight deck/, "Flight deck should use explicit visible product copy.");
assert.match(clientSource, /not a final verdict/, "Flight deck should avoid implying truth adjudication.");
assert.match(clientSource, /on this page only/, "Flight deck should visibly scope the paper footprint to the current page only.");
assert.match(clientSource, /aria-describedby=\{paperClaimFlightDeckDescriptionId\}/, "Flight deck should describe its ranking criterion for assistive tech.");
assert.match(clientSource, /page\.content, citations, claims, renderedClaimIds, slug/, "Flight deck should be derived from existing frontend page state, not a new backend endpoint.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:paper-claim-flight-deck"], "node scripts/test-paper-claim-flight-deck.mjs");

const aggregateSource = fs.readFileSync(aggregatePath, "utf8");
assert.match(aggregateSource, /test:paper-claim-flight-deck/, "Wiki UX aggregate smoke should include the flight deck probe.");
assert.match(aggregateSource, /paper_claim_flight_deck_ok/, "Wiki UX aggregate smoke should expect the flight deck marker.");

console.log("paper_claim_flight_deck_ok");
