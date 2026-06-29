import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const frontendRoot = path.resolve(import.meta.dirname, "..");
const SCHEMA_VERSION = "wiki_browser_ux_smoke.v1";
const STACKED_SCRIPT = "smoke:wiki-stacked-popover-browser";
const PAPER_PROFILE_SCRIPT = "smoke:wiki-paper-profile-browser";
const STACKED_JSON_PREFIX = "STACKED_POPOVER_BROWSER_JSON ";
const PAPER_PROFILE_JSON_PREFIX = "PAPER_PROFILE_BROWSER_JSON ";
const OUTPUT_TAIL_LINES = 18;

function compactTail(text, lineCount = OUTPUT_TAIL_LINES) {
  return String(text || "")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .slice(-lineCount)
    .join(" | ");
}

function readFixtureOutput(envName) {
  const fixturePath = process.env[envName];
  if (!fixturePath) return null;
  return {
    status: 0,
    stdout: fs.readFileSync(fixturePath, "utf8"),
    stderr: "",
    error: null,
    fromFixture: true,
  };
}

function runNpmScript(script, fixtureEnvName) {
  const fixture = readFixtureOutput(fixtureEnvName);
  if (fixture) return fixture;
  const result = spawnSync("npm", ["run", "--silent", script], {
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

function parseJsonLine(output, prefix) {
  const line = String(output || "")
    .split(/\r?\n/)
    .find((candidate) => candidate.startsWith(prefix));
  if (!line) return { parsed: null, parseError: `missing ${prefix.trim()} line` };
  try {
    return { parsed: JSON.parse(line.slice(prefix.length)), parseError: null };
  } catch (error) {
    return { parsed: null, parseError: `invalid ${prefix.trim()} payload: ${error.message}` };
  }
}

function summarizeStackedCase(rawCase) {
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

function summarizePaperProfileCase(rawCase) {
  const ok = rawCase?.ok === true;
  return {
    name: String(rawCase?.name || "paper-profile-journey"),
    status: ok ? "pass" : "fail",
    ok,
    route: rawCase?.route || null,
    url: rawCase?.url || null,
    profileId: rawCase?.profileId || null,
    pageCards: rawCase?.pageCards ?? null,
    claimRows: rawCase?.claimRows ?? null,
    truthFraming: rawCase?.truthFraming === true,
    readOnlyFraming: rawCase?.readOnlyFraming === true,
  };
}

function describeUpstream(script, command, prefix, result) {
  const combinedOutput = `${result.stdout || ""}\n${result.stderr || ""}`;
  const { parsed, parseError } = parseJsonLine(combinedOutput, prefix);
  return {
    script,
    command,
    exitCode: result.status,
    ok: result.status === 0 && parsed?.ok === true && !parseError,
    fromFixture: result.fromFixture,
    parseError,
    error: result.error ? result.error.message : null,
    outputTail: compactTail(combinedOutput),
    parsed,
    output: combinedOutput,
  };
}

function buildSummary(stackedResult, paperProfileResult, durationMs) {
  const stacked = describeUpstream(STACKED_SCRIPT, `npm run --silent ${STACKED_SCRIPT}`, STACKED_JSON_PREFIX, stackedResult);
  const paperProfile = describeUpstream(PAPER_PROFILE_SCRIPT, `npm run --silent ${PAPER_PROFILE_SCRIPT}`, PAPER_PROFILE_JSON_PREFIX, paperProfileResult);
  const stackedCases = Array.isArray(stacked.parsed?.cases) ? stacked.parsed.cases.map(summarizeStackedCase) : [];
  const paperProfileCase = paperProfile.parsed?.case ? [summarizePaperProfileCase(paperProfile.parsed.case)] : [];
  const cases = [...stackedCases, ...paperProfileCase];
  const failedCases = cases.filter((item) => !item.ok).map((item) => item.name);
  const parseErrors = [stacked, paperProfile]
    .filter((upstream) => upstream.parseError)
    .map((upstream) => `${upstream.script}: ${upstream.parseError}`);
  const upstreams = [stacked, paperProfile].map(({ parsed, output, ...safe }) => safe);
  const ok = stacked.ok && paperProfile.ok && cases.length > 0 && failedCases.length === 0 && parseErrors.length === 0;

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
    upstreams,
    upstream: upstreams[0],
    parseErrors,
  };
}

const startedAt = Date.now();
const stackedResult = runNpmScript(STACKED_SCRIPT, "WIKI_BROWSER_UX_SMOKE_FIXTURE_OUTPUT");
const paperProfileResult = runNpmScript(PAPER_PROFILE_SCRIPT, "WIKI_BROWSER_UX_SMOKE_PAPER_PROFILE_FIXTURE_OUTPUT");
const combinedOutput = [
  `${stackedResult.stdout || ""}${stackedResult.stderr ? `\n${stackedResult.stderr}` : ""}`.trim(),
  `${paperProfileResult.stdout || ""}${paperProfileResult.stderr ? `\n${paperProfileResult.stderr}` : ""}`.trim(),
].filter(Boolean).join("\n");
if (combinedOutput) console.log(combinedOutput);

const summary = buildSummary(stackedResult, paperProfileResult, Date.now() - startedAt);
console.log(
  `${summary.marker} passed=${summary.passed}/${summary.total} failed=${summary.failed} duration_ms=${summary.durationMs} upstream=${STACKED_SCRIPT},${PAPER_PROFILE_SCRIPT}`,
);
for (const parseError of summary.parseErrors) {
  console.log(`  parse_error=${parseError}`);
}
if (summary.failedCases.length > 0) {
  console.log(`  failed_cases=${summary.failedCases.join(",")}`);
}
console.log(`WIKI_BROWSER_UX_SMOKE_JSON ${JSON.stringify(summary)}`);
process.exit(summary.ok ? 0 : 1);
