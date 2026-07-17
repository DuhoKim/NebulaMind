"use client";

import { useRef, useState } from "react";
import { STEPS, useTab, setTab } from "./labTabStore";

const TOPICS = [
  { value: "simulations-vs-physics", label: "Simulations vs physics — calibration ≠ validation" },
  { value: "jwst-high-z-nebular", label: "JWST high-z nebular diagnostics" },
  { value: "cosmic-chemical-evolution", label: "Cosmic chemical evolution (MZR / FMR)" },
  { value: "main-sequence-quenching", label: "Star-forming main sequence & quenching" },
  { value: "massive-galaxies-too-early", label: "Massive galaxies too early (SMF tension)" },
  { value: "custom", label: "Custom question…" },
];

const DATA_SOURCES = [
  { id: "sdss", label: "SDSS", sub: "SkyServer SQL" },
  { id: "jwst", label: "JWST", sub: "VizieR catalogs" },
  { id: "tng", label: "IllustrisTNG", sub: "simulation API" },
];

const METHODS = [
  { value: "scaling-relation-evolution", label: "Scaling-relation evolution (MS / MZR vs z)" },
  { value: "stellar-mass-function", label: "Stellar mass function / abundance" },
  { value: "mass-metallicity", label: "Mass–metallicity relation" },
  { value: "sf-efficiency-baryon-budget", label: "Star-formation efficiency / baryon budget" },
  { value: "sim-vs-observation", label: "Simulation vs observation confrontation" },
];

const METHOD_BLURB =
  "Bottom-up frontier map: ~12,000 refereed astro-ph.GA abstracts (2016–2026, NASA ADS) were embedded and clustered into 32 themes; 278 open debates + 200 unknowns from 19 landmark reviews were overlaid; clusters were ranked by open-question density × recent growth. These five sit at the top of that ranking.";

type Deriv = { cluster: string; debate: string; rank: string; papers: string; study: string; caveat?: string };

const DERIVATIONS: Record<string, Deriv> = {
  "simulations-vs-physics": {
    cluster: "Cluster 14 · “Hydrodynamic Cosmological Simulations of Galaxies” — the single largest cluster (634 papers; keywords methods:numerical, hydrodynamics, galaxy formation; sample titles include IllustrisTNG, FIRE-2, SIMBA).",
    debate: "Highest debate concentration of all 32 clusters — 53 debates / 26 unknowns, drawn from Somerville & Davé (2015): subgrid degeneracy, feedback & wind-recycling timescales, and matching the stellar-mass function without over-calibration.",
    rank: "frontier_score 0.776 — elevated to the #1 headline frontier as the field’s densest concentration of open questions. The framing: sims are tuned to a few z≈0 observables, so the real test is their predictions away from that calibration point.",
    papers: "IllustrisTNG (Pillepich+2018, Nelson+2019), FIRE-2, SIMBA.",
    study: "“Calibration Is Not Validation” — TNG100 (~3×10⁴ galaxies) confronted with SDSS + JWST z≈4–6 scaling-relation evolution; TNG forms stars too vigorously at high z.",
  },
  "jwst-high-z-nebular": {
    cluster: "Cluster 26 · “Nebular Diagnostics in High-Redshift Galaxies” (405 papers; keywords high-redshift, abundances, ISM; sample titles include JADES/GN-z11 nitrogen enhancement and MOSDEF electron-density work).",
    debate: "13 debates / 10 unknowns from Maiolino & Mannucci (2019) and Kewley et al. (2019): do local strong-line calibrations hold at high-z; the ~0.5 dex offset between direct-Te and theoretical strong-line abundances; the origin of extreme N/O in young systems.",
    rank: "frontier_score 0.797 — the 2nd-highest of all 32 clusters, powered by a high recent-growth fraction (0.42).",
    papers: "Nakajima+2023 (180 NIRSpec galaxies), Lisiecki+2025 (3743 MIRI/CEERS), Sanders+2021.",
    study: "“Galaxy Scaling Relations from z≈0 to the JWST Frontier” — MS & MZR out to JWST; a ~0.4 dex high-z metallicity deficit, near-constant across z≈4–7 on a matched Tₑ-anchored scale.",
  },
  "cosmic-chemical-evolution": {
    cluster: "Cluster 1 · “Cosmic Chemical Evolution of Galaxies” (447 papers; keywords abundances, evolution; sample titles include “De re metallica”, the origin of the MZR, and a fully Tₑ-anchored FMR).",
    debate: "15 debates / 7 unknowns from Maiolino & Mannucci (2019): inflow vs outflow as the driver of the FMR, the FMR’s universality / redshift-invariance at z>3, and the absolute gas-phase abundance zero point.",
    rank: "frontier_score 0.78 (4th of 32) — one of the highest debate counts among non-simulation clusters.",
    papers: "Tremonti+2004, Mannucci+2010 (FMR), Curti / Maiolino & Mannucci (2019).",
    study: "SDSS mass–metallicity relation & the FMR aperture — N=202,968 DR18 galaxies; finds no canonical FMR anti-correlation with total SFR and argues it is an aperture artifact.",
  },
  "main-sequence-quenching": {
    cluster: "Nearest match: Cluster 11 · “Galaxy Evolution: Gas, Star Formation, Models” (432 papers) — no cluster is branded specifically “main sequence / quenching”.",
    debate: "13 debates / 10 unknowns spanning Somerville & Davé (2015), Tacconi et al. (2020) and Förster Schreiber & Wuyts (2020): low- vs high-mass quenching, the green valley, and supply-starvation vs suppressed SFE vs rapid gas removal.",
    rank: "Not an independently top-ranked, named frontier — it has no standalone frontier_score. It maps to the nearest star-formation cluster and is analysed inside the scaling-relations study.",
    papers: "Speagle+2014 (main-sequence calibration); Förster Schreiber & Wuyts (2020).",
    study: "Realized as the SFMS / quenching component of the scaling-relations study — N=494,635; quench-50% at logM≈10.6; quenched fraction 0.04→0.18→0.70 across logM 9/10/11.",
    caveat: "Honest note: this is not a top-scored cluster of its own — it is the nearest star-formation theme plus the review-base quenching debates.",
  },
  "massive-galaxies-too-early": {
    cluster: "Split signal: Cluster 30 · “High-Redshift Galaxy Formation” is the fastest-growing cluster (455 papers, 71% recent, median year 2023; CEERS / z≈9–16 titles) but low debate count; SMHM context from Cluster 23. No single high-scored “SMF tension” cluster exists.",
    debate: "The JWST “impossibly massive early galaxies” ΛCDM tension — Boylan-Kolchin (2023) baryon budget vs Labbé (2023): is the massive-end shortfall cosmological, or driven by star-formation efficiency? (Somerville & Davé downsizing; Wechsler & Tinker SMHM.)",
    rank: "Selected on the strength of the debate × the fastest-growing cluster — not a high frontier_score cluster (cluster 30 scores only 0.411). The tension itself comes from the review base, not a top density×growth score.",
    papers: "Labbé+2023, Boylan-Kolchin (2023), Chworowsky+2024 (120 z≈4–7 galaxies), Weibel+2024, Tinker (2008, HMF).",
    study: "“Does IllustrisTNG Make Enough Massive Galaxies Early Enough?” — an SMF stress test at z≈4–6; passed a 6-cycle Deep-Research review.",
    caveat: "Honest note: driven by the review-base tension intersecting the fastest-growing cluster, not by a top density×growth score.",
  },
};

type Run = {
  id: string; status: string; log?: string[];
  result?: { summary?: string; figure_url?: string; pdf_url?: string; review?: string; review_model?: string; review_verdict?: string; review_cycles?: number; error?: string } | null;
};

export default function LabConfigurator() {
  const [topic, setTopic] = useState(TOPICS[0].value);
  const [custom, setCustom] = useState("");
  const [data, setData] = useState<Record<string, boolean>>({ sdss: true, jwst: false, tng: false });
  const [method, setMethod] = useState(METHODS[0].value);
  const [aastex, setAastex] = useState(true);
  const [drReview, setDrReview] = useState(true);
  const tab = useTab();

  const [plan, setPlan] = useState<Record<string, unknown> | null>(null);
  const [copied, setCopied] = useState(false);
  const [token, setToken] = useState("");
  const [run, setRun] = useState<Run | null>(null);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);

  const selectedData = Object.entries(data).filter(([, v]) => v).map(([k]) => k);
  const canAssemble = (topic !== "custom" || custom.trim().length > 0) && selectedData.length > 0;

  function goNext() {
    const i = STEPS.findIndex((s) => s.key === tab);
    if (i < STEPS.length - 1) setTab(STEPS[i + 1].key);
  }

  function assemble() {
    const p = {
      topic: topic === "custom" ? custom.trim() : topic,
      topic_source: topic === "custom" ? "custom" : "frontier-map",
      data_sources: selectedData,
      method,
      outputs: [aastex && "aastex-draft", drReview && "dr-review-loop"].filter(Boolean),
    };
    setPlan(p); setRun(null); setErr(""); setCopied(false);
  }

  function copySpec() {
    if (plan && navigator.clipboard) {
      navigator.clipboard.writeText(JSON.stringify(plan, null, 2)).then(() => {
        setCopied(true); setTimeout(() => setCopied(false), 1600);
      });
    }
  }

  function poll(id: string) {
    const tick = async () => {
      try {
        const r = await fetch(`/api/lab/runs/${id}`, { cache: "no-store" });
        const rec: Run = await r.json();
        setRun(rec);
        if (["done", "accepted", "failed"].includes(rec.status)) { setBusy(false); return; }
      } catch { /* keep polling */ }
      timer.current = setTimeout(tick, 4000);
    };
    tick();
  }

  async function launch() {
    if (!plan || !token.trim()) return;
    setBusy(true); setErr(""); setRun(null);
    if (timer.current) clearTimeout(timer.current);
    try {
      const res = await fetch("/api/lab/runs", {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token.trim()}` },
        body: JSON.stringify(plan),
      });
      if (res.status === 401) { setErr("Invalid run token."); setBusy(false); return; }
      if (!res.ok) { setErr(`Submit failed (${res.status}).`); setBusy(false); return; }
      const { run_id } = await res.json();
      setRun({ id: run_id, status: "queued" });
      poll(run_id);
    } catch {
      setErr("Network error — could not reach the runner."); setBusy(false);
    }
  }

  const spec = plan ? JSON.stringify(plan, null, 2) : null;
  const statusColor = run?.status === "done" ? "var(--lab-accent2)"
    : run?.status === "failed" ? "#f47272"
    : run?.status === "accepted" ? "var(--lab-accent)" : "var(--lab-soft)";

  return (
    <div className="cfg">
      <style>{`
        .cfg{border:1px solid var(--lab-line);border-radius:14px;background:var(--lab-panel);overflow:hidden}
        .cfg-tabs{display:flex;background:#0c101c;border-bottom:1px solid var(--lab-line)}
        .cfg-tab{flex:1;display:flex;flex-direction:column;gap:.2rem;align-items:flex-start;padding:.8rem 1rem;background:transparent;border:none;border-right:1px solid var(--lab-line);cursor:pointer;text-align:left;transition:background .12s}
        .cfg-tab:last-child{border-right:none}
        .cfg-tab:hover{background:rgba(124,134,255,.06)}
        .cfg-tab.on{background:var(--lab-panel);box-shadow:inset 0 2px 0 var(--lab-accent)}
        .cfg-tab .n{font-family:ui-monospace,monospace;font-size:.64rem;letter-spacing:.14em;color:var(--lab-soft)}
        .cfg-tab.on .n{color:var(--lab-accent)}
        .cfg-tab .t{font-size:.92rem;font-weight:600;color:var(--lab-soft);display:flex;align-items:center;gap:.35rem}
        .cfg-tab.on .t{color:var(--lab-ink)}
        .cfg-tab .chk{color:var(--lab-accent2);font-size:.72rem}
        .cfg-panel{padding:1.3rem 1.25rem;border-bottom:1px solid var(--lab-line);min-height:104px}
        .cfg-panel-h{font-family:ui-monospace,monospace;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--lab-accent2);margin:0 0 .85rem}
        .cfg-method{font-size:.8rem;color:var(--lab-soft);line-height:1.6;margin:0 0 .95rem;padding:.7rem .85rem;border-left:2px solid var(--lab-accent);background:rgba(124,134,255,.05);border-radius:0 8px 8px 0}
        .cfg-deriv{margin-top:1rem;border:1px solid var(--lab-line);border-radius:10px;background:#0a0d17;overflow:hidden}
        .cfg-deriv-h{padding:.65rem .9rem;border-bottom:1px solid var(--lab-line);font-family:ui-monospace,monospace;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--lab-accent2)}
        .cfg-deriv-row{display:grid;grid-template-columns:118px 1fr;gap:.85rem;padding:.65rem .9rem;border-bottom:1px solid rgba(36,42,61,.55);font-size:.84rem;line-height:1.55}
        .cfg-deriv-row:last-child{border-bottom:none}
        .cfg-deriv-k{font-family:ui-monospace,monospace;font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;color:var(--lab-soft);padding-top:.15rem}
        .cfg-deriv-v{color:var(--lab-ink)}
        .cfg-deriv-caveat{padding:.6rem .9rem;background:rgba(224,164,88,.09);color:#e0a458;font-size:.78rem;line-height:1.5;border-top:1px solid var(--lab-line)}
        @media(max-width:560px){.cfg-deriv-row{grid-template-columns:1fr;gap:.2rem}}
        .cfg-next{margin-top:1.1rem;background:transparent;border:1px solid var(--lab-line);color:var(--lab-ink);border-radius:8px;padding:.45rem .95rem;font-size:.82rem;cursor:pointer}
        .cfg-next:hover{border-color:var(--lab-accent)}
        .cfg-label{font-family:ui-monospace,monospace;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--lab-accent2)}
        .cfg-label .step{display:block;color:var(--lab-soft);font-size:.66rem;margin-top:.2rem}
        .cfg-sel,.cfg-inp{width:100%;background:#0a0d17;color:var(--lab-ink);border:1px solid var(--lab-line);border-radius:8px;padding:.6rem .7rem;font-size:.9rem;font-family:inherit}
        .cfg-sel:focus,.cfg-inp:focus{outline:none;border-color:var(--lab-accent)}
        .cfg-chips{display:flex;gap:.55rem;flex-wrap:wrap}
        .cfg-chip{display:flex;flex-direction:column;gap:.1rem;border:1px solid var(--lab-line);border-radius:9px;padding:.5rem .8rem;cursor:pointer;background:#0a0d17;user-select:none;transition:border-color .12s,background .12s}
        .cfg-chip.on{border-color:var(--lab-accent);background:rgba(124,134,255,.12)}
        .cfg-chip b{font-size:.86rem;font-weight:600;color:var(--lab-ink)}
        .cfg-chip span{font-size:.68rem;color:var(--lab-soft);font-family:ui-monospace,monospace}
        .cfg-out{display:flex;gap:1.1rem;flex-wrap:wrap}
        .cfg-check{display:flex;align-items:center;gap:.45rem;font-size:.88rem;color:var(--lab-ink);cursor:pointer;user-select:none}
        .cfg-check input{accent-color:var(--lab-accent);width:15px;height:15px}
        .cfg-foot{display:flex;align-items:center;gap:1rem;padding:1.1rem 1.25rem;background:#0c101c;flex-wrap:wrap}
        .cfg-btn{background:var(--lab-accent);color:#0a0d17;font-weight:600;border:none;border-radius:9px;padding:.65rem 1.15rem;font-size:.9rem;cursor:pointer}
        .cfg-btn:disabled{opacity:.45;cursor:not-allowed}
        .cfg-btn.ghost{background:transparent;color:var(--lab-ink);border:1px solid var(--lab-line)}
        .cfg-hint{font-size:.78rem;color:var(--lab-soft)}
        .cfg-spec{border-top:1px solid var(--lab-line);background:#080b13}
        .cfg-spec .bar{display:flex;justify-content:space-between;align-items:center;padding:.6rem 1.25rem;font-family:ui-monospace,monospace;font-size:.72rem;color:var(--lab-soft)}
        .cfg-spec pre{margin:0;padding:0 1.25rem 1rem;font-family:ui-monospace,monospace;font-size:.82rem;color:#c7f0e6;overflow-x:auto;line-height:1.55}
        .cfg-copy{background:transparent;border:1px solid var(--lab-line);color:var(--lab-soft);border-radius:6px;padding:.25rem .6rem;font-size:.72rem;cursor:pointer;font-family:ui-monospace,monospace}
        .cfg-launch{border-top:1px solid var(--lab-line);padding:1.1rem 1.25rem;display:flex;gap:.7rem;align-items:center;flex-wrap:wrap;background:#0c101c}
        .cfg-tok{flex:1;min-width:160px;background:#0a0d17;color:var(--lab-ink);border:1px solid var(--lab-line);border-radius:8px;padding:.55rem .7rem;font-size:.85rem;font-family:ui-monospace,monospace}
        .cfg-err{color:#f47272;font-size:.8rem}
        .cfg-status{border-top:1px solid var(--lab-line);padding:1rem 1.25rem;background:#080b13}
        .cfg-pill{display:inline-block;font-family:ui-monospace,monospace;font-size:.72rem;padding:.2rem .6rem;border-radius:999px;border:1px solid var(--lab-line)}
        .cfg-log{margin:.7rem 0 0;font-family:ui-monospace,monospace;font-size:.74rem;color:var(--lab-soft);line-height:1.6;white-space:pre-wrap}
        .cfg-result{margin-top:.8rem;font-size:.9rem;color:var(--lab-ink);line-height:1.55}
        .cfg-result img{max-width:100%;border:1px solid var(--lab-line);border-radius:10px;margin-top:.7rem;background:#fff}
        @media(max-width:560px){.cfg-tab .n{display:none}.cfg-tab{padding:.7rem .5rem}.cfg-tab .t{font-size:.82rem}}
      `}</style>

      <div className="cfg-panel" role="tabpanel">
        <p className="cfg-panel-h">{STEPS.find((s) => s.key === tab)?.heading}</p>

        {tab === "topic" && (
          <div>
            <p className="cfg-method">{METHOD_BLURB}</p>
            <select className="cfg-sel" value={topic} onChange={(e) => setTopic(e.target.value)}>
              {TOPICS.map((t) => <option key={t.value} value={t.value}>{t.label}</option>)}
            </select>
            {topic === "custom" ? (
              <>
                <input className="cfg-inp" style={{ marginTop: ".55rem" }} placeholder="Describe your research question…"
                  value={custom} onChange={(e) => setCustom(e.target.value)} />
                <p className="cfg-hint" style={{ marginTop: ".7rem" }}>
                  A custom question bypasses the frontier map — you supply the research question directly.
                </p>
              </>
            ) : DERIVATIONS[topic] && (
              <div className="cfg-deriv">
                <div className="cfg-deriv-h">How this topic was derived</div>
                <div className="cfg-deriv-row"><span className="cfg-deriv-k">Cluster</span><span className="cfg-deriv-v">{DERIVATIONS[topic].cluster}</span></div>
                <div className="cfg-deriv-row"><span className="cfg-deriv-k">Open debate</span><span className="cfg-deriv-v">{DERIVATIONS[topic].debate}</span></div>
                <div className="cfg-deriv-row"><span className="cfg-deriv-k">Why it ranks</span><span className="cfg-deriv-v">{DERIVATIONS[topic].rank}</span></div>
                <div className="cfg-deriv-row"><span className="cfg-deriv-k">Key papers</span><span className="cfg-deriv-v">{DERIVATIONS[topic].papers}</span></div>
                <div className="cfg-deriv-row"><span className="cfg-deriv-k">Becomes</span><span className="cfg-deriv-v">{DERIVATIONS[topic].study}</span></div>
                {DERIVATIONS[topic].caveat && <div className="cfg-deriv-caveat">⚠ {DERIVATIONS[topic].caveat}</div>}
              </div>
            )}
          </div>
        )}

        {tab === "data" && (
          <div className="cfg-chips">
            {DATA_SOURCES.map((d) => (
              <div key={d.id} className={`cfg-chip${data[d.id] ? " on" : ""}`}
                onClick={() => setData((s) => ({ ...s, [d.id]: !s[d.id] }))} role="button" tabIndex={0}
                onKeyDown={(e) => { if (e.key === "Enter" || e.key === " ") setData((s) => ({ ...s, [d.id]: !s[d.id] })); }}>
                <b>{d.label}</b><span>{d.sub}</span>
              </div>
            ))}
          </div>
        )}

        {tab === "research" && (
          <select className="cfg-sel" value={method} onChange={(e) => setMethod(e.target.value)}>
            {METHODS.map((m) => <option key={m.value} value={m.value}>{m.label}</option>)}
          </select>
        )}

        {tab === "paper" && (
          <div className="cfg-out">
            <label className="cfg-check"><input type="checkbox" checked={aastex} onChange={(e) => setAastex(e.target.checked)} /> AASTeX draft + figures</label>
            <label className="cfg-check"><input type="checkbox" checked={drReview} onChange={(e) => setDrReview(e.target.checked)} /> Deep-Research review loop</label>
          </div>
        )}

        {tab !== "paper" && (
          <button className="cfg-next" onClick={goNext}>Next →</button>
        )}
      </div>

      <div className="cfg-foot">
        <button className="cfg-btn ghost" onClick={assemble} disabled={!canAssemble}>Assemble run plan →</button>
        <span className="cfg-hint">
          {canAssemble ? "Builds a reproducible run spec, then launch it below." : "Pick a topic and at least one data source."}
        </span>
      </div>

      {spec && (
        <div className="cfg-spec">
          <div className="bar">
            <span>run-plan.json</span>
            <button className="cfg-copy" onClick={copySpec}>{copied ? "copied ✓" : "copy"}</button>
          </div>
          <pre>{spec}</pre>
        </div>
      )}

      {plan && (
        <div className="cfg-launch">
          <input className="cfg-tok" type="password" placeholder="run token" value={token}
            onChange={(e) => setToken(e.target.value)} autoComplete="off" />
          <button className="cfg-btn" onClick={launch} disabled={busy || !token.trim()}>
            {busy ? "Running…" : "Launch run"}
          </button>
          {err && <span className="cfg-err">{err}</span>}
          {!err && <span className="cfg-hint">Gated — needs the run token.</span>}
        </div>
      )}

      {run && (
        <div className="cfg-status">
          <span className="cfg-pill" style={{ color: statusColor, borderColor: statusColor }}>{run.status}</span>
          <span style={{ marginLeft: ".6rem", fontFamily: "ui-monospace,monospace", fontSize: ".72rem", color: "var(--lab-soft)" }}>run {run.id}</span>
          {run.log && run.log.length > 0 && <div className="cfg-log">{run.log.slice(-5).join("\n")}</div>}
          {run.result && (
            <div className="cfg-result">
              {run.result.summary && <p style={{ margin: 0 }}>{run.result.summary}</p>}
              {run.result.error && <p style={{ margin: 0, color: "#f47272" }}>Error: {run.result.error}</p>}
              {run.result.figure_url && (
                // eslint-disable-next-line @next/next/no-img-element
                <img src={run.result.figure_url} alt="run figure" />
              )}
              {run.result.pdf_url && (
                <a href={run.result.pdf_url} target="_blank" rel="noopener noreferrer"
                   style={{ display: "inline-block", marginTop: ".6rem", color: "var(--lab-accent)", fontFamily: "ui-monospace,monospace", fontSize: ".82rem" }}>
                  Download AASTeX manuscript (PDF) ↓
                </a>
              )}
              {run.result.review && (
                <details style={{ marginTop: ".7rem" }}>
                  <summary style={{ cursor: "pointer", color: "var(--lab-accent2)", fontFamily: "ui-monospace,monospace", fontSize: ".78rem" }}>
                    Review–revise loop
                    {run.result.review_verdict ? ` · ${run.result.review_verdict}` : ""}
                    {run.result.review_cycles ? ` after ${run.result.review_cycles} cycle${run.result.review_cycles > 1 ? "s" : ""}` : ""}
                    {run.result.review_model ? ` · ${run.result.review_model}` : ""}
                  </summary>
                  <pre style={{ whiteSpace: "pre-wrap", fontSize: ".8rem", color: "var(--lab-soft)", margin: ".5rem 0 0", lineHeight: 1.5 }}>{run.result.review}</pre>
                </details>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
