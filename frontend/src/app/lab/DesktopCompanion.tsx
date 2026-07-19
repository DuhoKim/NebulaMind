"use client";

import { useTab, useSub } from "./labTabStore";

// The Astro-Note AI companion card — a landing recommendation, so it shows only
// on the Topic overview (the pipeline home), not on every sub-nav step page.
export default function DesktopCompanion() {
  const tab = useTab();
  const sub = useSub();
  if (!(tab === "topic" && sub === "")) return null;
  return (
    <section className="lab-sec">
      <p className="lab-kicker">Desktop companion</p>
      <a className="lab-card" href="https://github.com/star4citizen/Astro-NoteAI" target="_blank" rel="noopener noreferrer">
        <div className="row">
          <h3>Astro-Note AI — turn your own papers into a local LLM wiki</h3>
          <span className="tag">open source · macOS/Win/Linux</span>
        </div>
        <p>
          An open-source desktop app that turns your research-paper PDFs into a private, LLM-powered wiki
          — with summaries, a knowledge graph, and chat over your papers. The local companion to NebulaMind, by Suk Kim.
        </p>
      </a>
    </section>
  );
}
