"use client";
import { useEffect, useState } from "react";
import Link from "next/link";

interface AutowikiRun {
  id: number;
  page_id: number;
  tick_at: string;
  proposal_type: string | null;
  struct_score: number | null;
  quality_score: number | null;
  accepted: boolean | null;
  reject_reason: string | null;
  judge_rationale: string | null;
  judge_prompt_version: string | null;
  page_version_before: number | null;
  page_version_after: number | null;
}

const PROPOSAL_COLOR: Record<string, string> = {
  subtopic_expand: "#6366f1",
  debate_claim_add: "#f59e0b",
  evidence_refresh: "#10b981",
  hero_fact_upgrade: "#a855f7",
};

function QualityBadge({ score }: { score: number | null }) {
  if (score === null) return <span style={{ color: "#64748b" }}>—</span>;
  const color = score >= 7 ? "#10b981" : score >= 5 ? "#f59e0b" : "#ef4444";
  return <span style={{ color, fontWeight: 700 }}>{score.toFixed(2)}</span>;
}

function Sparkline({ data }: { data: (number | null)[] }) {
  const valid = data.filter((v): v is number => v !== null);
  if (valid.length < 2) return <span style={{ color: "#334155" }}>not enough data</span>;
  const min = Math.min(...valid);
  const max = Math.max(...valid);
  const range = max - min || 1;
  const W = 200;
  const H = 40;
  const pts = valid
    .map((v, i) => {
      const x = (i / (valid.length - 1)) * W;
      const y = H - ((v - min) / range) * H;
      return `${x},${y}`;
    })
    .join(" ");
  return (
    <svg width={W} height={H} style={{ display: "block" }}>
      <polyline
        points={pts}
        fill="none"
        stroke="#6366f1"
        strokeWidth={2}
        strokeLinejoin="round"
      />
    </svg>
  );
}

export default function AutowikiPage() {
  const [runs, setRuns] = useState<AutowikiRun[]>([]);
  const [pageId, setPageId] = useState(57);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/autowiki/runs?page_id=${pageId}&limit=50`)
      .then((r) => r.json())
      .then((data) => {
        setRuns(Array.isArray(data) ? data : []);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [pageId]);

  const qualityScores = [...runs].reverse().map((r) => r.quality_score);
  const accepted = runs.filter((r) => r.accepted).length;
  const rejected = runs.filter((r) => r.accepted === false).length;

  return (
    <div style={{ maxWidth: "72rem", margin: "0 auto", padding: "2rem 1rem", fontFamily: "sans-serif" }}>
      <div style={{ marginBottom: "1.5rem" }}>
        <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.5rem" }}>
          <Link href="/" style={{ color: "#6366f1", textDecoration: "none" }}>← Home</Link>
        </div>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 800, color: "#f8fafc", margin: 0 }}>
          ⚡ Autowiki Loop
        </h1>
        <p style={{ color: "#64748b", fontSize: "0.875rem", marginTop: "0.4rem" }}>
          Continuous AI-driven wiki improvement — AstroSage-70B drafts, Atom-7B gates, Rakon judges.
        </p>
      </div>

      {/* Page selector */}
      <div style={{ marginBottom: "1.5rem", display: "flex", alignItems: "center", gap: "0.75rem" }}>
        <label style={{ color: "#94a3b8", fontSize: "0.875rem" }}>Page ID:</label>
        <input
          type="number"
          value={pageId}
          onChange={(e) => setPageId(Number(e.target.value))}
          style={{
            background: "#1e293b",
            border: "1px solid #334155",
            borderRadius: "0.375rem",
            color: "#f8fafc",
            padding: "0.25rem 0.5rem",
            width: "80px",
            fontSize: "0.875rem",
          }}
        />
      </div>

      {/* Stats row */}
      <div style={{ display: "flex", gap: "1rem", marginBottom: "1.5rem", flexWrap: "wrap" }}>
        {[
          { label: "Total ticks", value: runs.length },
          { label: "Accepted", value: accepted, color: "#10b981" },
          { label: "Rejected", value: rejected, color: "#ef4444" },
          {
            label: "Accept rate",
            value: runs.length ? `${((accepted / runs.length) * 100).toFixed(0)}%` : "—",
          },
        ].map((s) => (
          <div
            key={s.label}
            style={{
              background: "#1e293b",
              border: "1px solid #334155",
              borderRadius: "0.5rem",
              padding: "0.75rem 1.25rem",
              minWidth: "120px",
            }}
          >
            <div style={{ fontSize: "0.75rem", color: "#64748b", marginBottom: "0.2rem" }}>{s.label}</div>
            <div style={{ fontSize: "1.5rem", fontWeight: 700, color: s.color || "#f8fafc" }}>{s.value}</div>
          </div>
        ))}
      </div>

      {/* Quality score chart */}
      <div
        style={{
          background: "#1e293b",
          border: "1px solid #334155",
          borderRadius: "0.5rem",
          padding: "1rem 1.25rem",
          marginBottom: "1.5rem",
        }}
      >
        <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.5rem" }}>
          Quality score over time (oldest → newest)
        </div>
        <Sparkline data={qualityScores} />
      </div>

      {/* Run table */}
      {loading ? (
        <div style={{ color: "#64748b" }}>Loading…</div>
      ) : runs.length === 0 ? (
        <div style={{ color: "#64748b" }}>No runs yet for page {pageId}.</div>
      ) : (
        <div style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: "0.8rem" }}>
            <thead>
              <tr style={{ color: "#64748b", borderBottom: "1px solid #334155" }}>
                {["Tick at", "Proposal type", "Quality", "Struct", "Accepted", "Reject reason", "Rationale", "Versions"].map(
                  (h) => (
                    <th key={h} style={{ textAlign: "left", padding: "0.5rem 0.75rem", fontWeight: 600 }}>
                      {h}
                    </th>
                  )
                )}
              </tr>
            </thead>
            <tbody>
              {runs.map((r) => (
                <tr
                  key={r.id}
                  style={{
                    borderBottom: "1px solid #1e293b",
                    background: r.accepted ? "rgba(16,185,129,0.04)" : undefined,
                  }}
                >
                  <td style={{ padding: "0.5rem 0.75rem", color: "#94a3b8", whiteSpace: "nowrap" }}>
                    {r.tick_at ? new Date(r.tick_at).toLocaleString() : "—"}
                  </td>
                  <td style={{ padding: "0.5rem 0.75rem" }}>
                    {r.proposal_type ? (
                      <span
                        style={{
                          background: PROPOSAL_COLOR[r.proposal_type] + "22",
                          color: PROPOSAL_COLOR[r.proposal_type] || "#94a3b8",
                          borderRadius: "0.25rem",
                          padding: "0.1rem 0.4rem",
                          fontSize: "0.75rem",
                        }}
                      >
                        {r.proposal_type.replace(/_/g, " ")}
                      </span>
                    ) : (
                      <span style={{ color: "#334155" }}>—</span>
                    )}
                  </td>
                  <td style={{ padding: "0.5rem 0.75rem" }}>
                    <QualityBadge score={r.quality_score} />
                  </td>
                  <td style={{ padding: "0.5rem 0.75rem", color: "#64748b" }}>
                    {r.struct_score !== null ? r.struct_score.toFixed(1) : "—"}
                  </td>
                  <td style={{ padding: "0.5rem 0.75rem" }}>
                    {r.accepted === null ? (
                      <span style={{ color: "#64748b" }}>—</span>
                    ) : r.accepted ? (
                      <span style={{ color: "#10b981", fontWeight: 700 }}>✓</span>
                    ) : (
                      <span style={{ color: "#ef4444", fontWeight: 700 }}>✗</span>
                    )}
                  </td>
                  <td style={{ padding: "0.5rem 0.75rem", color: "#94a3b8" }}>
                    {r.reject_reason || "—"}
                  </td>
                  <td
                    style={{
                      padding: "0.5rem 0.75rem",
                      color: "#64748b",
                      maxWidth: "220px",
                      overflow: "hidden",
                      textOverflow: "ellipsis",
                      whiteSpace: "nowrap",
                    }}
                    title={r.judge_rationale || ""}
                  >
                    {r.judge_rationale || "—"}
                  </td>
                  <td style={{ padding: "0.5rem 0.75rem", color: "#64748b" }}>
                    {r.page_version_before !== null
                      ? `v${r.page_version_before} → v${r.page_version_after ?? "—"}`
                      : "—"}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
