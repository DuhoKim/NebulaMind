"use client";

import { useMemo, useState } from "react";

type Topic = { title: string; slug: string; summary: string };
type Category = { id: string; label: string; emoji: string; topics: Topic[] };

export default function DirectoryClient({ categories }: { categories: Category[] }) {
  const [query, setQuery] = useState("");
  const q = query.trim().toLowerCase();

  const filtered = useMemo(() => {
    if (!q) return categories;
    return categories.map((c) => ({
      ...c,
      topics: c.topics.filter((t) => t.title.toLowerCase().includes(q)),
    }));
  }, [categories, q]);

  const totalShown = filtered.reduce((n, c) => n + c.topics.length, 0);

  return (
    <div>
      <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem", marginBottom: "1.5rem" }}>
        <input
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Filter topics by title…"
          aria-label="Filter topics"
          style={{
            width: "100%",
            padding: "0.65rem 0.9rem",
            background: "#1e293b",
            border: "1px solid #334155",
            borderRadius: "8px",
            color: "#f8fafc",
            fontSize: "0.95rem",
            outline: "none",
          }}
          onFocus={(e) => (e.currentTarget.style.borderColor = "#6366f1")}
          onBlur={(e) => (e.currentTarget.style.borderColor = "#334155")}
        />
        {q && (
          <div style={{ fontSize: "0.8rem", color: "#94a3b8" }}>
            {totalShown} match{totalShown === 1 ? "" : "es"} for “{query}”
          </div>
        )}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "2rem" }}>
        {filtered.map((cat) => (
          <section key={cat.id}>
            <h2
              style={{
                margin: "0 0 0.75rem",
                fontSize: "1.25rem",
                fontWeight: 600,
                color: "#f8fafc",
                display: "flex",
                alignItems: "center",
                gap: "0.5rem",
              }}
            >
              <span aria-hidden style={{ fontSize: "1.4rem" }}>{cat.emoji}</span>
              {cat.label}
              <span style={{ fontSize: "0.75rem", color: "#64748b", fontWeight: 400 }}>
                ({cat.topics.length})
              </span>
            </h2>
            {cat.topics.length === 0 ? (
              <div
                style={{
                  padding: "0.9rem 1rem",
                  border: "1px dashed #334155",
                  borderRadius: "8px",
                  color: "#64748b",
                  fontSize: "0.85rem",
                  fontStyle: "italic",
                }}
              >
                {q ? "No matches in this category." : "Coming soon."}
              </div>
            ) : (
              <div
                style={{
                  display: "grid",
                  gridTemplateColumns: "repeat(auto-fill, minmax(240px, 1fr))",
                  gap: "0.75rem",
                }}
              >
                {cat.topics.map((t) => (
                  <a
                    key={t.slug}
                    href={`/wiki/${t.slug}`}
                    style={{
                      display: "block",
                      padding: "0.85rem 1rem",
                      background: "#1e293b",
                      border: "1px solid #334155",
                      borderRadius: "8px",
                      textDecoration: "none",
                      color: "#f8fafc",
                      transition: "border-color 0.15s, transform 0.15s",
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.borderColor = "#6366f1";
                      e.currentTarget.style.transform = "translateY(-1px)";
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.borderColor = "#334155";
                      e.currentTarget.style.transform = "translateY(0)";
                    }}
                  >
                    <div style={{ fontWeight: 600, fontSize: "0.95rem", marginBottom: "0.25rem" }}>
                      {t.title}
                    </div>
                    <div style={{ fontSize: "0.8rem", color: "#94a3b8", lineHeight: 1.45 }}>
                      {t.summary || "—"}
                    </div>
                  </a>
                ))}
              </div>
            )}
          </section>
        ))}
      </div>
    </div>
  );
}
