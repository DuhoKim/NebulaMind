import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

const repoRoot = path.resolve(import.meta.dirname, "..");
const clientPath = path.join(repoRoot, "src/app/wiki/[slug]/WikiPageClient.tsx");
const panelPath = path.join(repoRoot, "src/app/wiki/[slug]/DebateEvidencePanel.tsx");
const packagePath = path.join(repoRoot, "package.json");

const clientSource = fs.readFileSync(clientPath, "utf8");
const panelSource = fs.readFileSync(panelPath, "utf8");
const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));

function countOccurrences(source, needle) {
  return source.split(needle).length - 1;
}

assert.equal(
  packageJson.scripts["test:evidence-panel-focus-return"],
  "node scripts/test-evidence-panel-focus-return.mjs",
  "package.json should expose the focused evidence-panel focus-return probe.",
);

assert.match(panelSource, /data-testid="evidence-panel-dialog"/, "Focus-return probe should preserve the evidence-panel dialog a11y root marker.");
assert.match(panelSource, /aria-labelledby=\{evidencePanelHeadingId\}/, "Evidence panel should keep visible-heading labelling while focus return is hardened.");
assert.match(panelSource, /aria-describedby=\{evidencePanelHintId\}/, "Evidence panel should keep visible Escape-hint description while focus return is hardened.");
assert.match(panelSource, /returnFocusRef\?: RefObject<HTMLElement>/, "Evidence panel should accept a focus-return ref.");
assert.match(panelSource, /const closePanel = useCallback\(\(\) => \{[\s\S]*?returnFocusRef\?\.current\?\.focus\(\)/, "Close path should return focus through the supplied origin ref.");
assert.match(panelSource, /const closeOnEscape = \(event: KeyboardEvent\) => \{[\s\S]*?if \(event\.key === "Escape"\) \{[\s\S]*?if \(selectedPaperFootprint\) \{[\s\S]*?event\.preventDefault\(\);[\s\S]*?event\.stopPropagation\(\);[\s\S]*?closePaperFootprint\(\);[\s\S]*?return;[\s\S]*?\}[\s\S]*?closePanel\(\);[\s\S]*?\}[\s\S]*?\};/, "Escape should close the stacked paper footprint first, then use closePanel for the parent evidence panel.");
assert.match(panelSource, /const closePaperFootprint = useCallback\(\(\) => \{[\s\S]*?const origin = paperFootprintReturnFocusRef\.current;[\s\S]*?window\.setTimeout\(\(\) => origin\?\.focus\(\), 0\)/, "Paper footprint close path should capture and return focus to the evidence-card footprint opener after remount.");
assert.match(panelSource, /onClick=\{\(e\) => \{ e\.stopPropagation\(\); closePanel\(\); \}\}/, "Close button should use the shared focus-return closePanel path.");
assert.equal(countOccurrences(panelSource, "returnFocusRef?.current?.focus()"), 1, "Evidence panel should have exactly one focus-return call so every close path shares it.");
assert.equal(countOccurrences(panelSource, "closePanel();"), 3, "Escape, overlay, and close button should all converge on closePanel.");

assert.match(clientSource, /const claimBadgeTriggerRef = useRef<HTMLButtonElement \| null>\(null\)/, "Claim annotations should keep a ref to the originating claim badge button.");
assert.match(clientSource, /const evidencePanelReturnFocusRef = useRef<HTMLElement \| null>\(null\)/, "Claim annotations should keep a dedicated focus-return origin ref for the evidence panel.");
assert.match(clientSource, /returnFocusRef=\{claimBadgeTriggerRef\}/, "ClaimTrustBadge should receive the externally owned originating badge ref.");
assert.match(clientSource, /returnFocusRef=\{evidencePanelReturnFocusRef\}/, "DebateEvidencePanel should receive the dedicated focus-return origin ref.");
assert.match(clientSource, /onOpen=\{\(origin\) => \{[\s\S]*?evidencePanelReturnFocusRef\.current = origin \?\? claimBadgeTriggerRef\.current \?\? claimTriggerRef\.current;[\s\S]*?setOpen\(true\);[\s\S]*?\}\}/, "Opening from the trust badge should record the originating badge before showing the panel.");
assert.match(clientSource, /onClick=\{\(e\) => \{[\s\S]*?onOpen\(e\.currentTarget\);[\s\S]*?\}\}/, "Claim badge click should identify itself as the focus-return origin.");
const claimBadgeButton = clientSource.match(/<button[\s\S]*?data-testid="claim-trust-badge"[\s\S]*?>/);
assert.ok(claimBadgeButton, "The stable claim badge marker should remain on a button element.");
assert.match(claimBadgeButton[0], /ref=\{claimMiniMapTriggerRef\}/, "The stable claim badge marker should remain on the focus-return button ref target.");
assert.doesNotMatch(clientSource, /returnFocusRef=\{claimTriggerRef\}/, "The evidence panel should not return claim-badge-origin closes to the inline claim span by default.");

console.log("evidence_panel_focus_return_ok");
