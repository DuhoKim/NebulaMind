"use client";
import { useEffect, useState } from "react";
import Link from "next/link";

interface AuditEvent {
  event_type: string;
  target_kind: string | null;
  target_id: number | null;
  created_at: string | null;
}

export default function AdminAuditPage() {
  const [events, setEvents] = useState<AuditEvent[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/audit/events?limit=100")
      .then((r) => r.json())
      .catch(() => [])
      .then((data) => {
        setEvents(Array.isArray(data) ? data : []);
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
          🔍 Audit Log
        </h1>
        <p style={{ color: "#64748b", fontSize: "0.875rem", marginTop: "0.4rem" }}>
          Last 100 audit events — public view (non-sensitive fields only).
        </p>
      </div>

      {loading ? (
        <p style={{ color: "#64748b" }}>Loading…</p>
      ) : events.length === 0 ? (
        <p style={{ color: "#64748b" }}>No audit events found.</p>
      ) : (
        <div style={{
          background: "#0f172a",
          border: "1px solid #1e293b",
          borderRadius: "0.75rem",
          overflow: "hidden",
        }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: "0.875rem" }}>
            <thead>
              <tr style={{ background: "#1e293b" }}>
                {["Event Type", "Target", "ID", "Timestamp"].map((h) => (
                  <th key={h} style={{
                    padding: "0.75rem 1rem",
                    textAlign: "left",
                    color: "#94a3b8",
                    fontWeight: 600,
                    fontSize: "0.8rem",
                    letterSpacing: "0.05em",
                    textTransform: "uppercase",
                  }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {events.map((e, i) => (
                <tr key={i} style={{
                  borderTop: "1px solid #1e293b",
                  background: i % 2 === 0 ? "transparent" : "#0a0f1a",
                }}>
                  <td style={{ padding: "0.6rem 1rem", color: "#a855f7", fontFamily: "monospace" }}>
                    {e.event_type}
                  </td>
                  <td style={{ padding: "0.6rem 1rem", color: "#94a3b8" }}>
                    {e.target_kind ?? "—"}
                  </td>
                  <td style={{ padding: "0.6rem 1rem", color: "#64748b" }}>
                    {e.target_id ?? "—"}
                  </td>
                  <td style={{ padding: "0.6rem 1rem", color: "#64748b", fontSize: "0.8rem", fontFamily: "monospace" }}>
                    {e.created_at ? new Date(e.created_at).toLocaleString() : "—"}
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
