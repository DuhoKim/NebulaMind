import React from "react";
import { AGN_DEBATE_MAP, type AxisStatusKey, type CounterLink } from "./debateAxisMapData";

const STATUS_COLOR: Record<AxisStatusKey, string> = {
  settled: "#34d399",
  emerging: "#93c5fd",
  debated: "#fbbf24",
  "model-dependent": "#94a3b8",
};

const RELATION_COLOR: Record<CounterLink["relation"], string> = {
  contradicts: "#f97316",
  qualifies: "#fbbf24",
  "same-axis position": "#93c5fd",
};

const card: React.CSSProperties = {
  background: "rgba(15,23,42,0.64)",
  border: "1px solid #334155",
  borderRadius: "12px",
  padding: "1rem 1.05rem",
  display: "flex",
  flexDirection: "column",
  gap: "0.55rem",
};

const sub: React.CSSProperties = { fontSize: "0.62rem", fontWeight: 800, textTransform: "uppercase", letterSpacing: "0.06em", color: "#64748b" };

export default function DebateAxisMap() {
  return (
    <section
      data-testid="agn-debate-axis-map"
      style={{ marginTop: "3rem", borderTop: "1px solid #334155", paddingTop: "2rem" }}
    >
      <div style={{ display: "flex", flexWrap: "wrap", alignItems: "baseline", gap: "0.6rem", marginBottom: "0.35rem" }}>
        <h2 style={{ fontSize: "1.25rem", fontWeight: 600, color: "#f8fafc", margin: 0 }}>{AGN_DEBATE_MAP.title}</h2>
        <span style={{ ...sub, color: "#94a3b8" }}>curated · descriptive</span>
      </div>
      <p style={{ color: "#94a3b8", fontSize: "0.82rem", lineHeight: 1.6, margin: "0 0 0.5rem", maxWidth: "72ch" }}>
        {AGN_DEBATE_MAP.intro}
      </p>
      <p style={{ ...sub, margin: "0 0 1.15rem", color: "#64748b" }}>{AGN_DEBATE_MAP.provenance}</p>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: "0.8rem" }}>
        {AGN_DEBATE_MAP.axes.map((axis) => {
          const color = STATUS_COLOR[axis.status];
          return (
            <div key={axis.key} data-testid={`agn-axis-${axis.key}`} style={card}>
              <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: "0.5rem", flexWrap: "wrap" }}>
                <span style={{ fontSize: "1rem", fontWeight: 700, color: "#f8fafc" }}>{axis.label}</span>
                <span
                  data-testid={`agn-axis-status-${axis.key}`}
                  style={{
                    color,
                    border: `1px solid ${color}66`,
                    background: `${color}1f`,
                    borderRadius: "999px",
                    padding: "0.1rem 0.5rem",
                    fontSize: "0.6rem",
                    fontWeight: 850,
                    textTransform: "uppercase",
                    letterSpacing: "0.04em",
                    whiteSpace: "nowrap",
                  }}
                >
                  {axis.statusLabel}
                </span>
              </div>

              <p style={{ margin: 0, color: "#cbd5e1", fontSize: "0.82rem", fontStyle: "italic" }}>{axis.question}</p>
              <p style={{ margin: 0, color: "#94a3b8", fontSize: "0.76rem", lineHeight: 1.55 }}>{axis.guide}</p>

              <div>
                <div style={sub}>Claims on this axis</div>
                <ul style={{ margin: "0.3rem 0 0", padding: 0, listStyle: "none", display: "flex", flexDirection: "column", gap: "0.35rem" }}>
                  {axis.claims.map((c) => (
                    <li key={c.id} style={{ display: "flex", gap: "0.45rem", color: "#e2e8f0", fontSize: "0.78rem", lineHeight: 1.5 }}>
                      <span aria-hidden style={{ color, flexShrink: 0, fontWeight: 800 }}>›</span>
                      <span>{c.text}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {axis.counters.length > 0 && (
                <div>
                  <div style={sub}>Counter-evidence &amp; qualifiers</div>
                  <ul style={{ margin: "0.3rem 0 0", padding: 0, listStyle: "none", display: "flex", flexDirection: "column", gap: "0.4rem" }}>
                    {axis.counters.map((k, i) => {
                      const rc = RELATION_COLOR[k.relation];
                      return (
                        <li key={i} style={{ fontSize: "0.76rem", lineHeight: 1.5, color: "#cbd5e1" }}>
                          <span
                            style={{
                              color: rc,
                              border: `1px solid ${rc}55`,
                              background: `${rc}14`,
                              borderRadius: "6px",
                              padding: "0.02rem 0.34rem",
                              fontSize: "0.6rem",
                              fontWeight: 800,
                              textTransform: "uppercase",
                              letterSpacing: "0.03em",
                              marginRight: "0.4rem",
                              whiteSpace: "nowrap",
                            }}
                          >
                            {k.relation}
                          </span>
                          {k.text}
                          <span style={{ color: "#64748b" }}> — vs. {k.against}</span>
                        </li>
                      );
                    })}
                  </ul>
                </div>
              )}
            </div>
          );
        })}
      </div>

      <p style={{ marginTop: "1rem", color: "#64748b", fontSize: "0.72rem", lineHeight: 1.55, fontStyle: "italic" }}>
        Descriptive scaffold — a curated worked example, not a live query and not human-validated. Every axis keeps its
        counter-evidence attached; nothing is dropped.
      </p>
    </section>
  );
}
