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
assert.match(clientSource, /data-testid="claim-trust-badge"/, "Claim badge trigger should stay mechanically testable.");
assert.match(clientSource, /data-testid="claim-mini-map-trigger"/, "Claim mini-map trigger should expose a stable keyboard UX test id.");
assert.match(clientSource, /data-testid="claim-mini-map-hover-card"/, "Claim badges should expose a testable mini-map hover card.");
assert.match(clientSource, /Claim mini-map/, "Claim badge hover cards should visibly label the mini-map.");
assert.match(clientSource, /onMouseEnter=/, "Claim mini-maps should open on hover.");
assert.match(clientSource, /onFocus=/, "Claim mini-maps should open for keyboard focus.");
assert.match(clientSource, /const handleMiniMapKeyDown[\s\S]*e\.key === "Escape"/, "Claim mini-map should close on Escape from trigger or card.");
assert.match(clientSource, /if \(e\.key === "Escape" && showMiniMap\)/, "Claim mini-map Escape handler should only intercept Escape while the mini-map is visible.");
// Keep this Escape isolation contract in lock-step with test-source-trace-hover.mjs.
const miniMapEscapeHandler = clientSource.match(/const handleMiniMapKeyDown = \(e: React\.KeyboardEvent\) => \{[\s\S]*?\n  \};/);
assert.ok(miniMapEscapeHandler, "Claim mini-map Escape handler should be extractable for isolation checks.");
const miniMapEscapeHandlerSource = miniMapEscapeHandler[0];
assert.ok(miniMapEscapeHandlerSource.length > 120, "Claim mini-map Escape handler extraction should include the full close/focus isolation block.");
const miniMapPreventDefaultIndex = miniMapEscapeHandlerSource.indexOf("e.preventDefault();");
const miniMapStopPropagationIndex = miniMapEscapeHandlerSource.indexOf("e.stopPropagation();");
const miniMapStopImmediatePropagationIndex = miniMapEscapeHandlerSource.indexOf("e.nativeEvent.stopImmediatePropagation();");
const miniMapCloseIndex = miniMapEscapeHandlerSource.indexOf("closeMiniMap();");
const miniMapFocusIndex = miniMapEscapeHandlerSource.indexOf("claimMiniMapTriggerRef.current?.focus();");
assert.ok(miniMapPreventDefaultIndex >= 0, "Claim mini-map Escape handler should prevent default before closing.");
assert.ok(miniMapStopPropagationIndex >= 0, "Claim mini-map Escape handler should stop React propagation before closing.");
assert.ok(miniMapStopImmediatePropagationIndex >= 0, "Claim mini-map Escape handler should stop the native event before document listeners can close parent dialogs.");
assert.ok(miniMapCloseIndex >= 0, "Claim mini-map Escape handler should close the mini-map.");
assert.ok(miniMapFocusIndex >= 0, "Claim mini-map Escape handler should return focus to the trigger.");
assert.ok(
  miniMapPreventDefaultIndex < miniMapStopPropagationIndex
    && miniMapStopPropagationIndex < miniMapStopImmediatePropagationIndex
    && miniMapStopImmediatePropagationIndex < miniMapCloseIndex
    && miniMapCloseIndex < miniMapFocusIndex,
  "Claim mini-map Escape isolation should prevent default, stop React propagation, and stop native document propagation before close/focus return.",
);
assert.match(clientSource, /claimMiniMapTriggerRef\.current\?\.focus\(\)/, "Claim mini-map Escape close should return focus to the trigger.");
assert.match(clientSource, /aria-describedby=\{showMiniMap \? miniMapId : undefined\}/, "Claim badges should only describe themselves with the mini-map while it is present.");
assert.match(clientSource, /aria-expanded=\{open \|\| showMiniMap\}/, "Claim badge expanded state should include the keyboard-visible mini-map.");
assert.match(clientSource, /aria-controls=\{showMiniMap \? miniMapId : panelId\}/, "Claim badge should point aria-controls at the visible mini-map when focused.");
assert.match(clientSource, /aria-labelledby=\{miniMapHeadingId\}/, "Claim mini-map tooltip should be labelled by its visible heading.");
assert.match(clientSource, /id=\{miniMapHeadingId\}/, "Claim mini-map heading id should match aria-labelledby.");
assert.match(clientSource, /Press Escape to close this mini-map/, "Claim mini-map should expose a visible keyboard dismissal hint.");
assert.match(clientSource, /Click for full evidence map/, "Mini-map should tell users click opens the full evidence map.");
assert.match(clientSource, /data-testid="claim-mini-map-open-evidence-map"/, "Mini-map should include a cross-link button into the full evidence map.");
assert.match(clientSource, /data-testid="claim-mini-map-jump-to-claim"/, "Mini-map should include a cross-link back to the claim text anchor.");
assert.match(clientSource, /miniMap\.primaryActionLabel/, "Mini-map action copy should come from the helper contract.");
assert.match(clientSource, /miniMap\.claimAnchorHref/, "Mini-map should use the helper-provided claim text anchor link.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:claim-minimap-hover"], "node scripts/test-claim-minimap-hover.mjs");

console.log("claim_minimap_hover_ok");
