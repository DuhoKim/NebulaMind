import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/evidenceStatus.ts");
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

const { evidenceStatusMeta } = module.exports;
assert.equal(typeof evidenceStatusMeta, "function");

const provisional = evidenceStatusMeta("provisional");
assert.equal(provisional.label, "provisional");
assert.equal(provisional.trustBlocking, true);
assert.match(provisional.detail, /not in trust/i);
assert.match(provisional.detail, /promoted/i);
assert.equal(provisional.tone, "amber");

const active = evidenceStatusMeta("active");
assert.equal(active.label, "active");
assert.equal(active.trustBlocking, false);
assert.match(active.detail, /included in trust/i);
assert.equal(active.tone, "green");

const missing = evidenceStatusMeta(null);
assert.equal(missing.label, "active");
assert.equal(missing.trustBlocking, false);

const normalized = evidenceStatusMeta(" PROVISIONAL ");
assert.equal(normalized.label, "provisional");
assert.equal(normalized.trustBlocking, true);

console.log("evidence_status_helper_ok");
