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
const wikiClientPath = path.join(repoRoot, "src/app/wiki/[slug]/WikiPageClient.tsx");

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
  buildClaimSourceContradictionAtlas,
  buildPageContradictionRankingAtlas,
  buildEvidenceCardDensityMeta,
  buildEvidencePanelCopy,
  buildEvidenceVoteCockpitVisuals,
  buildEvidenceVoteSignal,
  evidenceSide,
  formatLinkedPaperSourceCount,
} = module.exports;

assert.equal(typeof buildClaimSourceContradictionAtlas, "function");
assert.equal(typeof buildPageContradictionRankingAtlas, "function");
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

const atlas = buildClaimSourceContradictionAtlas([
  { id: 101, title: "Resolved stellar population evidence", stance: "supports", votes_agree: 7, votes_disagree: 1, quality_v2: 0.91 },
  { id: 202, title: "Dust-obscured counterexample survey", stance: "challenges", votes_agree: 5, votes_disagree: 2, quality_v2: 0.86 },
  { id: 303, title: "Context-only calibration sample", stance: "none", votes_agree: 1, votes_disagree: 0, quality_v2: 0.44 },
]);
assert.equal(atlas.hasContradiction, true);
assert.equal(atlas.headline, "Contradiction pressure: 1 supporting vs 1 countering source");
assert.equal(atlas.summary, "This claim has mapped support and counter-evidence; the atlas surfaces where sources disagree, not which side is correct.");
assert.match(atlas.summary, /not which side is correct/, "Atlas framing should say it surfaces corpus disagreement, not a final truth verdict.");
assert.equal(atlas.tensionScore, 67);
assert.equal(atlas.primarySupport?.sourceId, 101);
assert.equal(atlas.primarySupport?.anchorHref, "#evidence-source-101");
assert.equal(atlas.primaryCounter?.sourceId, 202);
assert.equal(atlas.primaryCounter?.anchorHref, "#evidence-source-202");
assert.equal(
  JSON.stringify(atlas.lanes.map((lane) => [lane.kind, lane.label, lane.count, lane.percent])),
  JSON.stringify([
    ["support", "supporting sources", 1, 33],
    ["counter", "countering sources", 1, 33],
    ["unresolved", "unresolved sources", 1, 33],
  ]),
);

const calmAtlas = buildClaimSourceContradictionAtlas([{ id: 404, title: "Single supporting paper", stance: "supports" }]);
assert.equal(calmAtlas.hasContradiction, false);
assert.equal(calmAtlas.headline, "No source contradiction mapped yet");
assert.equal(calmAtlas.summary, "Mapped evidence currently leans one direction; keep watching for counter-sources or unresolved links.");

const pageRanking = buildPageContradictionRankingAtlas(
  {
    sections: [
      {
        title: "Early assembly",
        claims: [
          { id: 501, text: "Massive galaxies assembled early.", trust_level: "challenged", evidence_count: 4, con_count: 2 },
          { id: 502, text: "Minor mergers add stellar halos.", trust_level: "accepted", evidence_count: 3, con_count: 0 },
          { id: 503, text: "Dust-obscured systems complicate counts.", trust_level: "debated", evidence_count: 2, con_count: 1 },
        ],
      },
    ],
  },
  {
    501: [
      { id: 101, title: "JWST support synthesis", stance: "supports", votes_agree: 6, quality_v2: 0.88 },
      { id: 202, title: "Dust-obscured counter survey", stance: "challenges", votes_agree: 7, quality_v2: 0.92 },
      { id: 203, title: "Morphology counter sample", stance: "contradicts", votes_agree: 4, quality_v2: 0.81 },
    ],
    502: [
      { id: 204, title: "Halo support sample", stance: "supports", votes_agree: 5, quality_v2: 0.74 },
    ],
  },
  [501, 502, 503],
);
assert.equal(pageRanking.totalClaims, 3);
assert.equal(pageRanking.surfacedClaims, 2);
assert.equal(pageRanking.surveyedClaims, 2);
assert.equal(pageRanking.hasRankedClaims, true);
assert.match(pageRanking.summary, /not which side is correct/, "Page atlas framing should not imply final truth adjudication.");
assert.equal(pageRanking.items[0].claimId, 501);
assert.equal(pageRanking.items[0].sourceSurveyed, true);
assert.equal(pageRanking.items[0].counterCount, 2);
assert.equal(pageRanking.items[0].supportCount, 1);
assert.equal(pageRanking.items[0].rankLabel, "2 countering · 1 supporting · tension 50%");
assert.equal(pageRanking.items[0].tierLabel, "Contradicted");
assert.equal(pageRanking.items[0].evidencePanelId, "claim-evidence-panel-501");
assert.equal(pageRanking.items[1].claimId, 503);
assert.equal(pageRanking.items[1].sourceSurveyed, false);
assert.equal(pageRanking.items[1].rankLabel, "1 countering · 1 supporting · source lanes pending");
assert.equal(pageRanking.items[1].tierLabel, "Questioned");

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
const wikiClientSource = fs.readFileSync(wikiClientPath, "utf8");
assert.match(panelSource, /from "\.\/evidencePanelCopy"/, "DebateEvidencePanel should use shared copy helpers.");
assert.match(panelSource, /data-testid="evidence-panel-neutral-summary"/, "Neutral-only evidence state should have a testable summary.");
assert.match(panelSource, /data-testid="evidence-vote-signal"/, "Panel should expose a visible counted vote signal summary.");
assert.match(panelSource, /data-testid="claim-source-contradiction-atlas"/, "Panel should expose a visible claim-to-source contradiction atlas.");
assert.match(panelSource, /data-testid="contradiction-atlas-lane-grid"/, "Contradiction atlas should show lane counts for supporting, countering, and unresolved sources.");
assert.match(panelSource, /data-testid="contradiction-atlas-tension-badge"/, "Contradiction atlas should expose a stable tension score marker.");
assert.match(panelSource, /data-testid="contradiction-atlas-source-link"/, "Contradiction atlas should link representative sources back to evidence cards.");
assert.match(panelSource, /Claim-to-source contradiction atlas/, "Contradiction atlas should use explicit user-facing copy.");
assert.match(panelSource, /id=\{`evidence-source-\$\{ev\.id\}`\}/, "Evidence cards should expose source anchors for atlas links.");
assert.match(panelSource, /data-testid="evidence-vote-balance-bar"/, "Vote cockpit polish should include a testable at-a-glance segmented balance bar.");
assert.match(panelSource, /data-testid="evidence-vote-metric-grid"/, "Vote cockpit polish should expose metric cards for support, weakening, and unresolved counts.");
assert.match(panelSource, /data-testid="evidence-card-density-shell"/, "Evidence cards should use a tighter testable density shell.");
assert.match(panelSource, /data-testid="evidence-card-density-rail"/, "Evidence cards should combine stance, vote, status, and quality metadata in a compact rail.");
assert.match(panelSource, /data-testid="evidence-card-summary-clamp"/, "Evidence summaries should be visually clamped to preserve scan density.");
assert.match(panelSource, /data-testid="evidence-card-activity-rail"/, "Comments and element links should move into a secondary compact activity rail.");
assert.match(panelSource, /data-testid="evidence-panel-dialog"/, "Evidence panel dialog should expose a stable root marker for a11y/visual probes.");
assert.match(panelSource, /const fallbackPanelId = useId\(\)/, "Evidence panel dialog should use a stable React id fallback when no panel id is provided.");
assert.match(panelSource, /const evidencePanelTitle = isContested \? "Debate map" : "Evidence map"/, "Evidence panel title should be single-sourced from contested state.");
assert.match(panelSource, /const evidencePanelNoun = isContested \? "debate map" : "evidence map"/, "Evidence panel hint noun should use the same contested state as the heading.");
assert.match(panelSource, /aria-labelledby=\{evidencePanelHeadingId\}/, "Evidence panel dialog should be labelled by its visible heading, not detached aria-label copy.");
assert.match(panelSource, /aria-describedby=\{evidencePanelHintId\}/, "Evidence panel dialog should describe itself with the visible keyboard dismissal hint.");
assert.match(panelSource, /Press Escape to close this \{evidencePanelNoun\}\./, "Evidence panel should expose visible Escape-dismissal copy inside the dialog.");
assert.doesNotMatch(panelSource, /aria-label=\{isContested \? "Debate map" : "Evidence map"\}/, "Evidence panel dialog should not keep a detached aria-label once visible heading ids exist.");
assert.ok(!panelSource.includes("undefined-heading") && !panelSource.includes("undefined-keyboard-hint"), "Evidence panel dialog ARIA ids should never contain undefined.");
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
assert.match(wikiClientSource, /buildPageContradictionRankingAtlas/, "Wiki page should derive a page-level claim contradiction ranking from shared helpers.");
assert.match(wikiClientSource, /data-testid="page-contradiction-atlas-ranking"/, "Wiki page should expose the page-level contradiction atlas ranking section.");
assert.match(wikiClientSource, /data-testid="page-atlas-ranked-claim"/, "Page atlas should render ranked claim rows with stable markers.");
assert.match(wikiClientSource, /data-testid="page-atlas-open-evidence-map"/, "Page atlas rows should open the existing evidence map dialog.");
assert.match(wikiClientSource, /Where evidence weighs against this page/, "Page atlas heading should avoid saying the wiki prose is simply wrong.");
assert.match(wikiClientSource, /aria-describedby=\{pageAtlasDescriptionId\}/, "Page atlas should describe the ranking criterion for screen readers.");
assert.match(wikiClientSource, /Claims ranked by mapped counter-source pressure/, "Page atlas should explain that ordering is meaningful.");
assert.match(wikiClientSource, /\{item\.tierLabel\}/, "Page atlas should expose textual tiers, not color-only contradiction signals.");
assert.match(wikiClientSource, /not which side is correct/, "Page atlas should preserve truth-framing copy in the visible UI.");
assert.match(wikiClientSource, /fetch\(`\/api\/claims\/\$\{claimId\}\/evidence`\)/, "Page atlas should reuse the existing claim evidence endpoint for source-lane surveys.");

console.log("evidence_panel_copy_ok");
