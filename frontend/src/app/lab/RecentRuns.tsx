"use client";

import { useEffect, useState } from "react";

type Run = {
  id: string;
  summary?: string;
  method?: string;
  data_sources?: string[];
  figure_url?: string;
  pdf_url?: string;
  review_url?: string;
  review_verdict?: string;
  review_cycles?: number;
};

const VERDICT_COLOR: Record<string, string> = {
  ACCEPT: "#4ad6c4",
  MINOR: "#7c86ff",
  MAJOR: "#e0a458",
  REJECT: "#f47272",
};

function title(r: Run): string {
  const s = (r.summary || "").split(" — ")[0].split(" -- ")[0].trim();
  return s || r.method || "Study";
}

export default function RecentRuns() {
  const [runs, setRuns] = useState<Run[] | null>(null);

  useEffect(() => {
    let live = true;
    fetch("/api/lab/runs?limit=40")
      .then((r) => (r.ok ? r.json() : { runs: [] }))
      .then((d) => {
        if (!live) return;
        // dedup by summary (identical query => identical study), keep newest (list is newest-first)
        const seen = new Set<string>();
        const uniq: Run[] = [];
        for (const r of (d.runs || []) as Run[]) {
          const k = r.summary || r.id;
          if (seen.has(k)) continue;
          seen.add(k);
          uniq.push(r);
        }
        setRuns(uniq.slice(0, 12));
      })
      .catch(() => live && setRuns([]));
    return () => {
      live = false;
    };
  }, []);

  if (runs === null) {
    return <p className="lab-note" style={{ opacity: 0.6 }}>Loading runs…</p>;
  }
  if (runs.length === 0) {
    return <p className="lab-note" style={{ opacity: 0.7 }}>No configurator runs yet — compose one above.</p>;
  }

  return (
    <div className="lab-studies">
      {runs.map((r) => (
        <div className="lab-card" key={r.id} style={{ cursor: "default" }}>
          <div className="row">
            <h3>{title(r)}</h3>
            <span className="tag">
              {r.review_verdict ? (
                <b style={{ color: VERDICT_COLOR[r.review_verdict] || "var(--lab-accent2)" }}>
                  {r.review_verdict}
                  {r.review_cycles ? ` · ${r.review_cycles}c` : ""}
                </b>
              ) : (
                "configurator run"
              )}
            </span>
          </div>
          {r.summary && <p>{r.summary}</p>}
          <p style={{ margin: ".55rem 0 0", display: "flex", gap: "1rem", flexWrap: "wrap", fontFamily: "ui-monospace,monospace", fontSize: ".78rem" }}>
            {r.figure_url && (
              <a href={r.figure_url} target="_blank" rel="noopener noreferrer" style={{ color: "var(--lab-accent2)" }}>figure ↗</a>
            )}
            {r.pdf_url && (
              <a href={r.pdf_url} target="_blank" rel="noopener noreferrer" style={{ color: "var(--lab-accent)" }}>AASTeX PDF ↓</a>
            )}
            {r.review_url && (
              <a href={r.review_url} target="_blank" rel="noopener noreferrer" style={{ color: "var(--lab-soft)" }}>review–revise log ↗</a>
            )}
          </p>
        </div>
      ))}
    </div>
  );
}
