import type { Metadata } from "next";
import WikiSourcesClient, { type WikiSourcesClientTestOnlyFixtureData } from "../../[slug]/sources/WikiSourcesClient";

const sourceTraceSourcesFixtureData = {
  page: {
    title: "Source Trace Browser Fixture",
    slug: "source-trace-browser-fixture",
  },
  sources: [
    {
      id: 990501,
      fact_kind: "hero",
      fact_index: 0,
      source_tier: "claim",
      authority: null,
      reference_url: null,
      reference_title: null,
      retrieval_year: null,
      claim_id: 990001,
      trust_level_snapshot: "debated",
      evidence_count_snapshot: 2,
      representative_arxiv_id: "2606.990101",
      attribution: "NebulaMind fixture claim (debated, 2 papers)",
      flagged: false,
      reason: null,
    },
  ],
  citations: [
    {
      evidence_id: 990101,
      author_year_key: "Fixture2026",
      title: "Deterministic source-trace fixture for stacked Escape browser smoke",
      arxiv_id: "2606.990101",
      url: "https://example.org/nebulamind/source-trace-fixture",
    },
    {
      evidence_id: 990102,
      author_year_key: "FixtureNull2026",
      title: "Nullable source-trace fixture citation",
      arxiv_id: null,
      url: null,
    },
  ],
  crossPageFootprints: [
    {
      schema_version: "cross_page_paper_footprint.v1",
      paper: {
        evidence_id: 990101,
        arxiv_id: "2606.990101",
        title: "Deterministic source-trace fixture for stacked Escape browser smoke",
        authors: ["NebulaMind Fixture Harness", "Hermes QA"],
        year: 2026,
        url: "https://example.org/nebulamind/source-trace-fixture",
        author_year_key: "Fixture2026",
        summary: "A deterministic cross-page paper footprint fixture used to verify source-page rendering.",
      },
      page_count: 2,
      claim_count: 2,
      evidence_count: 2,
      tone_counts: { support: 1, counter: 1, neutral: 0 },
      trust_counts: { debated: 1, challenged: 1 },
      scope: {
        label: "wiki-wide paper footprint",
        caveat: "Across indexed wiki evidence rows; this is not a final verdict about which claim is correct.",
      },
      pages: [
        {
          page_id: 990000,
          slug: "source-trace-browser-fixture",
          title: "Source Trace Browser Fixture",
          claim_count: 1,
          evidence_count: 1,
          support_count: 1,
          counter_count: 0,
          neutral_count: 0,
          claims: [
            {
              claim_id: 990001,
              claim_text: "A browser smoke can keep an evidence panel open while closing only the top source trace hover card.",
              section: "Fixture",
              trust_level: "debated",
              evidence_id: 990101,
              stance: "supporting",
              status: "accepted",
              tone: "support",
              href: "/wiki/source-trace-browser-fixture#claim-990001",
              votes_agree: 3,
              votes_disagree: 0,
            },
          ],
        },
        {
          page_id: 990010,
          slug: "cross-page-paper-footprint-fixture",
          title: "Cross-page Paper Footprint Fixture",
          claim_count: 1,
          evidence_count: 1,
          support_count: 0,
          counter_count: 1,
          neutral_count: 0,
          claims: [
            {
              claim_id: 990011,
              claim_text: "The same fixture paper can surface counter-pressure on another page.",
              section: "Cross-page",
              trust_level: "challenged",
              evidence_id: 990111,
              stance: "contradicting",
              status: "active",
              tone: "counter",
              href: "/wiki/cross-page-paper-footprint-fixture#claim-990011",
              votes_agree: 0,
              votes_disagree: 2,
            },
          ],
        },
      ],
    },
  ],
} satisfies WikiSourcesClientTestOnlyFixtureData;

export const metadata: Metadata = {
  title: "Source Trace Sources Fixture — NebulaMind",
  description: "Deterministic source-page fixture for cross-page paper footprint smoke coverage.",
  robots: { index: false, follow: false },
};

export default function SourceTraceSourcesFixturePage() {
  return (
    <WikiSourcesClient
      testOnlyFixtureSlug="source-trace-browser-fixture"
      testOnlyFixtureData={sourceTraceSourcesFixtureData}
    />
  );
}
