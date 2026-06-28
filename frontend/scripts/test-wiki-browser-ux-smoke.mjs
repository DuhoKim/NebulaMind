import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const frontendRoot = path.resolve(import.meta.dirname, "..");
const SCHEMA_VERSION = "wiki_browser_ux_smoke.v1";
const UPSTREAM_SCRIPT = "smoke:wiki-stacked-popover-browser";
const UPSTREAM_COMMAND = `npm run --silent ${UPSTREAM_SCRIPT}`;
const STACKED_JSON_PREFIX = "STACKED_POPOVER_BROWSER_JSON ";
const OUTPUT_TAIL_LINES = 16;

function compactTail(text, lineCount = OUTPUT_TAIL_LINES) {
  return String(text || "")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .slice(-lineCount)
    .join(" | ");
}

function readFixtureOutput() {
  const fixturePath = process.env.WIKI_BROWSER_UX_SMOKE_FIXTURE_OUTPUT;
  if (!fixturePath) return null;
  return {
    status: 0,
    stdout: fs.readFileSync(fixturePath, "utf8"),
    stderr: "",
    error: null,
    fromFixture: true,
  };
}

function runStackedPopoverSmoke() {
  const fixture = readFixtureOutput();
  if (fixture) return fixture;
  const result = spawnSync("npm", ["run", "--silent", UPSTREAM_SCRIPT], {
    cwd: frontendRoot,
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"],
    env: process.env,
  });
  return {
    status: result.status ?? (result.error ? 1 : 0),
    stdout: result.stdout || "",
    stderr: result.stderr || "",
    error: result.error || null,
    fromFixture: false,
  };
}

function parseStackedPopoverJson(output) {
  const line = String(output || "")
    .split(/\r?\n/)
    .find((candidate) => candidate.startsWith(STACKED_JSON_PREFIX));
  if (!line) return { parsed: null, parseError: `missing ${STACKED_JSON_PREFIX.trim()} line` };
  try {
    return { parsed: JSON.parse(line.slice(STACKED_JSON_PREFIX.length)), parseError: null };
  } catch (error) {
    return { parsed: null, parseError: `invalid ${STACKED_JSON_PREFIX.trim()} payload: ${error.message}` };
  }
}

function summarizeCase(rawCase) {
  const ok = rawCase?.ok === true;
  return {
    name: String(rawCase?.name || "unknown"),
    status: ok ? "pass" : "fail",
    ok,
    route: rawCase?.route || null,
    url: rawCase?.url || null,
    firstEscapeMarker: rawCase?.firstEscapeMarker || null,
  };
}

function buildSummary(upstreamResult, durationMs) {
  const combinedOutput = `${upstreamResult.stdout || ""}\n${upstreamResult.stderr || ""}`;
  const { parsed, parseError } = parseStackedPopoverJson(combinedOutput);
  const cases = Array.isArray(parsed?.cases) ? parsed.cases.map(summarizeCase) : [];
  const failedCases = cases.filter((item) => !item.ok).map((item) => item.name);
  const upstreamOk = upstreamResult.status === 0 && parsed?.ok === true && cases.length > 0 && failedCases.length === 0;
  const ok = upstreamOk && !parseError;

  return {
    schemaVersion: SCHEMA_VERSION,
    generatedAt: new Date().toISOString(),
    ok,
    status: ok ? "ok" : "fail",
    marker: ok ? "WIKI_BROWSER_UX_SMOKE_OK" : "WIKI_BROWSER_UX_SMOKE_FAIL",
    total: cases.length,
    passed: cases.length - failedCases.length,
    failed: failedCases.length,
    failedCases,
    durationMs,
    cases,
    upstream: {
      command: UPSTREAM_COMMAND,
      script: UPSTREAM_SCRIPT,
      exitCode: upstreamResult.status,
      ok: upstreamResult.status === 0 && parsed?.ok === true,
      fromFixture: upstreamResult.fromFixture,
      parseError,
      error: upstreamResult.error ? upstreamResult.error.message : null,
      outputTail: compactTail(combinedOutput),
    },
  };
}

const startedAt = Date.now();
const upstreamResult = runStackedPopoverSmoke();
const combinedOutput = `${upstreamResult.stdout || ""}${upstreamResult.stderr ? `\n${upstreamResult.stderr}` : ""}`.trim();
if (combinedOutput) {
  console.log(combinedOutput);
}

const summary = buildSummary(upstreamResult, Date.now() - startedAt);
console.log(
  `${summary.marker} passed=${summary.passed}/${summary.total} failed=${summary.failed} duration_ms=${summary.durationMs} upstream=${UPSTREAM_SCRIPT}`,
);
if (summary.upstream.parseError) {
  console.log(`  parse_error=${summary.upstream.parseError}`);
}
if (summary.failedCases.length > 0) {
  console.log(`  failed_cases=${summary.failedCases.join(",")}`);
}
console.log(`WIKI_BROWSER_UX_SMOKE_JSON ${JSON.stringify(summary)}`);
process.exit(summary.ok ? 0 : 1);
