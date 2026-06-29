import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

const repoRoot = path.resolve(import.meta.dirname, "..");
const routePath = path.join(repoRoot, "src/app/agent-reports/page58-label-upload/submit/route.ts");

assert.equal(fs.existsSync(routePath), true, "Page58 label-upload route file should exist");
const source = fs.readFileSync(routePath, "utf8");

assert.match(source, /export\s+const\s+runtime\s*=\s*["']nodejs["']/, "route must run in nodejs runtime for filesystem writes");
assert.match(source, /export\s+const\s+dynamic\s*=\s*["']force-dynamic["']/, "route must be dynamic so token state is not cached");
assert.match(source, /verifyUploadToken\(/, "route must verify one-time upload token");
assert.match(source, /MAX_UPLOAD_BYTES/, "route must enforce max upload size");
assert.match(source, /getUploadExtension\(/, "route must restrict uploads to JSON/CSV");
assert.match(source, /validateLabelUploadText\(/, "route must validate exported label content");
assert.match(source, /PAGE58_LABEL_UPLOAD_STATE/, "route must let tests/operators override token state path");
assert.match(source, /PAGE58_LABEL_UPLOAD_PUBLIC_DIR/, "route must let tests isolate uploaded output directory");
assert.match(source, /flag:\s*["']wx["']/, "route must use exclusive file creation for uploaded files");
assert.match(source, /export\s+async\s+function\s+GET\(/, "route must expose GET status check");
assert.match(source, /export\s+async\s+function\s+POST\(/, "route must expose POST upload path");
assert.match(source, /formData\(\)/, "route should receive multipart form uploads");
assert.match(source, /form\.get\(["']file["']\)/, "route should accept a single field named file");
assert.equal(/absolute_path\s*:/.test(source), false, "route must not expose server absolute paths in public or response metadata");

const forbidden = [
  /from\s+["']@\/app\/database["']/,
  /from\s+["'].*database["']/,
  /\bprisma\b/i,
  /\bsqlalchemy\b/i,
  /\bSessionLocal\b/,
  /\bdb\./,
  /\bexecute\s*\(/,
  /fetch\s*\(\s*["']\/api/,
];
for (const pattern of forbidden) {
  assert.equal(pattern.test(source), false, `route must not contain DB/API write surface: ${pattern}`);
}

console.log("page58_label_upload_route_contract_ok");
