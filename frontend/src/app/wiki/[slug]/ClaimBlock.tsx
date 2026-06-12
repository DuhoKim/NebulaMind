"use client";
import TrustTimeline from "./TrustTimeline";
import { useState, useEffect } from "react";

interface ClaimData {
  id: number;
  text: string;
  connector?: string | null;
  trust_level: string;
  evidence_count: number;
  con_count?: number;
  section: string;
  has_escalation?: boolean;
}


interface IdeaSummary {
  id: number;
  question: string;
  survey_combo: string;
  novelty: number;
  feasibility: number;
  well_posed_score?: number | null;
  saved_by_papa?: boolean;
  gap_type?: string | null;
}

interface ElementLink {
  element_id: string;
  element_text_snapshot: string | null;
}

interface EvidenceItem {
  id: number;
  title: string;
  arxiv_id: string | null;
  url: string | null;
  authors: string | null;
  year: number | null;
  summary: string | null;
  stance: string;
  votes_agree: number;
  votes_disagree: number;
  comments_count: number;
  element_links: ElementLink[];
  link_count: number;
  relevance?: number | null;
  entailment?: number | null;
  rigor?: number | null;
  confidence?: number | null;
  quality_v2?: number | null;
}

const GAP_TYPE_COLORS: Record<string, { bg: string; text: string }> = {
  gap:      { bg: "rgba(239,68,68,0.15)",   text: "#f87171" },
  tension:  { bg: "rgba(245,158,11,0.15)",  text: "#fbbf24" },
  bridge:   { bg: "rgba(16,185,129,0.15)",  text: "#34d399" },
  frontier: { bg: "rgba(99,102,241,0.15)",  text: "#818cf8" },
  synergy:  { bg: "rgba(14,165,233,0.15)",  text: "#38bdf8" },
};

function GapTypeChip({ gapType }: { gapType: string }) {
  const colors = GAP_TYPE_COLORS[gapType] ?? { bg: "rgba(100,116,139,0.15)", text: "#94a3b8" };
  return (
    <span style={{
      fontSize: "0.65rem", fontWeight: 600, letterSpacing: "0.02em",
      color: colors.text, background: colors.bg,
      padding: "1px 5px", borderRadius: "4px", textTransform: "uppercase",
    }}>
      {gapType}
    </span>
  );
}

const IDEA_Q_MAX = 100;

function IdeaQuestion({ text }: { text: string }) {
  const [expanded, setExpanded] = useState(false);
  if (!text) return null;
  if (text.length <= IDEA_Q_MAX) {
    return <p style={{ margin: 0, fontSize: "0.8rem", color: "#cbd5e1", lineHeight: 1.5 }}>{text}</p>;
  }
  return (
    <p style={{ margin: 0, fontSize: "0.8rem", color: "#cbd5e1", lineHeight: 1.5 }}>
      {expanded ? text : text.slice(0, IDEA_Q_MAX) + "…"}
      <button
        onClick={(e) => { e.stopPropagation(); setExpanded(!expanded); }}
        style={{ background: "none", border: "none", color: "#818cf8", cursor: "pointer", fontSize: "0.72rem", padding: "0 0.2rem", marginLeft: "0.2rem" }}
      >
        {expanded ? "less" : "more"}
      </button>
    </p>
  );
}

const TRUST_STYLES: Record<string, string> = {
  consensus:  "border-l-4 border-green-400 bg-green-900/30",
  accepted:   "border-l-4 border-blue-400 bg-blue-900/30",
  debated:    "border-l-4 border-orange-400 bg-orange-900/35",
  challenged: "border-l-4 border-red-500 bg-red-900/40",
  unverified: "border-l-2 border-gray-600 bg-gray-800/20",
};

const TRUST_LABELS: Record<string, string> = {
  consensus: "🟢 Consensus",
  accepted: "✅ Accepted",
  debated: "🟠 Debated",
  challenged: "🔴 Challenged",
  unverified: "⬜ Unverified",
};

const TRUST_BADGE: Record<string, { label: string; style: React.CSSProperties }> = {
  consensus: {
    label: "consensus",
    style: { background: "rgba(34,197,94,0.28)", color: "#4ade80", border: "1px solid rgba(34,197,94,0.65)", fontWeight: 700 },
  },
  accepted: {
    label: "accepted",
    style: { background: "rgba(59,130,246,0.25)", color: "#93c5fd", border: "1px solid rgba(59,130,246,0.6)", fontWeight: 700 },
  },
  debated: {
    label: "debated",
    style: { background: "rgba(249,115,22,0.28)", color: "#fb923c", border: "1px solid rgba(249,115,22,0.65)", fontWeight: 700 },
  },
  challenged: {
    label: "challenged",
    style: { background: "rgba(239,68,68,0.30)", color: "#f87171", border: "1px solid rgba(239,68,68,0.7)", fontWeight: 700 },
  },
};

const STANCE_ICON: Record<string, string> = {
  supports: "✅",
  challenges: "❌",
  neutral: "➖",
};

export default function ClaimBlock({ claim, showColors, ideas, showIdeas = false }: { claim: ClaimData; showColors: boolean; ideas?: IdeaSummary[]; showIdeas?: boolean }) {
  const [open, setOpen] = useState(false);
  const [evidence, setEvidence] = useState<EvidenceItem[] | null>(null);
  const [totalElements, setTotalElements] = useState(0);
  const [loading, setLoading] = useState(false);
  const [hoveredEvId, setHoveredEvId] = useState<number | null>(null);

  // Edit proposal state
  const [showEditModal, setShowEditModal] = useState(false);
  const [showOverrideModal, setShowOverrideModal] = useState(false);
  const [overrideLevel, setOverrideLevel] = useState(claim.trust_level);
  const [overrideReason, setOverrideReason] = useState("");
  const [overrideLocked, setOverrideLocked] = useState(true);
  const [overrideSubmitting, setOverrideSubmitting] = useState(false);
  const [overrideActive, setOverrideActive] = useState(false);
  const [overrideInfo, setOverrideInfo] = useState<any>(null);
  const [editText, setEditText] = useState(claim.text);
  const [arxivId, setArxivId] = useState("");
  const [evidenceSummary, setEvidenceSummary] = useState("");
  const [editEmail, setEditEmail] = useState("");
  const [editSubmitting, setEditSubmitting] = useState(false);
  const [editSubmitted, setEditSubmitted] = useState(false);
  const [ideasOpen, setIdeasOpen] = useState(false);

  const openPanel = async () => {
    if (!open && evidence === null) {
      setLoading(true);
      try {
        const res = await fetch(`/api/claims/${claim.id}/evidence`);
        const data = await res.json();
        setEvidence(data.evidence || []);
        setTotalElements(data.total_elements || 0);
      } catch {
        setEvidence([]);
        setTotalElements(0);
      }
      setLoading(false);
    }
    setOpen(!open);
  };

  const style = showColors ? TRUST_STYLES[claim.trust_level] || "" : "";

  return (
    <span className={`${style} rounded px-0.5 py-0.5 transition-colors relative`}>
      {claim.connector ? <span className="text-gray-500 italic">{claim.connector} </span> : null}{claim.text}{" "}
      {showColors && TRUST_BADGE[claim.trust_level] && (
        <span
          style={{
            ...TRUST_BADGE[claim.trust_level].style,
            display: "inline-flex",
            alignItems: "center",
            fontSize: "0.7rem",
            fontWeight: 700,
            letterSpacing: "0.04em",
            padding: "0.15rem 0.5rem",
            borderRadius: "999px",
            verticalAlign: "middle",
            marginLeft: "0.3rem",
            marginRight: "0.15rem",
            textTransform: "uppercase",
            cursor: "default",
            userSelect: "none",
          }}
          title={TRUST_LABELS[claim.trust_level]}
        >
          {TRUST_BADGE[claim.trust_level].label}
        </span>
      )}
      {claim.has_escalation && (
        <span
          style={{
            display: "inline-flex",
            alignItems: "center",
            fontSize: "0.65rem",
            fontWeight: 600,
            padding: "0.1rem 0.45rem",
            borderRadius: "999px",
            background: "rgba(59,130,246,0.15)",
            color: "#3b82f6",
            border: "1px solid rgba(59,130,246,0.3)",
            marginLeft: "0.3rem",
            cursor: "default",
            userSelect: "none",
          }}
          title="This claim is under council appeal"
        >
          🔵 Under appeal
        </span>
      )}
      <button
        onClick={openPanel}
        className="inline-flex items-center text-xs text-gray-400 hover:text-indigo-600 ml-0.5"
        title={`${TRUST_LABELS[claim.trust_level]} · ${claim.evidence_count} source(s)`}
      >
        📄{claim.evidence_count > 0 ? claim.evidence_count : ""}
      </button>
      {showIdeas && ideas && ideas.length > 0 && (() => {
        const isOpen = ['debated', 'challenged'].includes(claim.trust_level) || (claim.con_count ?? 0) >= 2;
        const chipStyle = isOpen
          ? { color: "#fbbf24", fontWeight: 700, background: "rgba(251,191,36,0.12)", borderRadius: "4px", padding: "1px 5px", border: "1px solid rgba(251,191,36,0.3)" }
          : { color: "#818cf8", fontWeight: 400, opacity: 0.6 };
        return (
        <>
          <button
            onClick={(e) => { e.stopPropagation(); setIdeasOpen(!ideasOpen); }}
            className="inline-flex items-center text-xs ml-0.5"
            style={chipStyle}
            title={isOpen
              ? `⚡ ${ideas.length} open research question${ideas.length > 1 ? "s" : ""} — this claim is actively debated`
              : `${ideas.length} research idea${ideas.length > 1 ? "s" : ""} linked to this claim`}
          >
            {isOpen ? "⚡" : "💡"} {ideas.length}
          </button>
          {ideasOpen && (
            <span
              style={{
                position: "absolute", left: 0, top: "100%", marginTop: "4px",
                zIndex: 60, background: "#1e293b", border: "1px solid #4f46e5",
                borderRadius: "8px", boxShadow: "0 8px 24px rgba(0,0,0,0.4)",
                padding: "0.75rem", width: "min(28rem, 92vw)", display: "block",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "0.5rem" }}>
                <span style={{ color: isOpen ? "#fbbf24" : "#818cf8", fontWeight: 600, fontSize: "0.8rem" }}>{isOpen ? "⚡ Open Research Questions" : "💡 Research Ideas"}</span>
                <button onClick={(e) => { e.stopPropagation(); setIdeasOpen(false); }} style={{ background: "none", border: "none", color: "#64748b", cursor: "pointer" }}>&#x2715;</button>
              </div>
              {ideas.map(idea => (
                <div key={idea.id} style={{ border: "1px solid #334155", borderRadius: "6px", padding: "0.6rem 0.75rem", marginBottom: "0.4rem", background: "#0f172a" }}>
                  <div style={{ display: "flex", gap: "0.5rem", alignItems: "center", marginBottom: "0.3rem", flexWrap: "wrap" }}>
                    <span style={{ fontSize: "0.7rem", fontWeight: 700, color: "#818cf8", background: "rgba(99,102,241,0.12)", padding: "1px 6px", borderRadius: "4px" }}>
                      {idea.survey_combo}
                    </span>
                    {idea.gap_type && <GapTypeChip gapType={idea.gap_type} />}
                    {idea.saved_by_papa && <span style={{ fontSize: "0.7rem", color: "#f59e0b" }}>★</span>}
                    <span style={{ marginLeft: "auto", fontSize: "0.68rem", color: "#475569" }}>
                      N:{Math.round((idea.novelty || 0) * 5)}/5 · F:{Math.round((idea.feasibility || 0) * 5)}/5
                      {idea.well_posed_score != null ? ` · W:${Math.round(idea.well_posed_score * 5)}/5` : ""}
                    </span>
                  </div>
                  <IdeaQuestion text={idea.question} />
                </div>
              ))}
            </span>
          )}
        </>
        );
      })()}
      <TrustTimeline claimId={claim.id} />
      <button
        onClick={(e) => { e.stopPropagation(); setShowEditModal(true); }}
        className="inline-flex items-center text-xs text-gray-400 hover:text-yellow-500 ml-0.5"
        title="Suggest an edit with arXiv evidence"
      >
        ✏️
      </button>
      {/* Researcher override button — only show if admin/researcher */}
      <button
        onClick={async (e) => {
          e.stopPropagation();
          // Check if override is active
          try {
            const r = await fetch(`/api/claims/${claim.id}/override-status`);
            const d = await r.json();
            setOverrideInfo(d);
            setOverrideActive(d.active);
            if (d.active) {
              setOverrideLevel(d.override_level || claim.trust_level);
              setOverrideReason(d.reason || "");
            }
          } catch {}
          setShowOverrideModal(true);
        }}
        className="inline-flex items-center text-xs text-gray-400 hover:text-purple-400 ml-0.5"
        title="Researcher: pin trust level"
        style={{ opacity: 0.5 }}
      >
        📌
      </button>

      {open && (
        <span
          className="absolute left-0 top-full mt-1 z-50 bg-white border border-gray-200 rounded-xl shadow-xl p-4 text-sm text-left"
          style={{ width: "min(24rem, 90vw)", maxWidth: "90vw", display: "block" }}
        >
          <div className="flex justify-between items-center mb-2">
            <span className="font-semibold text-gray-700">📎 Evidence</span>
            <span className="text-xs text-gray-400">{TRUST_LABELS[claim.trust_level]}</span>
            <button onClick={() => setOpen(false)} className="text-gray-400 hover:text-gray-600 ml-2">✕</button>
          </div>
          <p className="text-xs text-gray-500 mb-3 italic line-clamp-2">{claim.text}</p>

          {loading && <p className="text-gray-400 text-xs">Loading...</p>}

          {evidence && evidence.length === 0 && (
            <p className="text-gray-400 text-xs">No evidence linked yet.</p>
          )}

          {evidence && evidence.map(ev => (
            <div key={ev.id} className="border border-gray-100 rounded-lg p-2 mb-2 bg-gray-50">
              <div className="flex gap-1 items-start">
                <span className="text-sm">{STANCE_ICON[ev.stance]}</span>
                <div className="flex-1 min-w-0">
                  {ev.url ? (
                    <a href={ev.url} target="_blank" rel="noopener noreferrer" className="font-medium text-indigo-700 hover:underline text-xs leading-tight block">
                      {ev.title}
                    </a>
                  ) : (
                    <span className="font-medium text-gray-700 text-xs">{ev.title}</span>
                  )}
                  {ev.year && <span className="text-gray-400 text-xs ml-1">({ev.year})</span>}
                  {ev.element_links && ev.element_links.length > 0 && (
                    <div className="text-xs text-gray-500 mt-1">
                      supports: element {ev.link_count} of {totalElements}
                    </div>
                  )}
                  {ev.summary && <p className="text-xs text-gray-500 mt-1 leading-relaxed">{ev.summary}</p>}
                  <div className="flex gap-2 mt-1 text-xs text-gray-400 items-center justify-between">
                    <div className="flex gap-2">
                      <span>👍 {ev.votes_agree}</span>
                      <span>👎 {ev.votes_disagree}</span>
                      <span>💬 {ev.comments_count}</span>
                    </div>

                    {/* Scorecard Integration */}
                    {ev.quality_v2 !== undefined && ev.quality_v2 !== null ? (
                      <div className="relative">
                        <span
                          onMouseEnter={() => setHoveredEvId(ev.id)}
                          onMouseLeave={() => setHoveredEvId(null)}
                          style={{
                            fontSize: "0.68rem",
                            fontWeight: 700,
                            padding: "2px 6px",
                            borderRadius: "4px",
                            cursor: "help",
                            userSelect: "none",
                            background: ev.quality_v2 >= 0.8 
                              ? "rgba(16,185,129,0.15)" 
                              : ev.quality_v2 >= 0.5 
                                ? "rgba(245,158,11,0.15)" 
                                : "rgba(239,68,68,0.15)",
                            color: ev.quality_v2 >= 0.8 
                              ? "#10b981" 
                              : ev.quality_v2 >= 0.5 
                                ? "#fbbf24" 
                                : "#ef4444",
                            border: ev.quality_v2 >= 0.8 
                              ? "1px solid rgba(16,185,129,0.3)" 
                              : ev.quality_v2 >= 0.5 
                                ? "1px solid rgba(245,158,11,0.3)" 
                                : "1px solid rgba(239,68,68,0.3)",
                          }}
                        >
                          ⚖️ {Math.round(ev.quality_v2 * 100)}% Quality
                        </span>

                        {hoveredEvId === ev.id && (
                          <div
                            className="absolute right-0 bottom-full mb-2 bg-slate-900 border border-slate-700 text-slate-100 rounded-lg p-3 shadow-2xl z-50 text-left"
                            style={{ width: "200px" }}
                          >
                            <h4 className="text-xs font-bold text-white mb-2 border-b border-slate-700 pb-1 flex items-center justify-between">
                              <span>Trust Scorecard</span>
                              <span style={{ 
                                color: ev.quality_v2 >= 0.8 ? "#10b981" : ev.quality_v2 >= 0.5 ? "#fbbf24" : "#ef4444" 
                              }}>
                                {Math.round(ev.quality_v2 * 100)}%
                              </span>
                            </h4>
                            {[
                              { label: "Relevance", val: ev.relevance },
                              { label: "Factual Entailment", val: ev.entailment },
                              { label: "Methodological Rigor", val: ev.rigor },
                              { label: "Consensus/Confidence", val: ev.confidence }
                            ].map(({ label, val }) => {
                              const percent = Math.min(100, Math.max(0, Math.round((val ?? 0) * 100)));
                              return (
                                <div key={label} className="mb-2 last:mb-0">
                                  <div className="flex justify-between text-[10px] text-slate-400 font-medium">
                                    <span>{label}</span>
                                    <span>{percent}%</span>
                                  </div>
                                  <div className="w-full bg-slate-800 h-1 rounded-full overflow-hidden mt-0.5">
                                    <div 
                                      className="bg-indigo-500 h-full rounded-full transition-all duration-300" 
                                      style={{ width: `${percent}%` }}
                                    />
                                  </div>
                                </div>
                              );
                            })}
                          </div>
                        )}
                      </div>
                    ) : (
                      <span 
                        style={{
                          fontSize: "0.68rem",
                          fontWeight: 600,
                          padding: "2px 6px",
                          borderRadius: "4px",
                          background: "rgba(59,130,246,0.1)",
                          color: "#3b82f6",
                          border: "1px solid rgba(59,130,246,0.2)"
                        }}
                      >
                        ✓ Verified / Accepted
                      </span>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </span>
      )}

      {/* ── Researcher Trust Override Modal ── */}
      {showOverrideModal && (
        <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.8)", display: "flex", alignItems: "center", justifyContent: "center", zIndex: 2100 }} onClick={() => setShowOverrideModal(false)}>
          <div style={{ background: "#1e293b", border: "1px solid #475569", borderRadius: "8px", padding: "1.5rem", maxWidth: "480px", width: "90%" }} onClick={e => e.stopPropagation()}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "1rem" }}>
              <h3 style={{ margin: 0, color: "#f8fafc", fontWeight: 700 }}>📌 Researcher Trust Override</h3>
              <button onClick={() => setShowOverrideModal(false)} style={{ background: "none", border: "none", color: "#64748b", cursor: "pointer", fontSize: "1.1rem" }}>✕</button>
            </div>
            <p style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.75rem" }}>Pin this claim to a trust level, bypassing automated calculation.</p>

            {/* Override status banner */}
            {overrideActive && overrideInfo && (
              <div style={{ background: "rgba(168,85,247,0.1)", border: "1px solid rgba(168,85,247,0.3)", borderRadius: "6px", padding: "0.6rem 0.85rem", marginBottom: "0.75rem", fontSize: "0.78rem" }}>
                <strong style={{ color: "#a855f7" }}>Active override:</strong> <span style={{ color: "#d8b4fe" }}>{overrideInfo.override_level}</span>
                {overrideInfo.stale_reminder && (
                  <span style={{ color: "#fbbf24", marginLeft: "0.5rem" }}>⚠️ {overrideInfo.new_evidence_since_override} new evidence rows since override</span>
                )}
                {overrideInfo.expires_at && (
                  <div style={{ color: "#64748b", marginTop: "0.25rem" }}>Expires: {new Date(overrideInfo.expires_at).toLocaleDateString()}</div>
                )}
              </div>
            )}

            <div style={{ marginBottom: "0.75rem" }}>
              <label style={{ fontSize: "0.82rem", color: "#94a3b8", display: "block", marginBottom: "0.3rem" }}>Trust level</label>
              <select value={overrideLevel} onChange={e => setOverrideLevel(e.target.value)}
                style={{ width: "100%", padding: "0.4rem 0.75rem", background: "#0f172a", color: "#f8fafc", border: "1px solid #334155", borderRadius: "4px" }}>
                {["consensus","accepted","debated","challenged","unverified"].map(l => (
                  <option key={l} value={l}>{l}</option>
                ))}
              </select>
            </div>
            <textarea value={overrideReason} onChange={e => setOverrideReason(e.target.value)}
              placeholder="Reason for override (required, min 5 chars)..."
              style={{ width: "100%", minHeight: "70px", padding: "0.5rem", background: "#0f172a", color: "#f8fafc", border: "1px solid #334155", borderRadius: "4px", fontFamily: "inherit", marginBottom: "0.75rem", boxSizing: "border-box", resize: "vertical" }} />
            <label style={{ display: "flex", alignItems: "center", gap: "0.5rem", fontSize: "0.82rem", color: "#94a3b8", marginBottom: "1rem", cursor: "pointer" }}>
              <input type="checkbox" checked={overrideLocked} onChange={e => setOverrideLocked(e.target.checked)} />
              Lock (prevent automated recalculation)
            </label>
            <div style={{ display: "flex", gap: "0.5rem", justifyContent: "flex-end" }}>
              {overrideActive && (
                <button
                  onClick={async () => {
                    await fetch(`/api/claims/${claim.id}/trust-override`, { method: "DELETE" });
                    setOverrideActive(false);
                    setShowOverrideModal(false);
                  }}
                  style={{ padding: "0.4rem 0.85rem", background: "transparent", color: "#ef4444", border: "1px solid #ef4444", borderRadius: "4px", cursor: "pointer", fontSize: "0.85rem" }}>
                  Remove override
                </button>
              )}
              <button onClick={() => setShowOverrideModal(false)}
                style={{ padding: "0.4rem 0.85rem", background: "transparent", color: "#64748b", border: "1px solid #334155", borderRadius: "4px", cursor: "pointer" }}>Cancel</button>
              <button
                disabled={overrideSubmitting || overrideReason.trim().length < 5}
                onClick={async () => {
                  setOverrideSubmitting(true);
                  try {
                    await fetch(`/api/claims/${claim.id}/trust-override`, {
                      method: "PATCH",
                      headers: { "Content-Type": "application/json" },
                      body: JSON.stringify({ trust_level: overrideLevel, reason: overrideReason, locked: overrideLocked }),
                    });
                    setOverrideActive(true);
                    setShowOverrideModal(false);
                  } catch {} finally { setOverrideSubmitting(false); }
                }}
                style={{ padding: "0.4rem 0.85rem", background: "#6366f1", color: "#fff", border: "none", borderRadius: "4px", cursor: "pointer", opacity: overrideReason.trim().length < 5 ? 0.5 : 1 }}>
                {overrideSubmitting ? "Saving..." : overrideActive ? "Update override" : "Set override"}
              </button>
            </div>
          </div>
        </div>
      )}

      {showEditModal && (
        <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.75)", display: "flex", alignItems: "center", justifyContent: "center", zIndex: 2000 }} onClick={() => setShowEditModal(false)}>
          <div style={{ background: "#1e293b", borderRadius: "4px", padding: "1.5rem", maxWidth: "560px", width: "90%", boxShadow: "0 25px 60px rgba(0,0,0,0.3)" }} onClick={e => e.stopPropagation()}>
            {editSubmitted ? (
              <div style={{ textAlign: "center", padding: "1.5rem" }}>
                <h3 style={{ margin: "0 0 0.5rem", fontSize: "1rem", fontWeight: 700, color: "#f8fafc" }}>Proposal submitted</h3>
                <p style={{ color: "#94a3b8", fontSize: "0.85rem", marginBottom: "1rem" }}>Three votes required to apply this change.</p>
                <button onClick={() => { setShowEditModal(false); setEditSubmitted(false); }}
                  style={{ padding: "0.4rem 1rem", background: "#6366f1", color: "#f8fafc", border: "none", borderRadius: "4px", cursor: "pointer", fontSize: "0.88rem" }}>Close</button>
              </div>
            ) : (
              <>
                <h3 style={{ margin: "0 0 0.75rem", fontSize: "1rem", fontWeight: 700, color: "#f8fafc" }}>Edit Proposal</h3>
                <p style={{ margin: "0 0 0.75rem", fontSize: "0.8rem", color: "#94a3b8" }}>No account required. A published paper citation is mandatory.</p>
                <div style={{ background: "#0f172a", borderRadius: "4px", padding: "0.75rem", marginBottom: "0.75rem", border: "1px solid #334155" }}>
                  <p style={{ margin: 0, fontSize: "0.72rem", color: "#64748b", marginBottom: "0.25rem", textTransform: "uppercase", letterSpacing: "0.05em" }}>Original claim:</p>
                  <p style={{ margin: 0, fontSize: "0.85rem", color: "#94a3b8", lineHeight: 1.5 }}>{claim.text}</p>
                </div>
                <textarea value={editText} onChange={e => setEditText(e.target.value)}
                  style={{ width: "100%", minHeight: "80px", padding: "0.5rem 0.75rem", border: "1px solid #334155", borderRadius: "4px", marginBottom: "0.75rem", boxSizing: "border-box", fontFamily: "inherit", fontSize: "0.88rem", resize: "vertical", background: "#0f172a", color: "#f8fafc" }}
                  placeholder="Your improved version of this sentence..." />
                <div style={{ marginBottom: "0.75rem" }}>
                  <label style={{ fontSize: "0.82rem", fontWeight: 700, display: "block", marginBottom: "0.3rem" }}>
                    arXiv ID <span style={{ color: "#ef4444", fontWeight: 400 }}>*</span>
                  </label>
                  <input type="text" value={arxivId} onChange={e => setArxivId(e.target.value)}
                    placeholder="e.g. 2301.12345"
                    style={{ width: "100%", padding: "0.4rem 0.75rem", border: arxivId ? "1px solid #334155" : "1px solid #ef4444", borderRadius: "4px", background: "#0f172a", color: "#f8fafc", boxSizing: "border-box", fontSize: "0.88rem" }} />
                  <p style={{ margin: "0.2rem 0 0", fontSize: "0.73rem", color: "#64748b" }}>
                    Find papers at <a href="https://arxiv.org" target="_blank" rel="noopener noreferrer" style={{ color: "#4f46e5" }}>arxiv.org</a>
                  </p>
                </div>
                <textarea value={evidenceSummary} onChange={e => setEvidenceSummary(e.target.value)}
                  placeholder="How does this paper support your edit? (optional)"
                  style={{ width: "100%", minHeight: "60px", padding: "0.4rem 0.75rem", border: "1px solid #334155", borderRadius: "4px", marginBottom: "0.5rem", boxSizing: "border-box", fontFamily: "inherit", fontSize: "0.85rem", resize: "vertical", background: "#0f172a", color: "#f8fafc" }} />
                <input type="email" value={editEmail} onChange={e => setEditEmail(e.target.value)}
                  placeholder="Email for updates (optional)"
                  style={{ width: "100%", padding: "0.4rem 0.75rem", border: "1px solid #334155", borderRadius: "4px", marginBottom: "1rem", boxSizing: "border-box", fontSize: "0.85rem", background: "#0f172a", color: "#f8fafc" }} />
                <div style={{ display: "flex", gap: "0.5rem", justifyContent: "flex-end" }}>
                  <button onClick={() => setShowEditModal(false)}
                    style={{ padding: "0.4rem 0.85rem", border: "1px solid #334155", background: "transparent", color: "#94a3b8", borderRadius: "4px", cursor: "pointer", fontSize: "0.88rem" }}>Cancel</button>
                  <button
                    onClick={async () => {
                      if (!editText.trim() || !arxivId.trim()) return;
                      setEditSubmitting(true);
                      try {
                        await fetch(`/api/claims/${claim.id}/suggest-edit`, {
                          method: "POST",
                          headers: { "Content-Type": "application/json" },
                          body: JSON.stringify({ new_text: editText, arxiv_evidence: arxivId, evidence_summary: evidenceSummary || null, email: editEmail || null }),
                        });
                        setEditSubmitted(true);
                      } catch { setEditSubmitted(true); }
                      setEditSubmitting(false);
                    }}
                    disabled={editSubmitting || !editText.trim() || !arxivId.trim()}
                    style={{ padding: "0.4rem 1rem", background: "#6366f1", color: "#f8fafc", border: "none", borderRadius: "4px", cursor: "pointer", fontWeight: 600, opacity: (editText.trim() && arxivId.trim()) ? 1 : 0.5, fontSize: "0.88rem" }}>
                    {editSubmitting ? "Submitting..." : "Submit Edit Proposal"}
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      )}
    </span>
  );
}
