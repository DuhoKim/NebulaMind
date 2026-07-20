"use client";

import { useState, Fragment, type ReactNode } from "react";
import { STEPS, useTab, useSub, select, useLabUrlSync } from "./labTabStore";
import { FRONTIERS } from "./frontiersData";
import { itemsFor } from "./stageData";
import { SUBNAV_VIDEOS } from "./subnavVideos";
import { SCATTER_CLUSTERS, SCATTER_POINTS, SCATTER_ACTIVITY, ACTIVITY_MIN, ACTIVITY_MAX } from "./clusterScatter";
import { LANDSCAPE, GROUPS, BAND_META, BAND_ORDER, STATUS_META, STATUS_ORDER, IN_USE, type Band } from "./dataLandscape";
import { MEASUREMENTS, RESEARCH_GROUPS, VERDICT_META, SOURCE_META, DISPERSION, type Source } from "./researchCatalog";
import PipelineBoard from "./PipelineBoard";
import FlagshipStudies from "./FlagshipStudies";

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
      aria-label="120,676 papers embedded into vectors, clustered into themes, then ranked into research frontiers">
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
        <text x="88" y="176">120,676 papers</text>
        <text x="324" y="176">embed → vectors</text>
        <text x="566" y="176">clusters</text>
        <text x="795" y="176">ranked frontiers</text>
      </g>
    </svg>
  );
}

const CORPUS_YEARS = [3732, 5624, 5957, 6375, 6248, 6111, 6109, 6508, 6549, 6702, 6948, 7319, 7435, 7698, 7879, 8929, 9303, 5250];
// Composition by arXiv primary category (from ADS category keywords; 9,326 carry no category tag). n = 120,676.
const CORPUS_SPLIT: [string, number, string][] = [
  ["galaxy evolution", 54434, "#7c86ff"],
  ["cosmology", 44807, "#4ad6c4"],
  ["cross-listed", 12109, "#b98cff"],
  ["uncategorized", 9326, "#3a4560"],
];
// Top journals by paper count (ADS `pub` field).
const CORPUS_JOURNALS: [string, number][] = [
  ["MNRAS", 30590], ["ApJ", 27532], ["A&A", 16628], ["Phys. Rev. D", 11806],
  ["JCAP", 8551], ["AJ", 2416], ["ApJS", 1732], ["JHEP", 1674],
];
// Citation-count histogram over all 120,676 papers (real counts, sum = 120,676).
const CITE_HIST: [string, number][] = [
  ["0", 3673], ["1–10", 32877], ["11–50", 54652], ["51–100", 16912], ["101–500", 11769], ["0.5–1k", 580], [">1k", 213],
];
// Dataset usage — curated interest datasets (dataset-usage index over all 120,676 papers).
const CORPUS_DATASETS: [string, number][] = [
  ["ALMA", 3803], ["HST", 2396], ["Gaia", 1730], ["SDSS", 1698], ["JWST", 1418], ["IllustrisTNG", 512],
];
function SubnavVideo({ step }: { step: string }) {
  const id = SUBNAV_VIDEOS[step];
  if (!id) return null;
  return (
    <div className="subnav-video">
      <iframe src={`https://www.youtube.com/embed/${id}`} title="explainer" loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
    </div>
  );
}
function CorpusView() {
  const max = Math.max(...CORPUS_YEARS);
  const W = 900, H = 210, padX = 34, padTop = 16, baseY = H - 30;
  const bw = (W - padX * 2) / CORPUS_YEARS.length;
  return (
    <div className="corpus-view">
      <div className="corpus-stats">
        <div className="cst"><b>120,676</b><span>refereed papers</span></div>
        <div className="cst"><b>GA + CO</b><span>galaxy evolution + cosmology</span></div>
        <div className="cst"><b>2009–2026</b><span>18 years of literature</span></div>
        <div className="cst"><b>8.9M</b><span>&ldquo;cites&rdquo; links between papers</span></div>
        <div className="cst accent"><b>10×</b><span>the previous 12k corpus</span></div>
      </div>
      <div className="corpus-block">
        <div className="cch-h">Papers per year</div>
        <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label="Papers per year, 2009 to 2026, rising from ~3,700 to ~9,300">
          <defs>
            <linearGradient id="cbar" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stopColor="#7c86ff" /><stop offset="1" stopColor="#4ad6c4" />
            </linearGradient>
          </defs>
          {CORPUS_YEARS.map((c, i) => {
            const h = (baseY - padTop) * c / max, x = padX + i * bw, y = baseY - h, yr = 2009 + i;
            return (
              <g key={i}>
                <rect x={x + 2.5} y={y} width={bw - 5} height={h} rx="2.5" fill="url(#cbar)" fillOpacity={yr === 2026 ? 0.4 : 0.92} />
                <text x={x + bw / 2} y={baseY + 16} fontFamily="ui-monospace,monospace" fontSize="10" fill="#9aa3b8" textAnchor="middle">{`'${String(yr).slice(2)}`}</text>
              </g>
            );
          })}
          <text x={padX} y={padTop - 3} fontFamily="ui-monospace,monospace" fontSize="10" fill="#9aa3b8">9.3k/yr</text>
        </svg>
        <p className="cch-note">Steady, rising coverage across 18 years — no gap, no cherry-picking. 2026 (faded) is the year still in progress.</p>
      </div>
      <div className="corpus-block">
        <div className="cch-h">Composition · galaxy evolution vs cosmology</div>
        <div className="corpus-split">
          {CORPUS_SPLIT.map(([name, n, c]) => (
            <i key={name} style={{ width: `${(n / 120676) * 100}%`, background: c, color: name === "uncategorized" ? "var(--lab-soft)" : "#0a0d17" }}>
              {n / 120676 > 0.09 ? `${Math.round((n / 120676) * 100)}%` : ""}
            </i>
          ))}
        </div>
        <div className="corpus-legend">
          {CORPUS_SPLIT.map(([name, n, c]) => (
            <span key={name}><i style={{ background: c }} />{name} · {n.toLocaleString()}</span>
          ))}
        </div>
        <p className="cch-note">Two arXiv fields, split by primary category: <b>galaxy evolution</b> (astro-ph.GA) and <b>cosmology</b> (astro-ph.CO), with 12,109 cross-listed in both. The 9,326 &ldquo;uncategorized&rdquo; are in-scope by the pull query but carry no category tag to sort on.</p>
      </div>
      <div className="corpus-block">
        <div className="cch-h">How far the papers reach · citations</div>
        <div className="corpus-stats">
          <div className="cst"><b>21</b><span>median citations / paper</span></div>
          <div className="cst"><b>47</b><span>mean citations / paper</span></div>
          <div className="cst"><b>12,562</b><span>papers cited &gt;100&times;</span></div>
          <div className="cst"><b>213</b><span>papers cited &gt;1,000&times;</span></div>
          <div className="cst accent"><b>19,137</b><span>the single most-cited</span></div>
        </div>
        {(() => {
          const W = 900, H = 200, padX = 26, padTop = 24, baseY = H - 30;
          const bw = (W - padX * 2) / CITE_HIST.length;
          const max = Math.max(...CITE_HIST.map((c) => c[1]));
          return (
            <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label="Distribution of citation counts across the corpus" style={{ width: "100%", height: "auto", display: "block", marginTop: ".2rem" }}>
              <defs><linearGradient id="chbar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#7c86ff" /><stop offset="1" stopColor="#4ad6c4" /></linearGradient></defs>
              {CITE_HIST.map(([lab, n], i) => {
                const h = (baseY - padTop) * n / max, x = padX + i * bw, y = baseY - h;
                return (
                  <g key={lab}>
                    <rect x={x + 5} y={y} width={bw - 10} height={h} rx="3" fill="url(#chbar)" fillOpacity="0.92" />
                    <text x={x + bw / 2} y={y - 5} fontFamily="ui-monospace,monospace" fontSize="12" fill="#9aa3b8" textAnchor="middle">{n.toLocaleString()}</text>
                    <text x={x + bw / 2} y={baseY + 17} fontFamily="ui-monospace,monospace" fontSize="12" fill="#9aa3b8" textAnchor="middle">{lab}</text>
                  </g>
                );
              })}
            </svg>
          );
        })()}
        <p className="cch-note">A long-tailed field: most papers sit in the 11–50 band (median 21), but the top <b>213 clear a thousand citations</b> each — led by <b>Planck 2018 VI</b> at 19,137. Those anchor the retrieval.</p>
      </div>
      <div className="corpus-block">
        <div className="cch-h">Where it&rsquo;s published · top journals</div>
        <div className="embed-lb">
          {CORPUS_JOURNALS.map(([name, n]) => (
            <div className="elb-row" key={name}>
              <span className="elb-name">{name}</span>
              <span className="elb-bar"><i style={{ width: `${(n / CORPUS_JOURNALS[0][1]) * 100}%` }} /></span>
              <span className="elb-score">{(n / 1000).toFixed(1)}k</span>
            </div>
          ))}
        </div>
        <p className="cch-note">MNRAS, ApJ and A&amp;A carry the galaxy-evolution literature; Phys. Rev. D and JCAP carry the cosmology side — the split shows in the mastheads.</p>
      </div>
      <div className="corpus-block">
        <div className="cch-h">What the papers use · datasets</div>
        <div className="embed-lb">
          {CORPUS_DATASETS.map(([name, n]) => (
            <div className={`elb-row${["SDSS", "JWST", "IllustrisTNG"].includes(name) ? " chosen" : ""}`} key={name}>
              <span className="elb-name">{name}{["SDSS", "JWST", "IllustrisTNG"].includes(name) ? " ✓" : ""}</span>
              <span className="elb-bar"><i style={{ width: `${(n / CORPUS_DATASETS[0][1]) * 100}%` }} /></span>
              <span className="elb-score">{n.toLocaleString()}</span>
            </div>
          ))}
        </div>
        <p className="cch-note">Papers that name a specific dataset — the study itself runs on <b>SDSS</b>, <b>JWST</b> and <b>IllustrisTNG</b> (✓), so the corpus knows exactly which prior work used the same data. (Broader archive links: SIMBAD 64k, NED 31k, MAST 12k.)</p>
      </div>
      <div className="corpus-block">
        <div className="cch-h">How the papers connect · &ldquo;this one cites that one&rdquo;</div>
        <div className="corpus-stats">
          <div className="cst"><b>8.87M</b><span>&ldquo;cites&rdquo; links in total</span></div>
          <div className="cst"><b>73</b><span>references in a typical paper</span></div>
          <div className="cst accent"><b>3.89M</b><span>links between two papers we hold</span></div>
          <div className="cst"><b>97%</b><span>of papers link to another</span></div>
        </div>
        <p className="cch-note">Every paper&rsquo;s bibliography is traced to the paper it points at — 8.87M &ldquo;this paper cites that one&rdquo; links in all. <b>3.89M</b> of them connect two papers we already hold, so the whole library is stitched together; later steps follow these links to place a new result in its lineage.</p>
      </div>
      <div className="corpus-block">
        <div className="cch-h">Full-text deep layer · coverage</div>
        <div className="corpus-split">
          <i style={{ width: "95.9%", background: "#2b3350", color: "var(--lab-soft)" }}>abstract-only · 95.9%</i>
          <i style={{ width: "4.1%", background: "var(--lab-accent2)" }}></i>
        </div>
        <div className="corpus-legend">
          <span><i style={{ background: "#2b3350" }} />abstract-level · all 120,676</span>
          <span><i style={{ background: "var(--lab-accent2)" }} />full-text deep · 4,898 top-cited</span>
        </div>
        <p className="cch-note">Every paper is searchable by abstract; the <b>top ~5,000 most-cited</b> are also pulled in full — prose + tables — as the deep layer the gates read for real numbers. The rest are fetched on demand. HTML-first from arXiv/ar5iv, no paywalled PDFs.</p>
      </div>
    </div>
  );
}

// Full leaderboard from the citation-retrieval bake-off (leaderboard.json). recall@10; chosen = qwen3-embedding-4b.
const EMBED_LB: [string, number, boolean][] = [
  ["qwen3-embedding-8b", 0.704, false],
  ["qwen3-embedding-4b", 0.691, true],
  ["qwen3-embedding-0.6b", 0.639, false],
  ["mxbai-embed-large", 0.610, false],
  ["snowflake-arctic-v2", 0.604, false],
  ["nomic-embed (previous)", 0.589, false],
  ["bge-m3", 0.562, false],
  ["scincl", 0.499, false],
  ["specter2-base", 0.328, false],
];
// Live nearest-neighbor demo — top matches by cosine over the real 120,676-vector index (computed from emb_qwen4b.f32).
const NN_DEMO: { seed: string; meta: string; nbrs: [number, string][] }[] = [
  { seed: "Planck 2018 results VI · Cosmological parameters", meta: "Planck Collaboration · 2020 · cosmology anchor",
    nbrs: [
      [0.923, "Planck 2015 results XIII · Cosmological parameters — 2016"],
      [0.885, "Planck 2013 results XVI · Cosmological parameters — 2014"],
      [0.847, "Planck 2018 results I · Overview & the cosmological legacy — 2020"],
      [0.826, "Planck 2018 results VIII · Gravitational lensing — 2020"],
      [0.823, "Beyond six parameters: extending ΛCDM · Di Valentino — 2015"],
    ] },
  { seed: "First results from IllustrisTNG · matter & galaxy clustering", meta: "Springel · 2018 · simulation methods",
    nbrs: [
      [0.822, "MillenniumTNG · large-scale clustering of galaxies — 2023"],
      [0.822, "Impact of baryonic processes on galaxy correlations · van Daalen — 2014"],
      [0.817, "IllustrisTNG · stellar-mass content of groups & clusters — 2018"],
      [0.792, "Introducing the Illustris Project · Vogelsberger — 2014"],
      [0.790, "Baryonic feedback across halo mass · matter power spectrum — 2026"],
    ] },
];
function SimilarMap() {
  const bg = Array.from({ length: 46 }, (_, i) => [8 + sd(i * 3 + 1) * 84, 6 + sd(i * 7 + 2) * 50] as [number, number]);
  return (
    <svg viewBox="0 0 100 64" className="simmap" role="img" aria-label="Similar papers land close, different topics land far">
      {bg.map(([x, y], i) => <circle key={i} cx={x} cy={y} r="0.85" fill="#3a4560" fillOpacity="0.5" />)}
      <line x1="61" y1="24" x2="68" y2="27.5" stroke="#4ad6c4" strokeWidth="0.7" />
      <circle cx="61" cy="24" r="2" fill="#4ad6c4" />
      <circle cx="68" cy="27.5" r="2" fill="#4ad6c4" />
      <text x="48" y="18" fontSize="3.4" fill="#4ad6c4" fontFamily="ui-monospace,monospace">Planck ×2 · same physics</text>
      <circle cx="19" cy="50" r="2" fill="#f47272" />
      <text x="10" y="58" fontSize="3.4" fill="#f47272" fontFamily="ui-monospace,monospace">radio-burst paper · far off</text>
    </svg>
  );
}
function EmbeddingView() {
  const max = 0.72;
  return (
    <div className="corpus-view">
      <div className="corpus-stats">
        <div className="cst"><b>a map of meaning</b><span>every paper is a point</span></div>
        <div className="cst"><b>120,676</b><span>papers placed on it</span></div>
        <div className="cst"><b>same physics → nearby</b><span>similar science sits together</span></div>
        <div className="cst accent"><b>~7 in 10</b><span>top-10 finds the right related paper</span></div>
      </div>
      <div className="corpus-block">
        <div className="cch-h">The idea — similar papers land close</div>
        <p className="cch-note">Keyword search misses a paper that says the same thing in different words. So instead we turn each paper into a <b>point on a map of meaning</b>: papers about the same physics end up right next to each other, even with no shared words. &ldquo;Find related work&rdquo; becomes &ldquo;find the nearest points.&rdquo;</p>
        <SimilarMap />
        <p className="cch-note">Two Planck cosmology papers land almost on top of each other; a fast-radio-burst paper sits far across the map. Nothing was placed by hand — the <b>meaning</b> did it.</p>
      </div>
      <div className="corpus-block">
        <div className="cch-h">Does it really work? · ask for a paper&rsquo;s neighbors</div>
        <p className="cch-note">A live test on the real map: take a landmark paper and ask for its closest neighbors. The right related papers come back — across different years and author teams, nothing hand-picked. <span style={{ opacity: .75 }}>(The number is how close, 1.0 = right on top.)</span></p>
        {NN_DEMO.map((d) => (
          <div className="nn-demo" key={d.seed}>
            <div className="nn-seed"><b>{d.seed}</b><span>{d.meta}</span></div>
            <div className="nn-list">
              {d.nbrs.map(([cos, ttl]) => (
                <div className="nn-row" key={ttl}>
                  <span className="nn-cos">{cos.toFixed(2)}</span>
                  <span className="nn-bar"><i style={{ width: `${Math.max(8, ((cos - 0.7) / 0.3) * 100)}%` }} /></span>
                  <span className="nn-ttl">{ttl}</span>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
      <div className="corpus-block">
        <div className="cch-h">Two maps · whole papers, and their exact passages</div>
        <div className="two-layer">
          <div className="tl-col">
            <div className="tl-h">Every paper</div>
            <div className="tl-n">120,676</div>
            <p>One point per paper (the map above). Finds the <b>related work</b> a study should read and cite.</p>
          </div>
          <div className="tl-col accent">
            <div className="tl-h">Exact passages</div>
            <div className="tl-n">~4,900 top-cited</div>
            <p>Their full text is split into passages, each mapped too — so later steps can pull the <b>exact sentence</b> that backs a claim, not just the paper.</p>
          </div>
        </div>
      </div>
      <div className="corpus-block">
        <div className="cch-h">How it&rsquo;s actually done</div>
        <p className="cch-note">The map-maker is an <b>&ldquo;embedding&rdquo; model</b> (qwen3-embedding-4b) that turns a paper into a list of 2,560 numbers fixing its position. We chose it with a bake-off: <b>9 candidate models</b> were graded on whether a paper&rsquo;s <i>real citations</i> land among its nearest neighbors — how often the right related papers make the top 10 (&ldquo;recall@10&rdquo;). It won the accuracy-for-cost trade-off, placed all 120,676 papers in <b>5.3 hours</b>, and the finished map is a single 1.24 GB file that searches in ~1.8 seconds.</p>
        <div className="embed-lb">
          {EMBED_LB.map(([name, r, chosen]) => (
            <div className={`elb-row${chosen ? " chosen" : ""}`} key={name}>
              <span className="elb-name">{name}{chosen ? " ✓" : ""}</span>
              <span className="elb-bar"><i style={{ width: `${(r / max) * 100}%` }} /></span>
              <span className="elb-score">{r.toFixed(3)}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// Top clusters by frontier score — real c-TF-IDF term lists, sizes, and scores from frontier_map_v2.json.
const CLUSTER_TOPICS: [string, string, number, number][] = [
  ["JWST high-z galaxy formation & metallicity", "formation · metallicity · jwst · redshift · emission", 1296, 0.96],
  ["Dark energy & the Hubble tension", "dark energy · ΛCDM · EDE · BAO · tension", 1114, 0.75],
  ["Galactic chemical evolution", "gaia · chemical · apogee · spectra · abundances", 656, 0.63],
  ["Electroweak phase transitions & GWs", "electroweak · phase transition · bubble · higgs", 470, 0.59],
  ["Supermassive black-hole accretion", "black hole · accretion · supermassive · smbh", 960, 0.59],
  ["Fast radio bursts", "frb · radio · fast · bursts · dispersion", 437, 0.58],
  ["Reionization & the intergalactic medium", "reionization · igm · lyman-α forest · redshift", 541, 0.53],
  ["Weak lensing & large-scale structure", "lensing · power spectrum · survey · bias", 4253, 0.52],
  ["Lyman-continuum escape (LAEs)", "laes · lyc escape · lyman-α · emission · fraction", 892, 0.52],
  ["Fuzzy / ultralight dark matter", "fdm · soliton · sfdm · ultralight · fuzzy", 440, 0.51],
];
const SCATTER_COLS = ["#7c86ff", "#4ad6c4", "#e0a458", "#f47272", "#c084fc", "#38bdf8", "#facc15", "#fb7185", "#34d399", "#a3e635"];
function ClusterScatter() {
  const cmap = new Map<number, string>(SCATTER_CLUSTERS.map(([id], i) => [id, SCATTER_COLS[i % SCATTER_COLS.length]]));
  return (
    <div className="corpus-block">
      <div className="cch-h">The map — 120k papers, self-organized</div>
      <svg className="scatter" viewBox="0 0 100 100" role="img" aria-label="2D UMAP scatter of the corpus, colored by cluster">
        {SCATTER_POINTS.map(([x, y, cid], i) => {
          const c = cmap.get(cid);
          return <circle key={i} cx={x} cy={100 - y} r={c ? 0.75 : 0.55} fill={c || "#39435f"} fillOpacity={c ? 0.9 : 0.32} />;
        })}
      </svg>
      <div className="scatter-legend">
        {SCATTER_CLUSTERS.map(([id, label], i) => (
          <span key={id}><i style={{ background: SCATTER_COLS[i] }} />{label}</span>
        ))}
        <span><i style={{ background: "#39435f" }} />other + noise</span>
      </div>
      <p className="cch-note">A 2-D UMAP of a representative sample. The top-10 frontiers fall out as <b>distinct islands</b> — nobody drew the boundaries; the grey haze is the 43% the algorithm left unclustered rather than forcing into a theme.</p>
    </div>
  );
}
function ClusteringView() {
  return (
    <div className="corpus-view">
      <div className="corpus-stats">
        <div className="cst"><b>57</b><span>topics that formed themselves</span></div>
        <div className="cst"><b>68,772</b><span>papers that fell into a topic</span></div>
        <div className="cst"><b>43%</b><span>too scattered to group — left out</span></div>
        <div className="cst"><b>auto-named</b><span>from each group&rsquo;s distinctive words</span></div>
        <div className="cst accent"><b>JWST high-z #1</b><span>the most actively-cited topic</span></div>
      </div>
      <div className="corpus-block">
        <div className="cch-h">The map draws its own topics</div>
        <p className="cch-note">Nobody set a number of topics or drew any boundaries. Left alone on the map from the last step, <b>nearby papers fall into natural clumps</b> — the computer finds the clumps and names each one from the words that make it distinctive. Below is the real map, colored by the topics it found:</p>
      </div>
      <ClusterScatter />
      <div className="corpus-block">
        <div className="cch-h">The topics that emerged · most-cited first</div>
        <div className="embed-lb frontiers">
          {CLUSTER_TOPICS.map(([label, kws, size], i) => (
            <div className={`clu-row${i === 0 ? " top" : ""}`} key={label}>
              <span className="clu-label"><b>{label}</b><span className="clu-kw">{kws} · {size.toLocaleString()} papers</span></span>
              <span className="elb-bar"><i style={{ width: `${CLUSTER_TOPICS[i][3] * 100}%` }} /></span>
            </div>
          ))}
        </div>
        <p className="cch-note">These are the field&rsquo;s own topics, read straight out of the literature — the bar is how actively each is being cited. The top <b>galaxy-evolution</b> ones become the research questions the pipeline works on.</p>
      </div>
      <div className="corpus-block">
        <div className="cch-h">How it&rsquo;s actually done</div>
        <p className="cch-note">The map of 2,560 numbers per paper is first flattened to a 2-D picture (<b>UMAP</b>), then a clustering method finds the dense clumps and leaves loners unassigned (<b>HDBSCAN</b>, min-cluster-size 400), and each topic is auto-labeled from its most distinctive words (<b>c-TF-IDF</b>). No target count is set — 57 is what the data gave; topic sizes run 414 → 8,913 papers, and the 43% too scattered to belong anywhere (51,904 papers) are left out rather than forced.</p>
      </div>
    </div>
  );
}

// recent_cites_per_paper per cluster (2023+ citation edges into the cluster ÷ its size), from frontier_map_v2.json.
const OVERLAY_ACTIVE: [string, number][] = [
  ["JWST high-z galaxy formation", 39.2],
  ["Dark energy / Hubble tension", 27.1],
  ["Galactic chemical evolution", 24.8],
  ["Supermassive black-hole accretion", 24.7],
  ["Lyman-continuum escape (LAEs)", 21.9],
  ["Reionization & the IGM", 20.7],
  ["Weak lensing & large-scale structure", 18.1],
  ["Electroweak phase transitions", 17.0],
  ["Fuzzy / ultralight dark matter", 15.6],
  ["Fast radio bursts", 13.7],
  ["…settled floor: pulsars & MSPs", 3.0],
];
// Heat color for the activity overlay: cool grey-blue (settled) → teal → yellow → hot red (active).
function heatColor(t: number): string {
  const stops: [number, [number, number, number]][] = [
    [0, [58, 69, 96]], [0.4, [74, 214, 196]], [0.72, [250, 204, 21]], [1, [251, 90, 90]],
  ];
  t = Math.max(0, Math.min(1, t));
  for (let i = 1; i < stops.length; i++) {
    if (t <= stops[i][0]) {
      const [t0, c0] = stops[i - 1];
      const [t1, c1] = stops[i];
      const f = (t - t0) / (t1 - t0);
      const c = c0.map((v, k) => Math.round(v + (c1[k] - v) * f));
      return `rgb(${c[0]},${c[1]},${c[2]})`;
    }
  }
  return "rgb(251,90,90)";
}
function actNorm(a: number): number {
  return Math.pow((a - ACTIVITY_MIN) / (ACTIVITY_MAX - ACTIVITY_MIN), 0.6);
}
function ActivityScatter() {
  return (
    <div className="corpus-block">
      <div className="cch-h">The same map — now lit by how active each theme is</div>
      <svg className="scatter" viewBox="0 0 100 100" role="img" aria-label="Cluster map heat-colored by recent citation activity">
        {SCATTER_POINTS.map(([x, y, cid], i) => {
          const a = SCATTER_ACTIVITY[cid];
          const noise = a === undefined;
          const t = noise ? 0 : actNorm(a);
          return <circle key={i} cx={x} cy={100 - y} r={noise ? 0.5 : 0.7 + t * 0.7} fill={noise ? "#222a3a" : heatColor(t)} fillOpacity={noise ? 0.22 : 0.92} />;
        })}
      </svg>
      <div className="heat-scale">
        <span>❄ settled (barely cited now)</span>
        <div className="heat-bar" />
        <span>still argued about 🔥</span>
        <span className="heat-grey"><i />not in a topic</span>
      </div>
      <p className="cch-note">Exactly the <b>same 57-theme map</b> as the previous step — but recolored: each theme now glows by its <b>recent citations per paper</b>. A handful burn hot (the field is still piling citations on); most sit cool and settled. The single hottest island is <b>JWST high-z galaxy formation</b>.</p>
    </div>
  );
}
function OverlayView() {
  const max = 40;
  return (
    <div className="corpus-view">
      <div className="corpus-stats">
        <div className="cst"><b>2.30M</b><span>citation edges into clustered papers</span></div>
        <div className="cst"><b>911k</b><span>from recent (2023+) work</span></div>
        <div className="cst"><b>39 → 3</b><span>recent cites/paper · active → settled</span></div>
        <div className="cst accent"><b>data-driven</b><span>no hand-counted debates</span></div>
      </div>
      <div className="corpus-block">
        <div className="cch-h">The idea in one line</div>
        <div className="ov-flow">
          <span><b>1</b>take the 57-theme map</span><em>→</em>
          <span><b>2</b>count each theme&rsquo;s citations from 2023+ papers</span><em>→</em>
          <span><b>3</b>÷ its size = how hot it still runs</span>
        </div>
        <p className="cch-note">Still being cited = a live frontier; stopped being cited = settled. An objective signal, replacing debates hand-counted from review papers.</p>
      </div>
      <ActivityScatter />
      <div className="corpus-block">
        <div className="cch-h">Activity spectrum — recent citations per paper</div>
        <div className="embed-lb">
          {OVERLAY_ACTIVE.map(([label, v], i) => (
            <div className={`clu-row${i === 0 ? " top" : ""}`} key={label}>
              <span className="clu-label"><b>{label}</b></span>
              <span className="elb-bar"><i style={{ width: `${(v / max) * 100}%`, background: heatColor(actNorm(v)) }} /></span>
              <span className="elb-score">{v.toFixed(1)}</span>
            </div>
          ))}
        </div>
        <p className="cch-note">The same numbers that color the map, as a ranked bar — a <b>13×</b> spread from JWST high-z (39.2) to the settled floor (pulsars, 3.0). The hot themes are exactly the ones that rise in the next step.</p>
      </div>
    </div>
  );
}

// Real ranked frontiers from frontier_map_v2.json: score = frontier_score_cite; act = recent_cites_per_paper; grow = recent_frac (2023+ share). tag = dominant arXiv category.
// v1 frontier ranking (score_v1) — galaxy-evolution (in-scope) themes, from frontier_map_v3.json / rank_frontiers_v3.py.
// score = sat(activity) · tractability_veto · (0.6·tension + 0.4·growth); tension = strict-disagreement rate.
// v2.3 = measurement-dispersion with STELLAR MASSES mined from full-text tables. PDG scale factor S within same-epoch (z × mass × calibration) cells. dispersion_v23.json.
const QUANTITY_DISP: { q: string; N: number; S: number; Szm: number; verdict: string }[] = [
  { q: "Eddington ratio · AGN accretion", N: 37, S: 5.71, Szm: 3.53, verdict: "contested" },
  { q: "LyC escape fraction · f_esc", N: 64, S: 3.87, Szm: 3.20, verdict: "contested" },
  { q: "Quiescent fraction", N: 57, S: 3.56, Szm: 3.32, verdict: "contested" },
  { q: "Main-sequence slope · SFR–M✱", N: 23, S: 3.01, Szm: 3.10, verdict: "contested" },
  { q: "Cosmic SFR density · ψ(z)", N: 46, S: 3.78, Szm: 2.85, verdict: "contested" },
  { q: "Gas metallicity · 12+log(O/H)", N: 785, S: 7.76, Szm: 2.65, verdict: "mzr-fixed" },
  { q: "UV-LF faint-end slope · α", N: 30, S: 3.18, Szm: 1.42, verdict: "z-driven" },
  { q: "Stellar mass function · M✱", N: 10, S: 1.22, Szm: 1.06, verdict: "consistent" },
];
// v2.3 frontier ranking — ranked by measurement disagreement (mass-controlled). plain = one-line what's disputed.
const RANK_TOPICS: { label: string; score: number; plain: string; measured: string }[] = [
  { label: "JWST high-z galaxy formation", score: 0.60, plain: "How fast did the first galaxies grow and enrich? Early-JWST numbers clash.", measured: "star-formation density · metallicity at z>7" },
  { label: "Black-hole accretion", score: 0.56, plain: "How fast do supermassive black holes feed? Reported rates disagree.", measured: "Eddington ratio" },
  { label: "Escaping ionizing light (LAEs)", score: 0.48, plain: "How much ionizing radiation leaks out of galaxies? Estimates span a wide range.", measured: "escape fraction" },
  { label: "Quenching of star formation", score: 0.42, plain: "When and why do galaxies stop forming stars? The counts don't line up.", measured: "quiescent fraction · main sequence" },
  { label: "Dust-hidden star formation (SMGs)", score: 0.41, plain: "How much star formation is hidden behind dust? Measurements clash.", measured: "SFR density · main sequence" },
  { label: "AGN in X-rays", score: 0.37, plain: "Black-hole growth measured in X-rays — studies still disagree.", measured: "Eddington ratio" },
];
function SettledVsContested() {
  const settled = [196, 214, 232, 206, 246];
  const contested = [70, 150, 232, 314, 396];
  const bar = (x: number, y: number, eb: number, c: string, i: number) => (
    <g key={i}>
      <line x1={x - eb} y1={y} x2={x + eb} y2={y} stroke={c} strokeWidth="2" />
      <line x1={x - eb} y1={y - 4} x2={x - eb} y2={y + 4} stroke={c} strokeWidth="2" />
      <line x1={x + eb} y1={y - 4} x2={x + eb} y2={y + 4} stroke={c} strokeWidth="2" />
      <circle cx={x} cy={y} r="4" fill={c} />
    </g>
  );
  return (
    <svg viewBox="0 0 460 150" className="svc" role="img" aria-label="Settled versus contested measurements">
      <text x="8" y="19" fontFamily="ui-monospace,monospace" fontSize="12.5" fill="#9aa3b8">measurements <tspan fill="#4ad6c4" fontWeight="bold">agree</tspan> → a settled question</text>
      {settled.map((x, i) => bar(x, 47, 18, "#4ad6c4", i))}
      <text x="8" y="99" fontFamily="ui-monospace,monospace" fontSize="12.5" fill="#9aa3b8">they <tspan fill="#f47272" fontWeight="bold">disagree past their error bars</tspan> → contested</text>
      {contested.map((x, i) => bar(x, 127, 16, "#f47272", i))}
    </svg>
  );
}
function RankingView() {
  const smax = RANK_TOPICS[0].score;
  const Smax = 6.5;
  return (
    <div className="corpus-view">
      <div className="corpus-stats">
        <div className="cst"><b>disagreement</b><span>what we rank by — not popularity</span></div>
        <div className="cst"><b>same z &amp; mass</b><span>compared like-with-like</span></div>
        <div className="cst"><b>785 measurements</b><span>mined from paper tables</span></div>
        <div className="cst accent"><b>JWST high-z</b><span>#1 · most contested</span></div>
      </div>
      <div className="corpus-block">
        <div className="cch-h">How the ranking works — in one idea</div>
        <p className="cch-note">A good question to research is one <b>the field can&rsquo;t agree on yet</b> — and that we hold the data to settle. So instead of ranking topics by how popular they are, we rank them by <b>disagreement</b>. For each topic we gather independent measurements of the <i>same</i> number — at the same redshift and galaxy mass, so it&rsquo;s apples-to-apples — and simply ask: <b>do they agree?</b></p>
        <SettledVsContested />
      </div>
      <div className="corpus-block">
        <div className="cch-h">What the score is built from</div>
        <p className="cch-note">The ranking isn&rsquo;t one mysterious number — it&rsquo;s <b>disagreement</b>, kept honest by two guards. Multiply the three; miss any one and the topic drops out.</p>
        <div className="ing">
          <div className="ing-card"><p className="ing-k">the signal</p><b>How much do studies disagree?</b><span>the main ingredient — real, like-for-like clashing measurements</span></div>
          <div className="ing-x">×</div>
          <div className="ing-card g"><p className="ing-k">guard · testable</p><b>Do we hold the data?</b><span>if no telescope of ours can move it, it can&rsquo;t win</span></div>
          <div className="ing-x">×</div>
          <div className="ing-card f"><p className="ing-k">guard · alive</p><b>Is anyone still working on it?</b><span>a dead topic with no recent work is skipped</span></div>
        </div>
      </div>
      <div className="corpus-block">
        <div className="cch-h">The contested frontiers — where the field is unsettled</div>
        <div className="embed-lb frontiers">
          {RANK_TOPICS.map(({ label, score, plain, measured }, i) => (
            <div className={`clu-row${i === 0 ? " top" : ""}`} key={label}>
              <span className="clu-label"><b>{i + 1}. {label}</b><span className="clu-kw">{plain} <span style={{ opacity: .6 }}>· from: {measured}</span></span></span>
              <span className="elb-bar"><i style={{ width: `${(score / smax) * 100}%`, background: "var(--lab-accent2)" }} /></span>
            </div>
          ))}
        </div>
        <p className="cch-note">The bar shows how much the field disagrees — no cryptic score, just the level and the reason. The top galaxy-evolution frontiers become the studies the pipeline runs; <b>JWST high-z</b> leads, with a genuine early-universe disagreement over both how fast galaxies formed and how metal-rich they already were.</p>
      </div>
      <div className="corpus-block">
        <div className="cch-h">The measurements behind it · does the field agree?</div>
        <p className="cch-note">Each row is one measurable quantity. We score the scatter of independent measurements against their own error bars (the <b>PDG scale factor S</b>: <b>S ≈ 1</b> = they agree, <b>S ≫ 1</b> = they clash), after matching redshift and mass so we don&rsquo;t compare a dwarf to a giant.</p>
        <div className="embed-lb">
          {QUANTITY_DISP.map(({ q, N, S, Szm, verdict }) => {
            const col = verdict === "contested" || verdict === "mzr-fixed" ? heatColor(Math.min(1, (Szm - 1) / 3))
              : verdict === "z-driven" ? "#e0a458" : verdict === "mass-starved" ? "#b98cff" : "#5b6486";
            const kw = verdict === "contested" ? `contested — measurements clash (S ${Szm.toFixed(1)})`
              : verdict === "mzr-fixed" ? `contested, once real masses control for the mass–metallicity relation (S ${S.toFixed(1)} → ${Szm.toFixed(1)}); sharpest at z > 7`
              : verdict === "z-driven" ? `looked contested, but it was just cosmic evolution (S ${S.toFixed(1)} → ${Szm.toFixed(1)})`
              : verdict === "mass-starved" ? `S stays high but the masses are missing — unresolved`
              : `the field agrees (S ≈ 1)`;
            return (
              <div className="clu-row" key={q}>
                <span className="clu-label"><b>{q}</b><span className="clu-kw">{kw}</span></span>
                <span className="elb-bar"><i style={{ width: `${Math.min(100, (Szm / Smax) * 100)}%`, background: col }} /></span>
                <span className="elb-score">S {Szm.toFixed(1)}</span>
              </div>
            );
          })}
        </div>
        <p className="cch-note">Getting this honest took five passes, each removing one way to be fooled: counting <b>words</b> → mistaking <b>popularity</b> for disagreement → mistaking cosmic <b>evolution</b> for a fight → mistaking the <b>mass</b> sequence for one → and finally mining <b>stellar masses from full-text tables</b> to test gas metallicity properly. That last pass deflated a false signal <i>and</i> found a real one: an early-universe (z&gt;7) metallicity disagreement, right where JWST is looking.</p>
      </div>
    </div>
  );
}

const METHOD_STEPS = [
  "120,676 abstracts · astro-ph.GA + CO · 2009–2026 · NASA ADS",
  "qwen3-embedding-4b → cluster → rank",
  "overlay open debates + unknowns from landmark reviews",
  "rank = open-Q density × growth",
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

// Piecewise redshift axis — extra room at low z, extends to z=15 with an off-scale
// tail for the reionization-era surveys (JWST, ELT, SKA HI).
function zx(z: number): number {
  if (z <= 1) return 70 + z * 196;
  if (z <= 3) return 266 + ((z - 1) / 2) * 204;
  if (z <= 6) return 470 + ((z - 3) / 3) * 180;
  if (z <= 10) return 650 + ((z - 6) / 4) * 140;
  if (z <= 15) return 790 + ((z - 10) / 5) * 76;
  return 866;
}

function CoverageMap() {
  const rowH = 44;
  const top = 22;
  const height = top + BAND_ORDER.length * rowH + 46;
  const axisY = top + BAND_ORDER.length * rowH + 6;
  const ticks = [0, 1, 3, 6, 10, 15];
  return (
    <svg className="dv-cov" viewBox={`0 0 900 ${height}`} role="img"
      aria-label="Wavelength by redshift coverage of 44 public galaxy-evolution surveys">
      {/* redshift gridlines */}
      {ticks.map((z) => (
        <line key={`g${z}`} x1={zx(z)} y1={top - 6} x2={zx(z)} y2={axisY} stroke="#1a2033" strokeWidth="1" />
      ))}
      {BAND_ORDER.map((band, i) => {
        const rows = LANDSCAPE.filter((s) => s.band === band);
        if (rows.length === 0) return null;
        const uMin = Math.min(...rows.map((s) => s.z0));
        const uMax = Math.max(...rows.map((s) => s.z1));
        const meta = BAND_META[band];
        const yc = top + i * rowH + rowH / 2;
        const inUse = rows.find((s) => s.inUse);
        return (
          <g key={band}>
            <text x="8" y={yc + 3.5} fontSize="11" fill="#c7cede" fontFamily="ui-monospace,monospace">
              {meta.label}<tspan fill="#6b7386"> ·{rows.length}</tspan>
            </text>
            {/* coverage envelope: band reaches this far in redshift */}
            <rect x={zx(uMin)} y={yc - 11} width={Math.max(3, zx(uMax) - zx(uMin))} height="22" rx="5"
              fill={meta.color} fillOpacity="0.12" stroke={meta.color} strokeOpacity="0.32" strokeWidth="1" />
            {/* one reach-dot per survey at its high-z end */}
            {rows.filter((s) => !s.inUse).map((s) => (
              <circle key={s.name} cx={zx(s.z1)} cy={yc} r="2.3" fill={meta.color} fillOpacity="0.7" />
            ))}
            {/* highlighted in-use bar */}
            {inUse && (
              <g>
                <rect x={zx(inUse.z0)} y={yc - 5} width={Math.max(6, zx(inUse.z1) - zx(inUse.z0))} height="10" rx="5"
                  fill={meta.color} stroke="#e8ecf5" strokeWidth="1.2" />
                {inUse.arrow && <path d={`M${zx(inUse.z1) + 2} ${yc} l7 -4 v8 z`} fill="#e8ecf5" />}
                <text x={zx(inUse.z0) + 1} y={yc - 9} fontSize="10" fontWeight="700" fill={meta.color}
                  fontFamily="ui-monospace,monospace">★ {inUse.name}</text>
              </g>
            )}
          </g>
        );
      })}
      {/* redshift axis */}
      <line x1="70" y1={axisY} x2="866" y2={axisY} stroke="#242a3d" strokeWidth="1.5" />
      {ticks.map((z) => (
        <text key={`t${z}`} x={zx(z)} y={axisY + 16} fontSize="10" fill="#9aa3b8" textAnchor="middle"
          fontFamily="ui-monospace,monospace">z={z}{z === 15 ? "+" : ""}</text>
      ))}
      <text x="468" y={axisY + 34} fontSize="10" fill="#6b7386" textAnchor="middle">
        redshift → younger, farther universe →
      </text>
    </svg>
  );
}

function DataView() {
  const total = LANDSCAPE.length;
  const bandCounts = BAND_ORDER.map((b) => ({ b, n: LANDSCAPE.filter((s) => s.band === b).length }))
    .sort((a, z) => z.n - a.n);
  const maxBand = Math.max(...bandCounts.map((x) => x.n));
  const statusCounts = STATUS_ORDER.map((st) => ({ st, n: LANDSCAPE.filter((s) => s.status === st).length }));
  return (
    <div className="dv">
      <p className="dv-lead">
        Galaxy evolution is a <b>then-vs-now</b> science: to see how galaxies grew, you compare them across
        cosmic time — and that takes surveys spanning redshift, wavelength, and physics. NebulaMind pulls from
        and validates just <b>four sources today</b>. Everything below is the <b>wider public-data landscape</b> the
        field draws on and that we could add next — a map of the open sky, not a claim that we already mine it.
      </p>

      {/* What we use now */}
      <div className="corpus-block">
        <p className="cch-h">What the pipeline uses now — 4 of {total}</p>
        <div className="dv-meter"><i style={{ width: `${(4 / total) * 100}%` }} /></div>
        <div className="dv-chips">
          {IN_USE.map((s) => {
            const color = s.band === "sim" ? "#7c86ff" : BAND_META[s.band as Band].color;
            const sim = s.band === "sim";
            return (
              <div className={`dv-chip${sim ? " sim" : ""}`} key={s.name} style={{ borderLeftColor: color }}>
                <div className="dv-chip-h"><b>{s.name}</b><span>{s.z}</span></div>
                <p>{s.role}</p>
              </div>
            );
          })}
        </div>
        <p className="cch-note">
          Three observed sky surveys plus one cosmological <b style={{ color: "#8a92ff" }}>simulation</b> (IllustrisTNG,
          dashed — a model to test observations against, not a telescope).
        </p>
      </div>

      {/* Coverage map */}
      <div className="corpus-block">
        <p className="cch-h">The landscape — wavelength × cosmic time</p>
        <CoverageMap />
        <p className="cch-note">
          Each band reaches as far in redshift as its shaded bar; dots mark how far individual surveys see.
          The three bright, starred bars are the observed sources the pipeline mines today — SDSS anchors z≈0,
          JWST pushes to cosmic dawn, COSMOS2020 bridges between.
        </p>
      </div>

      {/* Band histogram + status split */}
      <div className="dv-two">
        <div className="corpus-block">
          <p className="cch-h">By wavelength — what the sky offers</p>
          <div className="dv-hist">
            {bandCounts.map(({ b, n }) => (
              <div className="dv-hrow" key={b}>
                <span className="dv-hname">{BAND_META[b].label}</span>
                <span className="dv-hbar"><i style={{ width: `${(n / maxBand) * 100}%`, background: BAND_META[b].color }} /></span>
                <span className="dv-hn">{n}</span>
              </div>
            ))}
          </div>
          <p className="cch-note">Optical spectroscopy dominates the public record; radio, IR and X-ray fill in gas, dust and black holes.</p>
        </div>
        <div className="corpus-block">
          <p className="cch-h">By status — live, coming, or archival</p>
          <div className="dv-statusbar">
            {statusCounts.map(({ st, n }) => (
              <i key={st} style={{ width: `${(n / total) * 100}%`, background: STATUS_META[st].color }}
                title={`${STATUS_META[st].label}: ${n}`} />
            ))}
          </div>
          <div className="dv-pills">
            {statusCounts.map(({ st, n }) => (
              <span key={st}><i style={{ background: STATUS_META[st].color }} />{STATUS_META[st].label} · {n}</span>
            ))}
          </div>
          <p className="cch-note">
            <b style={{ color: "#e0a800" }}>&ldquo;On sky&rdquo; isn&rsquo;t &ldquo;downloadable&rdquo;</b> — commissioning and planned
            facilities have little or no public data yet. Archival ≠ dead: retired surveys (SDSS legacy, GALEX, the CDFs) are still deep reference data.
          </p>
        </div>
      </div>

      {/* Grouped catalog */}
      <div className="dv-groups">
        <p className="cch-h" style={{ margin: "0 0 .2rem" }}>The full list — grouped by what it measures</p>
        {GROUPS.map((g) => {
          const members = LANDSCAPE.filter((s) => s.group === g.key);
          return (
            <div className="dv-group" key={g.key}>
              <div className="dv-group-h">
                <b>{g.title}</b><span>{g.sub}</span>
              </div>
              <p className="dv-group-d">{g.desc}</p>
              <div className="dv-list">
                {members.map((s) => (
                  <div className={`dv-grow${s.inUse ? " use" : ""}`} key={s.name}>
                    <span className="dv-gname">
                      {s.name}
                      {s.inUse && <span className="dv-use">in pipeline</span>}
                    </span>
                    <span className="dv-tags">
                      <span className="dv-band" style={{ color: BAND_META[s.band].color, borderColor: BAND_META[s.band].color }}>
                        {BAND_META[s.band].label}
                      </span>
                      <span className="dv-stat" style={{ color: STATUS_META[s.status].color }}>
                        <i style={{ background: STATUS_META[s.status].color }} />{STATUS_META[s.status].label}
                      </span>
                    </span>
                    <span className="dv-gline">{s.line}</span>
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>

      {/* Explorer on-ramp */}
      <a className="dv-explorer" href="/surveys">
        <div>
          <b>Browse the full public-data landscape →</b>
          <span>The interactive Surveys Explorer — all {total}+ surveys, filter by band, redshift, status and data release.</span>
        </div>
        <span className="dv-explorer-cta">Open Surveys Explorer</span>
      </a>
    </div>
  );
}

const RECIPE = [
  "pick a relation",
  "bin galaxies by mass",
  "take medians on a matched scale",
  "fit slope & normalisation",
  "overlay every survey + the simulation",
  "disagreement = a frontier",
];

// Graphic 1 — a measurement is the shape of a relation.
function RelationGallery() {
  const plots: { d: string; extra?: ReactNode; yl: string; xl: string; cap: string }[] = [
    { d: "M30 80 C60 68 96 46 132 30", yl: "log SFR", xl: "log M✱", cap: "Main sequence — lifts with redshift",
      extra: <path d="M30 68 C60 55 96 33 132 17" stroke="#7c86ff" strokeWidth="1.6" strokeOpacity="0.45" fill="none" /> },
    { d: "M30 84 C56 80 76 42 132 32", yl: "12+log(O/H)", xl: "log M✱", cap: "Mass–metallicity — rises then saturates" },
    { d: "M30 30 C70 32 92 38 108 50 C120 60 126 80 132 86", yl: "log φ", xl: "log M✱", cap: "Stellar mass function — Schechter cutoff" },
    { d: "M30 82 C48 72 60 24 78 24 C96 24 108 72 132 82", yl: "M✱/M_halo", xl: "log M_halo", cap: "SF efficiency — peaks at a special halo mass" },
    { d: "M30 78 C64 60 98 40 132 30", yl: "relation", xl: "log M✱", cap: "Data vs TNG — diverge at the massive end",
      extra: <path d="M30 78 C64 58 98 34 132 14" stroke="#9aa3b8" strokeWidth="1.8" strokeDasharray="4 3" fill="none" /> },
  ];
  return (
    <div className="cfg-viz">
      <div className="rg-grid">
        {plots.map((p, i) => (
          <figure className="rg-fig" key={i}>
            <svg viewBox="0 0 150 110" role="img" aria-label={p.cap}>
              <path d="M26 14 V88 H138" fill="none" stroke="#242a3d" strokeWidth="1" />
              <text x="8" y="52" fontSize="8.5" fill="#9aa3b8" fontFamily="ui-monospace,monospace" transform="rotate(-90 8 52)" textAnchor="middle">{p.yl}</text>
              <text x="82" y="104" fontSize="8.5" fill="#9aa3b8" fontFamily="ui-monospace,monospace" textAnchor="middle">{p.xl}</text>
              {p.extra}
              <path d={p.d} stroke="#4ad6c4" strokeWidth="2" fill="none" strokeLinecap="round" />
            </svg>
            <figcaption>{p.cap}</figcaption>
          </figure>
        ))}
      </div>
      <p className="cap">A measurement is the shape of a relation. Solid teal = the data; dashed grey = the IllustrisTNG simulation; faint violet = the same relation at higher redshift.</p>
    </div>
  );
}

// Graphic 2 — eight literature-dispersion quantities ranked by mass-controlled S.
function DispersionChart() {
  const x0 = 150, maxS = 3.6, k = 170 / maxS;
  const y = (i: number) => 16 + i * 25;
  return (
    <svg className="svc" viewBox="0 0 374 244" role="img"
      aria-label="Eight measured quantities ranked by PDG scale factor S; five contested (S>2), two settled (S near 1)">
      <rect x={x0 + 2 * k} y="10" width={(maxS - 2) * k} height="206" fill="#f47272" fillOpacity="0.06" />
      <text x={x0 + 2.8 * k} y="8" fontSize="7.5" fill="#f47272" textAnchor="middle" fontFamily="ui-monospace,monospace">contested · S&gt;2</text>
      <line x1={x0 + k} y1="10" x2={x0 + k} y2="216" stroke="#4ad6c4" strokeWidth="1" strokeDasharray="3 3" strokeOpacity="0.6" />
      <text x={x0 + k} y="230" fontSize="7.5" fill="#4ad6c4" textAnchor="middle" fontFamily="ui-monospace,monospace">S=1 · agree</text>
      {DISPERSION.map((d, i) => {
        const color = VERDICT_META[d.verdict].color;
        const w = (d.S / maxS) * 170;
        return (
          <g key={d.name}>
            <text x="4" y={y(i) + 9.5} fontSize="9.5" fill="#9aa3b8" fontFamily="ui-monospace,monospace">{d.name}</text>
            <rect x={x0} y={y(i)} width={w} height="12" rx="3" fill={color} />
            <text x={x0 + w + 5} y={y(i) + 9.5} fontSize="9" fill={color} fontFamily="ui-monospace,monospace">{d.S.toFixed(2)}</text>
            {d.tag && <text x={x0 + w + 30} y={y(i) + 9.5} fontSize="7.5" fill={color} fontFamily="ui-monospace,monospace">{d.tag}</text>}
          </g>
        );
      })}
    </svg>
  );
}

// Graphic 4 — which of the 4 sources feeds which relation.
function FeedMatrix() {
  const cols: { s: Source; x: number }[] = [
    { s: "SDSS", x: 150 }, { s: "JWST", x: 200 }, { s: "COSMOS2020", x: 250 }, { s: "IllustrisTNG", x: 296 },
  ];
  const rows: { m: string; y: number; fill: Record<string, "obs" | "sim" | "">; }[] = [
    { m: "Main sequence", y: 62, fill: { SDSS: "obs", JWST: "obs", COSMOS2020: "", IllustrisTNG: "sim" } },
    { m: "Mass–metallicity", y: 96, fill: { SDSS: "obs", JWST: "obs", COSMOS2020: "", IllustrisTNG: "sim" } },
    { m: "Stellar mass function", y: 130, fill: { SDSS: "obs", JWST: "obs", COSMOS2020: "obs", IllustrisTNG: "sim" } },
  ];
  return (
    <svg className="svc" viewBox="0 0 340 168" role="img" aria-label="Which data source feeds which measurement">
      {cols.map((c) => (
        <g key={c.s}>
          <text x={c.x} y="24" fontSize="8.5" fill="#c7cede" textAnchor="middle" fontFamily="ui-monospace,monospace">{c.s === "COSMOS2020" ? "COSMOS" : c.s === "IllustrisTNG" ? "TNG" : c.s}</text>
          <text x={c.x} y="35" fontSize="7.5" fill="#6b7386" textAnchor="middle" fontStyle="italic">{SOURCE_META[c.s].z}</text>
        </g>
      ))}
      {rows.map((r) => (
        <g key={r.m}>
          <text x="6" y={r.y + 4} fontSize="9" fill="#9aa3b8" fontFamily="ui-monospace,monospace">{r.m}</text>
          {cols.map((c) => {
            const v = r.fill[c.s];
            if (v === "obs") return <circle key={c.s} cx={c.x} cy={r.y} r="5.5" fill="#4ad6c4" />;
            if (v === "sim") return <circle key={c.s} cx={c.x} cy={r.y} r="5.5" fill="none" stroke="#7c86ff" strokeWidth="2" />;
            return <circle key={c.s} cx={c.x} cy={r.y} r="2" fill="#242a3d" />;
          })}
        </g>
      ))}
      <g transform="translate(150,156)">
        <circle cx="0" cy="-3" r="4.5" fill="#4ad6c4" /><text x="9" y="0" fontSize="8" fill="#9aa3b8">survey</text>
        <circle cx="66" cy="-3" r="4.5" fill="none" stroke="#7c86ff" strokeWidth="2" /><text x="76" y="0" fontSize="8" fill="#9aa3b8">simulation</text>
      </g>
    </svg>
  );
}

function ResearchView() {
  return (
    <div className="dv">
      <p className="dv-lead">
        A measurement here is the <b>shape of a relation</b> — plotted the same way for every survey and every
        simulation. Because the recipe never changes, any disagreement that&rsquo;s left is <b>physics, not method</b>.
        Each method below is a real, fixed recipe; the dispersion scores come from the <b>published literature</b>.
        But any relation the pipeline computes on its own is a <b>descriptive draft</b>, not a validated measurement,
        until a person has reviewed it.
      </p>

      {/* Recipe */}
      <div className="corpus-block">
        <p className="cch-h">How a measurement is built</p>
        <div className="cfg-pipe">
          {RECIPE.map((s, i) => (
            <span key={i}>{i > 0 && <em>→</em>}
              {i === RECIPE.length - 1 ? <b style={{ color: "#f47272" }}>{s}</b> : s}
            </span>
          ))}
        </div>
        <p className="cch-note">Every method here is the same recipe on a different relation — the last step is where the science is.</p>
      </div>

      {/* Relation gallery */}
      <div className="corpus-block">
        <p className="cch-h">What a relation looks like</p>
        <RelationGallery />
      </div>

      {/* Dispersion chart */}
      <div className="corpus-block">
        <p className="cch-h">Settled vs contested — how much the literature disagrees</p>
        <DispersionChart />
        <p className="cch-note">
          Independent published measurements of the same quantity, matched by mass and redshift. Bars past
          <b style={{ color: "#f47272" }}> S=2</b> disagree beyond their own error bars — a live frontier; near
          <b style={{ color: "#4ad6c4" }}> S=1</b> the field agrees. Two look contested but aren&rsquo;t:
          <b> UV-LF α</b> is <b style={{ color: "#4ad6c4" }}>z-driven</b> (cosmic evolution, not conflict), and gas
          <b> metallicity</b> only truly disagrees at <b style={{ color: "#e0a458" }}>z&gt;7</b> once you compare like-mass galaxies.
        </p>
        <p className="cfg-credit">Dispersion scores are computed from published measurements; the pipeline&rsquo;s own draft results are descriptive until a human review clears them — some have not met our publishable bar.</p>
      </div>

      {/* The catalog */}
      <div className="dv-groups">
        <p className="cch-h" style={{ margin: "0 0 .2rem" }}>The measurements — grouped by what they probe</p>
        {RESEARCH_GROUPS.map((g) => {
          const members = MEASUREMENTS.filter((m) => m.group === g.key);
          return (
            <div className="dv-group" key={g.key}>
              <div className="dv-group-h"><b>{g.title}</b><span>{members.length} {members.length === 1 ? "relation" : "relations"}</span></div>
              <p className="dv-group-d">{g.desc}</p>
              <div className="rc-list">
                {members.map((m) => {
                  const vm = VERDICT_META[m.verdict];
                  return (
                    <div className="rc-item" key={m.name}>
                      <div className="rc-head">
                        <b>{m.name}</b>
                        <span className="rc-verdict" style={{ color: vm.color, borderColor: vm.color }}>
                          {vm.label}{m.S != null && <i> · S {m.S.toFixed(2)}</i>}
                        </span>
                      </div>
                      <div className="rc-row"><span className="rc-k">measures</span><span>{m.measures}</span></div>
                      <div className="rc-row"><span className="rc-k">tests</span><span>{m.tests}</span></div>
                      <div className="rc-row"><span className="rc-k">how</span><span className="rc-how">{m.method}</span></div>
                      <div className="rc-tags">
                        {m.data.map((s) => (
                          <span className={`rc-src${SOURCE_META[s].sim ? " sim" : ""}`} key={s}>{s === "IllustrisTNG" ? "TNG" : s}</span>
                        ))}
                        {m.frontier && <span className="rc-frontier">frontier → {m.frontier}</span>}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>

      {/* Feed matrix */}
      <div className="corpus-block">
        <p className="cch-h">Which data feeds which measurement</p>
        <FeedMatrix />
        <p className="cch-note">Every relation is anchored at z≈0 by SDSS and pushed to the frontier by JWST; COSMOS2020 deepens only the mass function; IllustrisTNG (rings) is the simulation each one is checked against.</p>
      </div>

      {/* Cross-step footer */}
      <a className="dv-explorer" href="/lab">
        <div>
          <b>These measurements join the pipeline together →</b>
          <span>They run on the surveys in <b style={{ color: "#4ad6c4" }}>Data</b>; the disagreements they expose become the ranked frontiers in <b style={{ color: "#7c86ff" }}>Ranking</b>. Use the Topic menu above to walk the steps.</span>
        </div>
        <span className="dv-explorer-cta">Back to the pipeline</span>
      </a>
    </div>
  );
}

// Graphic 1 — the outputs pipeline spine: Draft → Referee → Revise (loop) → Gate.
// The full pipeline from a computed result to a compiled (descriptive) paper.
function PipelineFlow() {
  const stages: [string, string, "" | "gate" | "held"][] = [
    ["idea", "a ranked frontier", ""],
    ["study", "public data → numbers", ""],
    ["draft", "AASTeX manuscript", ""],
    ["referee", "astrosage-70b ⟲ revise", ""],
    ["gates", "novelty · citations", "gate"],
    ["PDF", "held: descriptive", "held"],
  ];
  return (
    <div className="pf2">
      <style>{`
        .pf2-row{display:flex;flex-wrap:wrap;align-items:stretch;gap:.25rem .2rem;padding:.7rem .8rem;background:#0a0d17;border:1px solid var(--lab-line);border-radius:9px}
        .pf2-node{display:flex;flex-direction:column;gap:.1rem;padding:.15rem .5rem}
        .pf2-node b{font-family:ui-monospace,monospace;font-size:.8rem;color:var(--lab-ink);font-weight:650}
        .pf2-node span{font-size:.61rem;color:var(--lab-soft);line-height:1.2;white-space:nowrap}
        .pf2-node.gate b{color:var(--lab-accent2)}
        .pf2-node.held b{color:#e0a458}
        .pf2-arr{align-self:center;color:var(--lab-accent);font-weight:700;font-family:ui-monospace,monospace;font-size:.8rem}
        .pf2-cap{font-size:.76rem;color:var(--lab-soft);line-height:1.6;margin:.6rem 0 0}
        .pf2-cap em{color:#e0a458;font-style:normal;font-weight:600}
      `}</style>
      <div className="pf2-row">
        {stages.map(([k, s, kind], i) => (
          <Fragment key={k}>
            {i > 0 && <span className="pf2-arr">→</span>}
            <span className={`pf2-node ${kind}`}><b>{k}</b><span>{s}</span></span>
          </Fragment>
        ))}
      </div>
      <p className="pf2-cap">Each station does one job a journal does — typeset the numbers, referee them, force revisions, then check every citation is real and the claim is new. <em>It&rsquo;s a filter, not a conveyor belt:</em> most runs stop early, and the line ends at a gate that holds the paper back as <b style={{ color: "#e0a458" }}>descriptive</b> until a human clears it.</p>
    </div>
  );
}

function PaperView() {
  const scatter = [[45,99],[62,90],[80,97],[98,85],[118,88],[138,78],[158,82],[178,70],[198,74],[220,62],[242,58],[258,50]];
  return (
    <div className="dv">
      <p className="dv-lead">
        <b>Writing a paper isn&rsquo;t proving it.</b> NebulaMind can write and referee a full, journal-formatted
        manuscript for every result it computes — automatically, overnight. What it does <b style={{ color: "#f47272" }}>not</b> do
        is decide the science is true. Every draft is labelled <b>descriptive, not validated</b> until a human clears it — and so far essentially none have.
      </p>

      {/* The pipeline: research -> journal paper */}
      <div className="corpus-block">
        <p className="cch-h">How a computed result becomes a journal paper</p>
        <PipelineFlow />
      </div>

      {/* Manuscript + referee */}
      <div className="corpus-block">
        <p className="cch-h">One manuscript, one referee — a real example</p>
        <div className="ms-row">
          <div className="ms-card">
            <span className="ms-stamp">descriptive — not validated</span>
            <p className="ms-eyebrow">AASTeX · aastex631 · compiled with tectonic</p>
            <h4 className="ms-title">The star-forming main sequence in GSWLC-2</h4>
            <p className="ms-auth">NebulaMind Lab · autonomous overnight</p>
            <p className="ms-abstract">
              <b>Bounded &amp; descriptive automated result — not a validated measurement.</b> Star-forming main
              sequence from GSWLC-2 (GALEX+WISE SED SFRs), z=0.01–0.10: N<sub>SF</sub>=36,842, slope ≈0.57,
              log SFR ≈0.04 at logM★=10. Uncorrected for completeness / selection; single calibration.
            </p>
            <div className="ms-fig">
              <svg viewBox="0 0 300 120" role="img" aria-label="Rising star-forming main sequence: SFR vs stellar mass, fit slope 0.57">
                <path d="M30 20 V105 H270" fill="none" stroke="#242a3d" strokeWidth="1" />
                <path d="M30 100 L270 40" stroke="#4ad6c4" strokeWidth="2" />
                {scatter.map(([cx, cy], i) => <circle key={i} cx={cx} cy={cy} r="2.4" fill="#9aa3b8" fillOpacity="0.85" />)}
                <text x="150" y="118" textAnchor="middle" fontFamily="ui-monospace,monospace" fontSize="8" fill="#9aa3b8">log M★</text>
                <text x="10" y="62" textAnchor="middle" fontFamily="ui-monospace,monospace" fontSize="8" fill="#9aa3b8" transform="rotate(-90 10 62)">log SFR</text>
              </svg>
            </div>
            <p className="ms-figcap">Fig. 1 — SFR vs stellar mass; fit slope ≈0.57.</p>
          </div>
          <div className="rv-card">
            <div className="rv-head">
              <span className="rv-chip">⚠ MAJOR · revise</span>
              <span className="rv-model">astrosage-70b · automated referee</span>
            </div>
            <p className="rv-verdict"><b>Verdict —</b> Preliminary results require further validation and analysis.</p>
            <ul className="rv-risks">
              <li><span className="rv-x">✗</span> <b>Dust attenuation</b> — GALEX+WISE SFRs may be biased; not corrected for.</li>
              <li><span className="rv-x">✗</span> <b>AGN contamination</b> — non-star-forming galaxies may inflate the sample.</li>
              <li><span className="rv-x">✗</span> <b>Selection &amp; redshift evolution</b> within z=0.01–0.10 — not accounted for.</li>
            </ul>
            <p className="rv-next"><b>Next step —</b> quantify systematic uncertainties and cross-check against alternative SFR indicators.</p>
          </div>
        </div>
        <p className="cch-note">The manuscript self-labels &ldquo;not a validated measurement,&rdquo; and the referee immediately names the systematics the draft glossed over — the machine criticising its own output.</p>
      </div>

      {/* Batch honesty bar */}
      <div className="corpus-block">
        <p className="cch-h">The overnight batch, honestly</p>
        <div className="bh-top">
          <span className="bh-big">2,490</span>
          <span className="bh-biglab">manuscripts drafted &amp; refereed in ~420 min<br />on GSWLC-2 · COSMOS2020 · JWST</span>
        </div>
        <div className="bh-meterrow">
          <span className="bh-mlab">validated</span>
          <span className="bh-meter"><i style={{ width: "0.4%" }} /></span>
          <span className="bh-pct">0.0%</span>
        </div>
        <div className="bh-chips">
          <span className="bh-chip">2,490 manuscripts</span>
          <span className="bh-chip amber">2,489 sent back · preliminary</span>
          <span className="bh-chip coral">0 cleared as validated</span>
        </div>
        <p className="cch-note">0 of 2,490 cleared — that is the referee doing its job, not a failure. Nothing is held up as a measurement until a human clears it.</p>
      </div>

      {/* Publishable bar + what descriptive means */}
      <div className="dv-two">
        <div className="corpus-block">
          <p className="cch-h">The publishable bar</p>
          <div className="pb-ladder">
            <ul>
              {["compiles", "lint-clean", "selection-honest"].map((t) => (
                <li key={t} className="pass"><span className="pb-ic">✓</span>{t}</li>
              ))}
              <li className="pb-div"><span>automatic ends · judgment begins</span></li>
              {["literature-grounded motivation", "non-circular result", "defensible conclusion"].map((t) => (
                <li key={t} className="fail"><span className="pb-ic">✗</span>{t}</li>
              ))}
            </ul>
            <p className="pb-foot">Still descriptive — a human decides.</p>
          </div>
        </div>
        <div className="corpus-block">
          <p className="cch-h">What &ldquo;descriptive&rdquo; means</p>
          <p className="cch-note" style={{ margin: "0 0 .7rem", fontSize: ".84rem", color: "#e8ecf5" }}>
            The number is <b>computed correctly</b> and its caveats are <b>stated honestly</b> — but <b style={{ color: "#f47272" }}>no
            human has yet vouched for it</b> as a result. Compiling cleanly and labelling honestly clears the floor, not the bar.
          </p>
          <p className="cch-note" style={{ margin: 0 }}>
            The gate has teeth: of the flagship auto-drafts put forward for human review, <b style={{ color: "#f47272" }}>all 9 were rejected</b>.
            Even our best hand-picked drafts don&rsquo;t clear automatically — which is exactly why the honest label is believable.
          </p>
        </div>
      </div>

      {/* Two output tracks */}
      <div className="pt-tracks">
        <button className="pt-track" onClick={() => select("paper", "flagship")}>
          <b>Flagship studies →</b>
          <span>The hand-guided, curated papers that went the full distance. Few, deep, complete — open the manuscripts.</span>
        </button>
        <button className="pt-track" onClick={() => select("paper", "pipeline")}>
          <b>Pipeline runs →</b>
          <span>The fully-automated track, live from the run pipeline. Many, fast, high-attrition — most stop early, 0 validated.</span>
        </button>
      </div>

      {/* Cross-step footer */}
      <a className="dv-explorer" href="/lab">
        <div>
          <b>Topic → Data → Research → Paper — the full loop →</b>
          <span>Pick a question, ground it in real <b style={{ color: "#4ad6c4" }}>surveys</b>, compute an honest <b style={{ color: "#7c86ff" }}>result</b>, then draft and referee it like a journal would. The last step is the one we <b>don&rsquo;t</b> automate: a human decides what&rsquo;s true.</span>
        </div>
        <span className="dv-explorer-cta">Back to the pipeline</span>
      </a>
    </div>
  );
}

export default function LabStages() {
  useLabUrlSync();
  const tab = useTab();
  const sub = useSub();
  const [topicOpen, setTopicOpen] = useState("simulations-vs-physics");

  function goNext() {
    const items = itemsFor(tab);
    const si = items.findIndex((it) => it.value === sub);
    if (sub && si >= 0 && si < items.length - 1) {
      select(tab, items[si + 1].value);
      return;
    }
    const i = STEPS.findIndex((s) => s.key === tab);
    if (i < STEPS.length - 1) select(STEPS[i + 1].key);
  }

  return (
    <div className="cfg">
      <style>{`
        .cfg{border:1px solid var(--lab-line);border-radius:14px;background:var(--lab-panel);overflow:hidden}
        .cfg-panel{padding:1.3rem 1.25rem;min-height:104px}
        .cfg-panel-h{font-family:ui-monospace,monospace;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--lab-accent2);margin:0 0 .85rem}
        .cfg-pipe{display:flex;flex-wrap:wrap;align-items:center;gap:.3rem .5rem;font-family:ui-monospace,monospace;font-size:.735rem;color:var(--lab-ink);line-height:1.5;margin:0 0 .5rem;padding:.55rem .7rem;background:#0a0d17;border:1px solid var(--lab-line);border-radius:8px}
        .cfg-pipe em{color:var(--lab-accent);font-style:normal;font-weight:700}
        .cfg-credit{font-size:.73rem;color:var(--lab-soft);line-height:1.4;margin:0 0 .6rem}
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
        .cfg-viz{margin:.25rem 0 .85rem;border:1px solid var(--lab-line);border-radius:10px;background:#0a0d17;padding:.75rem .9rem .55rem}
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
        .cfg-subnav{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:.9rem}
        .cfg-subnav button{background:#0a0d17;border:1px solid var(--lab-line);color:var(--lab-soft);font-size:.8rem;padding:.35rem .75rem;border-radius:999px;cursor:pointer;font-family:inherit;transition:color .12s,border-color .12s,background .12s}
        .cfg-subnav button:hover{color:var(--lab-ink);border-color:var(--lab-accent)}
        .cfg-subnav button.on{background:rgba(124,134,255,.14);border-color:var(--lab-accent);color:var(--lab-ink)}
        .cfg-subs{display:flex;flex-direction:column;gap:.7rem}
        .cfg-sub{border:1px solid var(--lab-line);border-radius:10px;background:#0a0d17;overflow:hidden}
        .cfg-sub-h{padding:.6rem .9rem;border-bottom:1px solid var(--lab-line);font-size:.92rem;font-weight:650;color:var(--lab-ink)}
        .cfg-sub-h span{font-family:ui-monospace,monospace;font-size:.66rem;color:var(--lab-accent2);font-weight:400;margin-left:.55rem}
        .cfg-sub-row{display:grid;grid-template-columns:84px 1fr;gap:.7rem;padding:.5rem .9rem;border-bottom:1px solid rgba(36,42,61,.5);font-size:.83rem;line-height:1.5}
        .cfg-sub-row:last-child{border-bottom:none}
        .cfg-sub-k{font-family:ui-monospace,monospace;font-size:.63rem;letter-spacing:.06em;text-transform:uppercase;color:var(--lab-soft);padding-top:.12rem}
        .cfg-sub-v{color:var(--lab-ink)}
        .cfg-sub-desc{padding:.7rem .9rem;font-size:.86rem;color:var(--lab-ink);line-height:1.55}
        .corpus-view{display:flex;flex-direction:column;gap:.8rem;margin-top:.7rem}
        .corpus-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(135px,1fr));gap:.5rem}
        .cst{background:#0a0d17;border:1px solid var(--lab-line);border-radius:10px;padding:.65rem .8rem}
        .cst b{display:block;font-size:1.35rem;color:var(--lab-ink);font-weight:700;letter-spacing:-.02em}
        .cst span{font-size:.71rem;color:var(--lab-soft);line-height:1.3}
        .cst.accent b{color:var(--lab-accent2)}
        .corpus-block{border:1px solid var(--lab-line);border-radius:10px;background:#0a0d17;padding:.85rem .9rem}
        .subnav-video{width:100%;max-width:420px;aspect-ratio:16/9;margin:.3rem 0 .9rem;border:1px solid var(--lab-line);border-radius:10px;overflow:hidden;background:#000}
        .subnav-video iframe{width:100%;height:100%;border:0;display:block}
        .cch-h{font-family:ui-monospace,monospace;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--lab-accent2);margin:0 0 .55rem}
        .corpus-block svg{width:100%;height:auto;display:block}
        .cch-note{font-size:.74rem;color:var(--lab-soft);margin:.5rem 0 0;line-height:1.5}
        .corpus-split{display:flex;height:30px;border-radius:7px;overflow:hidden;margin:.15rem 0 .55rem;border:1px solid var(--lab-line)}
        .corpus-split i{display:flex;align-items:center;justify-content:center;font-family:ui-monospace,monospace;font-size:.64rem;font-weight:600;min-width:0;overflow:hidden}
        .corpus-legend{display:flex;flex-wrap:wrap;gap:.45rem 1rem;font-size:.73rem;color:var(--lab-soft)}
        .corpus-legend span{display:inline-flex;align-items:center;gap:.35rem}
        .corpus-legend i{width:9px;height:9px;border-radius:2px;display:inline-block;flex-shrink:0}
        .corpus-tbl{width:100%;border-collapse:collapse;font-size:.84rem}
        .corpus-tbl td{padding:.45rem .55rem;border-top:1px solid rgba(36,42,61,.6);vertical-align:top;line-height:1.45}
        .corpus-tbl tr:first-child td{border-top:none}
        .corpus-tbl td:first-child{color:var(--lab-ink);font-weight:600;width:38%}
        .corpus-tbl td:last-child{color:var(--lab-soft)}
        .embed-lb{display:flex;flex-direction:column;gap:.32rem;margin-top:.1rem}
        .elb-row{display:grid;grid-template-columns:160px 1fr 3rem;gap:.6rem;align-items:center;font-size:.8rem}
        .elb-name{color:var(--lab-soft);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
        .elb-row.chosen .elb-name{color:var(--lab-accent2);font-weight:600}
        .elb-bar{height:6px;background:#1a1f30;border-radius:3px;overflow:hidden}
        .elb-bar i{display:block;height:100%;background:linear-gradient(90deg,var(--lab-accent),var(--lab-accent2))}
        .elb-row.chosen .elb-bar i{background:var(--lab-accent2)}
        .elb-score{font-family:ui-monospace,monospace;font-size:.75rem;color:var(--lab-soft);text-align:right}
        .elb-row.chosen .elb-score{color:var(--lab-accent2)}
        .scatter{width:100%;max-width:560px;aspect-ratio:1/1;display:block;margin:.1rem auto .2rem;background:radial-gradient(circle at 50% 45%,#0d1120,#080a12);border:1px solid var(--lab-line);border-radius:10px}
        .scatter circle{transition:none}
        .scatter-legend{display:flex;flex-wrap:wrap;gap:.35rem .9rem;font-size:.7rem;color:var(--lab-soft);justify-content:center;margin-top:.2rem}
        .scatter-legend span{display:inline-flex;align-items:center;gap:.32rem}
        .scatter-legend i{width:8px;height:8px;border-radius:50%;display:inline-block;flex-shrink:0}
        .svc{width:100%;max-width:520px;height:auto;display:block;margin:.55rem auto .1rem;background:#0a0d17;border:1px solid var(--lab-line);border-radius:9px}
        .simmap{width:100%;max-width:470px;aspect-ratio:100/64;display:block;margin:.5rem auto .2rem;background:radial-gradient(circle at 60% 40%,#0d1120,#080a12);border:1px solid var(--lab-line);border-radius:10px}
        .embed-lb.frontiers .clu-row{grid-template-columns:1fr 150px}
        .ing{display:flex;flex-wrap:wrap;gap:.5rem;align-items:stretch}
        .ing-card{flex:1 1 150px;background:#0d1120;border:1px solid var(--lab-line);border-radius:9px;padding:.6rem .75rem}
        .ing-k{font-family:ui-monospace,monospace;font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--lab-accent2);margin:0 0 .22rem}
        .ing-card.g .ing-k{color:#8a92ff}
        .ing-card.f .ing-k{color:#e0a458}
        .ing-card b{display:block;font-size:.9rem;color:var(--lab-ink);font-weight:650;margin-bottom:.14rem;line-height:1.3}
        .ing-card span{font-size:.77rem;color:var(--lab-soft);line-height:1.4}
        .ing-x{align-self:center;color:var(--lab-soft);font-family:ui-monospace,monospace;font-size:1.1rem}
        .heat-scale{display:flex;align-items:center;gap:.55rem;justify-content:center;flex-wrap:wrap;margin-top:.5rem;font-size:.7rem;color:var(--lab-soft);font-family:ui-monospace,monospace}
        .heat-bar{flex:0 1 200px;height:9px;border-radius:5px;background:linear-gradient(90deg,rgb(58,69,96),rgb(74,214,196),rgb(250,204,21),rgb(251,90,90))}
        .heat-grey{display:inline-flex;align-items:center;gap:.3rem;margin-left:.5rem}
        .heat-grey i{width:8px;height:8px;border-radius:50%;background:#222a3a;display:inline-block}
        .ov-flow{display:flex;flex-wrap:wrap;align-items:center;gap:.4rem .5rem;margin:.1rem 0 .2rem}
        .ov-flow span{background:#0d1120;border:1px solid var(--lab-line);border-radius:8px;padding:.42rem .7rem;font-size:.82rem;color:var(--lab-ink)}
        .ov-flow span b{color:var(--lab-accent2);font-family:ui-monospace,monospace;margin-right:.4rem}
        .ov-flow em{color:var(--lab-accent);font-style:normal;font-weight:700}
        .two-layer{display:grid;grid-template-columns:1fr 1fr;gap:.6rem;margin:.15rem 0 .1rem}
        .tl-col{border:1px solid var(--lab-line);border-radius:9px;padding:.7rem .8rem;background:#0d1120}
        .tl-col.accent{border-color:rgba(74,214,196,.4)}
        .tl-h{font-family:ui-monospace,monospace;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--lab-soft)}
        .tl-col.accent .tl-h{color:var(--lab-accent2)}
        .tl-n{font-size:1.25rem;font-weight:700;color:var(--lab-ink);letter-spacing:-.02em;margin:.15rem 0 .3rem}
        .tl-col p{font-size:.76rem;color:var(--lab-soft);margin:0;line-height:1.5}
        @media(max-width:540px){.two-layer{grid-template-columns:1fr}}
        .nn-demo{margin-top:.55rem}
        .nn-demo + .nn-demo{margin-top:.7rem;padding-top:.7rem;border-top:1px solid rgba(36,42,61,.6)}
        .nn-seed{display:flex;flex-direction:column;gap:.12rem;margin:0 0 .4rem}
        .nn-seed b{font-size:.86rem;color:var(--lab-ink);font-weight:650;line-height:1.3}
        .nn-seed span{font-size:.68rem;color:var(--lab-accent2);font-family:ui-monospace,monospace}
        .nn-list{display:flex;flex-direction:column;gap:.3rem}
        .nn-row{display:grid;grid-template-columns:2.3rem 54px 1fr;gap:.55rem;align-items:center;font-size:.79rem}
        .nn-cos{font-family:ui-monospace,monospace;font-size:.73rem;color:var(--lab-accent2)}
        .nn-bar{height:5px;background:#1a1f30;border-radius:3px;overflow:hidden}
        .nn-bar i{display:block;height:100%;background:linear-gradient(90deg,var(--lab-accent),var(--lab-accent2))}
        .nn-ttl{color:var(--lab-soft);line-height:1.3}
        .clu-row{display:grid;grid-template-columns:1fr 130px 2.6rem;gap:.7rem;align-items:center;padding:.4rem 0;border-top:1px solid rgba(36,42,61,.5)}
        .clu-row:first-child{border-top:none}
        .clu-label{display:flex;flex-direction:column;line-height:1.3}
        .clu-label b{font-size:.84rem;color:var(--lab-ink);font-weight:600}
        .clu-row.top .clu-label b{color:var(--lab-accent2)}
        .clu-kw{font-size:.68rem;color:var(--lab-soft);font-family:ui-monospace,monospace}
        .clu-row.top .elb-bar i{background:var(--lab-accent2)}
        .cfg-ov{font-size:.9rem;color:var(--lab-ink);line-height:1.6;margin:.5rem 0 0}
        .cfg-ov b{color:var(--lab-accent2);font-weight:600}
        @media(max-width:560px){.cfg-sub-row{grid-template-columns:1fr;gap:.15rem}}
        .cfg-list{display:flex;flex-direction:column;gap:.55rem}
        .cfg-item{border:1px solid var(--lab-line);border-radius:9px;background:#0a0d17;padding:.7rem .85rem}
        .cfg-item-k{font-size:.9rem;font-weight:650;color:var(--lab-ink)}
        .cfg-item-k span{font-family:ui-monospace,monospace;font-size:.7rem;color:var(--lab-accent2);font-weight:400;margin-left:.5rem}
        .cfg-item-v{font-size:.82rem;color:var(--lab-soft);line-height:1.5;margin-top:.25rem}
        @media(max-width:560px){.cfg-deriv-row{grid-template-columns:1fr;gap:.2rem}}
        .dv{display:flex;flex-direction:column;gap:.8rem;margin-top:.2rem}
        .dv-lead{font-size:.9rem;color:var(--lab-ink);line-height:1.6;margin:.1rem 0 .1rem}
        .dv-lead b{color:var(--lab-accent2);font-weight:600}
        .dv-meter{height:5px;border-radius:3px;background:#1a1f30;overflow:hidden;margin:.1rem 0 .7rem}
        .dv-meter i{display:block;height:100%;background:var(--lab-accent2)}
        .dv-chips{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:.5rem}
        .dv-chip{background:#0d1120;border:1px solid var(--lab-line);border-left:3px solid var(--lab-accent);border-radius:9px;padding:.55rem .7rem}
        .dv-chip.sim{border-left-style:dashed}
        .dv-chip-h{display:flex;align-items:baseline;justify-content:space-between;gap:.5rem}
        .dv-chip-h b{font-size:.92rem;color:var(--lab-ink);font-weight:700}
        .dv-chip-h span{font-family:ui-monospace,monospace;font-size:.66rem;color:var(--lab-soft)}
        .dv-chip p{font-size:.75rem;color:var(--lab-soft);line-height:1.4;margin:.3rem 0 0}
        .dv-cov{width:100%;height:auto;display:block;margin:.2rem 0}
        .dv-two{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}
        @media(max-width:620px){.dv-two{grid-template-columns:1fr}}
        .dv-hist{display:flex;flex-direction:column;gap:.32rem;margin:.1rem 0}
        .dv-hrow{display:grid;grid-template-columns:74px 1fr 1.6rem;gap:.5rem;align-items:center;font-size:.78rem}
        .dv-hname{color:var(--lab-soft);white-space:nowrap}
        .dv-hbar{height:9px;background:#1a1f30;border-radius:3px;overflow:hidden}
        .dv-hbar i{display:block;height:100%;border-radius:3px}
        .dv-hn{font-family:ui-monospace,monospace;font-size:.74rem;color:var(--lab-ink);text-align:right}
        .dv-statusbar{display:flex;height:26px;border-radius:6px;overflow:hidden;margin:.15rem 0 .5rem;border:1px solid var(--lab-line)}
        .dv-statusbar i{display:block;height:100%;border-right:2px solid #0a0d17}
        .dv-statusbar i:last-child{border-right:none}
        .dv-pills{display:flex;flex-wrap:wrap;gap:.35rem .8rem;font-size:.73rem;color:var(--lab-soft);margin-bottom:.15rem}
        .dv-pills span{display:inline-flex;align-items:center;gap:.32rem}
        .dv-pills i{width:9px;height:9px;border-radius:2px;display:inline-block;flex-shrink:0}
        .dv-groups{display:flex;flex-direction:column;gap:.55rem}
        .dv-group{border:1px solid var(--lab-line);border-radius:10px;background:#0a0d17;padding:.7rem .85rem}
        .dv-group-h{display:flex;align-items:baseline;gap:.55rem}
        .dv-group-h b{font-size:.92rem;color:var(--lab-ink);font-weight:650}
        .dv-group-h span{font-family:ui-monospace,monospace;font-size:.66rem;color:var(--lab-accent2)}
        .dv-group-d{font-size:.78rem;color:var(--lab-soft);line-height:1.5;margin:.25rem 0 .55rem}
        .dv-list{display:flex;flex-direction:column;gap:.1rem}
        .dv-grow{display:grid;grid-template-columns:170px 128px 1fr;gap:.6rem;align-items:start;padding:.4rem 0;border-top:1px solid rgba(36,42,61,.55);font-size:.8rem;line-height:1.45}
        .dv-grow:first-child{border-top:none}
        .dv-gname{color:var(--lab-ink);font-weight:600;display:flex;flex-direction:column;gap:.15rem}
        .dv-grow.use .dv-gname{color:var(--lab-accent2)}
        .dv-use{font-family:ui-monospace,monospace;font-size:.56rem;letter-spacing:.04em;text-transform:uppercase;color:var(--lab-accent2);border:1px solid rgba(74,214,196,.5);border-radius:999px;padding:.03rem .35rem;width:fit-content}
        .dv-tags{display:flex;flex-wrap:wrap;gap:.3rem;padding-top:.05rem}
        .dv-band{font-size:.6rem;font-family:ui-monospace,monospace;border:1px solid;border-radius:4px;padding:.03rem .3rem;opacity:.9}
        .dv-stat{display:inline-flex;align-items:center;gap:.25rem;font-size:.6rem;font-family:ui-monospace,monospace}
        .dv-stat i{width:6px;height:6px;border-radius:50%;display:inline-block}
        .dv-gline{color:var(--lab-soft)}
        @media(max-width:560px){.dv-grow{grid-template-columns:1fr;gap:.15rem}.dv-tags{padding-top:0}}
        .dv-explorer{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;text-decoration:none;border:1px solid rgba(124,134,255,.4);border-radius:11px;background:linear-gradient(90deg,rgba(124,134,255,.09),rgba(74,214,196,.06));padding:.85rem 1rem;transition:border-color .15s}
        .dv-explorer:hover{border-color:var(--lab-accent)}
        .dv-explorer>div>b{display:block;font-size:.95rem;color:var(--lab-ink);font-weight:650}
        .dv-explorer div span{display:block;font-size:.78rem;color:var(--lab-soft);line-height:1.45;margin-top:.2rem}
        .dv-explorer-cta{flex-shrink:0;font-size:.82rem;font-weight:600;color:var(--lab-accent2);border:1px solid rgba(74,214,196,.45);border-radius:8px;padding:.45rem .8rem;white-space:nowrap}
        .rg-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(132px,1fr));gap:.7rem}
        .rg-fig{margin:0}
        .rg-fig svg{width:100%;height:auto;display:block}
        .rg-fig figcaption{font-size:.68rem;color:var(--lab-soft);text-align:center;margin-top:.3rem;line-height:1.4}
        .rc-list{display:flex;flex-direction:column;gap:.45rem}
        .rc-item{border:1px solid var(--lab-line);border-radius:9px;background:#0d1120;padding:.6rem .75rem}
        .rc-head{display:flex;align-items:center;justify-content:space-between;gap:.6rem;flex-wrap:wrap;margin-bottom:.35rem}
        .rc-head b{font-size:.9rem;color:var(--lab-ink);font-weight:650}
        .rc-verdict{font-family:ui-monospace,monospace;font-size:.62rem;letter-spacing:.03em;border:1px solid;border-radius:999px;padding:.05rem .45rem;white-space:nowrap}
        .rc-verdict i{font-style:normal;opacity:.85}
        .rc-row{display:grid;grid-template-columns:62px 1fr;gap:.6rem;font-size:.79rem;line-height:1.45;padding:.08rem 0}
        .rc-k{font-family:ui-monospace,monospace;font-size:.6rem;letter-spacing:.06em;text-transform:uppercase;color:var(--lab-soft);padding-top:.18rem}
        .rc-row span:last-child{color:var(--lab-ink)}
        .rc-how{color:var(--lab-soft)!important;font-family:ui-monospace,monospace;font-size:.72rem}
        .rc-tags{display:flex;flex-wrap:wrap;gap:.3rem;margin-top:.4rem;align-items:center}
        .rc-src{font-family:ui-monospace,monospace;font-size:.62rem;color:var(--lab-accent2);border:1px solid rgba(74,214,196,.4);border-radius:4px;padding:.03rem .35rem}
        .rc-src.sim{color:var(--lab-accent);border-color:rgba(124,134,255,.45)}
        .rc-frontier{font-family:ui-monospace,monospace;font-size:.6rem;color:#f47272;margin-left:.15rem}
        @media(max-width:560px){.rc-row{grid-template-columns:1fr;gap:.05rem}}
        .ms-row{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}
        @media(max-width:600px){.ms-row{grid-template-columns:1fr}}
        .ms-card{position:relative;border:1px solid var(--lab-line);border-radius:12px;background:#0a0d17;padding:1rem 1.05rem}
        .ms-stamp{display:inline-block;background:rgba(244,114,114,.14);color:#f47272;border:1px solid rgba(244,114,114,.5);font-family:ui-monospace,monospace;font-size:.58rem;letter-spacing:.06em;text-transform:uppercase;padding:.2rem .55rem;border-radius:999px;margin:0 0 .55rem}
        .ms-eyebrow{font-family:ui-monospace,monospace;font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--lab-soft);margin:0 0 .5rem}
        .ms-title{font-size:1rem;font-weight:650;color:var(--lab-ink);margin:0 0 .2rem;line-height:1.3;max-width:32ch}
        .ms-auth{font-family:ui-monospace,monospace;font-size:.72rem;color:var(--lab-accent2);margin:0 0 .55rem}
        .ms-abstract{font-size:.79rem;color:var(--lab-soft);line-height:1.55;margin:0 0 .7rem}
        .ms-abstract b{color:var(--lab-ink);font-weight:600}
        .ms-fig{border:1px solid var(--lab-line);border-radius:8px;background:#0a0d17;padding:.4rem}
        .ms-fig svg{width:100%;height:auto;display:block}
        .ms-figcap{font-family:ui-monospace,monospace;font-size:.68rem;color:var(--lab-soft);margin:.4rem 0 0}
        .rv-card{border:1px solid var(--lab-line);border-radius:12px;background:#0a0d17;padding:1rem 1.05rem}
        .rv-head{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;margin:0 0 .7rem}
        .rv-chip{font-family:ui-monospace,monospace;font-size:.64rem;letter-spacing:.05em;color:#e0a458;background:rgba(224,164,88,.12);border:1px solid rgba(224,164,88,.5);border-radius:999px;padding:.18rem .55rem}
        .rv-model{font-family:ui-monospace,monospace;font-size:.68rem;color:var(--lab-soft)}
        .rv-verdict{font-size:.83rem;color:var(--lab-ink);line-height:1.5;margin:0 0 .6rem}
        .rv-risks{list-style:none;margin:0 0 .6rem;padding:0;display:flex;flex-direction:column;gap:.4rem}
        .rv-risks li{font-size:.78rem;color:var(--lab-soft);line-height:1.5}
        .rv-risks b{color:var(--lab-ink);font-weight:600}
        .rv-x{color:#f47272;font-family:ui-monospace,monospace}
        .rv-next{font-size:.78rem;color:var(--lab-soft);line-height:1.5;margin:0;border-top:1px solid var(--lab-line);padding-top:.55rem}
        .rv-next b,.rv-verdict b{color:var(--lab-ink)}
        .bh-top{display:flex;align-items:baseline;gap:.7rem;margin:.2rem 0 .8rem;flex-wrap:wrap}
        .bh-big{font-family:ui-monospace,monospace;font-size:2.4rem;font-weight:700;line-height:1;background:linear-gradient(120deg,var(--lab-accent),var(--lab-accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
        .bh-biglab{font-size:.75rem;color:var(--lab-soft);line-height:1.45}
        .bh-meterrow{display:grid;grid-template-columns:auto 1fr auto;gap:.6rem;align-items:center;margin:0 0 .85rem}
        .bh-mlab{font-family:ui-monospace,monospace;font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;color:var(--lab-soft)}
        .bh-meter{height:5px;border-radius:3px;background:#1a1f30;overflow:hidden}
        .bh-meter i{display:block;height:100%;min-width:2px;background:#f47272}
        .bh-pct{font-family:ui-monospace,monospace;font-size:.7rem;color:#f47272}
        .bh-chips{display:flex;gap:.5rem;flex-wrap:wrap}
        .bh-chip{font-family:ui-monospace,monospace;font-size:.7rem;color:var(--lab-soft);border:1px solid var(--lab-line);border-radius:999px;padding:.25rem .6rem}
        .bh-chip.amber{color:#e0a458;border-color:rgba(224,164,88,.5)}
        .bh-chip.coral{color:#f47272;border-color:rgba(244,114,114,.5)}
        .pb-ladder ul{list-style:none;margin:.1rem 0 0;padding:0;display:flex;flex-direction:column;gap:.5rem}
        .pb-ladder li{display:flex;align-items:center;gap:.6rem;font-size:.85rem;line-height:1.4}
        .pb-ic{width:1.15rem;height:1.15rem;flex-shrink:0;border-radius:50%;display:grid;place-items:center;font-size:.7rem;font-family:ui-monospace,monospace}
        .pb-ladder li.pass{color:var(--lab-ink)}
        .pb-ladder li.pass .pb-ic{color:var(--lab-accent2);border:1px solid rgba(74,214,196,.55)}
        .pb-ladder li.fail{color:var(--lab-soft)}
        .pb-ladder li.fail .pb-ic{color:#f47272;border:1px solid rgba(244,114,114,.55)}
        .pb-div{display:flex;align-items:center;font-family:ui-monospace,monospace;font-size:.6rem;letter-spacing:.08em;text-transform:uppercase;color:var(--lab-soft)}
        .pb-div span{padding-right:.6rem;white-space:nowrap}
        .pb-div::after{content:"";flex:1;height:1px;background:var(--lab-line)}
        .pb-foot{font-size:.78rem;color:#f47272;margin:.75rem 0 0;font-weight:500}
        .fs-card{display:block;text-decoration:none;border:1px solid rgba(124,134,255,.4);border-radius:11px;background:linear-gradient(90deg,rgba(124,134,255,.08),rgba(74,214,196,.05));padding:.85rem 1rem;transition:border-color .15s}
        .fs-card:hover{border-color:var(--lab-accent)}
        .fs-tag{display:inline-block;font-family:ui-monospace,monospace;font-size:.58rem;letter-spacing:.05em;text-transform:uppercase;color:#f47272;background:rgba(244,114,114,.14);border:1px solid rgba(244,114,114,.5);border-radius:999px;padding:.2rem .55rem;margin-bottom:.5rem}
        .fs-title{display:block;font-size:1rem;color:var(--lab-ink);font-weight:650;line-height:1.3;margin-bottom:.3rem}
        .fs-line{font-size:.82rem;color:var(--lab-soft);line-height:1.5;margin:0 0 .5rem}
        .fs-line b{color:var(--lab-ink);font-weight:600}
        .fs-meta{display:block;font-family:ui-monospace,monospace;font-size:.66rem;color:var(--lab-accent2);margin-bottom:.6rem}
        .fs-cta{display:inline-block;font-size:.82rem;font-weight:600;color:var(--lab-accent2);border:1px solid rgba(74,214,196,.45);border-radius:8px;padding:.4rem .75rem}
        .pt-tracks{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}
        @media(max-width:560px){.pt-tracks{grid-template-columns:1fr}}
        .pt-track{text-align:left;font:inherit;cursor:pointer;display:flex;flex-direction:column;gap:.3rem;border:1px solid rgba(124,134,255,.4);border-radius:11px;background:linear-gradient(135deg,rgba(124,134,255,.09),rgba(74,214,196,.05));padding:.85rem 1rem;transition:border-color .15s}
        .pt-track:hover{border-color:var(--lab-accent)}
        .pt-track b{font-size:.95rem;color:var(--lab-ink);font-weight:650}
        .pt-track span{font-size:.8rem;color:var(--lab-soft);line-height:1.5}
      `}</style>

      <div className="cfg-panel" role="tabpanel">
        <p className="cfg-panel-h">{STEPS.find((s) => s.key === tab)?.heading}</p>

        {tab === "topic" && (() => {
          const step = itemsFor("topic").find((i) => i.value === sub) || itemsFor("topic")[0];
          return (
          <div>
            {sub === "" ? (
              <>
            <div className="cfg-pipe">
              {METHOD_STEPS.map((s, i) => (
                <span key={i}>{i > 0 && <em>→</em>}{s}</span>
              ))}
            </div>
            <p className="cfg-credit">
              Method after <a href="https://github.com/star4citizen/Astro-NoteAI" target="_blank" rel="noopener noreferrer">Astro-Note&nbsp;AI</a> (Suk&nbsp;Kim) — turning a body of papers into a navigable, machine-read map of a field.
            </p>
            <div className="cfg-viz">
              <DerivationDiagram />
              <p className="cap">
                120,676 papers → embedded into vectors → self-organized clusters → ranked by open-question
                density × growth. The top science frontiers (lit) become the research topics.
              </p>
            </div>
              <p className="cfg-ov">From 120,676 papers to a ranked map of the field&rsquo;s open questions — no hand-picking. Use the <b>Topic</b> menu above to walk each step; the fifth reveals the ranked frontier map. <b>The map below is being re-derived on the newly expanded corpus.</b></p>
              </>
            ) : (<>
            <div className="cfg-sub">
              <div className="cfg-sub-h">{step.label}<span>{step.sub}</span></div>
              <div className="cfg-sub-desc">{step.desc}</div>
            </div>
            {step.value === "corpus" && <CorpusView />}
            {step.value === "embedding" && <EmbeddingView />}
            {step.value === "clustering" && <ClusteringView />}
            {step.value === "overlay" && <OverlayView />}
            {step.value === "ranking" && <RankingView />}
            <SubnavVideo step={step.value} />
            </>)}
          </div>
          );
        })()}

        {(tab === "data" || tab === "research" || tab === "paper") && (() => {
          if (sub === "") {
            if (tab === "data") return <DataView />;
            if (tab === "research") return <ResearchView />;
            return <PaperView />;
          }
          const items = itemsFor(tab);
          const active = items.find((i) => i.value === sub) || items[0];
          return (
            <div className="cfg-sub">
              <div className="cfg-sub-h">{active.label}<span>{active.sub}</span></div>
              {active.desc && <div className="cfg-sub-desc">{active.desc}</div>}
              {(active.rows || []).map(([k, v]) => (
                <div className="cfg-sub-row" key={k}>
                  <span className="cfg-sub-k">{k}</span><span className="cfg-sub-v">{v}</span>
                </div>
              ))}
              {tab === "paper" && sub === "flagship" && (
                <div style={{ padding: ".2rem .9rem 1rem" }}><FlagshipStudies /></div>
              )}
              {tab === "paper" && sub === "pipeline" && (
                <div style={{ padding: ".2rem .9rem 1rem" }}><PipelineBoard /></div>
              )}
            </div>
          );
        })()}

        {tab !== "paper" && (
          <button className="cfg-next" onClick={goNext}>Next →</button>
        )}
      </div>
    </div>
  );
}
