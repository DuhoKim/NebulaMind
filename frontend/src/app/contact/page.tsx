export const metadata = {
  title: "Contact — NebulaMind",
  description: "Get in touch with the NebulaMind team.",
};

export default function ContactPage() {
  return (
    <main style={{ minHeight: "70vh", padding: "4rem 1.5rem", maxWidth: "640px", margin: "0 auto" }}>
      <h1 style={{ fontSize: "2rem", fontWeight: 700, color: "#e2e8f0", marginBottom: "0.5rem" }}>
        Contact
      </h1>
      <p style={{ color: "#64748b", marginBottom: "2.5rem", lineHeight: 1.7 }}>
        Have a question, idea, or want to collaborate? Reach out — we would love to hear from you.
      </p>

      <div style={{
        background: "#0f1b2d",
        border: "1px solid #1e293b",
        borderRadius: "12px",
        padding: "2rem",
        display: "flex",
        flexDirection: "column",
        gap: "1rem",
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: "0.75rem" }}>
          <span style={{ fontSize: "1.5rem" }}>✉️</span>
          <div>
            <div style={{ color: "#94a3b8", fontSize: "0.75rem", fontWeight: 600, textTransform: "uppercase", letterSpacing: "0.07em", marginBottom: "0.25rem" }}>
              Email
            </div>
            <a
              href="mailto:hwao@nebulamind.net"
              style={{ color: "#7dd3fc", textDecoration: "none", fontSize: "1rem", fontWeight: 500 }}
            >
              hwao@nebulamind.net
            </a>
          </div>
        </div>

        <p style={{ color: "#475569", fontSize: "0.85rem", margin: 0, lineHeight: 1.7, borderTop: "1px solid #1e293b", paddingTop: "1rem" }}>
          NebulaMind is an open AI-powered astronomy encyclopedia. We welcome researchers, educators, developers, and curious minds.
        </p>
      </div>
    </main>
  );
}
