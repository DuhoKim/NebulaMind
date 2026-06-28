import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const frontendRoot = path.resolve(import.meta.dirname, "..");
const packageJson = JSON.parse(fs.readFileSync(path.join(frontendRoot, "package.json"), "utf8"));
const PROBE_TIMEOUT_MS = 30_000;
const OUTPUT_TAIL_LINES = 6;

const wikiUxProbes = [
  { script: "test:evidence-status", marker: "evidence_status_helper_ok" },
  { script: "test:trust-history-copy", marker: "trust_history_copy_helper_ok" },
  { script: "test:wiki-trust-visibility", marker: "wiki_trust_visibility_smoke_ok" },
  { script: "test:evidence-panel-copy", marker: "evidence_panel_copy_ok" },
  { script: "test:evidence-panel-visual-probe", marker: "evidence_panel_visual_probe_ok" },
  { script: "test:evidence-panel-focus-return", marker: "evidence_panel_focus_return_ok" },
  { script: "test:source-trace-hover", marker: "source_trace_hover_ok" },
  { script: "test:claim-minimap-hover", marker: "claim_minimap_hover_ok" },
];

const expectedScripts = new Set(wikiUxProbes.map((probe) => probe.script));
const packageWikiUxScripts = Object.keys(packageJson.scripts || {})
  .filter((script) => /^test:(evidence|trust|wiki|source|claim)/.test(script))
  .filter((script) => script !== "test:wiki-ux-smoke")
  .sort();
const runnerScripts = [...expectedScripts].sort();
const missingFromRunner = packageWikiUxScripts.filter((script) => !expectedScripts.has(script));
const missingFromPackage = runnerScripts.filter((script) => !packageWikiUxScripts.includes(script));

function compactTail(text, lineCount = OUTPUT_TAIL_LINES) {
  return String(text || "")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .slice(-lineCount)
    .join(" | ");
}

function printMembershipFailure() {
  console.log(
    `WIKI_UX_SMOKE_FAIL passed=0/${wikiUxProbes.length} duration_ms=0 reason=runner_membership_stale`
  );
  if (missingFromRunner.length > 0) {
    console.log(`  package scripts missing from runner: ${missingFromRunner.join(", ")}`);
  }
  if (missingFromPackage.length > 0) {
    console.log(`  runner scripts missing from package.json: ${missingFromPackage.join(", ")}`);
  }
}

if (missingFromRunner.length > 0 || missingFromPackage.length > 0) {
  printMembershipFailure();
  process.exit(1);
}

const startedAt = Date.now();
const results = [];

for (const probe of wikiUxProbes) {
  const probeStartedAt = Date.now();
  const result = spawnSync("npm", ["run", "--silent", probe.script], {
    cwd: frontendRoot,
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"],
    timeout: PROBE_TIMEOUT_MS,
  });
  const stdout = result.stdout || "";
  const stderr = result.stderr || "";
  const timedOut = Boolean(result.error && result.error.code === "ETIMEDOUT");
  const markerSeen = stdout.includes(probe.marker) || stderr.includes(probe.marker);
  const ok = result.status === 0 && markerSeen && !timedOut;
  results.push({
    ...probe,
    ok,
    exitCode: timedOut ? 124 : result.status ?? 1,
    timedOut,
    durationMs: Date.now() - probeStartedAt,
    outputTail: compactTail(`${stdout}\n${stderr}`),
  });
}

for (const result of results) {
  const status = result.ok ? "PASS" : "FAIL";
  const detail = result.timedOut ? `timed out after ${PROBE_TIMEOUT_MS}ms` : result.outputTail || result.marker;
  console.log(`${status} ${result.script} ${result.durationMs}ms ${detail}`);
  if (!result.ok) {
    console.log(`  re-run: npm run ${result.script}`);
  }
}

const failed = results.filter((result) => !result.ok);
const durationMs = Date.now() - startedAt;
const marker = failed.length === 0 ? "WIKI_UX_SMOKE_OK" : "WIKI_UX_SMOKE_FAIL";
const summary = {
  ok: failed.length === 0,
  status: failed.length === 0 ? "ok" : "fail",
  marker,
  total: results.length,
  passed: results.length - failed.length,
  failed: failed.length,
  durationMs,
  failedScripts: failed.map((result) => result.script),
  probes: results.map((result) => ({
    script: result.script,
    status: result.ok ? "pass" : "fail",
    ok: result.ok,
    durationMs: result.durationMs,
    exitCode: result.exitCode,
    timedOut: result.timedOut,
    marker: result.marker,
  })),
};

console.log(
  `${marker} passed=${summary.passed}/${summary.total} failed=${summary.failed} duration_ms=${summary.durationMs}`
);
console.log(`WIKI_UX_SMOKE_JSON ${JSON.stringify(summary)}`);
process.exit(summary.ok ? 0 : 1);
