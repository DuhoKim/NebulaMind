import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const root = process.cwd();
const scopePath = path.join(root, "src/app/lab/frontierScope.ts");
const dataPath = path.join(root, "src/app/lab/frontiersData.ts");
const rankingPath = path.join(root, "src/app/lab/LabStages.tsx");
const boardPath = path.join(root, "src/app/lab/DraftBoard.tsx");
const stageDataPath = path.join(root, "src/app/lab/stageData.ts");
const flagshipPath = path.join(root, "src/app/lab/FlagshipStudies.tsx");
const draftsPath = path.join(root, "src/app/lab/FrontierDrafts.tsx");
const packagePath = path.join(root, "package.json");

assert.ok(fs.existsSync(scopePath), "A hand-maintained Galaxy Evolution scope policy module should exist.");

function loadTypeScriptModule(filePath) {
  const source = fs.readFileSync(filePath, "utf8");
  const compiled = ts.transpileModule(source, {
    compilerOptions: {
      module: ts.ModuleKind.CommonJS,
      target: ts.ScriptTarget.ES2019,
      strict: true,
    },
    fileName: filePath,
  });
  const loaded = { exports: {} };
  vm.runInNewContext(
    compiled.outputText,
    { module: loaded, exports: loaded.exports },
    { filename: filePath },
  );
  return loaded.exports;
}

const scope = loadTypeScriptModule(scopePath);
const data = loadTypeScriptModule(dataPath);
const allClusterIds = data.FRONTIERS.map((frontier) => frontier.cluster).sort((a, b) => a - b);
const classifiedIds = Object.values(scope.GALAXY_EVOLUTION_SCOPE_IDS)
  .flat()
  .sort((a, b) => a - b);
assert.deepEqual(
  Array.from(classifiedIds),
  Array.from(allClusterIds),
  "Every generated frontier cluster must have exactly one explicit scope classification.",
);
assert.equal(new Set(classifiedIds).size, classifiedIds.length, "A frontier cannot appear in multiple scope classes.");
assert.equal(scope.galaxyEvolutionScope(999), "out_of_scope", "Unknown future clusters must fail closed.");

for (const cluster of [41, 40, 35, 19, 56, 17, 46, 27]) {
  assert.equal(scope.galaxyEvolutionScope(cluster), "core", `Cluster ${cluster} should remain in the core ranking.`);
}
for (const cluster of [4, 13, 16, 28, 31, 50, 51, 53, 55]) {
  assert.notEqual(scope.galaxyEvolutionScope(cluster), "core", `Known scope-leak cluster ${cluster} must not enter the core ranking.`);
}

const rankedCore = scope.coreGalaxyEvolutionFrontiers(data.FRONTIERS);
assert.deepEqual(
  Array.from(rankedCore.slice(0, 8), (frontier) => frontier.cluster),
  [41, 40, 35, 19, 56, 17, 46, 27],
  "The displayed core ranking must be deterministic and exclude adjacent stellar/transient topics.",
);
assert.ok(rankedCore.every((frontier) => frontier.scoreV1 > 0), "Core ranking rows must carry a positive controversy score.");

const flagshipSource = fs.readFileSync(flagshipPath, "utf8");
const draftsSource = fs.readFileSync(draftsPath, "utf8");
const curatedFrontiers = [...flagshipSource.matchAll(/frontier:\s*(\d+)/g), ...draftsSource.matchAll(/frontier:\s*(\d+)/g)]
  .map((match) => Number(match[1]));
assert.ok(curatedFrontiers.length > 0, "The curated PDF portfolio should expose frontier IDs.");
assert.ok(
  curatedFrontiers.every((cluster) => scope.galaxyEvolutionScope(cluster) !== "out_of_scope"),
  "Curated PDFs may be core or adjacent, but none should be presented from outside the Galaxy Evolution boundary.",
);
assert.equal(scope.galaxyEvolutionScope(16), "adjacent", "The reionization/Lyα draft should be labeled adjacent rather than core.");

const rankingSource = fs.readFileSync(rankingPath, "utf8");
assert.match(rankingSource, /from "\.\/frontierScope"/, "Ranking should import the shared scope policy.");
assert.match(
  rankingSource,
  /const CONTESTED = coreGalaxyEvolutionFrontiers\(FRONTIERS\)\.slice\(0, 8\)/,
  "The contested-topic list should be core-only.",
);
assert.match(
  rankingSource,
  /isCoreGalaxyEvolutionFrontier\(cid\)/,
  "The contested map overlay should darken adjacent and out-of-scope clusters.",
);
assert.match(
  rankingSource,
  /const CORE_RANK_BY_CID = new Map/,
  "Rank-mode tooltips should use the scoped ranking rather than the broad activity order.",
);
assert.match(
  rankingSource,
  /mode === "rank" && coreRank/,
  "The scoped tooltip rank should be rendered only in rank mode.",
);
assert.doesNotMatch(
  rankingSource,
  /The top galaxy-evolution frontiers become the studies/,
  "The supporting measurement shortlist must not claim adjacent probes seed ranked studies.",
);
assert.match(
  rankingSource,
  /core \+ adjacent measurement shortlist/i,
  "The hand-written measurement shortlist should disclose that it includes adjacent probes.",
);

const boardSource = fs.readFileSync(boardPath, "utf8");
assert.match(boardSource, /from "\.\/frontierScope"/, "Paper board should import the shared scope policy.");
assert.match(
  boardSource,
  /coreGalaxyEvolutionFrontiers\(FRONTIERS\)/,
  "Open-study suggestions should be seeded only from the core ranking.",
);
assert.match(boardSource, /core Galaxy Evolution/i, "The Paper board should name the core-only boundary plainly.");
assert.match(boardSource, /data-scope=\{scope\}/, "Frontier-grouped papers should expose their core/adjacent scope classification.");
assert.match(boardSource, /adjacent · supporting/, "Adjacent papers should be labeled plainly rather than hidden.");

const stageDataSource = fs.readFileSync(stageDataPath, "utf8");
assert.doesNotMatch(
  stageDataSource,
  /black-hole accretion, LyC escape and quenching rise to the top and become the studies/,
  "The Ranking intro must not promote adjacent probes as core study seeds.",
);
assert.match(
  stageDataSource,
  /Only hand-reviewed core Galaxy Evolution clusters enter the ranked study shortlist/,
  "The Ranking intro should state the strict study-seeding boundary.",
);
assert.doesNotMatch(stageDataSource, /ranked study queue/, "The UI must not imply a backend study queue that does not exist.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(
  packageJson.scripts["test:galaxy-frontier-scope"],
  "node scripts/test-galaxy-frontier-scope.mjs",
  "The focused scope contract should be available as a package script.",
);

console.log("galaxy_frontier_scope_ok");
