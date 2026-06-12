"use client";
import { useEffect, useState } from "react";
import Link from "next/link";

interface Proposal {
  id: number;
  suggested_slug: string;
  suggested_title: string;
  centroid_similarity: number;
  paper_count: number;
  cluster_papers?: string[];
  status: string;
  created_at: string | null;
}

export default function AdminProposalsPage() {
  const [proposals, setProposals] = useState<Proposal[]>([]);
  const [loading, setLoading] = useState(true);
  const [acting, setActing] = useState<number | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [expandedId, setExpandedId] = useState<number | null>(null);

  const fetchProposals = () => {
    setLoading(true);
    fetch("/api/new-page-proposals?status=pending&limit=100")
      .then((r) => r.json())
      .catch(() => ({ items: [] }))
      .then((data) => {
        setProposals(data.items ?? []);
        setLoading(false);
      });
  };

  useEffect(() => { fetchProposals(); }, []);

  const loadClusterPapers = async (id: number) => {
    if (expandedId === id) {
      setExpandedId(null);
      return;
    }
    try {
      const res = await fetch(`/api/new-page-proposals/${id}`);
      const data = await res.json();
      setProposals((prev) =>
        prev.map((p) => p.id === id ? { ...p, cluster_papers: data.cluster_papers } : p)
      );
      setExpandedId(id);
    } catch {
      setExpandedId(id);
    }
  };

  const decide = async (id: number, action: "accept" | "reject") => {
    setActing(id);
    setMessage(null);
    try {
      const res = await fetch(`/api/admin/proposals/${id}/decision`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action, actor: "papa" }),
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        setMessage(`Error: ${err.detail ?? res.statusText}`);
      } else {
        const data = await res.json();
        const detail = action === "accept" && data.page_id
          ? `Proposal ${id} accepted → wiki page #${data.page_id} created.`
          : `Proposal ${id} ${action === "accept" ? "approved" : "rejected"}.`;
        setMessage(detail);
        setProposals((prev) => prev.filter((p) => p.id !== id));
        if (expandedId === id) setExpandedId(null);
      }
    } catch (e) {
      setMessage(`Network error: ${e}`);
    } finally {
      setActing(null);
    }
  };

  return (
    <div style={{ maxWidth: "80rem", margin: "0 auto", padding: "2rem 1rem" }}>
      <div style={{ marginBottom: "2rem" }}>
        <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.5rem" }}>
          <Link href="/" style={{ color: "#6366f1", textDecoration: "none" }}>← Home</Link>
        </div>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 800, color: "#f8fafc", margin: 0 }}>
          🌌 New Page Proposals
        </h1>
        <p style={{ color: "#64748b", fontSize: "0.875rem", marginTop: "0.4rem" }}>
          Pending arXiv-sourced new page candidates. Accept creates the wiki page; reject dismisses.
        </p>
      </div>

      {message && (
        <div style={{
          marginBottom: "1rem",
          padding: "0.75rem 1rem",
          borderRadius: "0.5rem",
          background: message.startsWith("Error") ? "#450a0a" : "#052e16",
          color: message.startsWith("Error") ? "#fca5a5" : "#86efac",
          fontSize: "0.875rem",
        }}>
          {message}
        </div>
      )}

      {loading ? (
        <p style={{ color: "#64748b" }}>Loading…</p>
      ) : proposals.length === 0 ? (
        <p style={{ color: "#64748b" }}>No pending proposals.</p>
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
                {["Slug", "Title", "Papers", "Centroid Sim", "Created", "Actions"].map((h) => (
                  <th key={h} style={{
                    padding: "0.75rem 1rem",
                    textAlign: "left",
                    color: "#94a3b8",
                    fontWeight: 600,
                    fontSize: "0.75rem",
                    letterSpacing: "0.05em",
                    textTransform: "uppercase",
                  }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {proposals.map((p, i) => (
                <>
                  <tr key={p.id} style={{
                    borderTop: "1px solid #1e293b",
                    background: i % 2 === 0 ? "transparent" : "#0a0f1a",
                  }}>
                    <td style={{ padding: "0.65rem 1rem", color: "#a855f7", fontFamily: "monospace", fontSize: "0.8rem" }}>
                      {p.suggested_slug}
                    </td>
                    <td style={{ padding: "0.65rem 1rem", color: "#f1f5f9", maxWidth: "18rem" }}>
                      <span title={p.suggested_title}>
                        {p.suggested_title.length > 60
                          ? p.suggested_title.slice(0, 60) + "…"
                          : p.suggested_title}
                      </span>
                    </td>
                    <td style={{ padding: "0.65rem 1rem", color: "#94a3b8", textAlign: "center" }}>
                      <button
                        onClick={() => loadClusterPapers(p.id)}
                        style={{
                          background: "none",
                          border: "none",
                          color: "#6366f1",
                          cursor: "pointer",
                          fontSize: "0.85rem",
                          textDecoration: "underline",
                          padding: 0,
                        }}
                      >
                        {p.paper_count} {expandedId === p.id ? "▲" : "▼"}
                      </button>
                    </td>
                    <td style={{ padding: "0.65rem 1rem", color: "#64748b", fontFamily: "monospace", fontSize: "0.8rem" }}>
                      {p.centroid_similarity > 0 ? p.centroid_similarity.toFixed(3) : "—"}
                    </td>
                    <td style={{ padding: "0.65rem 1rem", color: "#64748b", fontSize: "0.75rem", fontFamily: "monospace" }}>
                      {p.created_at ? new Date(p.created_at).toLocaleDateString() : "—"}
                    </td>
                    <td style={{ padding: "0.65rem 1rem" }}>
                      <div style={{ display: "flex", gap: "0.5rem" }}>
                        <button
                          disabled={acting === p.id}
                          onClick={() => decide(p.id, "accept")}
                          style={{
                            padding: "0.3rem 0.75rem",
                            background: acting === p.id ? "#166534" : "#15803d",
                            color: "#f0fdf4",
                            border: "none",
                            borderRadius: "0.375rem",
                            cursor: acting === p.id ? "not-allowed" : "pointer",
                            fontSize: "0.8rem",
                            fontWeight: 600,
                          }}
                        >
                          Accept
                        </button>
                        <button
                          disabled={acting === p.id}
                          onClick={() => decide(p.id, "reject")}
                          style={{
                            padding: "0.3rem 0.75rem",
                            background: acting === p.id ? "#7f1d1d" : "#991b1b",
                            color: "#fef2f2",
                            border: "none",
                            borderRadius: "0.375rem",
                            cursor: acting === p.id ? "not-allowed" : "pointer",
                            fontSize: "0.8rem",
                            fontWeight: 600,
                          }}
                        >
                          Reject
                        </button>
                      </div>
                    </td>
                  </tr>
                  {expandedId === p.id && p.cluster_papers && p.cluster_papers.length > 0 && (
                    <tr key={`${p.id}-papers`} style={{ background: "#0a1628", borderTop: "1px solid #1e293b" }}>
                      <td colSpan={6} style={{ padding: "0.5rem 1rem 0.75rem 1rem" }}>
                        <div style={{ fontSize: "0.75rem", color: "#64748b", marginBottom: "0.25rem" }}>
                          arXiv papers in cluster:
                        </div>
                        <div style={{ display: "flex", flexWrap: "wrap", gap: "0.4rem" }}>
                          {p.cluster_papers.map((id) => (
                            <a
                              key={id}
                              href={`https://arxiv.org/abs/${id}`}
                              target="_blank"
                              rel="noopener noreferrer"
                              style={{
                                fontSize: "0.75rem",
                                color: "#38bdf8",
                                fontFamily: "monospace",
                                textDecoration: "none",
                                background: "#0c1e35",
                                padding: "0.15rem 0.5rem",
                                borderRadius: "0.25rem",
                                border: "1px solid #1e3a5f",
                              }}
                            >
                              {id}
                            </a>
                          ))}
                        </div>
                      </td>
                    </tr>
                  )}
                </>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <p style={{ color: "#475569", fontSize: "0.75rem", marginTop: "1rem" }}>
        {proposals.length} pending • actor: papa
      </p>
    </div>
  );
}
