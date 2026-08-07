import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const root = process.cwd();
const mapPath = path.join(root, "src/app/lab/paperVideos.ts");
const componentPath = path.join(root, "src/app/lab/PaperVideo.tsx");
const flagshipPath = path.join(root, "src/app/lab/FlagshipStudies.tsx");
const frontierPath = path.join(root, "src/app/lab/FrontierDrafts.tsx");
const draftBoardPath = path.join(root, "src/app/lab/DraftBoard.tsx");
const packagePath = path.join(root, "package.json");

const expected = {
  "/studies/z9-10-unlensed-metallicity-deficit.pdf": "5Edsa6kKWnQ",
  "/agent-reports/research-frontiers/reionization-fesc-budget-landscape.pdf": "19azFXDa2VA",
  "/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf": "uo2T7ShkmKc",
  "/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf": "gasowEBf6RI",
  "/agent-reports/research-frontiers/mzr-aperture-calibration-framework.pdf": "S8qvGJ1Gx9g",
  "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf": "pqkkQutFpxk",
  // Lane-keyed, not PDF-keyed: a probe with no manuscript. Approved by Duho 2026-08-07.
  "spin-parity-census-20260805T1922K": "uch2gFhtd3g",
};

// Bindings that intentionally key on a lane id rather than a /path.pdf, so the PDF-resolution
// assertions below skip them instead of failing.
const LANE_KEYED = new Set(["spin-parity-census-20260805T1922K"]);

assert.ok(fs.existsSync(mapPath), "Paper-stage video map should exist.");
assert.ok(fs.existsSync(componentPath), "Shared PaperVideo component should exist.");

const mapSource = fs.readFileSync(mapPath, "utf8");
const compiled = ts.transpileModule(mapSource, {
  compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2019, strict: true },
  fileName: mapPath,
});
const mapModule = { exports: {} };
vm.runInNewContext(compiled.outputText, { module: mapModule, exports: mapModule.exports, require }, { filename: mapPath });
assert.deepEqual(
  JSON.parse(JSON.stringify(mapModule.exports.PAPER_VIDEOS)),
  expected,
  "The map should contain exactly the seven approved video bindings.",
);
assert.ok(Object.values(mapModule.exports.PAPER_VIDEOS).every(id => /^[A-Za-z0-9_-]{11}$/.test(id)), "Every value should be one YouTube video ID.");

const component = fs.readFileSync(componentPath, "utf8");
assert.match(component, /if \(!videoId\) return null/, "Missing IDs should fail closed without an empty iframe.");
assert.match(component, /https:\/\/www\.youtube-nocookie\.com\/embed\/\$\{videoId\}/, "Paper embeds should use YouTube's privacy-enhanced host.");
assert.match(component, /loading="lazy"/, "Paper embeds should load lazily.");
assert.match(component, /allowFullScreen/, "Paper embeds should support fullscreen playback.");
assert.match(component, /referrerPolicy="strict-origin-when-cross-origin"/, "Paper embeds should use a strict referrer policy.");
assert.match(component, /title=\{`\$\{title\} explainer video`\}/, "Every iframe should expose the paper-specific title.");
assert.doesNotMatch(component, /autoplay/, "Paper videos should never autoplay inside manuscript cards.");
assert.match(component, /aspectRatio: "16 \/ 9"/, "Paper embeds should retain a responsive 16:9 frame.");

const flagship = fs.readFileSync(flagshipPath, "utf8");
assert.match(flagship, /import \{ PaperVideo \} from "\.\/PaperVideo"/);
assert.match(flagship, /import \{ PAPER_VIDEOS \} from "\.\/paperVideos"/);
assert.match(flagship, /<PaperVideo videoId=\{PAPER_VIDEOS\[f\.pdf\]\} title=\{f\.title\} \/>/, "Flagship card should render its exact mapped explainer.");

const frontier = fs.readFileSync(frontierPath, "utf8");
assert.match(frontier, /import \{ PaperVideo \} from "\.\/PaperVideo"/);
assert.match(frontier, /import \{ PAPER_VIDEOS \} from "\.\/paperVideos"/);
assert.match(frontier, /<PaperVideo videoId=\{PAPER_VIDEOS\[f\.pdf\]\} title=\{f\.title\} \/>/, "Each frontier card should render its exact mapped explainer.");

const renderedPdfPaths = [...flagship.matchAll(/pdf: "([^"]+)"/g), ...frontier.matchAll(/pdf: "([^"]+)"/g)]
  .map(match => match[1])
  .sort();
// 4 in FlagshipStudies (3 flagship + 1 human-rejected, which stays published) + 5 frontier drafts.
assert.equal(renderedPdfPaths.length, 9, "The current Paper Board catalog should contain nine manuscripts.");
for (const key of Object.keys(expected)) {
  if (LANE_KEYED.has(key)) {
    assert.ok(flagship.includes(`lane: "${key}"`), `Lane-keyed binding should resolve to a rendered track: ${key}`);
    continue;
  }
  assert.ok(renderedPdfPaths.includes(key), `Approved video binding should resolve to a rendered paper card: ${key}`);
}
assert.equal(Object.keys(expected).length, 7, "Exactly seven approved video bindings; unmapped papers fail closed without a chip.");

const draftBoard = fs.readFileSync(draftBoardPath, "utf8");
assert.match(draftBoard, /import \{ PAPER_VIDEOS \} from "\.\/paperVideos"/, "Paper Board should use the shared PDF-to-video map.");
assert.match(draftBoard, /const videoId = it\.pdf \? PAPER_VIDEOS\[it\.pdf\] : it\.lane \? PAPER_VIDEOS\[it\.lane\] : undefined/, "Each Paper Board row should resolve by PDF, then by lane, and fail closed when neither is mapped.");
assert.match(draftBoard, /href=\{`https:\/\/youtu\.be\/\$\{videoId\}`\}/, "The YouTube chip should open the exact mapped review URL.");
assert.match(draftBoard, />YouTube ↗<\/a>/, "The Paper Board chip should have a concise visible label.");
assert.match(draftBoard, /className="pb-chip db-lrow-video"/, "The YouTube link should render as a chip, not an unstyled link.");
assert.match(draftBoard, /target="_blank" rel="noopener noreferrer"/, "The external video link should open safely.");
assert.match(draftBoard, /onClick=\{\(e\) => e\.stopPropagation\(\)\}/, "Using the chip should not toggle the paper row.");
assert.match(draftBoard, /grid-template-columns:5rem minmax\(0,1fr\)/, "Mobile Paper Board rows should preserve a real title column after adding the chip.");
assert.match(draftBoard, /\.db-lrow-meta\{grid-column:2;flex-wrap:wrap/, "Mobile Paper Board controls should wrap below the title instead of squeezing it out.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:paper-videos"], "node scripts/test-paper-videos.mjs");

console.log("paper_videos_ok");
