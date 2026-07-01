import type { Metadata } from "next";
import type { CrossPagePaperFootprintResponse } from "../../[slug]/sources/crossPagePaperFootprint";
import PaperProfileClient from "../[paperId]/PaperProfileClient";
import type { PaperProfilePayload } from "../[paperId]/paperProfile";

const paperProfileFixture: PaperProfilePayload = {
  schema_version: "paper_profile.v1",
  paper_id: "arxiv:2606.990101",
  requested_paper_id: "arxiv:2606.990101",
  paper: {
    evidence_id: 9201,
    arxiv_id: "2606.990101",
    doi: null,
    url: "https://example.org/profile",
    title: "Paper profile fixture",
    authors: ["NebulaMind Fixture Harness"],
    year: 2026,
    summary: "A deterministic paper profile fixture with full wiki-wide footprint rows.",
    author_year_key: "Harness2026",
  },
  page_count: 3,
  claim_count: 4,
  evidence_count: 4,
  tone_counts: { support: 2, counter: 1, neutral: 1 },
  trust_counts: { accepted: 1, challenged: 1, debated: 1, unverified: 1 },
  vote_counts: { agree: 2, disagree: 1 },
  source_gap_count: 1,
  triage_status: "needs_adjudication",
  profile_summary: "3 pages · 4 claims · 1 countering",
  page_limit: 2,
  page_result_count: 2,
  pages_truncated: true,
  scope: { label: "paper profile", caveat: "Across indexed wiki evidence rows; this is not a final verdict. No labels are written." },
  directory_href: "/wiki/papers",
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

const paperFootprintFixture: CrossPagePaperFootprintResponse = {
  schema_version: "cross_page_paper_footprint.v1",
  paper: {
    evidence_id: 9201,
    arxiv_id: "2606.990101",
    doi: null,
    url: "https://example.org/footprint",
    title: "Cited across NebulaMind fixture",
    authors: ["NebulaMind Fixture Harness"],
    year: 2026,
    summary: "A deterministic paper-footprint fixture for the profile panel.",
    author_year_key: "Harness2026",
  },
  page_count: 2,
  claim_count: 3,
  evidence_count: 3,
  tone_counts: { support: 2, counter: 1, neutral: 0 },
  trust_counts: { accepted: 1, challenged: 1, debated: 1 },
  scope: { label: "wiki-wide paper footprint", caveat: "Across indexed wiki evidence rows; this is not a final verdict about which claim is correct." },
  pages: [
    {
      page_id: 990010,
      slug: "dust-obscured-galaxies",
      title: "Dust-obscured Galaxies",
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

export const metadata: Metadata = {
  title: "Paper Profile Fixture — NebulaMind",
  description: "Deterministic no-auth fixture for paper profile/detail smoke coverage.",
  robots: { index: false, follow: false },
};

export default function PaperProfileFixturePage() {
  return <PaperProfileClient paperId="arxiv:2606.990101" testOnlyFixtureData={paperProfileFixture} testOnlyFootprintData={paperFootprintFixture} />;
}
