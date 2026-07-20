"use client";

// Draft board — a portfolio-wide progress dashboard for every paper draft the Lab
// holds, across all three tracks: hand-guided Flagship studies, autonomous Frontier
// drafts, and the live automated Pipeline runs (/api/lab/runs). Each draft is placed
// on a 5-stage pipeline (Computed → Drafted → Compiled → Refereed → Cleared) so you
// can see at a glance how far each one got — and that none has cleared human review.
import { useEffect, useState } from "react";
import { PB_CSS } from "./PipelineBoard";
import { FLAGSHIP } from "./FlagshipStudies";
import { FRONTIER } from "./FrontierDrafts";

type Run = {
  id: string;
  summary: string | null;
  method: string | null;
  pdf_url: string | null;
  review_url: string | null;
  review_verdict: string | null;
  created_utc: string | null;
};
type Track = "flagship" | "frontier" | "pipeline";
type Item = { title: string; track: Track; stage: number; verdict: string | null; pdf: string | null; note: string };

// The pipeline a result walks: 1 Computed → 2 Drafted → 3 Compiled(PDF) → 4 Refereed → 5 Cleared(human).
const STAGES = ["Computed", "Drafted", "Compiled", "Refereed", "Cleared"];
const TRACK_META: Record<Track, { label: string; blurb: string }> = {
  flagship: { label: "Flagship", blurb: "hand-guided by the crew — the full forward-model + referee loop" },
  frontier: { label: "Frontier drafts", blurb: "autonomous multi-page manuscripts, one per top frontier" },
  pipeline: { label: "Pipeline runs", blurb: "the fully-automated, high-attrition track (live)" },
};
const VC: Record<string, string> = { ACCEPT: "#4ad6c4", MINOR: "#e0a458", MAJOR: "#e0774f", REJECT: "#f47272" };
const vcolor = (v: string | null) => (v ? VC[v.toUpperCase()] ?? "#9aa3b8" : "#9aa3b8");
const isDemo = (r: Run) => !r.created_utc || /demo/i.test(r.id);
const prettyMethod = (m: string | null) =>
  (m ?? "study").split("-").map((w) => (w ? w[0].toUpperCase() + w.slice(1) : w)).join(" ");

export default function DraftBoard() {
  const [runs, setRuns] = useState<Run[] | null>(null);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    let alive = true;
    fetch("/api/lab/runs")
      .then((r) => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.json(); })
      .then((d) => { if (alive) setRuns(d.runs ?? []); })
      .catch((e) => { if (alive) setErr(String(e?.message ?? e)); });
    return () => { alive = false; };
  }, []);

  if (err) return <div className="pb"><style>{PB_CSS}</style><div className="pb-state pb-err">Couldn&rsquo;t load the pipeline — {err}</div></div>;
  if (!runs) return <div className="pb"><style>{PB_CSS}</style><div className="pb-state">Loading the draft board…</div></div>;

  const items: Item[] = [];
  // Flagship — hand-guided, went the full distance (a compiled PDF with a logged referee verdict).
  for (const f of FLAGSHIP) items.push({ title: f.title, track: "flagship", stage: 4, verdict: f.verdict, pdf: f.pdf, note: f.summary });
  // Frontier — compiled multi-page drafts, but no referee verdict logged here.
  for (const f of FRONTIER) items.push({ title: f.title, track: "frontier", stage: 3, verdict: null, pdf: f.pdf, note: f.sub });
  // Pipeline — live automated runs; stage from how far each got.
  for (const r of runs.filter((x) => !isDemo(x))) {
    const stage = r.review_verdict ? 4 : r.pdf_url ? 3 : r.review_url ? 2 : 1;
    items.push({ title: prettyMethod(r.method), track: "pipeline", stage, verdict: r.review_verdict, pdf: r.pdf_url, note: r.summary ?? "—" });
  }

  const total = items.length;
  const withPdf = items.filter((i) => i.pdf || i.stage >= 3).length;
  const refereed = items.filter((i) => i.stage >= 4).length;
  const cleared = items.filter((i) => i.stage >= 5).length;
  // funnel: how many drafts reached at least each stage
  const perStage = STAGES.map((_, si) => items.filter((i) => i.stage >= si + 1).length);
  const fmax = Math.max(1, ...perStage);
  const byTrack: Track[] = ["flagship", "frontier", "pipeline"];

  return (
    <div className="pb db">
      <style>{PB_CSS}</style>
      <style>{DB_CSS}</style>

      <div className="pb-kpis">
        <div className="pb-kpi"><b>{total}</b><span>drafts tracked</span></div>
        <div className="pb-kpi"><b>{withPdf}</b><span>compiled to PDF</span></div>
        <div className="pb-kpi"><b>{refereed}</b><span>refereed</span></div>
        <div className="pb-kpi pb-kpi-zero"><b>{cleared}</b><span>cleared / validated</span></div>
      </div>
      <p className="pb-lede">
        Where <b>every draft</b> stands, across all three tracks. Each walks the same pipeline —
        <b> computed → drafted → compiled → refereed → cleared</b> — and every one is <b>descriptive, not validated</b>:
        the final gate is a human sign-off, and <b>none has passed it</b>.
      </p>

      <p className="pb-sect">Pipeline funnel — drafts reaching each stage</p>
      <div className="pb-card">
        {STAGES.map((s, si) => (
          <div className="pb-frow" key={s}>
            <span className="pb-fl">{s}</span>
            <span className="pb-barwrap">
              <i className={`pb-bar${si === 4 ? " db-bar-gate" : ""}`} style={{ width: `${(perStage[si] / fmax) * 100}%` }} />
              <span className="pb-barn">{perStage[si]}</span>
            </span>
          </div>
        ))}
        <p className="pb-attrition">The last stage, <em>Cleared</em>, is a human validating the science — <b>{cleared}</b> so far. Everything upstream is machine-made and honestly provisional.</p>
      </div>

      {byTrack.map((tk) => {
        const rows = items.filter((i) => i.track === tk);
        if (!rows.length) return null;
        return (
          <div key={tk}>
            <p className="pb-sect">{TRACK_META[tk].label} <span className="db-sect-sub">· {TRACK_META[tk].blurb}</span></p>
            <div className="db-rows">
              {rows.map((it, i) => (
                <div className={`db-row${tk === "flagship" ? " db-flag" : ""}`} key={`${tk}-${i}`}>
                  <div className="db-row-top">
                    <span className="db-row-title">{it.title}</span>
                    <span className="db-chip" style={{ borderColor: vcolor(it.verdict), color: vcolor(it.verdict) }}>
                      {it.verdict ? `${it.verdict}${it.verdict.toUpperCase() === "MINOR" ? " · not accepted" : ""}` : "no verdict yet"}
                    </span>
                  </div>
                  {it.note && <p className="db-row-note">{it.note}</p>}
                  <div className="db-track" role="img" aria-label={`Reached stage ${it.stage} of 5: ${STAGES[it.stage - 1]}`}>
                    {STAGES.map((s, si) => {
                      const done = si + 1 <= it.stage;
                      const cur = si + 1 === it.stage;
                      const gate = si === 4;
                      return (
                        <div className={`db-step${done ? " done" : ""}${cur ? " cur" : ""}${gate ? " gate" : ""}`} key={s}>
                          <i />
                          <span>{s}</span>
                        </div>
                      );
                    })}
                  </div>
                  <div className="db-row-foot">
                    {it.pdf ? <a href={it.pdf} target="_blank" rel="noopener noreferrer">draft PDF ↗</a> : <span className="pb-nolink">no PDF yet</span>}
                    <span className="db-tag">descriptive — not validated</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}

const DB_CSS = `
.db-sect-sub{color:var(--lab-soft);font-weight:400;text-transform:none;letter-spacing:0}
.db-bar-gate{background:repeating-linear-gradient(45deg,#3a4260,#3a4260 4px,#2a3145 4px,#2a3145 8px)}
.db-rows{display:flex;flex-direction:column;gap:.6rem}
.db-row{border:1px solid var(--lab-line);border-radius:11px;background:var(--lab-panel);padding:.85rem .95rem}
.db-row.db-flag{border-color:rgba(124,134,255,.5);background:linear-gradient(90deg,rgba(124,134,255,.08),rgba(74,214,196,.04))}
.db-row-top{display:flex;justify-content:space-between;align-items:baseline;gap:.6rem}
.db-row-title{font-weight:650;font-size:.94rem;color:var(--lab-ink);line-height:1.3}
.db-chip{display:inline-block;border:1px solid;border-radius:999px;padding:.06rem .55rem;font-size:.62rem;font-family:ui-monospace,monospace;white-space:nowrap;flex-shrink:0}
.db-row-note{font-size:.78rem;color:var(--lab-soft);line-height:1.5;margin:.35rem 0 .7rem}
.db-track{display:flex;align-items:flex-start;gap:0;margin:.2rem 0 .7rem}
.db-step{flex:1;display:flex;flex-direction:column;align-items:center;gap:.3rem;position:relative}
.db-step i{width:13px;height:13px;border-radius:50%;background:#1a1f30;border:2px solid #2a3145;z-index:1}
.db-step::before{content:"";position:absolute;top:6px;left:-50%;width:100%;height:2px;background:#2a3145}
.db-step:first-child::before{display:none}
.db-step span{font-size:.6rem;font-family:ui-monospace,monospace;color:var(--lab-soft);letter-spacing:.02em}
.db-step.done i{background:var(--lab-accent);border-color:var(--lab-accent)}
.db-step.done::before{background:var(--lab-accent)}
.db-step.done span{color:var(--lab-ink)}
.db-step.cur i{background:var(--lab-accent2);border-color:var(--lab-accent2);box-shadow:0 0 0 4px rgba(74,214,196,.18)}
.db-step.cur span{color:var(--lab-accent2);font-weight:600}
.db-step.gate i{background:transparent;border-style:dashed;border-color:#4b5473}
.db-step.gate.done i{background:var(--lab-accent);border-style:solid}
.db-row-foot{display:flex;align-items:center;justify-content:space-between;gap:.8rem;font-size:.78rem;font-family:ui-monospace,monospace}
.db-row-foot a{color:var(--lab-accent);text-decoration:none}
.db-row-foot a:hover{text-decoration:underline}
.db-tag{font-size:.6rem;letter-spacing:.05em;text-transform:uppercase;color:#e0a458}
@media(max-width:520px){.db-step span{font-size:.52rem}}
`;
