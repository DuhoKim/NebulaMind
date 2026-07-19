import type { Metadata } from "next";
import GlobalPaperDirectoryClient from "../GlobalPaperDirectoryClient";
import type { GlobalPaperDirectoryPayload } from "../globalPaperDirectory";

const globalPaperDirectoryFixture: GlobalPaperDirectoryPayload = {
  schema_version: "global_paper_directory.v1",
  query: "",
  limit: 25,
  total_papers: 4,
  result_count: 3,
  scope: {
    label: "global paper directory",
    caveat: "Across indexed wiki evidence rows; directory/search, not a final verdict. No labels are written.",
  },
  items: [
    {
      paper: {
        evidence_id: 990101,
        arxiv_id: "2606.990101",
        doi: null,
        url: "https://example.org/counter-paper",
        title: "Counter-pressure directory fixture",
        authors: ["NebulaMind Fixture Harness"],
        year: 2026,
        summary: "A deterministic fixture paper with counter-pressure across wiki pages.",
        author_year_key: "Harness2026",
      },
      page_count: 2,
      claim_count: 3,
      evidence_count: 3,
      tone_counts: { support: 2, counter: 1, neutral: 0 },
      trust_counts: { accepted: 1, challenged: 1, debated: 1 },
      triage_status: "needs_adjudication",
      impact_label: "2 pages · 3 claims · 1 countering",
      pages: [
        { page_id: 990010, slug: "dust-obscured-galaxies", title: "Dust-obscured Galaxies", href: "/wiki/dust-obscured-galaxies", claim_count: 1, evidence_count: 1, support_count: 0, counter_count: 1, neutral_count: 0 },
        { page_id: 990000, slug: "early-galaxies", title: "Early Galaxies", href: "/wiki/early-galaxies", claim_count: 2, evidence_count: 2, support_count: 2, counter_count: 0, neutral_count: 0 },
      ],
    },
    {
      paper: {
        evidence_id: 990102,
        arxiv_id: "2606.123456",
        doi: null,
        url: "https://example.org/ready-paper",
        title: "Synthesis-ready directory fixture",
        authors: ["Ready Reviewer"],
        year: 2025,
        summary: "A deterministic supporting fixture paper for ready-to-review directory rows.",
        author_year_key: "Reviewer2025",
      },
      page_count: 1,
      claim_count: 1,
      evidence_count: 1,
      tone_counts: { support: 1, counter: 0, neutral: 0 },
      trust_counts: { accepted: 1 },
      triage_status: "ready_to_review",
      impact_label: "1 page · 1 claim · 0 countering",
      pages: [
        { page_id: 990020, slug: "stellar-halos", title: "Stellar Halos", href: "/wiki/stellar-halos", claim_count: 1, evidence_count: 1, support_count: 1, counter_count: 0, neutral_count: 0 },
      ],
    },
    {
      paper: {
        evidence_id: 990103,
        arxiv_id: null,
        doi: null,
        url: null,
        title: "Unindexed source gap fixture",
        authors: [],
        year: null,
        summary: null,
        author_year_key: "Unindexed source gap fixture",
      },
      page_count: 1,
      claim_count: 1,
      evidence_count: 1,
      tone_counts: { support: 0, counter: 0, neutral: 1 },
      trust_counts: { unverified: 1 },
      triage_status: "needs_source",
      impact_label: "1 page · 1 claim · 0 countering",
      pages: [
        { page_id: 990030, slug: "source-gaps", title: "Source Gaps", href: "/wiki/source-gaps", claim_count: 1, evidence_count: 1, support_count: 0, counter_count: 0, neutral_count: 1 },
      ],
    },
  ],
};

export const metadata: Metadata = {
  title: "Global Paper Directory Fixture — NebulaMind",
  description: "Deterministic no-auth fixture for global paper directory smoke coverage.",
  robots: { index: false, follow: false },
};

export default function GlobalPaperDirectoryFixturePage() {
  return <GlobalPaperDirectoryClient testOnlyFixtureData={globalPaperDirectoryFixture} />;
}
