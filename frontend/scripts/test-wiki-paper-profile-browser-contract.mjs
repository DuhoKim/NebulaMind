import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const frontendRoot = path.resolve(import.meta.dirname, "..");
const packagePath = path.join(frontendRoot, "package.json");
const browserScriptPath = path.join(frontendRoot, "scripts/test-wiki-paper-profile-browser.mjs");
const browserAggregatePath = path.join(frontendRoot, "scripts/test-wiki-browser-ux-smoke.mjs");
const browserAggregateContractPath = path.join(frontendRoot, "scripts/test-wiki-browser-ux-smoke-contract.mjs");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(
  packageJson.scripts["smoke:wiki-paper-profile-browser"],
  "node scripts/test-wiki-paper-profile-browser.mjs",
  "Package should expose the real paper-profile browser journey smoke.",
);
assert.equal(
  packageJson.scripts["smoke:wiki-paper-profile-browser:contract"],
  "node scripts/test-wiki-paper-profile-browser-contract.mjs",
  "Package should expose a focused source contract for the paper-profile browser journey smoke.",
);
assert.ok(fs.existsSync(browserScriptPath), "Paper-profile browser smoke script should exist.");

const browserSource = fs.readFileSync(browserScriptPath, "utf8");
assert.match(browserSource, /\/wiki\/papers/, "Browser smoke should start from the global paper directory route.");
assert.match(browserSource, /global-paper-profile-link/, "Browser smoke should click a directory profile link instead of deep-linking first.");
assert.match(browserSource, /paper-profile-detail/, "Browser smoke should wait for the dynamic paper profile page.");
assert.match(browserSource, /paper-profile-page-card/, "Browser smoke should require rendered page footprint cards.");
assert.match(browserSource, /paper-profile-claim-row/, "Browser smoke should require rendered claim footprint rows.");
assert.match(browserSource, /not a final verdict/, "Browser smoke should lock truth-framing copy.");
assert.match(browserSource, /No labels are written/, "Browser smoke should lock read-only copy.");
assert.match(browserSource, /PAPER_PROFILE_BROWSER_OK/, "Browser smoke should emit a stable dashboard OK marker.");
assert.match(browserSource, /PAPER_PROFILE_BROWSER_JSON/, "Browser smoke should emit one parseable JSON summary line.");
assert.match(browserSource, /directoryCardsBeforeNavigation/, "Browser smoke should preserve pre-navigation directory card count separately from profile-page state.");
assert.match(browserSource, /paper_profile_browser\.v1/, "Browser smoke JSON should use an explicit schema version.");
assert.match(browserSource, /WIKI_PAPER_PROFILE_ONLY/, "Browser smoke should support a narrow scenario filter for future growth.");

const aggregateSource = fs.readFileSync(browserAggregatePath, "utf8");
assert.match(aggregateSource, /smoke:wiki-paper-profile-browser/, "Browser aggregate should run the paper-profile browser journey smoke.");
assert.match(aggregateSource, /PAPER_PROFILE_BROWSER_JSON/, "Browser aggregate should parse paper-profile browser JSON.");
assert.match(aggregateSource, /paper-profile-journey/, "Browser aggregate summary should include the paper-profile journey case.");
assert.match(aggregateSource, /WIKI_BROWSER_UX_SMOKE_PAPER_PROFILE_FIXTURE_OUTPUT/, "Browser aggregate contract should be able to fixture paper-profile output without launching Chrome.");

const aggregateContractSource = fs.readFileSync(browserAggregateContractPath, "utf8");
assert.match(aggregateContractSource, /PAPER_PROFILE_BROWSER_JSON/, "Browser aggregate contract should fixture paper-profile JSON.");
assert.match(aggregateContractSource, /paper-profile-journey/, "Browser aggregate contract should expect the paper-profile journey case.");

const fixtureOutput = [
  "PAPER_PROFILE_BROWSER_OK profile_id=arxiv:2606.990101 route=/wiki/papers/arxiv%3A2606.990101 page_cards=2 claim_rows=3",
  'PAPER_PROFILE_BROWSER_JSON {"schemaVersion":"paper_profile_browser.v1","ok":true,"case":{"name":"paper-profile-journey","ok":true,"route":"/wiki/papers/arxiv%3A2606.990101","profileId":"arxiv:2606.990101","directoryCards":2,"pageCards":2,"claimRows":3,"truthFraming":true,"readOnlyFraming":true}}',
].join("\n");
const fixturePath = path.join(os.tmpdir(), `paper-profile-browser-fixture-${process.pid}.log`);
fs.writeFileSync(fixturePath, fixtureOutput, "utf8");
try {
  const result = spawnSync(process.execPath, [browserScriptPath], {
    cwd: frontendRoot,
    encoding: "utf8",
    env: { ...process.env, WIKI_PAPER_PROFILE_BROWSER_FIXTURE_OUTPUT: fixturePath },
  });
  assert.equal(result.status, 0, `Fixture paper-profile browser run should pass. stdout=${result.stdout}\nstderr=${result.stderr}`);
  assert.match(result.stdout, /PAPER_PROFILE_BROWSER_OK profile_id=arxiv:2606\.990101/, "Fixture run should echo stable OK marker.");
  const jsonLine = result.stdout.split(/\r?\n/).find((line) => line.startsWith("PAPER_PROFILE_BROWSER_JSON "));
  assert.ok(jsonLine, `Fixture run should emit PAPER_PROFILE_BROWSER_JSON. stdout=${result.stdout}`);
  const summary = JSON.parse(jsonLine.replace("PAPER_PROFILE_BROWSER_JSON ", ""));
  assert.equal(summary.schemaVersion, "paper_profile_browser.v1");
  assert.equal(summary.ok, true);
  assert.equal(summary.case.name, "paper-profile-journey");
  assert.equal(summary.case.truthFraming, true);
  assert.equal(summary.case.readOnlyFraming, true);
} finally {
  fs.rmSync(fixturePath, { force: true });
}

console.log("wiki_paper_profile_browser_contract_ok");
