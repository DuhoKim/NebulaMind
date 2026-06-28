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

const fixturePageSource = fs.readFileSync(fixturePagePath, "utf8");
assert.match(fixturePageSource, /sourceTraceBrowserFixtureData/, "fixture page should pass deterministic data directly into the production wiki client.");
assert.match(fixturePageSource, /testOnlyFixtureSlug="source-trace-browser-fixture"/, "fixture route should use an explicitly test-only slug prop.");
assert.match(fixturePageSource, /testOnlyFixtureData=\{sourceTraceBrowserFixtureData\}/, "fixture page should not depend on /api rewrites for primary browser-smoke data.");

const fixtureDataSource = fs.readFileSync(fixtureDataPath, "utf8");
assert.match(fixtureDataSource, /satisfies WikiPageClientTestOnlyFixtureData/, "fixture data should type-check against the production wiki client fixture data contract.");
assert.match(fixtureDataSource, /source-trace-browser-fixture/, "fixture data should return the fixture slug.");
assert.match(fixtureDataSource, /<!--cite:990101,990102-->/, "fixture content should include deterministic citation markers, including nullable-shape coverage.");
assert.match(fixtureDataSource, /<!--claim:990001-->/, "fixture content should include a deterministic claim marker for the evidence panel.");
assert.match(fixtureDataSource, /evidence_id: 990102/, "fixture data should include a second nullable citation shape for browser coverage.");
assert.match(fixtureDataSource, /summary: null/, "fixture nullable citation should exercise missing-summary source-trace rendering.");

const fixtureSurface = fs.readFileSync(fixtureApiSurfacePath, "utf8");
assert.match(fixtureSurface, /citations/, "fixture surface route should serve citations.");
assert.match(fixtureSurface, /990101/, "fixture citations should include the primary evidence id referenced by the citation marker.");
assert.match(fixtureSurface, /990102/, "fixture citations API helper should include the nullable evidence id referenced by the citation marker.");
assert.match(fixtureSurface, /claims/, "fixture surface route should serve claims.");
assert.match(fixtureSurface, /990001/, "fixture claims should include the claim id referenced by the claim marker.");

const fixtureEvidence = fs.readFileSync(fixtureEvidenceApiPath, "utf8");
assert.match(fixtureEvidence, /990101/, "fixture evidence API should return evidence for the panel.");
assert.match(fixtureEvidence, /source-trace fixture/i, "fixture evidence should be clearly labelled as deterministic fixture data.");

const clientSource = fs.readFileSync(clientPath, "utf8");
assert.match(clientSource, /testOnlyFixtureSlug\??:/, "WikiPageClient should accept an explicitly test-only fixture slug for static fixture routes.");
assert.match(clientSource, /testOnlyFixtureData\??:/, "WikiPageClient should accept explicitly test-only deterministic fixture data.");
assert.match(clientSource, /testOnlyFixtureSlug \?\? params/, "WikiPageClient should use the fixture slug before dynamic route params.");
assert.match(clientSource, /testOnlyFixtureData\?\.page/, "WikiPageClient should seed page state from deterministic fixture data.");
assert.match(clientSource, /if \(testOnlyFixtureData\?\.citations\) return;/, "WikiPageClient should skip citation fetches for deterministic fixture data.");

console.log("stacked_popover_browser_fixture_contract_ok");
