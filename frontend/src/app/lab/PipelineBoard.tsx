"use client";

// Live pipeline board for the Lab "Paper" step — the papers/PDFs in progress.
// Reads /api/lab/runs (the real AI-Scientist runs) and shows honest attrition:
// most runs stop at the study stage, the best any reach is a MINOR referee verdict,
// and ZERO are validated or published. Every PDF here is a descriptive draft.
import { useEffect, useState } from "react";

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

// Referee-verdict colors. MINOR is amber (it means "small fixes", NOT accepted);
// only ACCEPT is teal. None accepted so far.
const VC: Record<string, string> = {
  ACCEPT: "#4ad6c4", MINOR: "#e0a458", MAJOR: "#e0774f", REJECT: "#f47272",
};
const SOFT = "#9aa3b8";
const vcolor = (v: string | null) => (v ? VC[v.toUpperCase()] ?? SOFT : SOFT);
const isDemo = (r: Run) => !r.created_utc || /demo/i.test(r.id);
const prettyMethod = (m: string | null) =>
  (m ?? "study").split("-").map((w) => (w ? w[0].toUpperCase() + w.slice(1) : w)).join(" ");

export default function PipelineBoard() {
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

  if (err) return <div className="pb-state pb-err">Couldn&rsquo;t load the pipeline — {err}</div>;
  if (!runs) return <div className="pb-state">Loading the pipeline…</div>;

  const total = runs.length;
  const nStudy = runs.filter((r) => r.summary).length;
  const nDraft = runs.filter((r) => r.review_url).length;
  const nPdf = runs.filter((r) => r.pdf_url).length;
  const nRefereed = runs.filter((r) => r.review_verdict).length;
  const nDemo = runs.filter(isDemo).length;
  const nAccept = runs.filter((r) => (r.review_verdict ?? "").toUpperCase() === "ACCEPT").length;
  const funnel: [string, number][] = [["Study", nStudy], ["Draft", nDraft], ["PDF", nPdf], ["Refereed", nRefereed]];
  const verdicts = runs.reduce<Record<string, number>>((a, r) => {
    const k = r.review_verdict ? r.review_verdict.toUpperCase() : "no verdict yet";
    a[k] = (a[k] ?? 0) + 1; return a;
  }, {});
  const verdictRows = Object.entries(verdicts).sort((a, b) => b[1] - a[1]);
  const vmax = Math.max(1, ...verdictRows.map(([, n]) => n));
  // real runs first, demos last
  const ordered = [...runs].sort((a, b) => (isDemo(a) ? 1 : 0) - (isDemo(b) ? 1 : 0));

  return (
    <div className="pb">
      <style>{PB_CSS}</style>

      <div className="pb-kpis">
        <div className="pb-kpi"><b>{total}</b><span>runs in flight</span></div>
        <div className="pb-kpi"><b>{nPdf}</b><span>compiled a draft PDF{nDemo ? ` · ${nDemo} demo` : ""}</span></div>
        <div className="pb-kpi pb-kpi-zero"><b>{nAccept}</b><span>accepted / validated</span></div>
      </div>
      <p className="pb-lede">
        This is the filter, not a trophy case. Every run below is an <b>automated descriptive draft</b>: most
        stop at the study stage, the best any reach is a referee <b>MINOR</b> (small fixes — <b>not</b> accepted),
        and <b>none is validated or published</b>. The PDFs are drafts a human still has to vouch for.
      </p>

      <p className="pb-sect">Funnel — how many runs reach each stage</p>
      <div className="pb-card">
        {funnel.map(([label, n]) => (
          <div className="pb-frow" key={label}>
            <span className="pb-fl">{label}</span>
            <span className="pb-barwrap"><i className="pb-bar" style={{ width: `${(n / total) * 100}%` }} /><span className="pb-barn">{n}</span></span>
          </div>
        ))}
        <p className="pb-attrition">Narrowing is the point: {nStudy} computed a study, {nPdf} compiled a PDF, {nRefereed} carry a logged referee verdict. Runs that stop are <em>stopped</em>, not failed.</p>
      </div>

      <p className="pb-sect">Referee verdicts</p>
      <div className="pb-mini">
        {verdictRows.map(([k, n]) => {
          const c = k === "no verdict yet" ? SOFT : vcolor(k);
          return (
            <div className="pb-drow" key={k}>
              <span className="pb-dk" style={{ color: c }}>{k}{k === "MINOR" ? " · small fixes" : ""}</span>
              <span className="pb-barwrap"><i className="pb-bar" style={{ width: `${(n / vmax) * 100}%`, background: c }} /><span className="pb-barn">{n}</span></span>
            </div>
          );
        })}
      </div>

      <p className="pb-sect">Papers in progress — the drafts themselves</p>
      <div className="pb-runs">
        {ordered.map((r) => {
          const v = r.review_verdict;
          const c = vcolor(v);
          const demo = isDemo(r);
          return (
            <div className={`pb-run${demo ? " pb-demo" : ""}`} key={r.id}>
              <div className="pb-run-top">
                <span className="pb-run-title">{prettyMethod(r.method)}</span>
                <span className="pb-chip" style={{ borderColor: c, color: c }}>{v ? `${v}${v.toUpperCase() === "MINOR" ? " · not accepted" : ""}` : "no verdict yet"}</span>
              </div>
              <p className="pb-run-summary">{r.summary ?? "—"}</p>
              <div className="pb-run-chips">
                {demo && <span className="pb-src pb-src-demo">demo fixture</span>}
                {r.data_sources.map((s) => <span className="pb-src" key={s}>{s.toUpperCase()}</span>)}
                {r.review_cycles != null && <span className="pb-src pb-src-cyc">{r.review_cycles} review cycle{r.review_cycles === 1 ? "" : "s"}</span>}
              </div>
              {demo ? (
                <div className="pb-run-links pb-nolink">demo fixture — no live artifact</div>
              ) : (
                <div className="pb-run-links">
                  {r.pdf_url && <a href={r.pdf_url} target="_blank" rel="noopener noreferrer">draft PDF ↗</a>}
                  {r.figure_url && <a href={r.figure_url} target="_blank" rel="noopener noreferrer">figure ↗</a>}
                  {r.review_url && <a href={r.review_url} target="_blank" rel="noopener noreferrer">referee ↗</a>}
                  {!r.pdf_url && !r.figure_url && !r.review_url && <span className="pb-nolink">stopped early — no artifact yet</span>}
                </div>
              )}
              <p className="pb-tag">descriptive draft — not validated, not published</p>
            </div>
          );
        })}
      </div>
    </div>
  );
}

const PB_CSS = `
.pb{color:var(--lab-ink);margin-top:.4rem}
.pb-state{padding:1.1rem;border:1px solid var(--lab-line);border-radius:12px;background:var(--lab-panel);color:var(--lab-soft);font-size:.86rem}
.pb-err{color:#f47272}
.pb-sect{font-family:ui-monospace,monospace;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--lab-accent2);margin:1.4rem 0 .6rem}
.pb-kpis{display:flex;gap:1.8rem;flex-wrap:wrap;margin:.2rem 0 .5rem}
.pb-kpi b{font-size:1.7rem;font-weight:700;display:block;line-height:1;color:var(--lab-ink)}
.pb-kpi span{font-size:.74rem;color:var(--lab-soft)}
.pb-kpi-zero b{color:#f47272}
.pb-lede{font-size:.84rem;color:var(--lab-ink);line-height:1.6;margin:.1rem 0 .2rem}
.pb-lede b{color:var(--lab-accent2);font-weight:600}
.pb-card{border:1px solid var(--lab-line);border-radius:12px;background:var(--lab-panel);padding:.9rem 1rem}
.pb-barwrap{display:flex;align-items:center;gap:.5rem;flex:1}
.pb-bar{height:14px;border-radius:4px;min-width:3px;background:linear-gradient(90deg,var(--lab-accent),var(--lab-accent2))}
.pb-barn{font-family:ui-monospace,monospace;font-size:.74rem;color:var(--lab-soft)}
.pb-frow{display:flex;align-items:center;gap:.8rem;margin:.3rem 0}
.pb-fl{width:82px;font-size:.83rem;color:var(--lab-ink)}
.pb-attrition{font-size:.74rem;color:var(--lab-soft);line-height:1.5;margin:.65rem 0 0;border-top:1px solid var(--lab-line);padding-top:.55rem}
.pb-attrition em{color:var(--lab-accent2);font-style:normal}
.pb-mini{border:1px solid var(--lab-line);border-radius:10px;background:#0a0d17;padding:.7rem .85rem}
.pb-drow{display:flex;align-items:center;gap:.7rem;margin:.28rem 0}
.pb-dk{width:150px;font-family:ui-monospace,monospace;font-size:.74rem}
.pb-runs{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:.7rem}
.pb-run{border:1px solid var(--lab-line);border-radius:11px;background:var(--lab-panel);padding:.8rem .9rem}
.pb-run.pb-demo{opacity:.72}
.pb-run-top{display:flex;justify-content:space-between;align-items:baseline;gap:.5rem}
.pb-run-title{font-weight:650;font-size:.92rem;color:var(--lab-ink)}
.pb-run-summary{font-size:.79rem;color:var(--lab-soft);line-height:1.5;margin:.4rem 0 .5rem}
.pb-run-chips{display:flex;flex-wrap:wrap;gap:.3rem;margin-bottom:.5rem}
.pb-src{font-family:ui-monospace,monospace;font-size:.62rem;letter-spacing:.04em;color:var(--lab-accent2);border:1px solid var(--lab-line);border-radius:999px;padding:.08rem .5rem}
.pb-src-cyc{color:var(--lab-soft)}
.pb-src-demo{color:var(--lab-soft);border-color:var(--lab-soft)}
.pb-chip{display:inline-block;border:1px solid;border-radius:999px;padding:.06rem .55rem;font-size:.63rem;font-family:ui-monospace,monospace;white-space:nowrap}
.pb-run-links{display:flex;gap:.9rem;font-size:.78rem;font-family:ui-monospace,monospace}
.pb-run-links a{color:var(--lab-accent);text-decoration:none}
.pb-run-links a:hover{text-decoration:underline}
.pb-nolink{color:var(--lab-soft);font-style:italic}
.pb-tag{font-family:ui-monospace,monospace;font-size:.6rem;letter-spacing:.05em;text-transform:uppercase;color:#e0a458;margin:.55rem 0 0}
@media(max-width:560px){.pb-kpis{gap:1.1rem}.pb-dk{width:120px}}
`;
