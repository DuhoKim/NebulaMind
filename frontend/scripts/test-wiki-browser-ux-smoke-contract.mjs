import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const frontendRoot = path.resolve(import.meta.dirname, "..");
const packagePath = path.join(frontendRoot, "package.json");
const sourceAggregatePath = path.join(frontendRoot, "scripts/test-wiki-ux-smoke.mjs");
const browserAggregatePath = path.join(frontendRoot, "scripts/test-wiki-browser-ux-smoke.mjs");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));

assert.equal(
  packageJson.scripts["test:wiki-ux-smoke"],
  "node scripts/test-wiki-ux-smoke.mjs",
  "Source-only wiki UX aggregate must stay fast and must not be replaced by browser/build smoke.",
);
assert.equal(
  packageJson.scripts["smoke:wiki-browser-ux"],
  "node scripts/test-wiki-browser-ux-smoke.mjs",
  "Browser UX aggregate should be a dedicated smoke command, separate from test:wiki-ux-smoke.",
);
assert.equal(
  packageJson.scripts["smoke:wiki-browser-ux:build"],
  "npm run build && npm run smoke:wiki-browser-ux",
  "Build-inclusive browser UX command should run Next build before the browser smoke wrapper.",
);
assert.equal(
  packageJson.scripts["smoke:wiki-browser-ux:contract"],
  "node scripts/test-wiki-browser-ux-smoke-contract.mjs",
  "The browser UX smoke/report contract should have a focused package command.",
);

const sourceAggregate = fs.readFileSync(sourceAggregatePath, "utf8");
assert.doesNotMatch(
  sourceAggregate,
  /smoke:wiki-browser-ux|smoke:wiki-stacked-popover-browser|test-wiki-browser-ux-smoke|npm run build/,
  "Source-only wiki UX aggregate must not invoke browser smoke or Next build.",
);

assert.ok(fs.existsSync(browserAggregatePath), "Browser UX smoke wrapper should exist.");
const browserAggregate = fs.readFileSync(browserAggregatePath, "utf8");
assert.match(
  browserAggregate,
  /smoke:wiki-stacked-popover-browser/,
  "Browser UX wrapper should consume the existing stacked-popover browser smoke instead of duplicating it.",
);
assert.match(browserAggregate, /STACKED_POPOVER_BROWSER_JSON/, "Wrapper should parse the existing browser-smoke JSON marker.");
assert.match(browserAggregate, /WIKI_BROWSER_UX_SMOKE_OK/, "Wrapper should emit a stable OK marker for dashboards.");
assert.match(browserAggregate, /WIKI_BROWSER_UX_SMOKE_JSON/, "Wrapper should emit one parseable JSON summary line.");
assert.match(browserAggregate, /wiki_browser_ux_smoke\.v1/, "Summary JSON should include an explicit schema version.");

const fixtureOutput = [
  "STACKED_POPOVER_CASE_OK name=claim-mini-map first_escape=mini_map_only second_escape=panel_closed url=http://127.0.0.1:3033/wiki/galaxy-evolution-v2",
  "STACKED_POPOVER_CASE_OK name=source-trace first_escape=source_trace_only second_escape=panel_closed url=http://127.0.0.1:3033/wiki/source-trace-browser-fixture",
  'STACKED_POPOVER_BROWSER_OK cases=2/2 first_escape=top_popover_only second_escape=panel_closed',
  'STACKED_POPOVER_BROWSER_JSON {"ok":true,"cases":[{"name":"claim-mini-map","ok":true,"route":"/wiki/galaxy-evolution-v2","url":"http://127.0.0.1:3033/wiki/galaxy-evolution-v2","firstEscapeMarker":"mini_map_only"},{"name":"source-trace","ok":true,"route":"/wiki/source-trace-browser-fixture","url":"http://127.0.0.1:3033/wiki/source-trace-browser-fixture","firstEscapeMarker":"source_trace_only"}]}',
].join("\n");
const fixturePath = path.join(os.tmpdir(), `wiki-browser-ux-smoke-fixture-${process.pid}.log`);
fs.writeFileSync(fixturePath, fixtureOutput, "utf8");
try {
  const result = spawnSync(process.execPath, [browserAggregatePath], {
    cwd: frontendRoot,
    encoding: "utf8",
    env: { ...process.env, WIKI_BROWSER_UX_SMOKE_FIXTURE_OUTPUT: fixturePath },
  });
  assert.equal(result.status, 0, `Fixture wrapper run should pass. stdout=${result.stdout}\nstderr=${result.stderr}`);
  assert.match(result.stdout, /WIKI_BROWSER_UX_SMOKE_OK passed=2\/2 failed=0/, "Wrapper should emit stable dashboard OK line.");
  const jsonLine = result.stdout.split(/\r?\n/).find((line) => line.startsWith("WIKI_BROWSER_UX_SMOKE_JSON "));
  assert.ok(jsonLine, `Wrapper should emit WIKI_BROWSER_UX_SMOKE_JSON. stdout=${result.stdout}`);
  const summary = JSON.parse(jsonLine.replace("WIKI_BROWSER_UX_SMOKE_JSON ", ""));
  assert.equal(summary.schemaVersion, "wiki_browser_ux_smoke.v1");
  assert.equal(summary.ok, true);
  assert.equal(summary.total, 2);
  assert.equal(summary.passed, 2);
  assert.equal(summary.failed, 0);
  assert.deepEqual(summary.failedCases, []);
  assert.deepEqual(
    summary.cases.map((item) => item.name),
    ["claim-mini-map", "source-trace"],
  );
  assert.equal(summary.upstream.command, "npm run --silent smoke:wiki-stacked-popover-browser");
  assert.ok(summary.generatedAt, "Summary should include a generated timestamp for report consumers.");
} finally {
  fs.rmSync(fixturePath, { force: true });
}

console.log("wiki_browser_ux_smoke_contract_ok");
