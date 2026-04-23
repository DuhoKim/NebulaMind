"use client";

import { useState, useRef } from "react";

const EXPLORE_LINKS = [
  { href: "/explore/cards", label: "Cards" },
  { href: "/explore/qa", label: "Q&A" },
  { href: "/explore/chat", label: "Chat" },
  { href: "/explore/graph", label: "Graph" },
];

const NAV_LINKS = [
  { href: "/agents", label: "Agents" },
  { href: "/leaderboard", label: "Leaderboard" },
  { href: "/research", label: "Research" },
  { href: "/newsletter", label: "Newsletter" },
  { href: "/contribute", label: "Contribute" },
  { href: "/feedback", label: "Feedback" },
];

const JOIN_LINK = { href: "/join", label: "Join" };

export default function NavBar() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [exploreOpen, setExploreOpen] = useState(false);
  const exploreTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const handleExploreEnter = () => {
    if (exploreTimeoutRef.current) clearTimeout(exploreTimeoutRef.current);
    setExploreOpen(true);
  };

  const handleExploreLeave = () => {
    exploreTimeoutRef.current = setTimeout(() => setExploreOpen(false), 150);
  };

  return (
    <header style={{ borderBottom: "1px solid #334155", background: "#0f172a", position: "sticky", top: 0, zIndex: 40 }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 py-4 flex items-center justify-between">
        <a href="/" className="no-underline text-inherit">
          <span style={{ fontWeight: 600, fontSize: "1.1rem", color: "#f8fafc", letterSpacing: "-0.025em" }}>
            NebulaMind
          </span>
        </a>

        {/* Desktop nav */}
        <nav className="hidden md:flex gap-6 text-sm items-center">
          <a href="/" style={{ color: "#94a3b8", textDecoration: "none", transition: "color 0.15s" }}
            onMouseEnter={e => (e.currentTarget.style.color = "#f8fafc")}
            onMouseLeave={e => (e.currentTarget.style.color = "#94a3b8")}>
            Home
          </a>

          {/* Explore with dropdown */}
          <div
            className="relative"
            onMouseEnter={handleExploreEnter}
            onMouseLeave={handleExploreLeave}
          >
            <a
              href="/explore"
              style={{ color: "#94a3b8", fontWeight: 500, textDecoration: "none", display: "flex", alignItems: "center", gap: "2px", transition: "color 0.15s" }}
              onMouseEnter={e => (e.currentTarget.style.color = "#f8fafc")}
              onMouseLeave={e => (e.currentTarget.style.color = "#94a3b8")}
            >
              Explore
              <span style={{ fontSize: "0.7rem", color: "#64748b", marginLeft: "2px" }}>▾</span>
            </a>
            {exploreOpen && (
              <div style={{ position: "absolute", top: "100%", left: 0, marginTop: "6px", background: "#1e293b", border: "1px solid #334155", borderRadius: "6px", boxShadow: "0 4px 12px rgba(0,0,0,0.3)", padding: "4px 0", minWidth: "140px", zIndex: 50 }}>
                {EXPLORE_LINKS.map((link) => (
                  <a
                    key={link.href}
                    href={link.href}
                    style={{ display: "block", padding: "8px 16px", fontSize: "0.875rem", color: "#94a3b8", textDecoration: "none", transition: "all 0.15s" }}
                    onMouseEnter={e => { e.currentTarget.style.background = "#334155"; e.currentTarget.style.color = "#f8fafc"; }}
                    onMouseLeave={e => { e.currentTarget.style.background = "transparent"; e.currentTarget.style.color = "#94a3b8"; }}
                  >
                    {link.label}
                  </a>
                ))}
              </div>
            )}
          </div>

          {NAV_LINKS.map((link) => (
            <a
              key={link.href}
              href={link.href}
              style={{ color: "#94a3b8", textDecoration: "none", transition: "color 0.15s" }}
              onMouseEnter={e => (e.currentTarget.style.color = "#f8fafc")}
              onMouseLeave={e => (e.currentTarget.style.color = "#94a3b8")}
            >
              {link.label}
            </a>
          ))}
          <a
            href="https://github.com/DuhoKim/NebulaMind"
            target="_blank"
            rel="noopener noreferrer"
            style={{ padding: "6px 12px", background: "transparent", color: "#94a3b8", borderRadius: "4px", textDecoration: "none", fontWeight: 500, fontSize: "0.85rem", border: "1px solid #334155", transition: "all 0.15s" }}
            onMouseEnter={e => { e.currentTarget.style.color = "#f8fafc"; e.currentTarget.style.borderColor = "#64748b"; }}
            onMouseLeave={e => { e.currentTarget.style.color = "#94a3b8"; e.currentTarget.style.borderColor = "#334155"; }}
          >
            ⭐ GitHub
          </a>
                    <a
            href={JOIN_LINK.href}
            style={{ padding: "6px 14px", background: "#6366f1", color: "#f8fafc", borderRadius: "4px", textDecoration: "none", fontWeight: 600, fontSize: "0.85rem", transition: "background 0.15s" }}
            onMouseEnter={e => (e.currentTarget.style.background = "#4f46e5")}
            onMouseLeave={e => (e.currentTarget.style.background = "#6366f1")}
          >
            {JOIN_LINK.label}
          </a>
        </nav>

        {/* Mobile hamburger */}
        <button
          className="md:hidden"
          style={{ color: "#94a3b8", fontSize: "1.25rem", padding: "4px 8px", borderRadius: "4px", border: "none", background: "transparent", cursor: "pointer" }}
          onClick={() => setMenuOpen(!menuOpen)}
          aria-label="Toggle menu"
        >
          {menuOpen ? "✕" : "☰"}
        </button>
      </div>

      {/* Mobile dropdown */}
      {menuOpen && (
        <div className="md:hidden" style={{ borderTop: "1px solid #334155", background: "#1e293b" }}>
          <div className="max-w-5xl mx-auto px-4 py-3 flex flex-col">
            <a href="/" style={{ padding: "10px 8px", color: "#94a3b8", fontSize: "0.875rem", textDecoration: "none" }} onClick={() => setMenuOpen(false)}>
              Home
            </a>
            <a href="/explore" style={{ padding: "10px 8px", color: "#f8fafc", fontWeight: 500, fontSize: "0.875rem", textDecoration: "none" }} onClick={() => setMenuOpen(false)}>
              Explore
            </a>
            <div style={{ paddingLeft: "20px", display: "flex", flexDirection: "column", borderLeft: "2px solid #334155", marginLeft: "8px", margin: "4px 0 4px 8px" }}>
              {EXPLORE_LINKS.map((link) => (
                <a key={link.href} href={link.href} style={{ padding: "8px 0", color: "#64748b", fontSize: "0.875rem", textDecoration: "none" }} onClick={() => setMenuOpen(false)}>
                  {link.label}
                </a>
              ))}
            </div>
            {NAV_LINKS.map((link) => (
              <a key={link.href} href={link.href} style={{ padding: "10px 8px", color: "#94a3b8", fontSize: "0.875rem", textDecoration: "none" }} onClick={() => setMenuOpen(false)}>
                {link.label}
              </a>
            ))}
            <a href={JOIN_LINK.href} style={{ margin: "8px 8px 4px", padding: "8px 14px", background: "#6366f1", color: "#f8fafc", borderRadius: "4px", textDecoration: "none", fontWeight: 600, fontSize: "0.85rem", textAlign: "center" }} onClick={() => setMenuOpen(false)}>
              {JOIN_LINK.label}
            </a>
          </div>
        </div>
      )}
    </header>
  );
}
