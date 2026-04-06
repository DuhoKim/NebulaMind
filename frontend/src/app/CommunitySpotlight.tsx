"use client";
import { useEffect, useState } from "react";
import Link from "next/link";

interface SpotlightItem {
  id: number;
  arxiv_id: string;
  title: string;
  authors: string[];
  summary: string;
  related_pages: string[];
  url: string;
  featured: boolean;
  submitted_by?: string;
  created_at: string;
}

export default function CommunitySpotlight() {
  const [items, setItems] = useState<SpotlightItem[]>([]);
  const [showModal, setShowModal] = useState(false);
  const [arxivId, setArxivId] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<"idle" | "success" | "error">("idle");

  useEffect(() => {
    fetch("/api/spotlight")
      .then(r => r.json())
      .then(d => setItems(Array.isArray(d) ? d : []))
      .catch(() => {});
  }, []);

  const handleSubmit = async () => {
    if (!arxivId.trim()) return;
    setSubmitting(true);
    try {
      const res = await fetch("/api/spotlight", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ arxiv_id: arxivId.trim() }),
      });
      if (res.ok) {
        const newItem = await res.json();
        setItems(prev => [newItem, ...prev]);
        setSubmitStatus("success");
        setArxivId("");
        setTimeout(() => { setShowModal(false); setSubmitStatus("idle"); }, 2000);
      } else {
        setSubmitStatus("error");
      }
    } catch {
      setSubmitStatus("error");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <section style={{ marginTop: "2.5rem" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1rem" }}>
        <div>
          <h3 style={{ margin: 0, fontSize: "1.1rem", fontWeight: 700 }}>🔬 Community Spotlight</h3>
          <p style={{ margin: "0.25rem 0 0", fontSize: "0.8rem", color: "#6b7280" }}>Researchers share their own work with the NebulaMind community</p>
        </div>
        <button
          onClick={() => setShowModal(true)}
          style={{ padding: "0.4rem 1rem", background: "#7c3aed", color: "white", border: "none", borderRadius: "0.5rem", cursor: "pointer", fontSize: "0.85rem", fontWeight: 600 }}
        >
          + Submit Your Paper
        </button>
      </div>

      {items.length === 0 ? (
        <div style={{ textAlign: "center", padding: "2rem", color: "#9ca3af", border: "1px dashed #e5e7eb", borderRadius: "0.75rem" }}>
          🌌 No papers submitted yet. Be the first!
        </div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
          {items.slice(0, 5).map(item => (
            <div key={item.id} style={{ border: "1px solid #e5e7eb", borderRadius: "0.75rem", padding: "1rem", background: item.featured ? "#faf5ff" : "white" }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: "0.5rem" }}>
                <div style={{ flex: 1 }}>
                  <div style={{ display: "flex", gap: "0.5rem", alignItems: "center", marginBottom: "0.4rem" }}>
                    {item.featured && <span style={{ fontSize: "0.7rem", background: "#7c3aed", color: "white", padding: "0.1rem 0.4rem", borderRadius: "9999px" }}>⭐ Featured</span>}
                    <span style={{ fontSize: "0.7rem", background: "#e0e7ff", color: "#4338ca", padding: "0.1rem 0.4rem", borderRadius: "9999px" }}>🔬 Community</span>
                  </div>
                  <a href={item.url} target="_blank" rel="noopener noreferrer" style={{ fontWeight: 600, fontSize: "0.9rem", color: "#1f2937", textDecoration: "none" }}>
                    {item.title}
                  </a>
                  <p style={{ margin: "0.4rem 0", fontSize: "0.82rem", color: "#4b5563", lineHeight: 1.5 }}>{item.summary}</p>
                  {item.related_pages.length > 0 && (
                    <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap" }}>
                      {item.related_pages.map(slug => (
                        <Link key={slug} href={`/wiki/${slug}`} style={{ fontSize: "0.75rem", color: "#4f46e5", textDecoration: "none", background: "#eef2ff", padding: "0.1rem 0.4rem", borderRadius: "9999px" }}>
                          🔗 {slug}
                        </Link>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {showModal && (
        <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", display: "flex", alignItems: "center", justifyContent: "center", zIndex: 1000 }}>
          <div style={{ background: "white", borderRadius: "1rem", padding: "2rem", maxWidth: "480px", width: "90%", boxShadow: "0 20px 60px rgba(0,0,0,0.3)" }}>
            <h3 style={{ margin: "0 0 1rem", fontSize: "1.1rem" }}>🔬 Submit Your Paper</h3>
            <p style={{ margin: "0 0 1rem", fontSize: "0.85rem", color: "#6b7280" }}>
              Enter an arXiv ID and our AI will generate a summary and link it to relevant wiki pages.
            </p>
            {submitStatus === "success" ? (
              <div style={{ textAlign: "center", padding: "1rem", color: "#16a34a", fontWeight: 600 }}>✅ Paper submitted successfully!</div>
            ) : (
              <>
                <input
                  type="text"
                  placeholder="e.g. 2604.01234"
                  value={arxivId}
                  onChange={e => setArxivId(e.target.value)}
                  style={{ width: "100%", padding: "0.6rem 1rem", border: "1px solid #d1d5db", borderRadius: "0.5rem", marginBottom: "0.75rem", boxSizing: "border-box", fontSize: "0.95rem" }}
                />
                {submitStatus === "error" && <p style={{ color: "#dc2626", fontSize: "0.85rem", marginBottom: "0.5rem" }}>Error. Check the arXiv ID and try again.</p>}
                <div style={{ display: "flex", gap: "0.5rem", justifyContent: "flex-end" }}>
                  <button onClick={() => setShowModal(false)} style={{ padding: "0.5rem 1rem", border: "1px solid #d1d5db", borderRadius: "0.5rem", cursor: "pointer", background: "white" }}>Cancel</button>
                  <button onClick={handleSubmit} disabled={submitting} style={{ padding: "0.5rem 1.25rem", background: "#7c3aed", color: "white", border: "none", borderRadius: "0.5rem", cursor: "pointer", fontWeight: 600 }}>
                    {submitting ? "Processing..." : "Submit"}
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      )}
    </section>
  );
}
