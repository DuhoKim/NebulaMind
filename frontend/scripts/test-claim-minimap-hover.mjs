import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/claimMiniMapHover.ts");
const clientPath = path.join(repoRoot, "src/app/wiki/[slug]/WikiPageClient.tsx");
const packagePath = path.join(repoRoot, "package.json");

assert.ok(fs.existsSync(helperPath), "claim mini-map hover helper should exist.");

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
  buildClaimMiniMapHover,
  formatClaimMiniMapSummary,
} = module.exports;

assert.equal(typeof buildClaimMiniMapHover, "function");
assert.equal(typeof formatClaimMiniMapSummary, "function");

const debated = buildClaimMiniMapHover({
  id: 2931,
  trust_level: "debated",
  evidence_count: 16,
  con_count: 1,
});
assert.equal(debated.eyebrow, "Claim mini-map");
assert.equal(debated.totalSources, 16);
assert.equal(debated.supportCount, 15);
assert.equal(debated.counterCount, 1);
assert.equal(debated.unresolvedCount, 0);
assert.equal(debated.stance, "mostly supporting");
assert.equal(formatClaimMiniMapSummary(debated), "15 supporting · 1 countering · 0 unresolved");
assert.equal(debated.evidencePanelId, "claim-evidence-panel-2931");
assert.equal(debated.claimAnchorHref, "#claim-2931");
assert.equal(debated.primaryActionLabel, "Open full evidence map");
assert.equal(debated.secondaryActionLabel, "Jump to claim text");
assert.equal(
  JSON.stringify(debated.segments.map((segment) => [segment.kind, segment.count, segment.percent])),
  JSON.stringify([["support", 15, 94], ["counter", 1, 6], ["unresolved", 0, 0]]),
);

const explicit = buildClaimMiniMapHover({
  evidence_count: 10,
  pro_count: 6,
  con_count: 2,
  unresolved_count: 2,
});
assert.equal(explicit.supportCount, 6);
assert.equal(explicit.counterCount, 2);
assert.equal(explicit.unresolvedCount, 2);
assert.equal(explicit.stance, "mixed evidence");
assert.equal(formatClaimMiniMapSummary(explicit), "6 supporting · 2 countering · 2 unresolved");

const empty = buildClaimMiniMapHover({ evidence_count: 0, con_count: 0 });
assert.equal(empty.totalSources, 0);
assert.equal(empty.stance, "no mapped sources yet");
assert.equal(formatClaimMiniMapSummary(empty), "No evidence mini-map yet");

const clientSource = fs.readFileSync(clientPath, "utf8");
assert.match(clientSource, /from "\.\/claimMiniMapHover"/, "WikiPageClient should use the claim mini-map helper.");
assert.match(clientSource, /data-testid="claim-mini-map-hover-card"/, "Claim badges should expose a testable mini-map hover card.");
assert.match(clientSource, /Claim mini-map/, "Claim badge hover cards should visibly label the mini-map.");
assert.match(clientSource, /onMouseEnter=/, "Claim mini-maps should open on hover.");
assert.match(clientSource, /onFocus=/, "Claim mini-maps should open for keyboard focus.");
assert.match(clientSource, /aria-describedby=\{miniMapId\}/, "Claim badges should describe themselves with the hover card when present.");
assert.match(clientSource, /Click for full evidence map/, "Mini-map should tell users click opens the full evidence map.");
assert.match(clientSource, /data-testid="claim-mini-map-open-evidence-map"/, "Mini-map should include a cross-link button into the full evidence map.");
assert.match(clientSource, /data-testid="claim-mini-map-jump-to-claim"/, "Mini-map should include a cross-link back to the claim text anchor.");
assert.match(clientSource, /miniMap\.primaryActionLabel/, "Mini-map action copy should come from the helper contract.");
assert.match(clientSource, /miniMap\.claimAnchorHref/, "Mini-map should use the helper-provided claim text anchor link.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:claim-minimap-hover"], "node scripts/test-claim-minimap-hover.mjs");

console.log("claim_minimap_hover_ok");
