import type { Metadata } from "next";
import WikiPageClient from "../[slug]/WikiPageClient";
import { sourceTraceBrowserFixtureData } from "./fixtureData";

export const metadata: Metadata = {
  title: "Source Trace Browser Fixture — NebulaMind",
  description: "Deterministic frontend fixture for browser-level source trace Escape sequencing smoke tests.",
  robots: { index: false, follow: false },
};

export default function SourceTraceBrowserFixturePage() {
  return (
    <WikiPageClient
      testOnlyFixtureSlug="source-trace-browser-fixture"
      testOnlyFixtureData={sourceTraceBrowserFixtureData}
    />
  );
}
