"use client";
import { useEffect, useState } from "react";
import Link from "next/link";

interface LlmCall {
  task_role: string;
  model_label: string;
  success: boolean;
  latency_ms: number | null;
  created_at: string;
}

interface RoutingEntry {
  role: string;
  models: string[];
}

const TIER_COLOR: Record<string, string> = {
  rakon: "#a855f7",
  "pro-32b": "#8b5cf6",
  blanc: "#6366f1",
  "gemini-2.0-flash": "#06b6d4",
  "cerebras-fast": "#10b981",
  sambanova: "#f59e0b",
};

const getTierColor = (label: string) =>
  TIER_COLOR[label] || "#64748b";

export default function AdminLlmPage() {
  const [calls, setCalls] = useState<LlmCall[]>([]);
  const [routing, setRouting] = useState<RoutingEntry[]>([]);
  const [stats, setStats] = useState<Record<string, { count: number; avg_ms: number; success_rate: number }>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      fetch("/api/admin/llm/calls?limit=100").then(r => r.json()).catch(() => []),
      fetch("/api/admin/llm/routing").then(r => r.json()).catch(() => []),
      fetch("/api/admin/llm/stats").then(r => r.json()).catch(() => {}),
    ]).then(([c, r, s]) => {
      setCalls(Array.isArray(c) ? c : []);
      setRouting(Array.isArray(r) ? r : []);
      setStats(s || {});
      setLoading(false);
    });
  }, []);

  return (
    <div style={{ maxWidth: "72rem", margin: "0 auto", padding: "2rem 1rem" }}>
      <div style={{ marginBottom: "2rem" }}>
        <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.5rem" }}>
          <Link href="/" style={{ color: "#6366f1", textDecoration: "none" }}>← Home</Link>
        </div>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 800, color: "#f8fafc", margin: 0 }}>
          🧠 LLM Routing Dashboard
        </h1>
        <p style={{ color: "#64748b", fontSize: "0.875rem", marginTop: "0.4rem" }}>
          Live model routing — 5-tier architecture. All inference costs: $0.
        </p>
      </div>

      {/* Tier legend */}
      <div style={{ display: "flex", flexWrap: "wrap", gap: "0.5rem", marginBottom: "2rem" }}>
        {Object.entries(TIER_COLOR).map(([label, color]) => (
          <span key={label} style={{
            padding: "0.25rem 0.75rem", borderRadius: "99px",
            background: `${color}20`, color, fontSize: "0.78rem", fontWeight: 600,
            border: `1px solid ${color}40`,
          }}>
            {label === "rakon" ? "🦖 Rakon (671B)" :
             label === "pro-32b" ? "Mac Pro 32B" :
             label === "blanc" ? "🤍 Blanc (70B)" :
             label}
          </span>
        ))}
      </div>

      {/* Routing table */}
      <div style={{ marginBottom: "2rem" }}>
        <h2 style={{ fontSize: "1rem", fontWeight: 700, color: "#f8fafc", marginBottom: "1rem", textTransform: "uppercase", letterSpacing: "0.08em" }}>
          Task → Model Routing
        </h2>
        {loading ? (
          <p style={{ color: "#64748b" }}>Loading...</p>
        ) : (
          <div style={{ display: "grid", gap: "0.5rem" }}>
            {routing.map(r => (
              <div key={r.role} style={{
                background: "#1e293b", border: "1px solid #334155",
                borderRadius: "8px", padding: "0.75rem 1rem",
                display: "flex", alignItems: "center", gap: "1rem", flexWrap: "wrap",
              }}>
                <span style={{ fontSize: "0.85rem", fontWeight: 600, color: "#94a3b8", minWidth: "160px" }}>
                  {r.role}
                </span>
                <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap" }}>
                  {r.models.map((m, i) => (
                    <span key={m} style={{
                      padding: "0.2rem 0.6rem", borderRadius: "4px", fontSize: "0.75rem",
                      background: `${getTierColor(m)}20`, color: getTierColor(m),
                      border: `1px solid ${getTierColor(m)}40`,
                      opacity: i === 0 ? 1 : 0.7,
                    }}>
                      {i === 0 ? "★ " : ""}{m}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Stats */}
      {Object.keys(stats).length > 0 && (
        <div style={{ marginBottom: "2rem" }}>
          <h2 style={{ fontSize: "1rem", fontWeight: 700, color: "#f8fafc", marginBottom: "1rem", textTransform: "uppercase", letterSpacing: "0.08em" }}>
            Model Performance (Last 24h)
          </h2>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", gap: "0.75rem" }}>
            {Object.entries(stats).map(([model, s]) => (
              <div key={model} style={{
                background: "#1e293b", border: "1px solid #334155",
                borderLeft: `3px solid ${getTierColor(model)}`,
                borderRadius: "8px", padding: "0.75rem 1rem",
              }}>
                <div style={{ fontSize: "0.8rem", fontWeight: 700, color: getTierColor(model), marginBottom: "0.4rem" }}>
                  {model}
                </div>
                <div style={{ fontSize: "0.75rem", color: "#94a3b8" }}>{s.count} calls</div>
                <div style={{ fontSize: "0.75rem", color: "#94a3b8" }}>{s.avg_ms ? `${s.avg_ms}ms avg` : "—"}</div>
                <div style={{ fontSize: "0.75rem", color: s.success_rate > 0.9 ? "#22c55e" : "#f59e0b" }}>
                  {(s.success_rate * 100).toFixed(0)}% success
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Recent calls */}
      <div>
        <h2 style={{ fontSize: "1rem", fontWeight: 700, color: "#f8fafc", marginBottom: "1rem", textTransform: "uppercase", letterSpacing: "0.08em" }}>
          Recent Calls
        </h2>
        {loading ? (
          <p style={{ color: "#64748b" }}>Loading...</p>
        ) : calls.length === 0 ? (
          <div style={{ textAlign: "center", padding: "3rem", color: "#475569" }}>
            <div style={{ fontSize: "2rem", marginBottom: "0.5rem" }}>🧠</div>
            <p>No calls recorded yet. Telemetry starts accumulating as agents run.</p>
          </div>
        ) : (
          <div style={{ display: "flex", flexDirection: "column", gap: "0.4rem" }}>
            {calls.map((c, i) => (
              <div key={i} style={{
                background: "#1e293b", border: "1px solid #334155",
                borderLeft: `3px solid ${c.success ? getTierColor(c.model_label) : "#ef4444"}`,
                borderRadius: "6px", padding: "0.5rem 1rem",
                display: "flex", justifyContent: "space-between", alignItems: "center",
                fontSize: "0.8rem",
              }}>
                <div style={{ display: "flex", gap: "1rem", alignItems: "center" }}>
                  <span style={{ color: "#64748b", minWidth: "140px" }}>{c.task_role}</span>
                  <span style={{ color: getTierColor(c.model_label), fontWeight: 600 }}>{c.model_label}</span>
                </div>
                <div style={{ display: "flex", gap: "1rem", color: "#64748b" }}>
                  {c.latency_ms && <span>{c.latency_ms}ms</span>}
                  <span style={{ color: c.success ? "#22c55e" : "#ef4444" }}>
                    {c.success ? "✓" : "✗"}
                  </span>
                  <span>{new Date(c.created_at).toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit" })}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
