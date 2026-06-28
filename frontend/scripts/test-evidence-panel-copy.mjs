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
  buildEvidenceCardDensityMeta,
  buildEvidencePanelCopy,
  buildEvidenceVoteCockpitVisuals,
  buildEvidenceVoteSignal,
  evidenceSide,
  formatLinkedPaperSourceCount,
} = module.exports;

assert.equal(typeof buildEvidenceCardDensityMeta, "function");
assert.equal(typeof buildEvidencePanelCopy, "function");
assert.equal(typeof buildEvidenceVoteCockpitVisuals, "function");
assert.equal(typeof buildEvidenceVoteSignal, "function");
assert.equal(typeof evidenceSide, "function");
assert.equal(typeof formatLinkedPaperSourceCount, "function");

assert.equal(evidenceSide("supports"), "support");
assert.equal(evidenceSide("strongly_challenges"), "counter");
assert.equal(evidenceSide("none"), "neutral");
assert.equal(formatLinkedPaperSourceCount(1), "1 linked paper source");
assert.equal(formatLinkedPaperSourceCount(36), "36 linked paper sources");

const denseMeta = buildEvidenceCardDensityMeta({
  stance: "supports",
  votes_agree: 4,
  votes_disagree: 1,
  comments_count: 2,
  link_count: 3,
  quality_v2: 0.83,
});
assert.equal(denseMeta.sideLabel, "supporting paper");
assert.equal(denseMeta.voteLabel, "4 support · 1 weakening");
assert.equal(denseMeta.activityLabel, "2 comments · 3 element links");
assert.equal(denseMeta.qualityLabel, "quality 83%");
assert.equal(denseMeta.hasActivity, true);

const quietMeta = buildEvidenceCardDensityMeta({ stance: "none", votes_agree: 0, votes_disagree: 0 });
assert.equal(quietMeta.sideLabel, "linked paper");
assert.equal(quietMeta.voteLabel, "no counted votes");
assert.equal(quietMeta.activityLabel, "no comments or element links yet");
assert.equal(quietMeta.qualityLabel, null);
assert.equal(quietMeta.hasActivity, false);

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

const voteSignal = buildEvidenceVoteSignal([
  { id: 1, stance: "supports", votes_agree: 4, votes_disagree: 1 },
  { id: 2, stance: "challenges", votes_agree: 3, votes_disagree: 2 },
  { id: 3, stance: "none", votes_agree: 5, votes_disagree: 6 },
]);
assert.equal(voteSignal.supportVotes, 6);
assert.equal(voteSignal.weakeningVotes, 4);
assert.equal(voteSignal.unresolvedVotes, 11);
assert.equal(voteSignal.totalVotes, 21);
assert.equal(voteSignal.netSupport, 2);
assert.equal(voteSignal.headline, "Counted vote signal: 6 support · 4 weakening · 11 unresolved");
assert.equal(voteSignal.verdict, "net_support");
assert.equal(voteSignal.verdictLabel, "Net +2 support signal");
assert.match(voteSignal.detail, /Countering evidence flips the meaning/);
const voteVisuals = buildEvidenceVoteCockpitVisuals(voteSignal);
assert.equal(voteVisuals.eyebrow, "At-a-glance vote balance");
assert.equal(voteVisuals.summary, "6 support votes · 4 weakening votes · 11 unresolved votes");
assert.equal(voteVisuals.dominantLabel, "unresolved votes dominate this cockpit");
assert.equal(
  JSON.stringify(voteVisuals.segments.map((segment) => [segment.kind, segment.count, segment.percent, segment.label])),
  JSON.stringify([
    ["support", 6, 29, "support"],
    ["weakening", 4, 19, "weakening"],
    ["unresolved", 11, 52, "unresolved"],
  ]),
);

const noVoteSignal = buildEvidenceVoteSignal([{ id: 4, stance: "supports", votes_agree: 0, votes_disagree: 0 }]);
assert.equal(noVoteSignal.totalVotes, 0);
assert.equal(noVoteSignal.verdict, "unvoted");
assert.equal(noVoteSignal.verdictLabel, "No counted evidence votes yet");
const noVoteVisuals = buildEvidenceVoteCockpitVisuals(noVoteSignal);
assert.equal(noVoteVisuals.summary, "No counted evidence votes yet");
assert.equal(noVoteVisuals.dominantLabel, "waiting for counted votes");
assert.equal(
  JSON.stringify(noVoteVisuals.segments.map((segment) => [segment.kind, segment.count, segment.percent])),
  JSON.stringify([["support", 0, 0], ["weakening", 0, 0], ["unresolved", 0, 0]]),
);

const unresolvedVoteSignal = buildEvidenceVoteSignal([{ id: 5, stance: "none", votes_agree: 5, votes_disagree: 6 }]);
assert.equal(unresolvedVoteSignal.supportVotes, 0);
assert.equal(unresolvedVoteSignal.weakeningVotes, 0);
assert.equal(unresolvedVoteSignal.unresolvedVotes, 11);
assert.equal(unresolvedVoteSignal.totalVotes, 11);
assert.equal(unresolvedVoteSignal.verdict, "unresolved");
assert.equal(unresolvedVoteSignal.verdictLabel, "Evidence votes unresolved");

const panelSource = fs.readFileSync(panelPath, "utf8");
assert.match(panelSource, /from "\.\/evidencePanelCopy"/, "DebateEvidencePanel should use shared copy helpers.");
assert.match(panelSource, /data-testid="evidence-panel-neutral-summary"/, "Neutral-only evidence state should have a testable summary.");
assert.match(panelSource, /data-testid="evidence-vote-signal"/, "Panel should expose a visible counted vote signal summary.");
assert.match(panelSource, /data-testid="evidence-vote-balance-bar"/, "Vote cockpit polish should include a testable at-a-glance segmented balance bar.");
assert.match(panelSource, /data-testid="evidence-vote-metric-grid"/, "Vote cockpit polish should expose metric cards for support, weakening, and unresolved counts.");
assert.match(panelSource, /data-testid="evidence-card-density-shell"/, "Evidence cards should use a tighter testable density shell.");
assert.match(panelSource, /data-testid="evidence-card-density-rail"/, "Evidence cards should combine stance, vote, status, and quality metadata in a compact rail.");
assert.match(panelSource, /data-testid="evidence-card-summary-clamp"/, "Evidence summaries should be visually clamped to preserve scan density.");
assert.match(panelSource, /data-testid="evidence-card-activity-rail"/, "Comments and element links should move into a secondary compact activity rail.");
assert.match(panelSource, /aria-label=\{scoreOpen \? "Hide evidence quality breakdown" : "Show evidence quality breakdown"\}/, "Quality pill should stay discoverable as an expandable control.");
assert.match(panelSource, /scoreOpen \? "▲" : "▼"/, "Quality control should include a compact visible disclosure cue.");
assert.match(panelSource, /buildEvidenceCardDensityMeta\(ev\)/, "Evidence cards should derive dense metadata from the shared helper contract.");
assert.match(panelSource, /WebkitLineClamp/, "Evidence summary clamp should be explicit in source for chunk verification.");
assert.ok(
  panelSource.indexOf("{statusMeta.trustBlocking && (") < panelSource.indexOf("data-testid=\"evidence-card-summary-clamp\""),
  "Trust-blocking caution should render before the clamped summary so warnings stay visible while density increases.",
);
assert.match(panelSource, /At-a-glance vote balance/, "Vote cockpit should use clearer visual hierarchy copy.");
assert.match(panelSource, /How counted votes map to the claim signal/, "Detailed semantics should move behind a disclosure instead of dominating the cockpit.");
assert.match(panelSource, /buildEvidenceVoteCockpitVisuals\(voteSignal\)/, "Panel should derive visual balance segments from the claim vote signal.");
assert.match(panelSource, /buildEvidenceVoteSignal\(evidence \|\| \[\]\)/, "Panel should derive claim-level support/weakening signal from evidence vote counts.");
assert.match(panelSource, /claim support signal/, "Evidence cards should explain claim-level support votes, not only raw pro/con counts.");
assert.match(panelSource, /claim weakening signal/, "Evidence cards should explain claim-level weakening votes, not only raw pro/con counts.");
assert.match(panelSource, /Linked paper sources/, "Neutral-only evidence rows should be grouped under linked paper source copy.");
assert.match(panelSource, /total > 0 && evidenceCopy\.hasDirectionalStance/, "Directional support/counter counts should render only when directional stances exist.");

console.log("evidence_panel_copy_ok");
