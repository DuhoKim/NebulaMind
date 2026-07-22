import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/trustVisibility.ts");
const clientPath = path.join(repoRoot, "src/app/wiki/[slug]/WikiPageClient.tsx");
const sourcesClientPath = path.join(repoRoot, "src/app/wiki/[slug]/sources/WikiSourcesClient.tsx");

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
  formatClaimTrustBadge,
  formatTrustSummaryLine,
  summarizeTrustClaims,
  trustVisibilityMeta,
} = module.exports;

assert.equal(typeof formatClaimTrustBadge, "function");
assert.equal(typeof formatTrustSummaryLine, "function");
assert.equal(typeof summarizeTrustClaims, "function");
assert.equal(typeof trustVisibilityMeta, "function");

const claimsPayload = {
  sections: [
    {
      name: "Trust-bearing claims",
      claims: [
        { id: 2929, text: "Internal AGN feedback", trust_level: "consensus", evidence_count: 36, con_count: 0 },
        { id: 2930, text: "Gas removal", trust_level: "consensus", evidence_count: 18, con_count: 0 },
        { id: 2931, text: "Mass and environment", trust_level: "debated", evidence_count: 16, con_count: 1 },
        { id: 2931, text: "Duplicate should not double count", trust_level: "debated", evidence_count: 16, con_count: 1 },
      ],
    },
  ],
};

const summary = summarizeTrustClaims(claimsPayload);
assert.equal(summary.totalClaims, 3);
assert.equal(summary.totalSources, 70);
assert.equal(summary.levels.consensus.claims, 2);
assert.equal(summary.levels.consensus.sources, 54);
assert.equal(summary.levels.debated.claims, 1);
assert.equal(summary.levels.debated.sources, 16);
assert.match(formatTrustSummaryLine(summary), /3 trust-bearing claims/i);
assert.match(formatTrustSummaryLine(summary), /2 consensus/i);
assert.match(formatTrustSummaryLine(summary), /1 debated/i);
assert.match(formatTrustSummaryLine(summary), /70 paper-source links/i);
assert.equal(formatClaimTrustBadge({ trust_level: "consensus", evidence_count: 36 }), "Consensus · 36 sources");
assert.equal(formatClaimTrustBadge({ trust_level: "debated", evidence_count: 1 }), "Debated · 1 source");
assert.equal(trustVisibilityMeta("challenged").icon, "!");

const clientSource = fs.readFileSync(clientPath, "utf8");
const sourcesClientSource = fs.readFileSync(sourcesClientPath, "utf8");
assert.match(clientSource, /from "\.\/trustVisibility"/);
assert.match(clientSource, /Page trust snapshot/);
assert.match(clientSource, /Provenance-gated claim layer/);
assert.match(clientSource, /formatClaimTrustBadge/);
assert.match(clientSource, /data-testid="trust-summary-panel"/);
assert.match(clientSource, /data-testid="claim-trust-badge"/);

// Phase 1 safety/reader-trust contracts for Galaxy V2.
assert.doesNotMatch(
  clientSource,
  /fetch\(`\/api\/pages\/\$\{slug\}\/health`\)/,
  "public wiki page must not auto-fetch the writing /health GET endpoint on load",
);
assert.match(
  clientSource,
  /p\?\.health_score/,
  "health badge should degrade from the already-read page payload instead of calling /health",
);
assert.match(
  clientSource,
  /\/api\/research\/ideas\/\$\{slug\}\?per_page=100/,
  "ideas loading should fall back to the legacy read-only research ideas endpoint",
);
assert.match(
  clientSource,
  /if \(!response\.ok\)/,
  "edit proposal submission must check response.ok before reporting success",
);
assert.doesNotMatch(clientSource, /Each sentence is sourced from a published paper/);
assert.match(clientSource, /Highlighted claims are linked to paper evidence/);
assert.doesNotMatch(sourcesClientSource, /No source records found for this page\./);
assert.match(sourcesClientSource, /claim evidence/i);

console.log("wiki_trust_visibility_smoke_ok");
