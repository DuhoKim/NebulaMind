import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/sources/evidenceTriageStudio.ts");
const sourcesClientPath = path.join(repoRoot, "src/app/wiki/[slug]/sources/WikiSourcesClient.tsx");
const fixtureSourcesPagePath = path.join(repoRoot, "src/app/wiki/source-trace-browser-fixture/sources/page.tsx");
const packagePath = path.join(repoRoot, "package.json");
const aggregatePath = path.join(repoRoot, "scripts/test-wiki-ux-smoke.mjs");

assert.ok(fs.existsSync(helperPath), "Evidence triage studio helper should live beside the wiki sources client.");

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

const { buildEvidenceTriageStudioDeck, normalizeTriageLane, buildEvidenceTriageQueueView } = module.exports;
assert.equal(typeof buildEvidenceTriageStudioDeck, "function");
assert.equal(typeof normalizeTriageLane, "function");
assert.equal(typeof buildEvidenceTriageQueueView, "function", "Triage queue safety view should be testable outside React.");
assert.equal(normalizeTriageLane({ tone: "counter", trustLevel: "challenged", votesDisagree: 2 }), "needs_adjudication");
assert.equal(normalizeTriageLane({ tone: "support", trustLevel: "accepted", votesDisagree: 0 }), "ready_to_review");
assert.equal(normalizeTriageLane({ tone: "neutral", trustLevel: "unverified", votesDisagree: 0 }), "needs_source");

const deck = buildEvidenceTriageStudioDeck({
  sources: [
    { id: 1, source_tier: "claim", claim_id: 7101, trust_level_snapshot: "debated", evidence_count_snapshot: 2, representative_arxiv_id: "2606.990101", flagged: false, attribution: "Debated claim source" },
    { id: 2, source_tier: "ai_estimate", claim_id: null, trust_level_snapshot: null, evidence_count_snapshot: null, representative_arxiv_id: null, flagged: true, reason: "No peer-reviewed source linked", attribution: "AI estimate" },
  ],
  citations: [
    { evidence_id: 990101, author_year_key: "Fixture2026", title: "Cross-page fixture", arxiv_id: "2606.990101", url: "https://example.org/paper" },
  ],
  crossPageFootprints: [
    {
      schema_version: "cross_page_paper_footprint.v2",
      paper: { arxiv_id: "9999.00001", title: "Future schema" },
      pages: [],
    },
    {
      schema_version: "cross_page_paper_footprint.v1",
      paper: { arxiv_id: "2606.990101", title: "Cross-page fixture", author_year_key: "Fixture2026" },
      page_count: 2,
      claim_count: 3,
      evidence_count: 3,
      tone_counts: { support: 2, counter: 1, neutral: 0 },
      trust_counts: { accepted: 1, challenged: 1, debated: 1 },
      pages: [
        {
          slug: "early-galaxies",
          title: "Early Galaxies",
          claim_count: 2,
          support_count: 2,
          counter_count: 0,
          claims: [
            { claim_id: 7101, claim_text: "Massive galaxies assembled early.", trust_level: "debated", tone: "support", href: "/wiki/early-galaxies#claim-7101", votes_agree: 1, votes_disagree: 0 },
            { claim_id: 7102, claim_text: "Minor mergers add halos.", trust_level: "accepted", tone: "support", href: "/wiki/early-galaxies#claim-7102", votes_agree: 0, votes_disagree: 0 },
          ],
        },
        {
          slug: "dust-obscured-galaxies",
          title: "Dust-obscured Galaxies",
          claim_count: 1,
          support_count: 0,
          counter_count: 1,
          claims: [
            { claim_id: 7201, claim_text: "Dust changes counts.", trust_level: "challenged", tone: "counter", href: "/wiki/dust-obscured-galaxies#claim-7201", votes_agree: 0, votes_disagree: 2 },
          ],
        },
      ],
    },
  ],
});

assert.equal(deck.hasTriageSignal, true);
assert.equal(deck.items.length, 4, "Three footprint claim rows plus one flagged source should be queued.");
assert.equal(deck.laneCounts.needs_adjudication, 2);
assert.equal(deck.laneCounts.ready_to_review, 1);
assert.equal(deck.laneCounts.needs_source, 1);
assert.equal(deck.items[0].lane, "needs_adjudication", "Counter-pressure or challenged rows should sort first.");
assert.equal(deck.items[0].paperLabel, "Fixture2026");
assert.equal(deck.items[0].actionLabel, "Adjudicate counter-pressure");
assert.match(deck.items[0].reasonText, /counter|challenged|disagree/i);
assert.match(deck.summary, /2 adjudication/i);
assert.match(deck.scopeCaveat, /review queue, not a final verdict/i);
assert.equal(deck.items.some((item) => item.paperLabel === "Future schema"), false, "Unknown schemas should not enter the triage queue.");

const pagedView = buildEvidenceTriageQueueView(deck, { laneFilter: "all", page: 0, pageSize: 2 });
assert.equal(pagedView.totalCount, 4);
assert.equal(pagedView.filteredCount, 4);
assert.equal(pagedView.visibleItems.length, 2, "Queue view should page long triage queues instead of silently slicing.");
assert.equal(pagedView.pageCount, 2);
assert.equal(pagedView.currentPage, 0);
assert.equal(pagedView.hasOverflow, true);
assert.match(pagedView.overflowDisclosure, /Showing 1-2 of 4 triage items/i);
assert.match(pagedView.overflowDisclosure, /paginated for review safety/i);

const adjudicationView = buildEvidenceTriageQueueView(deck, { laneFilter: "needs_adjudication", page: 0, pageSize: 1 });
assert.equal(adjudicationView.filteredCount, 2);
assert.equal(adjudicationView.hiddenByFilterCount, 2);
assert.equal(adjudicationView.visibleItems.every((item) => item.lane === "needs_adjudication"), true);
assert.match(adjudicationView.overflowDisclosure, /Needs adjudication/i);
assert.match(adjudicationView.overflowDisclosure, /2 hidden by the active lane filter/i);

const emptyFilteredView = buildEvidenceTriageQueueView(deck, { laneFilter: "needs_source", page: 3, pageSize: 6 });
assert.equal(emptyFilteredView.currentPage, 0, "Out-of-range requested pages should clamp safely.");
assert.equal(emptyFilteredView.visibleItems.length, 1);

const emptyDeck = buildEvidenceTriageStudioDeck({ sources: [], citations: [], crossPageFootprints: [] });
assert.equal(emptyDeck.hasTriageSignal, false);
assert.match(emptyDeck.summary, /No evidence triage signals/i);

const clientSource = fs.readFileSync(sourcesClientPath, "utf8");
assert.match(clientSource, /buildEvidenceTriageStudioDeck/, "Sources page should derive an evidence triage studio deck.");
assert.match(clientSource, /buildEvidenceTriageQueueView/, "Sources page should use the tested queue view for lane filters and pagination.");
assert.match(clientSource, /data-testid="evidence-triage-studio"/, "Sources page should expose a stable evidence triage studio section.");
assert.match(clientSource, /data-testid="evidence-triage-card"/, "Sources page should render stable triage cards.");
assert.match(clientSource, /data-testid="evidence-triage-lane-chip"/, "Triage lanes should have stable chips.");
assert.match(clientSource, /data-testid="evidence-triage-filter"/, "Triage lanes should have simple filter buttons.");
assert.match(clientSource, /aria-pressed=\{activeTriageLaneFilter === filter\.key\}/, "Lane filters should expose pressed state to assistive tech.");
assert.match(clientSource, /data-testid="evidence-triage-overflow-disclosure"/, "Triage queue should disclose truncation\/pagination instead of silently slicing.");
assert.match(clientSource, /data-testid="evidence-triage-page-control"/, "Triage queue should expose page controls when rows overflow.");
assert.match(clientSource, /data-testid="evidence-triage-action-link"/, "Triage cards should link to claim/page evidence context.");
assert.match(clientSource, /review queue, not a final verdict/i, "Triage surface should preserve truth-framing copy.");
assert.match(clientSource, /No labels are written/i, "Triage surface should be explicit that it is read-only.");
assert.match(clientSource, /aria-label=\{`Review \$\{item\.claimLabel\}/, "Action links should include explicit accessible review context.");

const fixtureSourcesSource = fs.readFileSync(fixtureSourcesPagePath, "utf8");
assert.match(fixtureSourcesSource, /source-trace-browser-fixture/, "Static source fixture should remain deterministic.");
assert.match(fixtureSourcesSource, /challenged/, "Static source fixture should include an adjudication-lane claim.");
assert.match(fixtureSourcesSource, /flagged: true/, "Static source fixture should include a needs-source row.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:evidence-triage-studio"], "node scripts/test-evidence-triage-studio.mjs");

const aggregateSource = fs.readFileSync(aggregatePath, "utf8");
assert.match(aggregateSource, /test:evidence-triage-studio/, "Wiki UX aggregate smoke should include the evidence triage probe.");
assert.match(aggregateSource, /evidence_triage_studio_ok/, "Wiki UX aggregate smoke should expect the evidence triage marker.");

console.log("evidence_triage_studio_ok");
