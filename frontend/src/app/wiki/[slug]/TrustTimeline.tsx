"use client";
import { useState } from "react";
import { emptyTrustHistoryText, formatHiddenRecomputes, formatTrustScoreChange } from "./trustHistoryCopy";

interface TimelineEvent {
  kind: string;
  icon: string;
  color: string;
  started_at: string;
  ended_at: string;
  level_before: string | null;
  level_after: string;
  score_before: number | null;
  score_after: number;
  score_delta: number | null;
  summary: string;
  detail: string | null;
  raw_count: number;
}

interface TrustHistory {
  claim_id: number;
  current: { trust_level: string; trust_score: number; claim_text: string };
  events: TimelineEvent[];
  stats: { total_raw_rows: number; events_returned: number; noise_filtered: number };
}

const COLOR_MAP: Record<string, { bg: string; text: string; dot: string }> = {
  gray:   { bg: "rgba(100,116,139,0.1)", text: "#64748b", dot: "#64748b" },
  blue:   { bg: "rgba(59,130,246,0.1)",  text: "#3b82f6", dot: "#3b82f6" },
  purple: { bg: "rgba(168,85,247,0.1)",  text: "#a855f7", dot: "#a855f7" },
  gold:   { bg: "rgba(234,179,8,0.1)",   text: "#ca8a04", dot: "#eab308" },
  orange: { bg: "rgba(249,115,22,0.1)",  text: "#ea580c", dot: "#f97316" },
  brown:  { bg: "rgba(120,53,15,0.1)",   text: "#92400e", dot: "#b45309" },
};

const TRUST_COLOR: Record<string, string> = {
  consensus: "#22c55e", accepted: "#94a3b8", debated: "#f97316",
  challenged: "#ef4444", unverified: "#475569",
};

function fmtDate(iso: string) {
  const d = new Date(iso);
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
}

export default function TrustTimeline({ claimId }: { claimId: number }) {
  const [open, setOpen] = useState(false);
  const [history, setHistory] = useState<TrustHistory | null>(null);
  const [loading, setLoading] = useState(false);

  const load = async () => {
    if (history) { setOpen(!open); return; }
    setLoading(true);
    try {
      const r = await fetch(`/api/claims/${claimId}/trust-history?limit=25`);
      const d = await r.json();
      setHistory(d);
      setOpen(true);
    } catch {}
    setLoading(false);
  };

  return (
    <span style={{ display: "inline-block" }}>
      <button
        onClick={(e) => { e.stopPropagation(); load(); }}
        style={{ background: "none", border: "none", cursor: "pointer",
          fontSize: "0.72rem", color: "#64748b", padding: "0 2px" }}
        title="View trust history"
      >
        {loading ? "⏳" : "🕒"}
      </button>

      {open && history && (
        <div
          onClick={(e) => e.stopPropagation()}
          style={{
            position: "absolute", left: 0, top: "100%", zIndex: 60,
            background: "#0f172a", border: "1px solid #334155",
            borderRadius: "10px", padding: "1rem", width: "min(28rem, 90vw)",
            boxShadow: "0 8px 32px rgba(0,0,0,0.4)", marginTop: "4px",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "0.75rem" }}>
            <span style={{ fontWeight: 600, color: "#f8fafc", fontSize: "0.82rem" }}>
              📜 Trust History
            </span>
            <div style={{ display: "flex", gap: "0.5rem", alignItems: "center" }}>
              <span style={{ fontSize: "0.7rem", color: "#475569" }}>
                {formatHiddenRecomputes(history.stats.noise_filtered)}
              </span>
              <button onClick={() => setOpen(false)}
                style={{ background: "none", border: "none", color: "#475569", cursor: "pointer", fontSize: "0.9rem" }}>✕</button>
            </div>
          </div>

          {/* Current state */}
          <div style={{ background: "#1e293b", borderRadius: "6px", padding: "0.5rem 0.75rem",
            marginBottom: "0.75rem", display: "flex", alignItems: "center", gap: "0.5rem" }}>
            <span style={{ fontSize: "0.75rem", color: "#64748b" }}>Now:</span>
            <span style={{ fontSize: "0.8rem", fontWeight: 700,
              color: TRUST_COLOR[history.current.trust_level] || "#f8fafc" }}>
              {history.current.trust_level}
            </span>
            <span style={{ fontSize: "0.72rem", color: "#64748b" }}>
              (TS={history.current.trust_score.toFixed(3)})
            </span>
          </div>

          {/* Events */}
          {history.events.length === 0 ? (
            <p style={{ color: "#475569", fontSize: "0.8rem" }}>{emptyTrustHistoryText}</p>
          ) : (
            <div style={{ display: "flex", flexDirection: "column", gap: 0 }}>
              {history.events.map((ev, i) => {
                const c = COLOR_MAP[ev.color] || COLOR_MAP.gray;
                const isLast = i === history.events.length - 1;
                const scoreChange = formatTrustScoreChange(ev);
                return (
                  <div key={i} style={{ display: "flex", gap: "0.75rem" }}>
                    {/* Dot + line */}
                    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", flexShrink: 0 }}>
                      <div style={{ width: "10px", height: "10px", borderRadius: "50%",
                        background: c.dot, flexShrink: 0, marginTop: "4px" }} />
                      {!isLast && <div style={{ width: "1px", flex: 1, background: "#1e293b",
                        minHeight: "20px", marginTop: "2px" }} />}
                    </div>
                    {/* Content */}
                    <div style={{ paddingBottom: isLast ? 0 : "0.75rem", flex: 1 }}>
                      <div style={{ display: "flex", alignItems: "baseline", gap: "0.4rem", flexWrap: "wrap" }}>
                        <span style={{ fontSize: "0.75rem" }}>{ev.icon}</span>
                        <span style={{ fontSize: "0.78rem", color: "#f8fafc", fontWeight: 500 }}>{ev.summary}</span>
                        {ev.level_before && ev.level_after && ev.level_before !== ev.level_after && (
                          <span style={{ fontSize: "0.68rem", padding: "1px 5px", borderRadius: "99px",
                            background: c.bg, color: c.text }}>
                            {ev.level_before} → {ev.level_after}
                          </span>
                        )}
                      </div>
                      {scoreChange && (
                        <div style={{ fontSize: "0.7rem", color: "#64748b", marginTop: "2px" }}>{scoreChange}</div>
                      )}
                      <div style={{ fontSize: "0.67rem", color: "#334155", marginTop: "2px" }}>
                        {fmtDate(ev.started_at)}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}
    </span>
  );
}
