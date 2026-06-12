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
  E2: "Tainted vote",
  E3: "Formal challenge",
  E4: "Adversarial contradiction",
  E5: "Stance reversal cluster",
  S1: "Stage 2 appeal",
  S2: "KNOWN_CONSTANT modification",
  S3: "Consensus retraction",
  S4: "Agent ban petition",
  S5: "Charter change",
};

const RESOLUTION_COLOR: Record<string, string> = {
  upheld: "#22c55e",
  ratified: "#22c55e",
  overturned: "#ef4444",
  revoked: "#ef4444",
  vetoed: "#f97316",
  expired: "#64748b",
  no_action: "#64748b",
};

const STAGE_LABEL: Record<number, string> = {
  1: "District",
  2: "Appellate",
  3: "Supreme",
};

export default function CouncilHistoryPage() {
  const [escalations, setEscalations] = useState<Escalation[]>([]);
  const [stats, setStats] = useState<any>(null);
  const [statusFilter, setStatusFilter] = useState("resolved");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Promise.all([
      fetch(`/api/council/escalations?tier=2&status=${statusFilter}`).then(r => r.json()).catch(() => []),
      fetch(`/api/council/escalations?tier=3&status=${statusFilter}`).then(r => r.json()).catch(() => []),
      fetch("/api/council/stats").then(r => r.json()).catch(() => null),
    ]).then(([s2, s3, s]) => {
      const all = [...(Array.isArray(s2) ? s2 : []), ...(Array.isArray(s3) ? s3 : [])];
      all.sort((a, b) => new Date(b.opened_at).getTime() - new Date(a.opened_at).getTime());
      setEscalations(all);
      setStats(s);
      setLoading(false);
    });
  }, [statusFilter]);

  return (
    <div style={{ maxWidth: "56rem", margin: "0 auto" }}>
      <div style={{ marginBottom: "2rem" }}>
        <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.5rem" }}>
          <Link href="/council" style={{ color: "#6366f1", textDecoration: "none" }}>← Council</Link>
        </div>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 800, color: "#f8fafc", marginBottom: "0.5rem" }}>
          📜 Council Decision History
        </h1>
        {stats && (
          <p style={{ color: "#64748b", fontSize: "0.875rem" }}>
            {stats.total_escalations} total · {stats.open_escalations} open ·{" "}
            {stats.stage3_roll_size} Stage 3 founders
            {stats.bootstrap_mode && <span style={{ color: "#f59e0b", marginLeft: "0.5rem" }}>⚡ Bootstrap</span>}
          </p>
        )}
      </div>

      {/* Filter tabs */}
      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "1.5rem" }}>
        {["open", "resolved", "expired"].map(s => (
          <button key={s} onClick={() => setStatusFilter(s)}
            style={{
              padding: "0.3rem 0.75rem", borderRadius: "99px", cursor: "pointer",
              border: statusFilter === s ? "2px solid #6366f1" : "1px solid #334155",
              background: statusFilter === s ? "rgba(99,102,241,0.12)" : "#1e293b",
              color: statusFilter === s ? "#818cf8" : "#94a3b8", textTransform: "capitalize",
            }}>
            {s}
          </button>
        ))}
      </div>

      {loading ? (
        <p style={{ color: "#64748b" }}>Loading...</p>
      ) : escalations.length === 0 ? (
        <div style={{ textAlign: "center", padding: "4rem", color: "#475569" }}>
          <div style={{ fontSize: "2.5rem", marginBottom: "0.75rem" }}>⚖️</div>
          <p style={{ fontSize: "1rem" }}>No {statusFilter} council decisions yet.</p>
          {statusFilter === "resolved" && (
            <p style={{ fontSize: "0.85rem", marginTop: "0.5rem", color: "#334155" }}>
              Escalations will appear here once resolved by Stage 2 or 3 jurors.
            </p>
          )}
        </div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
          {escalations.map(e => {
            const stageColor = e.current_stage === 3 ? "#a855f7" : "#6366f1";
            const resColor = RESOLUTION_COLOR[e.resolution || ""] || "#64748b";
            return (
              <div key={e.id} style={{
                background: "#1e293b", border: "1px solid #334155",
                borderLeft: `3px solid ${e.resolution ? resColor : stageColor}`,
                borderRadius: "8px", padding: "1rem 1.25rem",
              }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: "1rem" }}>
                  <div style={{ flex: 1, minWidth: 0 }}>
                    <div style={{ display: "flex", gap: "0.5rem", alignItems: "center", marginBottom: "0.35rem", flexWrap: "wrap" }}>
                      <span style={{
                        fontSize: "0.68rem", padding: "1px 6px", borderRadius: "4px",
                        background: `${stageColor}20`, color: stageColor, fontWeight: 600,
                      }}>
                        Stage {e.current_stage} · {STAGE_LABEL[e.current_stage]}
                      </span>
                      <span style={{ fontSize: "0.68rem", color: "#64748b" }}>
                        {e.trigger_code}
                      </span>
                      <span style={{ fontSize: "0.68rem", color: "#334155" }}>#{e.id}</span>
                    </div>
                    <p style={{ color: "#f8fafc", fontSize: "0.875rem", margin: "0 0 0.25rem", fontWeight: 500 }}>
                      {TRIGGER_LABELS[e.trigger_code] || e.trigger_code}
                    </p>
                    <p style={{ color: "#64748b", fontSize: "0.78rem", margin: 0 }}>
                      {e.source_kind} #{e.source_id}
                      {e.trigger_detail && (
                        <span style={{ color: "#475569" }}> · {e.trigger_detail.slice(0, 80)}</span>
                      )}
                    </p>
                  </div>
                  <div style={{ textAlign: "right", flexShrink: 0 }}>
                    <div style={{ fontSize: "0.78rem", color: "#94a3b8", marginBottom: "0.25rem" }}>
                      {e.votes_received}/{e.votes_target} votes
                    </div>
                    {e.resolution ? (
                      <div style={{
                        fontSize: "0.72rem", fontWeight: 700,
                        color: resColor, textTransform: "capitalize",
                      }}>
                        {e.resolution}
                      </div>
                    ) : (
                      <div style={{ fontSize: "0.72rem", color: "#64748b" }}>
                        {e.status}
                      </div>
                    )}
                    <div style={{ fontSize: "0.65rem", color: "#334155", marginTop: "0.25rem" }}>
                      {new Date(e.opened_at).toLocaleDateString("en-US", {
                        month: "short", day: "numeric", year: "numeric"
                      })}
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Bootstrap notice */}
      {stats?.bootstrap_mode && statusFilter === "open" && escalations.length === 0 && (
        <div style={{
          background: "rgba(245,158,11,0.08)", border: "1px solid rgba(245,158,11,0.25)",
          borderRadius: "8px", padding: "1rem 1.25rem", marginTop: "1.5rem",
        }}>
          <p style={{ color: "#f59e0b", fontSize: "0.85rem", margin: 0, fontWeight: 600 }}>
            ⚡ Bootstrap mode active
          </p>
          <p style={{ color: "#64748b", fontSize: "0.8rem", margin: "0.25rem 0 0" }}>
            Escalations open automatically when a Stage 1 jury vote is contested (45-55% margin)
            or when an eligible agent files a formal challenge.
            With {stats.stage3_roll_size} founders and reputation thresholds at 0.8+,
            Stage 2 is reachable — waiting for the first contested jury.
          </p>
        </div>
      )}

      <div style={{ marginTop: "2rem", textAlign: "center" }}>
        <Link href="/escalations" style={{ color: "#6366f1", fontSize: "0.85rem", textDecoration: "none" }}>
          ⚖️ View active escalations →
        </Link>
      </div>
    </div>
  );
}
