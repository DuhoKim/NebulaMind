import { notFound } from "next/navigation";
import WikiSourcesClient from "./WikiSourcesClient";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

type Props = { params: Promise<{ slug: string }> };

async function pageExists(slug: string): Promise<boolean> {
  try {
    const res = await fetch(`${API_BASE}/api/pages/${slug}`, { next: { revalidate: 3600 } });
    return res.ok;
  } catch {
    return false;
  }
}

export default async function WikiSourcesPage({ params }: Props) {
  const { slug } = await params;
  if (!(await pageExists(slug))) notFound();
  return <WikiSourcesClient />;
}
