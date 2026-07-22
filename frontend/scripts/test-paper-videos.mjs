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
const packagePath = path.join(root, "package.json");

const expected = {
  "/studies/z9-10-unlensed-metallicity-deficit.pdf": "hHxmycvPalE",
  "/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf": "QjdJ1WZpiJY",
  "/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf": "XiB4dpn2o3g",
  "/agent-reports/research-frontiers/mzr-aperture-calibration-framework.pdf": "jVyK-y_KQ14",
  "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf": "gDIVbF8ZUFg",
};

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
  "The map should contain exactly the five approved PDF-to-video bindings.",
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
assert.deepEqual(renderedPdfPaths, Object.keys(expected).sort(), "Every currently rendered paper card should have exactly one approved video binding.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:paper-videos"], "node scripts/test-paper-videos.mjs");

console.log("paper_videos_ok");
