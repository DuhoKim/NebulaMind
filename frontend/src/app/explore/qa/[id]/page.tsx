import { notFound } from "next/navigation";
import QuestionDetailClient from "./QuestionDetailClient";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

type Props = { params: Promise<{ id: string }> };

async function questionExists(id: string): Promise<boolean> {
  try {
    const res = await fetch(`${API_BASE}/api/qa/${id}`, { next: { revalidate: 3600 } });
    return res.ok;
  } catch {
    return false;
  }
}

export default async function QuestionDetailPage({ params }: Props) {
  const { id } = await params;
  if (!(await questionExists(id))) notFound();
  return <QuestionDetailClient />;
}
