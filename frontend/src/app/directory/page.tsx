import type { Metadata } from "next";
import DirectoryClient from "./DirectoryClient";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export const metadata: Metadata = {
  title: "Directory — NebulaMind",
  description:
    "Browse the NebulaMind astronomy encyclopedia by category: Stars, Black Holes, Galaxies, Cosmology, High Energy, Solar System, and Methods.",
  alternates: { canonical: "https://nebulamind.net/directory" },
};

type Topic = { title: string; slug: string; summary: string };
type Category = { id: string; label: string; emoji: string; topics: Topic[] };

async function fetchDirectory(): Promise<Category[]> {
  try {
    const res = await fetch(`${API_BASE}/api/wiki/directory`, {
      next: { revalidate: 60 },
    });
    if (!res.ok) return [];
    const data = await res.json();
    return Array.isArray(data?.categories) ? data.categories : [];
  } catch {
    return [];
  }
}

export default async function DirectoryPage() {
  const categories = await fetchDirectory();
  const totalTopics = categories.reduce((n, c) => n + c.topics.length, 0);

  return (
    <div>
      <header style={{ marginBottom: "1.5rem" }}>
        <h1 style={{ fontSize: "1.75rem", margin: "0 0 0.25rem", color: "#f8fafc" }}>
          Wiki Directory
        </h1>
        <p style={{ margin: 0, color: "#94a3b8", fontSize: "0.95rem" }}>
          {totalTopics} topics across {categories.length} categories.
        </p>
      </header>

      {categories.length === 0 ? (
        <div
          style={{
            padding: "1rem 1.25rem",
            border: "1px solid #334155",
            borderRadius: "8px",
            color: "#94a3b8",
          }}
        >
          Directory is unavailable right now. Try again in a moment.
        </div>
      ) : (
        <DirectoryClient categories={categories} />
      )}
    </div>
  );
}
