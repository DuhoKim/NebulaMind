"use client";
import { useState } from "react";

interface ClaimData {
  id: number;
  text: string;
  connector?: string | null;
  trust_level: string;
  evidence_count: number;
  section: string;
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
}

const TRUST_STYLES: Record<string, string> = {
  consensus: "bg-green-50 border-l-2 border-green-400",
  accepted: "bg-blue-50 border-l-2 border-blue-300",
  debated: "bg-orange-50 border-l-2 border-orange-400",
  challenged: "bg-red-50 border-l-2 border-red-400",
  unverified: "bg-gray-50",
};

const TRUST_LABELS: Record<string, string> = {
  consensus: "🟢 Consensus",
  accepted: "✅ Accepted",
  debated: "🟠 Debated",
  challenged: "🔴 Challenged",
  unverified: "⬜ Unverified",
};

const STANCE_ICON: Record<string, string> = {
  supports: "✅",
  challenges: "❌",
  neutral: "➖",
};

export default function ClaimBlock({ claim, showColors }: { claim: ClaimData; showColors: boolean }) {
  const [open, setOpen] = useState(false);
  const [evidence, setEvidence] = useState<EvidenceItem[] | null>(null);
  const [loading, setLoading] = useState(false);

  // Edit proposal state
  const [showEditModal, setShowEditModal] = useState(false);
  const [editText, setEditText] = useState(claim.text);
  const [arxivId, setArxivId] = useState("");
  const [evidenceSummary, setEvidenceSummary] = useState("");
  const [editEmail, setEditEmail] = useState("");
  const [editSubmitting, setEditSubmitting] = useState(false);
  const [editSubmitted, setEditSubmitted] = useState(false);

  const openPanel = async () => {
    if (!open && evidence === null) {
      setLoading(true);
      try {
        const res = await fetch(`/api/claims/${claim.id}/evidence`);
        const data = await res.json();
        setEvidence(data.evidence || []);
      } catch {
        setEvidence([]);
      }
      setLoading(false);
    }
    setOpen(!open);
  };

  const style = showColors ? TRUST_STYLES[claim.trust_level] || "" : "";

  return (
    <span className={`${style} rounded px-0.5 py-0.5 transition-colors relative`}>
      {claim.connector ? <span className="text-gray-500 italic">{claim.connector} </span> : null}{claim.text}{" "}
      <button
        onClick={openPanel}
        className="inline-flex items-center text-xs text-gray-400 hover:text-indigo-600 ml-0.5"
        title={`${TRUST_LABELS[claim.trust_level]} · ${claim.evidence_count} source(s)`}
      >
        📄{claim.evidence_count > 0 ? claim.evidence_count : ""}
      </button>
      <button
        onClick={(e) => { e.stopPropagation(); setShowEditModal(true); }}
        className="inline-flex items-center text-xs text-gray-400 hover:text-yellow-500 ml-0.5"
        title="Suggest an edit with arXiv evidence"
      >
        ✏️
      </button>

      {open && (
        <span
          className="absolute left-0 top-full mt-1 z-50 bg-white border border-gray-200 rounded-xl shadow-xl p-4 w-96 text-sm text-left"
          style={{ display: "block" }}
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
                  {ev.summary && <p className="text-xs text-gray-500 mt-1 leading-relaxed">{ev.summary}</p>}
                  <div className="flex gap-2 mt-1 text-xs text-gray-400">
                    <span>👍 {ev.votes_agree}</span>
                    <span>👎 {ev.votes_disagree}</span>
                    <span>💬 {ev.comments_count}</span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </span>
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
