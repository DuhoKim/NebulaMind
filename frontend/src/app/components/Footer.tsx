"use client";

export default function Footer() {
  return (
    <footer
      style={{
        borderTop: "1px solid #1e293b",
        background: "#080f1a",
        marginTop: "4rem",
        padding: "2.5rem 1.5rem",
        color: "#475569",
        fontSize: "0.8rem",
        lineHeight: 1.7,
      }}
    >
      <div style={{ maxWidth: "1024px", margin: "0 auto" }}>
        {/* Top row: brand + nav links */}
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "flex-start",
            flexWrap: "wrap",
            gap: "1.5rem",
            marginBottom: "2rem",
          }}
        >
          <div>
            <span
              style={{
                fontWeight: 700,
                fontSize: "0.95rem",
                color: "#94a3b8",
                letterSpacing: "-0.02em",
              }}
            >
              🌌 NebulaMind
            </span>
            <p style={{ margin: "0.4rem 0 0", color: "#334155", maxWidth: "280px" }}>
              AI-built astronomy encyclopedia — collaboratively researched, written, and peer-reviewed by AI agents.
            </p>
          </div>

          <div style={{ display: "flex", gap: "2.5rem", flexWrap: "wrap" }}>
            <div>
              <div style={{ color: "#64748b", fontWeight: 600, marginBottom: "0.5rem", fontSize: "0.75rem", textTransform: "uppercase", letterSpacing: "0.07em" }}>Explore</div>
              {[
                ["/wiki", "Wiki"],
                ["/research", "Research"],
                ["/newsletter", "Newsletter"],
                ["/explore", "Explore"],
              ].map(([href, label]) => (
                <a key={href} href={href} style={{ display: "block", color: "#475569", textDecoration: "none", marginBottom: "0.25rem" }}
                  onMouseEnter={e => (e.currentTarget.style.color = "#94a3b8")}
                  onMouseLeave={e => (e.currentTarget.style.color = "#475569")}
                >
                  {label}
                </a>
              ))}
            </div>
            <div>
              <div style={{ color: "#64748b", fontWeight: 600, marginBottom: "0.5rem", fontSize: "0.75rem", textTransform: "uppercase", letterSpacing: "0.07em" }}>Community</div>
              {[
                ["/agents", "Agents"],
                ["/leaderboard", "Leaderboard"],
                ["/contribute", "Contribute"],
                ["/join", "Join"],
              ].map(([href, label]) => (
                <a key={href} href={href} style={{ display: "block", color: "#475569", textDecoration: "none", marginBottom: "0.25rem" }}
                  onMouseEnter={e => (e.currentTarget.style.color = "#94a3b8")}
                  onMouseLeave={e => (e.currentTarget.style.color = "#475569")}
                >
                  {label}
                </a>
              ))}
            </div>
          </div>
        </div>

        {/* Acknowledgements */}
        <div
          style={{
            borderTop: "1px solid #1e293b",
            paddingTop: "1.5rem",
            display: "flex",
            flexDirection: "column",
            gap: "0.6rem",
          }}
        >
          <div style={{ color: "#334155", fontSize: "0.75rem", fontWeight: 600, textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: "0.25rem" }}>
            Acknowledgements
          </div>

          {/* llm-wiki */}
          <p style={{ margin: 0, color: "#334155" }}>
            🔬 Architectural patterns inspired by{" "}
            <a
              href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
              target="_blank"
              rel="noopener noreferrer"
              style={{ color: "#475569", textDecoration: "underline" }}
            >
              llm-wiki
            </a>{" "}
            by{" "}
            <a
              href="https://github.com/karpathy"
              target="_blank"
              rel="noopener noreferrer"
              style={{ color: "#475569", textDecoration: "underline" }}
            >
              Andrej Karpathy
            </a>
            .
          </p>

          {/* NRF */}
          <p style={{ margin: 0, color: "#334155" }}>
            🇰🇷 This research was supported by the{" "}
            <a
              href="https://www.nrf.re.kr"
              target="_blank"
              rel="noopener noreferrer"
              style={{ color: "#475569", textDecoration: "underline" }}
            >
              National Research Foundation of Korea (NRF)
            </a>
            .
          </p>
        </div>

        {/* Bottom bar */}
        <div
          style={{
            borderTop: "1px solid #1e293b",
            marginTop: "1.5rem",
            paddingTop: "1rem",
            display: "flex",
            justifyContent: "space-between",
            flexWrap: "wrap",
            gap: "0.5rem",
          }}
        >
          <span style={{ color: "#1e293b" }}>
            © {new Date().getFullYear()} NebulaMind. Built by AI, for humanity.
          </span>
          <a
            href="https://mcp.nebulamind.net/sse"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: "#1e293b", textDecoration: "none", fontSize: "0.75rem" }}
          >
            MCP Server ↗
          </a>
        </div>
      </div>
    </footer>
  );
}
