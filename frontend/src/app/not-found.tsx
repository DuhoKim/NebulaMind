import Link from "next/link";

export default function NotFound() {
  return (
    <div style={{
      minHeight: "60vh",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      textAlign: "center",
      padding: "2rem",
    }}>
      <div style={{ fontSize: "4rem", marginBottom: "1rem" }}>🌌</div>
      <h1 style={{ fontSize: "2rem", fontWeight: 700, color: "#f8fafc", marginBottom: "0.5rem" }}>
        404 — Page Not Found
      </h1>
      <p style={{ color: "#94a3b8", marginBottom: "2rem", maxWidth: "400px" }}>
        This region of spacetime doesn't exist in our wiki. Maybe the page was moved or the URL is incorrect.
      </p>
      <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap", justifyContent: "center" }}>
        <Link href="/" style={{
          padding: "0.5rem 1.25rem",
          background: "#6366f1",
          color: "#fff",
          borderRadius: "6px",
          textDecoration: "none",
          fontWeight: 600,
        }}>
          Home
        </Link>
        <Link href="/explore" style={{
          padding: "0.5rem 1.25rem",
          background: "transparent",
          color: "#94a3b8",
          border: "1px solid #334155",
          borderRadius: "6px",
          textDecoration: "none",
        }}>
          Explore
        </Link>
      </div>
      <p style={{ marginTop: "2rem", fontSize: "0.8rem", color: "#475569" }}>
        Looking for astronomy content? Try{" "}
        <Link href="/wiki/black-holes" style={{ color: "#6366f1" }}>Black Holes</Link>{" "}
        or{" "}
        <Link href="/wiki/dark-matter" style={{ color: "#6366f1" }}>Dark Matter</Link>.
      </p>
    </div>
  );
}
