import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/sourceTraceHover.ts");
const clientPath = path.join(repoRoot, "src/app/wiki/[slug]/WikiPageClient.tsx");
const packagePath = path.join(repoRoot, "package.json");

assert.ok(fs.existsSync(helperPath), "source trace hover helper should exist.");

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
  formatSourceTraceHoverCard,
  formatSourceTraceSummary,
} = module.exports;

assert.equal(typeof formatSourceTraceHoverCard, "function");
assert.equal(typeof formatSourceTraceSummary, "function");

const trace = formatSourceTraceHoverCard({
  evidence_id: 42,
  author_year_key: "Smith2024",
  title: "Quenching Pathways in Massive Galaxies",
  authors: ["Jane Smith", "Min Lee", "Ana Patel"],
  year: 2024,
  doi: "10.1234/galaxy.trace",
  arxiv_id: "2401.12345",
  journal_ref: "ApJ 900, 1",
  url: "https://example.org/paper",
  summary: "A compact paper summary explaining why this citation supports the specific wiki sentence rather than the whole page.",
}, "galaxy-evolution-v2");

assert.equal(trace.eyebrow, "Source trace");
assert.equal(trace.title, "Quenching Pathways in Massive Galaxies");
assert.equal(trace.traceLabel, "Evidence #42 · Smith2024");
assert.equal(trace.byline, "Jane Smith, Min Lee et al. · 2024 · ApJ 900, 1");
assert.equal(trace.locator, "arXiv:2401.12345 · DOI:10.1234/galaxy.trace");
assert.match(trace.summary, /specific wiki sentence/);
assert.equal(
  JSON.stringify(trace.crossLinks.map((link) => [link.kind, link.label, link.href, link.external])),
  JSON.stringify([
    ["source-index", "Open source index", "/wiki/galaxy-evolution-v2/sources", false],
    ["external-paper", "Open paper", "https://example.org/paper", true],
  ]),
);
assert.equal(
  formatSourceTraceSummary("0123456789".repeat(30), 64),
  `${"0123456789".repeat(6)}012…`,
);

const fallback = formatSourceTraceHoverCard({ evidence_id: 7, title: "" });
assert.equal(fallback.title, "Untitled source");
assert.equal(fallback.traceLabel, "Evidence #7");
assert.equal(fallback.byline, "Source metadata pending");
assert.equal(fallback.locator, "External source link unavailable");
assert.equal(fallback.summary, "No abstract or summary has been published for this source yet.");

const clientSource = fs.readFileSync(clientPath, "utf8");
assert.match(clientSource, /from "\.\/sourceTraceHover"/, "WikiPageClient should use the source trace helper.");
assert.match(clientSource, /data-testid="source-trace-trigger"/, "Citation trigger should be mechanically addressable for keyboard UX checks.");
assert.match(clientSource, /data-testid="source-trace-hover-card"/, "Citation popovers should expose a testable source trace hover card.");
assert.match(clientSource, /data-testid="source-trace-cross-links"/, "Source trace hover cards should expose cross-links into source surfaces.");
assert.match(clientSource, /Open source index/, "Source trace cards should link to the full wiki source index.");
assert.match(clientSource, /Open paper/, "Source trace cards should preserve an external paper link as a cross-link.");
assert.match(clientSource, /pageSlug=\{slug\}/, "Citation badges should receive the page slug for internal cross-links.");
assert.match(clientSource, /Source trace/, "Citation popovers should visibly label the hover card as a source trace.");
assert.match(clientSource, /onMouseEnter=/, "Citation source traces should open on hover.");
assert.match(clientSource, /onFocus=/, "Citation source traces should open for keyboard focus.");
assert.match(clientSource, /const handleSourceTraceKeyDown[\s\S]*e\.key === "Escape"/, "Source trace should close on Escape from trigger or card.");
assert.match(clientSource, /sourceTraceTriggerRef\.current\?\.focus\(\)/, "Source trace Escape close should return focus to the trigger.");
assert.match(clientSource, /aria-labelledby=\{sourceTraceHeadingId\}/, "Source trace dialog should be labelled by its visible heading.");
assert.match(clientSource, /id=\{sourceTraceHeadingId\}/, "Source trace heading id should match aria-labelledby.");
assert.match(clientSource, /Press Escape to close/, "Source trace hover card should expose a visible keyboard dismissal hint.");
assert.doesNotMatch(clientSource, /Citation metadata is still loading/, "Old generic citation-loading copy should be replaced with source trace language.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:source-trace-hover"], "node scripts/test-source-trace-hover.mjs");

console.log("source_trace_hover_ok");
