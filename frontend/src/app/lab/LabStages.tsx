"use client";

import { useState } from "react";
import { STEPS, useTab, setTab } from "./labTabStore";
import { FRONTIERS } from "./frontiersData";

const MAXSCORE = Math.max(...FRONTIERS.map((f) => f.score));

// deterministic pseudo-random in [0,1) — stable across SSR/CSR (no Math.random)
function sd(i: number): number {
  const x = Math.sin(i * 12.9898 + 78.233) * 43758.5453;
  return x - Math.floor(x);
}

const CLUSTER_COLS = ["#7c86ff", "#4ad6c4", "#e0a458", "#f47272", "#8b93c9"];

function DerivationDiagram() {
  return (
    <svg viewBox="0 0 900 190" role="img"
      aria-label="12,000 papers embedded into vectors, clustered into 32 themes, then ranked into research frontiers">
      <defs>
        <marker id="lab-ah" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto">
          <path d="M0 0 L6 3 L0 6 z" fill="#7c86ff" />
        </marker>
      </defs>
      {/* Stage 1 — papers grid */}
      {Array.from({ length: 30 }).map((_, i) => {
        const c = i % 6, r = Math.floor(i / 6);
        return <rect key={`p${i}`} x={44 + c * 12} y={44 + r * 13} width="8" height="10" rx="1.5" fill="#5b6486" />;
      })}
      <path d="M150 92 h42" stroke="#7c86ff" strokeWidth="1.5" markerEnd="url(#lab-ah)" />
      {/* Stage 2 — embedding scatter */}
      {Array.from({ length: 46 }).map((_, i) => (
        <circle key={`e${i}`} cx={278 + sd(i) * 92} cy={46 + sd(i + 46) * 88} r="2.6" fill="#7c86ff" fillOpacity="0.7" />
      ))}
      <path d="M402 92 h42" stroke="#7c86ff" strokeWidth="1.5" markerEnd="url(#lab-ah)" />
      {/* Stage 3 — 5 clusters */}
      {Array.from({ length: 46 }).map((_, i) => {
        const g = Math.floor(sd(i + 5) * 5);
        const gx = 508 + (g % 3) * 42, gy = 54 + Math.floor(g / 3) * 44;
        return <circle key={`c${i}`} cx={gx + (sd(i) - 0.5) * 26} cy={gy + (sd(i + 23) - 0.5) * 26} r="2.9" fill={CLUSTER_COLS[g]} />;
      })}
      <path d="M652 92 h42" stroke="#7c86ff" strokeWidth="1.5" markerEnd="url(#lab-ah)" />
      {/* Stage 4 — ranked bars, top 3 lit = frontiers */}
      {[0.95, 0.85, 0.78, 0.67, 0.57, 0.47, 0.37, 0.27].map((w, i) => (
        <rect key={`b${i}`} x="712" y={45 + i * 13} width={w * 150} height="7" rx="3" fill={i < 3 ? "#7c86ff" : "#2a3150"} />
      ))}
      {/* labels */}
      <g fontFamily="ui-monospace,monospace" fontSize="10.5" fill="#9aa3b8" textAnchor="middle">
        <text x="88" y="176">12,000 papers</text>
        <text x="324" y="176">embed → vectors</text>
        <text x="566" y="176">32 clusters</text>
        <text x="795" y="176">ranked frontiers</text>
      </g>
    </svg>
  );
}

const DATA_SOURCES = [
  { label: "SDSS", sub: "SkyServer SQL", desc: "z≈0 spectroscopic anchor — galSpecExtra / galSpecLine (mass–metallicity, main sequence)." },
  { label: "JWST", sub: "VizieR catalogs", desc: "high-z frontier — Nakajima+23 (NIRSpec), Lisiecki+25 (CEERS), Chworowsky+24." },
  { label: "IllustrisTNG", sub: "simulation API", desc: "TNG100-1 group catalogs — sim-vs-observation and stellar mass functions." },
];

const METHODS = [
  { label: "Scaling-relation evolution", desc: "main sequence & MZR vs redshift, z≈0 → JWST." },
  { label: "Stellar mass function / abundance", desc: "number density vs stellar mass; the massive-end tension." },
  { label: "Mass–metallicity relation", desc: "12+log(O/H) vs stellar mass; FMR aperture test." },
  { label: "Star-formation efficiency / baryon budget", desc: "M★ / (f_b M_halo) vs halo mass; Boylan-Kolchin check." },
  { label: "Simulation vs observation", desc: "confront TNG predictions with observed relations." },
];

const OUTPUTS = [
  { label: "AASTeX draft + figures", desc: "manuscript compiled to PDF via tectonic." },
  { label: "Review–revise loop", desc: "automated referee (astrosage-70b) — review → revise until the science holds." },
];

const METHOD_STEPS = [
  "12,000 abstracts · astro-ph.GA · 2016–2026 · NASA ADS",
  "embed → 32 clusters",
  "overlay 278 debates + 200 unknowns · 19 reviews",
  "rank = open-Q density × growth",
];

const PICK_STEPS: [string, string][] = [
  ["Corpus", "~12,000 refereed astro-ph.GA papers (2016–2026) are pulled from NASA ADS — the whole recent literature of galaxy evolution, not a hand-picked sample."],
  ["Embedding", "every abstract is turned into a vector, so papers that talk about the same physics land near each other in a space of meaning."],
  ["Clustering", "those vectors self-organize into 32 research themes with no human labeling — the field's own structure, read back out of it."],
  ["Debate overlay", "278 open debates and 200 unknowns, extracted from 19 landmark reviews, are mapped onto the clusters to mark where the science is genuinely unsettled."],
  ["Ranking", "each cluster is scored by open-question density × recent growth; the most contested, fastest-moving themes rise to the top."],
];

type Deriv = {
  cluster: string; size: string; score: string; debates: string;
  reviews: string; questions: string; papers: string; study: string; caveat?: string;
};

const DERIVATIONS: Record<string, Deriv> = {
  "simulations-vs-physics": {
    cluster: "14 · Hydrodynamic Cosmological Simulations of Galaxies",
    size: "634 papers · largest of 32",
    score: "0.776 · rank 5 / 32",
    debates: "53 debates / 26 unknowns · highest of any cluster",
    reviews: "Somerville & Davé (2015)",
    questions: "subgrid degeneracy · feedback & wind-recycling timescales · SMF without over-calibration",
    papers: "IllustrisTNG (Pillepich+18, Nelson+19) · FIRE-2 · SIMBA",
    study: "Calibration Is Not Validation — TNG100 (~3×10⁴) vs SDSS + JWST z≈4–6",
  },
  "jwst-high-z-nebular": {
    cluster: "26 · Nebular Diagnostics in High-Redshift Galaxies",
    size: "405 papers",
    score: "0.797 · rank 2 / 32",
    debates: "13 debates / 10 unknowns",
    reviews: "Maiolino & Mannucci (2019) · Kewley et al. (2019)",
    questions: "strong-line calibrations at high-z · Tₑ vs strong-line ≈0.5 dex offset · extreme N/O in young systems",
    papers: "Nakajima+23 (180 NIRSpec) · Lisiecki+25 (3743 CEERS) · Sanders+21",
    study: "Scaling relations z≈0→JWST — MS & MZR; ≈0.4 dex metallicity deficit, z≈4–7",
  },
  "cosmic-chemical-evolution": {
    cluster: "1 · Cosmic Chemical Evolution of Galaxies",
    size: "447 papers",
    score: "0.780 · rank 4 / 32",
    debates: "15 debates / 7 unknowns · highest of non-sim clusters",
    reviews: "Maiolino & Mannucci (2019)",
    questions: "inflow vs outflow driving the FMR · FMR universality at z>3 · absolute abundance zero point",
    papers: "Tremonti+04 · Mannucci+10 (FMR) · Curti / Maiolino & Mannucci 19",
    study: "SDSS MZR & FMR aperture — N=202,968 DR18; FMR = aperture artifact",
  },
  "main-sequence-quenching": {
    cluster: "11 · Galaxy Evolution: Gas, Star Formation, Models (nearest)",
    size: "432 papers",
    score: "0.759 · not an independently named frontier",
    debates: "13 debates / 10 unknowns",
    reviews: "Somerville & Davé (2015) · Tacconi et al. (2020) · Förster Schreiber & Wuyts (2020)",
    questions: "low- vs high-mass quenching · green valley · starvation vs suppressed SFE vs gas removal",
    papers: "Speagle+14 (MS) · Förster Schreiber & Wuyts 20",
    study: "SFMS / quenching within the scaling-relations study — N=494,635; quench-50% logM≈10.6",
    caveat: "Not a top-scored cluster of its own — nearest star-formation theme + review-base quenching debates.",
  },
  "massive-galaxies-too-early": {
    cluster: "30 · High-Redshift Galaxy Formation (+ 23, SMHM)",
    size: "455 papers · fastest-growing (71% recent, median 2023)",
    score: "0.411 · low — selected on the debate, not the score",
    debates: "2 in-cluster debates · tension from the review base",
    reviews: "Boylan-Kolchin (2023) vs Labbé (2023) · Wechsler & Tinker (2018)",
    questions: "massive-end shortfall: cosmological, or star-formation-efficiency-driven?",
    papers: "Labbé+23 · Boylan-Kolchin 23 · Chworowsky+24 (120 z≈4–7) · Weibel+24 · Tinker 08 (HMF)",
    study: "Does TNG make enough massive galaxies early? — SMF stress test z≈4–6; 6-cycle review",
    caveat: "Driven by the review-base tension × the fastest-growing cluster, not a top density×growth score.",
  },
};

export default function LabStages() {
  const [topic, setTopic] = useState("simulations-vs-physics");
  const tab = useTab();

  function goNext() {
    const i = STEPS.findIndex((s) => s.key === tab);
    if (i < STEPS.length - 1) setTab(STEPS[i + 1].key);
  }

  return (
    <div className="cfg">
      <style>{`
        .cfg{border:1px solid var(--lab-line);border-radius:14px;background:var(--lab-panel);overflow:hidden}
        .cfg-panel{padding:1.3rem 1.25rem;min-height:104px}
        .cfg-panel-h{font-family:ui-monospace,monospace;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--lab-accent2);margin:0 0 .85rem}
        .cfg-pipe{display:flex;flex-wrap:wrap;align-items:center;gap:.3rem .5rem;font-family:ui-monospace,monospace;font-size:.735rem;color:var(--lab-ink);line-height:1.5;margin:0 0 .5rem;padding:.6rem .75rem;background:#0a0d17;border:1px solid var(--lab-line);border-radius:8px}
        .cfg-pipe em{color:var(--lab-accent);font-style:normal;font-weight:700}
        .cfg-credit{font-size:.73rem;color:var(--lab-soft);line-height:1.4;margin:0 0 .9rem}
        .cfg-credit a{color:var(--lab-accent)}
        .cfg-sel{width:100%;background:#0a0d17;color:var(--lab-ink);border:1px solid var(--lab-line);border-radius:8px;padding:.6rem .7rem;font-size:.9rem;font-family:inherit}
        .cfg-sel:focus{outline:none;border-color:var(--lab-accent)}
        .cfg-next{margin-top:1.1rem;background:transparent;border:1px solid var(--lab-line);color:var(--lab-ink);border-radius:8px;padding:.45rem .95rem;font-size:.82rem;cursor:pointer}
        .cfg-next:hover{border-color:var(--lab-accent)}
        .cfg-deriv{margin-top:1rem;border:1px solid var(--lab-line);border-radius:10px;background:#0a0d17;overflow:hidden}
        .cfg-deriv-h{padding:.65rem .9rem;border-bottom:1px solid var(--lab-line);font-family:ui-monospace,monospace;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--lab-accent2)}
        .cfg-deriv-row{display:grid;grid-template-columns:118px 1fr;gap:.85rem;padding:.65rem .9rem;border-bottom:1px solid rgba(36,42,61,.55);font-size:.84rem;line-height:1.55}
        .cfg-deriv-row:last-child{border-bottom:none}
        .cfg-deriv-k{font-family:ui-monospace,monospace;font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;color:var(--lab-soft);padding-top:.15rem}
        .cfg-deriv-v{color:var(--lab-ink)}
        .cfg-deriv-caveat{padding:.6rem .9rem;background:rgba(224,164,88,.09);color:#e0a458;font-size:.78rem;line-height:1.5;border-top:1px solid var(--lab-line)}
        .cfg-steps{list-style:none;margin:.2rem 0 1rem;padding:0;display:flex;flex-direction:column;gap:.55rem}
        .cfg-steps li{display:grid;grid-template-columns:1.5rem 1fr;gap:.65rem;align-items:start;font-size:.85rem;line-height:1.55;color:var(--lab-soft)}
        .cfg-steps .n{font-family:ui-monospace,monospace;font-size:.68rem;color:var(--lab-accent);border:1px solid var(--lab-line);border-radius:5px;text-align:center;padding:.12rem 0;line-height:1.2}
        .cfg-steps b{color:var(--lab-ink);font-weight:650}
        .cfg-viz{margin:.3rem 0 1.1rem;border:1px solid var(--lab-line);border-radius:10px;background:#0a0d17;padding:1rem 1.1rem .75rem}
        .cfg-viz svg{width:100%;height:auto;display:block}
        .cfg-viz .cap{font-size:.72rem;color:var(--lab-soft);text-align:center;margin:.55rem 0 0;line-height:1.5}
        .cfg-maplead{font-size:.78rem;color:var(--lab-soft);line-height:1.5;margin:.2rem 0 .7rem}
        .cfg-map{display:flex;flex-direction:column;gap:.3rem}
        .cfg-mrow{border:1px solid var(--lab-line);border-radius:8px;background:#0a0d17;overflow:hidden}
        .cfg-mrow.topic{border-color:rgba(124,134,255,.4)}
        .cfg-mrow.open{border-color:var(--lab-accent)}
        .cfg-mhead{width:100%;display:grid;grid-template-columns:2.3rem 1fr auto 88px 3.1rem;gap:.55rem;align-items:center;background:transparent;border:none;padding:.5rem .7rem;text-align:left;font-family:inherit;cursor:default}
        .cfg-mrow.topic .cfg-mhead{cursor:pointer}
        .cfg-mrow.topic .cfg-mhead:hover{background:rgba(124,134,255,.06)}
        .cfg-mrank{font-family:ui-monospace,monospace;font-size:.7rem;color:var(--lab-soft)}
        .cfg-mname{font-size:.85rem;color:var(--lab-ink);font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
        .cfg-mrow:not(.topic) .cfg-mname{color:var(--lab-soft)}
        .cfg-mbadge{font-family:ui-monospace,monospace;font-size:.6rem;letter-spacing:.03em;color:var(--lab-accent);border:1px solid rgba(124,134,255,.5);border-radius:999px;padding:.05rem .4rem;white-space:nowrap}
        .cfg-mbadge.flag{color:#e0a458;border-color:rgba(224,164,88,.5)}
        .cfg-mbar{height:4px;border-radius:2px;background:#1a1f30;overflow:hidden}
        .cfg-mbar i{display:block;height:100%;background:linear-gradient(90deg,var(--lab-accent),var(--lab-accent2))}
        .cfg-mscoren{font-family:ui-monospace,monospace;font-size:.68rem;color:var(--lab-accent2);text-align:right}
        .cfg-mrow .cfg-deriv{margin:0;border:none;border-top:1px solid var(--lab-line);border-radius:0}
        @media(max-width:560px){.cfg-mhead{grid-template-columns:1.7rem 1fr auto;gap:.4rem}.cfg-mbar,.cfg-mscoren{display:none}}
        .cfg-list{display:flex;flex-direction:column;gap:.55rem}
        .cfg-item{border:1px solid var(--lab-line);border-radius:9px;background:#0a0d17;padding:.7rem .85rem}
        .cfg-item-k{font-size:.9rem;font-weight:650;color:var(--lab-ink)}
        .cfg-item-k span{font-family:ui-monospace,monospace;font-size:.7rem;color:var(--lab-accent2);font-weight:400;margin-left:.5rem}
        .cfg-item-v{font-size:.82rem;color:var(--lab-soft);line-height:1.5;margin-top:.25rem}
        @media(max-width:560px){.cfg-deriv-row{grid-template-columns:1fr;gap:.2rem}}
      `}</style>

      <div className="cfg-panel" role="tabpanel">
        <p className="cfg-panel-h">{STEPS.find((s) => s.key === tab)?.heading}</p>

        {tab === "topic" && (
          <div>
            <div className="cfg-pipe">
              {METHOD_STEPS.map((s, i) => (
                <span key={i}>{i > 0 && <em>→</em>}{s}</span>
              ))}
            </div>
            <p className="cfg-credit">
              Method after <a href="https://github.com/star4citizen/Astro-NoteAI" target="_blank" rel="noopener noreferrer">Astro-Note&nbsp;AI</a> (Suk&nbsp;Kim) — turning a body of papers into a navigable, machine-read map of a field.
            </p>
            <ol className="cfg-steps">
              {PICK_STEPS.map(([k, v], i) => (
                <li key={k}><span className="n">{i + 1}</span><span><b>{k}</b> — {v}</span></li>
              ))}
            </ol>
            <div className="cfg-viz">
              <DerivationDiagram />
              <p className="cap">
                12,000 papers → embedded into vectors → 32 self-organized clusters → ranked by open-question
                density × growth. The top science frontiers (lit) became the research topics.
              </p>
            </div>
            <p className="cfg-maplead">
              All 32 clusters, ranked by frontier score. The five that became research topics are marked —
              select one for its full derivation.
            </p>
            <div className="cfg-map">
              {FRONTIERS.map((f, i) => {
                const isTopic = !!f.topic;
                const open = isTopic && f.topic === topic;
                const dv = isTopic ? DERIVATIONS[f.topic as string] : null;
                const drows: [string, string][] = dv
                  ? [
                      ["Cluster", dv.cluster], ["Size", dv.size], ["Score", dv.score],
                      ["Debates", dv.debates], ["Reviews", dv.reviews], ["Open Qs", dv.questions],
                      ["Papers", dv.papers], ["Study", dv.study],
                    ]
                  : [];
                return (
                  <div key={f.cluster} className={`cfg-mrow${isTopic ? " topic" : ""}${open ? " open" : ""}`}>
                    <button type="button" className="cfg-mhead"
                      onClick={() => { if (isTopic) setTopic(f.topic as string); }} disabled={!isTopic}>
                      <span className="cfg-mrank">#{i + 1}</span>
                      <span className="cfg-mname">{f.name}</span>
                      {isTopic
                        ? <span className={`cfg-mbadge${f.topicFlagged ? " flag" : ""}`}>topic{f.topicFlagged ? " · nearest" : ""}</span>
                        : <span />}
                      <span className="cfg-mbar"><i style={{ width: `${(f.score / MAXSCORE) * 100}%` }} /></span>
                      <span className="cfg-mscoren">{f.score.toFixed(3)}</span>
                    </button>
                    {open && dv && (
                      <div className="cfg-deriv">
                        {drows.map(([k, v]) => (
                          <div className="cfg-deriv-row" key={k}>
                            <span className="cfg-deriv-k">{k}</span><span className="cfg-deriv-v">{v}</span>
                          </div>
                        ))}
                        {dv.caveat && <div className="cfg-deriv-caveat">⚠ {dv.caveat}</div>}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {tab === "data" && (
          <div className="cfg-list">
            {DATA_SOURCES.map((s) => (
              <div className="cfg-item" key={s.label}>
                <div className="cfg-item-k">{s.label}<span>{s.sub}</span></div>
                <div className="cfg-item-v">{s.desc}</div>
              </div>
            ))}
          </div>
        )}

        {tab === "research" && (
          <div className="cfg-list">
            {METHODS.map((m) => (
              <div className="cfg-item" key={m.label}>
                <div className="cfg-item-k">{m.label}</div>
                <div className="cfg-item-v">{m.desc}</div>
              </div>
            ))}
          </div>
        )}

        {tab === "paper" && (
          <div className="cfg-list">
            {OUTPUTS.map((o) => (
              <div className="cfg-item" key={o.label}>
                <div className="cfg-item-k">{o.label}</div>
                <div className="cfg-item-v">{o.desc}</div>
              </div>
            ))}
          </div>
        )}

        {tab !== "paper" && (
          <button className="cfg-next" onClick={goNext}>Next →</button>
        )}
      </div>
    </div>
  );
}
