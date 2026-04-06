"use client";
import { useState } from "react";

interface ClaimData {
  id: number;
  text: string;
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
      {claim.text}{" "}
      <button
        onClick={openPanel}
        className="inline-flex items-center text-xs text-gray-400 hover:text-indigo-600 ml-0.5"
        title={`${TRUST_LABELS[claim.trust_level]} · ${claim.evidence_count} source(s)`}
      >
        📄{claim.evidence_count > 0 ? claim.evidence_count : ""}
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
    </span>
  );
}
