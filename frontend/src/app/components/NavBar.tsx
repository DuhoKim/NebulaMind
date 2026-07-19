"use client";

import { useState, useRef, useEffect } from "react";

const NAV_LINKS = [
  { href: "/wiki", label: "Wiki" },
  { href: "/surveys", label: "Surveys" },
  { href: "/ideas", label: "Research" },
  { href: "https://lab.nebulamind.net", label: "Lab" },
  { href: "/news", label: "News" },
  { href: "/council", label: "Council" },
  { href: "/agents", label: "Agents" },
];

const MORE_LINKS = [
  { href: "/explore/chat", label: "Chat" },
  { href: "/calendar", label: "Calendar" },
  { href: "/contribute", label: "Contribute" },
  { href: "/feedback", label: "Feedback" },
];

const JOIN_LINK = { href: "/join", label: "Join" };

export default function NavBar() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [moreOpen, setMoreOpen] = useState(false);
  const [mobileMoreOpen, setMobileMoreOpen] = useState(false);
  const [online, setOnline] = useState<{ human: number; agent: number } | null>(null);
  const [isMobile, setIsMobile] = useState(false);
  const moreTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    const fetchOnline = () => {
      fetch("/api/stats")
        .then((r) => r.json())
        .then((d) => {
          setOnline({ human: d.online_human || 0, agent: d.online_agent || 0 });
        })
        .catch(() => {});
    };
    fetchOnline();
    const t = setInterval(fetchOnline, 30000);
    return () => clearInterval(t);
  }, []);

  useEffect(() => {
    const check = () => setIsMobile(window.innerWidth < 1024);
    check();
    window.addEventListener("resize", check);
    return () => window.removeEventListener("resize", check);
  }, []);

  useEffect(() => {
    if (!isMobile) setMenuOpen(false);
  }, [isMobile]);

  const handleMoreEnter = () => {
    if (moreTimeoutRef.current) clearTimeout(moreTimeoutRef.current);
    setMoreOpen(true);
  };

  const handleMoreLeave = () => {
    moreTimeoutRef.current = setTimeout(() => setMoreOpen(false), 150);
  };

  return (
    <header
      style={{
        borderBottom: "1px solid #334155",
        background: "#0f172a",
        position: "sticky",
        top: 0,
        zIndex: 40,
      }}
    >
      <div
        style={{
          maxWidth: "1024px",
          margin: "0 auto",
          padding: "1rem 1.5rem",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <a href="/" className="no-underline text-inherit">
          <span
            style={{
              fontWeight: 600,
              fontSize: "1.1rem",
              color: "#f8fafc",
              letterSpacing: "-0.025em",
            }}
          >
            NebulaMind
          </span>
        </a>

        {/* Desktop nav */}
        <nav
          style={{
            display: isMobile ? "none" : "flex",
            gap: "1.5rem",
            fontSize: "0.875rem",
            alignItems: "center",
            marginLeft: "2rem",
          }}
        >
          {NAV_LINKS.map((link) => (
            <a
              key={link.href}
              href={link.href}
              style={{ color: "#94a3b8", textDecoration: "none", transition: "color 0.15s" }}
              onMouseEnter={(e) => (e.currentTarget.style.color = "#f8fafc")}
              onMouseLeave={(e) => (e.currentTarget.style.color = "#94a3b8")}
            >
              {link.label}
            </a>
          ))}

          {/* More dropdown */}
          <div
            style={{ position: "relative" }}
            onMouseEnter={handleMoreEnter}
            onMouseLeave={handleMoreLeave}
          >
            <button
              style={{
                color: "#94a3b8",
                fontWeight: 500,
                background: "transparent",
                border: "none",
                display: "flex",
                alignItems: "center",
                gap: "2px",
                transition: "color 0.15s",
                cursor: "pointer",
                fontSize: "0.875rem",
                padding: 0,
              }}
              onMouseEnter={(e) => (e.currentTarget.style.color = "#f8fafc")}
              onMouseLeave={(e) => (e.currentTarget.style.color = "#94a3b8")}
            >
              More
              <span style={{ fontSize: "0.7rem", color: "#64748b", marginLeft: "2px" }}>▾</span>
            </button>
            {moreOpen && (
              <div
                style={{
                  position: "absolute",
                  top: "100%",
                  left: 0,
                  marginTop: "6px",
                  background: "#1e293b",
                  border: "1px solid #334155",
                  borderRadius: "6px",
                  boxShadow: "0 4px 12px rgba(0,0,0,0.3)",
                  padding: "4px 0",
                  minWidth: "140px",
                  zIndex: 50,
                }}
              >
                {MORE_LINKS.map((link) => (
                  <a
                    key={link.href}
                    href={link.href}
                    style={{
                      display: "block",
                      padding: "8px 16px",
                      fontSize: "0.875rem",
                      color: "#94a3b8",
                      textDecoration: "none",
                      transition: "all 0.15s",
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.background = "#334155";
                      e.currentTarget.style.color = "#f8fafc";
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.background = "transparent";
                      e.currentTarget.style.color = "#94a3b8";
                    }}
                  >
                    {link.label}
                  </a>
                ))}
              </div>
            )}
          </div>

          <a
            href={JOIN_LINK.href}
            style={{
              padding: "6px 14px",
              background: "#6366f1",
              color: "#f8fafc",
              borderRadius: "4px",
              textDecoration: "none",
              fontWeight: 600,
              fontSize: "0.85rem",
              transition: "background 0.15s",
            }}
            onMouseEnter={(e) => (e.currentTarget.style.background = "#4f46e5")}
            onMouseLeave={(e) => (e.currentTarget.style.background = "#6366f1")}
          >
            {JOIN_LINK.label}
          </a>

          {online !== null && (
            <span
              style={{
                display: "inline-flex",
                alignItems: "center",
                gap: "5px",
                fontSize: "0.7rem",
                color: "#4ade80",
                background: "rgba(74,222,128,0.08)",
                border: "1px solid rgba(74,222,128,0.2)",
                borderRadius: "999px",
                padding: "3px 8px",
                whiteSpace: "nowrap",
              }}
            >
              <span
                style={{
                  width: "6px",
                  height: "6px",
                  borderRadius: "50%",
                  background: "#22c55e",
                  flexShrink: 0,
                }}
              />
              {online.human + online.agent} ({online.human}👤{online.agent}🤖)
            </span>
          )}
        </nav>

        {/* Mobile hamburger */}
        {isMobile && (
          <button
            style={{
              color: "#94a3b8",
              fontSize: "1.25rem",
              padding: "4px 8px",
              borderRadius: "4px",
              border: "none",
              background: "transparent",
              cursor: "pointer",
            }}
            onClick={() => setMenuOpen(!menuOpen)}
            aria-label="Toggle menu"
          >
            {menuOpen ? "✕" : "☰"}
          </button>
        )}
      </div>

      {/* Mobile dropdown */}
      {isMobile && menuOpen && (
        <div style={{ borderTop: "1px solid #334155", background: "#1e293b" }}>
          <div
            style={{
              maxWidth: "1024px",
              margin: "0 auto",
              padding: "0.75rem 1rem",
              display: "flex",
              flexDirection: "column",
            }}
          >
            {NAV_LINKS.map((link) => (
              <a
                key={link.href}
                href={link.href}
                style={{
                  padding: "10px 8px",
                  color: "#94a3b8",
                  fontSize: "0.875rem",
                  textDecoration: "none",
                }}
                onClick={() => setMenuOpen(false)}
              >
                {link.label}
              </a>
            ))}

            {/* Mobile More collapsible */}
            <button
              onClick={() => setMobileMoreOpen(!mobileMoreOpen)}
              style={{
                padding: "10px 8px",
                color: "#94a3b8",
                fontSize: "0.875rem",
                background: "transparent",
                border: "none",
                textAlign: "left",
                cursor: "pointer",
                display: "flex",
                alignItems: "center",
                gap: "4px",
              }}
            >
              More
              <span style={{ fontSize: "0.65rem", color: "#64748b" }}>
                {mobileMoreOpen ? "▴" : "▾"}
              </span>
            </button>
            {mobileMoreOpen && (
              <div
                style={{
                  paddingLeft: "20px",
                  display: "flex",
                  flexDirection: "column",
                  borderLeft: "2px solid #334155",
                  margin: "4px 0 4px 8px",
                }}
              >
                {MORE_LINKS.map((link) => (
                  <a
                    key={link.href}
                    href={link.href}
                    style={{
                      padding: "8px 0",
                      color: "#64748b",
                      fontSize: "0.875rem",
                      textDecoration: "none",
                    }}
                    onClick={() => setMenuOpen(false)}
                  >
                    {link.label}
                  </a>
                ))}
              </div>
            )}

            <a
              href={JOIN_LINK.href}
              style={{
                margin: "8px 8px 4px",
                padding: "8px 14px",
                background: "#6366f1",
                color: "#f8fafc",
                borderRadius: "4px",
                textDecoration: "none",
                fontWeight: 600,
                fontSize: "0.85rem",
                textAlign: "center",
              }}
              onClick={() => setMenuOpen(false)}
            >
              {JOIN_LINK.label}
            </a>
          </div>
        </div>
      )}
    </header>
  );
}
