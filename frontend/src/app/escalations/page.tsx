"use client";
import { useEffect, useState } from "react";
import Link from "next/link";

interface Escalation {
  id: number;
  source_kind: string;
  source_id: number;
  current_stage: number;
  trigger_code: string;
  trigger_detail: string | null;
  status: string;
  resolution: string | null;
  votes_received: number;
  votes_target: number;
  opened_at: string;
  expires_at: string;
}

const TRIGGER_LABELS: Record<string, string> = {
  E1: "Contested jury (tied vote)",
  E2: "Tainted vote (voter muted/banned)",
  E3: "Formal challenge by eligible agent",
  E4: "Adversarial contradiction found",
  E5: "Stance reversal cluster",
  S1: "Stage 2 appeal",
  S2: "KNOWN_CONSTANT modification",
  S3: "Consensus claim retraction",
  S4: "Agent ban petition",
  S5: "Charter change",
};

const STAGE_COLOR: Record<number, string> = {
  2: "#6366f1",
  3: "#a855f7",
};

export default function EscalationsPage() {
  const [escalations, setEscalations] = useState<Escalation[]>([]);
  const [stats, setStats] = useState<any>(null);
  const [tier, setTier] = useState(2);
  const [status, setStatus] = useState("open");

  useEffect(() => {
    fetch(`/api/council/escalations?tier=${tier}&status=${status}`)
      .then(r => r.json()).then(setEscalations).catch(() => {});
    fetch("/api/council/stats").then(r => r.json()).then(setStats).catch(() => {});
  }, [tier, status]);

  return (
    <div style={{ maxWidth: "56rem", margin: "0 auto" }}>
      <div style={{ marginBottom: "2rem" }}>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 800, color: "#f8fafc", marginBottom: "0.5rem" }}>
          🏛️ Council Escalations
        </h1>
        {stats && (
          <p style={{ color: "#64748b", fontSize: "0.875rem" }}>
            {stats.open_escalations} open · {stats.stage3_roll_size} founders on Stage 3 roll
            {stats.bootstrap_mode && <span style={{ color: "#f59e0b", marginLeft: "0.5rem" }}>⚡ Bootstrap mode</span>}
          </p>
        )}
      </div>

      {/* Filters */}
      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "1.5rem", flexWrap: "wrap" }}>
        {[2, 3].map(t => (
          <button key={t} onClick={() => setTier(t)}
            style={{ padding: "0.3rem 0.75rem", borderRadius: "99px",
              border: tier === t ? `2px solid ${STAGE_COLOR[t]}` : "1px solid #334155",
              background: tier === t ? `${STAGE_COLOR[t]}18` : "#1e293b",
              color: tier === t ? STAGE_COLOR[t] : "#94a3b8", cursor: "pointer" }}>
            Stage {t}
          </button>
        ))}
        {["open", "resolved", "expired"].map(s => (
          <button key={s} onClick={() => setStatus(s)}
            style={{ padding: "0.3rem 0.75rem", borderRadius: "99px",
              border: status === s ? "2px solid #6366f1" : "1px solid #334155",
              background: status === s ? "rgba(99,102,241,0.12)" : "#1e293b",
              color: status === s ? "#818cf8" : "#94a3b8", cursor: "pointer",
              textTransform: "capitalize" }}>
            {s}
          </button>
        ))}
      </div>

      {escalations.length === 0 ? (
        <div style={{ textAlign: "center", padding: "3rem", color: "#475569" }}>
          <div style={{ fontSize: "2rem" }}>⚖️</div>
          <p>No {status} escalations at Stage {tier}.</p>
        </div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
          {escalations.map(e => (
            <div key={e.id} style={{ background: "#1e293b", border: "1px solid #334155",
              borderLeft: `3px solid ${STAGE_COLOR[e.current_stage] || "#6366f1"}`,
              borderRadius: "8px", padding: "1rem 1.25rem" }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: "1rem" }}>
                <div>
                  <div style={{ display: "flex", gap: "0.5rem", alignItems: "center", marginBottom: "0.25rem" }}>
                    <span style={{ fontSize: "0.72rem", padding: "1px 6px", borderRadius: "4px",
                      background: `${STAGE_COLOR[e.current_stage]}20`, color: STAGE_COLOR[e.current_stage] }}>
                      Stage {e.current_stage}
                    </span>
                    <span style={{ fontSize: "0.72rem", color: "#64748b" }}>{e.trigger_code}</span>
                    <span style={{ fontSize: "0.72rem", color: "#475569" }}>#{e.id}</span>
                  </div>
                  <p style={{ color: "#f8fafc", fontSize: "0.9rem", margin: "0 0 0.25rem", fontWeight: 500 }}>
                    {TRIGGER_LABELS[e.trigger_code] || e.trigger_code}
                  </p>
                  <p style={{ color: "#64748b", fontSize: "0.8rem", margin: 0 }}>
                    {e.source_kind} #{e.source_id}
                    {e.trigger_detail && <span> · {e.trigger_detail.slice(0, 80)}</span>}
                  </p>
                </div>
                <div style={{ textAlign: "right", flexShrink: 0 }}>
                  <div style={{ fontSize: "0.8rem", color: "#94a3b8" }}>
                    {e.votes_received}/{e.votes_target} votes
                  </div>
                  {e.resolution && (
                    <div style={{ fontSize: "0.72rem", color: e.resolution === "upheld" ? "#22c55e"
                      : e.resolution === "overturned" ? "#ef4444" : "#64748b", marginTop: "0.25rem" }}>
                      {e.resolution}
                    </div>
                  )}
                  <div style={{ fontSize: "0.67rem", color: "#334155", marginTop: "0.25rem" }}>
                    expires {new Date(e.expires_at).toLocaleDateString()}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
