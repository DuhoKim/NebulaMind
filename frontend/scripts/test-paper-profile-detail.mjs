import assert from "node:assert/strict";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import ts from "typescript";

const require = createRequire(import.meta.url);
const repoRoot = path.resolve(import.meta.dirname, "..");
const helperPath = path.join(repoRoot, "src/app/wiki/papers/[paperId]/paperProfile.ts");
const clientPath = path.join(repoRoot, "src/app/wiki/papers/[paperId]/PaperProfileClient.tsx");
const pagePath = path.join(repoRoot, "src/app/wiki/papers/[paperId]/page.tsx");
const fixturePath = path.join(repoRoot, "src/app/wiki/papers/profile-fixture/page.tsx");
const directoryHelperPath = path.join(repoRoot, "src/app/wiki/papers/globalPaperDirectory.ts");
const directoryClientPath = path.join(repoRoot, "src/app/wiki/papers/GlobalPaperDirectoryClient.tsx");
const packagePath = path.join(repoRoot, "package.json");
const aggregatePath = path.join(repoRoot, "scripts/test-wiki-ux-smoke.mjs");

assert.ok(fs.existsSync(helperPath), "Paper profile helper should live under /wiki/papers/[paperId].");

const helperSource = fs.readFileSync(helperPath, "utf8");
const compiled = ts.transpileModule(helperSource, {
  compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2019, strict: true },
  fileName: helperPath,
});
const module = { exports: {} };
vm.runInNewContext(compiled.outputText, { module, exports: module.exports, require }, { filename: helperPath });

const { buildPaperProfileDeck, normalizePaperProfileStatus, encodePaperProfileId } = module.exports;
assert.equal(typeof buildPaperProfileDeck, "function");
assert.equal(typeof normalizePaperProfileStatus, "function");
assert.equal(typeof encodePaperProfileId, "function");
assert.equal(normalizePaperProfileStatus({ counterCount: 1, trustCounts: {} }), "needs_adjudication");
assert.equal(normalizePaperProfileStatus({ counterCount: 0, trustCounts: { unverified: 1 }, hasStableIdentifier: true }), "needs_source");
assert.equal(normalizePaperProfileStatus({ counterCount: 0, trustCounts: { accepted: 1 }, hasStableIdentifier: true }), "ready_to_review");
assert.equal(encodePaperProfileId({ arxiv_id: "2606.990101" }), "arxiv:2606.990101");
assert.equal(encodePaperProfileId({ evidence_id: 9203 }), "evidence:9203");

const payload = {
  schema_version: "paper_profile.v1",
  paper_id: "arxiv:2606.990101",
  paper: {
    evidence_id: 9201,
    arxiv_id: "2606.990101",
    doi: null,
    url: "https://example.org/profile",
    title: "Paper profile fixture",
    authors: ["NebulaMind Fixture Harness"],
    year: 2026,
    summary: "A deterministic paper profile fixture with full wiki footprint rows.",
    author_year_key: "Harness2026",
  },
  page_count: 2,
  claim_count: 3,
  evidence_count: 3,
  tone_counts: { support: 2, counter: 1, neutral: 0 },
  trust_counts: { accepted: 1, challenged: 1, debated: 1 },
  vote_counts: { agree: 2, disagree: 1 },
  source_gap_count: 0,
  triage_status: "needs_adjudication",
  profile_summary: "2 pages · 3 claims · 1 countering",
  scope: { label: "paper profile", caveat: "Across indexed wiki evidence rows; this is not a final verdict. No labels are written." },
  pages_truncated: false,
  pages: [
    {
      page_id: 990010,
      slug: "dust-obscured-galaxies",
      title: "Dust-obscured Galaxies",
      href: "/wiki/dust-obscured-galaxies",
      claim_count: 1,
      evidence_count: 1,
      support_count: 0,
      counter_count: 1,
      neutral_count: 0,
      claims: [
        { claim_id: 9900101, claim_text: "Dust obscuration counters the headline census.", section: "Dust", trust_level: "challenged", evidence_id: 9202, stance: "contradicting", status: "active", tone: "counter", href: "/wiki/dust-obscured-galaxies#claim-9900101", votes_agree: 0, votes_disagree: 1 },
      ],
    },
    {
      page_id: 990000,
      slug: "early-galaxies",
      title: "Early Galaxies",
      href: "/wiki/early-galaxies",
      claim_count: 2,
      evidence_count: 2,
      support_count: 2,
      counter_count: 0,
      neutral_count: 0,
      claims: [
        { claim_id: 9900001, claim_text: "The fixture supports early assembly.", section: "Assembly", trust_level: "accepted", evidence_id: 9201, stance: "supporting", status: "active", tone: "support", href: "/wiki/early-galaxies#claim-9900001", votes_agree: 2, votes_disagree: 0 },
        { claim_id: 9900002, claim_text: "The fixture also supports high-redshift number density.", section: "Counts", trust_level: "debated", evidence_id: 9204, stance: "supporting", status: "active", tone: "support", href: "/wiki/early-galaxies#claim-9900002", votes_agree: 0, votes_disagree: 0 },
      ],
    },
  ],
};

const deck = buildPaperProfileDeck(payload);
assert.equal(deck.hasProfile, true);
assert.equal(deck.paperLabel, "Harness2026");
assert.equal(deck.statusLabel, "Needs adjudication");
assert.equal(deck.pageCount, 2);
assert.equal(deck.claimCount, 3);
assert.equal(deck.counterCount, 1);
assert.equal(deck.sourceGapCount, 0);
assert.match(deck.summary, /2 pages · 3 claims · 1 countering/i);
assert.match(deck.scopeCaveat, /not a final verdict/i);
assert.equal(deck.pages[0].slug, "dust-obscured-galaxies", "Countering pages should sort first.");
assert.equal(deck.pages[0].claims[0].toneLabel, "Countering");
assert.match(deck.pages[0].claims[0].accessibleSummary, /Dust-obscured Galaxies.*Countering.*challenged/i);
assert.equal(deck.externalHref, "https://example.org/profile");

const truncatedDeck = buildPaperProfileDeck({ ...payload, pages_truncated: true, page_count: 9, pages: payload.pages.slice(0, 1) });
assert.match(truncatedDeck.truncationDisclosure, /Showing 1 of 9 page footprints/i);
assert.match(truncatedDeck.truncationDisclosure, /not a final verdict/i);

const emptyDeck = buildPaperProfileDeck({ schema_version: "paper_profile.v1", paper_id: "arxiv:missing", paper: {}, pages: [] });
assert.equal(emptyDeck.hasProfile, false);
assert.match(emptyDeck.emptyMessage, /No paper profile footprint is available/i);

const unknownDeck = buildPaperProfileDeck({ ...payload, schema_version: "paper_profile.v2" });
assert.equal(unknownDeck.hasProfile, false, "Unknown future schemas should not render stale profile data.");

const clientSource = fs.readFileSync(clientPath, "utf8");
assert.match(clientSource, /data-testid="paper-profile-detail"/, "Profile route should expose a stable wrapper selector.");
assert.match(clientSource, /data-testid="paper-profile-status-chip"/, "Profile status should have a stable selector.");
assert.match(clientSource, /data-testid="paper-profile-scope-caveat"/, "Truth-framing caveat should render.");
assert.match(clientSource, /data-testid="paper-profile-page-card"/, "Page footprint cards should have stable selectors.");
assert.match(clientSource, /data-testid="paper-profile-claim-row"/, "Claim rows should have stable selectors.");
assert.match(clientSource, /data-testid="paper-profile-truncation-disclosure"/, "Truncated profile payloads should disclose hidden rows.");
assert.match(clientSource, /fetch\(`\/api\/pages\/paper-profile/, "Client should fetch the read-only paper profile endpoint.");
assert.match(clientSource, /not a final verdict/i, "Profile copy should avoid truth adjudication.");
assert.match(clientSource, /No labels are written/i, "Profile should be explicit that it is read-only.");
assert.match(clientSource, /aria-label=\{claim\.accessibleSummary\}/, "Claim rows should expose tone/trust/page context to assistive tech.");

assert.ok(fs.existsSync(pagePath), "Dynamic paper profile page route should exist.");
assert.ok(fs.existsSync(fixturePath), "Paper profile fixture route should exist for deterministic route/chunk probes.");
const fixtureSource = fs.readFileSync(fixturePath, "utf8");
assert.match(fixtureSource, /paper_profile\.v1/, "Fixture should carry production-like paper profile payload.");
assert.match(fixtureSource, /Paper profile fixture/, "Fixture should include a deterministic paper profile title.");

const directoryHelperSource = fs.readFileSync(directoryHelperPath, "utf8");
assert.match(directoryHelperSource, /profileHref/, "Global directory helper should expose a paper profile link.");
const directoryClientSource = fs.readFileSync(directoryClientPath, "utf8");
assert.match(directoryClientSource, /data-testid="global-paper-profile-link"/, "Directory cards should link directly to paper profiles.");

const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
assert.equal(packageJson.scripts["test:paper-profile-detail"], "node scripts/test-paper-profile-detail.mjs");

const aggregateSource = fs.readFileSync(aggregatePath, "utf8");
assert.match(aggregateSource, /test:paper-profile-detail/, "Wiki UX aggregate smoke should include the paper profile probe.");
assert.match(aggregateSource, /paper_profile_detail_ok/, "Wiki UX aggregate smoke should expect the profile marker.");

console.log("paper_profile_detail_ok");
