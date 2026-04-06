const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export interface WikiPage {
  id: number;
  title: string;
  slug: string;
  content: string;
  is_featured?: boolean;
}

export async function fetchPages(): Promise<WikiPage[]> {
  const res = await fetch(`${API_BASE}/api/pages`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch pages");
  return res.json();
}

export async function fetchPage(slug: string): Promise<WikiPage> {
  const res = await fetch(`${API_BASE}/api/pages/${slug}`, { cache: "no-store" });
  if (!res.ok) throw new Error("Page not found");
  return res.json();
}
