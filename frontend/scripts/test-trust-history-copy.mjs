import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/[slug]/trustHistoryCopy.ts");
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

const { formatHiddenRecomputes, formatTrustHistoryStats, emptyTrustHistoryText } = module.exports;
assert.equal(typeof formatHiddenRecomputes, "function");
assert.equal(typeof formatTrustHistoryStats, "function");

assert.equal(formatHiddenRecomputes(0), "0 recomputes hidden");
assert.equal(formatHiddenRecomputes(1), "1 recompute hidden");
assert.equal(formatHiddenRecomputes(2), "2 recomputes hidden");
assert.equal(formatHiddenRecomputes(null), "0 recomputes hidden");

assert.equal(
  formatTrustHistoryStats({ total_raw_rows: 3, events_returned: 2, noise_filtered: 1 }),
  "3 raw events → 2 timeline events · 1 recompute hidden",
);
assert.equal(
  formatTrustHistoryStats({ total_raw_rows: 1, events_returned: 1, noise_filtered: 0 }),
  "1 raw event → 1 timeline event · 0 recomputes hidden",
);
assert.match(emptyTrustHistoryText, /timeline events/i);
assert.doesNotMatch(emptyTrustHistoryText, /level transitions/i);

console.log("trust_history_copy_helper_ok");
