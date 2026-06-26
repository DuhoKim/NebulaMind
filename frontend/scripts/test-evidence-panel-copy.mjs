import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/evidencePanelCopy.ts");
const panelPath = path.join(repoRoot, "src/app/wiki/[slug]/DebateEvidencePanel.tsx");

assert.ok(fs.existsSync(helperPath), "Evidence panel copy helpers should live in evidencePanelCopy.ts.");

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
  buildEvidencePanelCopy,
  evidenceSide,
  formatLinkedPaperSourceCount,
} = module.exports;

assert.equal(typeof buildEvidencePanelCopy, "function");
assert.equal(typeof evidenceSide, "function");
assert.equal(typeof formatLinkedPaperSourceCount, "function");

assert.equal(evidenceSide("supports"), "support");
assert.equal(evidenceSide("strongly_challenges"), "counter");
assert.equal(evidenceSide("none"), "neutral");
assert.equal(formatLinkedPaperSourceCount(1), "1 linked paper source");
assert.equal(formatLinkedPaperSourceCount(36), "36 linked paper sources");

const neutralConsensus = Array.from({ length: 36 }, (_, id) => ({ id, stance: "none", status: "active" }));
const consensusCopy = buildEvidencePanelCopy(neutralConsensus, "consensus");
assert.equal(consensusCopy.total, 36);
assert.equal(consensusCopy.supportCount, 0);
assert.equal(consensusCopy.counterCount, 0);
assert.equal(consensusCopy.neutralCount, 36);
assert.equal(consensusCopy.hasDirectionalStance, false);
assert.equal(consensusCopy.directionalSplitLabel, "directional stance split not published");
assert.equal(
  consensusCopy.neutralOnlySummary,
  "36 linked paper sources are linked to this consensus claim; directional support/counter stance split is not published yet.",
);

const neutralDebated = Array.from({ length: 16 }, (_, id) => ({ id, stance: "none", status: "active" }));
const debatedCopy = buildEvidencePanelCopy(neutralDebated, "debated");
assert.equal(
  debatedCopy.neutralOnlySummary,
  "16 linked paper sources are linked to this debated claim; directional support/counter stance split is not published yet.",
);

const directionalCopy = buildEvidencePanelCopy([
  { id: 1, stance: "supports" },
  { id: 2, stance: "challenges" },
  { id: 3, stance: "none" },
], "debated");
assert.equal(directionalCopy.hasDirectionalStance, true);
assert.equal(directionalCopy.supportCount, 1);
assert.equal(directionalCopy.counterCount, 1);
assert.equal(directionalCopy.neutralCount, 1);
assert.equal(directionalCopy.neutralOnlySummary, null);
assert.equal(directionalCopy.directionalSplitLabel, "1 supporting · 1 countering");

const panelSource = fs.readFileSync(panelPath, "utf8");
assert.match(panelSource, /from "\.\/evidencePanelCopy"/, "DebateEvidencePanel should use shared copy helpers.");
assert.match(panelSource, /data-testid="evidence-panel-neutral-summary"/, "Neutral-only evidence state should have a testable summary.");
assert.match(panelSource, /Linked paper sources/, "Neutral-only evidence rows should be grouped under linked paper source copy.");
assert.match(panelSource, /total > 0 && evidenceCopy\.hasDirectionalStance/, "Directional support/counter counts should render only when directional stances exist.");

console.log("evidence_panel_copy_ok");
