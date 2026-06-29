import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/papers/globalPaperDirectory.ts");
const clientPath = path.join(repoRoot, "src/app/wiki/papers/GlobalPaperDirectoryClient.tsx");
const pagePath = path.join(repoRoot, "src/app/wiki/papers/page.tsx");
const fixturePath = path.join(repoRoot, "src/app/wiki/papers/fixture/page.tsx");
const wikiIndexPath = path.join(repoRoot, "src/app/wiki/page.tsx");
const packagePath = path.join(repoRoot, "package.json");
const aggregatePath = path.join(repoRoot, "scripts/test-wiki-ux-smoke.mjs");

assert.ok(fs.existsSync(helperPath), "Global paper directory helper should live at src/app/wiki/papers/globalPaperDirectory.ts");

const helperSource = fs.readFileSync(helperPath, "utf8");
const compiled = ts.transpileModule(helperSource, {
  compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2019, strict: true },
  fileName: helperPath,
});
const module = { exports: {} };
vm.runInNewContext(compiled.outputText, { module, exports: module.exports, require }, { filename: helperPath });

const { buildGlobalPaperDirectoryDeck, normalizeGlobalPaperTriageStatus } = module.exports;
assert.equal(typeof buildGlobalPaperDirectoryDeck, "function");
assert.equal(typeof normalizeGlobalPaperTriageStatus, "function");
assert.equal(normalizeGlobalPaperTriageStatus({ counterCount: 1, trustCounts: {} }), "needs_adjudication");
assert.equal(normalizeGlobalPaperTriageStatus({ counterCount: 0, trustCounts: { challenged: 1 } }), "needs_adjudication");
assert.equal(normalizeGlobalPaperTriageStatus({ counterCount: 0, trustCounts: { accepted: 1 }, hasStableIdentifier: false }), "needs_source");
assert.equal(normalizeGlobalPaperTriageStatus({ counterCount: 0, trustCounts: { accepted: 1 }, hasStableIdentifier: true }), "ready_to_review");

const payload = {
  schema_version: "global_paper_directory.v1",
  query: "",
  limit: 25,
  total_papers: 3,
  result_count: 3,
  scope: {
    label: "global paper directory",
    caveat: "Across indexed wiki evidence rows; directory/search, not a final verdict. No labels are written.",
  },
  items: [
    {
      paper: {
        evidence_id: 990101,
        arxiv_id: "2606.990101",
        doi: null,
        url: "https://example.org/counter-paper",
        title: "Counter-pressure directory fixture",
        authors: ["NebulaMind Fixture Harness"],
        year: 2026,
        summary: "A fixture paper with counter-pressure across wiki pages.",
        author_year_key: "Harness2026",
      },
      page_count: 2,
      claim_count: 3,
      evidence_count: 3,
      tone_counts: { support: 2, counter: 1, neutral: 0 },
      trust_counts: { accepted: 1, challenged: 1, debated: 1 },
      triage_status: "needs_adjudication",
      impact_label: "2 pages · 3 claims · 1 countering",
      pages: [
        { slug: "dust-obscured-galaxies", title: "Dust-obscured Galaxies", href: "/wiki/dust-obscured-galaxies", claim_count: 1, evidence_count: 1, support_count: 0, counter_count: 1, neutral_count: 0 },
        { slug: "early-galaxies", title: "Early Galaxies", href: "/wiki/early-galaxies", claim_count: 2, evidence_count: 2, support_count: 2, counter_count: 0, neutral_count: 0 },
      ],
    },
    {
      paper: {
        evidence_id: 990102,
        arxiv_id: "2606.123456",
        doi: null,
        url: "https://example.org/ready-paper",
        title: "Synthesis-ready directory fixture",
        authors: ["Ready Reviewer"],
        year: 2025,
        summary: "A supporting fixture paper.",
        author_year_key: "Reviewer2025",
      },
      page_count: 1,
      claim_count: 1,
      evidence_count: 1,
      tone_counts: { support: 1, counter: 0, neutral: 0 },
      trust_counts: { accepted: 1 },
      triage_status: "ready_to_review",
      impact_label: "1 page · 1 claim · 0 countering",
      pages: [
        { slug: "stellar-halos", title: "Stellar Halos", href: "/wiki/stellar-halos", claim_count: 1, evidence_count: 1, support_count: 1, counter_count: 0, neutral_count: 0 },
      ],
    },
    {
      paper: {
        evidence_id: 990103,
        arxiv_id: null,
        doi: null,
        url: null,
        title: "Unindexed source gap fixture",
        authors: [],
        year: null,
        summary: null,
        author_year_key: "Unindexed source gap fixture",
      },
      page_count: 1,
      claim_count: 1,
      evidence_count: 1,
      tone_counts: { support: 0, counter: 0, neutral: 1 },
      trust_counts: { unverified: 1 },
      triage_status: "needs_source",
      impact_label: "1 page · 1 claim · 0 countering",
      pages: [
        { slug: "source-gaps", title: "Source Gaps", href: "/wiki/source-gaps", claim_count: 1, evidence_count: 1, support_count: 0, counter_count: 0, neutral_count: 1 },
      ],
    },
  ],
};

const deck = buildGlobalPaperDirectoryDeck(payload);
assert.equal(deck.hasResults, true);
assert.equal(deck.paperCount, 3);
assert.equal(deck.resultCount, 3);
assert.equal(deck.totalPapers, 3);
assert.equal(deck.counterCount, 1);
assert.match(deck.summary, /3 papers/i);
assert.match(deck.scopeCaveat, /not a final verdict/i);
assert.equal(deck.items[0].paperLabel, "Harness2026", "Counter-pressure papers should sort first.");
assert.equal(deck.items[0].statusLabel, "Needs adjudication");
assert.match(deck.items[0].accessibleSummary, /2 pages, 3 claims, 1 countering/i);
assert.equal(deck.items[0].footprintHref, "/wiki/dust-obscured-galaxies/sources");
assert.equal(deck.items[0].profileHref, "/wiki/papers/arxiv%3A2606.990101");
assert.equal(deck.items[1].statusLabel, "Needs source");

const filteredDeck = buildGlobalPaperDirectoryDeck(payload, "stellar");
assert.equal(filteredDeck.items.length, 1);
assert.equal(filteredDeck.items[0].paperLabel, "Reviewer2025");
assert.match(filteredDeck.summary, /1 paper matching “stellar”/i);

const emptyDeck = buildGlobalPaperDirectoryDeck({ ...payload, items: [], total_papers: 0, result_count: 0 }, "missing");
assert.equal(emptyDeck.hasResults, false);
assert.match(emptyDeck.emptyMessage, /No indexed papers match “missing”/i);

const truncatedDeck = buildGlobalPaperDirectoryDeck({ ...payload, items: payload.items.slice(0, 1), result_count: 1, total_papers: 3 });
assert.match(truncatedDeck.truncationDisclosure, /Showing 1 of 3 indexed papers/i);
assert.match(truncatedDeck.truncationDisclosure, /Refine search/i);

const clientSource = fs.readFileSync(clientPath, "utf8");
assert.match(clientSource, /data-testid="global-paper-directory"/, "Global paper directory should expose a stable section marker.");
assert.match(clientSource, /data-testid="global-paper-search-input"/, "Search input should have a stable selector.");
assert.match(clientSource, /data-testid="global-paper-search-submit"/, "Search submit should have a stable selector.");
assert.match(clientSource, /data-testid="global-paper-card"/, "Paper cards should have a stable selector.");
assert.match(clientSource, /data-testid="global-paper-profile-link"/, "Directory cards should link directly to paper profiles.");
assert.match(clientSource, /data-testid="global-paper-footprint-link"/, "Cards should link to wiki footprint context.");
assert.match(clientSource, /data-testid="global-paper-scope-caveat"/, "Truth-framing caveat should be rendered.");
assert.match(clientSource, /data-testid="global-paper-truncation-disclosure"/, "Limited directory responses should disclose hidden matching papers.");
assert.match(clientSource, /not a final verdict/i, "Directory copy should avoid adjudication language.");
assert.match(clientSource, /No labels are written/i, "Directory should be explicit that it is read-only.");
assert.match(clientSource, /aria-label=\{item\.accessibleSummary\}/, "Paper cards should expose count/status context to assistive tech.");
assert.match(clientSource, /fetch\(`\/api\/pages\/paper-directory/, "Client should fetch the read-only paper directory endpoint.");

assert.ok(fs.existsSync(pagePath), "Global paper directory page route should exist.");
assert.ok(fs.existsSync(fixturePath), "Global paper directory fixture route should exist for deterministic route/chunk probes.");
const fixtureSource = fs.readFileSync(fixturePath, "utf8");
assert.match(fixtureSource, /global_paper_directory\.v1/, "Fixture should carry production-like v1 payload.");
assert.match(fixtureSource, /Counter-pressure directory fixture/, "Fixture should include a counter-pressure paper.");

const wikiIndexSource = fs.readFileSync(wikiIndexPath, "utf8");
assert.match(wikiIndexSource, /href="\/wiki\/papers"/, "Wiki index should link to the global paper directory.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:global-paper-directory"], "node scripts/test-global-paper-directory.mjs");

const aggregateSource = fs.readFileSync(aggregatePath, "utf8");
assert.match(aggregateSource, /test:global-paper-directory/, "Wiki UX aggregate smoke should include the global paper directory probe.");
assert.match(aggregateSource, /global_paper_directory_ok/, "Wiki UX aggregate smoke should expect the global paper directory marker.");

console.log("global_paper_directory_ok");
