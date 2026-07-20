"use client";

// Draft board — a portfolio-wide progress dashboard for every paper draft the Lab
// holds, across all three tracks: hand-guided Flagship studies, autonomous Frontier
// drafts, and the live automated Pipeline runs (/api/lab/runs). Each draft is placed
// on a 5-stage pipeline (Computed → Drafted → Compiled → Refereed → Cleared) so you
// can see at a glance how far each got — and that none has cleared human review.
//
// Density modeled on the internal "cockpit" pipeline board, but strictly from data we
// actually hold: the reference shows Novelty / Expected-value / Citation gates that this
// pipeline's API does NOT expose, so those are deliberately absent (not faked). What we
// add over the cockpit: real result-figure thumbnails and data-source chips.
import { useEffect, useState } from "react";
import { PB_CSS } from "./PipelineBoard";
import { FLAGSHIP } from "./FlagshipStudies";
import { FRONTIER } from "./FrontierDrafts";

type Run = {
  id: string;
  summary: string | null;
  method: string | null;
  data_sources: string[];
  figure_url: string | null;
  pdf_url: string | null;
  review_url: string | null;
  review_verdict: string | null;
  review_cycles: number | null;
  created_utc: string | null;
};
type Track = "flagship" | "frontier" | "pipeline";
type Item = {
  title: string; track: Track; stage: number; verdict: string | null; pdf: string | null; note: string;
  id?: string; method?: string | null; sources?: string[]; cycles?: number | null; figure?: string | null; review?: string | null;
};

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
const VORDER = ["ACCEPT", "MINOR", "MAJOR", "REJECT", "no verdict yet"];

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

  if (err) return <div className="pb db"><style>{PB_CSS}</style><style>{DB_CSS}</style><div className="pb-state pb-err">Couldn&rsquo;t load the pipeline — {err}</div></div>;
  if (!runs) return <div className="pb db"><style>{PB_CSS}</style><style>{DB_CSS}</style><div className="pb-state">Loading the draft board…</div></div>;

  const items: Item[] = [];
  for (const f of FLAGSHIP) items.push({ title: f.title, track: "flagship", stage: 4, verdict: f.verdict, pdf: f.pdf, note: f.summary });
  for (const f of FRONTIER) items.push({ title: f.title, track: "frontier", stage: 3, verdict: null, pdf: f.pdf, note: f.sub });
  for (const r of runs.filter((x) => !isDemo(x))) {
    const stage = r.review_verdict ? 4 : r.pdf_url ? 3 : r.review_url ? 2 : 1;
    items.push({
      title: prettyMethod(r.method), track: "pipeline", stage, verdict: r.review_verdict, pdf: r.pdf_url, note: r.summary ?? "—",
      id: r.id, method: r.method, sources: r.data_sources, cycles: r.review_cycles, figure: r.figure_url, review: r.review_url,
    });
  }

  const total = items.length;
  const withPdf = items.filter((i) => i.stage >= 3).length;
  const refereed = items.filter((i) => i.stage >= 4).length;
  const cleared = items.filter((i) => i.stage >= 5).length;
  const perStage = STAGES.map((_, si) => items.filter((i) => i.stage >= si + 1).length);
  const fmax = Math.max(1, ...perStage);

  const verdicts = items.reduce<Record<string, number>>((a, i) => {
    const k = i.verdict ? i.verdict.toUpperCase() : "no verdict yet";
    a[k] = (a[k] ?? 0) + 1; return a;
  }, {});
  const verdictRows = Object.entries(verdicts).sort((a, b) => VORDER.indexOf(a[0]) - VORDER.indexOf(b[0]));
  const vmax = Math.max(1, ...verdictRows.map(([, n]) => n));

  const halt = STAGES.map((label, si) => ({ label, si, n: items.filter((i) => i.stage === si + 1).length })).filter((h) => h.n > 0);
  const hmax = Math.max(1, ...halt.map((h) => h.n));

  const byTrack: Track[] = ["flagship", "frontier", "pipeline"];
  const pipeRows = items.filter((i) => i.track === "pipeline");

  const StageTrack = ({ stage }: { stage: number }) => (
    <div className="db-track" role="img" aria-label={`Reached stage ${stage} of 5: ${STAGES[stage - 1]}`}>
      {STAGES.map((s, si) => {
        const done = si + 1 <= stage, cur = si + 1 === stage, gate = si === 4;
        return <div className={`db-step${done ? " done" : ""}${cur ? " cur" : ""}${gate ? " gate" : ""}`} key={s}><i /><span>{s}</span></div>;
      })}
    </div>
  );

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
            <span className="pb-barwrap"><i className={`pb-bar${si === 4 ? " db-bar-gate" : ""}`} style={{ width: `${(perStage[si] / fmax) * 100}%` }} /><span className="pb-barn">{perStage[si]}</span></span>
          </div>
        ))}
        <p className="pb-attrition">The last stage, <em>Cleared</em>, is a human validating the science — <b>{cleared}</b> so far. Everything upstream is machine-made and honestly provisional.</p>
      </div>

      <div className="pb-mini-grid">
        <div className="pb-mini">
          <div className="pb-mh">Referee verdicts — the only logged gate</div>
          {verdictRows.map(([k, n]) => {
            const c = k === "no verdict yet" ? "#9aa3b8" : vcolor(k);
            return (
              <div className="pb-drow" key={k}>
                <span className="pb-dk" style={{ color: c }}>{k}{k === "MINOR" ? " · small fixes" : ""}</span>
                <span className="pb-barwrap"><i className="pb-bar" style={{ width: `${(n / vmax) * 100}%`, background: c }} /><span className="pb-barn">{n}</span></span>
              </div>
            );
          })}
        </div>
        <div className="pb-mini">
          <div className="pb-mh">Where drafts stop — furthest stage reached</div>
          {halt.map((h) => (
            <div className="pb-drow" key={h.label}>
              <span className="pb-dk">{h.si + 1 >= 5 ? "cleared" : h.si + 1 === 4 ? "refereed · stopped" : `stopped · ${h.label.toLowerCase()}`}</span>
              <span className="pb-barwrap"><i className="pb-bar" style={{ width: `${(h.n / hmax) * 100}%`, background: h.si + 1 >= 4 ? "var(--lab-accent2)" : "var(--lab-soft)" }} /><span className="pb-barn">{h.n}</span></span>
            </div>
          ))}
        </div>
      </div>
      <p className="db-note">Only the <b>referee</b> gate is instrumented in this pipeline&rsquo;s API — the internal cockpit&rsquo;s novelty / expected-value / citation gates aren&rsquo;t exposed here, so they&rsquo;re deliberately absent rather than guessed.</p>

      {byTrack.map((tk) => {
        const rows = items.filter((i) => i.track === tk);
        if (!rows.length) return null;
        return (
          <div key={tk}>
            <p className="pb-sect">{TRACK_META[tk].label} <span className="db-sect-sub">· {TRACK_META[tk].blurb}</span></p>
            <div className="pb-runs">
              {rows.map((it, i) => (
                <div className={`pb-run db-rcard${tk === "flagship" ? " pb-flag" : ""}`} key={`${tk}-${i}`}>
                  <div className="pb-run-top">
                    <span className="pb-run-title">{it.title}</span>
                    <span className="pb-chip" style={{ borderColor: vcolor(it.verdict), color: vcolor(it.verdict) }}>
                      {it.verdict ? `${it.verdict}${it.verdict.toUpperCase() === "MINOR" ? " · not accepted" : ""}` : "no verdict yet"}
                    </span>
                  </div>
                  <div className="pb-run-chips">
                    <span className="db-track-chip">{TRACK_META[tk].label}</span>
                    {it.sources?.map((s) => <span className="pb-src" key={s}>{s.toUpperCase()}</span>)}
                    {it.cycles != null && <span className="pb-src pb-src-cyc">{it.cycles} review cycle{it.cycles === 1 ? "" : "s"}</span>}
                  </div>
                  {it.note && <p className="pb-run-summary">{it.note}</p>}
                  {it.figure && (
                    <>
                      <a href={it.figure} target="_blank" rel="noopener noreferrer" className="db-thumb">
                        <img src={it.figure} loading="lazy" alt={`Draft figure from automated run ${it.title} — not validated`} />
                      </a>
                      <p className="db-figcap">draft figure — not validated</p>
                    </>
                  )}
                  <StageTrack stage={it.stage} />
                  <div className="db-row-foot">
                    <span className="db-links">
                      {it.pdf ? <a href={it.pdf} target="_blank" rel="noopener noreferrer">PDF ↗</a> : <span className="pb-nolink">no PDF</span>}
                      {it.figure && <a href={it.figure} target="_blank" rel="noopener noreferrer">figure ↗</a>}
                      {it.review && <a href={it.review} target="_blank" rel="noopener noreferrer">referee ↗</a>}
                    </span>
                    <span className="db-tag">descriptive — not validated</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        );
      })}

      <p className="pb-sect">All pipeline runs</p>
      <div className="db-table-wrap">
        <table className="db-table">
          <thead>
            <tr><th scope="col">run</th><th scope="col">topic</th><th scope="col">sources</th><th scope="col">cycles</th><th scope="col">referee</th><th scope="col">stage / outcome</th></tr>
          </thead>
          <tbody>
            {pipeRows.map((it) => (
              <tr key={it.id}>
                <td className="db-mono">{it.id?.slice(0, 12)}</td>
                <td>{prettyMethod(it.method ?? null)}</td>
                <td className="db-mono">{it.sources?.length ? it.sources.map((s) => s.toUpperCase()).join(" · ") : "—"}</td>
                <td className="db-mono">{it.cycles ?? "—"}</td>
                <td>{it.verdict ? <span className="pb-chip" style={{ borderColor: vcolor(it.verdict), color: vcolor(it.verdict) }}>{it.verdict}</span> : <span className="pb-nolink">—</span>}</td>
                <td className="db-mono">{it.stage >= 4 ? "refereed" : it.stage >= 3 ? "compiled · PDF" : it.stage >= 2 ? "drafted" : "stopped · study"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

const DB_CSS = `
.pb-mh{font-family:ui-monospace,monospace;font-size:.64rem;text-transform:uppercase;letter-spacing:.08em;color:var(--lab-accent2);margin-bottom:.5rem}
.pb-mini-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:.7rem;margin-top:.2rem}
.db-note{font-size:.72rem;color:var(--lab-soft);line-height:1.5;margin:.6rem 0 .2rem;font-style:italic}
.db-note b{color:var(--lab-accent2);font-style:normal}
.db-sect-sub{color:var(--lab-soft);font-weight:400;text-transform:none;letter-spacing:0}
.db-bar-gate{background:repeating-linear-gradient(45deg,#3a4260,#3a4260 4px,#2a3145 4px,#2a3145 8px)!important}
.db .pb-runs{grid-template-columns:repeat(auto-fit,minmax(340px,1fr))}
.db-rcard{display:flex;flex-direction:column}
.db-track-chip{font-family:ui-monospace,monospace;font-size:.6rem;letter-spacing:.05em;text-transform:uppercase;color:var(--lab-soft);border:1px solid var(--lab-line);border-radius:999px;padding:.06rem .5rem;white-space:nowrap}
.db-thumb{display:block;margin:.1rem 0 .25rem;border:1px solid var(--lab-line);border-radius:8px;overflow:hidden;max-width:200px}
.db-thumb img{display:block;width:100%;height:auto;max-height:120px;object-fit:cover;background:#0a0d17}
.db-figcap{font-family:ui-monospace,monospace;font-size:.58rem;letter-spacing:.04em;text-transform:uppercase;color:#e0a458;margin:0 0 .5rem}
.db-track{display:flex;align-items:flex-start;gap:0;margin:.35rem 0 .7rem}
.db-step{flex:1;display:flex;flex-direction:column;align-items:center;gap:.3rem;position:relative}
.db-step i{width:12px;height:12px;border-radius:50%;background:var(--lab-panel);border:2px solid var(--lab-line);z-index:1}
.db-step::before{content:"";position:absolute;top:5px;left:-50%;width:100%;height:2px;background:var(--lab-line)}
.db-step:first-child::before{display:none}
.db-step span{font-size:.58rem;font-family:ui-monospace,monospace;color:var(--lab-soft);letter-spacing:.02em}
.db-step.done i{background:var(--lab-accent);border-color:var(--lab-accent)}
.db-step.done::before{background:var(--lab-accent)}
.db-step.done span{color:var(--lab-ink)}
.db-step.cur i{background:var(--lab-accent2);border-color:var(--lab-accent2);box-shadow:0 0 0 4px rgba(74,214,196,.18)}
.db-step.cur span{color:var(--lab-accent2);font-weight:600}
.db-step.gate i{background:transparent;border-style:dashed;border-color:var(--lab-soft)}
.db-step.gate.done i{background:var(--lab-accent);border-style:solid}
.db-row-foot{display:flex;align-items:center;justify-content:space-between;gap:.8rem;font-size:.76rem;font-family:ui-monospace,monospace;margin-top:auto;padding-top:.4rem}
.db-links{display:flex;gap:.9rem}
.db-links a{color:var(--lab-accent);text-decoration:none}
.db-links a:hover{text-decoration:underline}
.db-tag{font-size:.58rem;letter-spacing:.05em;text-transform:uppercase;color:#e0a458;white-space:nowrap}
.db-table-wrap{overflow-x:auto;border:1px solid var(--lab-line);border-radius:12px;background:var(--lab-panel)}
.db-table{width:100%;border-collapse:collapse;font-size:.8rem;min-width:560px}
.db-table th{text-align:left;font-weight:500;font-size:.62rem;text-transform:uppercase;letter-spacing:.06em;color:var(--lab-soft);border-bottom:1px solid var(--lab-line);padding:.5rem .6rem;white-space:nowrap}
.db-table td{padding:.5rem .6rem;border-bottom:1px solid var(--lab-line);color:var(--lab-ink);vertical-align:middle}
.db-table tbody tr:last-child td{border-bottom:none}
.db-mono{font-family:ui-monospace,monospace;font-size:.72rem;color:var(--lab-soft)}
@media(max-width:520px){.db-step span{font-size:.5rem}.db-links{gap:.6rem}}
`;
