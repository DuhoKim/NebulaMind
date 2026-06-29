import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/lib/agentReportUpload.ts");
const source = fs.readFileSync(helperPath, "utf8");
const compiled = ts.transpileModule(source, {
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
  MAX_UPLOAD_BYTES,
  getUploadExtension,
  sanitizeUploadFileName,
  buildStoredUploadName,
  validateLabelUploadText,
  verifyUploadToken,
} = module.exports;

assert.equal(MAX_UPLOAD_BYTES, 2 * 1024 * 1024);
assert.equal(getUploadExtension("labels.JSON", "application/octet-stream"), ".json");
assert.equal(getUploadExtension("labels.txt", "text/csv"), ".csv");
assert.equal(getUploadExtension("labels.txt", "application/pdf"), null);

assert.equal(sanitizeUploadFileName("../../page58 labels (done).json"), "page58-labels-done.json");
assert.equal(
  buildStoredUploadName({ timestamp: "20260626T063000Z", token: "abcdef1234567890", originalName: "../labels.csv" }),
  "page58_labels_upload_20260626T063000Z_abcdef12_labels.csv",
);

const validJson = JSON.stringify({
  source_packet: "page58_calibration_spot_check_latest",
  rows: [
    { sample_id: "VC-001", final_decision: "count_as_support" },
    { sample_id: "PC-001", human_action: "keep_vote", human_should_count: "yes_pro" },
  ],
});
const jsonResult = validateLabelUploadText(validJson, ".json");
assert.equal(jsonResult.ok, true);
assert.equal(jsonResult.kind, "json");
assert.equal(jsonResult.rowCount, 2);

const splitBadJsonRows = JSON.stringify({
  rows: [
    { sample_id: "VC-001" },
    { final_decision: "count_as_support" },
  ],
});
assert.equal(validateLabelUploadText(splitBadJsonRows, ".json").ok, false);
assert.match(validateLabelUploadText(splitBadJsonRows, ".json").error, /same row|row must/i);

const missingJsonSampleId = JSON.stringify({ rows: [{ final_decision: "count_as_support" }] });
assert.equal(validateLabelUploadText(missingJsonSampleId, ".json").ok, false);
assert.match(validateLabelUploadText(missingJsonSampleId, ".json").error, /sample_id/i);

const missingJsonDecision = JSON.stringify({ rows: [{ sample_id: "VC-001" }] });
assert.equal(validateLabelUploadText(missingJsonDecision, ".json").ok, false);
assert.match(validateLabelUploadText(missingJsonDecision, ".json").error, /final_decision|human_action/i);

const validCsv = [
  "sample_id,final_decision,human_notes",
  "VC-001,count_as_weakening,looks real",
  "PC-001,drop_no_effect,topic only",
].join("\n");
const csvResult = validateLabelUploadText(validCsv, ".csv");
assert.equal(csvResult.ok, true);
assert.equal(csvResult.kind, "csv");
assert.equal(csvResult.rowCount, 2);

assert.match(validateLabelUploadText("sample_id,final_decision\n,count_as_support", ".csv").error, /sample_id/i);
assert.match(validateLabelUploadText("sample_id,final_decision\nVC-001,", ".csv").error, /final_decision|human_action/i);

assert.equal(validateLabelUploadText("{}", ".json").ok, false);
assert.match(validateLabelUploadText("not json", ".json").error, /valid JSON/i);
assert.match(validateLabelUploadText("sample_id,notes\nVC-001,x", ".csv").error, /final_decision|human_action/i);
assert.match(validateLabelUploadText("", ".csv").error, /empty/i);

const tokenState = { token: "secret-token", expires_at: "2030-01-01T00:00:00.000Z" };
assert.equal(verifyUploadToken("secret-token", tokenState, new Date("2026-01-01T00:00:00.000Z")).ok, true);
assert.equal(verifyUploadToken("wrong", tokenState, new Date("2026-01-01T00:00:00.000Z")).status, 401);
assert.equal(verifyUploadToken("secret-token", { ...tokenState, used_at: "2026-01-01T00:00:00.000Z" }, new Date("2026-01-01T00:00:00.000Z")).status, 410);
assert.equal(verifyUploadToken("secret-token", { ...tokenState, expires_at: "2020-01-01T00:00:00.000Z" }, new Date("2026-01-01T00:00:00.000Z")).status, 410);

console.log("agent_report_upload_helper_ok");
