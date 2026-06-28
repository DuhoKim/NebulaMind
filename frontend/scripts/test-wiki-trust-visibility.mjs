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
const panelPath = path.join(repoRoot, "src/app/wiki/[slug]/DebateEvidencePanel.tsx");

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
const renderedOnlySummary = summarizeTrustClaims(claimsPayload, new Set([2929, 2931]));
assert.equal(renderedOnlySummary.totalClaims, 2);
assert.equal(renderedOnlySummary.totalSources, 52);
assert.equal(renderedOnlySummary.levels.consensus.claims, 1);
assert.equal(renderedOnlySummary.levels.debated.claims, 1);
assert.equal(renderedOnlySummary.levels.consensus.sources, 36);
assert.equal(renderedOnlySummary.levels.debated.sources, 16);
assert.equal(formatClaimTrustBadge({ trust_level: "consensus", evidence_count: 36 }), "Consensus · 36 sources");
assert.equal(formatClaimTrustBadge({ trust_level: "debated", evidence_count: 1 }), "Debated · 1 source");
assert.equal(formatClaimTrustBadge({ trust_level: "debated", evidence_count: 16, con_count: 1 }), "Debated · 16 sources · 1 countering");
assert.equal(trustVisibilityMeta("challenged").icon, "!");

const clientSource = fs.readFileSync(clientPath, "utf8");
const panelSource = fs.readFileSync(panelPath, "utf8");
assert.match(clientSource, /from "\.\/trustVisibility"/);
assert.match(clientSource, /Page trust snapshot/);
assert.match(clientSource, /Provenance-gated claim layer/);
assert.match(clientSource, /formatClaimTrustBadge/);
assert.match(clientSource, /summarizeTrustClaims\(claims, renderedClaimIds\)/);
assert.match(clientSource, /data-testid="trust-summary-panel"/);
assert.match(clientSource, /data-testid="claim-trust-badge"/);
assert.match(clientSource, /aria-haspopup="dialog"/, "Trust chips should declare that they open an evidence dialog.");
assert.match(clientSource, /aria-expanded=\{open\}/, "Trust chips should expose their live evidence-dialog expanded state.");
assert.match(clientSource, /aria-controls=\{panelId\}/, "Trust chips should point assistive tech to the evidence dialog they open.");
assert.match(clientSource, /const evidencePanelId = claim\?\.id \? `claim-evidence-panel-\$\{claim\.id\}` : undefined/, "Claim annotations should derive a stable evidence-dialog id from the claim id.");
assert.match(clientSource, /panelId=\{evidencePanelId\}/, "The opened evidence dialog should receive the stable claim evidence panel id.");
assert.match(panelSource, /id=\{panelId\}/, "Evidence dialogs should expose the id referenced by aria-controls.");

console.log("wiki_trust_visibility_smoke_ok");
