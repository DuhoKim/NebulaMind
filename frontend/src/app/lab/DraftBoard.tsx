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
import { useEffect, useState, useRef, useCallback } from "react";
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
  updated?: string | null;
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

// ── Revision log (per-draft referee-loop history) ─────────────────────────────
// Parses a run's review_loop.md artifact into a structured, honest revision log.
// Reality (Trio referee): the ONLY feedback source recorded is one automated referee
// model; human feedback and gate history are NOT captured, and almost no run has
// iterated past a single pass — so this is a *revision log*, not iterative peer review.
//
// Provenance schema the backend would eventually populate (only `referee-model` is
// filled today; `human` / gates / lineage are reserved, rendered as explicit absences):
//   DraftRevision = { cycle, feedbackSource: "referee-model"|"novelty-gate"|
//     "citation-gate"|"expected-value-gate"|"human", feedbackBy, feedbackKind:{verdict,
//     categories[]}, feedbackText, draftBefore?, draftAfter?, changed:{summary,diffStat?},
//     timestamp } ; DraftHistory = { runId, model, converged, revisions[], lineage? }
type ReviewCycle = { n: number; verdict: string; feedback: string; draft: string };
type ReviewLoop = { model: string; convergedVerdict: string | null; cycles: ReviewCycle[]; final: string };

const stripDetails = (s: string) =>
  s.replace(/<details>\s*<summary>[^<]*<\/summary>/i, "").replace(/<\/details>/i, "").trim();
const stripVerdictLine = (s: string) => s.replace(/^\s*VERDICT:\s*[A-Z]+\s*\n/i, "").trim();

function parseReviewLoop(md: string): ReviewLoop {
  const text = md.replace(/\r\n/g, "\n");
  const model = text.match(/^Model:\s*(.+?)\.\s/m)?.[1]?.trim() ?? "automated referee";
  const convergedVerdict = text.match(/Converged to \*\*([A-Z]+)\*\*/)?.[1] ?? null;
  const finalSplit = text.split(/\n##\s*Final manuscript body\s*\n/);
  const body = finalSplit[0];
  const final = (finalSplit[1] ?? "").trim();
  const cycleRe = /##\s*Cycle\s*(\d+)\s*[—–-]\s*VERDICT:\s*([A-Z]+)\s*\n([\s\S]*?)(?=\n##\s|$)/g;
  const cycles: ReviewCycle[] = [];
  for (const m of body.matchAll(cycleRe)) {
    const rawBlock = m[3];
    const detIdx = rawBlock.search(/<details>/i);
    const feedbackRaw = detIdx >= 0 ? rawBlock.slice(0, detIdx) : rawBlock;
    const draftRaw = detIdx >= 0 ? rawBlock.slice(detIdx) : "";
    cycles.push({ n: Number(m[1]), verdict: m[2], feedback: stripVerdictLine(feedbackRaw), draft: draftRaw ? stripDetails(draftRaw) : "" });
  }
  return { model, convergedVerdict, cycles, final };
}

const dhWords = (s: string) => s.toLowerCase().match(/[a-z0-9']+/g) ?? [];
function draftDelta(prev: string, next: string) {
  const a = new Map<string, number>();
  const b = new Map<string, number>();
  for (const w of dhWords(prev)) a.set(w, (a.get(w) ?? 0) + 1);
  for (const w of dhWords(next)) b.set(w, (b.get(w) ?? 0) + 1);
  let added = 0;
  let removed = 0;
  b.forEach((c, w) => { added += Math.max(0, c - (a.get(w) ?? 0)); });
  a.forEach((c, w) => { removed += Math.max(0, c - (b.get(w) ?? 0)); });
  return { added, removed, unchanged: added === 0 && removed === 0 };
}

function StageTrack({ stage }: { stage: number }) {
  return (
    <div className="db-track" role="img" aria-label={`Reached stage ${stage} of 5: ${STAGES[stage - 1]}`}>
      {STAGES.map((s, si) => {
        const done = si + 1 <= stage;
        const cur = si + 1 === stage;
        const gate = si === 4;
        return <div className={`db-step${done ? " done" : ""}${cur ? " cur" : ""}${gate ? " gate" : ""}`} key={s}><i /><span>{s}</span></div>;
      })}
    </div>
  );
}

// Normalized revision-log shape rendered by <RevisionLog>. Sourced from the
// structured history.json (preferred — carries lineage + feedback categories +
// human/gate slots) or, as a fallback, parsed from review_loop.md.
type NormRev = { cycle: number | null; source: string; by: string; verdict: string | null; categories: string[]; feedback: string; changed: string | null };
type NormHist = { model: string; topicSource: string | null; topic: string | null; revisions: NormRev[]; refereeCycles: number; humanCaptured: boolean; final?: string };

function normalizeHistory(j: any): NormHist {
  const revisions: NormRev[] = (j?.revisions ?? []).map((r: any) => ({
    cycle: r.cycle ?? null,
    source: r.feedbackSource ?? "referee-model",
    by: r.feedbackBy ?? "unknown",
    verdict: r.feedbackKind?.verdict ?? null,
    categories: r.feedbackKind?.categories ?? [],
    feedback: r.feedbackText ?? "",
    changed: r.changed?.summary ?? null,
  }));
  return {
    model: j?.model ?? "automated referee",
    topicSource: j?.lineage?.topicSource ?? null,
    topic: j?.lineage?.topic ?? null,
    revisions,
    refereeCycles: revisions.filter((r) => r.source === "referee-model").length,
    humanCaptured: !!j?.humanFeedback?.captured,
  };
}
function normalizeLoop(md: string): NormHist {
  const p = parseReviewLoop(md);
  const revisions: NormRev[] = p.cycles.map((c, i) => {
    let changed: string | null = null;
    if (i > 0) { const d = draftDelta(p.cycles[i - 1].draft, c.draft); changed = d.unchanged ? "draft unchanged" : `+${d.added} / −${d.removed} words vs previous`; }
    return { cycle: c.n, source: "referee-model", by: p.model, verdict: c.verdict, categories: [], feedback: c.feedback, changed };
  });
  return { model: p.model, topicSource: null, topic: null, revisions, refereeCycles: revisions.length, humanCaptured: false, final: p.final };
}

const SOURCE_LABEL: Record<string, string> = { "referee-model": "automated referee", human: "human", "novelty-gate": "novelty gate", "citation-gate": "citation gate", "expected-value-gate": "expected-value gate" };

type HistState = { loading: boolean; data: NormHist | null; err: string | null };
function useRevisionLog(reviewUrl: string | null) {
  const [open, setOpen] = useState(false);
  const [st, setSt] = useState<HistState>({ loading: false, data: null, err: null });
  const fetched = useRef(false);
  const toggle = useCallback(() => {
    setOpen((o) => {
      const next = !o;
      if (next && !fetched.current && reviewUrl) {
        fetched.current = true;
        setSt({ loading: true, data: null, err: null });
        const historyUrl = reviewUrl.replace("review_loop.md", "history.json");
        (async () => {
          try {
            const hr = await fetch(historyUrl);
            if (hr.ok) { setSt({ loading: false, data: normalizeHistory(await hr.json()), err: null }); return; }
            const rr = await fetch(reviewUrl);
            if (rr.status === 404) throw new Error("none");
            if (!rr.ok) throw new Error(`http ${rr.status}`);
            setSt({ loading: false, data: normalizeLoop(await rr.text()), err: null });
          } catch (e: any) {
            setSt({ loading: false, data: null, err: e?.message || "error" });
          }
        })();
      }
      return next;
    });
  }, [reviewUrl]);
  return { open, toggle, ...st };
}

function RevisionLog({ h }: { h: ReturnType<typeof useRevisionLog> }) {
  if (h.loading) return <div className="dh-wrap"><div className="dh-note">Loading revision log…</div></div>;
  if (h.err === "none") return <div className="dh-wrap"><div className="dh-note">No review recorded — this run stopped before referee review. No revisions exist.</div></div>;
  if (h.err) return <div className="dh-wrap"><div className="dh-note">Couldn&rsquo;t load the referee log ({h.err}).</div></div>;
  if (!h.data) return null;
  const { model, revisions, refereeCycles, humanCaptured, topic, topicSource, final } = h.data;
  return (
    <div className="dh-wrap">
      {topic && <p className="dh-lineage">Seeded from the <b>{topicSource || "frontier"}</b> · topic: {topic}</p>}
      <p className="dh-banner">Automated referee (<b>{model}</b>) — unedited machine-generated feedback. Not a human or journal referee; the paper is <b>not validated</b>.</p>
      <p className="dh-state">
        {refereeCycles === 0 ? "The referee ran but logged no cycle."
          : refereeCycles === 1 ? "One automated review pass — the draft was not revised after it. A single machine read, not an iterative review."
          : `${refereeCycles} automated review passes by ${model}. The changes below are the model’s own revisions — no human reviewed any cycle.`}
      </p>
      <ol className="dh-timeline">
        {revisions.map((r, i) => (
          <li className="dh-node" key={i}>
            <span className="dh-dot" style={{ background: vcolor(r.verdict) }} />
            <div className="dh-body">
              <div className="dh-head">
                {r.verdict && <span className="pb-chip" style={{ borderColor: vcolor(r.verdict), color: vcolor(r.verdict) }}>{r.verdict}</span>}
                {r.cycle != null && <span className="dh-cycle">cycle {r.cycle}</span>}
                <span className="dh-by">{SOURCE_LABEL[r.source] || r.source} · {r.by}</span>
              </div>
              {r.categories.length > 0 && <div className="dh-cats">{r.categories.map((c) => <span className="dh-cat" key={c}>{c}</span>)}</div>}
              {r.changed && <div className="dh-delta">{r.changed}</div>}
              <p className="dh-fb">{r.feedback}</p>
            </div>
          </li>
        ))}
      </ol>
      {final && <details className="dh-draft dh-final"><summary>final manuscript body</summary><div className="dh-excerpt">{final}</div></details>}
      <p className="dh-human">Human feedback: <b>{humanCaptured ? "recorded above." : "not captured."}</b> {humanCaptured ? "A person has reviewed this draft." : "No person has reviewed this draft — its absence is real, not pending."}</p>
    </div>
  );
}

function DraftCard({ it }: { it: Item }) {
  const h = useRevisionLog(it.review ?? null);
  return (
    <div className={`pb-run db-rcard${it.track === "flagship" ? " pb-flag" : ""}`}>
      <div className="pb-run-top">
        <span className="pb-run-title">{it.title}</span>
        <span className="pb-chip" style={{ borderColor: vcolor(it.verdict), color: vcolor(it.verdict) }}>
          {it.verdict ? `${it.verdict}${it.verdict.toUpperCase() === "MINOR" ? " · not accepted" : ""}` : "no verdict yet"}
        </span>
      </div>
      <div className="pb-run-chips">
        <span className="db-track-chip">{TRACK_META[it.track].label}</span>
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
          {it.pdf && it.updated && <span className="db-updated" title="last updated">upd. {it.updated.slice(0, 10)}</span>}
          {it.figure && <a href={it.figure} target="_blank" rel="noopener noreferrer">figure ↗</a>}
          {it.review && <a href={it.review} target="_blank" rel="noopener noreferrer">referee ↗</a>}
          {it.review && <button type="button" className={`dh-toggle${h.open ? " on" : ""}`} onClick={h.toggle} aria-expanded={h.open}>revision log <span className="dh-caret">▸</span></button>}
        </span>
        <span className="db-tag">descriptive — not validated</span>
      </div>
      {h.open && <RevisionLog h={h} />}
    </div>
  );
}

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
  for (const f of FLAGSHIP) items.push({ title: f.title, track: "flagship", stage: 4, verdict: f.verdict, pdf: f.pdf, note: f.summary, updated: f.updated });
  for (const f of FRONTIER) items.push({ title: f.title, track: "frontier", stage: 3, verdict: null, pdf: f.pdf, note: f.sub, updated: f.updated });
  for (const r of runs.filter((x) => !isDemo(x))) {
    const stage = r.review_verdict ? 4 : r.pdf_url ? 3 : r.review_url ? 2 : 1;
    items.push({
      title: prettyMethod(r.method), track: "pipeline", stage, verdict: r.review_verdict, pdf: r.pdf_url, note: r.summary ?? "—",
      id: r.id, method: r.method, sources: r.data_sources, cycles: r.review_cycles, figure: r.figure_url, review: r.review_url, updated: r.created_utc,
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
              {rows.map((it, i) => <DraftCard it={it} key={`${tk}-${i}`} />)}
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
.db-links{display:flex;gap:.9rem;align-items:baseline;flex-wrap:wrap}
.db-links a{color:var(--lab-accent);text-decoration:none}
.db-updated{color:var(--lab-soft);font-size:.66rem;font-family:ui-monospace,monospace}
.db-links a:hover{text-decoration:underline}
.db-tag{font-size:.58rem;letter-spacing:.05em;text-transform:uppercase;color:#e0a458;white-space:nowrap}
.db-table-wrap{overflow-x:auto;border:1px solid var(--lab-line);border-radius:12px;background:var(--lab-panel)}
.db-table{width:100%;border-collapse:collapse;font-size:.8rem;min-width:560px}
.db-table th{text-align:left;font-weight:500;font-size:.62rem;text-transform:uppercase;letter-spacing:.06em;color:var(--lab-soft);border-bottom:1px solid var(--lab-line);padding:.5rem .6rem;white-space:nowrap}
.db-table td{padding:.5rem .6rem;border-bottom:1px solid var(--lab-line);color:var(--lab-ink);vertical-align:middle}
.db-table tbody tr:last-child td{border-bottom:none}
.db-mono{font-family:ui-monospace,monospace;font-size:.72rem;color:var(--lab-soft)}
@media(max-width:520px){.db-step span{font-size:.5rem}.db-links{gap:.6rem}}
.dh-toggle{background:transparent;border:1px solid var(--lab-line);color:var(--lab-soft);font:inherit;font-family:ui-monospace,monospace;font-size:.72rem;padding:.1rem .5rem;border-radius:7px;cursor:pointer;display:inline-flex;align-items:center;gap:.35rem}
.dh-toggle:hover,.dh-toggle.on{color:var(--lab-ink);border-color:var(--lab-accent)}
.dh-caret{display:inline-block;transition:transform .15s}
.dh-toggle.on .dh-caret{transform:rotate(90deg)}
.dh-wrap{margin-top:.75rem;padding:.85rem 1rem;background:#0a0d17;border:1px solid var(--lab-line);border-radius:10px}
.dh-note{font-size:.82rem;color:var(--lab-soft);font-style:italic}
.dh-banner{font-size:.72rem;line-height:1.5;color:var(--lab-soft);margin:0 0 .55rem;padding:.42rem .6rem;border:1px solid rgba(224,164,88,.35);border-radius:7px;background:rgba(224,164,88,.06)}
.dh-banner b{color:#e0a458}
.dh-state{font-size:.8rem;color:var(--lab-ink);margin:0 0 .85rem;line-height:1.5}
.dh-timeline{list-style:none;margin:0;padding:0;position:relative}
.dh-timeline::before{content:"";position:absolute;left:5px;top:6px;bottom:6px;width:1px;background:var(--lab-line)}
.dh-node{position:relative;padding:0 0 1.1rem 1.4rem}
.dh-dot{position:absolute;left:0;top:4px;width:11px;height:11px;border-radius:50%;box-shadow:0 0 0 3px #0a0d17}
.dh-head{display:flex;align-items:center;gap:.55rem;margin-bottom:.4rem;flex-wrap:wrap}
.dh-cycle{font-family:ui-monospace,monospace;font-size:.72rem;color:var(--lab-ink)}
.dh-by{font-size:.66rem;color:var(--lab-soft);font-family:ui-monospace,monospace}
.dh-delta{font-family:ui-monospace,monospace;font-size:.7rem;color:var(--lab-soft);margin:0 0 .4rem}
.dh-delta .add{color:var(--lab-accent2);font-style:normal}
.dh-delta .rm{color:#f47272;font-style:normal}
.dh-fb{font-size:.82rem;line-height:1.6;color:var(--lab-ink);margin:0 0 .5rem;white-space:pre-wrap}
.dh-draft{margin:.35rem 0 0}
.dh-draft>summary{cursor:pointer;font-size:.72rem;color:var(--lab-accent);font-family:ui-monospace,monospace}
.dh-excerpt{margin-top:.5rem;padding:.6rem .75rem;background:var(--lab-panel);border:1px solid var(--lab-line);border-radius:8px;font-size:.78rem;line-height:1.55;color:var(--lab-soft);white-space:pre-wrap;max-height:16rem;overflow:auto}
.dh-final>summary{color:var(--lab-accent2)}
.dh-human{font-size:.72rem;color:var(--lab-soft);margin:.7rem 0 0;padding-top:.6rem;border-top:1px solid var(--lab-line);font-style:italic}
.dh-human b{color:var(--lab-ink);font-style:normal}
.dh-lineage{font-size:.72rem;color:var(--lab-soft);margin:0 0 .5rem;font-family:ui-monospace,monospace}
.dh-lineage b{color:var(--lab-accent2)}
.dh-cats{display:flex;flex-wrap:wrap;gap:.3rem;margin:0 0 .45rem}
.dh-cat{font-family:ui-monospace,monospace;font-size:.58rem;letter-spacing:.03em;color:var(--lab-soft);border:1px solid var(--lab-line);border-radius:999px;padding:.05rem .45rem}
`;
