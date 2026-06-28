import assert from "node:assert/strict";
// Paired with test-evidence-panel-copy.mjs: copy probe locks helper semantics;
// this visual probe locks structural layout markers and helper-derived geometry.
// Keep expected strings inline so contract updates stay reviewable in PR diffs.
import { createHash } from "node:crypto";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const panelPath = path.join(repoRoot, "src/app/wiki/[slug]/DebateEvidencePanel.tsx");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/evidencePanelCopy.ts");
const packagePath = path.join(repoRoot, "package.json");

assert.ok(fs.existsSync(panelPath), "DebateEvidencePanel should exist for visual probing.");
assert.ok(fs.existsSync(helperPath), "Evidence panel copy helper should exist for visual probing.");

const panelSource = fs.readFileSync(panelPath, "utf8");
const helperSource = fs.readFileSync(helperPath, "utf8");
const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));

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
  buildEvidenceCardDensityMeta,
  buildEvidencePanelCopy,
  buildEvidenceVoteCockpitVisuals,
  buildEvidenceVoteSignal,
} = module.exports;

assert.equal(packageJson.scripts["test:evidence-panel-visual-probe"], "node scripts/test-evidence-panel-visual-probe.mjs");
assert.equal(typeof buildEvidenceCardDensityMeta, "function");
assert.equal(typeof buildEvidencePanelCopy, "function");
assert.equal(typeof buildEvidenceVoteSignal, "function");
assert.equal(typeof buildEvidenceVoteCockpitVisuals, "function");

function countOccurrences(source, needle) {
  return source.split(needle).length - 1;
}

const visualMarkers = [
  ["modal overlay dims background", /background: "rgba\(2,6,23,0\.58\)"/],
  ["overlay sits below panel", /zIndex: 139/],
  ["dialog sits above overlay", /zIndex: 140/],
  ["dialog has responsive width", /width: isNarrow \? "auto" : "min\(46rem, 94vw\)"/],
  ["dialog caps viewport height", /maxHeight: isNarrow \? "calc\(100vh - 4\.5rem\)" : "min\(38rem, 82vh\)"/],
  ["dialog scrolls internally", /overflowY: "auto"/],
  ["dialog root test id", /data-testid="evidence-panel-dialog"/],
  ["dialog stable fallback id", /const fallbackPanelId = useId\(\)/],
  ["dialog title single source", /const evidencePanelTitle = isContested \? "Debate map" : "Evidence map"/],
  ["dialog noun single source", /const evidencePanelNoun = isContested \? "debate map" : "evidence map"/],
  ["dialog labelled by visible heading", /aria-labelledby=\{evidencePanelHeadingId\}/],
  ["dialog described by keyboard hint", /aria-describedby=\{evidencePanelHintId\}/],
  ["dialog visible heading id", /id=\{evidencePanelHeadingId\}/],
  ["dialog keyboard hint id", /id=\{evidencePanelHintId\}/],
  ["dialog visible Escape hint", /Press Escape to close this \{evidencePanelNoun\}\./],
  ["header trust pill remains visible", /textTransform: "uppercase"[\s\S]*?\{trustLevel\}/],
  ["close button remains large enough", /width: "2\.75rem"[\s\S]*?height: "2\.75rem"/],
  ["neutral summary test id", /data-testid="evidence-panel-neutral-summary"/],
  ["vote signal root test id", /data-testid="evidence-vote-signal"/],
  ["vote cockpit visible headline", /Evidence vote cockpit/],
  ["vote segmented bar test id", /data-testid="evidence-vote-balance-bar"/],
  ["vote metric grid test id", /data-testid="evidence-vote-metric-grid"/],
  ["vote detail disclosure copy", /How counted votes map to the claim signal/],
  ["vote segment map consumed by panel", /voteVisuals\.segments\.map/],
  ["density card shell test id", /data-testid="evidence-card-density-shell"/],
  ["density metadata rail test id", /data-testid="evidence-card-density-rail"/],
  ["summary clamp test id", /data-testid="evidence-card-summary-clamp"/],
  ["summary clamp line count", /WebkitLineClamp: 3/],
  ["activity rail test id", /data-testid="evidence-card-activity-rail"/],
  ["quality toggle test id", /data-testid="evidence-card-score-toggle"/],
  ["quality toggle aria label", /aria-label=\{scoreOpen \? "Hide evidence quality breakdown" : "Show evidence quality breakdown"\}/],
  ["quality disclosure cue", /scoreOpen \? "▲" : "▼"/],
  ["supporting evidence column heading", />Supporting evidence</],
  ["countering evidence column heading", />Countering evidence</],
  ["neutral evidence group heading", />Neutral or unresolved</],
  ["two-column desktop evidence grid", /gridTemplateColumns: isNarrow \? "1fr" : "minmax\(0, 1fr\) minmax\(0, 1fr\)"/],
  ["linked element count line", /linked across \{totalElements\} claim element/],
];

for (const [label, pattern] of visualMarkers) {
  assert.match(panelSource, pattern, `Evidence panel visual marker missing: ${label}`);
}

assert.equal(countOccurrences(panelSource, 'data-testid="evidence-vote-signal"'), 1, "Vote cockpit root should remain singular.");
assert.equal(countOccurrences(panelSource, 'data-testid="evidence-vote-balance-bar"'), 1, "Vote balance bar should remain singular.");
assert.equal(countOccurrences(panelSource, 'data-testid="evidence-vote-metric-grid"'), 1, "Vote metric grid should remain singular.");
for (const marker of [
  'data-testid="evidence-card-density-shell"',
  'data-testid="evidence-card-density-rail"',
  'data-testid="evidence-card-summary-clamp"',
  'data-testid="evidence-card-activity-rail"',
]) {
  assert.equal(countOccurrences(panelSource, marker), 1, `${marker} should appear once in the EvidenceCard template.`);
}
assert.match(
  panelSource,
  /voteSignal\.verdict === "net_support"[\s\S]*?voteSignal\.verdict === "net_weakening"[\s\S]*?voteSignal\.verdict === "split"/,
  "Vote cockpit color ternary should still distinguish support, weakening, split, and fallback verdicts.",
);

const trustBlockingIndex = panelSource.indexOf("{statusMeta.trustBlocking && (");
const clampIndex = panelSource.indexOf("data-testid=\"evidence-card-summary-clamp\"");
const activityRailIndex = panelSource.indexOf("data-testid=\"evidence-card-activity-rail\"");
assert.ok(trustBlockingIndex >= 0, "Trust-blocking caution branch should exist.");
assert.ok(clampIndex >= 0, "Summary clamp branch should exist.");
assert.ok(activityRailIndex >= 0, "Activity rail branch should exist.");
assert.ok(trustBlockingIndex < clampIndex, "Trust-blocking caution should render before the clamped summary.");
assert.ok(trustBlockingIndex < activityRailIndex, "Trust-blocking caution should render before the compact activity rail.");

assert.ok(!panelSource.includes("undefined-heading") && !panelSource.includes("undefined-keyboard-hint"), "Dialog ARIA ids should never contain undefined.");
assert.ok(
  panelSource.indexOf("id={evidencePanelHintId}") < panelSource.indexOf("data-testid=\"evidence-vote-signal\""),
  "Evidence panel keyboard hint should stay near the header before the vote cockpit scan path.",
);

const voteSignalIndex = panelSource.indexOf("data-testid=\"evidence-vote-signal\"");
const evidenceGridIndex = panelSource.indexOf("Supporting evidence");
assert.ok(voteSignalIndex >= 0 && evidenceGridIndex >= 0 && voteSignalIndex < evidenceGridIndex, "Vote cockpit should render above the evidence-card grid.");

const sampleEvidence = [
  {
    id: 101,
    stance: "supports",
    votes_agree: 4,
    votes_disagree: 1,
    comments_count: 2,
    link_count: 3,
    quality_v2: 0.83,
  },
  {
    id: 102,
    stance: "challenges",
    votes_agree: 3,
    votes_disagree: 2,
    comments_count: 0,
    link_count: 1,
    quality_v2: 0.61,
  },
  {
    id: 103,
    stance: "none",
    votes_agree: 5,
    votes_disagree: 6,
    comments_count: 0,
    link_count: 0,
  },
];
const visualSnapshot = {
  supportDensity: buildEvidenceCardDensityMeta(sampleEvidence[0]),
  counterDensity: buildEvidenceCardDensityMeta(sampleEvidence[1]),
  neutralDensity: buildEvidenceCardDensityMeta(sampleEvidence[2]),
  neutralConsensusCopy: buildEvidencePanelCopy(Array.from({ length: 3 }, (_, id) => ({ id, stance: "none", status: "active" })), "consensus"),
  unvotedVisuals: buildEvidenceVoteCockpitVisuals(buildEvidenceVoteSignal([{ id: 104, stance: "supports", votes_agree: 0, votes_disagree: 0 }])),
  voteVisuals: buildEvidenceVoteCockpitVisuals(buildEvidenceVoteSignal(sampleEvidence)),
};

assert.equal(visualSnapshot.supportDensity.sideLabel, "supporting paper");
assert.equal(visualSnapshot.supportDensity.voteLabel, "4 support · 1 weakening");
assert.equal(visualSnapshot.supportDensity.activityLabel, "2 comments · 3 element links");
assert.equal(visualSnapshot.supportDensity.qualityLabel, "quality 83%");
assert.equal(visualSnapshot.counterDensity.sideLabel, "countering paper");
assert.equal(visualSnapshot.counterDensity.voteLabel, "2 support · 3 weakening");
assert.equal(visualSnapshot.neutralDensity.voteLabel, "0 support · 0 weakening · 11 unresolved");
assert.equal(visualSnapshot.neutralConsensusCopy.hasDirectionalStance, false);
assert.equal(visualSnapshot.neutralConsensusCopy.neutralOnlySummary, "3 linked paper sources are linked to this consensus claim; directional support/counter stance split is not published yet.");
assert.equal(visualSnapshot.unvotedVisuals.summary, "No counted evidence votes yet");
assert.equal(visualSnapshot.unvotedVisuals.segments.reduce((sum, segment) => sum + segment.percent, 0), 0);
assert.equal(visualSnapshot.voteVisuals.summary, "6 support votes · 4 weakening votes · 11 unresolved votes");
assert.equal(visualSnapshot.voteVisuals.dominantLabel, "unresolved votes dominate this cockpit");
assert.equal(
  JSON.stringify(visualSnapshot.voteVisuals.segments.map((segment) => [segment.kind, segment.count, segment.percent, segment.label])),
  JSON.stringify([
    ["support", 6, 29, "support"],
    ["weakening", 4, 19, "weakening"],
    ["unresolved", 11, 52, "unresolved"],
  ]),
);
assert.equal(visualSnapshot.voteVisuals.segments.length, 3);
assert.equal(visualSnapshot.voteVisuals.segments.reduce((sum, segment) => sum + segment.percent, 0), 100);

const visualContract = {
  markers: visualMarkers.map(([label]) => label),
  order: ["trust-blocking caution", "summary clamp", "vote cockpit", "evidence grid"],
  snapshot: visualSnapshot,
};
const fingerprint = createHash("sha256")
  .update(JSON.stringify(visualContract))
  .digest("hex")
  .slice(0, 12);

assert.equal(fingerprint, "3bfe8a2ef9cb", "Evidence panel visual contract fingerprint changed; review the visual probe snapshot before updating.");
console.log(`evidence_panel_visual_probe_ok ${fingerprint}`);
