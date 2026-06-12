"use client";

import { useEffect, useState } from "react";

interface Heading {
  level: number;
  text: string;
  id: string;
}

interface TOCSidebarProps {
  headings: Heading[];
  isMobile: boolean;
}

export default function TOCSidebar({ headings, isMobile }: TOCSidebarProps) {
  const [activeAnchor, setActiveAnchor] = useState<string>("");
  const [mobileOpen, setMobileOpen] = useState(false);
  const tooFew = headings.length < 3;

  // Desktop: active-section highlight via IntersectionObserver
  useEffect(() => {
    if (tooFew || isMobile) return;
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible[0]) setActiveAnchor(visible[0].target.id);
      },
      { rootMargin: "-96px 0px -60% 0px", threshold: 0 }
    );
    document.querySelectorAll("article h2[id], article h3[id]").forEach((h) =>
      observer.observe(h)
    );
    return () => observer.disconnect();
  }, [tooFew, isMobile, headings]);

  // Hide when fewer than 3 headings
  if (tooFew) return null;

  // Mobile: collapsible accordion above content
  if (isMobile) {
    return (
      <nav
        style={{
          marginBottom: "1.5rem",
          background: "#1e293b",
          border: "1px solid #334155",
          borderRadius: "8px",
          overflow: "hidden",
        }}
      >
        <button
          onClick={() => setMobileOpen((v) => !v)}
          style={{
            width: "100%",
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            padding: "0.75rem 1rem",
            background: "transparent",
            border: "none",
            cursor: "pointer",
            textAlign: "left",
          }}
        >
          <span style={{ fontSize: "0.82rem", fontWeight: 600, color: "#94a3b8" }}>
            📖 Contents ({headings.length}) {mobileOpen ? "▴" : "▾"}
          </span>
        </button>
        {mobileOpen && (
          <ul
            style={{
              listStyle: "none",
              padding: "0 1rem 0.75rem",
              margin: 0,
              display: "flex",
              flexDirection: "column",
              gap: "0.25rem",
            }}
          >
            {headings.map((h, i) => (
              <li key={i} style={{ paddingLeft: `${(h.level - 2) * 12}px` }}>
                <a
                  href={`#${h.id}`}
                  onClick={() => setMobileOpen(false)}
                  style={{ fontSize: "0.875rem", color: "#6366f1", textDecoration: "none" }}
                >
                  {h.text}
                </a>
              </li>
            ))}
          </ul>
        )}
      </nav>
    );
  }

  // Desktop: sticky right rail
  return (
    <nav
      style={{
        position: "sticky",
        top: "96px",
        alignSelf: "start",
        background: "#1e293b",
        border: "1px solid #334155",
        borderRadius: "8px",
        padding: "1rem",
        minWidth: 0,
      }}
    >
      <h3
        style={{
          fontSize: "0.75rem",
          fontWeight: 600,
          color: "#64748b",
          marginBottom: "0.5rem",
          textTransform: "uppercase",
          letterSpacing: "0.05em",
        }}
      >
        Contents
      </h3>
      <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "flex", flexDirection: "column", gap: "0.25rem" }}>
        {headings.map((h, i) => {
          const isActive = activeAnchor === h.id;
          return (
            <li key={i} style={{ paddingLeft: h.level === 3 ? "12px" : "0px" }}>
              <a
                href={`#${h.id}`}
                style={{
                  fontSize: "0.8rem",
                  color: isActive ? "#f8fafc" : "#6366f1",
                  textDecoration: "none",
                  display: "block",
                  paddingLeft: isActive ? "6px" : "8px",
                  borderLeft: isActive ? "2px solid #6366f1" : "2px solid transparent",
                  transition: "all 0.15s",
                  lineHeight: 1.5,
                }}
              >
                {h.text}
              </a>
            </li>
          );
        })}
      </ul>
    </nav>
  );
}
