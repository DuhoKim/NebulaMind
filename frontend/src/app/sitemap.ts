import { MetadataRoute } from "next";

const BASE_URL = "https://nebulamind.net";
const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  // Static pages
  const staticPages: MetadataRoute.Sitemap = [
    { url: BASE_URL, lastModified: new Date(), changeFrequency: "daily", priority: 1.0 },
    { url: `${BASE_URL}/explore`, lastModified: new Date(), changeFrequency: "daily", priority: 0.9 },
    { url: `${BASE_URL}/explore/cards`, lastModified: new Date(), changeFrequency: "daily", priority: 0.8 },
    { url: `${BASE_URL}/explore/graph`, lastModified: new Date(), changeFrequency: "weekly", priority: 0.7 },
    { url: `${BASE_URL}/explore/qa`, lastModified: new Date(), changeFrequency: "daily", priority: 0.7 },
    { url: `${BASE_URL}/research`, lastModified: new Date(), changeFrequency: "daily", priority: 0.8 },
    { url: `${BASE_URL}/agents`, lastModified: new Date(), changeFrequency: "weekly", priority: 0.6 },
    { url: `${BASE_URL}/leaderboard`, lastModified: new Date(), changeFrequency: "daily", priority: 0.5 },
    { url: `${BASE_URL}/feedback`, lastModified: new Date(), changeFrequency: "monthly", priority: 0.3 },
  ];

  // Dynamic wiki pages
  try {
    const res = await fetch(`${API_BASE}/api/pages`, { next: { revalidate: 3600 } });
    const pages = await res.json();
    const wikiPages: MetadataRoute.Sitemap = pages.map((p: any) => ({
      url: `${BASE_URL}/wiki/${p.slug}`,
      lastModified: p.updated_at ? new Date(p.updated_at) : new Date(),
      changeFrequency: "daily" as const,
      priority: 0.8,
    }));
    return [...staticPages, ...wikiPages];
  } catch {
    return staticPages;
  }
}
