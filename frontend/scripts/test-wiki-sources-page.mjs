import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

const repoRoot = path.resolve(import.meta.dirname, "..");
const sourcesClientPath = path.join(repoRoot, "src/app/wiki/[slug]/sources/WikiSourcesClient.tsx");
const source = fs.readFileSync(sourcesClientPath, "utf8");

assert.doesNotMatch(
  source,
  /const\s+heroSources\s*=\s*sources\.filter\(s\s*=>\s*s\.fact_kind\s*===\s*"hero"\)/,
  "Sources page must not hide claim/evidence source rows behind a hero-only filter",
);

assert.doesNotMatch(
  source,
  /renderSources\(heroSources,\s*"Hero Facts"\)/,
  "Sources page must not render only legacy hero fact sources",
);

assert.match(
  source,
  /renderSources\(sources,\s*"Claim and Page Sources"\)/,
  "Sources page should render all returned fact-source records, including claim/evidence rows",
);

assert.match(
  source,
  /\{sources\.length\}\s+\{sourceRecordLabel\}/,
  "Header should describe generic source records, not sourced facts",
);

assert.match(source, /source records/i);
assert.doesNotMatch(source, /sourced facts/i);
assert.match(source, /source_tier === "claim"/);
assert.match(source, /claim #\{s\.claim_id\}/);
assert.match(source, /arXiv:\{s\.representative_arxiv_id\}/);
assert.match(source, /No source records found for this page yet\./);

console.log("wiki_sources_page_smoke_ok");
