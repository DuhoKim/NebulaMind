import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const frontendRoot = path.resolve(import.meta.dirname, "..");
const packagePath = path.join(frontendRoot, "package.json");
const queryHelperPath = path.join(frontendRoot, "src/app/wiki/papers/[paperId]/paperFootprintQuery.ts");
const panelPath = path.join(frontendRoot, "src/app/wiki/papers/[paperId]/PaperFootprintPanel.tsx");
const profileClientPath = path.join(frontendRoot, "src/app/wiki/papers/[paperId]/PaperProfileClient.tsx");
const fixturePath = path.join(frontendRoot, "src/app/wiki/papers/profile-fixture/page.tsx");
const aggregatePath = path.join(frontendRoot, "scripts/test-wiki-ux-smoke.mjs");

assert.ok(fs.existsSync(queryHelperPath), "Paper profile should have a pure paperFootprintQuery helper.");
assert.ok(fs.existsSync(panelPath), "Paper profile should have a dedicated PaperFootprintPanel component.");

const queryHelperSource = fs.readFileSync(queryHelperPath, "utf8");
const compiledQuery = ts.transpileModule(queryHelperSource, {
  compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2019, strict: true },
  fileName: queryHelperPath,
});
const queryModule = { exports: {} };
vm.runInNewContext(compiledQuery.outputText, { module: queryModule, exports: queryModule.exports, require }, { filename: queryHelperPath });
const { buildPaperFootprintQuery } = queryModule.exports;
assert.equal(typeof buildPaperFootprintQuery, "function", "Query helper should export buildPaperFootprintQuery.");
assert.equal(buildPaperFootprintQuery("arxiv:2606.990101", null), "arxiv_id=2606.990101");
assert.equal(buildPaperFootprintQuery("evidence:9201", null), "evidence_id=9201");
assert.equal(
  buildPaperFootprintQuery("doi:10.0000/example", { paper: { arxiv_id: "2606.25367", evidence_id: 29767 } }),
  "arxiv_id=2606.25367",
  "A resolved arXiv ID from the profile payload should win because paper-footprint accepts arxiv_id directly.",
);
assert.equal(
  buildPaperFootprintQuery("doi:10.0000/example", { paper: { evidence_id: 29767 } }),
  "evidence_id=29767",
  "Evidence ID should be the fallback for DOI/URL paper profiles because paper-footprint only accepts arxiv_id or evidence_id.",
);

const panelSource = fs.readFileSync(panelPath, "utf8");
assert.match(panelSource, /Cited across NebulaMind/, "Panel should expose the user-facing title.");
assert.match(panelSource, /data-testid="paper-footprint-panel"/, "Panel should expose a stable wrapper selector.");
assert.match(panelSource, /data-testid="paper-footprint-summary"/, "Panel should expose a stable summary selector.");
assert.match(panelSource, /data-testid="paper-footprint-page-card"/, "Panel should render page cards with a stable selector.");
assert.match(panelSource, /data-testid="paper-footprint-claim-row"/, "Panel should render linked claim rows with a stable selector.");
assert.match(panelSource, /not a final verdict/i, "Panel copy should preserve truth-framing.");
assert.match(panelSource, /No labels are written/i, "Panel should remain explicitly read-only.");
assert.match(panelSource, /buildCrossPagePaperFootprintDeck/, "Panel should reuse the existing paper-footprint deck helper.");

const profileClientSource = fs.readFileSync(profileClientPath, "utf8");
assert.match(profileClientSource, /\/api\/pages\/paper-footprint\?/, "Paper profile client should consume the read-only paper-footprint endpoint.");
assert.match(profileClientSource, /buildPaperFootprintQuery/, "Paper profile client should derive arxiv_id/evidence_id safely.");
assert.match(profileClientSource, /testOnlyFootprintData/, "Paper profile client should allow deterministic no-auth footprint fixtures.");
assert.match(profileClientSource, /response\.status === 404/, "Missing paper-footprint rows should render the graceful empty state, not an error+retry state.");
assert.match(profileClientSource, /setFootprintPayload\(null\)/, "404/missing footprint handling should clear payload without writing labels or throwing.");
assert.match(panelSource, /data-testid="paper-footprint-error"/, "Paper footprint fetch failures should have a stable error selector.");
assert.match(panelSource, /data-testid="paper-footprint-retry"/, "Paper footprint fetch failures should expose a stable retry affordance.");

const fixtureSource = fs.readFileSync(fixturePath, "utf8");
assert.match(fixtureSource, /cross_page_paper_footprint\.v1/, "Paper profile fixture should include a deterministic paper-footprint payload.");
assert.match(fixtureSource, /Cited across NebulaMind fixture/, "Fixture should include a title unique to the footprint panel.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:wiki-paper-footprint-panel"], "node scripts/test-wiki-paper-footprint-panel.mjs");

const aggregateSource = fs.readFileSync(aggregatePath, "utf8");
assert.match(aggregateSource, /test:wiki-paper-footprint-panel/, "Wiki UX aggregate should include the paper footprint panel probe.");
assert.match(aggregateSource, /wiki_paper_footprint_panel_ok/, "Wiki UX aggregate should expect the footprint panel marker.");

console.log("wiki_paper_footprint_panel_ok");
