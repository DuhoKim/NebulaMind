import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

const frontendRoot = path.resolve(import.meta.dirname, "..");
const packagePath = path.join(frontendRoot, "package.json");
const browserSmokePath = path.join(frontendRoot, "scripts/test-wiki-stacked-popover-browser.mjs");
const fixturePagePath = path.join(frontendRoot, "src/app/wiki/source-trace-browser-fixture/page.tsx");
const fixtureApiPath = path.join(frontendRoot, "src/app/api/pages/source-trace-browser-fixture/route.ts");
const fixtureApiSurfacePath = path.join(frontendRoot, "src/app/api/pages/source-trace-browser-fixture/[surface]/route.ts");
const fixtureEvidenceApiPath = path.join(frontendRoot, "src/app/api/claims/990001/evidence/route.ts");
const fixtureDataPath = path.join(frontendRoot, "src/app/wiki/source-trace-browser-fixture/fixtureData.ts");
const clientPath = path.join(frontendRoot, "src/app/wiki/[slug]/WikiPageClient.tsx");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(
  packageJson.scripts["test:stacked-popover-browser-fixture"],
  "node scripts/test-stacked-popover-browser-fixture-contract.mjs",
  "package.json should expose the fixture contract test without adding it to the wiki UX aggregate allow-list.",
);
assert.equal(
  packageJson.scripts["smoke:wiki-stacked-popover-browser"],
  "node scripts/test-wiki-stacked-popover-browser.mjs",
  "stacked-popover browser smoke command should stay stable.",
);
assert.equal(
  packageJson.scripts["smoke:wiki-atlas-browser"],
  "WIKI_STACKED_POPOVER_ONLY=page-atlas-ranking node scripts/test-wiki-stacked-popover-browser.mjs",
  "package.json should expose a targeted atlas browser interaction smoke command.",
);
assert.equal(
  packageJson.scripts["smoke:wiki-paper-footprint-browser"],
  "WIKI_STACKED_POPOVER_ONLY=paper-footprint node scripts/test-wiki-stacked-popover-browser.mjs",
  "package.json should expose a targeted paper footprint modal browser smoke command.",
);

for (const filePath of [fixturePagePath, fixtureApiPath, fixtureApiSurfacePath, fixtureEvidenceApiPath, fixtureDataPath]) {
  assert.ok(fs.existsSync(filePath), `${path.relative(frontendRoot, filePath)} should exist for deterministic source-trace browser fixture coverage.`);
}

const browserSmoke = fs.readFileSync(browserSmokePath, "utf8");
assert.match(browserSmoke, /source-trace-browser-fixture/, "browser smoke should drive the deterministic source-trace fixture route.");
assert.ok(browserSmoke.includes("source-trace-trigger"), "browser smoke should query the source-trace trigger selector.");
assert.ok(browserSmoke.includes("source-trace-hover-card"), "browser smoke should query the source-trace hover-card selector.");
assert.match(browserSmoke, /SOURCE_TRACE_STACK_OK|source_trace_only/, "browser smoke output should expose a source-trace stack success marker.");
assert.match(browserSmoke, /sourceTraceOpen/, "browser smoke JSON should report sourceTraceOpen state.");
assert.match(browserSmoke, /panelOpen[\s\S]*true[\s\S]*sourceTraceOpen[\s\S]*false|sourceTraceOpen[\s\S]*false[\s\S]*panelOpen[\s\S]*true/, "first Escape source-trace assertion should require panel open and source trace closed.");
assert.match(browserSmoke, /page-atlas-ranking/, "browser smoke should include a page-atlas-ranking scenario.");
assert.ok(browserSmoke.includes("page-atlas-open-evidence-map"), "atlas browser smoke should click the ranked-row evidence map opener.");
assert.ok(browserSmoke.includes("page-contradiction-atlas-ranking"), "atlas browser smoke should wait for the page-level atlas section.");
assert.match(browserSmoke, /PAGE_ATLAS_BROWSER_OK|page_atlas_panel_closed_focus_returned/, "atlas browser smoke output should expose a page-atlas focus-return success marker.");
assert.match(browserSmoke, /activeTestId[\s\S]*page-atlas-open-evidence-map/, "atlas browser smoke should assert Escape returns focus to the atlas opener.");
assert.match(browserSmoke, /paper-footprint/, "browser smoke should include a paper-footprint scenario.");
assert.ok(browserSmoke.includes("paper-footprint-entry-button"), "paper footprint browser smoke should click the evidence-card footprint opener.");
assert.ok(browserSmoke.includes("paper-footprint-modal"), "paper footprint browser smoke should assert the modal mounts.");
assert.ok(browserSmoke.includes("paper-footprint-close"), "paper footprint browser smoke should assert modal close focus behavior.");
assert.match(browserSmoke, /PAPER_FOOTPRINT_BROWSER_OK|paper_footprint_modal_closed_panel_open/, "paper footprint browser smoke should expose a modal focus-return success marker.");

const fixturePageSource = fs.readFileSync(fixturePagePath, "utf8");
assert.match(fixturePageSource, /sourceTraceBrowserFixtureData/, "fixture page should pass deterministic data directly into the production wiki client.");
assert.match(fixturePageSource, /testOnlyFixtureSlug="source-trace-browser-fixture"/, "fixture route should use an explicitly test-only slug prop.");
assert.match(fixturePageSource, /testOnlyFixtureData=\{sourceTraceBrowserFixtureData\}/, "fixture page should not depend on /api rewrites for primary browser-smoke data.");

const fixtureDataSource = fs.readFileSync(fixtureDataPath, "utf8");
assert.match(fixtureDataSource, /satisfies WikiPageClientTestOnlyFixtureData/, "fixture data should type-check against the production wiki client fixture data contract.");
assert.match(fixtureDataSource, /source-trace-browser-fixture/, "fixture data should return the fixture slug.");
assert.match(fixtureDataSource, /<!--cite:990101,990102-->/, "fixture content should include deterministic citation markers, including nullable-shape coverage.");
assert.match(fixtureDataSource, /<!--claim:990001-->/, "fixture content should include a deterministic claim marker for the evidence panel.");
assert.match(fixtureDataSource, /con_count: 1/, "fixture claim should expose one counter-source so the page-level atlas ranking renders deterministically.");
assert.match(fixtureDataSource, /evidence_count: 2/, "fixture claim should expose at least two evidence links for source-lane ranking.");
assert.match(fixtureDataSource, /evidence_id: 990102/, "fixture data should include a second nullable citation shape for browser coverage.");
assert.match(fixtureDataSource, /summary: null/, "fixture nullable citation should exercise missing-summary source-trace rendering.");

const fixtureSurface = fs.readFileSync(fixtureApiSurfacePath, "utf8");
assert.match(fixtureSurface, /citations/, "fixture surface route should serve citations.");
assert.match(fixtureSurface, /990101/, "fixture citations should include the primary evidence id referenced by the citation marker.");
assert.match(fixtureSurface, /990102/, "fixture citations API helper should include the nullable evidence id referenced by the citation marker.");
assert.match(fixtureSurface, /claims/, "fixture surface route should serve claims.");
assert.match(fixtureSurface, /990001/, "fixture claims should include the claim id referenced by the claim marker.");
assert.match(fixtureSurface, /con_count: 1/, "fixture claims API should mirror the page-atlas counter-source fixture contract.");

const fixtureEvidence = fs.readFileSync(fixtureEvidenceApiPath, "utf8");
assert.match(fixtureEvidence, /990101/, "fixture evidence API should return evidence for the panel.");
assert.match(fixtureEvidence, /990102/, "fixture evidence API should include a second source lane for the atlas probe.");
assert.match(fixtureEvidence, /stance: "contradicting"|stance: "against"|stance: "challenge"/, "fixture evidence should include one countering stance so the atlas probe covers contradiction ranking.");
assert.match(fixtureEvidence, /source-trace fixture/i, "fixture evidence should be clearly labelled as deterministic fixture data.");

const clientSource = fs.readFileSync(clientPath, "utf8");
assert.match(clientSource, /testOnlyFixtureSlug\??:/, "WikiPageClient should accept an explicitly test-only fixture slug for static fixture routes.");
assert.match(clientSource, /testOnlyFixtureData\??:/, "WikiPageClient should accept explicitly test-only deterministic fixture data.");
assert.match(clientSource, /testOnlyFixtureSlug \?\? params/, "WikiPageClient should use the fixture slug before dynamic route params.");
assert.match(clientSource, /testOnlyFixtureData\?\.page/, "WikiPageClient should seed page state from deterministic fixture data.");
assert.match(clientSource, /if \(testOnlyFixtureData\?\.citations\) return;/, "WikiPageClient should skip citation fetches for deterministic fixture data.");

console.log("stacked_popover_browser_fixture_contract_ok");
