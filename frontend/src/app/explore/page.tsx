"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

const MODES = [
  { emoji: "\uD83C\uDFB4", title: "Cards", desc: "Browse wiki pages as visual cards", href: "/explore/cards" },
  { emoji: "\u2753", title: "Q&A", desc: "Ask and answer astronomy questions", href: "/explore/qa" },
  { emoji: "\uD83D\uDCAC", title: "Chat", desc: "Chat with the knowledge base", href: "/explore/chat" },
  { emoji: "\uD83D\uDD78\uFE0F", title: "Graph", desc: "Visualize page connections", href: "/explore/graph" },
];

export default function ExplorePage() {
  const [pageCount, setPageCount] = useState<number | null>(null);

  useEffect(() => {
    fetch("/api/pages")
      .then((r) => r.json())
      .then((data) => setPageCount(Array.isArray(data) ? data.length : 0))
      .catch(() => setPageCount(0));
  }, []);

  return (
    <div>
      <h2 style={{ fontSize: "1.5rem", margin: "0 0 0.25rem" }}>{"\uD83C\uDF0C"} NebulaMind Explore</h2>
      <p style={{ color: "#6b7280", margin: "0 0 1.5rem" }}>
        Discover astronomy knowledge in different ways.
        {pageCount !== null && (
          <span style={{ marginLeft: "0.5rem", background: "#e0e7ff", padding: "0.15rem 0.5rem", borderRadius: "9999px", fontSize: "0.8rem" }}>
            {pageCount} pages in knowledge base
          </span>
        )}
      </p>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))", gap: "1rem" }}>
        {MODES.map((m) => (
          <Link
            key={m.href}
            href={m.href}
            style={{
              textDecoration: "none",
              color: "inherit",
              border: "1px solid #e5e7eb",
              borderRadius: "0.75rem",
              padding: "1.25rem",
              transition: "box-shadow 0.15s",
            }}
            onMouseOver={(e) => (e.currentTarget.style.boxShadow = "0 4px 12px rgba(0,0,0,0.08)")}
            onMouseOut={(e) => (e.currentTarget.style.boxShadow = "none")}
          >
            <div style={{ fontSize: "2rem", marginBottom: "0.5rem" }}>{m.emoji}</div>
            <div style={{ fontWeight: 600, marginBottom: "0.25rem" }}>{m.title}</div>
            <div style={{ fontSize: "0.85rem", color: "#6b7280" }}>{m.desc}</div>
          </Link>
        ))}
      </div>
    </div>
  );
}
