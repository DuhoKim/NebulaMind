"use client";
import { useEffect, useState } from "react";

const CATEGORIES = [
  { id: "astro-ph.GA", label: "🌌 Galaxies" },
  { id: "astro-ph.CO", label: "🔭 Cosmology" },
  { id: "astro-ph.HE", label: "⚡ High Energy" },
  { id: "astro-ph.SR", label: "⭐ Stellar" },
];

interface SubscribeWidgetProps {
  compact?: boolean;
}

export default function SubscribeWidget({ compact = false }: SubscribeWidgetProps) {
  const [email, setEmail] = useState("");
  const [selectedCats, setSelectedCats] = useState<string[]>(["astro-ph.GA", "astro-ph.CO"]);
  const [frequency, setFrequency] = useState<"daily" | "weekly">("daily");
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle");
  const [specialty, setSpecialty] = useState<string>("general");
  const [subCount, setSubCount] = useState<number | null>(null);

  useEffect(() => {
    fetch("/api/subscribers/count")
      .then(r => r.json())
      .then(d => setSubCount(d.count))
      .catch(() => {});
  }, []);

  const toggleCat = (id: string) => {
    setSelectedCats(prev =>
      prev.includes(id) ? prev.filter(c => c !== id) : [...prev, id]
    );
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || selectedCats.length === 0) return;
    setStatus("loading");
    try {
      const res = await fetch("/api/subscribe", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, categories: selectedCats, frequency, specialty }),
      });
      if (res.ok) {
        setStatus("success");
        setSubCount(prev => prev !== null ? prev + 1 : null);
      } else {
        setStatus("error");
      }
    } catch {
      setStatus("error");
    }
  };

  if (compact) {
    return (
      <section style={{ background: "#1e1b4b", borderRadius: "1rem", padding: "1.5rem", color: "white", marginBottom: "2rem" }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", flexWrap: "wrap", gap: "1rem" }}>
          <div>
            <h3 style={{ margin: 0, fontSize: "1.1rem", fontWeight: 700 }}>
              📬 Get the cosmos in your inbox
            </h3>
            <p style={{ margin: "0.25rem 0 0", fontSize: "0.85rem", color: "#a5b4fc" }}>
              Daily arXiv summaries, curated by AI
              {subCount !== null && <span> · <b>{subCount}</b> subscribers</span>}
            </p>
          </div>
          {status === "success" ? (
            <span style={{ color: "#86efac", fontWeight: 600 }}>✅ Subscribed!</span>
          ) : (
            <form onSubmit={handleSubmit} style={{ display: "flex", gap: "0.5rem" }}>
              <input
                type="email"
                placeholder="your@email.com"
                value={email}
                onChange={e => setEmail(e.target.value)}
                required
                style={{ padding: "0.5rem 0.75rem", borderRadius: "0.5rem", border: "none", fontSize: "0.9rem", minWidth: "200px" }}
              />
              <button
                type="submit"
                disabled={status === "loading"}
                style={{ padding: "0.5rem 1rem", background: "#4f46e5", color: "white", border: "none", borderRadius: "0.5rem", cursor: "pointer", fontWeight: 600 }}
              >
                Subscribe
              </button>
            </form>
          )}
        </div>
      </section>
    );
  }

  return (
    <section style={{ background: "#1e1b4b", borderRadius: "1rem", padding: "2rem", color: "white", marginTop: "2rem" }}>
      <h3 style={{ margin: "0 0 0.5rem", fontSize: "1.3rem", fontWeight: 700 }}>
        📬 Get the cosmos in your inbox
      </h3>
      <p style={{ margin: "0 0 0.5rem", color: "#a5b4fc", fontSize: "0.9rem" }}>
        Get notified when papers in your field are cited on NebulaMind · Free · No spam
        {subCount !== null && <span style={{ marginLeft: "0.75rem", background: "#312e81", padding: "0.15rem 0.5rem", borderRadius: "9999px" }}>👥 {subCount} subscribers</span>}
      </p>

      {status === "success" ? (
        <div style={{ textAlign: "center", padding: "2rem", color: "#86efac", fontSize: "1.1rem", fontWeight: 600 }}>
          ✅ Subscribed! Check your inbox for confirmation.
        </div>
      ) : (
        <form onSubmit={handleSubmit}>
          <div style={{ display: "flex", gap: "0.75rem", marginBottom: "1rem", flexWrap: "wrap" }}>
            <input
              type="email"
              placeholder="your@email.com"
              value={email}
              onChange={e => setEmail(e.target.value)}
              required
              style={{ flex: 1, minWidth: "220px", padding: "0.6rem 1rem", borderRadius: "0.5rem", border: "none", fontSize: "0.95rem" }}
            />
            <select
              value={frequency}
              onChange={e => setFrequency(e.target.value as "daily" | "weekly")}
              style={{ padding: "0.6rem 1rem", borderRadius: "0.5rem", border: "none", fontSize: "0.9rem", background: "#312e81", color: "white" }}
            >
              <option value="daily">Daily digest</option>
              <option value="weekly">Weekly digest</option>
            </select>
            <select
              value={specialty}
              onChange={e => setSpecialty(e.target.value)}
              style={{ padding: "0.6rem 1rem", borderRadius: "0.5rem", border: "none", fontSize: "0.9rem", background: "#312e81", color: "white" }}
            >
              <option value="general">🔭 All fields</option>
              <option value="cosmology">🌌 Cosmology</option>
              <option value="stellar">⭐ Stellar Physics</option>
              <option value="exoplanets">🌍 Exoplanets</option>
              <option value="high-energy">⚡ High Energy</option>
              <option value="other">🔬 Other</option>
            </select>
          </div>

          <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap", marginBottom: "1rem" }}>
            {CATEGORIES.map(cat => (
              <button
                key={cat.id}
                type="button"
                onClick={() => toggleCat(cat.id)}
                style={{
                  padding: "0.35rem 0.75rem",
                  border: selectedCats.includes(cat.id) ? "2px solid #818cf8" : "2px solid #4338ca",
                  borderRadius: "9999px",
                  background: selectedCats.includes(cat.id) ? "#4338ca" : "transparent",
                  color: "white",
                  cursor: "pointer",
                  fontSize: "0.85rem",
                  fontWeight: selectedCats.includes(cat.id) ? 600 : 400,
                }}
              >
                {cat.label}
              </button>
            ))}
          </div>

          <button
            type="submit"
            disabled={status === "loading" || selectedCats.length === 0}
            style={{
              padding: "0.6rem 2rem",
              background: "#4f46e5",
              color: "white",
              border: "none",
              borderRadius: "0.5rem",
              cursor: "pointer",
              fontSize: "1rem",
              fontWeight: 600,
              opacity: selectedCats.length === 0 ? 0.5 : 1,
            }}
          >
            {status === "loading" ? "Subscribing..." : "🚀 Subscribe"}
          </button>

          {status === "error" && (
            <p style={{ color: "#fca5a5", marginTop: "0.5rem", fontSize: "0.85rem" }}>
              Something went wrong. Please try again.
            </p>
          )}
        </form>
      )}
    </section>
  );
}
